# Product Requirements Document (PRD)

A PRD explains the product problem, intended users, outcomes, and scope of a product or major feature. Create one when the team needs agreement on product goals and scope; update it when goals, audience, priorities, scope, or success criteria change. Use the [SDD](spec_driven_development.md) for detailed expected software behavior and the [plan](implementation_plan.md) for delivery.

## Principles

- Describe the problem and who experiences it before proposing capabilities. Distinguish research findings and reported needs from assumptions.
- Explain the intended benefit and how the team will assess it. Use supplied measures; leave baselines or targets undecided when they are unknown.
- State included and excluded scope and meaningful priorities. Distinguish agreed commitments from candidate features.
- Summarize user journeys or link [stories](user_story.md). Link behavior requirements rather than maintaining a competing specification.
- Identify dependencies, risks, and decisions that affect scope. A changed product goal requires reconciliation with affected SDD requirements, not a silent override.

## Structure

Identify status and source/decision authority when known; then problem, users, goals, scope, capabilities, success criteria, assumptions, dependencies, open decisions, and related specifications. Match detail to the initiative; a product brief may be enough before discovery is complete.

## Template

```md
# [Product or major feature]
Status/source: [Known status and supporting evidence]

## Problem and users
[Current difficulty, affected users, evidence]
## Goals and success criteria
[Desired outcomes, agreed measures, unknown baselines/targets]
## Scope and capabilities
[Included/prioritized capabilities and exclusions]
## User journeys
[Short scenarios or linked stories]
## Dependencies, risks, and open decisions
[Constraints and questions affecting the product]
## Related specifications
[Behavioral requirement sources and work links]
```

## Completed example

Read the [complete Websites Review example](../examples/product_requirements_document.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Can stakeholders explain the user problem, desired outcome, scope, and how success will be assessed? Confirm that evidence and priorities are attributed, open targets are visible, and product intent is connected to detailed behavior without introducing invented technical decisions.

## Source

- [Atlassian: product requirements documents](https://www.atlassian.com/agile/product-management/requirements/)
