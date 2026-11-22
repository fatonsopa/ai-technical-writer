# Websites Review requirements-quality checklist

Specification: [Websites Review behavior specification](spec_driven_development.md), revision version 1, 2026-10-27.

## Checks

| Requirement | Question | Evidence | Verdict | Correction or owner |
| --- | --- | --- | --- | --- |
| WEB-09 | Is it clear who may retry an uncertain batch? | "Do not retry an uncertain write automatically. Reconcile its actual state before presenting a retry, and make any retry an explicit administrator action." | Ready | None; the administrator retries, only after reconciliation. |
| WEB-03 | Are accepted and rejected ending inputs listed? | "`.CN`, ` cn `, and `cn.` must behave like `cn`… Reject wildcard inputs such as `c%n` and `*.cn`." | Ready | None. |
| WEB-12 | Is the performance limit measurable? | First-page database time at most 1,000 ms and 5,000 shared-buffer pages. | Ready | None. |

## History

- Draft 2026-10-20: WEB-09 read "Retries are handled by the system after a failure." Verdict: Needs decision. It didn't say whether retries are automatic or who starts them. Correction requested from the product owner.
- Version 1, 2026-10-27: WEB-09 now names the administrator as the only one who retries, after reconciliation. Verdict changed to Ready. Only this row was updated.
