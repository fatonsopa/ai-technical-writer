"""Verify complete repository installation, private exclusions and user links."""
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import zipfile

from install_skill import install
from repository_files import copy_repository, inventory
from validate_skill import validate

ROOT = Path(__file__).resolve().parents[1]


class PackageDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.folder = Path(self.temp.name)

    def tearDown(self):
        self.temp.cleanup()

    def test_repository_installs_and_checks_without_builder(self):
        target = self.folder / "technical-writer"
        install(ROOT, "codex", target)
        self.assertTrue((target / "README.md").is_file())
        self.assertTrue(list((target / "scripts").glob("test_*.py")))
        self.assertTrue(list((target / "scripts").glob("*.test.py")))
        self.assertIn("## Development", (target / "README.md").read_text())
        self.assertTrue(validate(target)["valid"])
        process = subprocess.run([sys.executable, str(target / "scripts/smoke_check.py")], cwd=self.folder, capture_output=True, text=True)
        self.assertEqual(process.returncode, 0, process.stdout + process.stderr)
        self.assertTrue(json.loads(process.stdout)["passed"])

    def test_existing_installation_is_preserved(self):
        target = self.folder / "technical-writer"
        install(ROOT, "claude-code", target)
        marker = target / "user-note.txt"
        marker.write_text("Keep the user's installation.")
        with self.assertRaises(ValueError):
            install(ROOT, "claude-code", target)
        self.assertEqual(marker.read_text(), "Keep the user's installation.")

    def test_repository_is_the_single_complete_artifact(self):
        target = self.folder / "copy"
        before = inventory(ROOT)
        copy_repository(ROOT, target)
        self.assertEqual(before, inventory(target))
        for name in ("SKILL.md", "README.md", "LICENSE", "scripts/requirements-lock.txt"):
            self.assertTrue((target / name).is_file(), name)
        self.assertFalse((target / "dist").exists())
        self.assertFalse((target / "distribution.json").exists())

    def test_private_files_are_not_selected_even_if_created_locally(self):
        source = self.folder / "source"
        copy_repository(ROOT, source)
        for name in ("docs/internal/private.md", "evals/runs/record.json", ".venv/secret.txt"):
            file = source / name
            file.parent.mkdir(parents=True, exist_ok=True)
            file.write_text("PRIVATE_SENTINEL")
        for profile in ("source", "runtime"):
            names = inventory(source, profile)
            self.assertFalse(any(name in names for name in ("docs/internal/private.md", "evals/runs/record.json", ".venv/secret.txt")))

    def test_all_installed_documentation_links_are_checked(self):
        source = self.folder / "source"
        copy_repository(ROOT, source)
        for name in ("README.md", "evals/README.md"):
            path = source / name
            old = path.read_text()
            path.write_text(old + "\n[Missing](missing-file.md)\n")
            result = validate(source)
            self.assertFalse(result["valid"])
            self.assertTrue(any("Broken local link: " + name in error for error in result["errors"]))
            path.write_text(old)

    def test_authored_examples_satisfy_the_same_output_contracts_as_generation(self):
        sys.path.insert(0, str(ROOT / "evals"))
        import audit_examples
        paths = sorted((ROOT / "examples").glob("*.md"))
        packet = audit_examples.make_packet(paths)
        response = {"packet_sha256": packet["packet_sha256"], "reviewer": {"kind": "current_host_self_review", "identity": "Unit control", "model": None, "method": "Authored score control tests only the mechanical acceptance path."}, "results": [{"id": path.stem, "scores": [3] * 7, "critical_failures": [], "reasons": ["A synthetic grade is not semantic-quality evidence."]} for path in paths]}
        result = audit_examples.assess_packet(packet, response)
        failures = {row["id"]: row["critical_failures"] for row in result["results"] if not row["passed"]}
        self.assertTrue(result["accepted"], failures)

    def test_bootstrap_installer_works_without_yaml_import(self):
        target = self.folder / "bootstrap" / "technical-writer"
        process = subprocess.run([sys.executable, "-S", str(ROOT / "scripts/install_skill.py"), "--host", "codex", "--destination", str(target)], capture_output=True, text=True)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertTrue((target / "scripts/requirements-lock.txt").is_file())


if __name__ == "__main__":
    unittest.main()
