# Slow category assignment in the Websites Review queue

## Decision

Decide whether bulk category actions for the Review queue should go to product definition. If you proceed, a Product Requirements Document (PRD) author defines the change from this brief. If not, administrators keep assigning categories one website at a time.

## Problem and who is affected

Administrators open each website in the Review queue separately to assign or clear its category. The product owner reports that this keeps them from clearing the queue in one sitting. The evidence is the owner's interview and the specification, where inline editing changes one row at a time (WEB-06) and bulk actions exist only in a separate dialog (WEB-08, WEB-09).

## Desired outcome

Administrators can assign or clear the category of several Review rows at once and finish the queue in one sitting.

## Non-goals

- Changing when automated confirmation parks a website and moves it into Review.
- Automatic category assignment.

## Unknowns and open choices

- Current time to clear the queue: no baseline has been measured, and the owner gave no target time. Measuring it would show whether the change helps.
- Maximum number of rows in one bulk action: deferred to the specification author.

## Sources

- [Faster Websites Review discovery interview](discovery_interview.md), confirmed by the product owner on 2026-11-18.
- [Websites Review behavior specification](spec_driven_development.md), WEB-01 to WEB-06.
- No appetite was supplied.
