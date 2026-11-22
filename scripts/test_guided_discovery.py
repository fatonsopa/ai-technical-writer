"""Readiness controls; these tests do not simulate user answers or prove elicitation quality."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import validate_document as delivery
from document_contracts import validate
from test_document_contracts import sample
from test_visual_contracts import sequence


class GuidedDiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.record = {"status": "ready", "source_ids": ["brief"], "decisions": []}
        self.request = {"kind": "hld", "sources": [{"id": "brief", "text": "The existing architecture and required behavior are supplied."}], "destination": "architecture.md", "context": {"discovery": self.record}}

    def tearDown(self):
        self.temp.cleanup()

    def prepare(self):
        path = self.root / "request.json"
        path.write_text(json.dumps(self.request))
        return delivery.prepare(path, self.root / "session")

    def decision(self):
        return {"id": "D-01", "question": "Who may change categories?", "status": "open", "blocking": True, "answer": "", "source_ids": []}

    def test_complete_planning_delivery_needs_record_but_not_a_question(self):
        for kind in ("prd", "sdd", "hld", "lld", "plan"):
            self.request.update(kind=kind, context={})
            with self.subTest(kind=kind), self.assertRaisesRegex(ValueError, "discovery record"):
                self.prepare()
        self.request.update(kind="hld", context={"discovery": self.record, "visuals": []})
        self.prepare()
        draft = self.root / "draft.md"
        draft.write_text(sample("hld"))
        self.assertTrue(delivery.check(self.root / "session", draft)["passed"])
        guidance = delivery.state_for(self.root / "session")["frozen"]["guidance"]
        self.assertIn("workflows/discover.md", guidance)
        self.assertNotIn("references/visuals.md", guidance)

    def test_a_known_unanswered_material_choice_cannot_be_ready(self):
        self.record["decisions"] = [self.decision()]
        with self.assertRaisesRegex(ValueError, "unresolved blocking decision"):
            self.prepare()
        self.assertFalse((self.root / "session").exists())

    def test_a_claimed_answer_needs_actual_text_and_captured_source_ids(self):
        decision = self.decision()
        decision.update(status="resolved", source_ids=["brief"])
        self.record["decisions"] = [decision]
        with self.assertRaisesRegex(ValueError, "actual answer"):
            self.prepare()
        decision.update(answer="Only administrators.", source_ids=["unrecorded-chat"])
        with self.assertRaisesRegex(ValueError, "captured source IDs"):
            self.prepare()

    def test_a_draft_exposes_the_unresolved_choice_and_cannot_hide_its_status_in_code(self):
        self.record.update(status="draft", decisions=[self.decision()])
        self.prepare()
        draft = self.root / "draft.md"
        text = sample("hld")
        for prefix, suffix in (("", "\nD-01: Permission policy remains open."), ("Status: Draft\n", ""), ("```md\nStatus: Draft\n```\n", "\nD-01: Open.")):
            result = validate(prefix + text + suffix, "hld", context={"discovery": self.record})
            self.assertFalse(result["passed"], result)
        draft.write_text("# Architecture\nStatus: Draft\n" + text.replace("# Example document", "") + "\nD-01: Permission policy remains open; affected behavior is provisional.\n")
        self.assertTrue(delivery.check(self.root / "session", draft)["passed"])

    def test_resolved_choices_are_bound_to_the_captured_answer(self):
        answer = self.root / "answer.md"
        answer.write_text("The user chose administrator-only category changes.")
        self.request["sources"].append({"id": "answer", "path": "answer.md"})
        decision = self.decision()
        decision.update(status="resolved", answer="Only administrators.", source_ids=["answer"])
        self.record.update(source_ids=["brief", "answer"], decisions=[decision])
        self.prepare()
        answer.write_text("The user changed the permission requirement.")
        with self.assertRaisesRegex(ValueError, "source changed"):
            delivery.state_for(self.root / "session")

    def test_small_edits_and_reviews_do_not_acquire_discovery_forms(self):
        self.request.update(operation="edit", scope="title", context={})
        self.prepare()
        draft = self.root / "title.md"
        draft.write_text("# A clearer architecture title\n")
        self.assertTrue(delivery.check(self.root / "session", draft)["passed"])
        self.assertTrue(validate("A source conflict remains unresolved.", "hld", "review")["passed"])

    def test_malformed_decisions_do_not_become_ready_by_truthy_values(self):
        self.record["decisions"] = [self.decision()]
        self.record["decisions"][0]["blocking"] = "false"
        with self.assertRaisesRegex(ValueError, "boolean blocking"):
            self.prepare()
        self.record["decisions"][0]["blocking"] = False
        self.record["decisions"][0]["status"] = ["resolved"]
        with self.assertRaisesRegex(ValueError, "open, resolved"):
            self.prepare()

    def test_ready_delivery_checks_embedded_syntax_instead_of_trusting_metadata(self):
        self.request["context"]["visuals"] = [{"heading": "Save a category change", "notation": "sequence", "reason": "Show confirmation order."}]
        self.prepare()
        draft = self.root / "draft.md"
        draft.write_text(sample("hld") + "\n" + sequence())
        with patch.object(delivery, "check_syntax", return_value={"status": "not_run"}):
            self.assertFalse(delivery.check(self.root / "session", draft)["passed"])
        with patch.object(delivery, "check_syntax", return_value={"status": "passed", "version": "authored test control"}):
            report = delivery.check(self.root / "session", draft)
            self.assertFalse(report["passed"])
            self.assertTrue(any("visible title, subtitle and symbol legend" in item for item in report["findings"]))
        self.assertIn("references/visuals.md", delivery.state_for(self.root / "session")["frozen"]["guidance"])


class MaterialTopicTests(unittest.TestCase):
    """W32: the product route derives its permission topic from the format, not the writer's list."""

    def prd(self, status_line, extra=''):
        from test_document_contracts import sample
        return sample('prd').replace('# Example document', '# Customer report downloads\n\n' + status_line, 1) + extra

    def record(self, status, decisions):
        return {'status': status, 'source_ids': ['brief'], 'decisions': decisions}

    def test_omitted_permission_topic_is_located_and_an_open_draft_passes_as_draft(self):
        from document_contracts import validate
        omitted = validate(self.prd('Status: Draft'), 'prd', context={'discovery': self.record('draft', [])})
        self.assertIn("Material topic 'permissions' is missing from discovery; it affects Scope and capabilities.", ' '.join(omitted['findings']))
        open_row = {'id': 'OWN-1', 'topic': 'permissions', 'question': 'Do customers download reports for themselves or for their whole organization?', 'status': 'open', 'blocking': True, 'answer': '', 'source_ids': []}
        draft = validate(self.prd('Status: Draft', '\nOpen decision OWN-1: report ownership.\n'), 'prd', context={'discovery': self.record('draft', [open_row])})
        self.assertTrue(draft['passed'], draft['findings'])
        ready = validate(self.prd('Status: Ready'), 'prd', context={'discovery': self.record('ready', [open_row])})
        self.assertTrue(any('prevents ready delivery: OWN-1' in f for f in ready['findings']))
        provisional = {**open_row, 'status': 'provisional', 'blocking': False, 'answer': 'Proposal: individual reports only.'}
        self.assertTrue(any('lacks authority' in f for f in validate(self.prd('Status: Ready'), 'prd', context={'discovery': self.record('ready', [provisional])})['findings']))

    def test_title_scope_and_older_records_without_topics_keep_their_route(self):
        from document_contracts import validate
        self.assertFalse(any('Material topic' in f for f in validate('# Customer report downloads\n', 'prd', scope='title', context={'discovery': self.record('draft', [])})['findings']))
