# Repository instructions

## Test changes

During implementation, use `scripts/run_tests.py --execute` to run only impacted tests. The script derives changes from the last successful checkpoint or Git HEAD and reports why each check was selected. Do not invoke full unittest/pytest discovery or a full-suite helper directly. Unmapped changes must be assigned an impact rule; they must not trigger a full-suite fallback.

Run the full suite only after the user confirms the batch is finished, with an authorization record bound to the current artifact. Do not create that record without the actual user instruction. Final testing does not grant push approval.

## Routine test retries

Routine testing and necessary retries are part of the authorized task. Choose and record bounded batches from task complexity and observed results; do not ask for each extra test or retry. Use scripts/continuation.py for bounded extensions with a concrete reason. Preserve frozen criteria and all attempts. Stop and report when retries stall or their ceiling is reached. Explicit user hard limits, host permissions, scope changes and paid-service restrictions still apply.

## GitHub approval

Do not push to GitHub without the user's explicit approval for the completed changes being published. An earlier approval does not cover later edits. Prepare a concrete, reviewable result, report its validation, and wait for approval before pushing. A request to continue editing is not push approval.

## Shared instructions

Keep repository workflow rules in AGENTS.md. Always provide CLAUDE.md with an @AGENTS.md import so Claude Code uses the same rules. Preserve this pattern in skills created or maintained by Skill Builder.

## Repository maintenance

Apply references/writing_style.md to every authored text surface, including diagrams, labels, questions, findings and delivery messages, before sending or accepting it. Keep each document format's rules in its owning reference. Preserve source facts, requirements, exceptions, literals and uncertainty when updating guides or examples. Update catalog, contracts, workflow links and affected cases when routing changes.

When changing agent, skill or output-style guidance and examples, apply [the instruction-writing guide](references/agents_and_skills.md) and its [complete example](examples/agents_and_skills.md). Preserve host formats, shared-rule ownership and actual authority and evidence limits.

Use the environment containing scripts/requirements-lock.txt. Run impacted test methods or modules while editing. The impact configuration owns the relevant integrity, regression, wording and example checks. Keep private review records and run snapshots outside the repository.
