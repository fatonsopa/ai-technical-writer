# Test Completion Report (TCR)

A test completion report assesses testing performed for a cycle, release, test level, or milestone. “Test Summary Report” is an accepted alias. Create it at that milestone; preserve the original run/build scope when later retesting adds evidence. Completion of a reporting period does not mean every test passed.

## Principles

- Identify the scope, behavior source, plan, tested build/environment, and reporting boundary.
- Summarize what actually ran and what did not. Reconcile passed, failed, blocked, and not-run counts with source evidence.
- Assess results against the agreed exit criteria. Explain deviations, excluded checks, unresolved defects, and remaining risks.
- Link requirements to checks/results. Define what a coverage measure counts rather than treating execution as proof of correctness.
- Preserve raw evidence and its provenance. Existing logs and CI exports are inputs, not a new authored log document.
- Separate the assessment or release recommendation from the authorized release decision. Do not invent sign-off, owners, or passing results.
- Match detail to the audience. A small bug may need only a verification comment; a wider milestone may need a separate report.

## Structure and template

Include scope/basis/build, actual testing and results, coverage/deviations, defects/risks, completion assessment/recommendation, evidence, and follow-up. Use [TSR](test_status_report.md) for ongoing progress.

```md
# [Milestone] test completion report
Scope/build/environment: [Known values and period]
## Testing and results
[Executed scope, result counts, evidence, requirement coverage]
## Deviations and remaining risks
[Unrun/blocked checks, unresolved defects, plan differences]
## Assessment and follow-up
[Exit criteria, recommendation, actual decision if confirmed, next checks]
## Sources
[Plan, test specification, run evidence, defects]
```

## Completed example

Fictional assessment using the same explicit result set as the status-report example.

```md
# Workspace rename candidate demo-7 assessment
Scope/build/environment: Rename acceptance cycle; demo-7; staging; illustrative 2026-10-30.

## Testing and results
The cycle ended with N1 passed, N2 failed, N3 blocked, and N4 not run. Two of four planned checks executed, and one passed. N1 supports REN-01 persistence. N2 contradicts REN-02 administrator-only updates. REN-03 and REN-04 remain unverified by this run.

## Deviations and remaining risks
The plan's four passing checks were not achieved. N3 lost access to the administrator test account; N4 lacked confirmed failure injection. The authorization failure remains unresolved. This evidence cannot establish that the release meets its acceptance requirements.

## Assessment and follow-up
Recommend holding this candidate until the authorization defect is fixed and N2–N4 are successfully checked on the appropriate build, with relevant regression coverage. The release decision is pending; no approver or sign-off is recorded. This report marks the end of this cycle, not release approval.

## Sources
Illustrative run R-7 and rename test specification N1–N4; proposed test plan. The result set is supplied within this fictional example, with no live attachments or claimed production tests.
```

## Quality check

Can a reviewer determine what was tested, which requirements have evidence, and what remains uncertain? Check arithmetic, run/build identity, exit criteria, exclusions, defects, and risk. A report with missing or failing tests must not imply full acceptance.

## Sources

- [ISTQB CTFL, section 5.3.2](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)
- [ISO/IEC/IEEE 29119-3](https://www.iso.org/standard/79429.html)
