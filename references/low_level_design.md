# Low Level Design (LLD)

A Low Level Design (LLD) explains how a component will work internally. Create one when contracts, state, algorithms, data, or failure handling need more detail than the [High Level Document (HLD)](high_level_document.md). Update it when that design changes; label proposed and verified implementation views separately.

## Principles

- Start with the component boundary and relevant [Spec Driven Development document (SDD)](spec_driven_development.md) requirements. Explain its place in the architecture.
- Define inputs, outputs, permissions, invariants, state changes, and errors precisely enough to review or implement.
- Give each internal unit one responsibility. Keep shared rules authoritative and dependencies explicit; separate domain behavior from persistence, provider transport and presentation when those concerns exist.
- Show transaction boundaries, concurrency, retries, idempotency, or compatibility when relevant. Do not add invented mechanisms or numbers to fill sections.
- Use pseudocode or diagrams when they explain a difficult relationship. Preserve exact API/schema contracts supplied by the project.
- Record important alternatives in a [Decision Record (DR)](decision_record.md). The [Implementation Plan (IP)](implementation_plan.md) owns work order and delivery; this document owns internal design.
- Link verification implications to the requirements. Resolve contradictions before calling a design ready.

## Conditional data and boundary detail

When data design is material, include a dictionary of fields/types/units, keys, null/default meanings, sensitivity, ownership, retention and relevant relationships. State invariants and where each is enforced; separate database constraints from application checks and cross-record rules. Explain transaction/isolation assumptions, races and compatibility under old/new readers and writers using the actual database/version. Link migrations to the Implementation Plan (IP) and verification to requirement IDs. Missing schema or policy is an open input, not authority to invent it. Use a separate [Interface Contract (IC)](interface_contract.md) for a shared consumer boundary, and link relevant [Threat Model (TM)](threat_model.md) decisions. PostgreSQL's [constraint guidance](https://www.postgresql.org/docs/current/ddl-constraints.html) is an example for that technology, not a universal storage requirement.

## Structure

Include scope/status/sources, terms and requirements, internal responsibilities, interface/data/state behavior, important algorithms and failure paths, decisions, checks, and unresolved questions. Omit irrelevant implementation detail instead of inventing it.

Use [discovery](../workflows/discover.md) to establish existing contracts before asking about missing design choices. Use [Visual Guidance (VG)](visuals.md) only where internals need clarification: component views for responsibilities, sequences for calls/transactions, activities for branching or concurrent work, state machines for event-driven behavior, and ERDs for meaningful schema relationships. Select relevant views, not the whole list. Keep observable behavior in Spec Driven Development document (SDD) and reuse the architectural overview in the High Level Document (HLD).

## Template

```md
# [Component] design
Status/sources: [Proposed/current, inspected inputs]
## Scope and requirements
[High Level Document (HLD) role, definitions, IDs, constraints]
## Internal design
[Responsibilities, contracts, data/state, algorithm or sequence]
## Failure and compatibility behavior
[Transactions, concurrency, errors, migration where relevant]
## Decisions and verification
[Decision-record links, requirement-linked checks, unresolved choices]
```

## Completed example

Read the [Low Level Design (LLD) example for Websites Review](../examples/low_level_design.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Can an implementer follow the internal sequence and every meaningful failure branch? Check contracts, invariants, source support, requirement-linked checks, and unresolved decisions. Detailed design must not silently choose missing product behavior.

## Sources

- [arc42: building blocks and runtime behavior](https://arc42.org/overview/)
- [C4: component and code views](https://c4model.com/diagrams)
