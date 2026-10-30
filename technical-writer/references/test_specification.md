# Test Specification (TS)

A test specification defines the checks and procedures used to assess required behavior. Create it before the relevant tests run; update it when behavior, coverage, data, or execution procedures change. The result can be a task section, a test-management record, a table linked to executable tests, or a standalone document.

## Principles

- Trace checks to [SDD](spec_driven_development.md) requirements or exact acceptance criteria. Expected results come from those sources, not from whatever the current code happens to do.
- Choose cases that distinguish meaningful normal, error, permission, and boundary behavior. State what is covered and what remains outside scope.
- Give each case an identifiable objective, preconditions, inputs/actions, and observable expected outcome.
- Include execution order, setup, cleanup, and dependencies when needed for repeatability. Use verified commands; report missing facilities instead of inventing them.
- Keep expected outcomes separate from actual run results. A written case is not a passing test.
- Use test models or detailed case/procedure specifications only where useful. This guide covers those details without requiring separate TMS/TCS/TPS files.
- Link existing automated tests where they already define the check; do not maintain a second prose copy of every assertion.

## Structure

Identify the test item/version, behavior source, coverage and cases, necessary data/environment, and procedures. Add model detail, dependencies, or cleanup where they affect execution. The [test plan](test_plan.md) owns overall approach; reports own observed outcomes.

## Template

```md
# [Capability] test specification
Test basis/item: [Requirements, target version or pending build]
## Coverage and setup
[Included behavior, exclusions, roles/data/environment]
## Cases
| ID / requirement | Preconditions and action/input | Expected outcome |
| --- | --- | --- |
| [Case / requirement] | [Repeatable check] | [Observable result] |
## Procedure and cleanup
[Execution order, verified interfaces, recovery/reset]
## Open prerequisites
[Missing decisions, data, access, or tools]
```

## Completed example

Fictional specification. The illustrative SDD explicitly requires persistence, administrator-only updates, empty-name rejection, and safe save failure.

```md
# Workspace rename checks
Test basis/item: REN-01–REN-04; target staging build to be supplied.

## Coverage and setup
Use an isolated workspace named Marketing Team, its administrator, and a non-administrator member. The illustrative interface has a Name field and Save control. Billing and ownership are outside scope.

## Cases
| ID / requirement | Preconditions and action/input | Expected outcome |
| --- | --- | --- |
| N1 / REN-01 | Administrator saves Growth Team, then makes a fresh workspace read. | Success is reported and the read returns Growth Team. |
| N2 / REN-02 | Member attempts the same change. | Access is denied and the saved name is unchanged. |
| N3 / REN-03 | Administrator submits an empty Name field. | Input is rejected and the saved name is unchanged. |
| N4 / REN-04 | In a disposable environment, force a save failure during an administrator's change. | Failure is reported and the old name remains saved. |

## Procedure and cleanup
Restore Marketing Team before each case and verify the active account role. For N1–N3, use the settings form and a fresh read of the workspace. For N4, use a confirmed failure-injection facility; block the case if none is available. Restore the isolated workspace afterward. Do not simulate failure in production.

## Open prerequisites
Confirm the target build and failure-injection method before execution. These cases have not been run.
```

## Quality check

Could another tester perform each check and judge its result? Confirm coverage, conditions, inputs, expected outcomes, environment, and cleanup. Preserve unknown requirements and distinguish planned checks from observed evidence.

## Sources

- [ISO/IEC/IEEE 29119-3](https://www.iso.org/standard/79429.html)
- [ASAM: test specification and its components](https://report.asam.net/test-specification)
