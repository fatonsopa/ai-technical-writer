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
PACKAGE = "@fission-ai/openspec"
OWNED = ("node_modules",)


def manifest():
    return json.loads((TOOLS / "package.json").read_text())


def pinned():
    """The exact version the manifest pins; the manifest is the single source."""
    return manifest()["dependencies"][PACKAGE]


def min_node():
    return tuple(int(x) for x in re.findall(r"\d+", manifest()["engines"]["node"])[:3])


class Prerequisite(Exception):
    """A missing or failed prerequisite, reported with the last confirmed state."""


def node_version():
    node = shutil.which("node")
    if not node:
        raise Prerequisite("Node.js 22.20.0 or later is required for OpenSpec, and node isn't on PATH. Install Node.js, then repeat the request.")
    found = subprocess.run([node, "--version"], capture_output=True, text=True).stdout.strip()
    parts = tuple(int(x) for x in re.findall(r"\d+", found)[:3])
    if parts < min_node():
        raise Prerequisite(f"OpenSpec needs Node.js 22.20.0 or later; found {found}. Upgrade Node.js, then repeat the request.")
    return found


def environment():
    """Run OpenSpec without telemetry; SpecDev sends no usage data on the user's behalf."""
    import os
    return {**os.environ, "DO_NOT_TRACK": "1", "OPENSPEC_TELEMETRY": "0"}


def consistency(installed_version=None):
    """Disagreements between the manifest pin, the lockfile and the installed CLI."""
    findings = []
    pin = pinned()
    if not re.fullmatch(r"\d+\.\d+\.\d+", pin):
        findings.append(f"package.json must pin {PACKAGE} to one exact version; found {pin!r}.")
    lock = json.loads((TOOLS / "package-lock.json").read_text())
    root = lock["packages"][""]
    resolved = lock["packages"].get("node_modules/" + PACKAGE, {}).get("version")
    if root.get("dependencies", {}).get(PACKAGE) != pin:
        findings.append(f"package-lock.json records {PACKAGE} {root.get('dependencies', {}).get(PACKAGE)!r}, but package.json pins {pin}. Regenerate the lockfile.")
    if resolved != pin:
        findings.append(f"package-lock.json resolves {PACKAGE} to {resolved!r}, not {pin}.")
    if root.get("engines") != manifest().get("engines"):
        findings.append("package-lock.json and package.json declare different Node.js engines.")
    if installed_version is not None and installed_version != pin:
        findings.append(f"The installed OpenSpec is {installed_version or 'unknown'}, but SpecDev pins {pin}.")
    return findings


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
    findings = consistency(version)
    if findings:
        raise Prerequisite(" ".join(findings) + f" Nothing was run. To reinstall the pinned runtime, run `scripts/openspec_runtime.py remove`, then repeat the request.")
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


NATIVE_REPLY_RULE = ("If you wrote or edited a native artifact, your final reply is: \"Wrote ARTIFACT for CHANGE. `openspec validate` passed. Only ARTIFACT changed.\" "
                     "(use Edited for an edit), then at most one sentence naming an open decision the artifact records. Add nothing else.")


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
    if verb == "validate" and result.returncode == 0:
        # Every host gets the same reply rule for a native artifact with the passing validation.
        return {"final_reply": NATIVE_REPLY_RULE, "status": "ok", "argv": argv[1:], "project": str(project), "exit_code": 0,
                "stdout": result.stdout, "stderr": result.stderr, "openspec": runtime["version"]}
    return {"status": "ok" if result.returncode == 0 else "failed", "argv": argv[1:], "project": str(project), "exit_code": result.returncode,
            "stdout": result.stdout, "stderr": result.stderr, "openspec": runtime["version"]}


def preview(new_manifest, new_lock):
    """What an upgrade would change, without changing it."""
    current = {"package.json": manifest(), "package-lock.json": json.loads((TOOLS / "package-lock.json").read_text())}
    proposed = {"package.json": json.loads(Path(new_manifest).read_text()), "package-lock.json": json.loads(Path(new_lock).read_text())}
    foreign = sorted(p.name for p in TOOLS.iterdir() if p.name not in {"package.json", "package-lock.json", ".previous", *OWNED})
    return {"from": current["package.json"]["dependencies"][PACKAGE], "to": proposed["package.json"]["dependencies"][PACKAGE],
            "replaces": [str(TOOLS / name) for name in ("package.json", "package-lock.json")], "reinstalls": [str(TOOLS / name) for name in OWNED],
            "keeps": [str(TOOLS / name) for name in foreign], "previous": str(TOOLS / ".previous")}


def upgrade(new_manifest, new_lock):
    """Install a reviewed manifest and lockfile, keeping the prior pair for recovery."""
    if consistency():
        raise Prerequisite("The current manifest and lockfile disagree, so they may hold local edits. Nothing was changed: " + " ".join(consistency()))
    plan = preview(new_manifest, new_lock)
    backup = TOOLS / ".previous"
    backup.mkdir(exist_ok=True)
    for name in ("package.json", "package-lock.json"):
        shutil.copy2(TOOLS / name, backup / name)
    shutil.copy2(new_manifest, TOOLS / "package.json")
    shutil.copy2(new_lock, TOOLS / "package-lock.json")
    try:
        if consistency():
            raise Prerequisite("The proposed manifest and lockfile disagree: " + " ".join(consistency()))
        remove()
        return {**plan, "status": "upgraded", "runtime": ensure()}
    except Prerequisite:
        restore()
        raise


def restore():
    """Put back the prior manifest and lockfile and reinstall them."""
    backup = TOOLS / ".previous"
    if not (backup / "package.json").is_file():
        raise Prerequisite("No prior OpenSpec manifest is kept in " + str(backup) + ".")
    for name in ("package.json", "package-lock.json"):
        shutil.copy2(backup / name, TOOLS / name)
    remove()
    return {"status": "restored", "version": pinned()}


def remove():
    """Remove only the installed runtime; the manifest, lockfile and any other file stay."""
    removed = []
    for name in OWNED:
        path = TOOLS / name
        if path.exists():
            shutil.rmtree(path)
            removed.append(str(path))
    return {"status": "removed", "removed": removed}


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--project", default=".", help="Project to run in; defaults to the current folder.")
    parser.add_argument("--status", action="store_true", help="Install if needed and report the runtime.")
    parser.add_argument("--check", action="store_true", help="Compare the manifest pin, lockfile and installed CLI without installing.")
    parser.add_argument("--preview", nargs=2, metavar=("MANIFEST", "LOCK"), help="Show what upgrading to a reviewed manifest and lockfile would change.")
    parser.add_argument("--upgrade", nargs=2, metavar=("MANIFEST", "LOCK"), help="Upgrade to a reviewed manifest and lockfile, keeping the prior pair.")
    parser.add_argument("--restore", action="store_true", help="Reinstall the prior manifest and lockfile.")
    parser.add_argument("--remove", action="store_true", help="Remove only the installed runtime (node_modules).")
    parser.add_argument("verb", nargs="?", help="An installed OpenSpec command, such as init, list or templates.")
    parser.add_argument("arguments", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    try:
        maintenance = (args.preview and preview(*args.preview)) or (args.upgrade and upgrade(*args.upgrade)) or (args.restore and restore()) or (args.remove and remove())
        if maintenance:
            print(json.dumps(maintenance, indent=2))
            return 0
        if args.check:
            version = subprocess.run([str(executable()), "--version"], capture_output=True, text=True, env=environment()).stdout.strip() if executable().exists() else None
            findings = consistency(version)
            print(json.dumps({"passed": not findings, "pinned": pinned(), "installed": version, "findings": findings}, indent=2))
            return 0 if not findings else 4
        result = ensure() if args.status or not args.verb else run(args.verb, args.arguments, args.project)
        print(json.dumps(result, indent=2))
        return 0 if result.get("status", "ok") in ("ok", None) or args.status else (3 if result.get("status") == "unknown" else 1)
    except Prerequisite as error:
        print(json.dumps({"status": "prerequisite", "error": str(error)}), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
