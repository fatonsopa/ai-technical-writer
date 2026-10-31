# A bulk category change can stop after some batches have already committed

Status: Accepted, 2026-10-27
Decision authority: Engineering lead and product owner
Component: Bulk category dialog and request coordinator

A category request accepts at most 500 website IDs. A selection of 1,001 IDs therefore requires three requests. If the second request fails, the first request may already have committed. If its response is lost, the second request may also have committed even though the browser cannot confirm it.

WEB-09 requires atomicity within each request and honest partial progress across requests. WEB-07 preserves attributable manual decisions, including concurrent edits. The [LLD](low_level_design.md) needs a client failure strategy that respects both requirements.

## Options considered

### Option A: Stop, reconcile, and offer an explicit retry

Submit batches sequentially and stop after the first failed request. Preserve confirmed counts, unresolved IDs, and unattempted IDs. Re-read an uncertain batch before the administrator chooses a retry.

This limits additional changes after trouble and avoids silently overwriting a concurrent administrator's choice. It requires more interface states and a way to explain that a transport failure differs from a definite server rejection. Reading current values cannot prove that a request never committed, so reconciliation should retain relevant history context.

### Option B: Retry failed requests automatically

This can recover from temporary connectivity failures with less user interaction. However, setting the same category again can still add history and overwrite a newer manual decision. Without a request-identity contract, the client cannot treat the operation as safely replayable. Adding that contract would expand this release.

### Option C: Continue with later batches

This maximizes attempted work after a failure. It also increases changes made while the administrator has incomplete feedback and creates several possible gaps to reconcile. There is no product requirement to continue in that situation.

## Recommended option (A)

Stop after the first failed request and keep progress explicit. For a definite rejection, identify that batch as unchanged. For a lost response, identify it as unresolved until a fresh read and history review establish current state. Refresh confirmed progress even while reconciliation remains open.

Report changed rows from successful responses, not simply submitted IDs; deleted rows may be skipped. Offer a retry only as a new explicit action, with the possibility of concurrent edits visible.

Test both rejection and response loss. A mocked error before the request reaches the server does not exercise the uncertain-commit branch.

## Outcome

Option A is accepted. WEB-09 and the LLD use this behavior. T16 covers failure branches and T17 covers refreshed counts in the [test specification](test_specification.md). The [SDD](spec_driven_development.md) owns the accepted behavior. Automatic write retry remains outside this release and would require a separate behavioral and design decision.
