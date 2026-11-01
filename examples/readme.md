# Websites Review documentation

This collection describes the administration feature that separates ongoing automated work from websites requiring a manual category decision. It covers requirements, design, implementation, testing, and administrator usage.

## Start

For a working introduction, open the [Tutorial (TUT)](tutorial.md). It needs Python 3 and an empty folder, with no application account, packages, or database connection. Copy its complete nine-row JSON fixture into `websites.json`, then run:

```sh
python3 -c 'import json; rows=json.load(open("websites.json")); print(", ".join(r["id"] for r in rows if r["active"] and r["review_state"]=="review"))'
```

The command prints `U3, U3H, US`. The tutorial also shows how to obtain All 6, Pending 4, and Review 3. Those different totals are intentional.

Administrators using the application should start with the [How-to Guide (HTG)](how_to_guide.md). It requires an authorized administrator account. Developers should read the behavior baseline before the implementation plan.

## Find your way around

| Need | Document |
| --- | --- |
| Understand the user problem and scope | [Product Requirements Document (PRD)](product_requirements_document.md) |
| Check expected behavior | [Spec Driven Development document (SDD)](spec_driven_development.md), WEB-01–WEB-12 |
| Understand architecture and contracts | [High Level Document (HLD)](high_level_document.md), [Low Level Design (LLD)](low_level_design.md) |
| Follow delivery dependencies | [Implementation Plan (IP)](implementation_plan.md) |
| Understand important choices | [Decision Record (DR): architecture](decision_record_architecture.md), [Decision Record (DR): component design](decision_record_component_design.md) |
| Find test cases and results | [Test Specification (TS)](test_specification.md), [Test Completion Report (TCR)](test_completion_report.md) |
| Review accountability and exact rules | [Policy (POL)](policy.md), [Technical Standard (STD)](technical_standard.md) |

## Check the result

The tutorial's expected IDs and totals provide its completion check. Product acceptance requires the separate T01–T20 cases against the target application build. Completing the tutorial does not establish that the application passes those cases.

## Limits and maintenance

This directory is documentation, not an application bootstrap package. Application setup and credentials belong to the project's maintained environment instructions. Never copy live credentials into these files.

When behavior changes, update the Spec Driven Development document (SDD) first and reconcile affected design, plan, cases, and usage guidance. Preserve prior run/build boundaries in reports. Update the living architecture from verified implementation.
