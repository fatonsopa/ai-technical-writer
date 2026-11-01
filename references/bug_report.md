# Bug Report (BR)

A bug report records an observed failure so a developer can investigate it, reproduce it when possible, assess its impact, and verify a fix. Create it to record a failure; update it as investigation or verification progresses. Combine this guide with [Issue](issue.md). It can live in a Bug task.

## Principles

- Name the observed failure and useful condition in the title. Keep possible causes labeled as hypotheses until evidence establishes them.
- Keep related symptoms together when they describe one failure; link separate problems.
- Keep expected behavior separate from actual observations. Cite the requirement or contract; flag an uncertain expectation for confirmation.
- Give precise actions, inputs, setup, order, timing, and real attempt counts. A once-observed or unreproducible failure can still be reported. An unreported reproduction attempt is unknown; do not turn “no further attempts were reported” into “no further attempts occurred.”
- Use evidence suited to the failure: request/response pairs, database rows, logs, traces, timings, tests, observations, or images. Screenshots are optional. Explain provenance and what each item establishes.
- Include inspected paths and symbols with their relationship to the failure. Attribute paths supplied by another investigator. A relevant file is not automatically the cause. When access is unavailable, say so and identify search areas without inventing paths.
- Explain known impact and workarounds. Follow the project's severity scale; assignment, priority, status, and release decisions remain with its task-management process.
- Protect sensitive evidence and preserve exact material values, units, identifiers, and errors. Planned verification is not a passing test.

## Relationship to an Incident Report (IR)

A Bug Report (BR) investigates defective behavior. If that defect also causes a disruptive event, use [Incident Report (IR)](incident_report.md) for impact, timeline, response, recovery and lessons. A verified recovery is not evidence that the permanent defect was fixed. A bug found during QA may need only a Bug Report (BR).

For one small event tied to one defect, keep a combined record in the same task or document when useful. Preserve every required defect section and add the relevant incident information from the other reference. In particular, Timeline and evidence does not replace Evidence; keep the Evidence section and link the shared timeline or artifacts. Keep shared evidence in one place, and distinguish service recovery from defect verification. Use linked records for longer response histories, multiple defects or repeated events. Keep the two reference files and their responsibilities separate.

## Structure

Use the following sections for a complete report. Keep **Expected result** and **Actual result** separate, name the reproduction section **How to reproduce**, and include **Relevant files** even when the repository has not been inspected. Do not merge these fields into a general supporting-information section. A narrow edit or review still follows the requested operation.

| Section | What to record |
| --- | --- |
| Title | Observed failure and important condition. |
| Description | What fails, where it occurs, and the context needed to understand it. |
| Environment | Relevant environment/build, role, screen/endpoint, device/OS/browser, flags, and time; mark material unknowns. |
| Prerequisites | Required permissions, starting state, or sanitized data; omit only when no setup is needed. |
| How to reproduce | Numbered steps when known. Otherwise record the observed sequence and explain that repeatable reproduction is unknown. |
| Expected result | Intended behavior and its source, or the expectation needing confirmation. |
| Actual result | Observed behavior, exact values/errors, and measurements with units and conditions. |
| Reproduction frequency | Actual attempts/results or a clear once/intermittent/unknown status. |
| Severity and impact | Known affected users/operations, scope, workaround, and a supported severity assessment; do not invent a rating or priority. |
| Evidence | Available or inspected artifacts and observations, their provenance, and what they demonstrate. Missing attachments mean none were provided; they do not establish that none were captured. |
| Relevant files | Verified or attributed paths/symbols and why they matter, or an explicit repository-access limitation. |
| Verification | Planned original-failure and regression checks linked to expected behavior; distinguish completed results from checks still needed. |
| Additional context | Optional related work, open questions, or clearly labeled hypotheses. |

For data failures, show a small input/expected/actual comparison. For performance, retain sample counts, units, conditions, and any supplied baseline; measurements alone do not establish a regression. A missing screenshot, log, source path, or reproduction must remain an honest gap rather than invented evidence.

## Template

```md
# [Observed failure and important condition]

## Description
[What fails and the context needed to understand it.]

## Environment
[Relevant build/environment, role, location, device, and timing; material unknowns.]

## Prerequisites
[Required setup, permissions, starting state, and sanitized data, when applicable.]

## How to reproduce
1. [Known action and input.]
2. [Next action and observation point.]

[If repeatable steps are unknown, give the reported sequence and say what is missing.]

## Expected result
[Required behavior and source, or expectation needing confirmation.]

## Actual result
[Observed output, error, data, or timing.]

## Reproduction frequency
[Reported attempts and conditions, or once/intermittent/unknown. An unreported attempt remains unknown.]

## Severity and impact
[Supported impact, affected scope, workaround, and severity assessment or uncertainty.]

## Evidence
[Provided or inspected evidence, its provenance, and what it establishes. If none was supplied, say that; do not infer that no capture exists.]

## Relevant files
[Inspected or attributed paths/symbols with their role; otherwise repository not inspected.]

## Verification
[Original failure and relevant regression checks; actual execution status.]

## Additional context
[Optional related work, open questions, or labeled hypotheses.]
```

## Completed example

Read the [Bug Report (BR) example for Websites Review](../examples/bug_report.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Can a new developer understand the failure, try the known sequence, distinguish required behavior from observations, locate relevant evidence/code, and verify a fix? Check every required section and its content. Preserve exact values and uncertainty; do not invent paths, attempts, attachments, causes, severity, or test results.

For a review, return gaps and focused corrections; give a full replacement only when requested. A narrow edit does not require the full report structure.

## Sources

- [Mozilla: bug-writing guidance](https://bugzilla.mozilla.org/page.cgi?id=bug-writing.html)
- [GitHub: issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms)
