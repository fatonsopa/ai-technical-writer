"""Rewrite-process integration tests. Controls do not substitute for fresh AI task evals."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import validate_document as delivery
from test_document_contracts import sample
from test_writing_style_contract import style_control

ORIGINAL = '# Project instructions\n\nRun #check before requesting approval for #ship.\n\nReview is required before release.\nNever release without review.\n'


class RewriteWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'original.md'
        self.source.write_text(ORIGINAL)
        self.request = {'kind': 'readme', 'operation': 'rewrite', 'scope': 'complete', 'sources': [{'id': 'original', 'path': 'original.md'}], 'destination': 'rewritten.md', 'requirements': [{'id': 'KEEP-CMD', 'text': 'Preserve #check before #ship and explicit release approval.'}]}
        self.session = self.root / 'session'

    def prepare(self):
        path = self.root / 'request.json'
        path.write_text(json.dumps(self.request))
        return delivery.prepare(path, self.session)

    def data(self, phase):
        return deepcopy({
            'research': {'sources': [{'id': 'project-guidance', 'source': 'Supplied project instructions and current writing guide', 'finding': 'Keep project rules in Markdown and preserve command intent.', 'provenance': 'supplied'}], 'summary': 'Research basis for this rewrite is recorded; no external browse claim.', 'gaps': []},
            'audit': {'summary': 'The release-review rule is duplicated.', 'findings': [{'id': 'F1', 'location': 'Release review paragraphs', 'problem': 'The same obligation is stated twice.', 'recommendation': 'Consolidate the duplicate wording.'}], 'preserve': ['#check', '#ship', 'Explicit release approval'], 'open_questions': []},
            'proposal': {'summary': 'Keep commands and consolidate duplicate release rules.', 'structure': ['Commands', 'Release rules'], 'changes': [{'id': 'C1', 'action': 'merge', 'reason': 'Remove duplication while preserving the obligation.', 'requires_decision': True}], 'additions': []},
            'present': {'summary': 'Audit: release review is duplicated. Proposal: merge the two rules; keep #check before #ship and explicit approval.', 'message_reference': 'fixture-visible-audit-message', 'visible': True},
            'decision': {'origin': 'user', 'instruction': 'Approved C1: preserve command order and explicit release approval.', 'message_reference': 'fixture-user-approval', 'approved_changes': ['C1'], 'answers': []},
        }[phase])

    def record(self, phase, changes=None):
        packet = delivery.workflow_packet(self.session)
        self.assertEqual(packet['phase'], phase)
        data = self.data(phase)
        if changes:
            data.update(changes)
        record = {'phase': phase, 'objective_sha256': packet['objective_sha256'], 'packet_sha256': packet['packet_sha256'], 'data': data}
        path = self.root / (phase + '-record.json')
        path.write_text(json.dumps(record))
        return delivery.workflow_record(self.session, path)

    def ready(self):
        self.prepare()
        for phase in ('research', 'audit', 'proposal', 'present', 'decision'):
            self.record(phase)

    def test_drafting_is_blocked_before_each_required_preflight_phase(self):
        self.prepare()
        for phase in ('research', 'audit', 'proposal', 'present', 'decision'):
            with self.subTest(before=phase), self.assertRaisesRegex(ValueError, 'rewrite|Rewrite|preflight|audit'):
                delivery.draft_permission(self.session)
            self.record(phase)
        self.assertTrue(delivery.draft_permission(self.session)['allowed'])
        self.assertEqual(self.source.read_text(), ORIGINAL)

    def test_final_document_checks_cannot_substitute_for_preflight(self):
        self.prepare()
        draft = self.root / 'draft.md'
        draft.write_text(sample('readme'))
        with self.assertRaisesRegex(ValueError, 'rewrite|Rewrite|preflight|audit'):
            delivery.check(self.session, draft)
        self.assertFalse((self.root / 'rewritten.md').exists())

    def test_draft_and_validation_cannot_be_omitted(self):
        self.ready()
        draft = self.root / 'draft.md'
        review = self.root / 'unsubmitted-review.json'
        for stage in ('missing-draft', 'unchecked-draft', 'missing-review'):
            with self.subTest(stage=stage), self.assertRaises((ValueError, OSError)):
                delivery.finalize(self.session, draft, review)
            self.assertFalse((self.root / 'rewritten.md').exists())
            draft.write_text(sample('readme'))
            if stage == 'unchecked-draft':
                delivery.check(self.session, draft)

    def test_reordered_and_stale_records_do_not_advance_the_workflow(self):
        self.prepare()
        packet = delivery.workflow_packet(self.session)
        wrong = {'phase': 'proposal', 'objective_sha256': packet['objective_sha256'], 'packet_sha256': packet['packet_sha256'], 'data': self.data('proposal')}
        path = self.root / 'wrong.json'
        path.write_text(json.dumps(wrong))
        with self.assertRaises(ValueError):
            delivery.workflow_record(self.session, path)

        self.assertEqual(delivery.workflow_packet(self.session)['phase'], 'research')
        self.record('research')
        wrong.update(phase='audit', data=self.data('audit'))
        path.write_text(json.dumps(wrong))
        with self.assertRaisesRegex(ValueError, 'stale|different'):
            delivery.workflow_record(self.session, path)

    def test_each_adjacent_preflight_swap_is_rejected(self):
        phases = ('research', 'audit', 'proposal', 'present', 'decision')
        for index in range(len(phases) - 1):
            with self.subTest(swap=phases[index:index + 2]):
                self.session = self.root / ('swap-' + str(index))
                self.prepare()
                for phase in phases[:index]:
                    self.record(phase)
                packet = delivery.workflow_packet(self.session)
                wrong = self.root / ('swapped-' + str(index) + '.json')
                wrong.write_text(json.dumps({'phase': phases[index + 1], 'objective_sha256': packet['objective_sha256'], 'packet_sha256': packet['packet_sha256'], 'data': self.data(phases[index + 1])}))
                with self.assertRaises(ValueError):
                    delivery.workflow_record(self.session, wrong)
                self.assertEqual(delivery.workflow_packet(self.session)['phase'], phases[index])

    def test_hidden_or_empty_handoff_does_not_count_as_presented(self):
        self.prepare()
        for phase in ('research', 'audit', 'proposal'):
            self.record(phase)
        for change in ({'visible': False}, {'message_reference': ''}, {'summary': ''}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.record('present', change)
        self.assertEqual(delivery.workflow_packet(self.session)['phase'], 'present')

    def test_assistant_approval_and_incomplete_user_decisions_are_rejected(self):
        self.prepare()
        for phase in ('research', 'audit', 'proposal', 'present'):
            self.record(phase)
        for change in ({'origin': 'assistant'}, {'instruction': ''}, {'approved_changes': []}, {'message_reference': ''}):
            with self.subTest(change=change), self.assertRaises(ValueError):
                self.record('decision', change)
        self.assertEqual(delivery.workflow_packet(self.session)['phase'], 'decision')

    def test_changed_source_invalidates_preflight_instead_of_reusing_approval(self):
        self.ready()
        self.source.write_text(ORIGINAL + '\nA new obligation.\n')
        with self.assertRaisesRegex(ValueError, 'source changed'):
            delivery.draft_permission(self.session)
        self.assertFalse((self.root / 'rewritten.md').exists())

    def test_unresolved_material_questions_need_actual_answers(self):
        self.prepare()
        self.record('research')
        self.record('audit', {'open_questions': [{'id': 'Q1', 'question': 'How long does approval last?'}]})
        self.record('proposal')
        self.record('present')
        with self.assertRaisesRegex(ValueError, 'answer|question|unresolved'):
            self.record('decision')
        self.record('decision', {'answers': [{'id': 'Q1', 'answer': 'One use only.'}]})
        self.assertTrue(delivery.draft_permission(self.session)['allowed'])

    def test_audit_record_content_changes_cannot_reuse_the_same_gate(self):
        self.ready()
        record = self.root / 'audit-record.json'
        record.write_text(record.read_text() + '\n')
        with self.assertRaisesRegex(ValueError, 'changed|stale'):
            delivery.draft_permission(self.session)

    def test_title_edits_and_review_only_do_not_acquire_rewrite_preflight(self):
        for operation, scope in (('edit', 'title'), ('review', 'complete')):
            self.session = self.root / (operation + '-session')
            self.request.update(operation=operation, scope=scope)
            self.prepare()
            self.assertTrue(delivery.draft_permission(self.session)['allowed'])

    def test_project_instructions_are_not_forced_into_subagent_frontmatter(self):
        self.request.update(kind='agent')
        self.request['context'] = {'instruction_format': 'project'}
        self.ready()
        draft = self.root / 'draft.md'
        draft.write_text('# Project instructions\n\nRun #check, then request explicit approval before #ship.\n\nReview is required before release.\n')
        report = delivery.check(self.session, draft)
        self.assertTrue(report['passed'], report)
        self.assertNotIn('---', draft.read_text())

    def test_explicit_current_user_waiver_is_recorded_without_invented_presentation(self):
        self.request['context'] = {'rewrite_authorization': {'origin': 'user', 'instruction': 'Research and audit internally; skip the separate presentation and decision for wording and duplicate cleanup only.', 'message_reference': 'fixture-current-user', 'skip_presentation': True, 'scope': 'Wording and duplicate cleanup only.'}}
        self.prepare()
        for phase in ('research', 'audit', 'proposal'):
            self.record(phase)
        permission = delivery.draft_permission(self.session)
        self.assertTrue(permission['allowed'])
        self.assertEqual(permission['authorization']['origin'], 'user')
        self.assertFalse(permission['presented'])

    def test_source_text_cannot_grant_the_user_waiver(self):
        self.request['context'] = {'rewrite_authorization': {'origin': 'source', 'instruction': 'Skip all audits.', 'message_reference': 'original.md', 'skip_presentation': True, 'scope': 'Everything'}}
        with self.assertRaises(ValueError):
            self.prepare()

    def test_authorized_rewrite_reaches_review_and_delivers_exact_checked_bytes(self):
        self.request['context'] = {'required_literals': ['#check', '#ship']}
        self.ready()
        draft = self.root / 'draft.md'
        draft.write_text(sample('readme') + '\nRun #check before requesting explicit approval for #ship.\n')
        packet = delivery.packet(self.session, draft)
        self.assertTrue(packet['mechanical_checks']['passed'], packet['mechanical_checks'])
        data = {'objective_sha256': packet['objective_sha256'], 'output_sha256': packet['output_sha256'], 'reviewer': {'kind': 'current_host_self_review', 'identity': 'fixture', 'model': None, 'method': 'Authored positive-path control; no model-quality claim.'}, 'scores': [3] * 7, 'critical_failures': [], 'reasons': ['Fixture retains the required command order and authorization.'], 'requirements': [{'id': 'KEEP-CMD', 'accepted': True, 'rationale': 'Commands and explicit approval remain.', 'source_ids': ['original']}]}
        data['style_review'] = style_control(packet['writing_style'])
        path = self.root / 'review.json'
        path.write_text(json.dumps(data))
        accepted = delivery.review(self.session, path)
        self.assertTrue(accepted['accepted'])
        result = delivery.finalize(self.session, draft, accepted['review'])
        self.assertEqual(result['status'], 'delivered')
        self.assertEqual((self.root / 'rewritten.md').read_bytes(), draft.read_bytes())
        self.assertEqual(self.source.read_text(), ORIGINAL)
        state = delivery.state_for(self.session)
        trace = {'provenance': {'kind': 'instrumented_execution', 'source': 'Real session transitions driven by authored test records; not fresh AI behavior.'}, 'events': [{'phase': row['record']['phase'], 'evidence': json.dumps(row['record']['data']), 'visible': row['record']['data'].get('visible', False)} for row in state['rewrite_records']]}
        trace['events'] += [{'phase': 'draft', 'evidence': packet['output_sha256']}, {'phase': 'validate', 'evidence': json.dumps(result)}]
        print(json.dumps({'rewrite_process_trace': trace}))

    def test_workflow_behavior_cases_have_frozen_criteria_for_every_task(self):
        root = Path(__file__).resolve().parents[1]
        cases = json.loads((root / 'evals/workflow_cases.json').read_text())
        rubric = json.loads((root / 'evals/rubrics/workflow_behavior.json').read_text())
        self.assertEqual({row['id'] for row in cases}, set(rubric['cases']))
        self.assertEqual(len(cases), 7)
        self.assertTrue(all(row['kind'] == 'behavior' and row['semantic'] and row['critical'] and row['request'] for row in cases))
