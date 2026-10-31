# Decision Record (DR)

A decision record explains a choice in the context that made it necessary. Draft a proposal when alternatives need discussion; record the outcome when a real decision is made. Usually write a comment on the relevant existing task. Use a standalone Decision task or document when the request or project convention calls for it. Writing a draft does not authorize posting it.

## Principles

- Title the situation before the decision. Explain the problem, requirements, and constraints before presenting a preference.
- Discuss meaningful alternatives actually available or considered. Mark newly suggested options as proposals; do not invent estimates or manufacture a weak alternative.
- Recommend one of the listed options with reasons and tradeoffs tied to the decision criteria.
- Keep a recommendation distinct from an accepted decision. Attribute the outcome, decision-maker, and date only when confirmed.
- Preserve settled history. Revise proposals as evidence changes; link a superseding decision when an accepted choice changes.
- Link affected requirements and design. Resolve a conflicting requirement explicitly; a comment cannot silently replace the governing SDD.

## Structure

Use the template for general decisions, including choices discussed within bugs, features, plans, or other documents. [ADR](architecture_decision_record.md) and [DDR](design_decision_record.md) compose this structure with architectural or component-design context. Common task metadata stays in [Issue](issue.md).

## Template

```md
# [Situation or problem before the decision]

[Context, relevant requirements, constraints, and decision criteria.]

## Options considered
### Option A: [Name]
[Meaning, benefits, costs, limits.]
### Option B: [Name]
[Meaning, benefits, costs, limits.]

## Recommended option ([Label])
[Why it best fits the criteria; tradeoffs and consequences.]

## Outcome
[Only after a real decision: selected option, reason, confirmed source/date/decision-maker. Otherwise omit or state pending.]
```

## Completed example

Read the [complete Websites Review example](../examples/decision_record.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Does the title explain the prior context? Are the alternatives meaningful and the recommended label listed? Can a reader understand the reasons and consequences without the original conversation? Confirm that recommendation, acceptance, implementation, and verification remain distinct and that no new task/file or posted comment was created by default.

## Sources

- [AWS: architectural decision records and their lifecycle](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html)
- The general task-comment format and context title are this package's user-approved conventions.
