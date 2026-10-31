# Website review queries and category mutation design

Status: Agreed component design
Sources: [HLD](high_level_document.md), [SDD](spec_driven_development.md)

## Scope and requirements

This design covers classification, filtered administration reads, category writes, and browser coordination. WEB-01–WEB-05 govern reads and permissions; WEB-06–WEB-10 govern editing; WEB-11–WEB-12 constrain compatibility and performance.

A queue value is `pending`, `review`, or null for no queue restriction in a read request. The classifier itself returns null for websites in neither queue. Those two uses of null must remain distinct in callers.

## Classification and read contracts

`public.website_review_state(websites)` returns:

| Condition | Result |
| --- | --- |
| Unverified and parked by the common confirmation helper | `review` |
| Pending, or unverified and not parked | `pending` |
| Verified or any other status | null |

Evaluate the shared parked rule rather than copying its attempt/reason branches. Do not filter deletion or citation presence inside this helper; callers use it outside active administration lists too.

`_admin_websites_predicate` combines active-row filtering, queue, domain search, category, and normalized domain ending. `list_admin_websites_page`, `count_admin_websites`, and `admin_website_ids` use that predicate. Add optional `p_queue` and `p_tld` parameters with null defaults. Reject unsupported non-null queue values with SQLSTATE `22023`. Keep existing supported calls working during the compatibility release.

Pending and Review use left joins for citation information. All retains its existing citation-based population. Pending and Review default to Added descending; All keeps its existing default. Sorting uses a deterministic ID tie-breaker with the selected key. A cursor belongs to its tab/filter/sort combination and must be discarded when any of those changes.

Trim whitespace and surrounding dots and lowercase the domain ending before building a suffix condition. Empty input applies no ending restriction. Reject unsupported wildcard syntax with SQLSTATE `22023`. Use escaped literals in dynamic SQL; a validated suffix is still not an SQL identifier. The reversed-domain index supports the corresponding suffix lookup.

## Mutation contract

`bulk_change_website_category(uuid[], text)` returns the count of changed rows. The second argument is an active category ID or the clear sentinel `__clear__`.

| Input or condition | Required handling |
| --- | --- |
| Missing authenticated administrator | Deny with `42501` before writes |
| More than 500 supplied IDs | Reject with `22023` before writes |
| Empty array from an authorized caller | Return 0 |
| Unknown or deleted category | Reject with `22023` |
| Deleted website among supplied IDs | Skip it; leave its fields unchanged |
| Failure during update or journaling | Roll back the complete request |

Validate the supplied array length before reducing duplicate IDs, so duplicates cannot bypass the request limit. Treat repeated IDs as one target row when counting changes.

For an assignment, set category, verified status, high confidence, attempts 0, `verified_by = user:<authenticated UUID>`, the manual reason, and verification time together. The journal must identify the same actor through the existing authenticated change path.

For `__clear__`, set category to null, status to pending, attempts to 0, and clear verification metadata. Clearing is available through the bulk dialog, not through an empty inline selection.

The mutation and its journal entries commit together. A success response follows commit. A category or permission rejection does not partially update a request. Concurrent transactions follow last-committed-choice behavior; inspect both committed journal records in T12. This design does not add optimistic locking or promise to reject a stale editor.

## Browser state and failure handling

The shared edit hook tracks active row, selected category, saving state, and error. Opening a second row closes an unsaved first edit after canceling its local selection. While a save is pending, reject another save for that row. Enter invokes save; Escape cancels only while no save is in flight. A failed save retains the row and selection for retry.

The bulk coordinator snapshots the selected IDs, partitions them into at most 500 IDs per request, and submits sequentially. It tracks:

- Confirmed batches and their returned changed-row counts.
- The batch that failed or lost its response.
- IDs not yet attempted.

A definite server rejection rolls back that request. A transport failure may occur after commit, so label that batch unresolved. Stop further submissions in either case. Refresh confirmed progress immediately, then re-read the unresolved IDs through the authorized read path. Show current values and history context before offering an explicit retry. A retry is a new attributable decision and can overwrite a concurrent edit; never perform it silently.

On full or partial completion, invalidate the affected list and count queries. Preserve the administrator's tab and filters, but reset a cursor that no longer identifies a valid page. Avoid a stale success message that announces the original selection size when fewer active rows changed.

## Compatibility and migration

M1 introduces classification and dependent readers. M2 adds optional administration filters. M3/M4 build indexes concurrently in separate migration units. M5 adds the attributed mutation. Generated TypeScript contracts must match those database signatures before the new UI is enabled.

Keep old read calls supported until the next compatibility release. M6 later removes the obsolete Review filter parameters after caller inspection. An interface rollback leaves additive database support and history intact.

## Decisions and verification

The [ADR](architecture_decision_record.md) selects one database classification rule. The [DDR](design_decision_record.md) selects explicit reconciliation rather than automatic bulk retry.

T01–T08 cover reads and authorization. T09–T17 cover editor state, atomic writes, metadata, concurrency, bulk boundaries, response loss, and refreshed state. T18–T20 cover controls, compatibility, and measured database behavior. These checks are defined in the [test specification](test_specification.md).

Before implementation, confirm the exact parked-helper signature, journal trigger behavior, and migration tool's concurrent-index support. A mismatch requires design reconciliation; changing the behavior silently is not an acceptable implementation shortcut.
