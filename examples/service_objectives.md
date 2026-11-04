# Website administration reliability objectives

Status: Draft; illustrative proposal, not approved service objectives or measured results.
Source: The example's explicitly proposed values and definitions below.

## Service and user experience

The user journey is an authenticated administrator reading a website list or receiving a committed category-save acknowledgment. Scope includes the administration API and its database dependency. Automated classification completion and public website availability are separate journeys and are excluded from these objectives. Maintenance affecting eligible administration requests remains included.

## Indicators and measurement

SLI-01 measures valid authorized category-save requests that receive a success acknowledgment within 1 second. Its numerator is good eligible requests; its denominator is all eligible save requests, including timeouts and server errors. Exclude requests independently identified as malformed or unauthorized; do not exclude service failures simply because they lack a success response. Count one received request as one event, including each client retry. Use the request arrival timestamp to place events in the window.

Measure at the API boundary where arrivals, validation classification, final outcome and elapsed time can be correlated. The exact instrumented query and actual telemetry coverage have not been supplied. Missing outcomes must be reconciled or reported as incomplete measurement, not counted as successful requests. List-read latency needs its own indicator before the broader user journey is covered.

## Objectives and windows

Proposed OBJ-01: at least 99.5% of SLI-01 eligible requests succeed within 1 second over a rolling 28-day window. The 1-second boundary is inclusive. The target and window are example proposals requiring approval; no baseline or compliance measurement is available. This request-based objective does not establish a downtime commitment or external Service Level Agreement (SLA).

## Error budget and response

The proposed bad-event allowance is 0.5% of eligible requests in the same window. For an illustrative 20,000 eligible requests, that permits 100 bad events. This calculation is not a traffic measurement. Budget consumption is actual bad events divided by that allowance once complete event data is available.

The response policy, burn-rate alerts and release restrictions remain undecided. Do not infer authority to freeze releases from this draft. The operational procedure should identify investigation, reconciliation and escalation steps before the objective is adopted.

## Ownership and review

The service owner, approver, measurement owner and review cadence are not supplied. Open decision SOD-01 covers target/window approval; SOD-02 covers measurement/query and missing-data treatment; SOD-03 covers response ownership and policy. These block calling this an operational agreement. Review after route/authorization changes, telemetry changes or evidence that the measure fails to represent users. All measurements and verification remain unexecuted.
