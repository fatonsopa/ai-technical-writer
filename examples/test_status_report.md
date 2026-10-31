# Websites Review testing status

Reporting period: 2026-10-28, 09:00–16:00 UTC
Build: wr-candidate-1
Environment: Isolated staging acceptance environment
Status: Testing in progress; release exit criteria are unmet

## Progress and results

Of 20 planned cases, 17 executed: 15 passed and 2 failed. One case is blocked and two have not run. Thus 17/20 cases executed and 15/20 passed; neither number is a code-coverage percentage.

| Cases | Result | Evidence and meaning |
| --- | --- | --- |
| T01–T09 | Passed | R1 database and interaction records support classification, populations, filters, selection, permission denial, and basic inline controls |
| T10 | Failed | R1-E10: rejected inline save closes the editor and loses the selected category, contradicting WEB-06 |
| T11–T14 | Passed | R1 mutation records show persisted metadata, actor history, concurrency, clearing, and request boundaries |
| T15 | Blocked | Journal-failure interception is unavailable on this candidate |
| T16 | Passed | R1-E16 covers full batching, definite rejection, and lost-response reconciliation |
| T17 | Failed | R1-E17: a partial bulk change leaves old tab counts until manual reload, contradicting WEB-10 |
| T18–T19 | Not run | Layout and compatibility work remains in this cycle |
| T20 | Passed | R1-P20 records the production-shaped query, batch, and index checks |

The R1-P20 snapshot contains 100,000 websites, 6,349 active Pending rows, and 615 active Review rows. Default Pending measured 11 ms and 420 shared-buffer pages; Review measured 9 ms and 310 pages. A 500-row journaled mutation took 1.6 seconds. The unsettled and reversed-domain indexes were valid; isolated build observations were 3.2 seconds/320 KB and 4.1 seconds/4.8 MB. These observations apply to this snapshot and candidate.

## Coverage, blockers, and risks

The passed cases support WEB-01–WEB-05 and WEB-07–WEB-09's exercised behavior. WEB-06 and WEB-10 have observed failures. WEB-09's journal-failure atomicity branch remains unverified despite passing boundary and batching checks. WEB-11 has no completed result yet. WEB-12 meets its stated checks on this candidate, but any relevant query or mutation fix requires another measurement.

The T10 failure risks forcing an administrator to reconstruct a choice after a rejected save. The T17 failure can make completed work appear outstanding and encourage unnecessary repeated changes. Neither observation establishes a database persistence defect. The missing T15 facility prevents a claim that history failure preserves atomicity.

## Next work

Engineering will retain selection after a failed inline save and invalidate counts after confirmed partial progress. Add the isolated journal-failure interception point. QA will run T15, T18, and T19, then rerun all 20 cases on the next candidate because shared state handling is changing.

Keep R1 results scoped to wr-candidate-1. Do not merge later passes into this candidate's totals. Release review remains blocked until the [test plan](test_plan.md) exit criteria are met.

## Sources

R1 case register and captures R1-E10, R1-E16, and R1-E17; performance record R1-P20; [test specification](test_specification.md), version 1; [test plan](test_plan.md).
