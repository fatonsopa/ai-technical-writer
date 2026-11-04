# Website category mutation contract

Status: Illustrative design agreement for this example, not a verified live API.
Sources: The supplied behavior in [Low Level Design (LLD)](low_level_design.md).

## Scope and authority

Provider: the authenticated database API. Consumer: the Websites administration browser. This contract describes `bulk_change_website_category(uuid[], text)`; it does not invent an HTTP route or replace the database schema. It covers category mutation and its count result, not list pagination or automated classification.

## Operations and messages

The first argument is the supplied website ID array; the second is an active category ID or `__clear__`. An authorized empty array returns 0. Validate the supplied array length before deduplicating; more than 500 submitted IDs is rejected. For accepted input, duplicate IDs identify one target row, deleted websites are skipped and the result counts changed rows, not submitted IDs. A success response follows commit of website changes and their journal.

Example input: two occurrences of the same existing UUID and one deleted website, with an active category, can change one row and return 1. This illustrates counting semantics, not an executed call.

## Data and validation

The ID argument is an array of UUID values. Category IDs are opaque text and must be active. `__clear__` is an explicit sentinel; it is not null, omitted input or an empty category. Nullable or omitted arguments are not specified by the supplied design and need a decision before a consumer relies on them.

Assignment writes category and verification metadata together, including the authenticated actor. Clearing resets category, status and verification metadata as defined in the component design. A client-supplied actor cannot substitute for authenticated identity.

## Access and failure semantics

Missing authenticated administrator authority is denied with SQLSTATE `42501` before writes. Invalid category, oversized array and other specified validation failures use `22023`. A state-update or journaling failure rolls back the entire request; skipped deleted rows do not turn it into partial commit on error.

The design supplies no idempotency key or exactly-once guarantee. A lost response can follow a committed change. Reconcile current values and history before retrying an uncertain request, because another administrator may have committed a later choice. Exact deadlines and transport-error envelopes remain unspecified.

## Compatibility and verification

Keep existing supported callers working during the compatibility release. Changes to sentinels, nullability, result meaning, grants or error codes require consumer review and an explicit migration decision.

Planned cases: administrator/unauthorized calls; 0, 500 and 501 supplied IDs including duplicates; deleted rows; unknown category; transaction failure during journaling; and lost response after commit. Compare both state and history. These are contract tests to implement, not observed results. Open questions are nullable/omitted arguments and transport deadline/error handling.
