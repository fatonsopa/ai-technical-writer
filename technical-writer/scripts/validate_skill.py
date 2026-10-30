#!/usr/bin/env python3
"""Static checks for the technical writer skill package; no external packages."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "SKILL.md"


def validate() -> dict[str, object]:
    text = MAIN.read_text(encoding="utf-8")
    errors = []
    if not text.startswith("---\n"):
        errors.append("SKILL.md frontmatter must be first")
    blocks = text.split("---\n", 2)
    header = blocks[1] if len(blocks) > 2 else ""
    if not re.search(r"^name: technical-writer$", header, re.M):
        errors.append("missing or incorrect skill name")
    description = re.search(r"^description:\s*(.+)$", header, re.M)
    if not description or not (1 <= len(description.group(1)) <= 1024):
        errors.append("invalid skill description")
    if len(text.encode()) > 6000:
        errors.append("main SKILL.md exceeds 6KB target")
    referenced = set(re.findall(r"`(references/[a-z-]+\.md|workflows/[a-z-]+\.md)`", text))
    for rel in referenced:
        if not (ROOT / rel).is_file():
            errors.append(f"missing referenced file: {rel}")
    refs = sorted((ROOT / "references").glob("*.md"))
    for ref in refs:
        body = ref.read_text(encoding="utf-8")
        if ref.name not in ("writing-style.md", "visuals.md"):
            if "## Quality check" not in body:
                errors.append(f"missing quality check: {ref.name}")
            if "## Completed example" not in body and "## Skill" not in body and "## Agent definition" not in body:
                errors.append(f"missing example section: {ref.name}")
        if body.count("```") % 2:
            errors.append(f"unbalanced code fences: {ref.name}")
    if text.count("```") % 2:
        errors.append("unbalanced code fences: SKILL.md")
    evals = json.loads((ROOT / "evals/evals.json").read_text(encoding="utf-8"))
    if len(evals.get("evals", [])) < 15:
        errors.append("not enough evaluation cases")
    return {"valid": not errors, "errors": errors, "reference_count": len(refs),
            "eval_count": len(evals["evals"]), "main_bytes": len(text.encode())}


if __name__ == "__main__":
    result = validate()
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["valid"] else 1)
