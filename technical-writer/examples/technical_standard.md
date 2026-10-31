# Website category change standard

Status: Adopted under the [manual review policy](policy.md)
Owner: Engineering lead

## Purpose and scope

These rules apply to Websites Review read contracts, inline assignments, and bulk assignments or clearing. They govern the implementation and its release evidence. Automated category-provider writes remain outside scope.

## Definitions

**Request** means one invocation of the category mutation. **Batch** is the group of at most 500 IDs submitted in that invocation. **Confirmed** means a successful response establishes committed progress. **Unresolved** means the final outcome is not established. **Actor** is the authenticated administrator, never an identity accepted solely from browser input.

## Principles

Enforce authority at the data boundary. Keep category state, verification metadata, and history consistent. Treat response loss as uncertainty. Use the specification's queue definition instead of duplicating rules in each consumer.

## Rules

- CAT-01: Administration reads and category writes must reject unauthenticated and non-administrator callers at the database boundary.
- CAT-02: One category request must accept no more than 500 supplied IDs and must commit all changes and journal entries together or none.
- CAT-03: Assignments must use an active category, set manual verification metadata, and attribute committed changes to the authenticated administrator. Deleted websites must remain unchanged.
- CAT-04: Clearing must remove the category, return verification state to Pending, reset attempts, and clear prior verification metadata.
- CAT-05: Pending and Review must use the common classifier and the same active/filter predicate for list, count, and matching IDs. All retains its existing citation-based population.
- CAT-06: Bulk callers must stop after the first failed request, retain confirmed progress and unresolved IDs, and reconcile uncertain outcomes before offering an explicit retry.
- CAT-07: The interface must refresh rows and counts after confirmed full or partial changes and must not report an unresolved operation as fully successful.
- CAT-08: Release evidence must measure the SDD's database limits with the stated dataset and conditions, including journaling for the maximum-size mutation.

## Verification

| Rule | Method and compliant result |
| --- | --- |
| CAT-01 | T08 makes direct calls with denied identities; requests are rejected and data is unchanged |
| CAT-02 | T14–T15 check 0/500/501 IDs and force a journal failure; limits hold with no partial changes |
| CAT-03 | T11–T13 inspect fresh values and history, including concurrent saves and deleted rows |
| CAT-04 | T13 clears a Review row; it becomes Pending with category and verification metadata removed |
| CAT-05 | T01–T07 compare classification, active populations, filters, counts, IDs, and pagination |
| CAT-06 | T16 rejects a batch and separately loses a post-commit response; later submissions stop and retry requires reconciliation |
| CAT-07 | T17 checks rows, counts, selection, and feedback after full and partial completion |
| CAT-08 | T20 archives query text, buffer hits/reads, elapsed time, mutation duration, and index measurements |

## Responsibilities and exceptions

Engineering maintains enforcement and repeatable tests. QA checks evidence, including failure paths. Product confirms feedback and scope.

The policy permits a temporary alternative interface with documented verification. It does not permit bypassing CAT-01 or losing actor history. No exception changes WEB-01–WEB-12 without an explicit specification revision.

## Ownership, review, and related policy

The engineering lead reviews changes to limits, authorization, attribution, and recovery. Update checks when an approved rule changes. The [policy](policy.md) supplies accountability, the [LLD](low_level_design.md) defines contracts, and the [test specification](test_specification.md) supplies procedures.
