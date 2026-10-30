# Design Decision Record (DDR)

A DDR explains an important choice inside a component or implementation design. Create one when future maintainers need to understand alternatives and constraints; revise the proposal as the discussion develops. Record the outcome when it is confirmed and preserve the reasoning behind accepted decisions. Here DDR means Design Decision Record, not Detailed Design Review.

## Principles

Use [Decision Record](decision_record.md) for the shared structure, then add the component’s constraints and design consequences. Link the [LLD](low_level_design.md), governing [SDD](spec_driven_development.md), and relevant tests. Focus on the internal contract, data structures, algorithms, transaction boundaries, or failure handling that distinguishes the options. Use [ADR](architecture_decision_record.md) for a choice shaping overall architecture; avoid recording the same decision twice.

Explain consequences in the component's terms. Attribute performance claims to measurements and leave missing evidence open. A shared task comment or decision log is sufficient when the project uses it.

## Structure and template

Use the shared decision template to explain the context, compare the options, and recommend an approach. Keep the eventual decision separate from the recommendation. Identify the component and requirement drivers in context. For each option describe the internal change, failure behavior, relevant complexity, and compatibility. Record the selected approach only when a decision is confirmed; link supersession rather than erasing it.

## Completed example

Fictional proposal in a workspace-renaming plan.

```md
# A workspace rename could be saved without its audit record

The proposed rename component must save the new name and audit entry together or save neither (AUD-01). The LLD needs a transaction boundary.

## Options considered
### Option A: Write both records in one database transaction
A failed audit insert rolls back the name change. The service must keep both writes within the same transaction boundary.

### Option B: Save the name and enqueue the audit write
The audit work can run separately, but a later audit failure could leave a changed name without its required history.

## Recommended option (A)
Use one transaction because it directly satisfies AUD-01. Keep failure propagation explicit: a failed transaction returns a failure response and leaves both records unchanged. Test a forced audit-write failure.

## Outcome
Pending design review. No schema, source path, owner, approval, or passing test is claimed.
```

## Quality check

Can a maintainer explain the component-level problem, compare real alternatives, and trace the recommendation to an internal contract and verification? Check that the choice is not presented as implemented or approved and that it does not silently alter the behavioral requirement.

## Sources

- [AWS: documenting decision context and consequences](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)
- DDR scope and the shared task-comment format are adopted package conventions.
