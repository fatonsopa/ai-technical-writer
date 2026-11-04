# Interface Contract (IC)

An Interface Contract (IC) defines the observable agreement between providers and consumers. Create it for a public or internal API, message/event, library boundary or file exchange when callers need precise behavior. Update it when schema, authorization, errors or compatibility change. Keep a maintained machine-readable definition authoritative for syntax and link explanatory semantics to it; do not create an inconsistent second schema.

## Principles

Identify the provider, consumers, protocol, operation/message names, version, source authority and status. Use the project's actual protocol/version. OpenAPI can describe HTTP APIs, but its current version is not automatically the project's version. Other protocols may need another schema format or concise tables.

Define request and response/envelope fields: exact names, types, units, identifiers, bounds, required/optional status, defaults, enum values, encoding and examples. Distinguish absence, null, empty values and zero where behavior differs. Preserve leading zeros and opaque identifiers. Document validation and unknown-field handling from verified requirements; unresolved behavior stays open.

Explain authentication, permissions, tenant/object checks and sensitive-data exposure for each operation. An authentication scheme does not specify application authorization. Describe success, failure categories and observable errors, atomicity/partial success, ordering, pagination and asynchronous completion where relevant. Document correlation and trace data without exposing secrets.

For state-changing or repeated operations, specify timeout/deadline meaning, retry eligibility, idempotency key scope/lifetime, same-key conflicts and lost-response reconciliation when applicable. Do not infer that a timeout rolled back work or that HTTP alone guarantees exactly-once processing. For events, address delivery/duplicate/ordering guarantees and acknowledgment when relevant. Mark inapplicable topics with reasons.

Explain compatibility for consumers, schema evolution, deprecation and migration. Tie examples and contract tests to requirement IDs, including valid, invalid, unauthorized, duplicate and older-consumer cases as applicable. A descriptive schema does not prove runtime conformance. Keep internal implementation in [Low Level Design (LLD)](low_level_design.md).

## Structure and template

Use [discovery](../workflows/discover.md) to resolve material choices; the author must not invent an endpoint or retry policy. Small contracts can live in a design or issue, preserving the same information.

```md
# [Boundary] contract
Status/sources: [Draft/agreed/current, provider/consumer, version and source authority]
## Scope and authority
[Protocol, maintained schema, in/out of scope and decision sources]
## Operations and messages
[Exact operation/message names, inputs, success results and sequencing]
## Data and validation
[Fields/types/units, required/default/absence/null rules, validation and examples]
## Access and failure semantics
[Authentication/authorization, errors, atomicity, timeout/retry/idempotency or inapplicability]
## Compatibility and verification
[Version/evolution/deprecation, consumer effects, requirement-linked cases and open decisions]
```

## Completed example

Read the [Interface Contract (IC) example](../examples/interface_contract.md). It illustrates supplied behavior without claiming a live endpoint exists.

## Quality check

Can independent consumers agree on a valid call, each meaningful error and safe recovery after an ambiguous result? Compare prose, schemas, examples and tests. Separate agreed intent from observed implementation and unresolved behavior.

## Sources

Reviewed 2026-11-04: [OpenAPI 3.2.1](https://spec.openapis.org/oas/v3.2.1.html), for HTTP operation/schema/response/security descriptions. General interface semantics still require project requirements; this guide does not mandate a protocol or specification version.
