# Product Requirements Document (PRD)

A PRD explains the product problem, intended users, outcomes, and scope of a product or major feature. Create one to align an initiative; update it when goals, audience, priorities, scope, or success criteria change. Use the [SDD](spec_driven_development.md) for detailed expected software behavior and the [plan](implementation_plan.md) for delivery.

## Principles

- Describe the problem and who experiences it before proposing capabilities. Attribute research, reported demand, and assumptions separately.
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

Fictional initiative with stated product assumptions; it is not a claim about the user's application.

```md
# Workspace identity management
Status/source: Draft product proposal based on an illustrative administrator interview.

## Problem and users
Workspace administrators cannot keep a workspace's displayed name aligned with team changes. Members use that name to distinguish their workspace from others.

## Goals and success criteria
Administrators can correct the name without support intervention. Review completed rename journeys and support requests associated with renaming. Baseline frequency and a numerical reduction target have not been established.

## Scope and capabilities
Include authorized renaming and an accurate confirmation of the saved name. Ownership transfers, workspace deletion, and billing changes are outside scope. Renaming is the first capability proposed for discovery.

## User journeys
An administrator changes the name and later sees the new name in a fresh workspace view. A member without permission receives a clear rejection.

## Dependencies, risks, and open decisions
Confirm naming rules and which existing role can administer a workspace. Incorrect permission assumptions could expose changes to the wrong users. The product owner is not yet assigned in this example.

## Related specifications
The workspace rename SDD will define persistence, permissions, error behavior, and acceptance checks. No implementation plan or approved release date exists yet.
```

## Quality check

Can stakeholders explain the user problem, desired outcome, scope, and how success will be assessed? Confirm that evidence and priorities are attributed, open targets are visible, and product intent is connected to detailed behavior without introducing invented technical decisions.

## Source

- [Atlassian: product requirements documents](https://www.atlassian.com/agile/product-management/requirements/)
