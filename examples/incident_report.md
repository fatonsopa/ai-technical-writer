# Partial category changes left stale Review counts in staging

Incident: WR-INC-01
Build: wr-candidate-1
Environment: Staging acceptance

## Status and impact

Resolved for the acceptance environment in wr-candidate-2. During a bulk-failure exercise on 2026-10-28, 500 category changes committed successfully, but the Review count continued to show the pre-operation total after the second batch was rejected.

The affected scope was one isolated 1,001-website selection. The first 500 websites changed, the next 500 were rejected, and the final website was not attempted. No repeated write or data loss was observed in the captured session. The stale count could have led an administrator to repeat work, so further acceptance activity using that page state was paused until its data was refreshed.

This was a staging interruption, not a production outage. It exposed a WEB-10 failure while WEB-09's stop-after-failure behavior worked as intended.

## Timeline and evidence

| Time UTC, 2026-10-28 | Event | Source |
| --- | --- | --- |
| 13:00 | QA started T16/T17 with 1,001 isolated Review rows | R1-E16 setup record |
| 13:02 | First 500-ID request committed and returned 500 | Request capture and change journal |
| 13:03 | Second request was rejected; the coordinator stopped before request 3 | R1-E16 request sequence |
| 13:04 | The dialog reported partial completion, but the tab count retained its earlier value | R1-E17 screen capture |
| 13:08 | A fresh authorized read confirmed the 500 committed assignments and remaining Review rows | R1-E17 database comparison |
| 13:12 | QA paused further actions from the stale page and reloaded it | Acceptance action record |
| 13:14 | Reloaded rows and counts matched the database | R1-E17 recovery capture |
| 15:20 | Engineering traced invalidation to the full-success branch only | Candidate-1 code review record |

## Response and recovery

The immediate mitigation was to stop acting on the stale page and perform a fresh read. That restored an accurate view without undoing the confirmed category decisions. The journal and returned count established which changes had committed, so no compensating write was needed.

Engineering moved affected-query invalidation into the confirmed-progress path, including partial completion. The change preserves the distinction between confirmed and unresolved batches; refreshing the page does not itself resolve an uncertain write.

R2-E17 repeated the rejected-second-batch sequence on candidate 2 and verified updated rows, counts, and feedback. R2-E16 separately covered a post-commit lost response. These checks establish recovery for the observed failure paths, rather than every possible future network failure.

## Causes and lessons

The immediate cause was a client invalidation path that ran after complete success but not after partial completion. The database had committed the first request correctly. Treating the bulk dialog as one logical success/failure unit obscured the fact that each request had its own transaction boundary.

The original interaction check asserted the partial message and stopped further requests, but did not assert the surrounding page counts. Testing the dialog in isolation was insufficient for WEB-10. A successful component-level failure check can coexist with incorrect page-level state.

The response was helped by retained request order, changed-row counts, and actor history. These let responders distinguish stale display state from failed persistence. Preserve that evidence before retrying or choosing a data repair.

## Follow-up

| Action | Owner | Acceptance criteria |
| --- | --- | --- |
| Refresh after any confirmed progress | Administration engineering | T17 verifies rows and counts after full success and a rejected later batch; completed in R2-E17 |
| Cover response loss after commit | QA and administration engineering | T16 distinguishes 500 confirmed, 500 unresolved, and 1 unattempted ID before reconciliation; completed in R2-E16 |
| Include page state in bulk regression checks | QA | The suite asserts counts and selection as well as dialog text; included in candidate-2 acceptance |
| Review released smoke evidence | Release owner | Released rows/counts and actor attribution match fresh reads; pending rollout |

The [completion report](test_completion_report.md) records the final candidate's complete results. The [DDR](design_decision_record.md) remains the decision source for partial and uncertain writes.
