# Behavioral specifications

Use this reference to define what a finished system or change must do. A specification records behavior, business rules, constraints, and acceptance criteria. It is the source of truth for expected behavior; an implementation plan explains how to satisfy it.

Read `references/requirements.md` when writing or reviewing individual requirements. Use `references/plan.md` for implementation work. A spec can follow an issue or generate several issues after planning. Small changes can keep their specification in explicit issue requirements and acceptance criteria.

## Principles

- Describe observable outcomes before choosing technologies or files. A genuine architectural, regulatory, or product constraint belongs in the spec with its source; a proposed implementation choice belongs in the design or plan.
- Define scope and terms before relying on them. Include normal behavior, permissions, errors, boundary conditions, and business rules that affect the result.
- Give requirements stable identifiers and verifiable acceptance conditions. Keep relevant units, limits, exceptions, and sources intact.
- Separate agreed requirements from assumptions, proposals, and unanswered questions. Do not invent product decisions to make the document appear complete.
- Keep one maintained statement of intended behavior. Link downstream designs, plans, issues, and tests to it instead of maintaining competing copies.
- Change the spec explicitly when intended behavior changes. A plan or implementation cannot silently override it. Record the reason and update affected acceptance checks.

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

## Quality and interface constraints
The export must use the caller's existing permission to view the results. It must not expose records the caller cannot view. Performance and maximum row count remain open.

## Acceptance
| Requirement | Check and expected result |
| --- | --- |
| REQ-01 | Filter to one known subset; every exported record belongs to it. |
| REQ-02 | Select and reorder columns; the CSV matches that order. |
| REQ-03 | Simulate a failed export; an error appears and no success confirmation appears. |
| REQ-04 | Use a filter matching nothing; the CSV contains headings only. |

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

