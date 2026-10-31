# Test Specification (TS)

A test specification defines the checks and procedures used to assess required behavior. Create it before the relevant tests run; update it when behavior, coverage, data, or execution procedures change. The result can be a task section, a test-management record, a table linked to executable tests, or a standalone document.

The test basis is the requirements, acceptance criteria, and other sources used to define the checks.

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
Test basis: [Requirements and source version]
Test item: [System/component and target build or pending version]
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

Read the [complete Websites Review example](../examples/test_specification.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Could another tester perform each check and judge its result? Confirm coverage, conditions, inputs, expected outcomes, environment, and cleanup. Preserve unknown requirements and distinguish planned checks from observed evidence.

## Sources

- [ISO/IEC/IEEE 29119-3](https://www.iso.org/standard/79429.html)
- [ASAM: test specification and its components](https://report.asam.net/test-specification)
