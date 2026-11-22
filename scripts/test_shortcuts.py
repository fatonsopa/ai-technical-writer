"""W35-W37: opt-in shortcuts from the README catalog, without touching content SpecDev doesn't own."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import shortcuts


class ShortcutTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.home = Path(temp.name)
        patcher = patch.object(Path, "home", return_value=self.home)
        patcher.start(); self.addCleanup(patcher.stop)

    def test_catalog_covers_every_documented_command(self):
        rows = shortcuts.catalog()
        names = [row["command"] for row in rows]
        self.assertEqual(len({row["document"] for row in rows}), 39)
        self.assertTrue({"dr", "task", "tasks", "story", "us"} <= set(names))
        self.assertEqual(len(names), len(set(names)))

    def test_every_catalog_command_resolves_to_its_contract_native_artifact_or_guidance(self):
        """W58: each advertised kind and alias has its own route; guidance-only entries keep their role."""
        import json
        documents = json.loads((shortcuts.ROOT / "contracts/documents.json").read_text())["documents"]
        routes = {row["command"]: shortcuts.route(row) for row in shortcuts.catalog()}
        for name, target in routes.items():
            with self.subTest(command=name):
                self.assertTrue(set(target.get("kinds", [])) <= set(documents))
        self.assertEqual(routes["dr"], {"kinds": ["decision"]})
        self.assertEqual(routes["tut"], {"kinds": ["tutorial"]})
        self.assertEqual(routes["brief"], {"kinds": ["brief"]})
        self.assertEqual(routes["design"], {"native": "design"})
        self.assertEqual(routes["epic"], {"guidance": "references/user_story.md#epics"})
        self.assertEqual(routes["story"], routes["us"])

    def test_only_opted_in_names_are_created_and_reinstall_keeps_one_entry(self):
        self.assertFalse((self.home / ".claude/skills").exists())
        result = shortcuts.install("claude-code", ["dr", "task", "tasks"])
        self.assertEqual([r["status"] for r in result], ["installed"] * 3)
        self.assertEqual(sorted(p.name for p in (self.home / ".claude/skills").iterdir()), ["dr", "task", "tasks"])
        page = (self.home / ".claude/skills/dr/SKILL.md").read_text()
        self.assertIn("name: dr", page)
        self.assertIn("Decision Record (DR)", page)
        shortcuts.install("claude-code", ["dr"])
        self.assertEqual(len(list((self.home / ".claude/skills").iterdir())), 3)

    def test_occupied_name_is_preserved_with_a_qualified_alternative_and_removal_keeps_foreign_content(self):
        foreign = self.home / ".agents/skills/task"
        foreign.mkdir(parents=True)
        (foreign / "SKILL.md").write_text("---\nname: task\ndescription: Someone else's task tool.\n---\n")
        result = {r["command"]: r for r in shortcuts.install("codex", ["task", "dr"])}
        self.assertEqual((result["task"]["status"], result["task"]["use"]), ("occupied", "$specdev doc task"))
        self.assertEqual(result["dr"]["use"], "$dr")
        self.assertEqual(shortcuts.remove("codex"), ["dr"])
        self.assertIn("Someone else's", (foreign / "SKILL.md").read_text())
        self.assertFalse((self.home / ".agents/skills/dr").exists())

    def test_unknown_command_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Not in the document catalog: nope"):
            shortcuts.install("codex", ["nope"])
