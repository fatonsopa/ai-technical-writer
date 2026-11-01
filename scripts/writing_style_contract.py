"""Require the shared writing guide and a source-bound review of authored text."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

from document_contracts import digest
from visual_contracts import diagram_blocks, MERMAID_TYPES

REFERENCE = 'references/writing_style.md'
SCOPE = 'Apply Writing Style (WS) to every authored text surface before sending or accepting it: documents, titles, headings, tables, diagram text and metadata, examples, templates, questions and options, audit findings, recommendations, comments and delivery messages. No format, length or workflow stage skips the guide. Preserve exact literals under the guide’s preservation rules.'


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
    return review['passed']
