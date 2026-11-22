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
        for patcher in (patch.object(runtime, "ensure", return_value=RUNTIME), patch.object(runtime, "commands", return_value=["init", "list", "status"]),
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
