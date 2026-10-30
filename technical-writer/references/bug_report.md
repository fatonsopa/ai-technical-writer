# Bug Report (BR)

A bug report explains an observed failure so a developer can investigate it, reproduce it when possible, and verify a fix. Create it when a failure needs recording; update it as evidence, reproduction, or fix verification changes. Combine this guide with [Issue](issue.md); the report can be the content of its Bug task.

## Principles

- Name the symptom and useful condition in the title. A suspected cause belongs in a labeled hypothesis, not an asserted explanation.
- Describe one problem that can be investigated coherently. Keep related symptoms together and link separate work.
- Separate expected behavior and its source from what was observed. If the expectation needs a product decision, say so.
- Give known prerequisites, actions, inputs, timing, and real attempt counts. A once-observed or unreproducible failure can still be useful.
- Use evidence appropriate to the failure: data rows, request/response pairs, timings, traces, logs, tests, observations, or images. A screenshot is optional.
- Explain what each item demonstrates and how it was obtained. Keep supplied evidence distinct from checks you performed.
- Include useful source paths only when inspected or explicitly attributed to the source. Otherwise describe investigation areas without inventing repository files.
- Describe impact and workarounds accurately. Use the project's severity scale when one exists; priority and workflow status follow project rules.
- Define verification against the requirement and original symptom. A planned regression check is not a completed test.

## Structure

Include title/summary, relevant environment and prerequisites, reproduction or observation sequence, expected/actual results, frequency, impact, evidence, useful files, and verification. Combine short sections naturally and mark material unknowns. Missing logs or images should not prevent recording the observation.

For data evidence, show input/expected/actual values with provenance. For performance, preserve units, sample count, conditions, and any supplied baseline. Redact sensitive values according to the project's evidence-handling rules.

## Template

```md
# [Observed failure and important condition]
## Summary and environment
[Affected behavior/users; build, role, endpoint/device/time when relevant]
## Reproduction or observed sequence
[Known setup, actions, inputs; real frequency or unknown]
## Expected and actual results
[Expected behavior/source; observed result and evidence]
## Impact and supporting information
[Scope/workaround, evidence provenance, verified or attributed files, hypotheses]
## Verification
[Original failure check and relevant regressions; current test status]
```

## Completed example

Fictional report using explicitly supplied API data; no repository or test execution is claimed.

```md
# Workspace name reverts after a successful save
## Summary and environment
In staging build demo-4, an administrator's saved workspace name does not appear in a fresh read. Production impact is unknown.

## Reproduction or observed sequence
For workspace 42, submit Growth Team in place of Marketing Team. The update returns success, then a separate workspace read returns the previous name. The reporter supplied one sequence; repetition has not been checked.

## Expected and actual results
The illustrative rename SDD, REN-01, requires a successful update to be visible in a fresh read.

| Observation | Supplied value |
| --- | --- |
| Submitted name | Growth Team |
| Update response | HTTP 200, name: Growth Team |
| Fresh read | HTTP 200, name: Marketing Team |

The data comes from the reporter's sanitized request/response transcript. No screenshot is needed to show this mismatch.

## Impact and supporting information
The administrator cannot rely on the success response. A workaround and the affected population are unknown. The repository has not been inspected; investigate the update handler, persistence, and fresh-read path without asserting file names or a root cause.

## Verification
Repeat the authorized update and fresh read; both should show Growth Team. Check failure handling and denied updates against the SDD. No fix or passing test is recorded.
```

## Quality check

Can a new developer understand the failure, evidence, uncertainty, and expected outcome? Check that useful conditions and exact values survived editing. Do not invent paths, attempts, attachments, causes, severity, or verification results.

For a review request, identify gaps and suggest focused corrections. The template helps assess completeness; it does not require rewriting the whole report.

## Sources

- [Mozilla: bug-writing guidance](https://bugzilla.mozilla.org/page.cgi?id=bug-writing.html)
- [GitHub: issue forms](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms)
