# Architecture Decision Record (ADR)

An ADR preserves the reasons for an architecturally significant choice: system boundaries, integrations, storage, deployment, or qualities that shape the system. Create one when such a choice needs a durable explanation. Revise a proposal during discussion. After a decision is accepted, preserve its reasoning and link any later decision that replaces it.

## Principles

Use [Decision Record](decision_record.md) for context, real options, recommendation, and confirmed outcome. Add architectural drivers and links to the [HLD](high_level_document.md) and governing [SDD](spec_driven_development.md). Explain effects across components and operational tradeoffs. A technology preference without a requirement or constraint is not an established architectural decision.

Use the project's shared decision history. A significant architecture choice can be a linked task comment; this guide does not mandate an additional decision system or a separate ADR stage.

## Structure and template

Use the shared decision template. In the context section, identify the part of the architecture affected, the relevant requirement IDs, and whether the design is current or proposed. For each option, explain affected components, boundaries, failure behavior, and operational cost where known. Add consequences and HLD updates to the recommendation. Add accepted outcome metadata only from a real source.

## Completed example

Read the [complete Websites Review example](../examples/architecture_decision_record.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Review the completed record using this guide and the shared decision template. Confirm scope is architectural, drivers trace to requirements, current/proposed views agree with the HLD, consequences include costs, and status is sourced. Do not rewrite accepted history to match a later implementation.

## Sources

- [AWS: ADR process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)
- [arc42: architecture topics](https://arc42.org/overview/)
