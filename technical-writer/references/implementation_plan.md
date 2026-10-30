# Implementation Plan (IP)

A plan explains how to deliver agreed behavior within the actual system. Create it when work needs sequencing or coordination; update it when the approach, dependencies, risks, or verification change. Read the governing [SDD](spec_driven_development.md), relevant [HLD](high_level_document.md), and decision history before choosing the approach.

## Principles

- Explain the current problem and desired result, then identify the requirements that define success. If a small issue is the specification, link its exact expected behavior and criteria.
- Inspect relevant code, configuration, data, and tests. Mark proposed components and source-reported paths separately from inspected facts.
- Explain the technical approach and meaningful alternatives. Link substantial internals to [LLD](low_level_design.md) and unresolved choices to [decision guidance](decision_record.md).
- Order work by dependency. Each step needs a concrete result and a way to check it; avoid invented owners, dates, paths, or estimates.
- Map every in-scope requirement to verification. Use [testing guidance](test_plan.md) when the effort needs it, without duplicating the entire test plan.
- Address rollout, compatibility, data changes, monitoring, and recovery according to impact. Preserve historical data when rollback cannot safely remove it.
- Resolve conflicts with requirements explicitly before proceeding. Implementation detail cannot silently change the intended outcome.

## Structure

Include goal/specification, important terms, verified context, approach, ordered steps/dependencies, test coverage, rollout/recovery, and risks/open decisions. A plan is not a policy or a full requirements document. Preserve script-consumed tables and project contracts when editing.

## Template

```md
# Implement [change]
## Goal and specification
[Problem, intended result, definitions, requirement links]
## Current context and approach
[Verified code/architecture, proposed changes, decision sources]
## Work sequence
1. [Change, dependency, result, verification]
## Requirement coverage
| Requirement | Check and expected result |
| --- | --- |
| [ID] | [Concrete verification] |
## Rollout and recovery
[Order, compatibility, monitoring, safe recovery]
## Risks and open decisions
[Unresolved choices, consequences, readiness limits]
```

## Completed example

Fictional plan; repository inspection and execution are not claimed.

```md
# Add history for workspace renames
## Goal and specification
Administrators need an attributable record of name changes. The illustrative SDD requires AUD-01: save the name and audit entry together or neither; AUD-02: only administrators of that workspace can read its history.

## Current context and approach
The supplied design places rename handling in the existing workspace service. Source files and schema have not been inspected. The LLD proposes one transaction for both writes; the DDR recommendation is pending acceptance.

## Work sequence
1. Inspect the current handler, permission check, transaction support, schema, and tests. Resolve the DDR and naming/concurrency constraints before coding.
2. Add the agreed audit storage through an additive migration; verify it on a disposable database.
3. Add the name/audit transaction and test its success and forced-failure paths.
4. Add authorized history reads; verify workspace isolation and denied access.
5. Review results against AUD-01/AUD-02 and update the design and architecture only for verified changes.

## Requirement coverage
| Requirement | Check and expected result |
| --- | --- |
| AUD-01 | Successful rename saves both records; forced audit failure saves neither. |
| AUD-02 | Authorized administrator reads only the target workspace history; other callers are denied. |

## Rollout and recovery
Apply additive storage before code that writes it. Check write failures and permission denials after deployment through the project's release process. Code rollback must preserve already collected history; destructive schema rollback needs a separately justified recovery plan.

## Risks and open decisions
Repository details, retention, concurrency, and the transaction decision remain unresolved. No deployment, test pass, estimate, or approval is claimed.
```

## Quality check

Can a developer identify the behavior source, follow the dependencies, and verify every requirement? Review assumptions, design conflicts, release impact, and recovery. A complete-looking sequence is not ready while a blocking product/design decision remains open.

## Sources

- [GitHub Spec Kit: requirements through planning and implementation](https://github.com/github/spec-kit)
- [arc42: architecture context and decisions](https://arc42.org/overview/)
