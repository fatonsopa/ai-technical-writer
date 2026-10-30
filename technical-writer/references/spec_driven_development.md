# Spec Driven Development document (SDD)

Use this reference to define what a finished system or change must do. A specification records behavior, business rules, constraints, and acceptance criteria. It is the source of truth for expected behavior; an implementation plan explains how to satisfy it.

This package uses SDD for the behavioral document as well as the development method. Create it when behavior needs explicit agreement; update it when intended behavior changes. Use [Implementation plan](implementation_plan.md) for delivery, [PRD](product_requirements_document.md) for product intent, and [User Story](user_story.md) for a user-value summary. A specification can follow a work item or generate several items after planning. Small changes can keep their specification in explicit task requirements and acceptance criteria.

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

An entry can use this compact template:

```md
### [ID]: [Subject]
Status/source: [Agreed/proposed; exact source]
Statement: [Condition, obligation, and exception]
Verification: [Setup/input, action, observable expected result]
Rationale: [Only if it helps interpretation]
```

Complete fictional entry: **REN-01: Retain a saved name.** Status/source: agreed in the workspace rename SDD for this example. Statement: after an authorized name update succeeds, a fresh workspace read must return the saved name. Verification: rename Marketing Team to Growth Team, then make a new read; it returns Growth Team. Rationale: a success response must correspond to a change later reads can observe.

## Document structure

The template below is this skill's default. Scale the detail to the work, while preserving the behavior and acceptance agreement.

Identify the spec's status, source request, owner or decision authority when known, and the version or date needed to distinguish revisions. Explain users, scope, terminology, and scenarios. State identified functional requirements, business rules, quality constraints, and externally visible interface/data behavior. Map requirements to acceptance checks.

Keep implementation details out unless they are confirmed constraints. An existing codebase can inform feasibility and compatibility, but code is not proof of what the product should do. If current code conflicts with an agreed requirement, document the difference.

A draft can contain open decisions. Identify which decisions block implementation or acceptance. Do not mark it ready by guessing answers.

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

## Acceptance
| Requirement | Check and expected result |
| --- | --- |
| REQ-01 | [Observable verification] |

## Open decisions
[Question, consequence, and responsible decision-maker when known.]

## Related design and work
[Current architecture, proposed design, plan, and issues when available.]
```

## Completed example

This fictional draft supplies its own product assumptions. Its row limit is deliberately unresolved, so it does not claim implementation readiness.

```md
# Filtered results export specification

Status: Draft
Source: Analyst request to review results outside the application

## Purpose and scope
Analysts can download the current results as CSV. This covers the results table and excludes charts.

## Definitions
Current results: records matching the active filters at the moment export starts.
Selected columns: the visible columns in their displayed order.

## Scenarios
An analyst filters the table, selects columns, and downloads the matching records. An empty result produces a CSV with column headings and no data rows.

## Requirements and business rules
- REQ-01: An export must contain only the current results.
- REQ-02: CSV columns must match the selected columns and their order.
- REQ-03: If export fails, the application must show an error without showing a success confirmation.
- REQ-04: If no records match, export must produce the selected column headings and no data rows.
- REQ-05: Export must apply the caller's existing view permissions and must not include records the caller cannot view.

## Quality and interface constraints
REQ-05 governs visibility. Performance and maximum row count remain open; neither is an agreed threshold.

## Acceptance
| Requirement | Check and expected result |
| --- | --- |
| REQ-01 | Filter to one known subset; every exported record belongs to it. |
| REQ-02 | Select and reorder columns; the CSV matches that order. |
| REQ-03 | Simulate a failed export; an error appears and no success confirmation appears. |
| REQ-04 | Use a filter matching nothing; the CSV contains headings only. |
| REQ-05 | Use a caller who cannot view a known record; the export excludes it. Check access denial separately when the caller has no permission to view results. |

## Open decisions
The product owner must decide the maximum export size before implementation is marked ready. Measure likely data volumes to inform that choice; no limit is assumed here.

## Related design and work
A plan will identify the existing query and export components after repository inspection. No new implementation is claimed.
```

## Quality check

Every required behavior has a source, clear conditions, and an acceptance check. Requirements agree with scenarios and business rules. Open decisions are visible; design proposals are not mistaken for requirements. A plan can reference exact IDs or sections without guessing the intended result.

## Sources

- [GitHub Spec Kit: specification through planning and tasks](https://github.com/github/spec-kit)
- [EARS: structured requirement wording](https://alistairmavin.com/ears/)
- [RFC 2119: requirement levels](https://www.rfc-editor.org/rfc/rfc2119)
- [RFC 8174: uppercase requirement terms](https://www.rfc-editor.org/rfc/rfc8174)

