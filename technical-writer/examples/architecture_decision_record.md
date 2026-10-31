# Different website readers can disagree about which sites need review

Status: Accepted, 2026-10-27
Decision authority: Engineering lead and product owner
Scope: Websites administration reads and shared confirmation state

The administration interface needs to show the same parked state used by automated confirmation. List, count, matching-ID selection, and other readers can diverge if each reimplements the attempt and reason rules. A browser-only rule also cannot restore uncited websites already excluded by an inner join.

WEB-01 requires consistent classification, WEB-02 requires complete queue populations, and WEB-04 requires agreement between rows, counts, and selected IDs. The [HLD](high_level_document.md) keeps website state in PostgreSQL and the browser as a consumer of that state.

## Options considered

### Option A: Share a database classifier

Add `website_review_state(websites)` and call the existing parked helper within it. Administration readers use a common predicate for queue and filter conditions.

This gives database readers one classification definition and lets queries include uncited websites before pagination. It also makes rule changes dependent on database deployment and requires careful review of function grants, indexes, and callers. Classification alone does not solve every visibility rule: active-row filtering and All's citation requirement remain explicit in the read contracts.

### Option B: Classify in the browser

Return verification fields and let the page determine Pending or Review. This keeps display changes near the interface and avoids a new database helper.

However, paging and counts would still need equivalent server logic. Filtering an unfiltered page locally produces incomplete pages and incorrect totals. Other readers would not automatically share the browser's rule.

### Option C: Store a separate review flag

Persist a new flag whenever confirmation state changes. Queries could filter it directly, but every existing writer would need to maintain it. A missed update could leave the flag inconsistent with verification state. This adds synchronization work and historical repair without a demonstrated need for another source of truth.

## Recommended option (A)

Use the shared database classifier. It fits existing data ownership and supports complete server-side filtering and pagination without creating another stored state.

Keep the helper narrow: it returns Pending, Review, or neither. It must not include deletion or citation visibility, because those are caller-specific population rules. Update the HLD to show the shared classifier and document which readers use it. Test the nine-state fixture and reader equivalence before enabling the tabs.

The main tradeoff is stronger coordination around database changes. Preserve compatible signatures during rollout and measure query behavior against WEB-12 rather than assuming the extra helper is free.

## Outcome

Option A is accepted for this initiative's baseline. The [LLD](low_level_design.md) defines the classifier and shared predicate contracts. The implementation plan deploys them before browser callers. Acceptance of this design does not establish that a migration has run or that its checks have passed.
