"""Authored convention controls; actual public messages need behavioral evals."""
from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import writing_style_contract as style
from test_writing_style_contract import style_control

ROOT = Path(__file__).resolve().parents[1]


class DocumentNameTests(unittest.TestCase):
    def test_names_come_from_the_installed_skill_without_development_catalog(self):
        labels = style.document_labels()
        self.assertEqual(labels['PRD'], 'Product Requirements Document')
        self.assertEqual(labels['WS'], 'Writing Style')
        self.assertGreater(len(labels), 15)
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'SKILL.md').write_bytes((ROOT / 'SKILL.md').read_bytes())
            self.assertEqual(style.document_labels(root), labels)

    def test_correct_labels_pass_and_repeated_bare_names_do_not(self):
        for acronym, name in style.document_labels().items():
            with self.subTest(name=name):
                self.assertEqual(style.document_name_findings(name + ' (' + acronym + ')'), [])
        text = 'I will write the PRD.\nThe HLD draft follows the Writing Style guide.'
        findings = style.document_name_findings(text)
        self.assertEqual({r['text'] for r in findings}, {'PRD', 'HLD', 'Writing Style'})
        self.assertEqual(style.document_name_findings('PRD and PRD.')[0]['expected'], 'Product Requirements Document (PRD)')
        self.assertEqual(len(style.document_name_findings('PRD and PRD.')), 2)

    def test_literals_source_quotes_external_titles_and_method_context_are_preserved(self):
        text = '`PRD` and README.md\n```json\n{"PRD": "value"}\n```\n"PRD"\n> HLD is the quoted source title.\n[External PRD template](https://example.org/template)\nThe SDD method guides development.\n'
        self.assertEqual(style.document_name_findings(text), [])
        self.assertEqual(style.document_name_findings('AI uses an IP address.'), [])
        self.assertTrue(style.document_name_findings('[PRD draft](output/document.md)'))

    def test_favorable_self_review_cannot_waive_confirmed_name_violations(self):
        for text in ['I will rewrite the PRD.', 'The Writing Style guide applies.', 'The Low Level Design draft is ready.']:
            contract = style.packet(text, style.load_guide(ROOT))
            self.assertTrue(contract['document_name_findings']['output'])
            self.assertFalse(style.check_review(contract, style_control(contract)))

    def test_diagram_code_identifiers_are_literals_but_visible_svg_labels_are_checked(self):
        content = '```text\nflowchart LR\n PRD["Product Requirements Document (PRD)"]\n```\n'
        contract = style.packet(content, style.load_guide(ROOT))
        self.assertTrue(style.check_review(contract, style_control(contract)))
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            svg = '<svg xmlns="http://www.w3.org/2000/svg"><text>PRD</text></svg>'
            contract = style.packet('![Document](diagram.svg)', style.load_guide(ROOT),
                                    [{'id': 'diagram', 'path': str(root / 'diagram.svg'), 'text': svg}], root / 'output.md')
            self.assertFalse(style.check_review(contract, style_control(contract)))

    def test_message_cli_returns_actual_findings_and_approved_names(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'message.md'
            path.write_text('I will write the PRD.\n')
            cmd = [sys.executable, str(ROOT / 'scripts/writing_style_contract.py')]
            bad = subprocess.run(cmd + ['check', str(path)], capture_output=True, text=True)
            self.assertEqual(bad.returncode, 1, bad.stderr)
            self.assertEqual(json.loads(bad.stdout)['findings'][0]['text'], 'PRD')
            path.write_text('I will write the Product Requirements Document (PRD).\n')
            good = subprocess.run(cmd + ['check', str(path)], capture_output=True, text=True)
            self.assertEqual(good.returncode, 0, good.stderr)
            names = subprocess.run(cmd + ['names'], capture_output=True, text=True)
            self.assertEqual(names.returncode, 0, names.stderr)
            self.assertEqual(json.loads(names.stdout)['PRD'], 'Product Requirements Document (PRD)')

    def test_actual_guide_author_check_review_chain(self):
        guide = style.load_guide(ROOT)
        labels = style.document_labels()
        content = 'I will review the ' + labels['PRD'] + ' (PRD).'
        findings = style.document_name_findings(content)
        contract = style.packet(content, guide)
        accepted = style.check_review(contract, style_control(contract))
        self.assertEqual(findings, [])
        self.assertTrue(accepted)
        print(json.dumps({'process_trace': {'provenance': {'kind': 'authored_control', 'source': 'Actual guide load, authored content, convention check and bound review; not model-quality evidence.'},
              'events': [{'phase': 'load', 'evidence': contract['guide_sha256']}, {'phase': 'author', 'evidence': content},
                         {'phase': 'check', 'evidence': json.dumps({'findings': findings})}, {'phase': 'review', 'evidence': json.dumps({'accepted': accepted, 'targets': contract['targets_sha256']})}]}}))

    def test_incomplete_work_does_not_support_none_exist_or_unimplemented_claims(self):
        source = 'No implementation or tests are complete. No independent repository inspection is available.'
        for content in ["No test has been identified or written.", "The tests: none exist yet.", "The proposed change hasn't been implemented.", "This is an unimplemented proposal.", "Nobody has inspected the repository."]:
            with self.subTest(content=content):
                contract = style.packet(content, style.load_guide(ROOT), [{'id': 'facts', 'text': source}])
                self.assertTrue(contract['unsupported_absence_findings']['output'])
                self.assertFalse(style.check_review(contract, style_control(contract)))
        content = 'No implementation or tests are complete; whether any tests exist is unknown.'
        contract = style.packet(content, style.load_guide(ROOT), [{'id': 'facts', 'text': source}])
        self.assertTrue(style.check_review(contract, style_control(contract)))

    def test_incomplete_tests_do_not_establish_zero_execution_or_passing_checks(self):
        source = 'Implementation and testing are incomplete. Existing results were not supplied.'
        for content in ['None of these checks has passed yet.', 'No acceptance tests have passed.',
                        'No tests have run.', 'No results were recorded.']:
            with self.subTest(content=content):
                contract = style.packet(content, style.load_guide(ROOT), [{'id': 'facts', 'text': source}])
                self.assertTrue(contract['unsupported_absence_findings']['output'])
                self.assertFalse(style.check_review(contract, style_control(contract)))
        for content in ['Implementation and testing are incomplete; existing results were not supplied.',
                        'Some checks passed; testing is incomplete.',
                        'Whether any checks passed is unknown.',
                        'No acceptance tests have passed.']:
            with self.subTest(supported=content):
                contract = style.packet(content, style.load_guide(ROOT), [{'id': 'actual_evidence', 'text': content}])
                self.assertTrue(style.check_review(contract, style_control(contract)))

    def test_unknown_values_and_incomplete_tests_do_not_support_unset_or_absent_results(self):
        source = 'The target, baseline and owner are unknown. Tests are incomplete.'
        for text in ['No numerical target or baseline has been set.',
                     'No owner has been assigned.', 'No test results are available, because tests are incomplete.']:
            with self.subTest(text=text):
                contract = style.packet(text, style.load_guide(ROOT), [{'id': 'facts', 'text': source}])
                self.assertTrue(contract['unsupported_absence_findings']['output'])
                self.assertFalse(style.check_review(contract, style_control(contract)))
        for text in ['The numerical target and baseline are unknown.',
                     'Tests are incomplete; results were not supplied.',
                     'No numerical target or baseline has been set.',
                     'No test results are available.']:
            contract = style.packet(text, style.load_guide(ROOT), [{'id': 'explicit_source', 'text': text}])
            self.assertTrue(style.check_review(contract, style_control(contract)))

        print(json.dumps({'provenance': {'kind': 'authored_control', 'source': 'Actual source-bound positive/negative style review checks, not model quality.'}, 'events': [{'phase': 'check', 'evidence': 'Unsupported unset/zero-result claims failed; explicit-source and unknown/partial-result controls passed.'}]}))

    def test_explicit_negative_evidence_and_source_quotations_are_preserved(self):
        content = 'No automated test has been written.'
        contract = style.packet(content, style.load_guide(ROOT), [{'id': 'facts', 'text': content}])
        self.assertTrue(style.check_review(contract, style_control(contract)))
        quoted = 'The source says "No automated test has been written."'
        self.assertEqual(style.unsupported_absence_findings(quoted), [])
        self.assertEqual(style.unsupported_absence_findings('Whether none exist yet is unknown.'), [])

    def test_invalid_prose_or_missing_catalog_cannot_create_a_pass(self):
        with self.assertRaises(TypeError):
            style.document_name_findings(None)
        with self.assertRaises(ValueError):
            style.packet('PRD', '')
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'SKILL.md').write_text('# No routing labels\n')
            with self.assertRaises(ValueError):
                style.document_labels(root)



if __name__ == '__main__':
    unittest.main()
