# Resolve one parked website without leaving Review

Parent: [Websites Review Feature](issue.md)
Task type when tracked: Feature

## User story

As an administrator reviewing website categories, I want to assign the correct category directly in Review so that I can resolve a parked website and continue through the queue.

## Context and scope

Review contains active unverified websites for which automated confirmation has stopped. The story covers one category assignment and its visible result. Bulk changes and category clearing belong to separate slices of the parent Feature.

## Acceptance criteria

- Given an active unverified website that is parked, including one without citations, when an administrator opens Review under matching filters, the website and its reason are visible (WEB-01–WEB-02).
- Given a selected active category, when the administrator saves, the row shows progress and prevents another submission until the request finishes (WEB-06).
- When the save succeeds, a fresh read returns the category, the website is manually verified, and history identifies the administrator (WEB-07).
- After success, the website leaves Review and its count refreshes (WEB-10).
- If the save fails, an error appears and the selected category remains in edit mode without a success message (WEB-06).
- A non-administrator cannot perform the same change through a direct request (WEB-05).

## Related checks

T03, T08–T11, and T17 cover this journey in the [test specification](test_specification.md). The parent SDD remains the source of detailed behavior.
