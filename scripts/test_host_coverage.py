"""Matrix/data and combined-format controls; authored samples are not AI results."""
from copy import deepcopy
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

import host_coverage
from document_contracts import validate
from test_document_contracts import sample

ROOT = Path(__file__).resolve().parents[1]


class HostCoverageTests(unittest.TestCase):
    def test_required_host_matrix_includes_every_declared_task(self):
        config = json.loads((ROOT / 'config/host_validation.json').read_text())
        plan = host_coverage.freeze(ROOT, config)
        result = host_coverage.assess(plan, ROOT, [])
        self.assertEqual(plan['required_hosts'], ['codex', 'claude-code'])
        self.assertEqual(len(plan['cases']), 70)
        required = {c['id'] for name in ['document_output_cases.json', 'diagram_cases.json', 'title_cases.json'] for c in json.loads((ROOT / 'evals' / name).read_text())}
        self.assertTrue(required <= {c['id'] for c in plan['cases'] if c.get('verify_delivery')})
        self.assertFalse(result['accepted'])
        self.assertTrue(all(row['coverage_percent'] == 0 for row in result['hosts'].values()))
        print(json.dumps({'provenance': {'kind': 'authored_control', 'source': 'test_host_coverage.py: actual frozen data and empty-evidence assessment, not model quality'}, 'events': [{'phase': 'freeze', 'evidence': plan['plan_sha256']}, {'phase': 'assess', 'evidence': json.dumps(result)}]}))

    def test_assessment_requires_a_frozen_unchanged_plan(self):
        # A missing or changed frozen plan cannot support matrix acceptance.
        config = json.loads((ROOT / 'config/host_validation.json').read_text())
        plan = host_coverage.freeze(ROOT, config)
        changed = deepcopy(plan);changed['required_hosts'] = ['codex']
        with self.assertRaises(ValueError):host_coverage.assess(changed, ROOT, [])
        with self.assertRaises((ValueError, KeyError)):host_coverage.assess({}, ROOT, [])

    def test_shared_provider_parser_matches_builder_and_rejects_error_outputs(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); package = root / 'package'; (package / 'evals').mkdir(parents=True)
            (package / 'SKILL.md').write_text('# Authored fixture\n')
            case = {'id': 'example', 'kind': 'behavior'}
            (package / 'evals/cases.json').write_text(json.dumps([case]))
            plan = host_coverage.freeze(package, {'required_hosts': ['claude-code'], 'case_files': [{'path': 'evals/cases.json'}]})
            report_dir = root / 'run'; attempt = report_dir / 'one'; (attempt / 'workspace').mkdir(parents=True)
            events = attempt / 'public-events.json'
            events.write_text(json.dumps([{'type': 'result', 'subtype': 'success', 'is_error': True, 'terminal_reason': 'api_error', 'api_error': 'usage_limit_reached', 'api_error_status': 429, 'result': 'Limit reached.', 'usage': {'input_tokens': 0, 'output_tokens': 0}}]))
            row = {'id': 'one', 'case_id': 'example', 'case_sha256': host_coverage.digest(case), 'status': 'pending_review', 'exit_code': 0, 'output': 'Limit reached.', 'provenance': {'host': 'claude-code'}, 'public_events': str(events), 'workspace_hashes': {}}
            report = report_dir / 'report.json'; report.write_text(json.dumps({'execution_host': 'claude-code', 'package_hashes': plan['package_hashes'], 'attempts': [row]}))
            with self.assertRaisesRegex(ValueError, 'error result'):
                host_coverage.assess(plan, package, [{'report': str(report)}])

    def test_later_unavailable_observation_does_not_erase_a_failed_task(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder); package = root / 'package'; (package / 'evals').mkdir(parents=True)
            (package / 'SKILL.md').write_text('# Authored fixture\n')
            case = {'id': 'example', 'kind': 'behavior'}
            (package / 'evals/cases.json').write_text(json.dumps([case]))
            plan = host_coverage.freeze(package, {'required_hosts': ['claude-code'], 'case_files': [{'path': 'evals/cases.json'}]})
            base = {'case_id': 'example', 'case_sha256': host_coverage.digest(case)}
            report = root / 'report.json'; report.write_text(json.dumps({'execution_host': 'claude-code', 'package_hashes': plan['package_hashes'], 'attempts': [{**base, 'id': 'old', 'status': 'failed'}, {**base, 'id': 'new', 'status': 'infrastructure_failure'}]}))
            result = host_coverage.assess(plan, package, [{'report': str(report)}])
            self.assertEqual(result['cells'][0]['status'], 'failed')
            self.assertEqual([r['status'] for r in result['attempt_history']], ['failed', 'not_run'])

    def test_document_contexts_cover_all_catalog_types_and_preserve_fixture_bytes(self):
        cases = json.loads((ROOT / 'evals/document_output_cases.json').read_text())
        full = [c for c in cases if c['operation'] in ['create', 'rewrite'] and not c['output_kind'].startswith('issue_') and c['output_kind'] != 'requirement']
        self.assertEqual(len(full), 44)
        self.assertEqual(len(cases), 51)
        source = {c['id']: c for c in [json.loads(line) for line in (ROOT / 'evals/cases/core.jsonl').read_text().splitlines() if line.strip()]}
        self.assertEqual(len({c['id'] for c in cases}), len(cases))
        catalog = json.loads((ROOT / 'evals/catalog.json').read_text())['output_kinds']
        self.assertEqual({c['output_kind'] for c in cases}, {c['id'] for c in catalog} - {'visual'})
        for case in cases:
            original = source[case['document_case_id']]
            self.assertEqual(case['request']['source'], (ROOT / 'evals' / original['fixture']).read_text())
            self.assertEqual(case['source_case_sha256'], host_coverage.digest(original))
            self.assertIn('references/writing_style.md', case['resources'])

    def test_one_record_can_satisfy_both_structures_without_weakening_either(self):
        bug = sample('bug_report')
        incident = sample('incident').split('\n', 1)[1]
        combined = bug + '\n' + incident
        self.assertTrue(validate(combined, 'bug_report')['passed'])
        self.assertTrue(validate(combined, 'incident')['passed'])
        print(json.dumps({'provenance': {'kind': 'authored_control', 'source': 'Complete authored combined record checked against both existing structures; not real semantic performance'}, 'events': [{'phase': 'validate', 'evidence': 'Both full structural checks passed on the same bytes.'}]}))

    def test_incident_sections_cannot_replace_required_defect_information(self):
        combined = sample('bug_report') + '\n' + sample('incident').split('\n', 1)[1]
        for title in ['Expected result', 'Actual result', 'How to reproduce', 'Relevant files']:
            with self.subTest(section=title):
                changed = combined.replace('## ' + title, title, 1)
                self.assertFalse(validate(changed, 'bug_report')['passed'])
        with self.assertRaises(ValueError):validate(combined, 'unknown_report')

    def test_draft_structure_command_rejects_missing_evidence_and_accepts_a_combined_record(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'draft.md'
            combined = sample('bug_report') + '\n' + sample('incident').split('\n', 1)[1]
            path.write_text(combined.replace('## Evidence', 'Evidence', 1))
            cmd = [sys.executable, str(ROOT / 'scripts/check_document.py'), str(path), '--kind', 'bug_report']
            invalid = subprocess.run(cmd, text=True, capture_output=True)
            self.assertEqual(invalid.returncode, 1)
            self.assertIn('Missing required section: Evidence', json.loads(invalid.stdout)['findings'])
            path.write_text(combined)
            valid = subprocess.run(cmd, text=True, capture_output=True)
            self.assertEqual(valid.returncode, 0, valid.stdout)
            self.assertTrue(json.loads(valid.stdout)['semantic_review_required'])
