# Implement Websites Review and category editing

Status: Ready for implementation against the agreed behavior baseline
Scope: Administration lists, category mutation, and supporting database contracts
Sources: [Spec Driven Development document (SDD)](spec_driven_development.md), [High Level Document (HLD)](high_level_document.md), [Low Level Design (LLD)](low_level_design.md)

## Goal and specification

Give administrators separate All, Pending, and Review views and a reliable way to assign or clear website categories. WEB-01 through WEB-12 define acceptance. In this plan, a parked website is an unverified website for which `website_confirm_is_parked` returns true. An active website is one not marked deleted. Queue classification and active-list visibility are separate concerns.

Implement the database contracts before enabling their callers. Preserve the old All population and old callers during the compatibility period. Do not turn this list change into a categorizer rewrite or a backfill.

## Current context and approach

The administration page is `src/pages/admin/websites/AdminWebsitesPage.tsx`. It already uses paged database functions, category controls, and a bulk category dialog. The existing All query joins citation aggregates, which excludes uncited websites. Pending and Review need a different population without changing All.

The database will own classification through `public.website_review_state(websites)`. The list, count, and matching-ID functions will apply a shared predicate with queue and domain-ending parameters. Category writes will go through `bulk_change_website_category(uuid[], text)`, including one-row inline edits. This keeps permission checks, verification metadata, and attribution consistent.

The parked-state helper is a prerequisite from task 46. Confirm its signature and behavior in the target migration chain before starting dependent work. The architecture and bulk-failure decisions are recorded in the [Decision Record (DR): architecture](decision_record_architecture.md) and [Decision Record (DR): component design](decision_record_component_design.md).

## Work sequence

### 1. Establish the baseline and fixtures

Inspect the existing definitions of `_admin_websites_predicate`, `list_admin_websites_page`, `count_admin_websites`, and `admin_website_ids`. Record current signatures, grants, All filtering, sort behavior, and callers. Inspect the shared change journal and confirm how `auth.uid()` is recorded for administration writes.

Create the nine-state fixture from the [Test Specification (TS)](test_specification.md) in a disposable database. Capture baseline All membership and the existing automated reader results before modifying functions. Include all nine states, including the deleted row.

Result: a reproducible baseline and confirmed prerequisite. Stop if the parked-state helper or actor handling differs from the design; resolve that conflict before writing dependent migrations.

### 2. Add central classification and compatible readers

Create migration M1 for `website_review_state` and the named automated readers that need the common parked definition. Keep classification free of citation joins and deletion filtering. Compare reader results before and after the change; the new helper must not accidentally restart parked work or change unrelated categorization behavior.

Create M2 to add `p_queue` and `p_tld` to the administration read contracts, with null defaults for existing callers. Build the queue, active-row, domain, category, and suffix conditions through the shared predicate. Pending and Review use left joins where aggregates are optional. All retains its existing population.

Verify list/count/ID agreement under combined filters, empty results, deleted fixtures, and permission denial. Verify keyset traversal without duplicates on an unchanged dataset. A count mismatch blocks the next stage because it makes selection unreliable.

### 3. Add and measure the read indexes

Use separate migrations M3 and M4 for the unsettled-created index and reversed-domain index. Each concurrent index build must run outside a transaction according to the deployment tool's supported procedure. Inspect failed-build remnants and index validity before retrying; do not blindly create a duplicate index.

On a production-shaped disposable dataset, capture `EXPLAIN (ANALYZE, BUFFERS)` for the agreed first-page queries. Check WEB-12's database execution-time and buffer-page limits. Record dataset size, query, sort, cache conditions, and index definitions. A fast small-fixture query does not satisfy this check. Measure index build duration and size before scheduling production rollout.

### 4. Implement the attributed mutation

Create M5 for `bulk_change_website_category(uuid[], text)`. Enforce administrator authorization, the 500-ID request limit, active category validation, and deleted-row protection. Apply each request atomically. Set the category and manual verification metadata together; the clear sentinel resets category and verification state to Pending.

Verify journal entries identify the signed-in administrator. Test zero IDs, 500 IDs, 501 IDs, inactive categories, denied callers, deleted rows, forced failure, and concurrent manual changes. Confirm a 500-row request remains below the authenticated role's eight-second statement timeout with journaling enabled. Do not increase the timeout to conceal an unmeasured mutation cost.

Regenerate `src/integrations/supabase/types.ts` and `packages/supabase/src/database.types.ts` through the repository's established process. Review the resulting signatures against the Low Level Design (LLD).

### 5. Build tabs and filter behavior

Add `src/pages/admin/websites/WebsitesSubTabs.tsx` and integrate it in `AdminWebsitesPage.tsx`. Keep tab selection, query parameters, pagination reset, and counts consistent. Pending and Review default to Added descending; All retains its current default.

Place the typed domain-ending field in More filters. Remove the old Review status filter and duplicate browser classification. Restrict school filtering and citation-population actions to All. Show the Review reason and hide Check category on Review. Update `e2e/admin-route-catalog.ts` for any changed route coverage.

Verify the layout at the agreed desktop widths, including long category labels and the All toolbar with its school filter. Confirm filtering does not retain a stale keyset cursor from the previous tab.

### 6. Add inline and bulk editing

Add `src/components/admin/websites/WebsiteCategoryCell.tsx` and a shared `useWebsiteCategoryEdit` hook. Allow one active row, explicit save/cancel actions, Enter/Escape behavior, and a saving indicator. A failed save retains the selection and edit state. Do not add inline clearing.

Change `src/components/admin/dialogs/BulkChangeWebsiteCategoryDialog.tsx` to call the same mutation in chunks of at most 500 IDs. Stop after the first failed request. Keep confirmed progress separate from the unresolved batch and unattempted IDs. Reconcile an uncertain request through a fresh read before offering a retry, as defined in the component design decision.

Refresh rows and counts after confirmed changes, including partial completion. Inspect `AdminWebsiteDetailPage.tsx` only if the detail-page reproduction demonstrates the same stale-review defect. Keep that fix conditional rather than expanding scope preemptively.

### 7. Verify, document, and prepare rollout

Run the defined database, component, and browser checks, then review all WEB requirements against their evidence. Record progress in a Test Status Report (TSR) and the milestone outcome in a Test Completion Report (TCR). Remove the mockup route and `WebsitesReviewMockup.tsx` only after the replacement interface has been verified. Update `src/routes/AdminRoutes.tsx` accordingly.

Update the living High Level Document (HLD) from the implemented design, publish the administrator how-to, and reconcile any approved behavior changes with the Spec Driven Development document (SDD). Do not mark a planned check as passed because its implementation exists.

## Requirement coverage

| Requirement | Implementation area | Verification |
| --- | --- | --- |
| WEB-01 | Central classifier and readers | T01–T02: nine-state classification and reader equivalence |
| WEB-02 | Queue list joins and active predicate | T03: uncited inclusion, deleted exclusion, unchanged All |
| WEB-03 | Shared filter normalization | T04–T05: valid endings, wildcard rejection, combined filters |
| WEB-04 | List/count/ID contracts and pagination | T06–T07: matching populations and keyset traversal |
| WEB-05 | Function grants and administrator checks | T08: direct read/write denial for unauthorized callers |
| WEB-06 | Shared inline editor | T09–T10: save/cancel and retained error state |
| WEB-07 | Category mutation and journal | T11–T12: manual verification, actor, concurrency |
| WEB-08 | Bulk clear branch | T13: clear metadata and Pending transition |
| WEB-09 | Request validation and batch coordinator | T14–T16: boundaries, atomicity, partial failure |
| WEB-10 | Page refresh and bulk feedback | T17: rows/counts refresh after full or partial completion |
| WEB-11 | Tabs, actions, and compatibility | T18–T19: control placement and old callers |
| WEB-12 | Indexes and measured queries | T20: first-page and mutation performance evidence |

## Rollout and recovery

Deploy the additive database changes to staging first, then the administration interface. Keep old parameters and callers supported while both versions may run. Promote the same reviewed artifacts after staging verification and the project's release approval.

Observe permission errors, mutation failures, first-page query performance, queue/count consistency, and actor attribution. If the interface fails, disable the new controls or restore the prior interface while leaving additive database support in place. Preserve category changes and their history; reverting application code does not authorize deleting administrator decisions.

For incorrect committed categories, identify affected IDs and journal entries, obtain the required correction authorization, and apply an attributable compensating change. Do not restore an entire table to undo a narrow category mistake.

Remove the old `p_needs_review` and `__needs_review__` compatibility paths in M6 only after one compatibility release and evidence that no supported caller uses them. Handle that removal as a separate release step.

## Risks and readiness limits

Index build cost and 500-row mutation duration require measurement. Partial failures need both a definite server rejection and a lost-response test. The detail-page fix remains conditional. No production date or duration estimate is committed here; scheduling follows these dependency and readiness checks.
