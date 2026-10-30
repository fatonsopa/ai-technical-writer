# Migrate the Technical Writer

The main skill selects the operation and document type, then reads the shared writing guide and relevant references. Detailed rewrite safeguards and library maintenance remain separate workflows. Preserve a copy of the previous package and check project integrations before replacing an installed skill.

## Names and responsibilities

Reference filenames use full names with underscores. Familiar request aliases still work; generated project documents follow the destination project's naming conventions.

| Earlier path | Current owner |
| --- | --- |
| `writing-style.md` | `writing_style.md` |
| `spec.md`, `requirements.md` | `spec_driven_development.md` |
| `architecture.md` | `high_level_document.md` |
| `plan.md` | `implementation_plan.md` |
| `decision-record.md` | `decision_record.md` |
| `bug-report.md` | `bug_report.md` |
| `standard.md` | `technical_standard.md` |
| `how-to.md` | `how_to_guide.md` |
| `incident-report.md` | `incident_report.md` |
| `agents-and-skills.md` | `agents_and_skills.md` |
| `workflows/improve-references.md` | `workflows/improve_references.md` |

The generic `reference.md` is retired. Individual requirement writing belongs to SDD; general decisions remain supported, with specialized ADR and DDR guides. `issue.md` retains the shared six-type task format. The transient `work_item.md` name is not canonical; User Story has its own `user_story.md` guide and can be embedded in a task or PRD/SDD.

Added references cover PRD, LLD, ADR, DDR, User Story, Policy, and four testing formats: Test Plan, Test Specification, Test Status Report, and Test Completion Report. Cases, models, and procedures fit within Test Specification when needed. Execution logs are evidence, with no separate writing reference.

The catalog in [SKILL.md](SKILL.md) defines names, aliases, purpose, and create/update triggers. Its diagram shows flexible handoffs. A small task can contain its own expected behavior and acceptance checks; no universal document sequence or automatic separate file is required.

## Preserve project contracts

The original supplied skill included repository-specific worktree, merge, document-location, task-management, and generated-plan rules. These remain binding wherever the host project requires them. Keep them in the project's governing instructions; a portable writer cannot replace those contracts.

Search project callers for renamed paths, section anchors, parser-dependent headings, generated blocks, and script flags. Preserve exact consumed formats or update consumers in the same change. In particular, inspect any plan parser expecting an H1, increments table, or `04-tests.md`, and any writing-style test expecting numbered sections, fixed columns, or a specific wording table. This refactor does not claim those external integrations were tested.

The current `zero_loss.py` and `plain_words.py` retain their execution-baseline behavior. The wording checker is advisory; the preservation checker assists an inventory/mapping review and cannot prove semantic equivalence. Read each script's help before adapting existing commands. This delivery does not claim compatibility with every older script invocation from the original supplied archive.

## Replace an installation

1. Preserve the old folder and locate project instructions and consumers.
2. Update renamed links and any project-specific integration tests.
3. Copy the complete `technical-writer/` directory to the host's supported skill location.
4. Run the package checks listed in the repository README, then the host project's relevant checks.
5. Run representative writing requests with real project sources. Check facts, obligation strength, scoped edits, and reference loading before switching the active installation.

The refactor's [validation report](../analysis/VALIDATION.md) records actual model runs, script tests, example checks, and limits. Claude Code activation and a real project's integrations require their own verification; a valid Markdown package does not establish either.
