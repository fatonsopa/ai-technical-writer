"""Require the shared writing guide and a source-bound review of authored text."""
from pathlib import Path
import argparse
import json
import re
import xml.etree.ElementTree as ET

from document_contracts import digest
from visual_contracts import diagram_blocks, MERMAID_TYPES

REFERENCE = 'references/writing_style.md'
SCOPE = 'Apply Writing Style (WS) to every authored text surface before sending or accepting it: documents, titles, headings, tables, diagram text and metadata, examples, templates, questions and options, audit findings, recommendations, comments and delivery messages. No format, length or workflow stage skips the guide. Preserve exact literals under the guide’s preservation rules.'


ROOT = Path(__file__).resolve().parents[1]
# These abbreviations are sufficiently specific in this skill's documentation domain.
# Ambiguous tokens such as AI, IP and TS still require contextual semantic review.
UNAMBIGUOUS = {'PRD', 'SDD', 'HLD', 'LLD', 'TSR', 'TCR', 'README', 'WS', 'VG'}


def document_labels(root=ROOT):
    text = (Path(root) / 'SKILL.md').read_text()
    labels = {}
    for name, acronym in re.findall(r'\[([^\]\n]+?) \(([A-Z][A-Z0-9]+)\)\]\(references/', text):
        if acronym in labels and labels[acronym] != name:
            raise ValueError('Conflicting approved document labels: ' + acronym)
        labels[acronym] = name
    if not labels:
        raise ValueError('The skill has no approved document labels.')
    return labels


def document_name_findings(text, labels=None):
    labels = document_labels() if labels is None else labels
    def mask(match):
        return re.sub(r'[^\n]', ' ', match.group())
    visible = re.sub(r'```.*?```|~~~.*?~~~', mask, text, flags=re.S)
    visible = re.sub(r'`[^`\n]*`', mask, visible)
    visible = re.sub(r'\[[^\]\n]*\]\(https?://[^)\n]*\)', mask, visible)
    visible = re.sub(r'https?://[^\s)>]+|[\w./-]+\.(?:md|json|py|mmd|svg|png|sql|yaml|yml)\b', mask, visible)
    visible = re.sub(r'"[^"\n]*"|“[^”\n]*”|^\s*>[^\n]*', mask, visible, flags=re.M)
    visible = re.sub(r'\bSDD(?=\s+(?:method|approach)\b)', mask, visible)
    for acronym, name in labels.items():
        visible = re.sub(re.escape(name) + r'\s+\(' + re.escape(acronym) + r'\)', mask, visible)
    findings = []
    for acronym, name in labels.items():
        # Only exact multiword names and unambiguous abbreviations are mechanical
        # failures. Common words and ambiguous domain abbreviations need AI review.
        patterns = [re.escape(name)] if len(name.split()) > 1 else []
        if acronym in UNAMBIGUOUS:
            patterns.append(re.escape(acronym))
        if not patterns:
            continue
        matcher = re.compile(r'(?<!\w)(?:' + '|'.join(patterns) + r')(?!\w)')
        for match in matcher.finditer(visible):
            findings.append({'line': visible.count('\n', 0, match.start()) + 1,
                             'text': match.group(), 'expected': name + ' (' + acronym + ')'})
    return sorted(findings, key=lambda row: (row['line'], row['text']))


ABSENCE_PATTERNS = [
    r"\bno [^.!?;\n]{0,140}\b(?:has|have|had) been (?:set|assigned|defined|established)\b",
    r"\bno (?:test )?results (?:are|were) available\b",
    r"\b(?:none of|no) (?:these |the |those |any )?(?:acceptance |automated |implementation |project )?(?:tests?|checks?|results?)[^.!?;\n]{0,60}\b(?:passed|run|executed|recorded)\b",
    r"\bnone exist(?:s)?(?: yet)?\b",
    r"\bno [^.!?;\n]{0,100}\b(?:written|identified|exists?|exist)\b",
    r"\b(?:hasn't|has not|haven't|have not) been implemented\b",
    r"\bunimplemented (?:proposal|change|design|feature)\b",
    r"\bnobody [^.!?\n]{0,70}\binspected\b",
]


def unsupported_absence_findings(text, sources=()):
    def mask(match):
        return re.sub(r'[^\n]', ' ', match.group())
    visible = re.sub(r'```.*?```|~~~.*?~~~', mask, text, flags=re.S)
    visible = re.sub(r'`[^`\n]*`|"[^"\n]*"|“[^”\n]*”|^\s*>[^\n]*', mask, visible, flags=re.M)
    evidence = [' '.join(str(value).casefold().split()) for value in sources]
    findings = []
    for pattern in ABSENCE_PATTERNS:
        for match in re.finditer(pattern, visible, re.I):
            claim = ' '.join(match.group().casefold().split())
            prefix = visible[max(visible.rfind('\n', 0, match.start()), visible.rfind('.', 0, match.start())) + 1:match.start()]
            if re.search(r'\b(?:whether|if|unknown|not known|does not establish|does not say)\b', prefix, re.I):
                continue
            if not any(claim in source for source in evidence):
                findings.append({'line': visible.count('\n', 0, match.start()) + 1, 'text': match.group(),
                                 'kind': 'unsupported_absence', 'reason': 'Supply explicit source evidence for absence, quote the source accurately, or preserve what is unknown/incomplete. Incomplete work does not establish zero work or zero passing checks; unavailable evidence does not establish absence.'})
    return findings


def load_guide(root):
    root = Path(root).resolve()
    path = (root / REFERENCE).resolve()
    if not path.is_relative_to(root):
        raise ValueError('The mandatory writing guide must belong to the skill.')
    content = path.read_text()
    if not content.strip():
        raise ValueError('The mandatory writing guide is empty.')
    return content


def required_references(references):
    return list(dict.fromkeys([REFERENCE, *references]))


def guide_packet(guide, include_text=True):
    if not isinstance(guide, str) or not guide.strip():
        raise ValueError('Every output needs the captured Writing Style (WS) guide.')
    result = {'guide': REFERENCE, 'guide_sha256': digest(guide.encode()), 'scope': SCOPE}
    if include_text:
        result['text'] = guide
    return result


def svg_text(content):
    try:
        root = ET.fromstring(content)
    except ET.ParseError as error:
        raise ValueError('Diagram text is unavailable for writing-style review: ' + str(error)) from error
    values = []
    def visit(node):
        tag = node.tag.rsplit('}', 1)[-1]
        if tag in {'style', 'script', 'defs'}:
            return
        if tag in {'text', 'title', 'desc', 'foreignObject'}:
            value = ' '.join(''.join(node.itertext()).split())
            if value:
                values.append(value)
            return
        for child in node:
            visit(child)
    visit(root)
    return '\n'.join(values)


def packet(content, guide, sources=(), destination=None):
    if not isinstance(guide, str) or not guide.strip():
        raise ValueError('Every output needs the captured Writing Style (WS) guide.')
    source_texts = [row['text'] for row in sources if isinstance(row, dict) and isinstance(row.get('text'), str) and not str(row.get('path', '')).lower().endswith('.svg') and not row['text'].lstrip().startswith('<svg')]
    absence_evidence = list(dict.fromkeys(match.group() for source in source_texts for pattern in ABSENCE_PATTERNS for match in re.finditer(pattern, source, re.I)))
    targets = [{'id': 'output', 'sha256': digest(content.encode()), 'text': content}]
    for index, block in enumerate(diagram_blocks(content, languages=('mermaid', 'text'))[0]):
        if re.search(r'(?m)^\s*(?:' + '|'.join(map(re.escape, MERMAID_TYPES)) + r')\b', block['body']):
            targets.append({'id': 'diagram-source-' + str(index + 1), 'sha256': digest(block['body'].encode()), 'text': block['body']})
    if destination:
        captured = {str(Path(row['path']).resolve()): row for row in sources if 'path' in row}
        lines = content.splitlines()
        languages = tuple(re.findall(r'(?m)^\s{0,3}(?:`{3,}|~{3,})([^\n]*)$', content))
        for block in diagram_blocks(content, languages=languages)[0]:
            lines[block['line'] - 1:block['end_line']] = [''] * (block['end_line'] - block['line'] + 1)
        visible = '\n'.join(lines)
        image_matches = re.findall(r'!\[[^\]\n]*\]\((?:<([^>\n]+\.svg)>|([^)]+\.svg))\)', visible, re.I)
        images = dict.fromkeys(first or second for first, second in image_matches)
        for name in images:
            path = str((Path(destination).parent / name).resolve())
            if path not in captured:
                raise ValueError('Capture every linked SVG so its text can receive writing-style review: ' + name)
            raw = captured[path]['text']
            targets.append({'id': 'diagram:' + name, 'sha256': digest(raw.encode()), 'text': svg_text(raw)})
    target_hash = digest([{'id': row['id'], 'sha256': row['sha256']} for row in targets])
    return {'guide': REFERENCE, 'guide_sha256': digest(guide.encode()), 'targets_sha256': target_hash, 'scope': SCOPE, 'targets': targets,
            'source_claim_evidence': absence_evidence,
            'unsupported_absence_findings': {row['id']: unsupported_absence_findings(row['text'], source_texts) for row in targets if not row['id'].startswith('diagram-source-')},
            'document_labels': {a: n + ' (' + a + ')' for a, n in document_labels().items()},
            'document_name_findings': {row['id']: document_name_findings(row['text']) for row in targets if not row['id'].startswith('diagram-source-')},
            'review_fields': {'guide_sha256': 'Copy this guide hash.', 'output_sha256': 'Copy the output target hash.', 'targets_sha256': 'Copy the complete target manifest hash.', 'reviewed_targets': 'List every target ID exactly once.', 'passed': 'Boolean judgment of actual text against the guide.', 'rationale': 'Explain the actual wording/context/literal checks and corrections; a receipt alone does not prove quality.'}}


def check_review(contract, review):
    if not isinstance(review, dict) or set(review) != {'guide_sha256', 'output_sha256', 'targets_sha256', 'reviewed_targets', 'passed', 'rationale'}:
        raise ValueError('A writing-style review needs guide/output/target hashes, reviewed_targets, passed and rationale.')
    if review['guide_sha256'] != contract['guide_sha256'] or review['output_sha256'] != contract['targets'][0]['sha256'] or review['targets_sha256'] != contract['targets_sha256']:
        raise ValueError('Writing-style review is stale or belongs to another guide/output/diagram.')
    targets = review['reviewed_targets']
    expected = {row['id'] for row in contract['targets']}
    if not isinstance(targets, list) or any(not isinstance(value, str) for value in targets) or len(targets) != len(set(targets)) or set(targets) != expected:
        raise ValueError('Writing-style review must cover every text target exactly once, including diagrams.')
    if type(review['passed']) is not bool or not isinstance(review['rationale'], str) or not review['rationale'].strip():
        raise ValueError('Writing-style review needs a boolean result and a substantive rationale.')
    conventions_passed = not any(document_name_findings(row['text']) for row in contract['targets'] if not row['id'].startswith('diagram-source-'))
    evidence_passed = not any(unsupported_absence_findings(row['text'], contract.get('source_claim_evidence', ())) for row in contract['targets'] if not row['id'].startswith('diagram-source-'))
    return review['passed'] and conventions_passed and evidence_passed



def main(argv=None):
    parser = argparse.ArgumentParser(description='Check explicit document-name conventions; meaning still needs review.')
    sub = parser.add_subparsers(dest='operation', required=True)
    sub.add_parser('names')
    check = sub.add_parser('check')
    check.add_argument('files', nargs='+', type=Path)
    check.add_argument('--source', action='append', type=Path, default=[], help='Captured source text supporting factual absence claims.')
    args = parser.parse_args(argv)
    if args.operation == 'names':
        print(json.dumps({a: n + ' (' + a + ')' for a, n in document_labels().items()}, indent=2))
        return 0
    records = []
    sources = [path.read_text() for path in args.source]
    for path in args.files:
        text = svg_text(path.read_text()) if path.suffix.lower() == '.svg' else path.read_text()
        records.extend({'file': str(path), **finding} for finding in [*document_name_findings(text), *unsupported_absence_findings(text, sources)])
    print(json.dumps({'passed': not records, 'findings': records, 'limits': 'Checks high-confidence names and selected unsupported absence claims. Semantic equivalence, source authority, ambiguous terms and actual public-message delivery still need review.'}, indent=2))
    return int(bool(records))


if __name__ == '__main__':
    raise SystemExit(main())
