"""Check recorded discovery without pretending to infer decisions from prose."""
import re

def discovery_errors(record, source_ids=None):
    if not isinstance(record, dict) or set(record) != {"status", "source_ids", "decisions"}:
        return ["Discovery needs status, source_ids and decisions."]
    errors = []
    if record["status"] not in ("ready", "draft"):
        errors.append("Discovery status must be ready or draft.")

    def sources(values):
        valid = isinstance(values, list) and bool(values) and all(isinstance(v, str) and v.strip() for v in values)
        if not valid or source_ids is not None and any(v not in source_ids for v in values):
            errors.append("Discovery must refer to nonempty captured source IDs.")

    sources(record["source_ids"])
    decisions = record["decisions"]
    if not isinstance(decisions, list):
        return errors + ["Discovery decisions must be a list."]
    seen = set()
    for row in decisions:
        if not isinstance(row, dict) or set(row) != {"id", "question", "status", "blocking", "answer", "source_ids"}:
            errors.append("Each discovery decision needs id, question, status, blocking, answer and source_ids.")
            continue
        if any(not isinstance(row[k], str) or not row[k].strip() for k in ("id", "question")):
            errors.append("Discovery decisions need nonempty IDs and questions.")
        elif row["id"] in seen:
            errors.append("Discovery decision IDs must be unique.")
        else:
            seen.add(row["id"])
        if row["status"] not in ("open", "resolved") or type(row["blocking"]) is not bool:
            errors.append("Discovery decisions need open/resolved status and boolean blocking.")
        if not isinstance(row["answer"], str):
            errors.append("Discovery answers must be strings.")
        if row["status"] == "resolved":
            if not isinstance(row["answer"], str) or not row["answer"].strip():
                errors.append("A resolved decision needs its actual answer.")
            sources(row["source_ids"])
        elif row["status"] == "open":
            if row["answer"] or row["source_ids"]:
                errors.append("An open decision cannot contain a claimed answer or answer sources.")
            if row["blocking"] and record["status"] == "ready":
                errors.append("An unresolved blocking decision prevents ready delivery: " + str(row["id"]))
    return errors


def check_discovery(text, record):
    errors = discovery_errors(record)
    if errors:
        return errors
    # Ignore fenced examples: a quoted 'Status: Draft' is not the document's status.
    header, fence = [], None
    for line in text.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
            continue
        if marker:
            fence = marker[1][0], len(marker[1])
        elif re.match(r"^##\s", line):
            break
        else:
            header.append(line)
    if record["status"] == "draft" and not re.search(r"(?mi)^Status:\s*Draft\b", "\n".join(header)):
        errors.append("Draft discovery requires Status: Draft before the document sections.")
    if record["status"] == "draft":
        for row in record["decisions"]:
            if row["status"] == "open" and not re.search(r"(?<![\w-])" + re.escape(row["id"]) + r"(?![\w-])", text):
                errors.append("Draft must identify its open decision: " + row["id"])
    return errors
