# Test Plan (TP)

A test plan explains the objectives, scope, risks, and approach of a testing effort. Create it when testing needs coordination; update it when scope, risks, resources, environments, or the approach change. It can be a section in an [Implementation Plan (IP)](implementation_plan.md) or a separate document for a larger effort.

## Principles

- Start from the governing [Spec Driven Development document (SDD)](spec_driven_development.md), relevant stories, known risks, and existing tests. Identify what will and will not be covered.
- Choose test levels, techniques, environments, and data according to risk. Explain the purpose of each activity rather than listing every possible test category.
- Define observable entry and exit criteria. Record who can decide to proceed with unmet criteria when that authority is known.
- Link the [Test Specification (TS)](test_specification.md) for detailed cases/procedures. The implementation plan explains how to build the change; this plan explains how testing will assess it.
- State dependencies, responsibilities, timing, and resources only from available evidence. Keep unknown access or tooling visible.
- Plan how results and defects will be recorded. Logs are evidence, not an additional document to author.

## Structure

Describe the test basis and objectives, scope/exclusions, risks, approach, environment/data, responsibilities/dependencies, entry/exit criteria, and reporting. Scale the plan to the effort.

## Template

```md
# [Change] test plan
Status/basis: [Proposal or agreed plan; requirement links]
## Objectives and scope
[Requirements, included/excluded checks, risks]
## Approach and resources
[Test levels, techniques, environment/data, known responsibilities/dependencies]
## Entry and exit criteria
[Observable conditions for starting/completing; unresolved authority]
## Reporting and follow-up
[Case/specification links, evidence, defect tracking, reports]
```

## Completed example

Read the [Test Plan (TP) example for Websites Review](../examples/test_plan.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Can the team explain what testing will establish, what it excludes, and what could prevent completion? Check that exit criteria are observable, dependencies are real, and scope matches requirements. A plan is not proof that tests have run.

## Sources

- [ISTQB CTFL, section 5.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)
- [ISO/IEC/IEEE 29119-3](https://www.iso.org/standard/79429.html)
