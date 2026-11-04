# Repository instructions

## Test changes

During implementation, use `scripts/run_tests.py --execute` to run only impacted tests. The script derives changes from the last successful checkpoint or Git HEAD and reports why each check was selected. Do not invoke full unittest/pytest discovery or a full-suite helper directly. Unmapped changes must be assigned an impact rule; they must not trigger a full-suite fallback.

Run the full suite after the author verifies that every planned implementation change is delivered and no implementation work remains. Use an external implementation-completion record bound to the current artifact; user batch approval is not required. Final validation and publication follow that implementation gate and do not become invented completed implementation steps.

## Routine test retries

Routine testing and necessary retries are part of the authorized task. Choose and record bounded batches from task complexity and observed results; do not ask for each extra test or retry. Use scripts/continuation.py for bounded extensions with a concrete reason. Preserve frozen criteria and all attempts. Stop and report when retries stall or their ceiling is reached. Explicit user hard limits, host permissions, scope changes and paid-service restrictions still apply.

## GitHub approval

Publish within the user's existing explicit authority for the completed deliverable, remote and branch. Routine edits and retries within that scope do not require renewed push approval. If publication is not authorized, prepare the tested result and ask for that remaining action; editing or testing alone grants no push or merge authority.

## Shared instructions

Keep repository workflow rules in AGENTS.md. Always provide CLAUDE.md with an @AGENTS.md import so Claude Code uses the same rules. Preserve this pattern in skills created or maintained by Skill Builder.

## Repository maintenance

Apply references/writing_style.md to every authored text surface, including diagrams, labels, questions, findings and delivery messages, before sending or accepting it. Keep each document format's rules in its owning reference. Preserve source facts, requirements, exceptions, literals and uncertainty when updating guides or examples. Update catalog, contracts, workflow links and affected cases when routing changes.

When changing agent, skill or output-style guidance and examples, apply [the instruction-writing guide](references/agents_and_skills.md) and its [complete example](examples/agents_and_skills.md). Preserve host formats, shared-rule ownership and actual authority and evidence limits.

Use the environment containing scripts/requirements-lock.txt. Run impacted test methods or modules while editing. The impact configuration owns the relevant integrity, regression, wording and example checks. Keep private review records and run snapshots outside the repository.
