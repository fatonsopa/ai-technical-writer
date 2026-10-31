"""Portable evaluation, frozen evidence, invalid outputs and bounded continuation."""
import importlib.util
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "evals"))
import evaluation
from document_contracts import digest
from grades import assess_output
from test_document_contracts import sample
import audit_examples


class EvaluationSessionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.session = self.root / "session"
        self.fixture = self.root / "input.md"
        self.fixture.write_text("The imported identifier is 0042. Goals and owner remain undecided.")
        self.case = {"id": "new-prd", "kind": "prd", "operation": "create", "fixture": "input.md", "request": "Write the PRD using only the supplied facts.", "references": ["references/product_requirements_document.md"], "expected_properties": ["Keep 0042 and unknown goals."], "context": {"required_literals": ["0042"]}}

    def tearDown(self):
        self.temp.cleanup()

    def prepare(self, handoffs=2, selected=None):
        return evaluation.prepare(ROOT, selected or [self.case], self.session, handoffs, 600, case_root=self.root, host="codex", model=None)

    def submit(self, phase, data, case=None):
        packet = evaluation.packet(self.session, case or self.case["id"], phase)
        return evaluation.submit(self.session, {"case_id": packet["case_id"], "phase": phase, "packet_sha256": packet["packet_sha256"], "data": data})

    def generate(self, content=None):
        return self.submit("generate", {"content": content if content is not None else sample("prd") + "\nIdentifier 0042.\n", "references_read": ["references/product_requirements_document.md"]})

    def judgment(self, **extra):
        return {"id": self.case["id"], "scores": [3] * 7, "critical_failures": [], "reasons": ["Authored test control; not a real model judgment."], "reviewer": {"kind": "current_host_self_review", "identity": "Unit control", "model": None, "method": "Deterministic harness test."}, **extra}

    def test_native_input_output_round_trip_requires_both_checks(self):
        self.prepare()
        packet = evaluation.packet(self.session, self.case["id"], "generate")
        self.assertNotIn("case", packet)
        self.assertNotIn("rubric", packet)
        self.assertEqual(packet["source"], self.fixture.read_text())
        pending = self.generate()
        self.assertFalse(pending["accepted"])
        self.assertEqual(pending["pending_review"], 1)
        result = self.submit("grade", self.judgment())
        self.assertTrue(result["accepted"])
        self.assertEqual(result["task_success_percent"], 100)
        self.assertEqual(result["coverage_percent"], 100)
        self.assertIsNone(result["model"])

    def test_structurally_invalid_output_fails_without_a_model_override(self):
        self.prepare()
        result = self.generate("# Product\nOnly identifier 0042.")
        self.assertFalse(result["accepted"])
        self.assertEqual(result["task_success_percent"], 0)
        self.assertEqual(result["coverage_percent"], 100)
        self.assertGreater(result["critical_failures"], 0)
        with self.assertRaisesRegex(ValueError, "not awaiting"):
            evaluation.packet(self.session, self.case["id"], "grade")

    def test_malformed_task_outputs_are_failures_not_coverage_gaps(self):
        self.prepare()
        result = self.submit("generate", {"content": None, "references_read": []})
        self.assertEqual((result["evaluated_attempts"], result["planned_attempts"]), (1, 1))
        self.assertEqual(result["task_success_percent"], 0)

    def test_out_of_range_scores_remain_unaccepted_and_require_new_allowance(self):
        self.prepare()
        self.generate()
        with self.assertRaisesRegex(ValueError, "0–3"):
            self.submit("grade", self.judgment(scores=[99] * 7))
        self.assertEqual(len(list((self.session / "attempts").glob("*.json"))), 2)
        with self.assertRaisesRegex(ValueError, "allowance exhausted"):
            evaluation.packet(self.session, self.case["id"], "grade")
        evaluation.extend(self.session, 1, 0, "User approved one additional judgment.")
        self.assertTrue(self.submit("grade", self.judgment())["accepted"])

    def test_unknown_and_critical_reviews_never_accept(self):
        self.prepare()
        self.generate()
        result = self.submit("grade", self.judgment(critical_failures=["Invented approval."]))
        self.assertFalse(result["accepted"])
        self.assertEqual(result["task_success_percent"], 0)

    def test_source_facts_and_executable_changes_are_detected(self):
        self.prepare()
        self.fixture.write_text("Facts changed after preparation.")
        with self.assertRaisesRegex(ValueError, "Source fixture changed"):
            evaluation.read_state(self.session)
        copied = self.root / "skill"
        shutil.copytree(ROOT, copied, ignore=shutil.ignore_patterns("__pycache__", "runs"))
        before = evaluation.fingerprint(copied)
        (copied / "scripts/plain_words.py").write_text('raise RuntimeError("changed helper")\n')
        self.assertNotEqual(before, evaluation.fingerprint(copied))

    def test_coverage_excludes_pending_and_reports_unevaluated_cases(self):
        second = {**self.case, "id": "second-prd"}
        self.prepare(selected=[self.case, second])
        self.generate()
        result = self.submit("grade", self.judgment())
        self.assertFalse(result["accepted"])
        self.assertEqual(result["task_success_percent"], 100)
        self.assertEqual(result["coverage_percent"], 50)

    def test_changed_output_cannot_keep_a_passing_status(self):
        self.prepare()
        self.generate()
        self.submit("grade", self.judgment())
        state = evaluation.read_state(self.session)
        state["records"][self.case["id"]]["content"] += " An unreviewed claim."
        evaluation.save(self.session / "state.json", state)
        with self.assertRaisesRegex(ValueError, "task output changed"):
            evaluation.read_state(self.session)

    def test_case_or_objective_changes_require_new_evidence(self):
        self.prepare()
        state = evaluation.read_state(self.session)
        state["bundle"]["cases"][0]["expected_properties"] = ["Weakened criterion."]
        evaluation.save(self.session / "state.json", state)
        with self.assertRaisesRegex(ValueError, "Frozen evaluation inputs changed"):
            evaluation.read_state(self.session)

    def test_target_is_part_of_the_frozen_input_bundle(self):
        self.prepare()
        state = evaluation.read_state(self.session)
        self.assertEqual(state["bundle"]["target_success_percent"], 100)

    def test_target_only_change_cannot_weaken_the_frozen_objective(self):
        self.prepare()
        state = evaluation.read_state(self.session)
        state["target_success_percent"] = 0
        evaluation.save(self.session / "state.json", state)
        with self.assertRaisesRegex(ValueError, "Frozen evaluation target changed"):
            evaluation.read_state(self.session)

    def test_bounded_external_call_budget_is_shared_and_counts_failures(self):
        budget = evaluation.CallBudget(2, 10)
        self.assertGreater(budget.reserve(), 0)
        self.assertGreater(budget.reserve(), 0)
        with self.assertRaises(ValueError):
            budget.reserve()
        self.assertEqual(budget.report()["cli_invocations"], 2)

    def test_authored_example_scores_use_the_same_strict_contract(self):
        packet = audit_examples.make_packet([ROOT / "examples/issue.md"])
        response = {"packet_sha256": packet["packet_sha256"], "reviewer": self.judgment()["reviewer"], "results": [{"id": "issue", "scores": [99] * 7, "critical_failures": [], "reasons": ["Invalid score control."]}]}
        with self.assertRaisesRegex(ValueError, "0–3"):
            audit_examples.assess_packet(packet, response)
        response["results"][0]["scores"] = [3] * 7
        self.assertTrue(audit_examples.assess_packet(packet, response)["accepted"])

    def test_metadata_does_not_claim_an_unknown_model_or_independence(self):
        self.prepare()
        self.generate()
        self.submit("grade", self.judgment())
        record = evaluation.read_state(self.session)["records"][self.case["id"]]
        self.assertEqual(record["reviewer"]["kind"], "current_host_self_review")
        self.assertIsNone(record["reviewer"]["model"])


if __name__ == "__main__":
    unittest.main()
