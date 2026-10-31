import importlib.util
import json
import subprocess
import sys
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('eval_runner', ROOT / 'evals/run.py')
runner = importlib.util.module_from_spec(spec); spec.loader.exec_module(runner)


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.folder = Path(self.temp.name)
        self.case = next(c for c in runner.cases() if c['id'] == 'user_story-create')
        self.args = SimpleNamespace(skill=ROOT, out=self.folder / 'out', generated=self.folder / 'generated',
                                    variant='unit-test', model='test-model', temp_root=None)

    def tearDown(self): self.temp.cleanup()

    def test_calibration_rejects_false_pass_and_missing_control(self):
        labels = {'bad':{'passed':False,'critical_expected':True},
                  'good':{'passed':True,'critical_expected':False}}
        self.assertEqual(runner.calibration_agreement([
            {'id':'bad','passed':True,'critical_failures':[]}], labels), ['bad','good'])
        self.assertEqual(runner.calibration_agreement([
            {'id':'bad','passed':False,'critical_failures':['Invented result']},
            {'id':'good','passed':True,'critical_failures':[]}], labels), [])

    def test_cli_preserves_an_existing_attempt(self):
        folder = self.args.out / 'user_story'; folder.mkdir(parents=True)
        record = folder / 'record.json'; record.write_text('original attempt')
        result = subprocess.run([sys.executable, str(ROOT / 'evals/run.py'), 'generate',
            '--model', 'unused-model', '--kind', 'user_story', '--out', str(self.args.out)],
            text=True, capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('preserve prior attempts', result.stderr)
        self.assertEqual(record.read_text(), 'original attempt')

    def seed(self):
        folder = self.args.generated / 'user_story'; folder.mkdir(parents=True)
        self.seed_record(folder, self.case, 'Supplied output')


    def seed_record(self, folder, case, content):
        generator = getattr(self.args, 'generator_skill', None) or self.args.skill
        bundle = runner.evaluation.capture(generator, [case])
        values = [{'id': case['id'], 'content': content, 'references_read': []}]
        (folder / 'frozen.json').write_text(json.dumps(bundle))
        (folder / 'record.json').write_text(json.dumps({'status': 'completed', 'variant': 'unit-test',
            'input_snapshot_sha256': runner.digest(bundle), 'output_sha256': runner.digest(values), 'results': values}))

    def test_generation_hides_grader_inputs(self):
        def fake(work, output, prompt, model, grading=False):
            self.assertFalse((work / 'skill/evals').exists())
            self.assertTrue((work / 'skill/examples/user_story.md').is_file())
            request = json.loads((work / 'requests.json').read_text())[0]
            self.assertEqual(set(request), {'id','request','source'})
            self.assertNotIn('expected_properties', request)
            self.assertTrue((work / request['source']).exists())
            self.assertIn('Do not edit files', prompt)
            output.mkdir(parents=True)
            return {'status':'completed','results':[{'id':self.case['id'],'content':'Story','references_read':[]}]}
        with patch.object(runner, 'invoke', fake):
            self.assertEqual(runner.generate(('user_story',[self.case]), self.args)[1], 'completed')

    def test_missing_output_id_is_not_a_pass(self):
        def fake(work, output, *args, **kwargs):
            output.mkdir(parents=True); return {'status':'completed','results':[]}
        with patch.object(runner, 'invoke', fake):
            self.assertEqual(runner.generate(('user_story',[self.case]), self.args)[1], 'infrastructure_error')

    def test_critical_failure_overrides_high_scores(self):
        self.seed()
        def fake(work, output, *args, **kwargs):
            packet = json.loads((work / 'packet.json').read_text())
            self.assertIn('sources', packet); self.assertIn('guides', packet)
            self.assertNotIn('type_guidance', packet['cases'][0])
            output.mkdir(parents=True)
            return {'status':'completed','results':[{'id':self.case['id'],'scores':[3]*7,
                    'critical_failures':['Invented approval'],'reasons':['Source has no approval.']}]}
        with patch.object(runner, 'invoke', fake): runner.grade(('user_story',[self.case]), self.args)
        record = json.loads((self.args.out / 'user_story/record.json').read_text())
        self.assertFalse(record['results'][0]['passed'])

    def test_missing_grade_id_is_infrastructure_error(self):
        self.seed()
        def fake(work, output, *args, **kwargs):
            output.mkdir(parents=True); return {'status':'completed','results':[]}
        with patch.object(runner, 'invoke', fake):
            self.assertEqual(runner.grade(('user_story',[self.case]), self.args)[1], 'infrastructure_error')

    def test_grader_receives_actual_resource_and_tool_context(self):
        self.args.generator_skill = self.folder / 'baseline'
        self.args.generator_skill.mkdir()
        (self.args.generator_skill / 'SKILL.md').write_text('Baseline only')
        (self.args.generator_skill / 'scripts').mkdir()
        (self.args.generator_skill / 'scripts/helper.py').write_text('print("check")')
        self.seed()
        event = {'type':'item.completed','item':{'type':'command_execution',
                 'command':'python3 inventory.py source.md','exit_code':0}}
        (self.args.generated / 'user_story/events.jsonl').write_text(json.dumps(event)+'\n')
        def fake(work, output, *args, **kwargs):
            context = json.loads((work / 'packet.json').read_text())['generator_context']
            self.assertEqual(context['available_runtime_files'], ['SKILL.md', 'scripts/helper.py'])
            self.assertEqual(context['tool_actions'][0]['exit_code'], 0)
            self.assertIn('sources/name.md', context['source_path_mapping'])
            output.mkdir(parents=True)
            return {'status':'completed','results':[{'id':self.case['id'],'scores':[3]*7,
                    'critical_failures':[],'reasons':['Checked.']}]}
        with patch.object(runner, 'invoke', fake): runner.grade(('user_story',[self.case]), self.args)

    def test_acceptance_standard_uses_same_governance_gate(self):
        self.case = next(c for c in runner.cases() if c['id'] == 'accept-standard-exception')
        self.args.generated = self.folder / 'acceptance'
        folder = self.args.generated / self.case['kind']; folder.mkdir(parents=True)
        self.seed_record(folder, self.case, '# Standard\n\nA rule without required sections.')
        def fake(work, output, *args, **kwargs):
            output.mkdir(parents=True)
            return {'status':'completed','results':[{'id':self.case['id'],'scores':[3]*7,
                    'critical_failures':[],'reasons':['Incorrectly accepted by model.']}]}
        with patch.object(runner, 'invoke', fake): runner.grade((self.case['kind'],[self.case]), self.args)
        record = json.loads((self.args.out / self.case['kind'] / 'record.json').read_text())
        self.assertFalse(record['results'][0]['passed'])
        self.assertTrue(any('Definitions' in value for value in record['results'][0]['critical_failures']))
        self.assertTrue(any('Verification' in value for value in record['results'][0]['critical_failures']))

    def test_sdd_cannot_be_mislabeled_as_software_design(self):
        self.case = next(c for c in runner.cases() if c['id'] == 'sdd-create')
        folder = self.args.generated / 'sdd'; folder.mkdir(parents=True)
        self.seed_record(folder, self.case, '# Rename: software design document\n\nBehavior.')
        def fake(work, output, *args, **kwargs):
            output.mkdir(parents=True)
            return {'status':'completed','results':[{'id':self.case['id'],'scores':[3]*7,
                    'critical_failures':[],'reasons':['Missed acronym confusion.']}]}
        with patch.object(runner, 'invoke', fake): runner.grade(('sdd',[self.case]), self.args)
        record = json.loads((self.args.out / 'sdd/record.json').read_text())
        self.assertFalse(record['results'][0]['passed'])

    def test_complete_bug_cannot_combine_results_or_omit_files(self):
        self.case = next(c for c in runner.cases() if c['id'] == 'bug_report-create')
        folder = self.args.generated / 'bug_report'; folder.mkdir(parents=True)
        self.seed_record(folder, self.case, '# Bug\n\n## Expected and actual results\nA mismatch.')
        def fake(work, output, *args, **kwargs):
            packet=json.loads((work / 'packet.json').read_text())
            self.assertIn('How to reproduce', packet['cases'][0]['required_sections'])
            output.mkdir(parents=True)
            return {'status':'completed','results':[{'id':self.case['id'],'scores':[3]*7,
                    'critical_failures':[],'reasons':['Missed required structure.']}]}
        with patch.object(runner, 'invoke', fake): runner.grade(('bug_report',[self.case]), self.args)
        record = json.loads((self.args.out / 'bug_report/record.json').read_text())
        failures = record['results'][0]['critical_failures']
        self.assertFalse(record['results'][0]['passed'])
        self.assertIn('Missing required section: Relevant files', failures)
        self.assertIn('Missing required section: How to reproduce', failures)

    def test_issue_contract_respects_description_only_scope(self):
        complete = next(c for c in runner.cases() if c['id'] == 'issue_chore-create')
        narrow = next(c for c in runner.cases() if c['id'] == 'accept-small-chore')
        self.assertIn('Acceptance criteria', runner.required_sections(complete))
        self.assertEqual(runner.required_sections(narrow), [])

    def test_prd_missing_structure_fails_even_when_legacy_judge_awards_threes(self):
        self.case = next(c for c in runner.cases() if c['id'] == 'prd-create')
        folder = self.args.generated / 'prd'; folder.mkdir(parents=True)
        self.seed_record(folder, self.case, '# Product\n\nA note without required PRD sections.')
        def fake(work, output, *args, **kwargs):
            output.mkdir(parents=True)
            return {'status': 'completed', 'results': [{'id': self.case['id'], 'scores': [3]*7,
                'critical_failures': [], 'reasons': ['Deliberately mistaken judge control.']}]}
        with patch.object(runner, 'invoke', fake):
            runner.grade(('prd', [self.case]), self.args)
        record = json.loads((self.args.out / 'prd/record.json').read_text())
        self.assertFalse(record['results'][0]['passed'])
        assessment = runner.evaluation.assess_saved(self.args.generated, self.args.out)
        self.assertFalse(assessment['accepted'])
        self.assertEqual(assessment['task_success_percent'], 0)
        result = subprocess.run([sys.executable, str(ROOT/'evals/run.py'), 'summary',
            '--generated', str(self.args.generated), '--grades', str(self.args.out)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertFalse(json.loads(result.stdout)['accepted'])

    def test_grading_refuses_mutated_generated_content(self):
        self.seed()
        path = self.args.generated / 'user_story/record.json'
        record = json.loads(path.read_text())
        record['results'][0]['content'] = 'A different captured answer.'
        path.write_text(json.dumps(record))
        with self.assertRaisesRegex(ValueError, 'generated output changed'):
            runner.grade(('user_story', [self.case]), self.args)

    def test_optional_provider_transport_shares_the_declared_call_budget(self):
        from adapters import codex
        budget = runner.evaluation.CallBudget(1, 10)
        with patch.object(runner, 'LIVE_BUDGET', budget), patch.object(codex.subprocess, 'Popen', side_effect=OSError('CLI unavailable')) as process:
            first = runner.invoke(self.folder, self.folder / 'provider-first', 'An authored transport control.', 'unit-model')
            second = runner.invoke(self.folder, self.folder / 'provider-second', 'An authored transport control.', 'unit-model')
        self.assertEqual(process.call_count, 1)
        self.assertEqual(first['status'], 'infrastructure_error')
        self.assertEqual(first['budget']['cli_invocations'], 1)
        self.assertIn('allowance exhausted', second['error'])
        self.assertEqual(second['budget']['cli_invocations'], 1)


if __name__ == '__main__': unittest.main()
