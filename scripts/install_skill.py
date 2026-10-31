#!/usr/bin/env python3
"""Install the complete skill repository; preserve an existing installation."""
import argparse
import json
from pathlib import Path
import sys

from repository_files import ROOT, copy_repository, skill_name


def install(source, host, destination=None):
    source = Path(source).resolve()
    if host not in {"codex", "claude-code"}:
        raise ValueError("Unsupported local host.")
    name = skill_name(source)
    base = Path.home() / (".agents/skills" if host == "codex" else ".claude/skills")
    target = Path(destination).expanduser().resolve() if destination else base / name
    if source.is_relative_to(target):
        raise ValueError("Do not install over the source or its parents.")
    files = copy_repository(source, target)
    return {"status": "installed", "name": name, "destination": str(target), "files": len(files)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=["codex", "claude-code"], required=True)
    parser.add_argument("--source", type=Path, default=ROOT)
    parser.add_argument("--destination", type=Path)
    args = parser.parse_args()
    try:
        print(json.dumps(install(args.source, args.host, args.destination), indent=2))
        return 0
    except (OSError, ValueError, KeyError) as error:
        print(json.dumps({"error": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
