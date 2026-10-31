# Source facts

Draft logging policy and proposed standard, not approved. Scope: completed production application HTTP requests, excluding infrastructure access logs. Credentials mean access tokens, session cookies and passwords; route pattern means matched template rather than raw URL. Principles: trace requests and minimize captured data.
Policy: service owners provide diagnostic request metadata and never log credentials. Engineering lead owns proposal and may approve extra non-sensitive context for a documented incident until closure; credentials remain forbidden.
Standard: LOG-01 each completed request records request ID, method, route pattern, status and duration in milliseconds; LOG-02 never record credentials; LOG-03 timestamps identify UTC. Service owners maintain checks. No exception or adoption approved.

## Existing draft for editing/review/rewriting

# Draft

The following information is provided for the purpose of facilitating understanding of the subject.

Draft logging policy and proposed standard, not approved. Scope: completed production application HTTP requests, excluding infrastructure access logs. Credentials mean access tokens, session cookies and passwords; route pattern means matched template rather than raw URL. Principles: trace requests and minimize captured data.
Policy: service owners provide diagnostic request metadata and never log credentials. Engineering lead owns proposal and may approve extra non-sensitive context for a documented incident until closure; credentials remain forbidden.
Standard: LOG-01 each completed request records request ID, method, route pattern, status and duration in milliseconds; LOG-02 never record credentials; LOG-03 timestamps identify UTC. Service owners maintain checks. No exception or adoption approved.
