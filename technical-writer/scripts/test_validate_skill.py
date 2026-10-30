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
        shutil.copytree(HERE.parent, self.root, ignore=shutil.ignore_patterns('__pycache__', 'runs'))

    def tearDown(self): self.temp.cleanup()

    def rejects(self, fragment):
        result = validator.validate(self.root)
        self.assertFalse(result['valid'])
        self.assertTrue(any(fragment in error for error in result['errors']), result['errors'])

    def test_valid_package(self): self.assertTrue(validator.validate(self.root)['valid'])

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

    def test_stale_issue_link_label(self):
        p = self.root / 'SKILL.md'
        p.write_text(p.read_text() + '\n[Work items](references/issue.md)\n')
        self.rejects('Stale issue link label')

    def test_issue_title_matches_canonical_name(self):
        p = self.root / 'references/issue.md'
        p.write_text(p.read_text().replace('# Issue', '# Work item', 1))
        self.rejects('Canonical issue guide title')

    def test_empty_principles_in_actual_example(self):
        p = self.root / 'references/policy.md'
        body = p.read_text()
        body = body.replace('## Principles\nCollect only information needed to diagnose service behavior. Keep requests traceable without exposing credentials.', '## Principles\n')
        p.write_text(body)
        self.rejects('Missing/empty Principles')

    def test_missing_operation_coverage(self):
        p = self.root / 'evals/coverage.json'
        data = json.loads(p.read_text()); data['output_kinds']['user_story']['rewrite'] = []
        p.write_text(json.dumps(data))
        self.rejects('Missing operation coverage')

    def test_unclosed_nested_example(self):
        p = self.root / 'references/tutorial.md'
        body = p.read_text(); marker = chr(96) * 4
        p.write_text(body.replace('\n' + marker + '\n', '\n', 1))
        self.rejects('Unclosed code fence')

    def test_fence_parser_handles_literal_inner_blocks(self):
        tick = chr(96)
        text = tick*4 + 'md\n# Example\n' + tick*3 + 'sh\necho ok\n' + tick*3 + '\n' + tick*4 + '\n'
        blocks, broken = validator.blocks(text)
        self.assertFalse(broken); self.assertEqual(len(blocks), 1)
        self.assertIn('echo ok', blocks[0][1])


if __name__ == '__main__': unittest.main()
