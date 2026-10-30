# Software architecture document

An architecture document explains how a system is organized, how its major parts communicate, where important data moves, and why the team chose the design. It should help developers understand, change, and operate the system. Use arc42 as a checklist of possible topics and C4 as a way to draw useful levels of detail. Include only sections and diagrams that answer a real reader question.

## Principles

1. **Set the boundary.** Explain the system's purpose, users, outside dependencies, and what this document covers.
2. **Explain the shape before the code.** Show components and their responsibilities before diving into files or functions.
3. **Describe connections explicitly.** For each important interaction, name who calls whom, the protocol or event, the data exchanged, and the failure behavior when relevant.
4. **Trace important data.** Explain where data originates, where it is stored, which system owns it, how it changes, and what happens on failure.
5. **Separate current and proposed behavior.** Do not present an architectural plan as if deployed. Identify versions and environments when differences matter.
6. **Record important decisions and tradeoffs.** State the problem, options considered when known, chosen option, consequences, and source of the decision. Use a linked architecture decision record if one exists.
7. **Include operational concerns that change the design.** Address deployment, security boundaries, availability, scaling limits, observability, backups, and recovery only where relevant.
8. **Verify the model.** Cross-check component names, technology, deployment details, and paths against code and infrastructure. Label diagrams as illustrative if the real system is not confirmed.

## Choose the right level of detail

A **system context** view shows people, the system, and outside services. A **container** view shows applications and data stores. A **component** view explains the important parts inside an application. A code-level view is useful only when it clarifies complex internal design. A C4 “container” is an independently running or deployable application or data store; it is not necessarily a Docker container.

A focused architecture document might contain: purpose and scope; context; architecture overview; components and responsibilities; key data or request flows; data stores; deployment and trust boundaries; important design decisions; risks and open questions; source links. Arc42 offers a broader twelve-section structure for more complex systems.

## Template

```md
# [System] architecture

## Purpose and scope
[System purpose, readers, current or proposed status.]

## System context
[Users, external systems, diagram or clear description.]

## Components
| Component | Responsibility | Communicates with |
| --- | --- | --- |
| [Name] | [Specific function] | [Name and protocol] |

## Main data flow
1. [Trigger, data, destination]
2. [Processing and storage]
3. [Response or downstream effect]

## Deployment and operations
[Environments, trust boundaries, failure handling, logs, backups if relevant.]

## Decisions and tradeoffs
[Decision, reason, consequence, link to owner decision.]

## Risks and open questions
[Known limitations, uncertain behavior, decisions needed.]

## Sources
[Code paths, diagrams, deployment files, ADRs; verified where possible.]
```

## Completed example: an event delivery service

This is a proposed design example, not a description of an existing system.

### Event delivery architecture

**Purpose.** The service receives order events and sends them to a partner API. It retries temporary failures and records the final result.

**System context.** A commerce application sends an event when an order is created. The delivery service forwards the event to a partner system.

**Components.**

| Component | Responsibility | Connection |
| --- | --- | --- |
| HTTP receiver | Validates incoming order events | Receives HTTPS requests from commerce app |
| Queue | Holds events awaiting delivery | Receiver writes; worker reads |
| Delivery worker | Sends events and retries temporary failures | HTTPS to partner API |
| PostgreSQL | Stores delivery status and attempts | Worker reads and writes |

**Main data flow.** 1. The commerce app posts an order event with a unique event ID. 2. The receiver validates the request and places the event in the queue. 3. A worker sends it to the partner. 4. The worker records success or failure in PostgreSQL. 5. Temporary failures are retried according to a policy that still needs approval.

**Deployment and operations.** The receiver and worker are separate processes. Logs should include the event ID so operators can trace one delivery without exposing customer information.

**Decision.** Use a queue between event receipt and partner delivery so a slow partner does not keep the original request open. This adds queue operations and the need to handle duplicate deliveries.

**Open questions.** The retry limit, retention period, message deduplication contract, and queue product are undecided.

## Quality check

A new developer can identify each major part, follow a real request or event, explain where important data lives, and find the source for significant design decisions. Every diagram is labeled and does not contradict the prose.

## Sources

- arc42 architecture template: https://arc42.org/overview/
- C4 model diagrams: https://c4model.com/diagrams
- AWS architecture decision records: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/faq.html
