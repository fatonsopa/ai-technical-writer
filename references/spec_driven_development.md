# Spec Driven Development document (SDD)

Use this reference to define what a finished system or change must do. A specification records behavior, business rules, constraints, and acceptance criteria. It is the source of truth for expected behavior; an implementation plan explains how to satisfy it.

This package uses “SDD” for both the behavioral document and the development method; the document name is a local convention. Create it when behavior needs explicit agreement; update it when intended behavior changes. Use [Implementation Plan (IP)](implementation_plan.md) for delivery, [Product Requirements Document (PRD)](product_requirements_document.md) for product intent, and [User Story (US)](user_story.md) for a user-value summary. A specification can follow a work item or generate several items after planning. Small changes can keep their specification in explicit task requirements and acceptance criteria.

## Principles

- Describe observable outcomes before choosing technologies or files. A genuine architectural, regulatory, or product constraint belongs in the spec with its source; a proposed implementation choice belongs in the design or plan.
- Define scope and terms before relying on them. Include normal behavior, permissions, errors, boundary conditions, and business rules that affect the result.
- Give requirements stable identifiers and verifiable acceptance conditions. Keep relevant units, limits, exceptions, and sources intact.
- Separate agreed requirements from assumptions, proposals, and unanswered questions. Do not invent product decisions to make the document appear complete.
- Keep one maintained statement of intended behavior. Link downstream designs, plans, issues, and tests to it instead of maintaining competing copies.
- Change the spec explicitly when intended behavior changes. A plan or implementation cannot silently override it. Record the reason and update affected acceptance checks.

## Writing an individual requirement

State one independently verifiable obligation with its actor/system, relevant condition or trigger, outcome, and exception. Keep stable IDs when rewording the same requirement; do not reuse a retired ID for different behavior. Record the source and whether the statement is agreed, proposed, or unresolved. A useful optional pattern is “When [event], the [system] must [response].” Natural equivalent wording is valid.

Distinguish behavior, measurable quality constraints, and mandated design constraints. A quality target needs units and operating conditions, such as load, dataset, and measurement point. An unknown threshold is an open decision, not a number to invent. Preserve obligation strength: must expresses an obligation, should a recommendation, and may permission. Adopt RFC 2119/8174 uppercase terms only when the governing document explicitly uses that convention.

For a complete standalone entry, keep the ID, Status/source, Statement, and Verification fields in this compact template. An entry inside a larger specification can inherit its status and linked acceptance mapping; narrow edits retain their requested scope:

```md
### [ID]: [Subject]
Status/source: [Agreed/proposed; exact source]
Statement: [Condition, obligation, and exception]
Verification: [Setup/input, action, observable expected result]
Rationale: [Only if it helps interpretation]
```

For a complete requirement entry, see WEB-07 and its acceptance mapping in the [Spec Driven Development document (SDD) worked example](../examples/spec_driven_development.md).

## Document structure

The template below is this skill's default. Scale the detail to the work, while preserving the behavior and acceptance agreement.

Identify the spec's status, source request, owner or decision authority when known, and the version or date needed to distinguish revisions. Explain users, scope, terminology, and scenarios. State identified functional requirements, business rules, quality constraints, and externally visible interface/data behavior. Map requirements to acceptance checks.

Keep implementation details out unless they are confirmed constraints. An existing codebase can inform feasibility and compatibility, but code is not proof of what the product should do. If current code conflicts with an agreed requirement, document the difference.

A draft can contain open decisions. Identify which decisions block implementation or acceptance. Do not mark it ready by guessing answers.

Follow [discovery](../workflows/discover.md) before settling missing behavior. Inspect existing workflows, then ask about genuine gaps or proposed changes. Use [Visual Guidance (VG)](visuals.md) for user flows when branching makes interactions difficult to follow, wireflows when changing screens matter, and state machines when observable lifecycle rules need agreement. Map relevant paths to requirement IDs and acceptance checks. Keep technical execution in High Level Document (HLD)/Low Level Design (LLD); a small specification may need no diagram.

## Template

```md
# [Capability] specification

Status: [Draft / agreed / changed, using the project's terms]
Source: [Request, issue, or product decision]

## Purpose and scope
[Users, need, included behavior, and important exclusions.]

## Definitions
[Terms needed to interpret the requirements.]

## Scenarios
[Relevant starting conditions, user actions, and outcomes.]

## Requirements and business rules
- REQ-01: [Condition, required behavior, and exception.]
- REQ-02: [A separate requirement.]

## Quality and interface constraints
[Measurable qualities, permissions, compatibility, inputs/outputs; sources.]

## Acceptance criteria
| Requirement | Check and expected result |
| --- | --- |
| REQ-01 | [Observable verification] |

## Open decisions
[Question, consequence, and responsible decision-maker when known.]

## Related design and work
[Current architecture, proposed design, plan, and issues when available.]
```

## Completed example

Read the [Spec Driven Development document (SDD) example for Websites Review](../examples/spec_driven_development.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Every required behavior has a source, clear conditions, and an acceptance check. Requirements agree with scenarios and business rules. Open decisions are visible; design proposals are not mistaken for requirements. A plan can reference exact IDs or sections without guessing the intended result.

## Sources

- [GitHub Spec Kit: specification through planning and tasks](https://github.com/github/spec-kit)
- [EARS: structured requirement wording](https://alistairmavin.com/ears/)
- [RFC 2119: requirement levels](https://www.rfc-editor.org/rfc/rfc2119)
- [RFC 8174: uppercase requirement terms](https://www.rfc-editor.org/rfc/rfc8174)

