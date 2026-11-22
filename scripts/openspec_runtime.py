#!/usr/bin/env python3
"""Run SpecDev's private, pinned OpenSpec CLI in a selected project.

SpecDev ships `tools/openspec/package.json` and its lockfile. This script installs
that exact dependency with `npm ci`, resolves the local `openspec` executable and
forwards any command the installed CLI offers, with the selected project as its
working directory. It owns no OpenSpec command list: the installed CLI decides.
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools/openspec"
PINNED = "2.1.1"
MIN_NODE = (22, 20, 0)


class Prerequisite(Exception):
    """A missing or failed prerequisite, reported with the last confirmed state."""


def node_version():
    node = shutil.which("node")
    if not node:
        raise Prerequisite("Node.js 22.20.0 or later is required for OpenSpec, and node isn't on PATH. Install Node.js, then repeat the request.")
    found = subprocess.run([node, "--version"], capture_output=True, text=True).stdout.strip()
    parts = tuple(int(x) for x in re.findall(r"\d+", found)[:3])
    if parts < MIN_NODE:
        raise Prerequisite(f"OpenSpec needs Node.js 22.20.0 or later; found {found}. Upgrade Node.js, then repeat the request.")
    return found


def environment():
    """Run OpenSpec without telemetry; SpecDev sends no usage data on the user's behalf."""
    import os
    return {**os.environ, "DO_NOT_TRACK": "1", "OPENSPEC_TELEMETRY": "0"}


def executable():
    return TOOLS / "node_modules/.bin/openspec"


def ensure():
    """Install the locked dependency once and report what is installed."""
    node = node_version()
    lock = TOOLS / "package-lock.json"
    if not lock.is_file():
        raise Prerequisite("The OpenSpec lockfile is missing from this SpecDev installation: " + str(lock))
    binary = executable()
    if not binary.exists():
        npm = shutil.which("npm")
        if not npm:
            raise Prerequisite("npm is required to install SpecDev's locked OpenSpec runtime, and npm isn't on PATH.")
        result = subprocess.run([npm, "ci", "--no-audit", "--no-fund"], cwd=TOOLS, capture_output=True, text=True)
        if result.returncode or not binary.exists():
            raise Prerequisite("npm ci failed in " + str(TOOLS) + "; no OpenSpec runtime is installed. " + (result.stderr or result.stdout).strip()[-400:])
    version = subprocess.run([str(binary), "--version"], capture_output=True, text=True, env=environment()).stdout.strip()
    if version != PINNED:
        raise Prerequisite(f"The installed OpenSpec is {version or 'unknown'}, but SpecDev pins {PINNED}. Remove {TOOLS / 'node_modules'} and repeat the request.")
    return {"executable": str(binary), "version": version, "node": node, "lockfile": str(lock)}


def commands():
    """Commands the installed CLI offers, read from its own help."""
    text = subprocess.run([str(executable()), "--help"], capture_output=True, text=True, env=environment()).stdout
    section = text.split("Commands:", 1)[1] if "Commands:" in text else ""
    return sorted({m for m in re.findall(r"^  ([a-z][a-z0-9-]*)", section, re.M)} - {"help"})


def installed(verb):
    """Whether the installed CLI offers a verb, including commands its top-level help doesn't list."""
    if verb in commands():
        return True
    if not re.fullmatch(r"[a-z][a-z0-9-]*", verb):
        return False
    probe = subprocess.run([str(executable()), verb, "--help"], capture_output=True, text=True, env=environment())
    return probe.returncode == 0 and probe.stdout.startswith("Usage: openspec " + verb)


def run(verb, arguments, project):
    """Forward one native command; unknown verbs return a result without running anything."""
    runtime = ensure()
    available = commands()
    if not installed(verb):
        return {"status": "unknown", "command": verb, "message": f"'{verb}' is neither a SpecDev document command nor an installed OpenSpec command. Nothing was run.", "openspec_commands": available}
    project = Path(project).resolve()
    if not project.is_dir():
        raise Prerequisite(f"The selected project {project} doesn't exist.")
    argv = [runtime["executable"], verb, *arguments]
    if verb == "init":
        if not any(a == "--tools" or a.startswith("--tools=") for a in arguments):
            argv.append("--tools=none")
        # Without an explicit choice, keep generated host files in the project, not the user's home.
        if not any(a == "--scope" or a.startswith("--scope=") for a in arguments):
            argv.append("--scope=project")
    result = subprocess.run(argv, cwd=project, capture_output=True, text=True, env=environment())
    return {"status": "ok" if result.returncode == 0 else "failed", "argv": argv[1:], "project": str(project), "exit_code": result.returncode,
            "stdout": result.stdout, "stderr": result.stderr, "openspec": runtime["version"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--project", default=".", help="Project to run in; defaults to the current folder.")
    parser.add_argument("--status", action="store_true", help="Install if needed and report the runtime.")
    parser.add_argument("verb", nargs="?", help="An installed OpenSpec command, such as init, list or templates.")
    parser.add_argument("arguments", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    try:
        result = ensure() if args.status or not args.verb else run(args.verb, args.arguments, args.project)
        print(json.dumps(result, indent=2))
        return 0 if result.get("status", "ok") in ("ok", None) or args.status else (3 if result.get("status") == "unknown" else 1)
    except Prerequisite as error:
        print(json.dumps({"status": "prerequisite", "error": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
