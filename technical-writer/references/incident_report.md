# Incident Report (IR; postmortem)

An incident report records impact, events, response, recovery, and lessons. Create it when an incident needs a shared record; update it as evidence, recovery status, causes, or follow-up work become clearer. An active-incident update can be short; a later postmortem can explain more.

## Principles

- Lead with the affected users/service, impact, time period, and current status. Preserve unknown scope rather than inventing counts.
- Build a timeline from identified evidence. Include timezones and mark estimates.
- Separate the initiating event, contributing conditions, and root cause. Recovery can be verified while the cause remains unknown.
- Explain detection, investigation, mitigation, recovery, and how recovery was checked.
- Write without personal blame. Focus on conditions and decisions visible to responders at the time.
- Give follow-up work a measurable completion check and an owner/link when assigned. Unknown ownership and dates remain open.
- Preserve incident facts. Proposed preventive changes link to [issues](issue.md), decisions, and affected requirements rather than becoming binding policy inside the timeline.

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
| Action | Owner | Completion check / link |
| --- | --- | --- |
| [Action] | [Assigned or unassigned] | [Observable result] |
```

## Completed example

Fictional event with explicitly supplied observations; no live service or attached log is claimed.

```md
# Email delivery worker stopped processing jobs

## Status and impact
Recovered after a worker restart. The illustrative queue grew from 09:10 to 09:42 UTC on 2026-10-20. Messages were delayed; the number of affected recipients and any message loss are unknown.

## Timeline and evidence
| Time UTC | Event | Source |
| --- | --- | --- |
| 09:10 | Successful processing stopped. | Supplied worker metric |
| 09:18 | Queue-growth alert fired. | Supplied alert event |
| 09:25 | Responder found a stopped worker process. | Responder observation |
| 09:30 | Worker restarted. | Supplied action record |
| 09:42 | Queue returned to its prior range. | Supplied queue metric |

## Response and recovery
The responder restarted the worker. Processing resumed and queue growth reversed. These checks establish queue recovery; they do not establish that every recipient read a message.

## Causes and lessons
The worker had stopped, but its exit reason remains unknown. Queue growth exposed the problem; the supplied evidence contains no earlier process-liveness signal. Preserve the exit evidence before selecting a code fix.

## Follow-up
| Action | Owner | Completion check / link |
| --- | --- | --- |
| Investigate worker exit | Unassigned | Evidence supports an explanation or records the remaining uncertainty. |
| Review liveness detection | Unassigned | A disposable worker-stop exercise demonstrates detection against an agreed threshold. |

No follow-up issue, deadline, or threshold has been approved in this example.
```

## Quality check

Can a reader reconstruct the known event and recovery, distinguish causes from hypotheses, and find verifiable follow-up work? Check timezones, attribution, impact limits, and the absence of invented owners or results.

## Source

- [Google SRE: blameless postmortems](https://sre.google/sre-book/postmortem-culture/)
