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
Reporting period: [Time bounds and timezone]
Build: [Verified version]
Environment: [Where testing ran]
Status: [Current testing status]
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

Read the [complete Websites Review example](../examples/test_status_report.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Do counts reconcile with the source cases? Can readers distinguish current progress from planned work and missing evidence? Check build/period consistency, coverage meaning, risk, next work, and the absence of invented execution or approval.

## Sources

- [ISTQB CTFL, section 5.3.2](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)
- [ISO/IEC/IEEE 29119-3](https://www.iso.org/standard/79429.html)
