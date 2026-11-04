# Service Objectives Document (SOD)

A Service Objectives Document (SOD) records which user experiences a service aims to protect and how those objectives are measured. Create it when reliability needs an explicit operational agreement; update it when journeys, measurement or targets change. A Service Level Objective (SLO) is a target, a Service Level Indicator (SLI) is its measurement, and a Service Level Agreement (SLA) is a separate external commitment. Do not infer one from another.

## Principles

Start with service boundaries, users and important journeys. Select meaningful availability, latency, correctness, freshness or durability indicators for the actual workload. Infrastructure utilization may diagnose a problem without measuring user experience. Explain which dependencies and partial failures affect users.

Define every indicator operationally: eligible events, good events, numerator/denominator or distribution, units, measurement location/query, aggregation, coverage gaps and missing/late telemetry. Include failures such as timeouts in the denominator when they represent eligible unsuccessful requests. State treatment of retries, client errors, maintenance, low traffic and incomplete observation. Unknown measurement is not a zero-failure result.

Record each target, its approval/proposal source, evaluation window and threshold/boundary semantics. Distinguish rolling/calendar windows and a percentile from the proportion below a latency threshold. Do not invent targets, baselines, owners or alert thresholds. If a ratio target is 99.9%, its allowed bad-event fraction is 0.1% of eligible events; a request-based budget is not automatically a downtime allowance.

Describe how the error budget is calculated and who responds when it is depleted. Link the actual incident, alerting, deployment or [How-to Guide (HTG)](how_to_guide.md) policy; do not authorize a release freeze or invent an escalation schedule. Explain exclusions and tradeoffs, review cadence/triggers, ownership and unresolved approvals. Targets can be proposed in a draft without claiming agreement or observed attainment.

## Structure and template

Use [discovery](../workflows/discover.md) for missing decisions and [Test Plan (TP)](test_plan.md) for verification work. Separate objective definitions from dashboards, live results and external commitments. This capability does not make a separate document mandatory for every project.

```md
# [Service] reliability objectives
Status/sources: [Draft/agreed, service version, proposal/approval sources]
## Service and user experience
[Users, journeys, boundaries, dependencies and exclusions]
## Indicators and measurement
[Indicator IDs, exact good/eligible definitions, measurement/query and data limitations]
## Objectives and windows
[Targets and status, threshold boundaries, rolling/calendar windows and exclusions]
## Error budget and response
[Calculation/units, actual response policy or open decision, linked operational guidance]
## Ownership and review
[Known owners/approval, review triggers, evidence, unresolved decisions and readiness]
```

## Completed example

Read the [Service Objectives Document (SOD) example](../examples/service_objectives.md). Its numerical proposal is illustrative and is not an approved target or observed result.

## Quality check

Could two reviewers compute the same result from the same events? Check units, boundary inclusion, denominators, window and missing-data handling. Trace targets and actions to real authority. A complete template cannot establish measurement availability or objective attainment.

## Sources

Reviewed 2026-11-04: [Google SRE objective example](https://sre.google/workbook/slo-document/). Its operational definitions and explicit windows inform the guide; the project supplies target values and authority.
