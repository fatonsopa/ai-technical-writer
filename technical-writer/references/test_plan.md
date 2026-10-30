# Test Plan (TP)

A test plan explains the objectives, scope, risks, and approach of a testing effort. Create it when testing needs coordination; update it when scope, risks, resources, environments, or the approach change. It can be a section in an [implementation plan](implementation_plan.md) or a separate document for a larger effort.

## Principles

- Start from the governing [SDD](spec_driven_development.md), relevant stories, known risks, and existing tests. Identify what will and will not be covered.
- Choose test levels, techniques, environments, and data according to risk. Explain the purpose of each activity rather than listing every possible test category.
- Define entry conditions and observable exit criteria. Record who can decide to proceed with unmet criteria when that authority is known.
- Link the [test specification](test_specification.md) for detailed cases/procedures. The implementation plan explains how to build the change; this plan explains how testing will assess it.
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
## Results and follow-up
[Case/specification links, evidence, defect tracking, reports]
```

## Completed example

Fictional plan for an illustrative rename feature. No test execution or approval is claimed.

```md
# Workspace rename test plan
Status/basis: Proposed; illustrative rename SDD, REN-01–REN-04.

## Objectives and scope
Check saved-name persistence, administrator-only updates, empty-name rejection, and preservation of the old name after a failed save. Billing changes and workspace ownership transfers are outside scope. Unauthorized updates and misleading success responses are the main risks.

## Approach and resources
Use integration checks for permission and storage outcomes and a UI check for feedback after saving. Test in staging with an isolated workspace, an administrator, and a member account. Use the test specification's N1–N4 cases. The method for simulating a storage failure must be confirmed in a disposable test environment. The test owner is unassigned.

## Entry and exit criteria
Start after the target build is available, the four behavior rules are agreed, and the accounts/workspace are ready. Complete the planned acceptance when all four checks pass and no unresolved defect contradicts them. Any decision to stop earlier must report unmet criteria and remaining risks; the release authority is not assigned here.

## Results and follow-up
Record build/environment and case evidence during testing. Use a status report if coordination needs ongoing updates. At the milestone, summarize outcomes and remaining risk in a completion report, which can be a task comment. Record failures as Bug tasks without inventing their cause.
```

## Quality check

Can the team explain what testing will establish, what it excludes, and what could prevent completion? Check that exit criteria are observable, dependencies are real, and scope matches requirements. A plan is not proof that tests have run.

## Sources

- [ISTQB CTFL, section 5.1](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)
- [ISO/IEC/IEEE 29119-3](https://www.iso.org/standard/79429.html)
