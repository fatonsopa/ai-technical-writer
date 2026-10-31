# Why Pending, Review, and All can show different totals

Pending and Review answer a question about outstanding work. Pending means automation still owes an answer; Review means automated confirmation has stopped and a person needs to decide. A verified website belongs to neither queue.

All answers a different question. It preserves the existing citation-based administration population. A website without a citation aggregate can therefore appear in Review but be absent from All. Adding the Pending and Review totals is not a way to calculate All.

## Classification and visibility

The database classifier uses verification state and the common parked rule. It does not decide whether a website is deleted or has citations. The administration query then applies active-row and filter conditions.

This separation matters for deleted websites. A deleted parked website can still classify as Review, while the active Review page correctly excludes it. Moving deletion into the classifier would change the helper's meaning for other readers.

## What a manual decision changes

Assigning a category confirms a human choice. The website becomes verified, its attempts reset, and history identifies the administrator. It leaves Review because that outstanding work has been resolved.

Clearing a category is different: it removes the classification and returns the website to Pending. It does not count as a completed manual verification. The bulk dialog offers clearing explicitly so an empty inline selection is not mistaken for that action.

## Why counts must come from the same rules

Rows, counts, and matching-ID selection must share the same population and filters. A browser cannot repair a missing uncited row after the server has paginated a different set. The [ADR](architecture_decision_record.md) explains why classification stays in the database; the [SDD](spec_driven_development.md) defines the required behavior.
