"""One grade contract for task outputs and authored-example audits."""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from document_contracts import load_contracts, validate, validate_grade


def validate_results(results, expected_ids):
    if len(set(expected_ids)) != len(expected_ids) or not isinstance(results, list) or len(results) != len(expected_ids) or not all(isinstance(item, dict) for item in results):
        raise ValueError("Grade IDs do not match requested cases.")
    if {item.get("id") for item in results} != set(expected_ids):
        raise ValueError("Grade IDs do not match requested cases.")
    for item in results:
        validate_grade(item)
    return results


def assess_output(content, case, grade, contracts=None):
    accepted = validate_grade(grade)
    data = contracts or load_contracts()
    kind = case.get("intended_output_kind", case["kind"])
    mechanical = None
    if kind in data["documents"]:
        operation = case["operation"]
        scope = case.get("artifact_scope", "excerpt" if operation == "edit" else "complete")
        if scope not in {"complete", "excerpt", "title"}:
            scope = "excerpt"
        mechanical = validate(content, kind, operation, scope, case.get("context", {}), data)
    failures = list(grade["critical_failures"])
    if mechanical and not mechanical["passed"]:
        failures.extend(mechanical["findings"])
    failures = list(dict.fromkeys(failures))
    return {**grade, "critical_failures": failures, "mechanical": mechanical, "passed": accepted and not failures}
