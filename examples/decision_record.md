# The Websites toolbar has no room for another always-visible filter

The All tab already includes domain search, category filtering, and a school filter. Making the new domain-ending field permanently visible would crowd the toolbar at the supported desktop width. WEB-03 requires the filter on every tab; it does not require permanent visibility.

## Options considered

### Option A: Put the field in More filters

Keep the main toolbar compact and use the existing expandable filter area. The field remains available on All, Pending, and Review. Its active value needs a visible indication when the panel is closed.

### Option B: Keep the field on the main toolbar

The field is immediately discoverable, but All needs another toolbar row or narrower controls. Long category labels and the school filter make this especially difficult.

## Recommended option (A)

Use More filters and show the active ending in the filter summary. This fits the existing page pattern without reducing space for primary controls. Verify applying, clearing, and rediscovering the value at supported widths.

## Outcome

Accepted for the first release by the product owner and engineering lead on 2026-10-27. [WEB-11](spec_driven_development.md#web-11-preserve-controls-and-compatibility) records the placement rule and [T18](test_specification.md#interface-compatibility-and-performance-cases) checks layout. This record can live as a comment on the parent Feature.
