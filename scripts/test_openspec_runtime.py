"""W47: the pinned OpenSpec runtime forwards installed commands and runs nothing for unknown ones."""
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import openspec_runtime as runtime

RUNTIME = {"executable": "/pinned/openspec", "version": "2.1.1", "node": "v22.23.5", "lockfile": "lock"}


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.project = Path(temp.name)
        self.calls = []
        def fake(argv, **kwargs):
            self.calls.append((argv, kwargs.get("cwd")))
            return subprocess.CompletedProcess(argv, 0, "Usage: openspec templates" if "--help" in argv else "done", "")
        for patcher in (patch.object(runtime, "ensure", return_value=RUNTIME), patch.object(runtime, "commands", return_value=["init", "list", "status", "validate"]),
                        patch.object(runtime.subprocess, "run", side_effect=fake)):
            patcher.start(); self.addCleanup(patcher.stop)

    def test_default_init_adds_no_host_tools_and_stays_in_the_project(self):
        result = runtime.run("init", [], self.project)
        self.assertEqual(result["argv"], ["init", "--tools=none", "--scope=project"])
        self.assertEqual(self.calls[-1][1], self.project.resolve())

    def test_explicit_native_options_reach_the_cli_unchanged(self):
        result = runtime.run("init", ["--tools", "claude", "--scope", "global"], self.project)
        self.assertEqual(result["argv"], ["init", "--tools", "claude", "--scope", "global"])
        self.assertEqual(runtime.run("status", ["--change", "refunds"], self.project)["argv"], ["status", "--change", "refunds"])

    def test_passing_validate_states_the_native_reply_rule_first(self):
        result = runtime.run("validate", ["refunds"], self.project)
        self.assertEqual(next(iter(result)), "final_reply")
        self.assertEqual(result["final_reply"], runtime.NATIVE_REPLY_RULE)
        self.assertNotIn("final_reply", runtime.run("status", [], self.project))

    def test_unknown_verb_runs_nothing_in_the_project(self):
        with patch.object(runtime, "installed", return_value=False):
            result = runtime.run("frobnicate", ["--x"], self.project)
        self.assertEqual(result["status"], "unknown")
        self.assertEqual(self.calls, [])
        self.assertEqual(list(self.project.iterdir()), [])

    def test_unlisted_command_is_discovered_from_the_cli(self):
        self.calls.clear()
        self.assertTrue(runtime.installed("templates"))
        self.assertEqual(self.calls[-1][0][1:], ["templates", "--help"])


class PrerequisiteTests(unittest.TestCase):
    def test_missing_node_is_reported_before_any_install(self):
        with patch.object(runtime.shutil, "which", return_value=None):
            with self.assertRaisesRegex(runtime.Prerequisite, "Node.js 22.20.0 or later is required"):
                runtime.ensure()

    def test_old_node_is_reported(self):
        with patch.object(runtime.shutil, "which", return_value="/bin/node"), patch.object(runtime.subprocess, "run", return_value=subprocess.CompletedProcess([], 0, "v20.1.0\n", "")):
            with self.assertRaisesRegex(runtime.Prerequisite, "found v20.1.0"):
                runtime.ensure()


class MaintenanceTests(unittest.TestCase):
    """W53: drift is detected, upgrades keep the prior pair, and removal touches only the runtime."""
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.tools = self.root / "tools"
        self.tools.mkdir()
        self.write(self.tools, "2.1.1")
        (self.tools / "node_modules/.bin").mkdir(parents=True)
        (self.tools / "NOTES.md").write_text("A maintainer note.\n")
        patcher = patch.object(runtime, "TOOLS", self.tools)
        patcher.start(); self.addCleanup(patcher.stop)

    def write(self, folder, version, locked=None):
        import json
        folder.mkdir(parents=True, exist_ok=True)
        engines = {"node": ">=22.20.0"}
        (folder / "package.json").write_text(json.dumps({"name": "specdev-openspec-runtime", "private": True, "engines": engines, "dependencies": {runtime.PACKAGE: version}}))
        (folder / "package-lock.json").write_text(json.dumps({"packages": {"": {"dependencies": {runtime.PACKAGE: version}, "engines": engines},
                                                                     "node_modules/" + runtime.PACKAGE: {"version": locked or version}}}))

    def test_manifest_lock_and_cli_mismatches_are_reported(self):
        self.assertEqual(runtime.consistency("2.1.1"), [])
        self.assertIn("SpecDev pins 2.1.1", runtime.consistency("2.2.0")[0])
        self.write(self.tools, "2.1.1", locked="2.1.0")
        self.assertIn("resolves", runtime.consistency()[0])
        self.write(self.tools, "^2.1.1")
        self.assertIn("exact version", runtime.consistency()[0])

    def test_upgrade_previews_keeps_the_prior_pair_and_restores_it_on_failure(self):
        proposal = self.root / "proposal"
        self.write(proposal, "2.2.0")
        plan = runtime.preview(proposal / "package.json", proposal / "package-lock.json")
        self.assertEqual((plan["from"], plan["to"]), ("2.1.1", "2.2.0"))
        self.assertEqual(plan["keeps"], [str(self.tools / "NOTES.md")])
        with patch.object(runtime, "ensure", side_effect=runtime.Prerequisite("npm ci failed")):
            with self.assertRaisesRegex(runtime.Prerequisite, "npm ci failed"):
                runtime.upgrade(proposal / "package.json", proposal / "package-lock.json")
        self.assertEqual(runtime.pinned(), "2.1.1")
        with patch.object(runtime, "ensure", return_value={"version": "2.2.0"}):
            result = runtime.upgrade(proposal / "package.json", proposal / "package-lock.json")
        self.assertEqual((result["status"], runtime.pinned()), ("upgraded", "2.2.0"))
        runtime.restore()
        self.assertEqual(runtime.pinned(), "2.1.1")
        self.assertEqual((self.tools / "NOTES.md").read_text(), "A maintainer note.\n")

    def test_edited_manifest_blocks_upgrade_and_removal_keeps_everything_but_the_runtime(self):
        self.write(self.tools, "2.1.1", locked="2.1.0")
        proposal = self.root / "proposal"
        self.write(proposal, "2.2.0")
        with self.assertRaisesRegex(runtime.Prerequisite, "local edits"):
            runtime.upgrade(proposal / "package.json", proposal / "package-lock.json")
        self.assertFalse((self.tools / ".previous").exists())
        runtime.remove()
        self.assertEqual(sorted(p.name for p in self.tools.iterdir()), ["NOTES.md", "package-lock.json", "package.json"])
