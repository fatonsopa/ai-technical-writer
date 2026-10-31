#!/usr/bin/env python3
"""Check the installed runtime without the development test suite."""
import json
from pathlib import Path
import tempfile

from document_contracts import load_contracts, validate
from validate_document import check, finalize, packet, prepare, review
from validate_skill import validate as validate_package

ROOT = Path(__file__).resolve().parents[1]


def run():
    package = validate_package(ROOT)
    if not package["valid"]:
        return {"passed": False, "findings": package["errors"]}
    if len(load_contracts()["documents"]) != 32:
        return {"passed": False, "findings": ["Missing output contracts."]}
    if validate("# Product\nA note without the required PRD structure.", "prd")["passed"]:
        return {"passed": False, "findings": ["Missing PRD structure was accepted."]}
    with tempfile.TemporaryDirectory(prefix="technical-writer-smoke-") as directory:
        folder = Path(directory)
        request = {"kind": "prd", "operation": "edit", "scope": "title", "sources": [{"id": "request", "text": "Rename the draft to Import preview. This is a title-only exercise."}], "destination": "title.md"}
        (folder / "request.json").write_text(json.dumps(request))
        (folder / "draft.md").write_text("# Import preview\n")
        prepare(folder / "request.json", folder / "session")
        value = packet(folder / "session", folder / "draft.md")
        judgment = {"objective_sha256": value["objective_sha256"], "output_sha256": value["output_sha256"], "scores": [3] * 7, "critical_failures": [], "reasons": ["Authored installation control verifies code flow only."], "requirements": [], "reviewer": {"kind": "current_host_self_review", "identity": "Installation control", "model": None, "method": "Authored deterministic control, not an actual AI judgment or writing-quality observation."}}
        (folder / "review.json").write_text(json.dumps(judgment))
        accepted = review(folder / "session", folder / "review.json")
        finalize(folder / "session", folder / "draft.md", accepted["review"])
        if (folder / "title.md").read_text() != "# Import preview\n":
            return {"passed": False, "findings": ["Checked delivery did not preserve output."]}
    return {"passed": True, "checks": ["Self-contained runtime documentation and resources", "32 output contracts and authored examples", "Invalid PRD structure is rejected", "Output-bound preparation, check, review and delivery"], "limits": "Authored installation controls; not model-performance evidence or target-application testing."}


if __name__ == "__main__":
    result = run()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["passed"] else 1)
