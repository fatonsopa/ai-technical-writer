# Websites Review acceptance completion report

Scope: First-release staging acceptance cycle
Build: wr-candidate-2
Environment: Isolated staging acceptance environment
Reporting period: 2026-10-29, 09:00–15:00 UTC
Basis: [Test plan](test_plan.md) and [test specification](test_specification.md), version 1

## Testing and results

All 20 planned cases executed and passed on wr-candidate-2: 20 passed, 0 failed, 0 blocked, and 0 not run. Run R2 is a complete rerun, not a combination of selected passes from candidate 1.

| Requirement | Cases and evidence | Assessment |
| --- | --- | --- |
| WEB-01–WEB-02 | R2 T01–T03 | Nine classifications match; active Review/Pending/All populations are 3/4/6, including the uncited rows in their intended queues |
| WEB-03–WEB-04 | R2 T04–T07 | Normalization, wildcard rejection, combined filters, selection agreement, and stable keyset traversal pass |
| WEB-05 | R2 T08 | Direct denied calls leave data and successful-change history unchanged |
| WEB-06 | R2 T09–T10, R2-E10 | Save/cancel/progress behavior passes; rejected saves retain the selected category |
| WEB-07–WEB-08 | R2 T11–T13 | Persistence, actor metadata, concurrent decisions, clear transitions, and deleted-row protection pass |
| WEB-09 | R2 T14–T16, R2-E15/R2-E16 | Limits, journal-failure rollback, sequential batching, rejection, and response-loss reconciliation pass |
| WEB-10 | R2 T17, R2-E17 | Rows and counts refresh after full and partial progress |
| WEB-11 | R2 T18–T19 | Desktop layout, control placement, and compatible old calls pass |
| WEB-12 | R2 T20, R2-P20 | Measured database and maximum-batch conditions pass on the recorded snapshot |

R2-P20 uses the same 100,000-website snapshot dimensions as R1, with 6,349 active Pending and 615 active Review rows. Pending first page measured 12 ms/428 shared-buffer pages; Review measured 10 ms/316 pages. The 500-row journaled mutation took 1.7 seconds. Both indexes were valid; isolated builds measured 3.3 seconds/320 KB and 4.2 seconds/4.8 MB. The record includes query text, schema revision, sort, and cache conditions.

## Defect disposition and deviations

Candidate 1 ended with 15 passes, 2 failures, 1 blocked case, and 2 not-run cases. Its T10 failed-save selection loss and T17 stale-count defect were corrected before R2. R2-E10 and R2-E17 verify the original failure conditions and adjacent success/cancel behavior.

The missing journal-failure facility was added in the isolated environment. R2-E15 forces history insertion failure and verifies that the entire request leaves website and journal state unchanged. This closes the earlier atomicity evidence gap.

No planned case was waived or substituted. The final run includes the previously unrun layout and compatibility cases. The [incident report](incident_report.md) records the earlier staging interruption associated with partial-progress feedback; its follow-up checks are included here.

## Remaining risks and limits

Results cover the defined desktop experience, controlled fixtures, and one production-shaped snapshot. They do not measure mobile layout, provider classification accuracy, every possible concurrent workload, or future queue growth. Database execution checks do not establish end-to-end browser latency.

Production index scheduling still needs the release team's environment-specific review. Keep additive compatibility support in place for the agreed release period. Monitor attribution, permission errors, mutation failures, and row/count agreement after rollout.

## Assessment and follow-up

The test plan's exit criteria are met for wr-candidate-2. Recommend controlled rollout of the reviewed artifacts with the stated monitoring and recovery plan. This report supplies the QA assessment; it does not record a production deployment or substitute for the authorized release decision.

After rollout, run the smoke checks on the released version and record any difference separately. Remove obsolete filter compatibility only after caller evidence and the compatibility period are complete.

## Sources

R2 case register T01–T20; captures R2-E10, R2-E15, R2-E16, and R2-E17; performance record R2-P20; R1 status and defect evidence. The [status report](test_status_report.md) preserves candidate 1's unfinished result set.
