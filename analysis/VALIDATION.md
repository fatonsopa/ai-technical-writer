# Technical Writer validation

The follow-up delivers 25 audited references and 24 complete, connected Websites Review examples. The current corpus contains 188 cases: 167 development requests, 11 acceptance requests and 10 grader controls. The final assessed set passes after targeted guidance repairs and correction of a grader error. Original failures and every retained attempt remain available.

## Observed writing results

| Stage | Actual result | Meaning |
| --- | --- | --- |
| Bug-structure checks | 11/11 passed | Complete bug sections, distinct results, relevant files and scoped review behavior |
| Second reference audit suite | 159/159 passed | Full supported-output suite plus style, routing and evidence checks before the connected examples |
| Matched task comparison | Baseline 0/2; revision 2/2 | Same Bug/Feature create requests under the stronger structure contracts; a selected comparison, not a general improvement rate |
| Connected-example suite, first grading | 162/167 passed | Two real writing failures and three false-positive style judgments |
| Decision and Standard retests | 4/4 each passed | All four operations retested for the two affected guides |
| Saved style outputs regraded | 26/26 passed | Explicit requested prose/title format took precedence over generic review defaults |
| Final assessed development set | 167/167 passed | Original suite combined with the targeted retests and corrected style grades |
| Acceptance | 11/11 passed | Eight earlier requests rerun as regressions, plus three fresh structure/destination cases |
| Substantial documents | 8/8 passed | PRD, plan, SDD, HLD, LLD, TP, TS and TCR on a different import-preview initiative |
| Authored example audits | 24/24 usable | Separate model reviews, followed by refinements and targeted checks |
| Grader controls | 10/10 agreed with labels | Author-assigned controls, including deliberately flawed outputs; no independent human calibration |

The 128 core cases cover 32 output kinds across create, edit, review and rewrite. The remaining development cases include 26 language regressions, five routing/evidence regressions and eight substantial-document requests. Across the complete final assessed set, there are 39 create, 33 edit, 37 review and 58 rewrite requests.

The full 167-case suite was not freshly rerun against one final frozen snapshot after every repair. Four-operation retests cover the affected Decision and Standard guidance; saved language outputs were regraded without regeneration. Runtime hashes identify revisions during the run. The substantial requests loaded their matching full examples according to successful command traces and used different source facts. No Websites Review limits or results were accepted as facts about the import initiative.

## Failures and corrections

The Decision excerpt retained an obsolete instruction to draft a Feature comment despite the current Decision destination. The Issue guide now resolves stale author directions using the current request while preserving a narrow edit.

The Standard rewrite left every verification method unspecified. The guide now permits concrete proposed checks derived from existing rules while keeping tooling, approval and execution unknown. A proposed check is not an invented pass or a new product obligation.

Three style cases explicitly requested prose or a title, but the first grader required review findings. Source inspection showed that the answers met the original expected properties. The grader now honors explicit output format. A duplicate regrade that began before the patch also passed all 26 answers, demonstrating judge variance; the later result is not proof that wording alone caused a score improvement. Both attempts and the original judgments are retained. Controls were checked again after the actual correction.

The separate example audit prompted concrete fixes: an unverified condition in the story, T13 for deleted-row protection, explicit LLD normalization/defaults, reproducible bug fixtures, decision authority/links, TS setup and measurement conditions, and the README's runnable start. Mermaid rendering caught semicolon-sensitive syntax; visual inspection prompted a shorter participant label.

See the [phase summary](validation/final_evaluation_summary.json), [actual answers and grades](validation/final_evaluation_outputs.jsonl), [run registry](validation/final_run_registry.json), [example audits](validation/final_example_audits.json), and [reference-by-reference audit](REFERENCE-AUDIT-2026-10-31.md).

## Package, examples and size

Static checks verify canonical names, routing, local links, fences, external example presence, required fields in templates and completed artifacts, SDD acceptance mapping, shared test-case meanings, and operation coverage. All 28 unit tests pass, including negative cases for removed files, stale labels, lost bug sections, missing acceptance criteria, broken examples and requirement drift. Wording regressions and nine preservation groups pass. The system skill validator also accepts the package.

The tutorial's two Python commands and README's first command were executed against the supplied nine-row JSON fixture in an empty temporary directory. Displayed IDs and 6/4/3 totals matched. This check does not execute the UI how-to, SQL, or source application.

Three Mermaid diagrams were rendered to SVG and PNG with Mermaid 12.2.0 and headless Chrome. Their accessible titles/descriptions were checked and their PNGs visually inspected. Other host renderers were not activated.

References retain compact principles, structures, templates and checks. Full examples are separate and loaded by relevant filename for complete creation/substantial rewriting. Narrow edits and located reviews need not load them. All files are within the chosen role budgets; these are advisory maintenance limits, not output word targets. [Per-file sizes](validation/final_sizes.json) use UTF-8 bytes and characters/4 estimates. [Resource traces](validation/final_resource_traces.json) record named resources and actual reported reads; command mentions do not prove every byte entered context. Host token usage is recorded separately in the run registry.

The selected six project documents retain their original hashes. Teaching additions and source status are tracked in the [internal manifest](validation/example_source_manifest.json); the examples read as complete documents, as requested. Source reports, teaching reports and actual skill-evaluation results have separate roles.

## Boundaries and delivery

Generation used authenticated Codex CLI sessions pinned to gpt-6.1-sol with read-only workspaces and separate grading contexts. Expected properties/rubrics were withheld from generators. Four operations share a context per output kind; these are not 167 mutually independent sessions. No seed or temperature was pinned. Same-model grading and author controls do not establish independent human acceptance or future reliability.

No source-application commands, database queries, migrations, tracker writes, deployments or host-skill activation were performed. The source project remains read-only. The authored example test reports are not evidence of application testing.

The first delivery and its older counts remain in the unprefixed validation artifacts. They did not catch the later user-reported structural losses and are not final compliance evidence. Current artifacts use the final_ prefix. GitHub delivery is verified through committed-tree checks and the final delivery receipt; the remote branch must match the delivered commit.

The clean export of content commit a896aa4 passed all seven committed-tree checks. It was pushed to main and fetched again; remote and local commits matched, as did the validated skill tree. The [delivery receipt](validation/final_delivery.json) records that checkpoint. The following evidence-only commit adds the receipt and exported-tree checks while preserving the package tree, and its remote HEAD is verified before the final response.
