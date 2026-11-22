# Websites Review critical journeys

## Journeys

### CJ-1: Resolve a parked website

Actor: administrator. Criticality: websites in Review are no longer resolved by automation, so a lost save leaves them unresolved (specification WEB-01, WEB-07).

1. Open the Review tab ([feature map](feature_map.md), Review tab).
2. Choose a category in the row's inline control and press Save (feature map, inline category assignment).
3. Refresh the list.

End state: the website shows the saved category and no longer appears in Review; history names the administrator.
Check: T11 in the [test specification](test_specification.md). Result: not run on any candidate yet.

### CJ-2: Recover after a lost bulk response

Actor: administrator. Criticality: a partial bulk failure can leave rows uncertain, and an automatic retry could repeat changes (specification WEB-09).

1. Select 1,001 rows and open the bulk dialog (feature map, bulk category dialog).
2. Assign a category; the second batch's response is lost.

End state: the page shows 500 confirmed, 500 unresolved and 1 unattempted, and offers a retry only after a fresh read.
Check: T16 in the test specification. Result: not run on any candidate yet.

### CJ-3: Filter Review by reason

Actor: administrator. Criticality: proposed by the product owner; not yet a requirement.

1. Open the Review tab and choose a reason filter. This screen is unresolved: the feature map has no reason-filter surface.

End state: not defined. Check: undefined; the journey can't pass until one is written.
