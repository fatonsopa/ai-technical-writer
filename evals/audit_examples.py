#!/usr/bin/env python3
"""Review authored examples using native-host packets or a bounded optional CLI."""
import argparse
import json
from pathlib import Path
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
sys.path.insert(0, str(ROOT / 'evals'))
from document_contracts import digest, validate
from repository_files import inventory
from validate_document import save
from validate_skill import blocks
from grades import assess_output, validate_results


def entry_for(filename):
    catalog = json.loads((ROOT / 'evals/catalog.json').read_text())
    return next(item for item in catalog['output_kinds'] if item['reference'] == 'references/' + filename or 'examples/' + filename in item.get('examples', []))


def kind_for(filename):
    return 'issue_feature' if filename == 'issue.md' else entry_for(filename)['id']


def make_packet(paths):
    examples = ROOT / 'examples'
    context = {name: (examples / name).read_text() for name in ('spec_driven_development.md', 'test_specification.md', 'test_status_report.md', 'test_completion_report.md', 'incident_report.md')}
    value = {'schema_version': 1, 'artifact_manifest': inventory(ROOT, 'runtime'),
             'context': context, 'writing_style': (ROOT / 'references/writing_style.md').read_text(),
             'basis': 'Teaching documents describe an illustrative initiative. Their scenario statuses and results are not claims that this audit executed the application. Check internal consistency, requirements, arithmetic, depth and language. Do not require source-versus-invention labels within these authorized teaching examples.',
             'documents': [{'id': path.stem, 'kind': kind_for(path.name), 'content': path.read_text(), 'guide': (ROOT / entry_for(path.name)['reference']).read_text()} for path in paths],
             'instructions': 'Review every document against its own guide, writing style and shared context. Return packet_sha256, reviewer {kind, identity, model, method} and results [{id, scores (seven integers 0–3: grounding, preservation, completeness, usefulness, language, scope, traceability), critical_failures, reasons}]. Identify self-review honestly. Require useful content, preserve scenario evidence boundaries and do not claim real application execution.'}
    value['packet_sha256'] = digest(value)
    return value


def assess_packet(packet, response, verify=True):
    frozen = {key: value for key, value in packet.items() if key != 'packet_sha256'}
    if digest(frozen) != packet['packet_sha256'] or response.get('packet_sha256') != packet['packet_sha256']:
        raise ValueError('The response does not match the frozen authored-example packet.')
    if verify and inventory(ROOT, 'runtime') != packet['artifact_manifest']:
        raise ValueError('Example, guide or evaluator changed; version the audit before continuing.')
    reviewer = response.get('reviewer', {})
    if reviewer.get('kind') not in {'current_host_self_review', 'current_host_review', 'independent_model', 'human'} or not all(isinstance(reviewer.get(key), str) and reviewer[key].strip() for key in ('identity', 'method')):
        raise ValueError('Identify the actual example reviewer and method.')
    results = validate_results(response.get('results'), [doc['id'] for doc in packet['documents']])
    assessed = []
    for item in results:
        doc = next(doc for doc in packet['documents'] if doc['id'] == item['id'])
        value = assess_output(doc['content'], {'kind': doc['kind'], 'operation': 'review' if doc['id'] == 'agents_and_skills' else 'create'}, item)
        if doc['id'] == 'agents_and_skills':
            snippets = [body for tag, body in blocks(doc['content'])[0] if tag == 'md']
            if len(snippets) != 3:
                value['critical_failures'].append('The configuration collection needs three complete artifacts.')
            else:
                for kind, text in zip(('agent', 'skill', 'output_style'), snippets):
                    value['critical_failures'].extend(validate(text, kind)['findings'])
            value['passed'] = value['passed'] and not value['critical_failures']
        assessed.append(value)
    return {'status': 'completed', 'accepted': all(item['passed'] for item in assessed), 'reviewer': reviewer,
            'packet_sha256': packet['packet_sha256'], 'results': assessed,
            'input_kind': 'Authored teaching examples; this is review, not independent document generation or product testing.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path)
    parser.add_argument('--document', action='append')
    parser.add_argument('--provider', choices=['host', 'codex'], default='host')
    parser.add_argument('--model')
    parser.add_argument('--max-calls', type=int)
    parser.add_argument('--max-seconds', type=int)
    parser.add_argument('--packet', type=Path, help='Assess a previously issued packet with --response.')
    parser.add_argument('--response', type=Path)
    args = parser.parse_args()
    try:
        if args.packet:
            if not args.response or not args.out:
                raise ValueError('Packet assessment needs --response and a new --out file.')
            if args.out.exists():
                raise ValueError('Preserve existing assessment results.')
            record = assess_packet(json.loads(args.packet.read_text()), json.loads(args.response.read_text()))
            save(args.out, record)
            print(json.dumps(record, indent=2))
            return 0 if record['accepted'] else 1
        if not args.out or args.out.exists() or args.out.resolve().is_relative_to(ROOT):
            raise ValueError('Choose a new output directory outside the skill.')
        paths = sorted((ROOT / 'examples').glob('*.md'))
        if args.document:
            names = set(args.document)
            if names - {path.name for path in paths}:
                raise ValueError('Unknown example filename.')
            paths = [path for path in paths if path.name in names]
        if args.provider == 'codex':
            if not args.model:
                raise ValueError('Select the exact available Codex model.')
            import run as runner
            runner.LIVE_BUDGET = runner.evaluation.CallBudget(args.max_calls, args.max_seconds)
        args.out.mkdir(parents=True, mode=0o700)
        failed = False
        for start in range(0, len(paths), 6):
            folder = args.out / f'batch-{start:02}'
            packet = make_packet(paths[start:start + 6])
            save(folder / 'packet.json', packet)
            if args.provider == 'host':
                print(json.dumps({'status': 'awaiting_current_host_review', 'packet': str(folder / 'packet.json'), 'documents': [doc['id'] for doc in packet['documents']]}))
                continue
            with tempfile.TemporaryDirectory(prefix='writer-example-review-') as directory:
                work = Path(directory)
                save(work / 'packet.json', packet)
                result = runner.invoke(work, folder / 'model', 'Read packet.json and return its requested results. Use only the local packet; no network, writing or project execution.', args.model, grading=True)
            if result['status'] != 'completed':
                save(folder / 'record.json', result)
                failed = True
                continue
            response = {'packet_sha256': packet['packet_sha256'], 'reviewer': {'kind': 'independent_model', 'identity': 'Codex CLI grading context', 'model': args.model, 'method': 'Separate context reviewing authored examples against a captured packet.'}, 'results': result['results']}
            record = assess_packet(packet, response)
            save(folder / 'record.json', record)
            failed = failed or not record['accepted']
            print(json.dumps({'batch': folder.name, 'accepted': record['accepted']}))
        return 1 if failed else 0
    except (OSError, ValueError, KeyError, TypeError, StopIteration) as error:
        print(json.dumps({'error': str(error)}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    sys.exit(main())
