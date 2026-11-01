"""Inspect embedded visuals; optional Mermaid rendering is a separate check."""
import argparse
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile

# Notation identifiers, not a claim that every construct has been syntax-checked.
MERMAID_TYPES = {
    "flowchart": "flowchart", "graph": "flowchart", "sequenceDiagram": "sequence",
    "stateDiagram-v2": "state", "stateDiagram": "state", "erDiagram": "erd",
    "classDiagram": "class", "C4Context": "context", "C4Container": "container",
    "C4Component": "component", "C4Dynamic": "dynamic", "C4Deployment": "deployment",
    "journey": "journey", "gantt": "gantt", "pie": "chart", "xychart-beta": "chart",
    "mindmap": "mindmap", "timeline": "timeline", "requirementDiagram": "requirements",
    "block-beta": "block", "architecture-beta": "deployment", "sankey-beta": "chart",
    "quadrantChart": "chart", "gitGraph": "git", "packet-beta": "packet",
    "kanban": "kanban", "zenuml": "sequence",
}


def diagram_blocks(text, languages=("mermaid", "dot", "plantuml")):
    blocks, opened, body = [], None, []
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if opened:
            if marker and marker[1][0] == opened[0] and len(marker[1]) >= opened[1] and not marker[2].strip():
                if opened[2] in languages:
                    blocks.append({"language": opened[2], "line": opened[3], "end_line": number, "body": "\n".join(body)})
                opened, body = None, []
            else:
                body.append(line)
        elif marker:
            opened = marker[1][0], len(marker[1]), marker[2].strip(), number
    return blocks, bool(opened)


def embedded_source_errors(section, source):
    """The editable copy follows the diagram's table and matches its frozen source."""
    blocks, _ = diagram_blocks(section, languages=("text",))
    matching = [block for block in blocks if block["body"] == source.replace("\r\n", "\n").rstrip("\n")]
    if len(matching) != 1:
        return ["Embed the matching Mermaid source once in a text code block below the diagram's explanation table."]
    before = "\n".join(section.splitlines()[:matching[0]["line"] - 1])
    image = re.search(r"!\[[^\]\n]+\]\([^)]+\.svg\)", before)
    prose = before[image.end():] if image else ""
    # Code samples cannot impersonate an explanation table.
    prose = re.sub(r"(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$", "", prose)
    table = re.search(r"(?m)^\|[^\n]+\|[ \t]*\n\|[ \t:|\-]+\|[ \t]*\n\|[^\n]+\|", prose)
    return [] if table else ["Place the embedded Mermaid source after the SVG and its explanation table."]


def visual_errors(text, nodes, expected=None):
    errors = []
    blocks, unclosed = diagram_blocks(text)
    if unclosed:
        errors.append("Unclosed fenced block in document.")
    for block in blocks:
        preceding = [node for node in nodes if node["line"] < block["line"]]
        level = preceding[-1]["level"] if preceding else 1
        boundaries = [node["line"] - 1 for node in nodes if node["line"] > block["end_line"] and node["level"] <= level]
        boundaries += [other["line"] - 1 for other in blocks if other["line"] > block["end_line"]]
        end = min(boundaries, default=len(text.splitlines()))
        following = "\n".join(text.splitlines()[block["end_line"]:end])
        # Explanations inside another code example cannot satisfy this diagram's explanations.
        following = re.sub(r"(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$", "", following)
        if not re.search(r"(?m)^(?!\s*(?:[|#*-]|\d+[.)]\s))\s*[A-Za-z]", following):
            errors.append(f"Missing overview after diagram at line {block['line']}.")
        if not re.search(r"(?m)^\s*(?:\|[^\n]+\||[-*]\s+\S|\d+[.)]\s+\S)", following):
            errors.append(f"Missing element explanations after diagram at line {block['line']}.")
        if block["language"] != "mermaid":
            continue
        body = block["body"]
        for label in ("accTitle", "accDescr"):
            # Also allow Mermaid's multiline accessible description form.
            suffix = r"[ \t]*:[ \t]*\S" if label == "accTitle" else r"[ \t]*(?::[ \t]*\S|\{\s*[^\s}])"
            if not re.search(r"(?m)^[ \t]*" + label + suffix, body):
                errors.append(f"Mermaid at line {block['line']} needs a nonempty {label}.")
    if expected is None:
        return errors
    if not isinstance(expected, list):
        return errors + ["Visual selections must be a list."]
    seen = set()
    for row in expected:
        if not isinstance(row, dict) or set(row) != {"heading", "notation", "reason"} or any(not isinstance(v, str) or not v.strip() for v in row.values()):
            errors.append("Each selected visual needs heading, notation and reason.")
            continue
        if row["notation"] not in set(MERMAID_TYPES.values()) | {"image", "flowchart_svg", "diagram_svg", "dot", "plantuml"}:
            errors.append("Unknown selected visual notation: " + row["notation"])
        key = row["heading"].casefold()
        if key in seen:
            errors.append("Selected visual headings must be unique.")
        seen.add(key)
        matches = [node for node in nodes if node["title"].casefold() == key]
        if len(matches) != 1:
            errors.append("Expected one selected visual heading: " + row["heading"])
            continue
        section = matches[0]["body"]
        section_blocks, _ = diagram_blocks(section)
        notations = set()
        for block in section_blocks:
            if block["language"] == "mermaid":
                # Search line starts so inline labels cannot impersonate a notation declaration.
                declaration = re.search(r"(?m)^\s*(" + "|".join(map(re.escape, MERMAID_TYPES)) + r")\b", block["body"])
                if declaration:
                    notations.add(MERMAID_TYPES[declaration[1]])
            else:
                notations.add(block["language"])
        if re.search(r"!\[[^\]\n]+\]\([^)]+\)", section):
            notations.add("image")
        if re.search(r"!\[[^\]\n]+\]\([^)]+\.svg\)", section):
            notations.update({"flowchart_svg", "diagram_svg"})
        if row["notation"] in {"flowchart_svg", "diagram_svg"}:
            match = re.search(r"!\[[^\]\n]+\]\([^)]+\.svg\)", section)
            following = section[match.end():] if match else ""
            following = re.sub(r"(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$", "", following)
            if not re.search(r"(?m)^(?!\s*(?:[|#*-]|\d+[.)]\s))\s*[A-Za-z]", following):
                errors.append("Missing overview after selected diagram: " + row["heading"])
            if not re.search(r"(?m)^\s*(?:\|[^\n]+\||[-*]\s+\S|\d+[.)]\s+\S)", following):
                errors.append("Missing element explanations after selected diagram: " + row["heading"])
        if row["notation"] not in notations:
            errors.append("Missing selected visual notation under " + row["heading"] + ": " + row["notation"])
    return errors


def render_mermaid(text, destination, renderer="mmdc", timeout=30):
    executable = shutil.which(renderer)
    if not executable:
        raise ValueError("Mermaid renderer unavailable; rendering was not run.")
    target = Path(destination).resolve()
    blocks = [block for block in diagram_blocks(text)[0] if block["language"] == "mermaid"]
    if not blocks:
        raise ValueError("No Mermaid diagrams to render.")
    if target.exists():
        raise ValueError("Use a new render directory to preserve earlier results.")
    target.mkdir(parents=True)
    rendered = []
    with tempfile.TemporaryDirectory(prefix="writer-mermaid-") as temporary:
        for index, block in enumerate(blocks):
            source = Path(temporary) / f"diagram-{index}.mmd"
            source.write_text(block["body"])
            output = target / f"diagram-{index}.svg"
            result = subprocess.run([executable, "-i", str(source), "-o", str(output)], capture_output=True, text=True, timeout=timeout, check=False)
            if result.returncode or not output.is_file() or not output.stat().st_size:
                raise ValueError(f"Mermaid rendering failed at line {block['line']}: " + result.stderr[-2000:])
            rendered.append(str(output))
    return rendered


def check_syntax(text, module_root):
    blocks = [block for block in diagram_blocks(text)[0] if block["language"] == "mermaid"]
    if not blocks:
        return {"status": "not_applicable", "results": []}
    node = shutil.which("node")
    if not node or not module_root:
        return {"status": "not_run", "reason": "Configure Node and TECHNICAL_WRITER_MERMAID_MODULE_ROOT, or use --module-root."}
    process = subprocess.run([node, str(Path(__file__).with_name("check_mermaid.mjs")), str(Path(module_root).resolve())], input=json.dumps(blocks), capture_output=True, text=True, timeout=30, check=False)
    report = json.loads(process.stdout)
    report["status"] = "passed" if process.returncode == 0 and report.get("passed") is True else "failed"
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("document", type=Path)
    parser.add_argument("--render-dir", type=Path)
    parser.add_argument("--renderer", default="mmdc")
    parser.add_argument("--module-root", default=os.environ.get("TECHNICAL_WRITER_MERMAID_MODULE_ROOT"))
    parser.add_argument("--require-syntax", action="store_true")
    args = parser.parse_args()
    from document_contracts import headings
    try:
        text = args.document.read_text()
        findings = visual_errors(text, headings(text))
        syntax = check_syntax(text, args.module_root)
        if syntax["status"] == "failed" or args.require_syntax and syntax["status"] not in {"passed", "not_applicable"}:
            findings.append("Mermaid syntax check did not pass.")
        result = {"passed": not findings, "findings": findings, "syntax": syntax, "render_status": "not_run", "semantic_review_required": True}
        if args.render_dir and not findings:
            result.update(rendered=render_mermaid(text, args.render_dir, args.renderer), render_status="passed")
        print(json.dumps(result, indent=2))
        return int(bool(findings))
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        print(json.dumps({"passed": False, "error": str(error), "render_status": "not_passed"}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
