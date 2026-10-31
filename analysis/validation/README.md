# Validation evidence index

The final follow-up evidence uses the `final_` prefix. Files without that prefix record the first delivery or intermediate audits and retain their historical counts and criteria.

- [Final evaluation summary](final_evaluation_summary.json): phase counts, observed failures, repairs and acceptance boundaries.
- [Final outputs and grades](final_evaluation_outputs.jsonl): sanitized actual generated answers, original grades and retests.
- [Run registry](final_run_registry.json): model, timestamps, hashes, usage and infrastructure status.
- [Authored-example audits](final_example_audits.json): separate model reviews of the 24 teaching documents.
- [Package checks](final_package_checks.json): static integrity, 28 unit tests, wording/preservation regressions and offline commands.
- [Sizes](final_sizes.json) and [resource traces](final_resource_traces.json): selective-loading evidence and measurement limits.
- [Diagram checks](final_diagram_checks.json): actual Mermaid renders and visual review.
- [Source manifest](example_source_manifest.json) and [source checks](final_source_checks.json): selected project inputs, authorized teaching additions and unchanged source documents.

The teaching reports under the skill's examples directory are authored examples. Actual skill-validation results live here. Raw CLI events, temporary workspaces and unrelated source attachments remain outside the committed deliverables.

[Committed-tree checks](final_committed_tree.json) and the [GitHub delivery receipt](final_delivery.json) record the validated content commit and verified package tree.
