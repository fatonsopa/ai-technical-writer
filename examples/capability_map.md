# Websites Review capability map

## Initiative

Administrators resolve websites whose automated category confirmation has stopped, as described in the [Product Requirements Document (PRD)](product_requirements_document.md) for Websites Review.

## Capabilities

| ID | Capability | Responsibility |
| --- | --- | --- |
| CAP-1 | Find websites that need attention | Pending and Review lists with counts, filters and reasons. Excludes editing. |
| CAP-2 | Assign one website's category | Inline assignment with attribution and a fresh read. Excludes bulk changes. |
| CAP-3 | Change many categories at once | Bulk assign and clear, batching and partial-completion feedback. |

## Dependencies

| Capability | Depends on | Reason |
| --- | --- | --- |
| CAP-3 | CAP-2 | Bulk changes reuse the attributed, actor-aware category save that CAP-2 delivers; without it, a bulk change can't record who made it. |

CAP-1 and CAP-2 don't depend on each other: the lists work with today's editing, and inline editing works from today's list.

## Build order

CAP-1 and CAP-2 can start now, in parallel. CAP-3 starts when CAP-2's attributed save is available.

## Open questions

- Whether CAP-3's clear action belongs in CAP-2 later; the product owner decides after the first release.
