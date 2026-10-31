# Technical Writer

Write, edit, review, and rewrite technical documents using shared language guidance and document-specific references. Supported outputs include issues, PRDs, behavioral specifications, architecture, implementation plans, decision records, governance, testing reports, tutorials, and READMEs.

The [catalog and workflow](SKILL.md) explain when to use each format. The skill preserves source facts, requirements, exceptions, exact values, and uncertainty. Complete documents are checked against [versioned output contracts](contracts/documents.json); accepted delivery also requires a source-grounded review of the actual draft.

## Requirements

- A host with file access and code execution: Codex, filesystem-enabled ChatGPT desktop, Claude Code, or a Claude environment supporting custom skills and Python.
- Python 3.11 or later on macOS, Linux, or WSL, with the packages in `scripts/requirements-lock.txt`.
- Source facts, a draft, or project files appropriate to the requested task. Missing evidence stays visible.

An external model CLI is optional. The native evaluation workflow uses the model already available in your host.

## Installation

### Get the source

```sh
git clone https://github.com/fatonsopa/ai-technical-writer.git technical-writer
cd technical-writer
```

You can also download and extract the repository ZIP, then open its `technical-writer` folder.

### Codex and ChatGPT desktop

```sh
python3 scripts/install_skill.py --host codex
```

The installer prints its destination, normally `~/.agents/skills/technical-writer`. Invoke `$technical-writer` in Codex or select `@technical-writer` in ChatGPT desktop. If discovery does not refresh, start a new session or restart the app.

### Claude Code

```sh
python3 scripts/install_skill.py --host claude-code
```

The normal destination is `~/.claude/skills/technical-writer`. Invoke `/technical-writer` in Claude Code. An existing installation is preserved; use `--destination NEW_FOLDER` to test a separate installation.

### Set up the Python environment

Change to the installed folder printed by the installer, then run:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements-lock.txt
.venv/bin/python scripts/smoke_check.py
```

The self-check reports `passed: true`. It checks installed resources and exercises the document gate; it does not establish writing quality across all future inputs.

The repository is the complete skill. You can download its GitHub ZIP instead of cloning. For a Claude custom-skill upload, extract the repository, give the folder the name `technical-writer`, and compress that folder with your archive tool. Enable code execution in the host. See [Claude's upload instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).

## Quick start

Examples use Codex's `$technical-writer` invocation. Use `/technical-writer` in Claude Code or `@technical-writer` in ChatGPT desktop.

> $technical-writer Write a Bug report from these facts: a category change was observed once; Save closed the dialog, but a fresh read still returned the old category. The expected behavior is that a confirmed save persists the chosen category. We have no inspected code or logs. Keep expected and actual results separate, preserve the unknown reproduction frequency, and do not invent a cause or file path.

Expected result: a scoped bug report with **How to reproduce**, **Expected result**, **Actual result**, **Relevant files**, and the other required report sections. It attributes the observations, preserves the evidence gaps, and proposes verification without claiming tests ran.

With code/file tools, the skill stages a draft, runs its applicable checks, reviews it against the source, and delivers the accepted file with a receipt. Without those tools or a completed review, it can provide a clearly identified draft; it must not claim validated acceptance.

## Usage scenarios

### Create a complete document

> $technical-writer Write a PRD from the attached product brief. Use the PRD reference and output contract. Separate agreed scope, proposed capabilities, and unresolved goals. Save the accepted document to the requested project path.

You receive a complete product document with the required sections and source-supported content. A heading check cannot replace the review of its purpose, facts, and scope.

### Make a focused edit

> $technical-writer Change only this issue's title to describe the observed failure. Preserve the description and every other field.

You receive the requested title change. A file edit preserves content outside its declared title or excerpt; it does not expand into a complete document rewrite.

### Review a document

> $technical-writer Review this implementation plan against the supplied SDD. Return located gaps and recommended corrections. Do not rewrite the plan.

You receive findings tied to the source requirements. A review does not overwrite the document being reviewed or authorize implementation.

### Rewrite while preserving obligations

> $technical-writer Rewrite this technical standard for clarity. Preserve every obligation, exception, limit, and identifier. Explain any unresolved contradiction before changing its meaning.

The result retains the required governance structure and is checked against the original text. The preservation tools assist the comparison; semantic review is still required.

### Improve after a failed output

> $technical-writer This output omitted a required PRD section. Correct the draft and identify the reusable guidance or check responsible for the miss. Keep the failing input and output as a regression case; preserve unrelated guidance.

The failure remains recorded. A repaired draft needs new checks and review; a previous receipt does not transfer to changed content. Persistent skill maintenance follows the authorized scope.

## Validate and deliver a document

The host normally runs this workflow for you. Use [the document-gate commands](workflows/rewrite.md#validate-the-actual-output) to inspect it or run it yourself. A request identifies the document type, operation, scope, source inputs, destination, explicit requirements, and material values to preserve.

1. `prepare` captures the source, destination baseline, selected guides, contract, and validator identity.
2. `check` validates the draft's structure and declared data constraints.
3. `packet` supplies the actual draft and frozen evidence for review.
4. `review` validates the submitted judgment, including every explicit requirement.
5. `finalize` delivers only the exact reviewed bytes when the applicable gates pass.

Missing sections, incorrect hierarchy, failed requirements, stale reviews, changed inputs, and newer destination edits block accepted delivery. Required structure does not authorize inventing content to fill a gap. Narrow edits and reviews use their own scope.

## Evaluate and improve the skill

Start with one representative case. From the installed skill folder:

```sh
.venv/bin/python evals/run.py prepare --session ../writer-eval-prd --kind prd --operation create --max-handoffs 2 --max-seconds 600 --host unknown
.venv/bin/python evals/run.py packet --session ../writer-eval-prd --case prd-create --phase generate
```

Use a new session path outside the skill for each attempt. The host performs the generation request, then submits its structured response with `submit --session SESSION --response RESPONSE.json`. A structurally valid output then receives a `grade` packet and a source-grounded judgment. See [evaluation instructions](evals/README.md) for the complete response format, custom input fixtures, expected properties, optional CLI adapters, and failure handling.

```sh
.venv/bin/python evals/run.py assess --session ../writer-eval-prd
```

| Result | Meaning |
| --- | --- |
| `task_success_percent` | Accepted attempts divided by evaluated attempts |
| `coverage_percent` | Evaluated attempts divided by planned attempts |
| `critical_failures` | Failed mandatory checks; these block acceptance |
| `pending_review` | Generated outputs still awaiting a valid judgment |
| `accepted` | Target, full coverage, critical checks, and reviews all pass |

Eight accepted results out of ten evaluated results is 80% task success. If twelve were planned, coverage is 83.3%. With no evaluated attempts, success is unmeasured. Malformed or structurally wrong task outputs count as failures. Missing execution or review leaves incomplete coverage. These are sampled task results, not universal accuracy.

Review failed outputs against their original inputs before changing the skill. Add a faithful regression, make a scoped correction, and rerun unchanged criteria on a new captured version. Use separate acceptance cases to assess generalization. Report the original failure as well as the retest.

The scripts enforce declared attempt/handoff and runtime allowances. When a limit is reached below target, the host reports the gap and requests a bounded extension. Extend only with the user's actual authorization; do not change targets or expected answers to obtain a pass. Native handoffs count phase packets, not hidden provider requests or a billing cap.

## Troubleshooting and help

- **The skill is missing:** confirm the installed folder contains `SKILL.md` and use your host's explicit invocation. Refresh the session if needed.
- **A Python import fails:** run the environment setup with the installed `scripts/requirements-lock.txt` and use `.venv/bin/python`.
- **Checks reject a draft:** read the actual findings. Correct missing structure or data; do not add unsupported facts or weaken the contract.
- **An input, guide, or evaluator changed:** preserve the old evidence and prepare a new versioned session.
- **A result remains pending:** obtain the required review. A high aggregate score cannot waive critical failures or missing coverage.

For support, [open an issue](https://github.com/fatonsopa/ai-technical-writer/issues) with the skill version, host, sanitized input, expected result, actual result, and reproduction steps. Keep credentials and private project data out of public reports.

## Development

The repository includes regression tests. From the skill folder with dependencies installed:

```sh
.venv/bin/python scripts/validate_skill.py
.venv/bin/python -m unittest discover -s scripts -p 'test_*.py'
.venv/bin/python scripts/plain_words.test.py
.venv/bin/python scripts/zero_loss.test.py
.venv/bin/python scripts/check_examples.py
```

Test actual output contracts and invalid-output controls as well as package integrity. Installation uses the same public repository files, including its tests. Private records, run snapshots and local environments stay outside the installed copy.


## Repository responsibilities

`SKILL.md` coordinates writing. `references/` owns document and language guidance; `examples/` demonstrates it. `contracts/` owns output structures. `scripts/` handles validation, accepted delivery and installation. `evals/` owns behavioral cases and assessment; its `adapters/` folder contains optional provider transport. `config/` records layout and component ownership. These components share contracts and preserve the distinction between mechanical checks and source-grounded judgment.

## License

[MIT](LICENSE).
