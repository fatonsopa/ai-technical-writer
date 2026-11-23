#!/usr/bin/env python3
"""Validate a document and bind accepted delivery to its actual inputs and review."""
import record_retention

import argparse
from contextlib import contextmanager
import json
import os
import re
from pathlib import Path
import sys
import tempfile
import time

from document_contracts import ROOT, canonical_kind, digest, document_contract, headings, load_contracts, validate, validate_grade
from planning_readiness import discovery_errors
from visual_contracts import check_syntax, diagram_blocks, embedded_source_errors
from render_diagram import check_svg
from diagram_components import explanation_errors, read_manifest
import xml.etree.ElementTree as ET
import rewrite_workflow
import writing_style_contract as writing_style
from continuation import check_totals, extension as routine_extension


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as stream:
        temporary = Path(stream.name)
        json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write("\n")
    try:
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def load(path):
    return json.loads(Path(path).read_text())


def tool_identity():
    return {name: digest((ROOT / name).read_bytes()) for name in ("SKILL.md", "scripts/record_retention.py", "scripts/continuation.py", "scripts/document_contracts.py", "scripts/title_contract.py", "scripts/validate_document.py", "scripts/rewrite_workflow.py", "scripts/writing_style_contract.py", "scripts/planning_readiness.py", "scripts/visual_contracts.py", "scripts/check_mermaid.mjs", "scripts/diagram_components.py", "scripts/diagram_inventory.mjs", "scripts/mermaid_runtime.mjs", "scripts/audit_diagram.mjs", "scripts/render_diagram.py", "scripts/diagram_presentation.py", "config/diagram_style.json", "contracts/documents.json", "contracts/delivery_message.json")}


@contextmanager
def locked(session):
    lock = Path(session) / ".lock"
    descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    try:
        os.close(descriptor)
        yield
    finally:
        lock.unlink(missing_ok=True)


def prepare(request_file, session):
    request_file, session = Path(request_file).resolve(), Path(session).resolve()
    if session.is_relative_to(ROOT):
        raise ValueError("Keep document sessions outside the installed skill.")
    if session.exists():
        raise ValueError("Session already exists; preserve its evidence.")
    request = load(request_file)
    allowed = {"kind", "operation", "scope", "sources", "destination", "context", "requirements", "limits", "hard_limits"}
    if not isinstance(request, dict) or set(request) - allowed:
        raise ValueError("Unknown document request fields.")
    if not {"kind", "sources", "destination"} <= request.keys():
        raise ValueError("The request needs kind, sources and destination.")
    contracts = load_contracts()
    writing_style.load_guide(ROOT)
    request["kind"] = canonical_kind(contracts, request["kind"])
    if request["kind"] not in contracts["documents"]:
        raise ValueError("Unknown document kind. Supported kinds: " + ", ".join(sorted(contracts["documents"])))
    request.setdefault("operation", "create")
    request.setdefault("scope", "complete")
    if request["operation"] not in {"create", "rewrite", "edit", "review"} or request["scope"] not in {"complete", "excerpt", "title"}:
        raise ValueError("Invalid operation/scope.")
    sources = request["sources"]
    if not isinstance(sources, list) or not sources:
        raise ValueError("Supply the source facts or original document.")
    captured, ids = [], set()
    for source in sources:
        if not isinstance(source, dict) or set(source) not in ({"id", "path"}, {"id", "text"}):
            raise ValueError("Each source needs id and exactly one of path or text.")
        if not isinstance(source["id"], str) or not source["id"].strip() or source["id"] in ids:
            raise ValueError("Source IDs must be nonempty and unique.")
        ids.add(source["id"])
        row = dict(source)
        if "path" in row:
            path = (request_file.parent / row["path"]).resolve()
            row.update(path=str(path), text=path.read_bytes().decode("utf-8"))
        if not isinstance(row["text"], str) or not row["text"].strip():
            raise ValueError("Source text cannot be empty.")
        row["sha256"] = digest(row["text"].encode())
        captured.append(row)
    requirements = request.setdefault("requirements", [])
    if not isinstance(requirements, list) or any(not isinstance(row, dict) or set(row) != {"id", "text"} or not all(isinstance(value, str) and value.strip() for value in row.values()) for row in requirements):
        raise ValueError("Requirements need explicit id/text entries.")
    if len({row["id"] for row in requirements}) != len(requirements):
        raise ValueError("Requirement IDs must be unique.")
    context = request.setdefault("context", {})
    if not isinstance(context, dict) or set(context) - {"required_literals", "requirement_ids", "open_prerequisites", "decision_made", "edit_region", "discovery", "visuals", "instruction_format", "instruction_version", "rewrite_authorization", "coverage", "parents", "destination_requested"}:
        raise ValueError("Unsupported document context.")
    rewrite_workflow.authorization(context)
    if 'instruction_format' in context and (request['kind'] != 'agent' or context['instruction_format'] not in contracts['documents']['agent']['instruction_formats']):
        raise ValueError('instruction_format applies to agent documents. Supported formats: ' + ', '.join(contracts['documents']['agent']['instruction_formats']))
    for name in ("required_literals", "requirement_ids"):
        if name in context and (not isinstance(context[name], list) or any(not isinstance(value, str) or not value for value in context[name])):
            raise ValueError(f"{name} must contain nonempty strings.")
    coverage = context.get("coverage")
    if coverage is not None and (not isinstance(coverage, dict) or coverage.get("source_id") not in ids or set(coverage) - {"source_id", "revision"}):
        raise ValueError("coverage needs the source_id of a supplied source and an optional revision.")
    parents = context.get("parents")
    if parents is not None and (not isinstance(parents, list) or any(not isinstance(row, dict) or row.get("source_id") not in ids or set(row) - {"source_id", "revision"} for row in parents)):
        raise ValueError("parents needs a list of supplied source_id values with optional revisions.")
    for name in ("open_prerequisites", "decision_made"):
        if name in context and type(context[name]) is not bool:
            raise ValueError(f"{name} must be boolean.")
    planning = document_contract(contracts, request["kind"]).get("discovery_before_delivery") and request["scope"] == "complete" and request["operation"] != "review"
    if planning and "discovery" not in context and not rewrite_workflow.required(request):
        raise ValueError("Complete planning documents need a discovery record; inspect sources and resolve material choices first.")
    if "discovery" in context:
        problems = discovery_errors(context["discovery"], ids)
        if problems:
            raise ValueError(" ".join(problems))
    if "visuals" in context:
        # Validate selection metadata here; the actual headings/notation are checked on the draft.
        selections = context["visuals"]
        if not isinstance(selections, list):
            raise ValueError("Visual selections must be a list.")
        for selection in selections:
            if not isinstance(selection, dict) or set(selection) != {"heading", "notation", "reason"} or any(not isinstance(v, str) or not v.strip() for v in selection.values()):
                raise ValueError("Each selected visual needs heading, notation and reason.")
    limits = {"max_attempts": 3, "max_seconds": 600, **request.get("limits", {})}
    if set(limits) != {"max_attempts", "max_seconds"} or any(type(value) is not int or value <= 0 for value in limits.values()):
        raise ValueError("Document limits must be positive integer attempt/time bounds.")
    check_totals({"attempts": limits["max_attempts"], "seconds": limits["max_seconds"]}, request.get("hard_limits"))
    destination = (request_file.parent / request["destination"]).resolve()
    if destination.is_relative_to(session) or destination.is_relative_to(ROOT):
        raise ValueError("The destination must be outside the session and writing skill.")
    before_text = destination.read_bytes().decode("utf-8") if destination.exists() else None
    if before_text is not None and request["operation"] == "create":
        raise ValueError("Creation needs a new destination; use an explicit edit/rewrite for an existing file.")
    if request["operation"] == "review" and any(row.get("path") == str(destination) for row in captured):
        raise ValueError("A review must deliver findings separately from the reviewed source.")
    if "destination_requested" in context and type(context["destination_requested"]) is not bool:
        raise ValueError("destination_requested must be boolean.")
    if any(row.get("path") == str(destination) for row in captured) and context.get("destination_requested") is not True:
        raise ValueError("The destination is one of this document's sources. Save the new document as its own file, or set context.destination_requested to true only when the user asked to change that file.")
    region = context.get("edit_region")
    if region is not None and (not isinstance(region, list) or len(region) != 2 or any(type(value) is not int for value in region) or region[0] <= 0 or region[1] < region[0]):
        raise ValueError("edit_region needs the inclusive original start/end line numbers.")
    if before_text is not None and request["operation"] == "edit" and request["scope"] == "excerpt" and region is None:
        raise ValueError("An excerpt edit of an existing file needs an explicit edit_region.")
    request.update(sources=captured, destination=str(destination), limits=limits)
    contract = document_contract(contracts, request["kind"])
    guide_names = {contract["reference"], "references/writing_style.md", "workflows/validation_review.md"}
    if rewrite_workflow.required(request):
        guide_names.update({'workflows/rewrite.md', 'workflows/rewrite_preflight.md'})
    if "discovery" in context:
        guide_names.add("workflows/discover.md")
    if context.get("visuals"):
        guide_names.add("references/visuals.md")
        if any(row["notation"] in {"flowchart_svg", "diagram_svg"} for row in context["visuals"]):
            guide_names.add("workflows/diagram_rendering.md")
        if any(row["notation"] == "flowchart_svg" for row in context["visuals"]):
            guide_names.add("workflows/flowcharts.md")
    if request["kind"].startswith("task_") or request["kind"] == "bug_report":
        guide_names.add("references/task.md")
    if any(row.get("path", "").endswith(".svg") and "data-diagram-type=" in row["text"] for row in captured):
        guide_names.update({"references/visuals.md", "workflows/diagram_rendering.md"})
    guidance = {}
    for name in sorted(guide_names):
        path = (ROOT / name).resolve()
        if not path.is_relative_to(ROOT):
            raise ValueError("Guidance must be self-contained in the skill.")
        guidance[name] = path.read_bytes().decode("utf-8")
    frozen = {"request": request, "contracts": contracts, "tool_identity": tool_identity(),
              "guidance": guidance,
              "destination_before": digest(destination.read_bytes()) if destination.exists() else None,
              "destination_before_text": before_text}
    state = {"schema_version": 1, "frozen": frozen, "objective_sha256": digest(frozen),
             "started": time.time(), "attempts": [], "extensions": [], "delivery": None}
    record_retention.begin(session, 'technical-writer',
        protected=[ROOT, *[row['path'] for row in captured if row.get('path')]], outputs=[destination])
    record_retention.cleanup(session.parent, 'technical-writer')
    save(session / "state.json", state)
    return {"status": "prepared", "session": str(session), "objective_sha256": state["objective_sha256"], "limits": limits}


def state_for(session, budget=True):
    state = load(Path(session) / "state.json")
    if digest(state["frozen"]) != state["objective_sha256"]:
        raise ValueError("Frozen document objective changed; start a new versioned session.")
    if tool_identity() != state["frozen"]["tool_identity"]:
        raise ValueError("Validator or contract changed; start a new session.")
    for name, content in state["frozen"]["guidance"].items():
        if (ROOT / name).read_bytes().decode("utf-8") != content:
            raise ValueError("Document guidance changed; start a new session.")
    for source in state["frozen"]["request"]["sources"]:
        if "path" in source:
            actual = digest(Path(source["path"]).read_bytes())
            delivered = state.get("delivery") or {}
            is_own_delivery = source["path"] == delivered.get("destination") and actual == delivered.get("output_sha256")
            if actual != source["sha256"] and not is_own_delivery:
                raise ValueError("A source changed after preparation; start a new session.")
    rewrite_workflow.records(state)
    allowance = state["frozen"]["request"]["limits"]["max_seconds"] + sum(row["seconds"] for row in state["extensions"])
    if budget and time.time() - state["started"] > allowance:
        raise ValueError("Document runtime allowance exhausted; assess results and use the bounded continuation policy.")
    return state


def workflow_packet(session):
    return rewrite_workflow.packet(state_for(session))


def workflow_record(session, record_file):
    state = state_for(session)
    result = rewrite_workflow.accept(state, record_file)
    save(Path(session) / 'state.json', state)
    return result


def draft_permission(session):
    return rewrite_workflow.permission(state_for(session))


def check(session, draft, budget=True):
    session, draft = Path(session), Path(draft)
    state = state_for(session, budget=budget)
    rewrite_workflow.permission(state)
    request = state["frozen"]["request"]
    context = rewrite_workflow.draft_context(state)
    if "coverage" in context:
        selected = context["coverage"]
        source = next(row for row in request["sources"] if row["id"] == selected["source_id"])
        context = {**context, "coverage": {**selected, "source": selected["source_id"], "source_text": source["text"]}}
    if "parents" in context:
        captured = {row["id"]: row for row in request["sources"]}
        context = {**context, "parents": [{**row, "source": row["source_id"], "path": captured[row["source_id"]].get("path", row["source_id"]), "source_text": captured[row["source_id"]]["text"]} for row in context["parents"]]}
    text = draft.read_bytes().decode("utf-8")
    result = validate(text, request["kind"], request["operation"], request["scope"], context, state["frozen"]["contracts"])
    if request["scope"] == "complete" and request["operation"] != "review":
        captured = {row.get("path"): row["text"] for row in request["sources"] if row.get("path")}
        for selection in request["context"].get("visuals", []):
            if selection["notation"] not in {"flowchart_svg", "diagram_svg"}:
                continue
            sections = [node for node in headings(text) if node["title"].casefold() == selection["heading"].casefold()]
            images = re.findall(r"!\[[^\]\n]+\]\(([^)]+\.svg)\)", sections[0]["body"]) if len(sections) == 1 else []
            if len(images) != 1:
                result["findings"].append("Selected diagram needs one SVG under " + selection["heading"])
                continue
            image = (Path(request["destination"]).parent / images[0]).resolve()
            source = image.with_suffix(".mmd")
            if str(image) not in captured or str(source) not in captured:
                result["findings"].append("Capture the SVG and its same-named Mermaid source before preparing delivery.")
                continue
            result["findings"].extend(check_svg(captured[str(image)], captured[str(source)]))
            result["findings"].extend(embedded_source_errors(sections[0]["body"], captured[str(source)]))
            try:
                result["findings"].extend(explanation_errors(sections[0]["body"], read_manifest(ET.fromstring(captured[str(image)]))))
            except (ValueError, ET.ParseError) as error:
                result["findings"].append("Invalid diagram component inventory: " + str(error))
            if selection["notation"] == "flowchart_svg" and not re.search(r"(?m)^\s*(?:flowchart|graph)\b", captured[str(source)]):
                result["findings"].append("The selected flowchart SVG contains a different diagram family.")
    if request["scope"] == "complete" and request["operation"] != "review":
        captured = {row.get("path"): row["text"] for row in request["sources"] if row.get("path")}
        images = list(re.finditer(r'!\[[^\]\n]+\]\(([^)\n]+\.svg)\)', text))
        for index, match in enumerate(images):
            image = (Path(request["destination"]).parent / match[1]).resolve()
            source = image.with_suffix(".mmd")
            raw = captured.get(str(image), "")
            if 'data-diagram-type=' not in raw and str(source) not in captured:
                continue  # A quantitative chart or other external SVG has its own checks.
            if str(source) not in captured:
                result["findings"].append("Capture the SVG and its same-named Mermaid source before preparing delivery.")
                continue
            segment = text[match.start():images[index + 1].start() if index + 1 < len(images) else len(text)]
            result["findings"].extend(check_svg(raw, captured[str(source)]))
            result["findings"].extend(embedded_source_errors(segment, captured[str(source)]))
            try:
                result["findings"].extend(explanation_errors(segment, read_manifest(ET.fromstring(raw))))
            except (ValueError, ET.ParseError) as error:
                result["findings"].append("Invalid diagram component inventory: " + str(error))
    if request["scope"] == "complete" and request["operation"] != "review" and any(row["language"] == "mermaid" for row in diagram_blocks(text)[0]):
        if any(row["language"] == "mermaid" and re.search(r"(?m)^\s*(?:flowchart|graph)\b", row["body"]) for row in diagram_blocks(text)[0]):
            result["findings"].append("Complete flowcharts need a source-bound SVG with the shared light dotted canvas; inline Mermaid cannot guarantee that background.")
        else:
            result["findings"].append("Complete diagrams need a source-bound SVG with a visible title, subtitle and symbol legend; accessibility metadata alone is insufficient.")
        result["visual_syntax"] = check_syntax(text, os.environ.get("TECHNICAL_WRITER_MERMAID_MODULE_ROOT"))
        if result["visual_syntax"]["status"] != "passed":
            result["findings"].append("Embedded Mermaid syntax is failed or unverified; configure the parser before accepted delivery.")
    original = state["frozen"]["destination_before_text"]
    if original is not None and request["operation"] == "edit" and request["scope"] == "title":
        old_titles = [node for node in headings(original) if node["level"] == 1]
        new_titles = [node for node in headings(text) if node["level"] == 1]
        old_lines, new_lines = original.splitlines(keepends=True), text.splitlines(keepends=True)
        if len(old_titles) != 1 or len(new_titles) != 1 or old_titles[0]["line"] != new_titles[0]["line"]:
            result["findings"].append("A title-only file edit must retain one H1 in its original position.")
        else:
            index = old_titles[0]["line"] - 1
            if old_lines[:index] + old_lines[index + 1:] != new_lines[:index] + new_lines[index + 1:]:
                result["findings"].append("A title-only file edit changed content outside the title.")
    if original is not None and request["operation"] == "edit" and request["scope"] == "excerpt":
        start, end = request["context"]["edit_region"]
        old_lines = original.splitlines(keepends=True)
        prefix, suffix = "".join(old_lines[:start - 1]), "".join(old_lines[end:])
        if end > len(old_lines) or not text.startswith(prefix) or not text.endswith(suffix) or len(text) < len(prefix) + len(suffix):
            result["findings"].append("An excerpt edit changed content outside its declared original lines.")
    result["passed"] = not result["findings"]
    identifier = result["output_sha256"]
    if not budget and identifier not in state["attempts"]:
        raise ValueError("Delivery requires passing checks and review for these exact output bytes; check and review a changed draft first.")
    maximum = request["limits"]["max_attempts"] + sum(row["attempts"] for row in state["extensions"])
    if identifier not in state["attempts"]:
        if len(state["attempts"]) >= maximum:
            raise ValueError("Document attempt allowance exhausted; retain the failures and use the bounded continuation policy.")
        state["attempts"].append(identifier)
    result['writing_style'] = writing_style.packet(text, state['frozen']['guidance'][writing_style.REFERENCE], request['sources'], request['destination'])
    state.setdefault('style_contracts', {})[identifier] = result['writing_style']
    save(session / 'state.json', state)
    result.update(objective_sha256=state["objective_sha256"], accepted=False, review_status="pending")
    save(session / "checks" / (identifier + ".json"), result)
    return result


def packet(session, draft):
    result = check(session, draft)
    state = state_for(session)
    request = state["frozen"]["request"]
    return {"objective_sha256": state["objective_sha256"], "output_sha256": result["output_sha256"],
            "mechanical_checks": result, "sources": request["sources"], "requirements": request["requirements"],
            "original_destination": state["frozen"]["destination_before_text"],
            "guidance": state["frozen"]["guidance"],
            "rewrite_preflight": rewrite_workflow.packet(state),
            "writing_style": result['writing_style'],
            "contract": document_contract(state["frozen"]["contracts"], request["kind"]), "output": Path(draft).read_bytes().decode("utf-8"),
            "instructions": state['frozen']['guidance']['workflows/validation_review.md']}

def assess_review(state, data):
    if data.get("objective_sha256") != state["objective_sha256"]:
        raise ValueError("Review objective does not match this session.")
    identifier = data.get("output_sha256")
    if identifier not in state["attempts"]:
        raise ValueError("Review does not refer to a checked output.")
    reviewer = data.get("reviewer", {})
    if reviewer.get("kind") not in {"current_host_self_review", "current_host_review", "independent_model", "human"} or not all(isinstance(reviewer.get(key), str) and reviewer[key].strip() for key in ("identity", "method")) or not (reviewer.get("model") is None or isinstance(reviewer.get("model"), str)):
        raise ValueError("Review must identify its actual reviewer and method.")
    passed = validate_grade(data)
    entries = data.get("requirements")
    expected = {row["id"] for row in state["frozen"]["request"]["requirements"]}
    source_ids = {row["id"] for row in state["frozen"]["request"]["sources"]}
    if not isinstance(entries, list) or len(entries) != len(expected) or {row.get("id") for row in entries if isinstance(row, dict)} != expected:
        raise ValueError("Review must cover every explicit requirement exactly once.")
    for row in entries:
        if type(row.get("accepted")) is not bool or not isinstance(row.get("rationale"), str) or not row["rationale"].strip() or not isinstance(row.get("source_ids"), list) or any(value not in source_ids for value in row["source_ids"]):
            raise ValueError("Malformed requirement judgment or unsupported source reference.")
    style_passed = writing_style.check_review(state['style_contracts'][identifier], data.get('style_review'))
    return passed and style_passed and all(row["accepted"] for row in entries)


def review(session, review_file):
    state = state_for(session)
    data = load(review_file)
    passed = assess_review(state, data)
    identifier = data["output_sha256"]
    mechanical = load(Path(session) / "checks" / (identifier + ".json"))
    accepted = mechanical["passed"] and passed
    record = {**data, "accepted": accepted, "mechanical_passed": mechanical["passed"]}
    folder = Path(session) / "reviews" / identifier
    target = folder / (digest(data) + ".json")
    if not target.exists():
        save(target, record)
    return {"accepted": accepted, "review": str(target), "output_sha256": identifier}


def finalize(session, draft, review_file, *, _close_records=True):
    session, draft = Path(session), Path(draft)
    state = state_for(session, budget=False)
    checked = check(session, draft, budget=False)
    record = load(review_file)
    review_path = Path(review_file).resolve()
    if not review_path.is_relative_to((session / "reviews").resolve()):
        raise ValueError("Use a review accepted through this session.")
    expected_name = digest({key: value for key, value in record.items() if key not in {"accepted", "mechanical_passed"}}) + ".json"
    if review_path.name != expected_name:
        raise ValueError("Review receipt changed after submission.")
    if not assess_review(state, record) or not record.get("accepted") or not checked["passed"] or record.get("output_sha256") != checked["output_sha256"] or record.get("objective_sha256") != state["objective_sha256"]:
        raise ValueError("Delivery requires passing checks and review for these exact output bytes.")
    target = Path(state["frozen"]["request"]["destination"])
    actual = digest(target.read_bytes()) if target.exists() else None
    if actual not in {state["frozen"]["destination_before"], checked["output_sha256"]}:
        raise ValueError("Destination changed; preserve the newer user content.")
    content = draft.read_bytes()
    if digest(content) != checked["output_sha256"]:
        raise ValueError("Draft changed during validation.")
    decision = reviewed_decision(record, content)
    successor = reviewed_successor(record, target)
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as stream:
        temporary = Path(stream.name)
        stream.write(content)
    try:
        os.replace(temporary, target)
    finally:
        temporary.unlink(missing_ok=True)
    state["delivery"] = {"destination": str(target), "output_sha256": checked["output_sha256"], "objective_sha256": state["objective_sha256"], "review": str(review_path), "reviewer": record["reviewer"], "document_status": state["frozen"]["request"]["context"].get("discovery", {}).get("status", "unspecified"), "message_version": 2}
    if decision:
        state["delivery"]["decision"] = decision
    if successor:
        state["delivery"]["successor"] = successor
    # A deterministic handoff reports the actual validation only. Product facts
    # remain in the reviewed artifact rather than an unreviewed final summary.
    message = delivery_message_text(state['delivery'])
    state['delivery'].update(message=message, message_sha256=digest(message.encode()))
    (session / 'message.md').write_text(message)
    save(session / "state.json", state)
    save(session / "delivery.json", state["delivery"])
    if _close_records and (session / record_retention.MARKER).exists():
        record_retention.finish(session, resolved=True, pin='accepted_document:' + checked['output_sha256'])
        record_retention.cleanup(session.parent, 'technical-writer')
    return {"status": "delivered", **state["delivery"]}



def delivery_message_text(receipt):
    target = str(receipt['destination']).replace('>', '%3E').replace('<', '%3C').replace('\n', '%0A').replace('\r', '%0D')
    template = load(ROOT / 'contracts/delivery_message.json')
    status = receipt['document_status']
    status_text = template['status'].format(status=status) if status != 'unspecified' else ''
    decision = receipt.get('decision') if receipt.get('message_version', 1) >= 2 else None
    if decision:
        anchor = str(decision['anchor']).replace('>', '%3E').replace(')', '%29').replace(' ', '-')
        status_text += template['decision'].format(sentence=decision['sentence'], destination=target, anchor=anchor)
    successor = receipt.get('successor') if receipt.get('message_version', 1) >= 2 else None
    if successor:
        status_text += template['successor'].format(document=successor['document'], reason=successor['reason'])
    return template['message'].format(destination=target, status=status_text,
                                      reviewer=template['reviewers'][receipt['reviewer']['kind']])


def reviewed_decision(record, content):
    """An optional decision sentence for the handoff, taken verbatim from the reviewed bytes."""
    decision = record.get("delivery_decision")
    if decision is None:
        return None
    if not isinstance(decision, dict) or set(decision) != {"sentence", "anchor"} or not all(isinstance(v, str) and v.strip() for v in decision.values()):
        raise ValueError("delivery_decision needs a reviewed sentence and its section anchor.")
    text = content.decode("utf-8")
    sentence = decision["sentence"].strip()
    if "\n" in sentence or sentence not in text:
        raise ValueError("The delivery decision must be one sentence copied verbatim from the reviewed document.")
    anchors = {re.sub(r"[^\w\- ]", "", node["title"].lower()).replace(" ", "-") for node in headings(text)}
    if decision["anchor"] not in anchors:
        raise ValueError("The delivery decision's anchor is not a section of the reviewed document.")
    return {"sentence": sentence, "anchor": decision["anchor"]}



def reviewed_successor(record, target):
    """An optional next-document suggestion, bound to the current bytes of the sources it relies on."""
    successor = record.get("delivery_successor")
    if successor is None:
        return None
    if not isinstance(successor, dict) or set(successor) != {"document", "reason", "sources"} or not all(isinstance(successor[k], str) and successor[k].strip() and "\n" not in successor[k] for k in ("document", "reason")):
        raise ValueError("delivery_successor needs a document name, a one-line reason and the source files it relies on.")
    if not isinstance(successor["sources"], list) or not successor["sources"]:
        raise ValueError("delivery_successor must name at least one source file it relies on.")
    bound = {}
    for name in successor["sources"]:
        path = (target.parent / name).resolve() if not Path(name).is_absolute() else Path(name)
        if not path.is_file():
            raise ValueError(f"The suggested next document relies on {name}, which doesn't exist.")
        bound[str(path)] = digest(path.read_bytes())
    return {"document": successor["document"].strip(), "reason": successor["reason"].strip(), "sources": bound}


def stale_successor_sources(receipt):
    """Sources of a bound suggestion whose bytes changed after delivery."""
    successor = receipt.get("successor") or {}
    return sorted(path for path, sha in successor.get("sources", {}).items() if not Path(path).is_file() or digest(Path(path).read_bytes()) != sha)


def verify_message(session, message):
    state = state_for(session, budget=False)
    receipt = state.get('delivery')
    if not receipt or 'message' not in receipt:
        raise ValueError('Finalize the reviewed document before checking its public message.')
    if digest(Path(receipt['destination']).read_bytes()) != receipt['output_sha256']:
        raise ValueError('Delivered document changed after finalization.')
    expected = delivery_message_text(receipt)
    if receipt['message'] != expected or digest(expected.encode()) != receipt['message_sha256']:
        raise ValueError('Delivery message receipt changed.')
    actual = Path(message).read_text()
    findings = [] if actual.rstrip('\r\n') == expected.rstrip('\r\n') else ['Public delivery text differs from the finalized message. Send the returned message unchanged.']
    findings += [f'The suggested next document is stale: {path} changed after delivery. Re-evaluate what to write next before continuing.' for path in stale_successor_sources(receipt)]
    passed = not findings
    return {'passed': passed, 'message_sha256': receipt['message_sha256'],
            'findings': findings,
            'limits': ['This checks the supplied message file; the host transcript must also match. Artifact meaning still needs source-grounded review.']}


def extend(session, attempts, seconds, authorization):
    state = state_for(session, budget=False)
    if state.get("delivery"):
        raise ValueError("The document is already delivered; no extension is needed.")
    request = state["frozen"]["request"]
    current = {"attempts": request["limits"]["max_attempts"] + sum(row["attempts"] for row in state["extensions"]), "seconds": request["limits"]["max_seconds"] + sum(row["seconds"] for row in state["extensions"])}
    receipt = routine_extension(state["extensions"], {"attempts": attempts, "seconds": seconds}, authorization, current=current, hard_limits=request.get("hard_limits"))
    state["extensions"].append({"attempts": attempts, "seconds": seconds, **receipt, "recorded_at": time.time()})
    save(Path(session) / "state.json", state)
    return {"status": "extended", "extension": state["extensions"][-1]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("prepare")
    create.add_argument("--request", type=Path, required=True)
    create.add_argument("--session", type=Path, required=True)
    for name in ("check", "packet", "review", "finalize", "extend", "workflow-packet", "workflow-record", "draft-permission", "verify-message"):
        command = sub.add_parser(name)
        command.add_argument("--session", type=Path, required=True)
        if name in {"check", "packet", "finalize"}:
            command.add_argument("--draft", type=Path, required=True)
        if name in {"review", "finalize"}:
            command.add_argument("--review", type=Path, required=True)
        if name == "verify-message":
            command.add_argument("--message", type=Path, required=True)
        if name == "extend":
            command.add_argument("--attempts", type=int, default=0)
            command.add_argument("--seconds", type=int, default=0)
            command.add_argument("--reason", "--authorization-note", dest="authorization_note", required=True, help="Concrete reason for a bounded retry within the writing task.")
        if name == 'workflow-record':
            command.add_argument('--record', type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.command == "prepare":
            result = prepare(args.request, args.session)
        else:
            with locked(args.session):
                if args.command == "check": result = check(args.session, args.draft)
                elif args.command == "packet": result = packet(args.session, args.draft)
                elif args.command == "review": result = review(args.session, args.review)
                elif args.command == "finalize": result = finalize(args.session, args.draft, args.review, _close_records=False)
                elif args.command == "verify-message": result = verify_message(args.session, args.message)
                elif args.command == 'workflow-packet': result = workflow_packet(args.session)
                elif args.command == 'workflow-record': result = workflow_record(args.session, args.record)
                elif args.command == 'draft-permission': result = draft_permission(args.session)
                else: result = extend(args.session, args.attempts, args.seconds, args.authorization_note)
        if args.command == 'finalize' and (args.session / record_retention.MARKER).exists():
            record_retention.finish(args.session, resolved=True, pin='accepted_document:' + result['output_sha256'])
            record_retention.cleanup(args.session.parent, 'technical-writer')
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 1 if result.get("passed") is False or result.get("accepted") is False and args.command == "review" else 0
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
