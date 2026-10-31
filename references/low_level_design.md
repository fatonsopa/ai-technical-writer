# Low Level Design (LLD)

An LLD explains how a component will work internally. Create one when contracts, state, algorithms, data, or failure handling need more detail than the [HLD](high_level_document.md). Update it when that design changes; label proposed and verified implementation views separately.

## Principles

- Start with the component boundary and relevant [SDD](spec_driven_development.md) requirements. Explain its place in the architecture.
- Define inputs, outputs, permissions, invariants, state changes, and errors precisely enough to review or implement.
- Give each internal unit one responsibility. Keep shared rules authoritative and dependencies explicit; separate domain behavior from persistence, provider transport and presentation when those concerns exist.
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

Read the [complete Websites Review example](../examples/low_level_design.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Can an implementer follow the internal sequence and every meaningful failure branch? Check contracts, invariants, source support, requirement-linked checks, and unresolved decisions. Detailed design must not silently choose missing product behavior.

## Sources

- [arc42: building blocks and runtime behavior](https://arc42.org/overview/)
- [C4: component and code views](https://c4model.com/diagrams)
