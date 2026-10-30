# Technical Writer validation

The refactor covers all 25 references and 32 supported output kinds. The 128-case development suite passed after targeted repairs, with 32 accepted results for each operation: create, edit, review, and rewrite. The 26 style regressions passed. Final acceptance coverage passed eight cases, including a fresh replacement for one failed case used during repair. These are sampled model results, not a guarantee of future behavior.

## What was evaluated

The accepted [specification](SKILL-SPEC.md) defines TW-001–TW-034. [Coverage](../technical-writer/evals/coverage.json) maps each requirement to files, checks, and cases. The [review ledger](REVIEW-LEDGER.md) records reference-level findings and revisions; [research choices](RESEARCH.md) distinguish external guidance from the user's conventions.

Generation and grading used the authenticated Codex CLI, pinned to `gpt-6.1-sol`, with user configuration ignored, ephemeral sessions, and a read-only sandbox. The CLI metadata reported reasoning effort `none`. No seed or temperature was pinned. Expected properties and rubrics were excluded from generator workspaces. One fresh context handled each output kind; its four operations shared that context. Six matched create requests and the title comparison used one operation per context for both baseline and revision. The baseline is the preserved execution draft in commit `3a65c56`, not an untouched original from the earliest conversation.

The grader used a separate context with source fixtures, target guides, actual resource availability, and tool evidence. It scored seven dimensions from 0–3; each needed at least 2, with no critical failure. Required governance sections and the known SDD naming confusion also have deterministic gates. The same model family generated and graded outputs, so correlated blind spots remain possible. Author source review resolved flagged results; no independent human acceptance or calibration is claimed.

## Results

| Check | Result | Interpretation |
| --- | --- | --- |
| Core development suite | Initial 127/128; 128/128 after targeted repairs | One unsupported backlink-check claim failed. An unrelated TS false failure was corrected in grading context, without changing its output. |
| Mixed SQL/timing evidence | 1/1 | Two snapshots and all five measured durations retained without invented comparisons or execution. |
| Style regressions | 26/26 | Preserved inputs/context/criteria from the conversation-derived cases. |
| Original protected acceptance | 7/8 | A bug review expanded into a full replacement report. |
| Final acceptance | 8/8 | Seven untouched cases plus a fresh incident-review case. The failed bug review remains a development regression. |
| Review repair checks | 5/5 | Bug, issue, README, standard, and the observed failure; findings remained within review scope. |
| HLD rewrite retest | 1/1 | Actual content search supports the narrower validation statement. |
| Final canonical-name retests | 2/2 | Acronym/lifecycle routing and title-only edit after correcting Issue headings and labels. |
| Acronym/lifecycle exercise | 1/1 grouped exercise | Twenty acronym/full-name pairs, four aliases, and four lifecycle scenarios. This does not measure automatic host activation. |
| Matched create comparison | Baseline 4/6; revision 6/6 | Baseline policy lacked named sections; baseline SDD was mislabeled a Software Design Document. |
| Matched title comparison | Both accepted | Same title; revision loaded two references instead of three. |
| Predeclared risk repetitions | 4/4 additional trials | Two more TCR-create and two more standard-rewrite trials; all retained. A small variability check, not a reliability estimate. |
| Grader controls | 10/10 author labels matched | Good/flawed controls, real local checks, invented product tests, and documented workflow descriptions. |

After shared guidance repairs, affected development cases were rerun. The final 128-case count combines the initial suite with those targeted retests; it is not a claim that all 128 outputs were independently regenerated after the last edit. Final acceptance and focused risk trials assess the repaired behavior.

The baseline SDD originally received passing model scores despite the wrong document identity. The explicit title gate was added after author review, based on the user's already accepted convention, and applied without variant-specific rules. Baseline policy substance was preserved but still failed its mandatory section structure. The comparison is small and deliberately includes areas changed by this refactor; it does not estimate overall production improvement.

## Failures and repairs

The HLD rewrite's inventory claim was supported by tool evidence, but its claim that no other documents linked to the draft was not. The rewrite workflow now distinguishes inventory, content searches, mapping checks, and product tests. Its retest performed a content search and passed.

The first bug-review acceptance output was factually careful but supplied a full replacement. The main operation guidance and bug quality check now require located findings and targeted corrections for a review. The failed holdout was moved to observed regressions; a fresh incident-review request passed without another full rewrite.

Grading also failed in ways the documents did not. The early grader lacked tool evidence, confused target guides with baseline resources, and listed only Markdown when checking available scripts. Corrected those inputs, added controls, and regraded affected outputs. The TS output's description of a mapping command was supported by the guide; it did not claim execution. Superseded judgments and infrastructure attempts remain identifiable in the artifacts.

A usage-limit interruption stopped some grading calls after generation had completed. Saved outputs were reused after access resumed. Infrastructure errors were not counted as document failures or silently replaced with author-written results.

## Size and context

Runtime Markdown grew from 97,466 to 130,504 bytes as references grew from 17 to 25. The entry point grew from 5,083 to 9,996 bytes to include the requested full-name/acronym catalog, create/update triggers, diagram, and supporting relationships. This refactor expanded supported coverage; it did not reduce every context path.

Role budgets are review thresholds: 11 KiB for the entry point, 14 KiB for the shared writing guide, and 8 KiB for other guides. SDD is 8,257 bytes, 65 bytes over its soft budget. It combines behavioral and individual-requirement guidance; the retained content and selective loading justify the exception. No prose was compressed into shorthand to clear the warning.

In the matched title-only exercise, unique runtime Markdown named in successful read commands fell from 33,880 to 29,323 bytes, about 13.5%. The baseline read writing style, issue, and bug-report guidance; the revision read writing style and issue. Character-based token estimates fell from 8,439 to 7,303. Other paths grew, particularly those that gained a dedicated guide; the [context data](validation/context.json) reports all six create comparisons as well as the title comparison. These figures exclude source files, system prompts, wrappers, repeated reads, and other host overhead. Actual host usage is recorded separately.

[Size data](validation/sizes.json) includes per-file bytes, words, hashes, and estimates. Tokens are estimated as Unicode characters divided by four, not measured by the model tokenizer. The original supplied entry point was measured separately and must not be confused with the execution baseline.

## Package and example verification

The package validator checks links, reachable references, canonical paths, fences, governance content, requirement mapping, case integrity, operation coverage, and role budgets. Its negative tests exercise missing files, broken nested links, retired paths, empty substantive sections, missing operation coverage, and nested fences. Two added negative cases reject a stale issue link label and a mismatched issue-guide title. Runner tests cover hidden grading inputs, missing IDs, critical gates, actual resource/tool context, acceptance governance checks, SDD identity, and calibration agreement. Exact command results are saved in [script checks](validation/script_checks.json).

The wording checker regression passed; its suggestions are advisory. All nine preservation-script regression groups passed. Tutorial, how-to, and README commands passed in temporary fictional-project fixtures, including backup, isolated edits, unchanged unrelated data, success, and recovery checks. The system skill validator accepted the package.

The writing-guide preservation review accounted for all 149 inventoried sentences/rows and 38 literals, with no gaps. Its relative issue link was explicitly mapped from `references/issue.md` to `issue.md`. The six Linear originals and all 26 style inputs/contexts/criteria were independently compared with their supplied sources. This mechanical result supports, but cannot prove, semantic preservation. Other reference rewrites were audited against their source responsibilities and the accepted specification; no whole-library semantic-equivalence proof is claimed.

Three Mermaid diagrams passed syntax checks; an invalid control was rejected. All three rendered through Mermaid CLI and local Chrome and were visually inspected for legible labels, connections, clipping, and overlap. [Rendered artifacts](validation/diagrams/) preserve that check. Other host renderers and narrow-screen layouts remain untested.

## Reproduce and inspect

See [evaluation instructions](../technical-writer/evals/README.md). The committed [outputs](validation/evaluation_outputs.jsonl) contain generated text, grades, case/source hashes, recorded skill hashes, and reference traces. [Summary](validation/evaluation_summary.json) and [run registry](validation/run_registry.json) retain outcomes and infrastructure attempts. Raw CLI logs, account data, transient workspaces, original conversations, and raw CSV exports stay outside the repository.

Initial core records used a legacy hash that included MIGRATION.md. Reconstructing the tested runtime plus the baseline migration file reproduced that hash exactly. The normalized runtime hash excludes MIGRATION.md; both are recorded. [Core-to-final diff](validation/core_to_final.json) preserves the instruction changes after that run. Later runs record their own runtime hashes.

The work did not install this skill, activate it in Claude Code, test a real application's integrations, run production queries, or establish independent human acceptance. The approved delivery is this skill package and its evidence. Remote delivery is recorded separately in delivery.json after the push is verified.
