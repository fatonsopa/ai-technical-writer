"""Actual new-format acceptance/rejection controls; no model-quality claim."""
from copy import deepcopy
import json
from pathlib import Path
import re
import unittest
from document_contracts import validate, load_contracts
from test_document_contracts import sample
import validate_skill

ROOT = Path(__file__).resolve().parents[1]
KINDS = ('threat_model', 'interface_contract', 'service_objectives')

class EngineeringDocumentsTests(unittest.TestCase):
    def test_complete_examples_pass_the_actual_new_contracts(self):
        for kind in KINDS:
            with self.subTest(kind=kind):
                result = validate((ROOT / 'examples' / (kind + '.md')).read_text(), kind)
                self.assertTrue(result['passed'], result['findings'])

    def test_each_required_section_is_enforced_in_authored_examples(self):
        for kind in KINDS:
            text = (ROOT / 'examples' / (kind + '.md')).read_text()
            for section in load_contracts()['documents'][kind]['sections']:
                heading = '## ' + section['id']
                for changed in (text.replace(heading, section['id'], 1), text.replace(heading, '#' + heading, 1)):
                    with self.subTest(kind=kind, section=heading):
                        self.assertFalse(validate(changed, kind)['passed'])

    def test_empty_duplicate_and_fenced_sections_do_not_pass(self):
        for kind in KINDS:
            text = sample(kind)
            empty = text.replace('A source-supported explanation for this section.', 'TODO', 1)
            self.assertFalse(validate(empty, kind)['passed'])
            rule = load_contracts()['documents'][kind]['sections'][0]['id']
            self.assertFalse(validate(text + '\n## ' + rule + '\nRepeated.\n', kind)['passed'])
            self.assertFalse(validate('# Sample\n```md\n' + text + '\n```', kind)['passed'])

    def test_narrow_operations_keep_their_scope(self):
        for kind in KINDS:
            self.assertTrue(validate('A located finding with supporting source.', kind, 'review')['passed'])
            self.assertTrue(validate('# Corrected topic', kind, 'edit', 'title')['passed'])
            self.assertTrue(validate('Corrected excerpt.', kind, 'edit', 'excerpt')['passed'])
            self.assertFalse(validate('A complete document without required sections.', kind)['passed'])

    def test_exact_literals_and_requirement_ids_remain_enforced(self):
        context = {'required_literals': ['0042', '28-day'], 'requirement_ids': ['FJ-01']}
        for kind in KINDS:
            self.assertFalse(validate(sample(kind) + '\n42 28 days FJ-010', kind, context=context)['passed'])
            self.assertTrue(validate(sample(kind) + '\n0042 28-day FJ-01', kind, context=context)['passed'])

    def test_unknown_blocking_decisions_cannot_be_claimed_ready(self):
        record = {'status': 'ready', 'source_ids': ['facts'], 'decisions': [{'id': 'OPEN-01', 'question': 'Who approved the target?', 'status': 'open', 'blocking': True, 'answer': '', 'source_ids': []}]}
        for kind in KINDS:
            self.assertFalse(validate(sample(kind), kind, context={'discovery': record})['passed'])
            draft = deepcopy(record); draft['status'] = 'draft'
            self.assertTrue(validate('Status: Draft\n' + sample(kind) + '\nOPEN-01 remains unresolved.', kind, context={'discovery': draft})['passed'])

    def test_catalog_operation_cases_and_fixtures_are_resolvable(self):
        cases = [json.loads(line) for line in (ROOT / 'evals/cases/engineering_documents.jsonl').read_text().splitlines()]
        expected = {(kind, operation) for kind in KINDS for operation in ('create', 'edit', 'review', 'rewrite')}
        self.assertEqual({(c['kind'], c['operation']) for c in cases}, expected)
        self.assertEqual(len(cases), 12)
        for case in cases:
            self.assertTrue((ROOT / 'evals' / case['fixture']).is_file())
            self.assertTrue(all((ROOT / ref).is_file() for ref in case['references']))
            self.assertTrue(case['expected_properties'] and case['prohibited'])

    def test_current_package_integrity_uses_real_contracts(self):
        result = validate_skill.validate(ROOT)
        self.assertTrue(result['valid'], result['errors'])

if __name__ == '__main__':
    unittest.main()
