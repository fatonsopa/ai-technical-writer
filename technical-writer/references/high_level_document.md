# High Level Document (HLD)

An HLD explains how a system is organized, how its major parts communicate, and where important data moves. This package also accepts High Level Design and architecture document. Create it for a new system or substantial subsystem; maintain it when the architecture changes. Consult the existing HLD when planning relevant work.

## Principles

- Establish the system boundary, readers, purpose, and requirements that shape the design.
- Explain components and responsibilities before code details. Name important callers, protocols, data, and failure paths.
- Distinguish verified current architecture from proposed views. After implementation, update current views from evidence rather than assuming the plan was followed.
- Explain data ownership, trust boundaries, deployment, reliability, and recovery where they affect the design.
- Link architectural choices to [ADRs](architecture_decision_record.md); use [LLD](low_level_design.md) for substantial component internals. Link the governing [SDD](spec_driven_development.md) and avoid redefining its behavior.
- Tailor arc42 topics and C4 views to actual reader questions. A C4 container is an application or data store, not necessarily a Docker container.

## Structure

Identify status/scope and requirement drivers; define important terms; describe context, components, runtime/data flows, deployment and operations, decisions, and risks. Use [visual guidance](visuals.md) for useful diagrams. An implementation plan schedules the changes; this document explains the system.

## Template

```md
# [System] architecture
Status and sources: [Current/proposed, version/environment, inspected sources]
## Scope, terms, and drivers
[System boundary, readers, relevant requirements]
## Context and components
[External actors/services, responsibilities, connections]
## Runtime and data flow
[Trigger, processing, storage/ownership, response, failures]
## Deployment and operations
[Relevant environments, trust boundaries, monitoring, recovery]
## Decisions and risks
[ADR links, consequences, limits, unresolved questions]
```

## Completed example

Read the [complete Websites Review example](../examples/high_level_document.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Can a new developer identify the major parts, follow a request and its data, and find the requirements and decision sources? Check diagram/prose agreement and distinguish verified architecture, proposed design, and unresolved details.

## Sources

- [arc42: tailorable architecture topics](https://arc42.org/overview/)
- [C4: levels of architectural detail](https://c4model.com/diagrams)
