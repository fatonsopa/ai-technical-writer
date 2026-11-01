"""Check observable document acceptance, including deliberately misleading outputs."""
from copy import deepcopy
import json
from pathlib import Path
import re
import unittest

from document_contracts import document_contract, headings, load_contracts, validate

ROOT = Path(__file__).resolve().parents[1]


def sample(kind):
    contract = document_contract(load_contracts(), kind)
    mode = contract.get("format", "document")
    if mode == "frontmatter":
        return "---\nname: example-skill\ndescription: Explain supplied data.\n---\n\nRead the supplied data and return supported findings.\n"
    if mode == "requirement":
        return "### REQ-01: Preserve identifiers\nStatus/source: Agreed in the supplied request.\nStatement: Preserve the identifier as supplied.\nVerification: Compare the returned identifier with the input.\n"
    if mode == "visual":
        return "### Request flow\n\nThe supplied example shows a request.\n\n```mermaid\nflowchart LR\naccTitle: Request flow\naccDescr: A caller sends a request to a service.\nA --> B\n```\n\nThe service receives the request.\n\n- A: The caller sends the request.\n- B: The service receives it.\n"
    rows = ["# Example document", ""]
    if contract.get("task_type"):
        rows += ["Type: " + contract["task_type"], ""]
    for rule in contract.get("sections", []):
        if "alternatives" in rule:
            rules = rule["alternatives"][0]
        else:
            rules = [rule]
        for item in rules:
            if not item.get("required", True) or item.get("when"):
                continue
            title = item["labels"][0] if "labels" in item else "Recommended option (A)"
            rows += ["## " + title, "", "A source-supported explanation for this section.", ""]
            for child in item.get("children", []):
                rows += ["### Option A: Keep the current design", "", "Preserve the known behavior.", "", "### Option B: Change the design", "", "Use the proposed alternative with its stated cost.", ""]
    return "\n".join(rows)


class DocumentContractTests(unittest.TestCase):
    def test_catalog_and_contracts_cover_the_same_outputs(self):
        catalog = json.loads((ROOT / "evals/catalog.json").read_text())
        self.assertEqual(set(load_contracts()["documents"]), {item["id"] for item in catalog["output_kinds"]})

    def test_every_type_accepts_a_structurally_complete_example(self):
        for kind in load_contracts()["documents"]:
            with self.subTest(kind=kind):
                result = validate(sample(kind), kind)
                self.assertTrue(result["passed"], result["findings"])
                self.assertTrue(result["semantic_review_required"])

    def test_removing_each_required_heading_fails_independently(self):
        for kind in load_contracts()["documents"]:
            text = sample(kind)
            required = [node for node in headings(text) if node["level"] == 2]
            for node in required:
                with self.subTest(kind=kind, section=node["title"]):
                    changed = text.replace("## " + node["title"], node["title"], 1)
                    self.assertFalse(validate(changed, kind)["passed"])

    def test_missing_prd_structure_does_not_defer_to_a_model(self):
        result = validate("# Product\n\nA note with no PRD sections.", "prd")
        self.assertFalse(result["passed"])
        self.assertTrue(any("Problem and users" in finding for finding in result["findings"]))

    def test_code_fences_cannot_supply_required_headings(self):
        text = "# Product\n\n```md\n" + sample("prd") + "\n```\n"
        self.assertFalse(validate(text, "prd")["passed"])

    def test_empty_placeholder_and_duplicate_sections_fail(self):
        text = sample("prd")
        for body in ("", "[Current difficulty, affected users, evidence]", "TODO"):
            changed = text.replace("A source-supported explanation for this section.", body, 1)
            self.assertFalse(validate(changed, "prd")["passed"])
        self.assertFalse(validate(text + "\n## Problem and users\nDuplicated content.\n", "prd")["passed"])

    def test_hierarchy_and_nested_options_are_enforced(self):
        text = sample("decision")
        for changed in (text.replace("### Option B:", "#### Option B:"), text.replace("### Option B:", "Option B:"), text.replace("Recommended option (A)", "Recommended option (Z)")):
            self.assertFalse(validate(changed, "decision")["passed"])

    def test_declared_order_is_enforced(self):
        text = sample("decision")
        first, second = text.split("## Recommended option (A)")
        reordered = "# Decision\n\n## Recommended option (A)" + second + "\n" + first.replace("# Example document", "")
        self.assertFalse(validate(reordered, "decision")["passed"])

    def test_title_edits_and_reviews_do_not_acquire_full_templates(self):
        self.assertTrue(validate("# New title", "prd", "edit", "title")["passed"])
        self.assertTrue(validate("The goal has no source or acceptance condition.", "prd", "review")["passed"])
        self.assertFalse(validate("", "prd", "edit", "title")["passed"])

    def test_required_literals_and_ids_are_exact(self):
        context = {"required_literals": ["0042", "15 minutes"], "requirement_ids": ["IMP-01"]}
        self.assertFalse(validate(sample("prd") + "42, 15 minutes, IMP-010", "prd", context=context)["passed"])
        self.assertTrue(validate(sample("prd") + "0042, 15 minutes, IMP-01", "prd", context=context)["passed"])

    def test_conditional_sections_and_split_sections(self):
        text = sample("ts")
        self.assertTrue(validate(text, "ts")["passed"])
        self.assertFalse(validate(text, "ts", context={"open_prerequisites": True})["passed"])
        text = sample("tp").replace("## Entry and exit criteria\n\nA source-supported explanation for this section.", "## Entry criteria\nInputs are available.\n## Exit criteria\nAll required checks pass.")
        self.assertTrue(validate(text, "tp")["passed"])

    def test_frontmatter_must_have_real_string_fields_and_valid_yaml(self):
        for text in ("# Instructions", "---\nname: invalid name\ndescription: true\n---\nBody.", "---\nname: [broken\ndescription: Text\n---\nBody."):
            self.assertFalse(validate(text, "skill")["passed"])


if __name__ == "__main__":
    unittest.main()
