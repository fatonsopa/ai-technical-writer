# AI Technical Writer

A reusable skill for creating, editing, reviewing, and rewriting technical documents. It applies a shared writing guide, selects the relevant document reference, and preserves source facts, requirements, exceptions, and uncertainty.

Start with [SKILL.md](technical-writer/SKILL.md) for the document catalog and workflow diagram. [Writing style](technical-writer/references/writing_style.md) governs the prose of both the guides and their outputs. The package has 25 references covering 32 evaluated output kinds, including six task types, specifications, design, decisions, governance, testing, and instructional documents.

The package includes 24 [complete worked examples](technical-writer/examples/readme.md) from one Websites Review initiative. Each reference links to its matching example. Full creation and substantial rewriting load the relevant example; narrow edits stay focused. The examples demonstrate appropriate substance and connected requirements, design, delivery, and testing without imposing a fixed document length.

The specification defines expected behavior; design and implementation plans explain how to achieve it. Small tasks can carry their own expected behavior and acceptance criteria. The skill does not require a separate file for every format or one universal development sequence.

## Use the skill

Place the entire `technical-writer/` directory in a skill location supported by your host. For a Codex project, use `.agents/skills/technical-writer/`; for a Claude Code project, use `.claude/skills/technical-writer/`. Keep references, examples, scripts, and workflows beside SKILL.md. These locations follow the [Codex skill documentation](https://learn.chatgpt.com/docs/build-skills) and [Claude Code skill documentation](https://code.claude.com/docs/en/skills), checked on 2026-10-31. This repository does not install the skill automatically.

Ask by acronym, full name, or a familiar alias, and supply the source facts or files:

- “Write an SDD for this feature. Separate agreed requirements from unresolved behavior.”
- “Review this High Level Document against the specification.”
- “Draft a Bug task from these observations. We have no reproduction or root cause yet.”
- “Rewrite this Technical Standard while preserving every obligation and exception.”

The [migration guide](technical-writer/MIGRATION.md) describes renamed files and project integrations to check. The skill drafts content at the requested destination; posting to trackers, implementation, and deployment require their own authorization.

## Validate changes

From the repository root:

```bash
python3 technical-writer/scripts/validate_skill.py
python3 -m unittest discover -s technical-writer/scripts -p 'test_*.py'
python3 technical-writer/scripts/plain_words.test.py
python3 technical-writer/scripts/zero_loss.test.py
python3 technical-writer/scripts/check_examples.py
```

These checks use Python's standard library. Behavioral evaluation additionally requires an authenticated Codex CLI and an available model; see [evaluation instructions](technical-writer/evals/README.md). Static checks do not establish writing quality or future model reliability.

The [execution specification](analysis/SKILL-SPEC.md), [reference audit](analysis/REVIEW-LEDGER.md), and [validation report](analysis/VALIDATION.md) record this refactor. [Skill-building lessons](analysis/SKILL-CREATION-LESSONS.md) capture evidence for future work. Maintenance records and evaluation data stay outside normal writing context.
