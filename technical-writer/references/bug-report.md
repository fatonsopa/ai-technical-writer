# Bug report

A bug report describes an observed failure so another developer can investigate, reproduce it when possible, assess its impact, and verify a fix. Use this standard for web apps, mobile apps, APIs, background jobs, integrations, performance problems, and data errors. The report describes evidence; it does not need to prove the root cause.

## Principles

1. **One fixable problem per report.** Combine symptoms only if they clearly describe the same failure. Link related issues.
2. **Describe the symptom in the title.** Name the feature, triggering condition when relevant, and observed failure. “Workspace name reverts after saving” is stronger than “Settings broken.”
3. **Give reproducible steps when known.** Specify role, setup, data, actions, order, and timing. State attempts and results honestly. A serious problem is still reportable if reproduction is unknown.
4. **Separate expected and actual results.** Expected behavior comes from a contract, requirement, established behavior, or an explicitly identified assumption requiring product confirmation. Actual behavior comes from an observation.
5. **Use evidence appropriate to the failure.** Screenshots are optional. Database rows, API request and response pairs, logs, traces, tests, accessibility results, timings, and recorded observations may be stronger.
6. **Distinguish facts from suspicions.** A suspicious file or error does not establish the root cause. State hypotheses separately and label uncertainty.
7. **Identify relevant source files carefully.** When the repository is available, inspect entry points, handlers, services, schemas, and tests on the failing path. Include only useful verified paths. Label uninspected search targets as possible locations, never confirmed files.
8. **Explain the impact.** State which people, records, or operations are affected if known, and whether a workaround exists. Do not exaggerate reach or severity.
9. **Keep reports safe.** Remove passwords, tokens, cookies, private records, and personal information from attachments or snippets. Use restricted channels for sensitive security flaws.
10. **Make the fix testable.** Include verification conditions for the original issue and nearby paths. Do not claim testing occurred unless it did.

## Required content

| Field | What to record |
| --- | --- |
| Title | `[Area] Observed failure and condition` |
| Summary | What failed, when, and practical impact |
| Environment | Production/staging/local; build or commit; screen/route/endpoint; role; browser/OS/device if relevant; flags and timestamp when relevant |
| Prerequisites | Account permissions, initial state, sanitized sample data; omit if none |
| Reproduction | Numbered steps with expected inputs; or observed event sequence, attempts, and unknowns |
| Expected result | What should occur and its source, or “Needs product confirmation” |
| Actual result | Exact observable behavior, values, error, or measurement |
| Reproduction status | Always, intermittent, once, unknown; include real attempt counts |
| Severity and impact | S1 critical, S2 high, S3 medium, S4 low, with reasoning and scope |
| Evidence | Appropriate proof, its source, time/environment, and what it demonstrates; or “None captured” |
| Relevant files | Verified paths and symbols with relationship; otherwise “Repository not inspected” |
| Verification | Checks that would show the issue fixed, plus relevant regression checks |

Optional: related issues or pull requests, workaround, hypothesis clearly marked, priority assigned by the responsible team, open questions, release/build containing a verified fix.

## Evidence without screenshots

| Problem | Suitable evidence |
| --- | --- |
| Visual or responsive layout | Screenshot, video, browser viewport, DOM and computed styles |
| Workflow or interaction | Reproduction sequence, browser console, recorded events, state changes |
| API or authentication | Sanitized request/response, HTTP status, error body, request ID, server log, failing test |
| Wrong or missing data | Input values, expected versus actual rows, read-only SQL query and result, export comparison, audit trail |
| Persistence | Before and after values, refresh/requery results, transaction log or failing test |
| Performance | Multiple timed samples, baseline, data size, endpoint/trace and test conditions |
| Background job | Job ID, timestamps, retries, queue state, worker logs, downstream effects |
| Integration | Webhook event ID, delivery attempt, redacted payload, partner response |
| Mobile crash | Build, device and OS, crash report, stack trace, last action |
| Accessibility | Keyboard sequence, screen reader output, accessibility audit, relevant markup |
| Security or privacy | Minimal redacted evidence in a restricted report; follow security response process |

If the only evidence is data, show a small **input / expected / actual** comparison and state how the values were obtained. If there is no saved artifact, record the observer, original conditions, what was seen, and the next useful check. Do not demand an image for a data or backend problem. A report with no screenshot and no log can still be actionable if its observation and context are clear.

For each attached item, identify what it proves. Use actual paths or issue attachments when they exist; never invent attachment names. Keep sensitive production data out of public issues. Do not execute write queries in production merely to collect evidence.

## Severity and workflow ownership

| Severity | Meaning |
| --- | --- |
| S1 Critical | Widespread outage, serious data loss, or major security exposure |
| S2 High | Core or important feature cannot be used and no reasonable workaround exists |
| S3 Medium | Incorrect behavior with limited scope or a workable alternative |
| S4 Low | Minor functional or visual issue with limited impact |

Severity describes impact. Priority describes when the team chooses to fix the problem. Issue status, assignment, and closure are owned by the project's task management process. A developer or tester may propose severity, but should not invent a final priority or release date.

## Copyable template

```md
# [Area] Specific observed failure

## Summary
[What happens, under which conditions, and who is affected.]

## Environment
- Environment: [production/staging/local/unknown]
- Build or commit: [verified value/unknown]
- Page, screen, or endpoint: [value]
- Role, browser, device, flags: [only relevant verified values]
- Time and timezone: [if relevant]

## Prerequisites
[Setup and sanitized test data, or none.]

## Steps to reproduce
1. [Action]
2. [Action]
3. [Observation point]

If not reproducible: observed sequence, attempts, and missing conditions.

## Expected result
[Behavior and source, or needs confirmation.]

## Actual result
[Observed output, values, error, or timing.]

## Reproduction status
[Actual attempts and frequency, or unknown.]

## Severity and impact
[Suggested severity, justification, affected scope, workaround.]

## Evidence
[Actual files, logs, request/response, data rows, tests, or none captured.]

## Relevant files
[Inspected repository paths with reasons, or repository not inspected.]

## Verification
- [Original failure case]
- [Relevant regression case]

## Additional context
[Optional links, uncertainty, or hypotheses clearly marked.]
```

## Completed example: database values revert after a successful update

The following is a **fictional example**. The paths, values, dates, and request IDs are illustrative and are not evidence from any actual repository.

### [Workspace settings] Name returns to its previous value after saving

**Summary.** A workspace administrator changes the workspace name. The application displays “Saved,” but the old name remains after the page reloads. The administrator cannot reliably rename the workspace.

**Environment.** Staging; illustrative build `2.4.1`; `PATCH /api/workspaces/42`; Admin role; Chrome on macOS. The example does not establish whether production is affected.

**Prerequisites.** Sign in as an administrator of workspace 42. Its current name is `Marketing Team`.

**Steps to reproduce.** 1. Open Workspace Settings. 2. Replace `Marketing Team` with `Growth Team`. 3. Select Save. 4. Reload the page and fetch the workspace again.

**Expected result.** The workspace name remains `Growth Team` after the save and reload. This expectation requires confirmation against the actual product contract.

**Actual result.** The UI displays “Saved”; the following illustrative values show the mismatch:

| Check | Input or result |
| --- | --- |
| Submitted value | `Growth Team` |
| Update response | HTTP `200`, `{ "name": "Growth Team" }` |
| Subsequent read | HTTP `200`, `{ "name": "Marketing Team" }` |

**Reproduction status.** 3 of 3 attempts in this fictional scenario. A real report must record the actual count.

**Suggested severity.** S2 High if workspace renaming is an important administrator function without a workaround. The actual scope and priority need confirmation.

**Evidence.** The request and subsequent read are the primary evidence; a screenshot is unnecessary. In a real report, attach sanitized network traces and the request ID, timestamp, and tested build. No actual trace is attached to this example.

**Relevant files.** Repository unavailable. No source paths can be confirmed. Investigate the settings form, update handler, workspace persistence service, and nearest API tests after inspecting the repository.

**Verification.** Change a name, save, reload, and make a fresh API read; all should show the new value. Repeat for another authorized workspace. Confirm unauthorized users cannot change the name. Record tested build and result before closing.

## Quality check

A developer unfamiliar with the report should know what failed, how to try it, which values matter, and what success looks like. The report should accurately mark missing evidence, uncertain expectations, uninspected files, and untested behavior. Keep a security or production incident actionable even when reproducibility is unknown.

## Sources

- GitHub issue forms and bug report examples: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/syntax-for-issue-forms
- Mozilla Bugzilla bug writing guidance: https://bugzilla.mozilla.org/page.cgi?id=bug-writing.html
