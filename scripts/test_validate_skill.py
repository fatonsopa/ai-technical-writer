import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('validator', HERE / 'validate_skill.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class IntegrityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name) / 'skill'
        shutil.copytree(HERE.parent, self.root, ignore=shutil.ignore_patterns('__pycache__', 'runs', '.git', '.venv'))

    def tearDown(self): self.temp.cleanup()

    def rejects(self, fragment):
        result = validator.validate(self.root)
        self.assertFalse(result['valid'])
        self.assertTrue(any(fragment in error for error in result['errors']), result['errors'])

    def test_valid_package(self): self.assertTrue(validator.validate(self.root)['valid'])

    def test_root_license_is_required(self):
        (self.root / 'LICENSE').unlink()
        self.rejects('LICENSE')

    def test_nested_entry_point_is_rejected(self):
        p = self.root / 'examples/archive/SKILL.md'
        p.parent.mkdir(parents=True)
        p.write_text('# Archived skill\n')
        self.rejects('Nested skill')

    def test_dist_directory_is_rejected(self):
        (self.root / 'dist').mkdir()
        self.rejects('dist')

    def test_case_sensitive_fixture_paths_are_enforced(self):
        p = self.root / 'evals/cases/core.jsonl'
        p.write_text(p.read_text().replace('fixtures/skill_input.md', 'fixtures/SKILL_INPUT.md'))
        self.rejects('Missing fixture')

    def test_missing_routed_reference(self):
        (self.root / 'references/user_story.md').unlink()
        self.rejects('Broken local link')

    def test_broken_nested_link(self):
        p = self.root / 'references/issue.md'
        p.write_text(p.read_text() + '\n[Lost document](not_present.md)\n')
        self.rejects('Broken local link')

    def test_retired_reference_returns(self):
        (self.root / 'references/requirements.md').write_text('# Duplicate owner\n')
        self.rejects('Unexpected retired reference')

    def test_missing_complete_example(self):
        (self.root / 'examples/implementation_plan.md').unlink()
        self.rejects('Missing complete example')

    def test_missing_external_example_section(self):
        p = self.root / 'examples/implementation_plan.md'
        p.write_text(p.read_text().replace('## Rollout and recovery', '## Deployment', 1))
        self.rejects('Missing/empty example section')

    def test_external_example_link_is_checked(self):
        p = self.root / 'examples/product_requirements_document.md'
        p.write_text(p.read_text() + '\n[Plan](missing_plan.md)\n')
        self.rejects('Broken local link')

    def test_stale_issue_link_label(self):
        p = self.root / 'SKILL.md'
        p.write_text(p.read_text() + '\n[Work items](references/issue.md)\n')
        self.rejects('Stale issue link label')

    def test_issue_title_matches_canonical_name(self):
        p = self.root / 'references/issue.md'
        p.write_text(p.read_text().replace('# Issue', '# Work item', 1))
        self.rejects('Canonical issue guide title')

    def test_bug_template_keeps_separate_results(self):
        p = self.root / 'references/bug_report.md'
        p.write_text(p.read_text().replace('## Expected result\n', '## Expected and actual results\n', 1))
        self.rejects('Missing/empty Expected result in bug template')

    def test_bug_example_retains_relevant_files(self):
        p = self.root / 'examples/bug_report.md'
        p.write_text(p.read_text().replace('## Relevant files', '## Supporting information', 1))
        self.rejects('Missing/empty Relevant files in bug example')

    def test_issue_uses_acceptance_criteria(self):
        p = self.root / 'references/issue.md'
        p.write_text(p.read_text().replace('## Acceptance criteria', '## Completion criteria', 1))
        self.rejects('Missing/empty Acceptance criteria in issue template')

    def test_shared_requirement_ids_do_not_drift(self):
        p = self.root / 'examples/test_specification.md'
        p.write_text(p.read_text().replace('T13 / WEB-08', 'T13 / WEB-07'))
        self.rejects('Shared example requirement mismatch')

    def test_empty_principles_in_actual_example(self):
        p = self.root / 'examples/policy.md'
        body = p.read_text()
        start = body.index('## Principles\n'); end = body.index('## Policy obligations', start)
        body = body[:start] + '## Principles\n\n' + body[end:]
        p.write_text(body)
        self.rejects('Missing/empty Principles')

    def test_missing_operation_coverage(self):
        p = self.root / 'evals/coverage.json'
        data = json.loads(p.read_text()); data['output_kinds']['user_story']['rewrite'] = []
        p.write_text(json.dumps(data))
        self.rejects('Missing operation coverage')

    def test_unclosed_nested_example(self):
        p = self.root / 'examples/agents_and_skills.md'
        body = p.read_text(); marker = chr(96) * 4
        head, tail = body.rsplit('\n' + marker + '\n', 1)
        p.write_text(head + '\n' + tail)
        self.rejects('Unclosed code fence')

    def test_fence_parser_handles_literal_inner_blocks(self):
        tick = chr(96)
        text = tick*4 + 'md\n# Example\n' + tick*3 + 'sh\necho ok\n' + tick*3 + '\n' + tick*4 + '\n'
        blocks, broken = validator.blocks(text)
        self.assertFalse(broken); self.assertEqual(len(blocks), 1)
        self.assertIn('echo ok', blocks[0][1])


if __name__ == '__main__': unittest.main()
