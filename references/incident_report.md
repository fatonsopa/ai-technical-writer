# Incident Report (IR)

An incident report records impact, events, response, recovery, and lessons. Create it when an incident needs a shared record; update it as evidence, recovery status, causes, or follow-up work become clearer. An active-incident update can be short; a later postmortem can explain more.

## Principles

- Lead with the affected users/service, impact, time period, and current status. Preserve unknown scope rather than inventing counts.
- Build a timeline from identified evidence. Include timezones and mark estimates. Keep failure observations, mitigation and recovery verification as separate events. A rollback time does not establish the end of user impact. Leave incident start, end and duration unknown unless evidence establishes them.
- Separate the initiating event, contributing conditions, and root cause. Recovery can be verified while the cause remains unknown.
- Explain detection, investigation, mitigation, recovery, and how recovery was checked.
- Write without personal blame. Focus on conditions and decisions visible to responders at the time.
- Give follow-up work observable acceptance criteria and an owner/link when assigned. Unknown ownership and dates remain open.
- Preserve incident facts. Proposed preventive changes link to [issues](issue.md), decisions, and affected requirements rather than becoming binding policy inside the timeline.

## Relationship to a Bug Report (BR)

An Incident Report (IR) describes one disruptive event and the response to it. A Bug Report (BR) describes defective behavior and how a correction will be verified. An incident can recover through a rollback while the underlying defect remains open. An incident may also have an operational cause rather than a software defect. A routine QA failure does not by itself require an Incident Report (IR).

Keep the references separate. For a small event closely tied to one defect, one task or document can hold both records. Choose the primary format from the user's purpose, then include the relevant content from [Bug Report (BR)](bug_report.md). Preserve expected and actual results, reproduction limits and relevant files when documenting the defect; preserve incident impact, timeline, response and recovery checks when documenting the event. Link shared evidence rather than repeating it. State recovery and permanent-fix status separately.

Use linked records when a long response, several defects or repeated incidents need separate histories. Do not create extra documents merely to satisfy a template. An active update can remain brief; a retrospective adds supported causes, lessons and follow-up work when that depth is warranted.

## Structure and template

Include status/impact, evidence-backed timeline, response/recovery checks, causes/unknowns, lessons, and follow-up actions.

```md
# [Service] [Observed incident]
## Status and impact
[Known effects, period, scope, unknowns]
## Timeline and evidence
| Time/timezone | Event | Source |
| --- | --- | --- |
| [Time] | [Observed event/action] | [Evidence] |
## Response and recovery
[Actions and observable recovery checks]
## Causes and lessons
[Known trigger/contributing conditions, unknown cause, useful lessons]
## Follow-up
| Action | Owner | Acceptance criteria / link |
| --- | --- | --- |
| [Action] | [Assigned or unassigned] | [Observable result] |
```

## Completed example

Read the [Incident Report (IR) example for Websites Review](../examples/incident_report.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Can a reader reconstruct the known event and recovery, distinguish causes from hypotheses, and find verifiable follow-up work? Check timezones, attribution, impact limits, and the absence of invented owners or results.

## Source

- [Google SRE: blameless postmortems](https://sre.google/sre-book/postmortem-culture/)
