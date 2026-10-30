# Production incident report and postmortem

Record a service incident so the team can understand what happened, how users were affected, how service returned, and what changes will reduce the chance or impact of a repeat. Keep the report factual and free of personal blame. A short incident update written during an outage may contain fewer details than a postmortem written afterward.

## Principles

1. Start with the user impact, time period, affected services, and current status. Give counts or durations only when verified.
2. Build the timeline from monitoring data, logs, tickets, and confirmed operator actions. Include timezones and distinguish approximate times.
3. Separate the **trigger** (what immediately started the event) from the underlying contributing conditions; root causes may remain unknown.
4. Describe detection, response, mitigation, recovery, and verification. Do not describe a suspected fix as a verified recovery.
5. State what worked and what was difficult using system and process explanations. Avoid attributing blame to individuals.
6. Assign follow-up actions with a responsible team or person, measurable completion condition, and tracking link when available. Do not invent owners or due dates.
7. Protect sensitive data and security details. Use restricted documents for information that increases risk.
8. Keep the incident record distinct from binding preventive standards, which should link to approved decisions.

## Template

```md
# [Incident date] [Service] [Observed failure]

## Summary and status
[What happened and whether the service has recovered.]

## Customer and business impact
[Who was affected, duration, verified numbers, unknown scope.]

## Timeline
[Time, timezone, event, source.]

## Detection and response
[First signal, investigation, mitigation, recovery checks.]

## Causes and contributing conditions
[Evidence-based trigger and causes; unknowns clearly marked.]

## What we learned
[Useful facts about systems and response.]

## Follow-up actions
| Action | Owner | Completion check | Link |
| --- | --- | --- | --- |
| [Action] | [Owner/Unassigned] | [Measurable result] | [Issue if created] |

## Sources and open questions
[Logs, dashboards, incident room, remaining unknowns.]
```

## Completed example: queue worker stopped processing emails

The following is fictional; times and counts are illustrative.

### 2026-10-20 Email queue stopped delivering messages

**Summary and status.** A delivery worker stopped processing queued emails between 09:10 and 09:42 UTC. Service recovered after the worker restarted and the queue began draining.

**Impact.** In this hypothetical event, 180 messages were delayed. The example has no evidence that messages were lost. Recipient delivery confirmation was outside the incident check.

**Timeline.** At 09:10 UTC the worker stopped sending success events. At 09:18 monitoring detected queue growth. At 09:25 an engineer identified a stopped worker process. At 09:30 the worker restarted. At 09:42 the queue returned to its normal size.

**Detection and response.** The alert detected queue growth, but it did not immediately reveal that the worker process had stopped. The team restarted the worker and watched queue length and send errors.

**Causes and contributing conditions.** The immediate trigger was a stopped worker process. Why it stopped remains unknown. Missing process health alerts delayed diagnosis.

**Follow-up actions.** Add a worker liveness alert, owned by the operations team, with a test that stops a worker and confirms an alert fires within the approved threshold. Investigate the worker exit reason before choosing a code fix. Tracking links and due dates are pending.

**Sources and open questions.** A real report would link monitoring and process logs. The example has none attached.

## Quality check

A reader can reconstruct the verified event and its impact, distinguish known causes from unknowns, and understand which corrective actions will be checked.

## Source

- AWS post-incident and response guidance: https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_testing_resiliency_playbook_resiliency.html
