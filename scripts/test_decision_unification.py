"""One decision format across subjects, with no retired routes or unchecked variants."""
import json
from pathlib import Path
import re
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'evals'))
from document_contracts import digest, load_contracts, validate
import audit_examples
from validate_document import prepare, state_for


class DecisionUnificationTests(unittest.TestCase):
    def setUp(self):
        self.catalog = json.loads((ROOT / 'evals/catalog.json').read_text())
        self.entry = next(item for item in self.catalog['output_kinds'] if item['id'] == 'decision')

    def test_one_catalog_kind_owns_the_decision_examples(self):
        self.assertNotIn('adr', {item['id'] for item in self.catalog['output_kinds']})
        self.assertNotIn('ddr', {item['id'] for item in self.catalog['output_kinds']})
        self.assertEqual(self.entry['reference'], 'references/decision_record.md')
        self.assertEqual(len(self.entry['examples']), 3)
        for name in self.entry['examples']:
            self.assertEqual(audit_examples.kind_for(Path(name).name), 'decision')
            self.assertEqual(audit_examples.entry_for(Path(name).name)['reference'], self.entry['reference'])

    def test_retired_document_kinds_are_rejected_instead_of_aliased(self):
        for kind in ('adr', 'ddr', 'ADR', 'DDR'):
            with self.subTest(kind=kind), self.assertRaisesRegex(ValueError, 'Unsupported document type'):
                validate('# A decision\n', kind)
        self.assertNotIn('adr', load_contracts()['documents'])
        self.assertNotIn('ddr', load_contracts()['documents'])

    def test_context_cases_cover_all_four_operations_under_one_kind(self):
        coverage = json.loads((ROOT / 'evals/coverage.json').read_text())['output_kinds']
        self.assertNotIn('adr', coverage)
        self.assertNotIn('ddr', coverage)
        cases = {row['id']: row for row in (json.loads(line) for path in (ROOT / 'evals/cases').glob('*.jsonl') for line in path.read_text().splitlines() if line.strip())}
        for operation in ('create', 'edit', 'review', 'rewrite'):
            expected = {f'decision-{operation}', f'decision-architecture-{operation}', f'decision-component-design-{operation}'}
            self.assertEqual(set(coverage['decision'][operation]), expected)
            for identifier in expected:
                self.assertEqual(cases[identifier]['kind'], 'decision')
                self.assertIn(self.entry['reference'], cases[identifier]['references'])
                self.assertTrue((ROOT / 'evals' / cases[identifier]['fixture']).is_file())

    def test_every_context_uses_the_same_required_structure(self):
        for name in self.entry['examples']:
            with self.subTest(example=name):
                text = (ROOT / name).read_text()
                self.assertTrue(validate(text, 'decision')['passed'])
                self.assertFalse(validate(text.replace('## Options considered', 'Options considered', 1), 'decision')['passed'])
                self.assertFalse(validate(text.replace('### Option B:', '#### Option B:', 1), 'decision')['passed'])

    def test_example_audit_cannot_waive_a_missing_context_section(self):
        paths = [ROOT / name for name in self.entry['examples']]
        packet = audit_examples.make_packet(paths)
        # Synthetic favorable grades exercise the checker, not writing quality.
        response = {'packet_sha256': packet['packet_sha256'], 'reviewer': {'kind': 'current_host_self_review', 'identity': 'Unit control', 'model': None, 'method': 'Authored checker control.'}, 'results': [{'id': path.stem, 'scores': [3] * 7, 'critical_failures': [], 'reasons': ['Synthetic control, not semantic evidence.']} for path in paths]}
        self.assertTrue(audit_examples.assess_packet(packet, response)['accepted'])
        packet['documents'][1]['content'] = packet['documents'][1]['content'].replace('## Options considered', 'Options considered', 1)
        packet['packet_sha256'] = digest({key: value for key, value in packet.items() if key != 'packet_sha256'})
        response['packet_sha256'] = packet['packet_sha256']
        result = audit_examples.assess_packet(packet, response, verify=False)
        self.assertFalse(result['accepted'])
        self.assertTrue(any('Options considered' in reason for row in result['results'] for reason in row['critical_failures']))

    def test_option_labels_are_unique_and_code_examples_are_not_choices(self):
        text = (ROOT / 'examples/decision_record_architecture.md').read_text()
        self.assertFalse(validate(text.replace('### Option C:', '### Option A:', 1), 'decision')['passed'])
        fenced = text + '\n```md\n### Option A: Literal example\n## Recommended option (Z)\n```\n'
        self.assertTrue(validate(fenced, 'decision')['passed'])

    def test_removed_guides_and_names_are_absent_from_active_routing(self):
        for name in ('architecture_decision_record.md', 'design_decision_record.md'):
            self.assertFalse((ROOT / 'references' / name).exists())
            self.assertFalse((ROOT / 'examples' / name).exists())
        for name in ('SKILL.md', 'evals/catalog.json', 'evals/fixtures/routing.md', 'references/decision_record.md', 'references/high_level_document.md', 'references/low_level_design.md', 'references/issue.md'):
            text = (ROOT / name).read_text()
            self.assertIsNone(re.search(r'\b(?:ADRs?|DDRs?)\b', text), name)
            self.assertNotIn('references/architecture_decision_record.md', text)
            self.assertNotIn('references/design_decision_record.md', text)

    def test_delivery_loads_only_the_shared_decision_and_writing_guides(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            request = {'kind': 'decision', 'sources': [{'id': 'facts', 'text': 'A choice between two approaches is still pending.'}], 'destination': 'decision.md'}
            (root / 'request.json').write_text(json.dumps(request))
            prepare(root / 'request.json', root / 'session')
            state = state_for(root / 'session')
            self.assertEqual(set(state['frozen']['guidance']), {'references/decision_record.md', 'references/writing_style.md'})
