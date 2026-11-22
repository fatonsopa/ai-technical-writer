# Retrying an uncertain bulk-edit batch

## Question

Should the bulk category editor retry a batch automatically when its response is lost? The batch coordinator's design depends on the answer.

## Sources

- [Websites Review behavior specification](spec_driven_development.md#web-09-respect-request-boundaries-and-partial-completion), WEB-09, version 1, 2026-10-27. Read in full.
- [Websites Review acceptance checks](test_specification.md), T16. Read in full.
- Reviewer report, 2026-11-18: "the batch timed out, so the tool should just retry it."

## Findings

WEB-09 says: "Do not retry an uncertain write automatically. Reconcile its actual state before presenting a retry, and make any retry an explicit administrator action." T16 shows why: after the second batch's response is lost, 500 rows are confirmed, 500 are unresolved and 1 was not attempted. The unresolved batch may already have committed, so retrying it blindly could repeat changes. The reviewer's report describes the symptom correctly but proposes the retry that WEB-09 excludes.

## Alternatives

| Option | What the evidence shows |
| --- | --- |
| Retry the batch automatically | Excluded by WEB-09. |
| Reconcile, then offer the administrator an explicit retry | Required by WEB-09 and checked by T16. |
| Stop and report without offering a retry | Consistent with WEB-09, but leaves the administrator to rebuild the selection by hand. |

## Uncertainty and gaps

Why the second response was lost is unknown; no log or trace was supplied. That doesn't affect the retry rule, but it does affect any claim about how often the problem occurs.

## Recommendation and decision owner

Recommendation: reconcile the unresolved batch, then offer an explicit retry. Changing WEB-09 to allow automatic retry would need the product owner's decision and a specification revision. State: open; this record recommends and doesn't decide.
