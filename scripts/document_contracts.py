"""Versioned document-output checks, independent of a model's quality score."""
import hashlib
import json
from pathlib import Path
import re

import yaml

from planning_readiness import check_discovery
from visual_contracts import visual_errors

ROOT = Path(__file__).resolve().parents[1]
CONTRACTS = ROOT / "contracts/documents.json"


def digest(value):
    data = value if isinstance(value, bytes) else json.dumps(value, sort_keys=True, ensure_ascii=False).encode()
    return hashlib.sha256(data).hexdigest()


def load_contracts():
    data = json.loads(CONTRACTS.read_text())
    if data.get("schema_version") != 1 or not isinstance(data.get("documents"), dict):
        raise ValueError("Unsupported document contract.")
    return data


def document_contract(data, kind):
    document = data["documents"][kind]
    inherited = data.get("profiles", {}).get(document.get("profile"), {})
    return {**inherited, **document}


def headings(text):
    """Read ATX headings outside fenced blocks, retaining hierarchy and source lines."""
    lines = text.splitlines()
    found, stack, fence = [], [], None
    for number, line in enumerate(lines):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = marker[1][0], len(marker[1])
            continue
        match = re.match(r"^\s{0,3}(#{1,6})\s+(.+?)\s*$", line)
        if not match:
            continue
        level = len(match[1])
        title = re.sub(r"\s+#+\s*$", "", match[2]).strip()
        while stack and found[stack[-1]]["level"] >= level:
            stack.pop()
        found.append({"level": level, "title": title, "line": number + 1, "parent": stack[-1] if stack else None})
        stack.append(len(found) - 1)
    for index, node in enumerate(found):
        end = next((row["line"] - 1 for row in found[index + 1:] if row["level"] <= node["level"]), len(lines))
        node["body"] = "\n".join(lines[node["line"]:end]).strip()
    return found


def normalized(value):
    return re.sub(r"\s+", " ", value.strip().strip("*_` ")).casefold()


def matches(node, rule):
    if node["level"] != rule.get("level", 2):
        return False
    if "pattern" in rule:
        return bool(re.fullmatch(rule["pattern"], node["title"], re.I))
    return normalized(node["title"]) in {normalized(label) for label in rule["labels"]}


def substantive(body):
    content = re.sub(r"(?m)^\s*#{1,6}\s+.*$", "", body).strip()
    return bool(content) and not re.fullmatch(r"\[[^\]\n]+\]|\.{3}|TODO|TBD", content, re.I)


def section_errors(nodes, rules, context, ordered=False):
    errors, previous = [], -1
    for rule in rules:
        if "alternatives" in rule:
            alternatives = [section_errors(nodes, option, context, ordered) for option in rule["alternatives"]]
            if all(alternatives):
                errors.append(f"Missing required section group: {rule['id']}")
                errors.extend(min(alternatives, key=len))
            continue
        required = rule.get("required", True)
        if rule.get("when"):
            required = bool(context.get(rule["when"]))
        found = [index for index, node in enumerate(nodes) if matches(node, rule)]
        label = rule["id"]
        if required and not found:
            errors.append(f"Missing required section: {label}")
            continue
        if len(found) > 1:
            errors.append(f"Repeated section: {label}")
        for index in found:
            node = nodes[index]
            if not substantive(node["body"]):
                errors.append(f"Empty or placeholder section: {label}")
            if ordered and index < previous:
                errors.append(f"Section out of order: {label}")
            previous = index
            for child in rule.get("children", []):
                children = [candidate for candidate in nodes if candidate["parent"] == index and matches(candidate, child)]
                if len(children) < child.get("minimum", 1):
                    errors.append(f"Missing required subheadings under {label}: {child['id']}")
                if any(not substantive(candidate["body"]) for candidate in children):
                    errors.append(f"Empty required subheading under {label}: {child['id']}")
    return errors


def validate(text, kind, operation="create", scope="complete", context=None, contracts=None):
    context = context or {}
    data = contracts or load_contracts()
    if kind not in data["documents"]:
        raise ValueError(f"Unsupported document type: {kind}")
    if operation not in {"create", "rewrite", "edit", "review"} or scope not in {"complete", "excerpt", "title"}:
        raise ValueError("Unknown operation or output scope.")
    contract = document_contract(data, kind)
    errors, nodes = [], headings(text)
    if not text.strip():
        errors.append("Output is empty.")
    complete = scope == "complete" and operation != "review"
    if complete:
        format_name = contract.get("format", "document")
        if kind == 'agent' and context.get('instruction_format') == 'project':
            format_name = 'document'
        if format_name == "frontmatter":
            parts = text.split("---\n", 2)
            try:
                if len(parts) != 3 or parts[0]:
                    raise ValueError("Missing YAML frontmatter.")
                header = yaml.safe_load(parts[1])
                if not isinstance(header, dict):
                    raise ValueError("Frontmatter must be a mapping.")
                for field in ("name", "description"):
                    if not isinstance(header.get(field), str) or not header[field].strip():
                        errors.append(f"Missing/non-string frontmatter field: {field}")
                if kind in {"skill", "agent"} and not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(header.get("name", ""))):
                    errors.append("Invalid skill/agent name.")
                if kind == "skill" and isinstance(header.get("description"), str) and len(header["description"]) > 1024:
                    errors.append("Skill description exceeds 1,024 characters.")
                if not substantive(parts[2]):
                    errors.append("Instruction body is empty.")
            except (ValueError, yaml.YAMLError) as error:
                errors.append(str(error))
        elif format_name == "requirement":
            if not any(node["level"] == 3 and re.match(r"[A-Za-z][A-Za-z0-9_-]*[- ]\d+:", node["title"]) for node in nodes):
                errors.append("Missing identified requirement heading at level 3.")
            for field in ("Status/source", "Statement", "Verification"):
                if not re.search(r"(?m)^" + re.escape(field) + r":\s*\S", text):
                    errors.append(f"Missing requirement field: {field}")
        else:
            levels = contract.get("title_levels", [3]) if format_name == "visual" else [1]
            expected_level = levels[0]
            titles = [node for node in nodes if node["level"] in levels]
            if not titles or (format_name == "document" and len(titles) != 1):
                errors.append(f"Expected {'one' if format_name == 'document' else 'a'} level-{expected_level} title.")
            if format_name == "visual":
                if not re.search(r"(?:`{3,}|~{3,})(?:mermaid|dot|plantuml)\b|!\[[^\]]+\]\(", text):
                    errors.append("Missing diagram or image with meaningful alternative text.")
        errors.extend(section_errors(nodes, contract.get("sections", []), context, contract.get("ordered", False)))
        for index, node in enumerate(nodes):
            if node["parent"] is not None and node["level"] > nodes[node["parent"]]["level"] + 1:
                errors.append(f"Heading level skips its parent at line {node['line']}.")
        if contract.get("task_type") and not re.search(r"(?mi)^Type:\s*" + re.escape(contract["task_type"]) + r"\s*$", text):
            errors.append(f"Missing task type: {contract['task_type']}")
        if kind == "decision":
            options = [(node, re.match(r"Option\s+([A-Za-z0-9]+)\s*:", node["title"], re.I)) for node in nodes]
            options = [(node, match) for node, match in options if match]
            labels = [match[1] for node, match in options]
            for node, match in options:
                parent = nodes[node["parent"]] if node["parent"] is not None else None
                if node["level"] != 3 or not parent or parent["level"] != 2 or normalized(parent["title"]) != "options considered":
                    errors.append(f"Option {match[1]} must be a level-3 heading under Options considered.")
            if len({label.casefold() for label in labels}) != len(labels):
                errors.append("Decision option labels must be unique.")
            recommended = next((match for node in nodes if node["level"] == 2 and (match := re.match(r"Recommended option\s*\(([^)]+)\)", node["title"], re.I))), None)
            if recommended and recommended[1].casefold() not in {value.casefold() for value in labels}:
                errors.append("Recommended option is not among the listed options.")
        if kind == "sdd" and nodes and re.search(r"software design document", nodes[0]["title"], re.I):
            errors.append("Behavioral SDD must not be labeled Software Design Document.")
        errors.extend(visual_errors(text, nodes, context.get("visuals")))
    if "discovery" in context:
        errors.extend(check_discovery(text, context["discovery"]))
    for value in context.get("required_literals", []):
        if not isinstance(value, str) or value not in text:
            errors.append(f"Missing required literal: {value!r}")
    for value in context.get("requirement_ids", []):
        if not re.search(r"(?<![\w-])" + re.escape(value) + r"(?![\w-])", text):
            errors.append(f"Missing required requirement ID: {value}")
    return {"passed": not errors, "findings": errors, "kind": kind, "operation": operation, "scope": scope,
            "contract_sha256": digest(data), "output_sha256": digest(text.encode()), "semantic_review_required": True}


def validate_grade(item):
    """Reject malformed model judgments before evaluating their quality scores."""
    scores = item.get("scores")
    if not isinstance(scores, list) or len(scores) != 7 or any(type(score) is not int or not 0 <= score <= 3 for score in scores):
        raise ValueError("A grade needs exactly seven integer scores in 0–3.")
    for field in ("critical_failures", "reasons"):
        if not isinstance(item.get(field), list) or any(not isinstance(value, str) or not value.strip() for value in item[field]):
            raise ValueError(f"Invalid grade field: {field}")
    if not item["reasons"]:
        raise ValueError("A grade needs a source-supported rationale.")
    return all(score >= 2 for score in scores) and not item["critical_failures"]
