# Architecture decision record (ADR)

Record a meaningful technical decision once, near the code or design it affects. The record explains what was decided, why it was necessary, and what consequences follow. Use it for choices that would be difficult for a future developer to infer from the implementation.

## Principles

1. Record one important decision per document. Give it a stable ID and descriptive title when the project uses numbered records.
2. Explain the situation and constraints that created the decision. Include relevant alternatives that were actually considered.
3. State the decision plainly and identify its status: proposed, accepted, superseded, or another established team status.
4. Explain both benefits and costs, including operational work and possible future limits. Do not claim the decision has already succeeded without evidence.
5. Link the deciding issue, discussion, or approved proposal when one exists. Do not invent approval or owner details.
6. Update status and links when a later decision supersedes it; retain the historical record where the project keeps an audit trail.

## Template

```md
# ADR-[ID]: [Decision]

- Status: [Proposed / Accepted / Superseded]
- Date: [Verified date, if used]

## Context
[Problem, constraints, alternatives considered.]

## Decision
[What was chosen and its boundary.]

## Consequences
[Benefits, costs, operational changes, risks.]

## References
[Decision issue, design, replacement ADR if any.]
```

## Completed example: use a job queue for email delivery

This is a fictional proposed decision.

### ADR-0007: Send emails through a background job queue

**Status.** Proposed.

**Context.** The application currently calls an outside mail service during an HTTP request. Slow responses increase request duration, and temporary mail service failures affect the user's request.

**Decision.** Send email through a queue processed by a separate worker. The API will record that it accepted the job; the worker will report whether delivery to the mail provider succeeds.

**Consequences.** HTTP requests can complete without waiting for the mail provider. The team must operate a queue, monitor failed jobs, decide retry limits, and handle duplicate deliveries. User messages must distinguish “queued” from “delivered.”

**References.** Product acceptance behavior, queue provider, and final approver remain to be confirmed.

## Quality check

The record makes sense to someone who was absent from the decision meeting and does not claim unknown options, approvals, or outcomes.

## Sources

- AWS ADR guidance: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/faq.html
- Martin Fowler on decision records: https://martinfowler.com/bliki/ArchitectureDecisionRecord.html
