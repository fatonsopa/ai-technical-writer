# Websites Review release test plan

Status: Agreed
Basis: [SDD](spec_driven_development.md), WEB-01–WEB-12, version 1

## Objectives and scope

Establish that administrators can find every active website requiring attention and make attributable category decisions without misleading feedback. The release must preserve existing All behavior and current callers while adding Pending and Review.

Testing covers central classification, read populations, combined filters, counts and selected IDs, keyset navigation, permissions, inline state, mutation metadata, concurrent changes, clearing, bulk boundaries, partial failures, control placement, compatibility, and database performance. It does not assess provider classification accuracy, historical backfill quality, or changes to automated categorization rules.

The highest risks are silent omissions and incorrect changes: an uncited website can disappear before pagination; an inconsistent matching-ID query can change the wrong selection; a lost response can cause a repeat write; missing actor history can make a manual decision untraceable. These risks require direct failure and data checks, not only browser screenshots.

## Approach and resources

Use database integration tests for classification, population agreement, grants, transaction behavior, and history. Use component tests for edit/cancel/progress state and batch coordination. Use browser tests for complete administrator journeys, combined controls, refreshed counts, and supported desktop layouts.

The [test specification](test_specification.md) defines T01–T20 and the nine website states. Run database cases against a disposable database with isolated fixture rows and refreshed citation aggregates. Use seeded administrator and non-administrator identities, active and deleted categories, and two administrator sessions for concurrency.

Use an isolated production-shaped snapshot for performance measurements. Record the snapshot dimensions and index definitions so later results are comparable. Do not infer production readiness from the nine-row functional fixture.

Failure facilities must distinguish a server-side rejection, a journal error before commit, and a response dropped after commit. Browser network failure alone does not establish database rollback. Use test-only interception in the isolated environment; no failure injection is allowed against a live administration session.

## Sequence and responsibilities

Engineering provides the target build, migrations, generated contracts, fixtures, and test interception points. QA independently checks observed outcomes against the specification. Product reviews language, scope, and the manual-review journey. The engineering lead owns the release-readiness review.

Start with T01–T08, because later UI checks depend on correct populations and authorization. Then run mutation and interaction cases T09–T17. Finish controls, compatibility, and performance T18–T20. Repeat relevant earlier checks after any shared-predicate or mutation fix. The implementation plan owns delivery order; this plan owns assessment.

## Entry criteria

- The SDD baseline and decision records are available, including partial-failure behavior.
- The parked-state prerequisite and additive read/mutation contracts are installed in the isolated target environment.
- The target build and schema revision are recorded.
- The nine-state fixture, roles, active/deleted categories, and citation refresh are verified.
- Failure injection and evidence capture are available. Mark dependent cases blocked if a facility is missing.

## Exit criteria

All 20 cases must pass on the final candidate, with evidence for every WEB requirement and no unresolved acceptance defect. T20 must meet both first-page database limits and the eight-second maximum-batch condition with journaling enabled. Index validity and build measurements must be recorded before production scheduling.

Any failed, blocked, or unrun required case leaves the corresponding exit criterion unmet. A request to reduce scope requires an explicit product and engineering decision and an updated specification; reporting a cycle complete does not waive acceptance.

Browser coverage is desktop-only for this release, including 1,280 px and 1,600 px widths, long category labels, and the All school filter. Mobile layout, provider accuracy, and production-only workload effects remain outside this cycle.

## Reporting and follow-up

For each case, retain build, environment, fixture revision, observed outcome, and evidence locator. Record failed expectations as Bug reports and link the affected requirement. Keep raw logs and captures as evidence rather than authoring another execution-log document.

Use a [status report](test_status_report.md) while the cycle is active and a [completion report](test_completion_report.md) at the milestone. Keep results from different builds separate. A final candidate must rerun all 20 cases; prior passes do not automatically transfer to a changed shared predicate.

Clean up isolated rows and credentials after testing. Preserve evidence and report any cleanup failure before reusing the environment.
