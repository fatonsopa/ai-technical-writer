#!/usr/bin/env python3
"""Opt-in document shortcuts generated from the README catalog.

Each shortcut is a small skill folder in the host's skills directory that hands
the request to SpecDev with one document selected. Setup writes only names the
user chooses, never replaces content it doesn't own, and removes only its own.
"""
import argparse
import json
from pathlib import Path
import re
import shutil
import sys

from repository_files import ROOT, skill_name

MARKER = "<!-- specdev shortcut -->"
HOSTS = {"codex": ".agents/skills", "claude-code": ".claude/skills"}
INVOKE = {"codex": "$", "claude-code": "/"}


def catalog(root=ROOT):
    """Command names, document names and guide links from the README's supported-document table."""
    text = (Path(root) / "README.md").read_text()
    rows = []
    for commands, document, link in re.findall(r"^\| (`/[^|]+`) \| \[([^\]]+)\]\(([^)]+)\) \|", text, re.M):
        for name in re.findall(r"`/([a-z0-9-]+)`", commands):
            rows.append({"command": name, "document": document, "guide": link})
    if not rows:
        raise ValueError("The README has no supported-document catalog to read.")
    return rows


def entry(row, skill):
    return (f"---\nname: {row['command']}\ndescription: Write or edit a {row['document']} with {skill}. Shortcut for '{skill} doc {row['command']}'.\n---\n\n"
            f"{MARKER}\n\nHand this request to the installed `{skill}` skill as `doc {row['command']}`: "
            f"the user wants a {row['document']}. Follow {skill}'s instructions, its catalog and its checks exactly as if the request had used the full document name. "
            "An OpenSpec operation or artifact configured in the selected change takes precedence over this shortcut.\n")


def install(host, names, root=ROOT):
    base = Path.home() / HOSTS[host]
    rows = {row["command"]: row for row in catalog(root)}
    wanted = sorted(rows) if names == ["all"] else names
    unknown = sorted(set(wanted) - set(rows))
    if unknown:
        raise ValueError("Not in the document catalog: " + ", ".join(unknown))
    skill, results = skill_name(root), []
    for name in wanted:
        folder = base / name
        page = folder / "SKILL.md"
        if folder.exists() and not (page.is_file() and MARKER in page.read_text()):
            results.append({"command": name, "status": "occupied", "path": str(folder), "use": f"{INVOKE[host]}{skill} doc {name}"})
            continue
        folder.mkdir(parents=True, exist_ok=True)
        page.write_text(entry(rows[name], skill))
        results.append({"command": name, "status": "installed", "path": str(folder), "use": f"{INVOKE[host]}{name}"})
    return results


def remove(host, root=ROOT):
    base = Path.home() / HOSTS[host]
    names = {row["command"] for row in catalog(root)}
    removed = []
    for name in sorted(names):
        page = base / name / "SKILL.md"
        if page.is_file() and MARKER in page.read_text() and set(p.name for p in page.parent.iterdir()) == {"SKILL.md"}:
            shutil.rmtree(page.parent)
            removed.append(name)
    return removed


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="action", required=True)
    sub.add_parser("list")
    add = sub.add_parser("install"); add.add_argument("--host", choices=sorted(HOSTS), required=True); add.add_argument("names", nargs="+", help="Catalog commands such as dr task tasks, or all.")
    drop = sub.add_parser("remove"); drop.add_argument("--host", choices=sorted(HOSTS), required=True)
    args = parser.parse_args()
    try:
        result = catalog() if args.action == "list" else install(args.host, args.names) if args.action == "install" else {"removed": remove(args.host)}
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, ValueError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
