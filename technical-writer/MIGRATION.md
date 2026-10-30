# Migration guide for the refactored Technical Writer

This file explains how to replace the earlier skill safely. It is a maintainer document and is not loaded for normal writing tasks.

## What changed

The main `SKILL.md` now selects the requested operation and document type. It loads the shared writing guide and the relevant document reference, with a separate workflow for major rewrites. The former main file combined these responsibilities with detailed project-specific rules, historical explanations, exact repository paths, and lengthy audit instructions.

The revised shared writing guide focuses on meaning, context, natural language, useful headings, factual accuracy, and removing repetition. It drops universal rules requiring complete-sentence headings, a bold anchor on each bullet, fixed sentence length, or active voice in every sentence. Those requirements could make ordinary technical explanations sound unnatural.

Each document reference now contains its own purpose, principles, recommended structure, template, completed example, and checks. The package retains the original eleven specialized document types and adds bug reports, incident reports, and architecture decision records. The shared visual guide remains optional.

The separate rewrite workflow still calls the original `zero_loss.py` script, which has been retained without changing its behavior. The `plain_words.py` script has been replaced with a shorter advisory checker. It catches likely padding but does not claim to judge clarity or fail ordinary documentation builds by default.

## Document-by-document changes

| Reference | Main improvement |
| --- | --- |
| `writing-style.md` | Meaning and reader context come first; natural sentence structures and a three-pass review replace mechanical heading and grammar rules. |
| `bug-report.md` | Defines reproducibility, expected and actual results, severity, evidence from data/logs/API records, relevant verified files, and a full example without screenshots. |
| `tutorial.md` | Uses a bounded learning exercise with a clean starting point, expected output, and a completed lesson. |
| `how-to.md` | Focuses on a working procedure, prerequisites, verification, safe failure handling, and recovery. |
| `reference.md` | Defines exact lookup fields, types, defaults, errors, and accurate examples. |
| `explanation.md` | Explains concepts, causes, choices, and tradeoffs without mixing in step-by-step instructions. |
| `requirements.md` | Uses testable, identified requirements with triggers, exceptions, acceptance checks, and explicit open decisions. |
| `architecture.md` | Uses arc42 topics selectively and C4 views when helpful, with current and proposed designs kept distinct. |
| `plan.md` | Uses ordered implementation work with dependencies, tests, deployment, rollback, risks, and approved decisions. A formal RFC remains optional. |
| `standard.md` | Defines binding scope, independent obligations, verification, exceptions, and ownership. |
| `readme.md` | Gives newcomers a short, verified path to use and test a repository, plus links to deeper docs. |
| `agents-and-skills.md` | Separates agents, skills, and output styles, gives validated examples, and warns that platform options can change. |
| `visuals.md` | Chooses diagrams and screenshots by reader need and adds clear labeling and accessibility rules. |
| `incident-report.md` | Adds timelines, impact, causes and unknowns, recovery, and testable follow-up actions. |
| `decision-record.md` | Adds a compact record of context, decision, consequences, and approval status. |

## Important project integrations to review

The old skill included instructions that should continue to apply **where the host project requires them**, but do not belong in a portable writing skill:

1. **Repository worktrees and merges.** The earlier skill required writing in an isolated worktree and referred to `scripts/merge-to-dev.sh` and `CLAUDE.md` sections 9 and 12. Keep this rule in the host project's `CLAUDE.md` or engineering standards if it is still required. The new skill follows project instructions instead of asserting this workflow in every repository.
2. **Documentation locations.** The old skill assumed `.claude/docs/<type>/` and special `.claude/knowledge/<PLAN>/` paths. Keep required paths and naming rules in the project. The new skill uses the location the request or project defines.
3. **Plan-specific generated content.** The old `plan.md` referred to the first H1, an increments table, `04-tests.md`, and parsing scripts. These are implementation contracts for that repository. Check the scripts and preserve the exact markers in the project's plan convention before deploying the new `plan.md`.
4. **Task management ownership.** The old skill used Linear-specific history and issue decisions, while also claiming the issue format belongs to `task-management.md`. Keep assignment, status, decision records, and prioritization in the task management standard. The new bug reference defines the content of a useful defect report.
5. **Referenced heading numbers.** Search the repository for links to sections of the old `SKILL.md` or `writing-style.md`, including `§` references. Update them when replacing the files. The new references do not preserve the old section numbering.
6. **Generated blocks and exact paths.** Search scripts for references to filenames, headings, markers, and blocks before removing or moving content. Preserve script-consumed content exactly or change its consumers in the same repository change.
7. **Tests that parse writing-style.md.** The old `plain_words.py` read the `| Instead of | Write |` table and the tests expected a particular `§6`, `§15`, and 120-column layout. The new script does not parse those tables. Update `src/test/pipeline/technical-writer-skill.test.ts` and any lint task that expects the old table, mandatory passive voice checks, bold anchors, or line wrapping.
8. **Old script flags.** The new `plain_words.py` accepts `--strict`, `--report`, and the legacy `--anchors` flag (ignored). It does not accept the old `--table` or `--also-table` arguments. Update callers before deploying.
9. **Approval procedure for substantive rewrites.** The old skill always stopped for approval before any substantial rewrite. The new workflow still seeks approval when an obligation, decision, or other binding meaning would change without authorization. Explicit user instructions to perform a full refactor are sufficient to proceed with noncontroversial structural changes. If the team wants every rewrite gated, enforce that rule in the project's governing standard.
10. **Independent checks.** `zero_loss.py` helps track text and literal preservation. It cannot prove semantic equivalence. Keep human review of significant requirements, exceptions, and factual corrections.

## Suggested installation sequence

1. Preserve the previous skill folder or the original `technical-writer.zip` so it can be restored.
2. Update repository tests and references listed above, or stage the revised skill under a temporary name for comparison.
3. Copy the new `technical-writer/` folder to the project's `.claude/skills/` location, or install it in the matching personal or plugin skills directory.
4. Run `python3 scripts/validate_skill.py` from inside the revised skill folder. Run `python3 scripts/zero_loss.test.py` and `python3 scripts/plain_words.test.py`.
5. Run your existing project tests and inspect errors arising from changed headings, table parsers, document locations, or old CLI flags.
6. Compare the old and new skills using the same prompts from `evals/evals.json`. Review output quality and token usage under the same conditions.
7. Switch the production skill only after the project's integration checks and representative writing tasks pass.

## Evidence of checks completed for this delivery

The package was checked for missing referenced files, valid main frontmatter, balanced code fences, a short main skill, quality checks in document references, and a 24-case evaluation set. The preserved `zero_loss.py` regression tests passed all nine groups. The updated advisory checker passed its own regression test.

**Limits:** No actual Claude Code or Codex model evaluations were executed from this environment. The new references were reviewed for structure and wording, but they have not yet been tested against a live project with its exact code, issue history, validation scripts, and repository-specific document conventions.

## Industry references used

- Agent Skills specification: https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
- Claude Code skills: https://code.claude.com/docs/en/skills
- Diátaxis documentation types: https://diataxis.fr/
- Google developer documentation style: https://developers.google.com/style
- Microsoft Writing Style Guide: https://learn.microsoft.com/en-us/style-guide/
- arc42 architecture documentation: https://arc42.org/overview/
- C4 diagrams: https://c4model.com/diagrams
- ISO/IEC/IEEE 29148 requirements standard: https://www.iso.org/standard/72089.html
- Mozilla bug reporting: https://bugzilla.mozilla.org/page.cgi?id=bug-writing.html
