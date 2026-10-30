# Low Level Design (LLD)

An LLD explains how a component will work internally. Create one when contracts, state, algorithms, data, or failure handling need more detail than the [HLD](high_level_document.md). Update it when that design changes; label proposed and verified implementation views separately.

## Principles

- Start with the component boundary and relevant [SDD](spec_driven_development.md) requirements. Explain its place in the architecture.
- Define inputs, outputs, permissions, invariants, state changes, and errors precisely enough to review or implement.
- Show transaction boundaries, concurrency, retries, idempotency, or compatibility when relevant. Do not add invented mechanisms or numbers to fill sections.
- Use pseudocode or diagrams when they explain a difficult relationship. Preserve exact API/schema contracts supplied by the project.
- Record important alternatives in a [DDR](design_decision_record.md). The [plan](implementation_plan.md) owns work order and delivery; this document owns internal design.
- Link verification implications to the requirements. Resolve contradictions before calling a design ready.

## Structure

Include scope/status/sources, terms and requirements, internal responsibilities, interface/data/state behavior, important algorithms and failure paths, decisions, checks, and unresolved questions. Omit irrelevant implementation detail instead of inventing it.

## Template

```md
# [Component] design
Status/sources: [Proposed/current, inspected inputs]
## Scope and requirements
[HLD role, definitions, IDs, constraints]
## Internal design
[Responsibilities, contracts, data/state, algorithm or sequence]
## Failure and compatibility behavior
[Transactions, concurrency, errors, migration where relevant]
## Decisions and verification
[DDR links, requirement-linked checks, unresolved choices]
```

## Completed example

Fictional design proposal with an explicitly assumed requirement.

```md
# Workspace rename and audit design
Status/sources: Proposed; illustrative workspace service HLD and agreed AUD-01.

## Scope and requirements
The service changes a workspace name and records who changed it. AUD-01 requires the name update and audit insert to succeed together or leave neither change saved. The actor is the authenticated administrator of the target workspace.

## Internal design
The handler checks workspace administration permission before changing data. Within one database transaction, it updates the name and inserts an audit entry containing the workspace, actor, previous/new names, and event time. Commit completes before the handler reports success. Exact tables and function names require repository inspection.

## Failure and compatibility behavior
If either write fails, roll back the transaction and return a failure response. Keep the previous name and omit the audit entry. Concurrent rename behavior and repeated-request handling remain open; the design does not assume a locking or idempotency mechanism.

## Decisions and verification
DDR proposal: “A rename could be saved without its audit record” recommends a single transaction. For AUD-01, force the audit write to fail and verify that the name remains unchanged and no audit entry exists. No test has run. Resolve concurrency and naming constraints before implementation.
```

## Quality check

Can an implementer follow the internal sequence and every meaningful failure branch? Check contracts, invariants, source support, requirement-linked checks, and unresolved decisions. Detailed design must not silently choose missing product behavior.

## Sources

- [arc42: building blocks and runtime behavior](https://arc42.org/overview/)
- [C4: component and code views](https://c4model.com/diagrams)
