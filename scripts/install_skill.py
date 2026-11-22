#!/usr/bin/env python3
"""Install the complete skill repository and its former-name entry; preserve installations it does not own."""
import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import shutil
import sys

from repository_files import ROOT, copy_repository, skill_name

LEGACY = "technical-writer"
REPOSITORY = "github.com/fatonsopa/ai-technical-writer"
LEGACY_MARKER = "<!-- specdev legacy entry -->"


class Collision(ValueError):
    """The destination holds an installation this installer must preserve."""


def is_this_skill(folder):
    """An installation of this repository, under either name."""
    readme = Path(folder) / "README.md"
    return (Path(folder) / "scripts/validate_document.py").is_file() and readme.is_file() and REPOSITORY in readme.read_text()


def legacy_entry(target):
    return (f"---\nname: {LEGACY}\ndescription: Former name of SpecDev. Use for existing technical-writer requests; it hands each one to the installed specdev skill.\n---\n\n"
            f"{LEGACY_MARKER}\n\n# Former name of SpecDev\n\n"
            f"This entry keeps the former `/technical-writer` and `$technical-writer` invocations working. "
            f"Read the installed SpecDev skill at `{target}/SKILL.md` and follow it for this request, with its scripts and references from that folder. "
            "Treat the request exactly as if it had used `/specdev` or `$specdev`.\n")


def install(source, host, destination=None):
    source = Path(source).resolve()
    if host not in {"codex", "claude-code"}:
        raise ValueError("Unsupported local host.")
    name = skill_name(source)
    base = Path.home() / (".agents/skills" if host == "codex" else ".claude/skills")
    target = Path(destination).expanduser().resolve() if destination else base / name
    if source.is_relative_to(target):
        raise ValueError("Do not install over the source or its parents.")
    if target.exists():
        owner = "an earlier SpecDev installation" if is_this_skill(target) else "another skill or folder that SpecDev did not install"
        raise Collision(f"{target} already holds {owner}. It was left unchanged. Move it or use --destination NEW_FOLDER.")
    files = copy_repository(source, target)
    result = {"status": "installed", "name": name, "destination": str(target), "files": len(files)}
    if destination is None:
        result["legacy"] = install_legacy(base / LEGACY, target, host)
    return result


def install_legacy(folder, target, host):
    """Keep the former name working; replace only an entry or installation this skill owns."""
    skill = folder / "SKILL.md"
    if folder.exists():
        if skill.is_file() and LEGACY_MARKER in skill.read_text():
            skill.write_text(legacy_entry(target))
            return {"status": "updated", "destination": str(folder)}
        if not is_this_skill(folder):
            return {"status": "preserved", "destination": str(folder), "reason": "An unrelated technical-writer skill is installed there; invoke SpecDev as specdev."}
        stem = Path.home() / ".local/share/specdev/backups" / (host + "-" + LEGACY + "-" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ"))
        backup, number = stem, 1
        while backup.exists():
            number += 1
            backup = stem.with_name(stem.name + "-" + str(number))
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(folder), str(backup))
        result = {"status": "replaced", "destination": str(folder), "previous_installation": str(backup)}
    else:
        result = {"status": "installed", "destination": str(folder)}
    folder.mkdir(parents=True)
    skill.write_text(legacy_entry(target))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=["codex", "claude-code"], required=True)
    parser.add_argument("--source", type=Path, default=ROOT)
    parser.add_argument("--destination", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(install(args.source, args.host, args.destination), indent=2))
        return 0
    except Collision as error:
        print(json.dumps({"error": str(error), "kind": "collision"}), file=sys.stderr)
        return 3
    except (OSError, ValueError, KeyError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
