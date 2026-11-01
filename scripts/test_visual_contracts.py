"""Embedded visual checks and renderer wiring, separate from model/diagram quality."""
from pathlib import Path
import os
import subprocess
import tempfile
import unittest
from unittest.mock import patch

from document_contracts import validate
from test_document_contracts import sample
from visual_contracts import check_syntax, render_mermaid


def sequence():
    return "### Save a category change\n\nA proposed commit/response view.\n\n```mermaid\nsequenceDiagram\n    accTitle: Save confirmation\n    accDescr: The browser confirms success after commit.\n    UI->>DB: Save\n    DB-->>UI: Committed result\n```\n\nThe response confirms the commit.\n\n- UI: The browser submits the change.\n- DB: The database commits it before responding.\n"


class VisualContractTests(unittest.TestCase):
    def selection(self, notation="sequence"):
        return {"visuals": [{"heading": "Save a category change", "notation": notation, "reason": "Explain commit confirmation."}]}

    def test_selected_views_are_enforced_inside_a_complete_hld(self):
        text = sample("hld") + "\n" + sequence()
        self.assertTrue(validate(text, "hld", context=self.selection())["passed"])
        for changed in (text.replace("### Save a category change", "### A different scenario"), text.replace("sequenceDiagram", "flowchart LR")):
            self.assertFalse(validate(changed, "hld", context=self.selection())["passed"])

    def test_one_accessible_diagram_cannot_cover_a_second_missing_description(self):
        text = sample("sdd") + "\n" + sequence() + "\n" + sequence().replace("accDescr: The browser confirms success after commit.", "accDescr:")
        self.assertFalse(validate(text, "sdd")["passed"])

    def test_a_quoted_diagram_is_not_an_embedded_visual(self):
        text = sample("hld") + "\n### Save a category change\n\n````md\n" + sequence() + "\n````\n"
        self.assertFalse(validate(text, "hld", context=self.selection())["passed"])

    def test_empty_visual_selection_does_not_force_diagrams_on_simple_documents(self):
        self.assertTrue(validate(sample("prd"), "prd", context={"visuals": []})["passed"])
        self.assertTrue(validate(sample("plan"), "plan")["passed"])

    def test_explanation_and_element_key_are_required_per_diagram(self):
        text = sequence()
        self.assertFalse(validate(text.replace("The response confirms the commit.", ""), "visual")["passed"])
        self.assertFalse(validate(text[:text.index("- UI:")], "visual")["passed"])
        second = sequence().replace("The response confirms the commit.", "").split("- UI:")[0]
        self.assertFalse(validate(text + "\n" + second, "visual")["passed"])

    def test_selected_images_need_alternative_text_and_unknown_notations_fail(self):
        text = sample("hld") + "\n### Save a category change\n\n![Editable wireflow of save feedback](save.svg)\n"
        self.assertTrue(validate(text, "hld", context=self.selection("image"))["passed"])
        self.assertFalse(validate(text.replace("Editable wireflow of save feedback", ""), "hld", context=self.selection("image"))["passed"])
        self.assertFalse(validate(text, "hld", context=self.selection("invented"))["passed"])

    def test_tilde_fences_are_checked_and_unclosed_fences_fail(self):
        text = sequence().replace("```", "~~~")
        self.assertTrue(validate(text, "visual")["passed"])
        self.assertFalse(validate(text.rsplit("~~~", 1)[0], "visual")["passed"])

    def test_unavailable_renderer_is_reported_without_a_render_claim(self):
        with tempfile.TemporaryDirectory() as folder, patch("visual_contracts.shutil.which", return_value=None):
            with self.assertRaisesRegex(ValueError, "not run"):
                render_mermaid(sequence(), Path(folder) / "rendered")
            self.assertFalse((Path(folder) / "rendered").exists())

    def test_missing_parser_is_distinct_from_passed_syntax(self):
        self.assertEqual(check_syntax(sequence(), None)["status"], "not_run")

    def test_documents_without_mermaid_do_not_require_parser_dependencies(self):
        with patch("visual_contracts.shutil.which", return_value=None):
            self.assertEqual(check_syntax("A small task needs no diagram.", None)["status"], "not_applicable")

    def test_parser_failure_cannot_be_overruled_by_a_success_flag(self):
        with patch("visual_contracts.shutil.which", return_value="/node"), patch("visual_contracts.subprocess.run", return_value=subprocess.CompletedProcess([], 1, '{"passed":true,"version":"test"}', "")):
            self.assertEqual(check_syntax(sequence(), "/test-tools")["status"], "failed")

    @unittest.skipUnless(os.environ.get("TECHNICAL_WRITER_MERMAID_MODULE_ROOT"), "Mermaid integration dependencies are not configured.")
    def test_real_parser_rejects_the_reported_semicolon_regression(self):
        text = sequence().replace("DB-->>UI: Committed result", "Note over UI: Outcome uncertain; bulk recovery requires reconciliation")
        report = check_syntax(text, os.environ["TECHNICAL_WRITER_MERMAID_MODULE_ROOT"])
        self.assertEqual(report["status"], "failed")
        self.assertTrue(any("Parse error" in row.get("error", "") for row in report["results"]))

    def test_renderer_wiring_requires_success_and_an_output_file(self):
        # Authored process control, not an actual Mermaid syntax/rendering observation.
        def render(argv, **kwargs):
            Path(argv[-1]).write_text('<svg xmlns="http://www.w3.org/2000/svg"/>')
            return subprocess.CompletedProcess(argv, 0, "", "")
        with tempfile.TemporaryDirectory() as folder, patch("visual_contracts.shutil.which", return_value="/renderer with spaces"), patch("visual_contracts.subprocess.run", side_effect=render) as call:
            result = render_mermaid(sequence(), Path(folder) / "rendered")
            self.assertEqual(len(result), 1)
            self.assertEqual(call.call_args.args[0][0], "/renderer with spaces")
        with tempfile.TemporaryDirectory() as folder, patch("visual_contracts.shutil.which", return_value="/renderer"), patch("visual_contracts.subprocess.run", return_value=subprocess.CompletedProcess([], 1, "", "Syntax error")):
            with self.assertRaisesRegex(ValueError, "rendering failed"):
                render_mermaid(sequence(), Path(folder) / "failed")
