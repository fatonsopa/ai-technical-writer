# Keep the selected category after a failed inline save

## Description

When an inline category save fails, the administrator must see that the change wasn't saved and keep their selection, so they can retry or cancel. Today the outcome of a failed save isn't specified at the row.

## Expected outcome

After a failed save, the row shows an error, stays in edit mode with the selected category, and shows no success message.

## Specification

Delivers the failed-save criterion of the [story to resolve one parked website](user_story.md#acceptance-criteria): "If the save fails, an error appears and the selected category remains in edit mode without a success message (WEB-06)." The story belongs to the [Websites Review Feature](task.md). Governing requirement: WEB-06 in the [Spec Driven Development document (SDD)](spec_driven_development.md), version 1.

## Scope

One row's inline save failure. Bulk changes, category clearing and successful saves belong to other slices of the Feature.

## Acceptance criteria

- Given a row in edit mode with a selected category, when the save request fails, an error appears at that row.
- The row stays in edit mode with the same category still selected.
- No success message appears, and the row's displayed category is unchanged.

## Relevant files

- Proposed `src/components/admin/websites/WebsiteCategoryCell.tsx`

## Additional context

T10 in the [Test Specification (TS)](test_specification.md) checks this behavior by forcing the save to fail and observing the row.
