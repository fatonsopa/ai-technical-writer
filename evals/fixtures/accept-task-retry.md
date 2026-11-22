# Source facts

Governing requirement WEB-09 (Websites Review behavior specification, version 1): A request may contain at most 500 website IDs. For a larger selection, submit sequential batches. After the first failed request, stop submitting further batches. Keep confirmed progress, the unresolved batch, and unattempted IDs distinguishable. Do not retry an uncertain write automatically. Reconcile its actual state before presenting a retry, and make any retry an explicit administrator action.

WEB-10: After confirmed changes, refresh affected rows and tab counts. Never label a partial or uncertain operation fully successful.

## Existing task excerpt

## Acceptance criteria

- WEB-05–WEB-08: Only administrators can change categories; inline assignment, attribution, and clearing have the specified outcomes.
- WEB-09–WEB-10: Requests respect the 500-ID boundary; partial or uncertain writes stop and are reported honestly; confirmed rows and counts refresh.
