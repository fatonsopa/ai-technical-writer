# Websites Review feature map

## Surfaces

| Surface | Entry or route | Control or handle | End state | Source and status |
| --- | --- | --- | --- | --- |
| Review tab | Websites administration page, Review tab | Tab labeled Review | Lists unverified parked websites with their reason and a count | Specification WEB-01, WEB-02, version 1; source-reported, not observed in a build |
| Inline category assignment | Any tab, a website row | The row's category control, then Save or Enter; Cancel or Escape discards | The website shows the saved category and, if it was in Review, leaves Review after refresh | Specification WEB-06, user flow steps 6 to 11, version 1; source-reported |
| Domain-ending filter | Any tab, More filters | Domain-ending field under More filters | Rows and counts show only matching endings; `.CN` behaves like `cn` | Specification WEB-03, version 1; source-reported |
| Bulk category dialog | Any tab, selected rows | The bulk dialog's assign or clear action | Confirmed rows refresh; a partial failure shows confirmed and unresolved work separately | Specification WEB-08, WEB-09, WEB-10, version 1; source-reported |

## Gaps

- No route, accessible name or selector for any control has been observed in a running build. A verifier needs one observation per surface before relying on a handle.
- The bulk dialog's opening control isn't named in the specification.
