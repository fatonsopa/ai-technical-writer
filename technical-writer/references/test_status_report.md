# Test Status Report (TSR)

A test status report explains progress during an active testing effort. Create it when the team needs an update; issue a new period's report when progress, blockers, or risks change. “Test progress report” is an accepted alias. Keep a short update in the existing task when that serves the audience.

## Principles

- Identify the reporting period, test scope, build, environment, and source evidence. Separate results from different builds or runs.
- Compare observed progress with the [test plan](test_plan.md). Explain deviations and their consequences.
- Distinguish passed, failed, blocked, and not-run cases. A blocked case has no passing result.
- State meaningful coverage and its denominator. Executed, passing, requirement, and code coverage are different measures.
- Link defects and evidence instead of inferring root causes from failed checks.
- Explain blockers, changed risks, and next work. Attribute owners and dates only when assigned.
- Use [Test Completion Report](test_completion_report.md) for a milestone assessment. “QA report” needs context to determine whether status or completion is intended.

## Structure and template

Include period/scope, progress/results, coverage/deviations, blockers/risks, next work, and sources. Use a compact comment or a fuller report according to audience and scope.

```md
# [Scope] testing status
Period/build/environment: [Verified values]
## Progress and results
[Counts, denominators, cases, evidence]
## Blockers and risks
[Deviations, defects, missing facilities, consequences]
## Next work
[Actions and assigned owners/dates where known]
## Sources
[Runs, test specification, plan, defects]
```

## Completed example

Fictional report based on an explicit four-case result set, not a claim of real testing.

```md
# Workspace rename testing status
Period/build/environment: Illustrative 2026-10-30, 09:00–10:00 UTC; demo-7; staging.

## Progress and results
Of four planned checks, N1 passed, N2 failed, N3 was blocked, and N4 was not run. Two of four checks executed; one of four passed. N1 verified persistence after a fresh read. N2 observed that a member could change the name, contrary to REN-02. Acceptance is not complete.

## Blockers and risks
The administrator test account became unavailable before N3. N4 still needs a confirmed failure-injection method. The N2 result presents an unresolved authorization defect; this report does not establish its root cause or release priority.

## Next work
Record the N2 evidence in the existing Bug task, restore the N3 account access, and confirm the N4 test facility. Owners and dates are unassigned. Retest affected checks against the next candidate build without merging its results into this run.

## Sources
Illustrative run R-7: N1 passed, N2 failed, N3 blocked after administrator account access was lost, N4 not run. Rename test specification N1–N4; proposed test plan. No live tracker link or attached log is claimed.
```

## Quality check

Do counts reconcile with the source cases? Can readers distinguish current progress from planned work and missing evidence? Check build/period consistency, coverage meaning, risk, next work, and the absence of invented execution or approval.

## Sources

- [ISTQB CTFL, section 5.3.2](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)
- [ISO/IEC/IEEE 29119-3](https://www.iso.org/standard/79429.html)
