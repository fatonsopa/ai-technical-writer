"""Versioned document-output checks, independent of a model's quality score."""
import title_contract
import hashlib
import json
from pathlib import Path
import re

import yaml
import tomllib

from planning_readiness import check_discovery, material_topic_errors
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


def canonical_kind(data, kind):
    """Use the stored contract first so frozen validation sessions keep their original identity."""
    if isinstance(kind, str) and kind not in data["documents"] and kind.startswith("issue_"):
        return "task_" + kind.removeprefix("issue_")
    return kind


def document_contract(data, kind):
    document = data["documents"][canonical_kind(data, kind)]
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


IDENTIFIER = re.compile(r"(?<![\w-])[A-Z][A-Z0-9]*-\d+[a-z]?(?![\w-])")


def slug(title):
    """GitHub-style heading anchor."""
    return re.sub(r"[^\w\- ]", "", title.lower()).replace(" ", "-")


def coverage_errors(text, coverage):
    """Resolve each coverage row against its declared source, and each source requirement back to a row.

    The check is mechanical: it decides whether cited IDs and section links exist in
    the declared source revision. Whether the row's work actually serves the
    requirement still needs review.
    """
    label = coverage.get("source", "the declared source")
    revision = coverage.get("revision") or "unrecorded revision"
    source = coverage.get("source_text")
    if source is None:
        return [f"Coverage source unavailable: {label} ({revision}). Its citations were not checked; supply the source before relying on coverage."]
    declared = []
    for row in headings(source):
        found = IDENTIFIER.match(row["title"])
        if found and found[0] not in declared:
            declared.append(found[0])
    for line in source.splitlines():
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")] if line.lstrip().startswith("|") else []
        found = IDENTIFIER.match(cells[0]) if cells else None
        if found and found[0] not in declared:
            declared.append(found[0])
    sections = {slug(row["title"]) for row in headings(source)} | set(re.findall(r'<a id="([^"]+)"', source))
    rows, in_table, errors = [], False, []
    for number, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if not stripped.startswith("|"):
            in_table = False
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if not in_table:
            in_table = bool(re.match(r"(requirement|outcome|criterion)", cells[0], re.I))
            continue
        if set(cells[0]) <= set("-: "):
            continue
        rows.append((number, cells))
    if not rows:
        return [f"No requirement coverage table was found to compare with {label} ({revision})."]
    cited = {value for _, cells in rows for value in IDENTIFIER.findall(cells[0])}
    uncovered = [value for value in declared if value not in cited]
    for number, cells in rows:
        first = cells[0]
        if re.match(r"safeguard\b", first, re.I):
            if len(cells) < 2 or not any(cell for cell in cells[1:]):
                errors.append(f"Coverage row on line {number} declares a safeguard without its justification or work.")
            continue
        ids = IDENTIFIER.findall(first)
        anchors = re.findall(r"\]\([^)#]*#([^)]+)\)", first)
        if not ids and not anchors:
            errors.append(f"Coverage row on line {number} ({first!r}) cites no requirement ID or section of {label}. Cite the governing requirement or mark the row as a justified safeguard.")
        for value in ids:
            if value not in declared:
                hint = f" It likely replaced {uncovered[0]}, which no row covers now." if len(uncovered) == 1 else ""
                errors.append(f"Coverage row on line {number} ({first!r}) cites {value}, which {label} at {revision} does not declare.{hint} Correct the row to the requirement it implements.")
        for value in anchors:
            if value not in sections:
                errors.append(f"Coverage row on line {number} ({first!r}) links to section #{value}, which {label} at {revision} does not contain.")
            else:
                cited.add("#" + value)
    for value in declared:
        if value not in cited:
            errors.append(f"Requirement {value} in {label} at {revision} has no coverage row, so no work owns it. Add its owning work or record why it is excluded.")
    return errors


def parent_errors(text, parents):
    """Check each declared parent edge: a link into the parent at an anchor it contains, and its revision.

    A child with an unresolved parent is held rather than treated as standalone.
    """
    errors = []
    for parent in parents:
        label = parent.get("source", "the declared parent")
        revision = parent.get("revision")
        source = parent.get("source_text")
        if source is None:
            errors.append(f"Parent {label} is unavailable, so this child is not ready. Restore or relink the parent; a missing parent does not make the work standalone.")
            continue
        anchors = {slug(row["title"]) for row in headings(source)} | set(re.findall(r'<a id="([^"]+)"', source))
        name = Path(parent.get("path", label)).name
        links = [anchor for target, anchor in re.findall(r"\]\(([^)#\s]*)#([^)\s]+)\)", text) if Path(target).name == name]
        if not links:
            errors.append(f"No link to a section of parent {label}, so the edge to its outcome or criterion is missing. Link the exact story criterion or epic outcome this work serves.")
        for anchor in links:
            if anchor not in anchors:
                errors.append(f"Broken parent edge: #{anchor} is not in {label}" + (f" at {revision}" if revision else "") + ". The parent may be stale or contradict this child; hold dependent work until the edge resolves.")
        if revision and revision not in text:
            errors.append(f"The child does not state the parent revision {revision} for {label}, so a reader cannot tell which version governs it.")
    return errors


def validate(text, kind, operation="create", scope="complete", context=None, contracts=None):
    context = context or {}
    data = contracts or load_contracts()
    kind = canonical_kind(data, kind)
    if kind not in data["documents"]:
        raise ValueError(f"Unsupported document type: {kind}. Supported kinds: {", ".join(sorted(data["documents"]))}")
    if operation not in {"create", "rewrite", "edit", "review"} or scope not in {"complete", "excerpt", "title"}:
        raise ValueError("Unknown operation or output scope.")
    contract = document_contract(data, kind)
    errors, nodes = [], headings(text)
    formats = contract.get('instruction_formats', {}) if kind == 'agent' else {}
    selected = context.get('instruction_format', 'subagent')
    if kind == 'agent' and selected not in formats:
        raise ValueError('Unsupported instruction_format. Supported formats: ' + ', '.join(formats))
    if kind == 'agent' and 'instruction_version' in context and context['instruction_version'] != formats[selected].get('version'):
        raise ValueError('Unsupported instruction version for ' + selected)

    if not text.strip():
        errors.append("Output is empty.")
    complete = scope == "complete" and operation != "review"
    if complete:
        format_name = contract.get("format", "document")
        if kind == 'agent' and context.get('instruction_format') == 'project':
            format_name = 'document'
        if kind == 'agent' and selected == 'codex-toml':
            format_name = 'toml'
        if format_name == 'toml':
            try:
                header = tomllib.loads(text)
                route = formats[selected]
                allowed = {*route['required_strings'], *route['optional_strings'], *route['optional_tables']}
                if set(header) - allowed:
                    errors.append('Unsupported TOML agent fields: ' + ', '.join(sorted(set(header) - allowed)))
                for field in route['required_strings']:
                    if not isinstance(header.get(field), str) or not header[field].strip():
                        errors.append('Missing/non-string TOML agent field: ' + field)
                for field in route['optional_strings']:
                    if field in header and (not isinstance(header[field], str) or not header[field].strip()):
                        errors.append('Invalid TOML agent field: ' + field)
                if 'features' in header and (not isinstance(header['features'], dict) or any(type(v) is not bool for v in header['features'].values())):
                    errors.append('Agent features must be a table of boolean flags.')
                if 'skills' in header and not isinstance(header['skills'], dict):
                    errors.append('Agent skills must be a table.')
                if not re.fullmatch(r'[a-z0-9]+(?:[-_][a-z0-9]+)*', str(header.get('name', ''))):
                    errors.append('Invalid TOML agent name.')
            except tomllib.TOMLDecodeError as error:
                errors.append('Invalid TOML agent syntax: ' + str(error))
        elif format_name == "frontmatter":
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
            decision_comment = (
                kind == "decision" and not titles
                and text.lstrip().startswith("## Decision:\n")
            )
            if not decision_comment and (not titles or (format_name == "document" and len(titles) != 1)):
                errors.append(f"Expected {'one' if format_name == 'document' else 'a'} level-{expected_level} title.")
            if format_name == "visual":
                if not re.search(r"(?:`{3,}|~{3,})(?:mermaid|dot|plantuml)\b|!\[[^\]]+\]\(", text):
                    errors.append("Missing diagram or image with meaningful alternative text.")
        errors.extend(section_errors(nodes, contract.get("sections", []), context, contract.get("ordered", False)))
        for index, node in enumerate(nodes):
            if node["parent"] is not None and node["level"] > nodes[node["parent"]]["level"] + 1:
                errors.append(f"Heading level skips its parent at line {node['line']}.")
        if contract.get("task_type"):
            first_section = next((node["line"] - 1 for node in nodes if node["level"] == 2), len(text.splitlines()))
            prose, fence = [], None
            for line in text.splitlines()[:first_section]:
                marker = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
                if fence:
                    if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                        fence = None
                elif marker:
                    fence = marker[1][0], len(marker[1])
                else:
                    prose.append(line)
            preamble = "\n".join(prose)
            if re.search(r"(?mi)^Type:\s*(?:Bug|Chore|Decision|Feature|Improvement|Release)\s*$", preamble):
                errors.append("Keep task type in tracker metadata, outside the task text.")
        if kind == "decision":
            options = [(node, re.match(r"Option\s+([A-Za-z0-9]+)\s*:", node["title"], re.I)) for node in nodes]
            options = [(node, match) for node, match in options if match]
            labels = [match[1] for node, match in options]
            expected_labels = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:len(labels)])
            if labels != expected_labels:
                errors.append("Decision options must use consecutive uppercase labels A, B, C and so on.")
            decision = next((node for node in nodes if node["level"] == 2 and node["title"] == "Decision:"), None)
            if decision and substantive(decision["body"]):
                if "\n" in decision["body"] or re.search(r"^\s*[#>`*-]", decision["body"]):
                    errors.append("Decision title must be one plain-English paragraph.")
                errors.extend(title_contract.title_errors(decision["body"]))
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
    if complete or scope == 'title':
        for node in nodes:
            if node['level'] == 1:
                errors.extend(title_contract.title_errors(node['title'], task=bool(contract.get('task_type')) or kind in {'task', 'bug_report', 'story'}))
    if "discovery" in context:
        errors.extend(check_discovery(text, context["discovery"]))
        if complete and contract.get("material_topics"):
            errors.extend(material_topic_errors(context["discovery"], contract["material_topics"]))
    for value in context.get("required_literals", []):
        if not isinstance(value, str) or value not in text:
            errors.append(f"Missing required literal: {value!r}")
    if "coverage" in context:
        errors.extend(coverage_errors(text, context["coverage"]))
    if "parents" in context:
        errors.extend(parent_errors(text, context["parents"]))
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
