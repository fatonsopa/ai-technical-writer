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

Include scope/basis/build, actual testing and results, coverage/deviations, defects/risks, completion assessment/recommendation, evidence, and follow-up. Use [Test Status Report (TSR)](test_status_report.md) for ongoing progress.

```md
# [Milestone] test completion report
Scope: [Cycle, milestone, or release being assessed]
Build: [Tested version]
Environment: [Where testing ran]
Reporting period: [Time bounds and timezone]
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

Read the [Test Completion Report (TCR) example for Websites Review](../examples/test_completion_report.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Can a reviewer determine what was tested, which requirements have evidence, and what remains uncertain? Check arithmetic, run/build identity, exit criteria, exclusions, defects, and risk. A report with missing or failing tests must not imply full acceptance.

## Sources

- [ISTQB CTFL, section 5.3.2](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)
- [ISO/IEC/IEEE 29119-3](https://www.iso.org/standard/79429.html)
