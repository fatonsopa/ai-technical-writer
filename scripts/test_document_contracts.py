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
    def test_explicit_agent_formats_reject_mismatch_and_unknown_fields(self):
        text = 'name = "reference_reviewer"\ndescription = "Review references"\ndeveloper_instructions = "Inspect supplied sources."\n'
        context = {'instruction_format': 'codex-toml', 'instruction_version': 'standalone-v1'}
        self.assertTrue(validate(text, 'agent', context=context)['passed'])
        self.assertFalse(validate(text, 'agent')['passed'])
        self.assertFalse(validate(text + 'sandbox_mode = "danger-full-access"\n', 'agent', context=context)['passed'])
        self.assertFalse(validate('name = [', 'agent', context=context)['passed'])
        with self.assertRaisesRegex(ValueError, 'version'):
            validate(text, 'agent', context={**context, 'instruction_version': 'unknown'})
        self.assertTrue(validate('# Project rules\n\nPreserve source evidence.', 'agent', context={'instruction_format':'project'})['passed'])
        self.assertFalse(validate('# Project rules', 'agent', context={'instruction_format':'subagent'})['passed'])

    def test_legacy_issue_requests_use_the_matching_task_contract(self):
        current = load_contracts()
        for name in ("bug", "chore", "decision", "feature", "improvement", "release"):
            legacy, kind = "issue_" + name, "task_" + name
            with self.subTest(kind=kind):
                self.assertEqual(document_contract(current, legacy), document_contract(current, kind))
                self.assertTrue(validate(sample(kind), legacy)["passed"])

        frozen = {"documents": {"issue_bug": {"reference": "references/issue.md"}}}
        self.assertEqual(document_contract(frozen, "issue_bug")["reference"], "references/issue.md")

    def test_task_type_is_metadata_without_a_duplicate_text_field(self):
        for name in ("Bug", "Chore", "Decision", "Feature", "Improvement", "Release"):
            kind = "task_" + name.lower()
            with self.subTest(kind=kind):
                self.assertEqual(document_contract(load_contracts(), kind)["task_type"], name)
                text = sample(kind)
                self.assertTrue(validate(text, kind)["passed"])
                duplicated = text.replace("# Example document\n", "# Example document\n\nType: " + name + "\n", 1)
                self.assertIn("Keep task type in tracker metadata, outside the task text.", validate(duplicated, kind)["findings"])

    def test_quoted_type_literals_are_preserved_as_task_evidence(self):
        original = sample("task_bug")
        quoted = "```text\nType: Bug\n```\n"
        for text in (original + "\n" + quoted, original.replace("## Description", quoted + "\n## Description", 1)):
            with self.subTest(text=text):
                self.assertTrue(validate(text, "task_bug")["passed"])

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


class CoverageResolutionTests(unittest.TestCase):
    """W03: coverage rows resolve against the declared source in both directions."""
    SOURCE = '# Spec\n\n### WEB-08: Clear\n\nText.\n\n### WEB-09: Batches\n\nText.\n'
    PLAN = '# Plan\n\n## Requirement coverage\n\n| Requirement | Implementation area | Verification |\n| --- | --- | --- |\n| WEB-08 | Clear branch | T13 |\n| WEB-09 | Batch coordinator | T14–T16 |\n'

    def findings(self, plan, source=SOURCE):
        from document_contracts import coverage_errors
        return coverage_errors(plan, {'source': 'spec.md', 'revision': 'rev-1', 'source_text': source})

    def test_valid_rows_pass_and_a_displaced_id_reports_row_revision_lost_coverage_and_correction(self):
        self.assertEqual(self.findings(self.PLAN), [])
        found = self.findings(self.PLAN.replace('| WEB-09 |', '| WEB-999 |'))
        self.assertEqual(len(found), 2)
        self.assertRegex(found[0], r'line 8 .*WEB-999.*spec.md at rev-1 does not declare.*likely replaced WEB-09')
        self.assertRegex(found[1], r'Requirement WEB-09 .*no coverage row')

    def test_unavailable_source_is_reported_separately(self):
        self.assertEqual(self.findings(self.PLAN, source=None), ['Coverage source unavailable: spec.md (rev-1). Its citations were not checked; supply the source before relying on coverage.'])

    def test_justified_safeguard_is_eligible_and_an_unjustified_one_is_not(self):
        plan = self.PLAN + '| Safeguard: keep audit rows | Journal retention | Required by the data policy |\n'
        self.assertEqual(self.findings(plan), [])
        self.assertRegex(self.findings(self.PLAN + '| Safeguard | | |\n')[0], 'safeguard without its justification')

    def test_project_without_ids_resolves_exact_section_links(self):
        source = '# Spec\n\n## Save a website\n\nText.\n'
        plan = '# Plan\n\n## Requirement coverage\n\n| Requirement | Check |\n| --- | --- |\n| [Save](spec.md#save-a-website) | T09 |\n'
        self.assertEqual(self.findings(plan, source), [])
        self.assertRegex(self.findings(plan.replace('#save-a-website', '#save-websites'), source)[0], 'links to section #save-websites')
