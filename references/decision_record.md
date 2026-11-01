# Decision Record (DR)

A decision record explains a choice and the context that made it necessary. Use this format for architecture, component design, product, operations, or another subject. Draft a proposal when alternatives need discussion; record the outcome when a real decision is made. Update proposals as evidence changes and preserve the reasoning behind settled choices.

Usually draft a comment on the relevant existing task. Use a standalone Decision task or document when requested or required by the project. Writing a draft does not authorize posting it or creating another task.

## Principles

- Title the situation before the decision. Explain the problem, relevant requirements, constraints and decision criteria before presenting a preference.
- Compare meaningful alternatives actually available or considered. Mark newly suggested options as proposals. Include benefits, costs, risks and consequences that matter to this choice; leave unsupported estimates and measurements unknown.
- Recommend one of the listed options with reasons tied to the criteria. Explain its tradeoffs and what accepting it would change.
- Distinguish a recommendation, confirmed decision, implementation and verification. Attribute the outcome, decision-maker and date only when supported by a real source.
- Preserve settled history. Revise proposals during discussion; link a superseding record when an accepted choice changes. Use the project's existing decision history and record a choice once.
- Link governing requirements and affected documents. Resolve a conflicting requirement explicitly; a decision comment cannot silently replace the Spec Driven Development document (SDD).

## Adapt to the decision

Keep the same structure and choose detail according to what readers need to decide or understand. A subject does not require a separate record type or another development stage.

| Subject | Context and consequences to explain |
| --- | --- |
| Architecture | Relevant requirement drivers; system boundaries, integrations, data ownership, affected components and operational qualities. Link the High Level Document (HLD) and Spec Driven Development document (SDD). Explain deployment, reliability, recovery and cross-component costs where they distinguish the options. Identify current and proposed views; a technology preference alone does not establish a decision. |
| Component design | Component role, interfaces, data structures, algorithms, transactions, failure behavior, concurrency and compatibility where relevant. Link the Low Level Design (LLD), requirements and verification implications. Attribute performance claims to measurements. |
| Product, workflow, operations or another subject | The affected users or process, constraints and criteria, then the benefits, costs and follow-up work that distinguish the available choices. Link the relevant task, plan or other governing source. |

Use the High Level Document (HLD) or Low Level Design (LLD) for the design itself and the implementation plan for delivery work. The record preserves why a choice was recommended or made and its consequences. It can arise inside a bug, feature, plan or another document. Common task metadata belongs in [Issue](issue.md).

## Structure and template

Use a prior-context title, an explanation of the situation, meaningful options and a recommendation. Add an outcome when confirmed; an unresolved proposal can omit it or state that it is pending. Include status, scope and source metadata when known and useful.

```md
# [Situation or problem before the decision]

[Context, relevant requirements, constraints, and decision criteria.]

## Options considered
### Option A: [Name]
[Meaning, benefits, costs, limits.]
### Option B: [Name]
[Meaning, benefits, costs, limits.]

## Recommended option ([Label])
[Why it best fits the criteria; tradeoffs, consequences and affected documents.]

## Outcome
[Only after a real decision: selected option, reason, confirmed source/date/decision-maker. Otherwise omit or state pending.]
```

## Completed examples

These Websites Review records use the same format for different choices. Read the example closest to the requested subject; use the new request's facts when writing.

- [Decision Record (DR): product and interface placement](../examples/decision_record.md): where the domain-ending filter belongs.
- [Decision Record (DR): architecture](../examples/decision_record_architecture.md): how readers share website classification.
- [Decision Record (DR): component design](../examples/decision_record_component_design.md): how bulk changes handle partial and uncertain writes.

## Quality check

Does the title explain the prior context? Are the alternatives meaningful and the recommended label listed? Can a reader understand the criteria, reasons, consequences and relevant subject details without the original conversation? Check requirement/design consistency, sourced status and the distinction between acceptance, implementation and verification. Keep one record for the choice and preserve accepted history.

## Sources

- [AWS: decision context, consequences and lifecycle](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html).
- [Decision-record practice across architecture, design and other choices](https://adr.github.io/).
- The shared task-comment format and prior-context title are this package's user-approved conventions.
