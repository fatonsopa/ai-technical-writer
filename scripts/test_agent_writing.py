"""Instruction example/routing controls; no claim of actual host activation."""
import json
from pathlib import Path
import re
import unittest

from document_contracts import validate
from validate_skill import blocks

ROOT = Path(__file__).resolve().parents[1]


class AgentWritingTests(unittest.TestCase):
    def examples(self):
        return [body for tag, body in blocks((ROOT / 'examples/agents_and_skills.md').read_text())[0] if tag == 'md']

    def test_all_three_actual_configurations_pass_their_output_contract(self):
        examples = self.examples()
        self.assertEqual(len(examples), 3)
        for kind, content in zip(('agent', 'skill', 'output_style'), examples):
            self.assertTrue(validate(content, kind)['passed'], kind)
            self.assertFalse(validate(content.replace('description:', 'unknown-field:', 1), kind)['passed'], kind)

    def test_read_only_agent_and_output_style_keep_their_existing_fields(self):
        agent, skill, style = self.examples()
        self.assertIn('tools: Read, Glob, Grep', agent)
        self.assertIn('name: website-review-migration-reviewer', agent)
        self.assertIn('name: website-review-summary', skill)
        self.assertIn('keep-coding-instructions: true', style)
        self.assertIn('This communication style does not authorize implementation or external actions.', style)

    def test_shared_rules_and_optional_role_are_substantive_in_the_skill_example(self):
        skill = self.examples()[1]
        for heading in ('Shared evidence rules', 'Lead and optional batch review'):
            section = re.search(r'^## ' + re.escape(heading) + r'\n(.+?)(?=^## |\Z)', skill, re.M | re.S)
            self.assertIsNotNone(section)
            self.assertGreater(len(section[1].split()), 30)
        self.assertEqual(skill.count('Distinguish a definite server rejection from response loss after a possible commit.'), 1)
        self.assertIn('This skill does not authorize category writes, retries, database reads, tracker changes, or external messages.', skill)

    def test_catalog_and_maintenance_routes_resolve_without_new_document_kinds(self):
        contracts = json.loads((ROOT / 'contracts/documents.json').read_text())
        for kind in ('agent', 'skill', 'output_style'):
            self.assertEqual(contracts['documents'][kind]['reference'], 'references/agents_and_skills.md')
        for name in ('SKILL.md', 'AGENTS.md'):
            links = re.findall(r'\]\(([^)]+)\)', (ROOT / name).read_text())
            self.assertIn('references/agents_and_skills.md', links)
            self.assertTrue((ROOT / 'references/agents_and_skills.md').is_file())
        guide = (ROOT / 'references/agents_and_skills.md').read_text()
        for target in ('policy.md', 'technical_standard.md'):
            self.assertIn('](' + target + ')', guide)
            self.assertTrue((ROOT / 'references' / target).is_file())
