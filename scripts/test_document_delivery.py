"""Exercise input → draft → checks → review → accepted delivery and failure paths."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import validate_document as delivery
from continuation import MAX_EXTENSIONS
from test_document_contracts import sample
from test_writing_style_contract import style_control


class DocumentDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.request = self.root / "request.json"
        self.session = self.root / "session"
        self.draft = self.root / "draft.md"
        self.target = self.root / "accepted.md"
        self.data = {"kind": "prd", "sources": [{"id": "request", "text": "Preserve identifier 0042. This control's product goals are agreed."}], "destination": "accepted.md", "context": {"required_literals": ["0042"], "discovery": {"status": "ready", "source_ids": ["request"], "decisions": []}}, "requirements": [{"id": "KEEP-ID", "text": "Preserve 0042."}]}
        self.draft.write_text(sample("prd") + "\nIdentifier: 0042.\n")

    def tearDown(self):
        self.temp.cleanup()

    def prepare(self):
        self.request.write_text(json.dumps(self.data))
        result = delivery.prepare(self.request, self.session)
        if self.data.get('operation') == 'rewrite' and self.data.get('scope', 'complete') == 'complete':
            # Actual session transitions using authored evidence, not model behavior.
            phases = {'research': {'summary': 'Fixture source and local type guide inspected.', 'sources': [{'id': 'fixture', 'source': 'Supplied unit fixture', 'finding': 'Retain identifier 0042.', 'provenance': 'supplied'}], 'gaps': []}, 'audit': {'summary': 'Fixture requirements inventoried.', 'findings': [], 'preserve': ['0042'], 'open_questions': []}, 'proposal': {'summary': 'Preserve all fixture requirements.', 'structure': ['Existing type contract'], 'changes': [], 'additions': []}, 'present': {'summary': 'Fixture audit and unchanged requirements presented.', 'visible': True, 'message_reference': 'Authored unit-control handoff; not a live host message.'}}
            for phase, data in phases.items():
                packet = delivery.workflow_packet(self.session)
                record = self.root / (phase + '.json')
                record.write_text(json.dumps({'phase': phase, 'objective_sha256': packet['objective_sha256'], 'packet_sha256': packet['packet_sha256'], 'data': data}))
                delivery.workflow_record(self.session, record)
        return result

    def judgment(self, **updates):
        report = delivery.check(self.session, self.draft)
        data = {"objective_sha256": report["objective_sha256"], "output_sha256": report["output_sha256"], "reviewer": {"kind": "current_host_self_review", "identity": "Authored unit-test control", "model": None, "method": "Test fixture; not a model-performance observation."}, "scores": [3] * 7, "critical_failures": [], "reasons": ["A deliberately authored positive control."], "requirements": [{"id": "KEEP-ID", "accepted": True, "rationale": "The identifier remains 0042.", "source_ids": ["request"]}], **updates}
        data.setdefault("style_review", style_control(report["writing_style"]))
        path = self.root / ("review-" + delivery.digest(data) + ".json")
        path.write_text(json.dumps(data))
        return delivery.review(self.session, path)

    def test_complete_source_bound_document_is_delivered_with_honest_receipt(self):
        self.prepare()
        packet = delivery.packet(self.session, self.draft)
        self.assertEqual(packet["sources"][0]["text"], self.data["sources"][0]["text"])
        self.assertEqual(packet["requirements"][0]["id"], "KEEP-ID")
        result = self.judgment()
        receipt = delivery.finalize(self.session, self.draft, result["review"])
        self.assertEqual(self.target.read_bytes(), self.draft.read_bytes())
        self.assertEqual(receipt["reviewer"]["kind"], "current_host_self_review")
        self.assertEqual(delivery.load(self.session / "delivery.json")["output_sha256"], delivery.digest(self.target.read_bytes()))

    def test_final_message_reports_only_actual_document_validation_and_matches_bytes(self):
        self.prepare()
        result = self.judgment()
        receipt = delivery.finalize(self.session, self.draft, result['review'])
        message = self.session / 'message.md'
        self.assertEqual(message.read_text(), receipt['message'])
        self.assertIn('author self-review', receipt['message'])
        self.assertIn(str(self.target), receipt['message'])
        self.assertTrue(delivery.verify_message(self.session, message)['passed'])
        self.assertNotIn('implementation', receipt['message'])
        self.assertNotIn('tests passed', receipt['message'])
        print(json.dumps({'provenance': {'kind': 'authored_control', 'source': 'Actual finalized receipt and verify_message call, not model quality.'}, 'events': [{'phase': 'verify', 'evidence': json.dumps(delivery.verify_message(self.session, message))}]}))

    def test_changed_message_is_rejected_and_a_corrected_copy_can_pass(self):
        self.prepare()
        result = self.judgment()
        receipt = delivery.finalize(self.session, self.draft, result['review'])
        message = self.session / 'message.md'
        message.write_text(receipt['message'] + 'No target has been set.\n')
        self.assertFalse(delivery.verify_message(self.session, message)['passed'])
        message.write_text(receipt['message'])
        self.assertTrue(delivery.verify_message(self.session, message)['passed'])

    def test_message_verification_rejects_premature_or_stale_delivery(self):
        self.prepare()
        message = self.root / 'message.md'
        message.write_text('Passed.')
        with self.assertRaisesRegex(ValueError, 'Finalize'):
            delivery.verify_message(self.session, message)
        result = self.judgment()
        receipt = delivery.finalize(self.session, self.draft, result['review'])
        message.write_text(receipt['message'])
        self.target.write_text('Newer document.')
        with self.assertRaisesRegex(ValueError, 'changed'):
            delivery.verify_message(self.session, message)

    def test_high_semantic_scores_cannot_override_missing_prd_structure(self):
        self.prepare()
        self.draft.write_text("# Product\n\nIdentifier: 0042.\n")
        result = self.judgment()
        self.assertFalse(result["accepted"])
        with self.assertRaisesRegex(ValueError, "passing checks"):
            delivery.finalize(self.session, self.draft, result["review"])
        self.assertFalse(self.target.exists())

    def test_changed_draft_invalidates_its_accepted_review(self):
        self.prepare()
        result = self.judgment()
        self.draft.write_text(self.draft.read_text() + "\nA later change.\n")
        with self.assertRaisesRegex(ValueError, "exact output bytes"):
            delivery.finalize(self.session, self.draft, result["review"])
        self.assertFalse(self.target.exists())

    def test_missing_or_failed_requirement_blocks_delivery(self):
        self.prepare()
        with self.assertRaisesRegex(ValueError, "every explicit requirement"):
            self.judgment(requirements=[])
        result = self.judgment(requirements=[{"id": "KEEP-ID", "accepted": False, "rationale": "Deliberate failed control.", "source_ids": ["request"]}])
        self.assertFalse(result["accepted"])

    def test_out_of_range_boolean_and_incomplete_scores_are_errors(self):
        self.prepare()
        for scores in ([99] * 7, [True] * 7, [3] * 6, [-1] * 7):
            with self.subTest(scores=scores), self.assertRaises(ValueError):
                self.judgment(scores=scores)

    def test_forged_acceptance_flag_cannot_overrule_failed_scores(self):
        self.prepare()
        result = self.judgment(scores=[1] * 7)
        path = Path(result["review"])
        record = delivery.load(path)
        record["accepted"] = True
        delivery.save(path, record)
        with self.assertRaisesRegex(ValueError, "passing checks"):
            delivery.finalize(self.session, self.draft, path)

    def test_changed_input_and_validator_require_new_session(self):
        source = self.root / "source.md"
        source.write_text("Original facts, including 0042.")
        self.data["sources"] = [{"id": "request", "path": "source.md"}]
        self.prepare()
        source.write_text("Changed facts.")
        with self.assertRaisesRegex(ValueError, "source changed"):
            delivery.check(self.session, self.draft)
        source.write_text("Original facts, including 0042.")
        with patch.object(delivery, "tool_identity", return_value={}):
            with self.assertRaisesRegex(ValueError, "Validator or contract changed"):
                delivery.check(self.session, self.draft)

    def test_newer_destination_content_is_preserved(self):
        self.target.write_text("Original destination.")
        self.data["operation"] = "rewrite"
        self.prepare()
        result = self.judgment()
        self.target.write_text("A newer user edit.")
        with self.assertRaisesRegex(ValueError, "newer user content"):
            delivery.finalize(self.session, self.draft, result["review"])
        self.assertEqual(self.target.read_text(), "A newer user edit.")

    def test_budget_blocks_new_attempts_until_bounded_extension(self):
        self.data["limits"] = {"max_attempts": 1, "max_seconds": 600}
        self.prepare()
        delivery.check(self.session, self.draft)
        self.draft.write_text(self.draft.read_text() + "\nRevised draft.\n")
        with self.assertRaisesRegex(ValueError, "attempt allowance exhausted"):
            delivery.check(self.session, self.draft)
        delivery.extend(self.session, 1, 0, "Validate the scoped draft correction against the same requirements.")
        self.assertTrue(delivery.check(self.session, self.draft)["passed"])

    def test_unknown_reviewer_or_source_cannot_be_accepted(self):
        self.prepare()
        with self.assertRaises(ValueError):
            self.judgment(reviewer={})
        with self.assertRaisesRegex(ValueError, "source reference"):
            self.judgment(requirements=[{"id": "KEEP-ID", "accepted": True, "rationale": "Invalid source control.", "source_ids": ["invented"]}])

    def test_routine_retries_preserve_user_hard_limit_without_new_approval(self):
        self.data['limits'] = {'max_attempts': 1, 'max_seconds': 600}
        self.data['hard_limits'] = {'attempts': 2}
        self.prepare()
        before = delivery.load(self.session / 'state.json')['objective_sha256']
        receipt = delivery.extend(self.session, 1, 0, 'Check the scoped wording correction.')
        self.assertTrue(receipt['extension']['automatic'])
        self.assertEqual(delivery.load(self.session / 'state.json')['objective_sha256'], before)
        with self.assertRaisesRegex(ValueError, 'hard limit'):
            delivery.extend(self.session, 1, 0, 'Check another correction.')
        self.assertEqual(len(delivery.load(self.session / 'state.json')['extensions']), 1)

    def test_routine_retries_stop_at_the_cumulative_ceiling(self):
        self.prepare()
        for index in range(MAX_EXTENSIONS):
            delivery.extend(self.session, 1, 0, f'Check scoped correction {index + 1}.')
        with self.assertRaisesRegex(ValueError, 'ceiling'):
            delivery.extend(self.session, 1, 0, 'Try another correction.')

    def test_crlf_bytes_are_bound_and_delivered_without_normalization(self):
        self.prepare()
        self.draft.write_bytes(self.draft.read_bytes().replace(b"\n", b"\r\n"))
        result = self.judgment()
        delivery.finalize(self.session, self.draft, result["review"])
        self.assertEqual(self.target.read_bytes(), self.draft.read_bytes())

    def test_replacing_an_input_document_keeps_its_frozen_original_for_review(self):
        self.target.write_text("Original product draft: 0042.")
        self.data["sources"] = [{"id": "request", "path": "accepted.md"}]
        self.data["operation"] = "rewrite"
        self.prepare()
        result = self.judgment()
        delivery.finalize(self.session, self.draft, result["review"])
        delivery.finalize(self.session, self.draft, result["review"])
        self.assertEqual(delivery.state_for(self.session)["frozen"]["request"]["sources"][0]["text"], "Original product draft: 0042.")

    def test_title_only_edit_cannot_replace_the_document_with_only_a_title(self):
        self.target.write_text("# Original title\n\nKeep identifier 0042 and this body.\n")
        self.data.update(operation="edit", scope="title")
        self.prepare()
        self.draft.write_text("# New title\n")
        self.assertFalse(delivery.check(self.session, self.draft)["passed"])
        self.draft.write_text("# New title\n\nKeep identifier 0042 and this body.\n")
        self.assertTrue(delivery.check(self.session, self.draft)["passed"])

    def test_excerpt_edit_preserves_bytes_outside_the_selected_lines(self):
        self.target.write_text("# Title\n\nOld paragraph: 0042.\n\nKeep this ending.\n")
        self.data.update(operation="edit", scope="excerpt")
        self.data["context"]["edit_region"] = [3, 3]
        self.prepare()
        self.draft.write_text("# Title\n\nRevised paragraph: 0042.\n\nKeep this ending.\n")
        self.assertTrue(delivery.check(self.session, self.draft)["passed"])
        self.draft.write_text("# Title\n\nRevised paragraph: 0042.\n\nChanged ending.\n")
        self.assertFalse(delivery.check(self.session, self.draft)["passed"])

    def test_review_cannot_overwrite_the_document_being_reviewed(self):
        self.target.write_text("# Original\nIdentifier 0042.")
        self.data.update(operation="review", sources=[{"id": "request", "path": "accepted.md"}])
        with self.assertRaisesRegex(ValueError, "findings separately"):
            self.prepare()

    def test_ready_delivery_does_not_request_more_runtime_for_completed_ai_work(self):
        self.prepare()
        result = self.judgment()
        state = delivery.state_for(self.session)
        with patch.object(delivery.time, "time", return_value=state["started"] + 700):
            delivered = delivery.finalize(self.session, self.draft, result["review"])
        self.assertEqual(delivered["status"], "delivered")
        with self.assertRaisesRegex(ValueError, "already delivered"):
            delivery.extend(self.session, 1, 300, "Unneeded extension.")


if __name__ == "__main__":
    unittest.main()
