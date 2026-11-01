# Add Websites Review tabs and category editing

Type: Feature

## Description

Administrators need to separate websites still awaiting automation from parked websites that require a human decision. The current All view can omit uncited websites and does not provide a consistent manual-review flow.

Add All, Pending, and Review tabs with counts, shared filters, and inline category assignment. Use the existing bulk dialog for assigning or clearing categories. Keep All's existing population and enforce administrator authorization and attributable history.

This is the parent Feature. Focused implementation tasks can follow the [Implementation Plan (IP)](implementation_plan.md); a [User Story (US)](user_story.md) captures the single-website review journey.

## Expected outcome

An administrator can find every active website requiring review, understand its reason, save a category, and see the updated queue state. Ongoing automated work remains separate in Pending. Bulk changes report confirmed and unresolved progress accurately.

## Acceptance criteria

- WEB-01–WEB-04: Classification, active populations, filters, counts, selection, and pagination follow the [Spec Driven Development document (SDD)](spec_driven_development.md).
- WEB-05–WEB-08: Only administrators can change categories; inline assignment, attribution, and clearing have the specified outcomes.
- WEB-09–WEB-10: Requests respect the 500-ID boundary; partial or uncertain writes stop and are reported honestly; confirmed rows and counts refresh.
- WEB-11–WEB-12: Controls, compatible callers, and measured database limits pass the defined checks.
- T01–T20 pass on the final candidate, with results recorded in the completion report.

## Relevant files

- `src/pages/admin/websites/AdminWebsitesPage.tsx`
- `src/components/admin/dialogs/BulkChangeWebsiteCategoryDialog.tsx`
- Proposed `src/components/admin/websites/WebsiteCategoryCell.tsx`
- Proposed database changes M1–M5 in the implementation plan

## Additional context

Provider rules, backfills, restarting parked work, and a new Reason filter are outside scope. The parked-state helper is a prerequisite. Consult the [High Level Document (HLD)](high_level_document.md) before implementation.
