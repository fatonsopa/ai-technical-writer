# Lessons for a future skill-building skill

The user requested this record on 2026-10-30 while the Technical Writer refactor was in progress. It informs a future task; it does not expand this task into building or installing another skill. Recheck current official OpenAI, Anthropic/Claude Code, and Agent Skills documentation when that work begins. Record the checked version/date and distinguish portable conventions from vendor-specific features.

## Decisions to carry forward

These are accepted design decisions, not claims of proven performance. Add evidence and limitations as the current evaluations run.

| Decision | Problem it addresses | What a future skill builder should do |
| --- | --- | --- |
| Define behavior and acceptance before implementation. | A polished-looking package can miss the user's actual requirements. | Keep a specification and trace its requirements to instructions, resources, and observable checks. |
| Keep a focused entry point and load specialized guidance selectively. | Large skills spend context on unrelated document types and rules. | Put shared purpose/routing in SKILL.md; keep conditional detail in clearly owned references. Measure actual loaded context as well as file sizes. |
| Give each writing format a clear owner. | User Story guidance was incorrectly assigned to work_item.md because stories can appear in tasks. | Separate the reference that teaches a format from the place its output is stored. Use stable names, full-name filenames, accepted aliases, and explicit composition. |
| Select useful capabilities rather than copying a standards catalog. | The testing discussion included execution logs as if another authored document were needed. | Treat existing logs as evidence. Add a reference, script, or artifact only for a concrete supported task. |
| Test generated behavior as well as package structure. | Heading checks and example files alone cannot establish output quality. | Supply realistic fixtures, explicit rubrics, a coverage map, negative cases, protected acceptance cases, and actual recorded runs. Distinguish static tests, author review, independent model generation, and human review. |
| Evaluate the evaluator. | A fluent document can receive a high score while omitting an obligation or inventing a result. | Calibrate graders using good and deliberately flawed outputs, preserve critical-failure gates, and disclose whose labels are used. |
| Use scripts for repeatable or fragile checks. | Manual repetition is error-prone; unnecessary scripts also add maintenance. | Add executable helpers when they materially improve repeatability or reliability, and test their meaningful behavior. Do not require scripts merely to complete a directory checklist. |
| Inspect complete templates and examples. | Earlier governance templates mentioned principles in instructions but omitted them from the actual document. | Validate real section content and a complete example, including domain-specific requirements; do not accept keyword presence as proof. |
| Preserve meaning during simplification. | Shortening can silently remove conditions, exceptions, or obligation strength. | Inventory material constraints and exact literals; combine mechanical comparisons with semantic review. |
| Keep scope and authorization explicit. | Drafting a prompt was mistaken for permission to refactor; agreeing on a design was mistaken for no action at all. | Distinguish discussion, approved updates to the execution prompt, implementation authorization, and the final authorized delivery. Do not invent extra approval gates once the execution scope is approved. |

## Evidence log

- Preliminary baseline title exercise: a fresh Codex CLI run produced a clear title, but read the bug-report guide for a title-only request. This suggests a context-routing issue; it is one observation, not proof that the baseline fails generally. Preserve the final case/run ID and measured comparison when available.
- Reference-level outcomes, failed cases, repairs, final measurements, and remaining limitations will be linked here as they are observed. Do not promote an untested design preference into a universal rule.

## Future review questions

Which behaviors actually improved under the same model and fixtures? Which checks caught defects? Which supporting files were used, and which added no value? What broke across host products? Which instructions required project context or explicit user decisions? Which rules belong to this writing skill rather than to every skill?

The future skill should answer those questions using recorded evidence and current primary documentation. It should help choose appropriate evals, tests, scripts, references, and assets rather than requiring every possible resource for every skill.

- During execution the user clarified that the common six-type task guide should retain issue.md. User Story remains user_story.md. A semantically reasonable alias (Work Item) did not justify renaming an established user-facing reference without a real need. Reconcile later naming corrections everywhere.

- Evaluator failure observed: a grader seeing only final text falsely called an actually executed preservation inventory fabricated, and treated baseline-missing guides as available. Provide the judge with the actual permitted resource snapshot, relevant tool evidence, and harness path mappings. Keep the common target rubric separate from what the generator could access. A plausible grading explanation can itself be wrong.

- Observed rewrite failure: a valid inventory command did not support the separate claim that no documents linked to a draft. State evidence at the scope of the actual check. A focused instruction repair produced a passing retest with a real content search.
- Observed operation failure: a source-grounded bug review still failed by supplying a full rewritten report. Test the requested operation independently of factual correctness; templates should guide assessment without overriding scope. Preserve a failed acceptance case as regression and replenish acceptance coverage after repair.
- Infrastructure interruption: generation artifacts survived a usage-limit failure during grading. Separate saved generation from grading so a retry does not need to regenerate outputs or discard failed attempts. Record infrastructure errors separately from document quality.

## Observed final results

See VALIDATION.md and validation/evaluation_summary.json for denominators and limits. Core coverage reached 128 accepted cases after targeted repairs; 26 language cases and eight final acceptance cases passed. The six matched create requests passed 4/6 on the preserved execution baseline and 6/6 on the revision under final gates. This small, deliberately selected comparison does not establish a general improvement rate.

The matched title exercise produced the same title in both versions. Selective routing reduced unique runtime Markdown read from 33,880 to 29,323 bytes, about 13.5%, while the total library grew to support more formats. Measure relevant paths and quality together; total byte reduction is not the only useful outcome.

The package validator, 19 unit tests, nine preservation regression groups, wording regression, three executable example checks, and system skill validator passed. The shared writing guide's mapping accounted for 149 sentences/rows and 38 literals without gaps. Three diagrams were rendered and visually inspected. None of these checks substitutes for independent human acceptance or host activation.

The user's final file-layout concern reinforced another check: verify the actual tree and active callers, then record deletions explicitly in Git. A file named in a historical diff or migration record is not an active reference, but the distinction must be clear. The accepted final names are issue.md and user_story.md; reference.md and requirements.md are absent.

- A path can be correct while the visible link label still presents the wrong canonical document name. Audit names, labels, headings, catalog entries, and actual targets together. The final Issue label correction passed dedicated routing/title retests and two negative packaging tests.

- User review caught a structural loss despite passing model scores: a bug report combined expected/actual fields and hid relevant files under another heading. Content presence is insufficient when the user requires distinct sections or an exact heading. Inventory those contracts before rewriting, check the real template and example, and apply deterministic gates to complete generated outputs. Keep narrow-edit/review scope exceptions. Earlier scores do not retroactively prove compliance with the stronger check.

## Lessons from complete project examples

- Keep a guide compact and provide an actual complete artifact when a skeletal example cannot demonstrate the needed depth. Load the example conditionally; do not force every writing request to load the collection. Measure relevant context as well as total package bytes.
- One coherent initiative exposes cross-document defects that isolated examples hide. The second audit caught mismatched requirement meanings; the connected collection audit caught a missing unverified condition and a test link that omitted deleted-row coverage. Stable IDs help only when their meanings agree.
- Test substantial outputs on a different scenario. A model can imitate headings while copying example limits, approvals, roles or results. Our import-preview cases require edition isolation, expiry, atomic history, repeat confirmation and response-loss handling, with no Websites Review facts.
- Separate source provenance from the finished teaching artifact when the user requests natural examples. Explicit permission to invent example details does not authorize inventing evidence in normal documents. Keep that distinction in maintenance records and eval inputs.
- A narrow edit can preserve stale author directions while otherwise improving language. Evaluate current-request precedence and the finished destination, not just grammatical clarity or factual preservation.
- Unknown execution evidence is different from a proposed verification method. A usable standard can propose a check derived from its rule while keeping tools, approval and results unknown. Avoid both invented passes and empty verification columns.
- Render diagrams. A syntactically plausible sequence failed on semicolons in labels; visual inspection also exposed an overlong participant label. Neither a Markdown fence nor a model score validates rendering.

- Graders must honor explicit requested response format. Three style cases asked for prose/title output while their generic operation label said review. The first grader demanded findings despite the actual requests and predefined properties. Inspect the original request before treating a score as a writing failure; preserve the first judgment, correct the judge, regrade saved answers and recalibrate. This is not permission to relax a real document requirement.
