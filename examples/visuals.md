# How a partial bulk change stops and recovers

This sequence shows the Websites Review design for a 1,001-ID selection when the second request loses its response after committing.

```mermaid
sequenceDiagram
    accTitle: Partial category change with a lost response
    accDescr: Batch one confirms 500 changes. Batch two commits but its response is lost. The client stops before the final ID, reports uncertainty, and reads current state before offering an explicit retry.
    actor A as Administrator
    participant UI as Bulk dialog
    participant DB as Database API
    A->>UI: Assign category to 1,001 IDs
    UI->>DB: Batch 1: 500 IDs
    DB-->>UI: 500 changes committed
    UI->>DB: Batch 2: 500 IDs
    Note over DB: Changes and history commit
    DB--xUI: Response lost
    Note over UI: Stop, do not send batch 3
    UI-->>A: 500 confirmed, 500 unresolved, 1 unattempted
    UI->>DB: Authorized reconciliation read
    DB-->>UI: Current values and relevant history
    UI-->>A: Show state before an explicit retry
```

The first successful response confirms 500 changed rows. Losing the second response does not establish rollback, so those 500 IDs remain unresolved until reconciliation. The last ID is unattempted. The client must not report that only 500 rows changed in the database; it can only confirm that many before the read.

Each mutation request is atomic, but the entire selection is not one transaction. The [DDR](design_decision_record.md) explains the retry tradeoff, and T16 in the [test specification](test_specification.md) checks this branch.
