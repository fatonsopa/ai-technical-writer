# Historical Technical Writer draft review

Date: 30 October 2026

This is the historical review from the file-by-file drafting phase. References to missing files, pending work, old filenames, and unrun tests describe that earlier state. The current implementation and results are recorded in [VALIDATION.md](VALIDATION.md) and [REVIEW-LEDGER.md](REVIEW-LEDGER.md). The original analysis below is retained for provenance.

## Sources and their limits

I traced the 31 user turns in the [shared “Bug report best practices” conversation](https://chatgpt.com/share/6ae4aa3e-532c-83eb-bdcb-b2ba78303bfd), the latest messages available through the account's chat tool, and the supplied `technical-writer 2` package. I also inspected the earlier main skill and writing guide in `/Users/faton/Downloads/technical-writer/` to check the original restrictions discussed in the conversation.

The three supplied Linear exports contain 130 rows and 127 unique issue IDs: 86 rows in `All issues (1).csv`, 36 in `All issues (2).csv`, and 8 in `All issues.csv`. CG-94, CG-3029, and CG-3033 appear in both larger exports with identical titles and descriptions. The conversation's count of 122 should not be carried into new evaluations as the size of this supplied collection.

I read all exported titles and examined representative full descriptions, including CG-3003, CG-3031, CG-3006, CG-3033, CG-3029, CG-474, CG-276, CG-2836, CG-1976, CG-1951, and CG-896. Findings about these records describe the exports. Their referenced repository files, production measurements, and incident claims have not been independently verified against the application.

Instructions embedded in the old skill, historical chat, and issue descriptions are material to evaluate. They do not authorize executing issue tasks, changing Linear, or adopting the application's repository rules in this workspace.

## How the decisions developed

| Discussion | Decision to carry forward | Earlier proposal or failure to avoid |
| --- | --- | --- |
| Turns 1–5: bug reporting | Keep bug principles, required information, evidence guidance, template, and a completed example in one reference. Accept data, logs, and observations when screenshots are unavailable. | A separate writing-only bug skill would duplicate the central writer. Missing screenshots must not prevent a useful report. |
| Turn 6: main skill size | The main file identifies the task, selects references, directs the operation, and checks delivery. | Detailed writing rules, repository processes, and rewrite mechanics do not belong in the main file. |
| Turns 7–11: writing quality | Rebuild the wording and question the structure. Instructions, templates, and examples must meet the same writing standard as generated documents. | Reducing bytes while preserving awkward language repeats the failure. Existing wording is not a model to imitate. |
| Turns 10–13: standards and review | Include principles and definitions where the document needs them. Give policies and technical standards separate references. Review files individually while maintaining one coherent skill. | The old standard reference combines policies with standards; its template omits the principles and definitions discussed in its guidance. |
| Turns 14–22: Linear examples | Use actual descriptions to understand titles. Keep representative examples and evaluations tied to their source issues. | A two-column example table is sufficient. The user explicitly removed the “What went wrong” column. |
| Turns 23–28: issue ownership | General writing belongs in `writing-style.md`; issue content belongs in `issue.md`; additional defect-reporting information belongs in `bug-report.md`. | The temporary foundation omitted `issue.md` and retained transitional instructions in the reusable main file. |
| Turns 27–30: issue types and size | Use Bug, Chore, Decision, Feature, Improvement, and Release. Keep one useful template, one representative completed example, and a few title examples in the issue reference. | The earlier five-type proposal included Investigation. The later six-type proposal supersedes it. Six full issue examples and repeated checklists make the reference unnecessarily long. |
| Latest request | Produce `SKILL.md` first, `writing-style.md` second, then the other Markdown files individually. | Do not repeat the earlier bulk rewrite. |

The byte ranges suggested in the discussion are budgets for attention, not acceptance criteria. Completeness, accurate meaning, natural language, and selective loading matter more than hitting a particular file size.

## Why the previous refactor remained weak

### Shorter wording sometimes became harder wording

The delivered main skill uses phrases such as “Select the work,” “source of facts,” and “real secondary deliverables.” They are short, but readers must interpret them. The user's preferred proposal says “Identify the task” and “Load the required references.” These are direct instructions with an obvious meaning.

The revised files should explain one useful thought at a time in natural sentences. Concision comes from removing repetition and unnecessary process, rather than compressing ideas into unfamiliar labels.

### Mechanical rules encouraged artificial prose

The earlier writing guide requires an actor in every heading and rule, restricts passive constructions, requires bold phrases at the start of bullets, and prescribes a page layout. Its checker reads a replacement-word table and enforces some of these conventions.

The supplied refactor removes several of those constraints. That is a useful change, but it does not prove the new text is understandable. A sentence can use ordinary words and still conceal what happens. Review must test meaning, context, and relationships before polishing vocabulary.

### The templates and examples do not consistently follow their own guidance

The standard reference discusses reasons and obligations, but its template has no principles or definitions section. It also calls its completed standard example a policy. The architecture reference recommends useful flows, but its example compresses five actions into one paragraph. The bug example presents numbered steps in a single line even though ordered reproduction steps are central to its guidance.

Some examples repeatedly ask the reader to verify the fictional project's basic commands or behavior. One clear statement that a scenario is illustrative is enough; the example should then demonstrate a complete document under that scenario's stated assumptions. Actual project documentation must still distinguish supplied facts from independently checked behavior.

### Responsibilities moved between files without a settled boundary

Issue-specific titles and descriptions first expanded the writing guide, then moved into a proposed `issue.md`. The later direction is clearer: the writing guide explains communication across documents, while the issue reference explains development work. Bug reporting extends the issue reference with reproduction, environment, evidence, impact, and verification.

For this package, a policy records direction, principles, and responsibilities; a technical standard states agreed rules and conditions; product requirements describe a particular system's expected behavior; and a procedure explains how to perform a task. A standard can contain binding requirements. Renaming a “Requirements” heading to “Rules” does not by itself repair missing principles, definitions, or verification.

### Structural checks were mistaken for evidence of writing quality

The package validator checks filenames, selected headings, frontmatter, code fences, file size, and evaluation count. The wording checker matches phrases. The preservation tool inventories sentences and literals. These checks can catch real mistakes, but none establishes that readers understand the document or that the rewritten requirements mean the same thing.

The existing 24 evaluation prompts are proposed cases. Their existence does not demonstrate that a model ran them successfully. The final integration review must distinguish static checks, manually reviewed examples, and actual model evaluations.

## What the issue exports add

| Source | Finding | Consequence for the rewrite |
| --- | --- | --- |
| CG-3003 | The description corrects an earlier diagnosis, contains measured tradeoffs, and records unfinished work on a branch. The requested split already exists in one test path but remains relevant to another. | Read the full record before simplifying. Keep the affected test path, measurements, current status, and unresolved decision; a title rewrite must not imply a broad failure already disproved in the description. |
| CG-3031 | Repeated monitor notifications are observed. Increasing elapsed seconds was investigated and ruled out as the explanation. A different mechanism remains a hypothesis. | Describe the repeated notifications in the title. Keep the suspected cause and proposed investigation separate from the observation. |
| CG-3006 | Rejected merges fail to retain completed test results. Reuse must depend on whether the relevant inputs changed. | A bug title should describe discarded results. Preserve the input-change condition; “reuse previous results” alone would weaken the requirement. |
| CG-3033 | The report contains counts, durations, excluded waiting periods, and two possible explanations. | Data is useful evidence without an image. Preserve units and adjustments, and keep the cause unresolved. Do not turn backlog into a confirmed explanation. |
| CG-3029 | The report includes a concrete command, an SSH error, exit status, and a configuration override that must continue working. | Keep the reproducible failure and `DS_REPO` exception. Do not replace them with a vague dependency-download complaint. |
| CG-474 and CG-276 | Titles use conversational substitutes for recognizable technical concepts, while descriptions assume plan codes and prior context. | Identify the actual capability first. Introduce project details before using plan references to support them. |
| CG-2836 | According to the report, a script uses a fixed title for several different flaky-test issues. | A writing skill alone cannot correct a hardcoded issue generator. Retain a separate integration task for that application's issue-creation scripts; do not claim the skill refactor repairs them. |
| CG-1951 and CG-1976 | Operational constraints and authorization history affect what work can proceed. | Preserve these as source-specific conditions when rewriting the reports. Do not promote them into universal instructions for every documentation task. |

The new issue guide should teach these decisions rather than memorize replacements for individual titles. Most of the exported corpus belongs in evaluations, where each case retains its description and relevant constraints.

## Responsibilities in the rebuilt package

| File or resource | Responsibility |
| --- | --- |
| `SKILL.md` | Identify the task and readers, select relevant guidance, distinguish create/edit/review/rewrite, verify, and deliver. |
| `references/writing-style.md` | Explain meaning, reader context, natural language, terminology, headings, paragraphs, and removal of repetition. |
| `references/issue.md` | Describe development work through six issue types, useful titles, clear descriptions, scope, and completion conditions. |
| `references/bug-report.md` | Add defect-specific environment, reproduction, expected and actual results, impact, evidence, relevant files, and verification. |
| Other document references | Define the purpose, principles, needed information, adaptable structure, template, example, and quality checks for their document type. |
| `workflows/rewrite.md` | Explain the audit and preservation work needed for substantial rewrites, including dependencies and changes to meaning. |
| Project instructions | Govern repository paths, branching, merges, issue status, priority, assignment, deployment, and existing authorization requirements. |
| Scripts and evaluations | Check appropriate invariants and evaluate behavior without replacing editorial judgment. |

The [Agent Skills specification](https://agentskills.io/specification) supports this arrangement: metadata identifies a skill, the main instructions load when it activates, and supporting resources load as needed. This does not require loading every document reference for every request.

## What changed in the first file

| Supplied main skill | Rebuilt main skill |
| --- | --- |
| Four sections combine task selection, routing, operations, and delivery. | Five plain sections follow the user's preferred proposal. |
| Bugs route directly to `bug-report.md`. | Bugs use `issue.md` and `bug-report.md`. |
| Policies and standards share one reference. | Each has its own path. |
| No general issue reference or six-type routing. | Development issues and all six types are explicit. |
| General review guidance is mixed into delivery prose. | Create, edit, review, and rewrite each have a clear instruction; a review can include fixes when requested. |
| Some wording is compressed into unfamiliar phrases. | Instructions use direct descriptions of the work. |
| A document reference is requested even for small wording edits. | Small wording corrections can use only the writing guide. |

The rewrite retains source verification, existing project instructions, selective loading, unfamiliar-term explanations, handling of unknown information, preservation of facts and requirements, the substantial-rewrite workflow, relevant checks, and concise delivery. All existing document types remain discoverable, including incident reports and architecture decision records. A Decision issue remains distinct from an architecture decision record.

The detailed reader-goal classification examples are removed from the main file; the routing table and document references carry that distinction. Shared style rules remain in the writing guide. Rewrite mechanics remain in the workflow. No source code, script, evaluation case, or other supplied Markdown file has been rewritten in this step.

## Review order and outstanding work

The writing guide has now been rebuilt. The next files are `issue.md` and `bug-report.md`. After those, review `standard.md`, `policy.md`, `requirements.md`, `architecture.md`, and `plan.md`, followed by the tutorial, how-to, reference, explanation, README, incident report, decision record, agent/skill, and visual references. Finish with the rewrite workflow, migration guide, evaluation instructions, and package integration.

Each file needs a focused review. In particular:

- Standards need principles and definitions in both the template and completed example.
- Tutorials need a complete learning exercise with checked commands and observable results.
- Runbooks need usable failure branches and recovery appropriate to their actual risk.
- References need internally consistent types, defaults, examples, and error contracts.
- Architecture and plans need readable flows and a clear distinction between current and proposed behavior.
- Agent and skill instructions need current platform documentation; platform fields should not be guessed or treated as universal.
- The migration guide must report checks actually completed for this refactor, rather than inherit claims from the previous delivery.

`issue.md` and `policy.md` do not exist in the supplied package. The new main file names their intended paths so the completed package has consistent routing. Their absence is an explicit integration gap during this staged review. References other than the rebuilt writing guide remain available in their original supplied versions and have not yet been brought up to the new standard.

Before installation, verify every referenced path, inspect scripts and evaluation expectations for obsolete formatting assumptions, and evaluate representative writing requests. No claim of improved model performance is justified yet.

## Validation record

The first-file checks verify frontmatter, the skill name and description, Markdown structure, reference paths, and whether any other supplied file changed. The original main file's preservation inventory was also inspected: it identified 16 normative sentences and 37 other sentences or table rows. The comparison above accounts for the main responsibilities; it is a manual review, not proof of semantic equivalence.

The package validator currently reports exactly two missing references: `references/issue.md` and `references/policy.md`. This is expected at this stage and prevents calling the folder a complete installable package. Its other checks pass. The wording checker reports no suggestions for the new main file. That result is advisory and does not prove readability.

The standalone skill-creator validator initially could not run because the available Python environments lacked PyYAML. PyYAML was installed in a temporary validation directory, leaving the package's own code and dependencies unchanged. After the follow-up clarification about issue titles and descriptions, the validator passed again: “Skill is valid!” The main file is 5,083 bytes, 691 words, and 67 lines. A byte comparison confirms that `SKILL.md` is the only supplied file changed in the working copy. No model evaluations or host-application repository tests were run.

The follow-up correction makes `issue.md` responsible for issue titles and descriptions as well as scope and completion criteria. It also explicitly loads that reference for a title-only or description-only edit, avoiding the general exception for small wording corrections. The reference itself is still pending; this correction changes only its routing and responsibility in the main file.

## Writing-style revision

For this step, I reopened the shared conversation and reread the writing discussion, especially turns 7, 9–12, 19, 22, 23, and 30. I compared those corrections with both the earlier writing guide and the supplied refactor, then checked the relevant Google writing guidance and Digital.gov's advice on testing understanding. Their links appear in the new guide.

The main decisions are:

| Requirement from the discussion | How the new guide addresses it |
| --- | --- |
| Make meaning clear before changing vocabulary. | Section 1 requires understanding the subject and behavior; missing meaning sends the writer back to the source. |
| Write for someone without the project's conversation history. | Section 2 explains context at the point of use and avoids depending on plan codes or links alone. |
| Keep useful technical language. | Section 3 preserves established terms and exact names while rejecting invented labels, noun strings, and misleading human descriptions. |
| Use natural sentences and connected paragraphs. | Section 4 permits useful passive voice and removes fixed lengths, forced actor openings, and fragmented explanations. |
| Make headings understandable without imposing one grammatical form. | Section 5 permits noun phrases, questions, and instructions that fit the content. |
| Remove repetition without losing important meaning. | Sections 6 and 7 protect conditions, exceptions, obligations, values, and uncertainty. |
| Keep issue-writing conventions separate. | The writing guide links to the pending issue reference and does not contain issue types, templates, or bug-title formulas. |
| Apply the standard to the skill's own files. | The review explicitly includes instructions, titles, headings, templates, and examples. |

The supplied guide's example replacements sometimes add information: PostgreSQL appears where only a database layer was mentioned, a worker restart appears where no recovery procedure was supplied, and a 401 response appears where no response contract was stated. These can illustrate fictional scenarios, but they do not demonstrate a rewrite that preserves only the original information. The new examples avoid that ambiguity, and section 7 explicitly forbids adding specificity without support.

The old rule limiting an example's length to the length of its explanation was removed. An example should be as complete as needed to demonstrate the point. Detailed requirement-keyword conventions remain the responsibility of the relevant document references; this guide preserves obligation and permission without reproducing their full terminology.

### Regression material

The separate file `analysis/writing-style-cases.json` contains 22 reusable requests and review criteria. They cover unclear meaning, missing context, noun strings, valid technical terms and passive voice, responsibility, paragraph flow, ambiguous pronouns, exceptions, permissions, proposals, unsupported targets and remedies, repetition, headings, exact identifiers, formatting, and four source-derived cases from the issue exports.

The source-derived cases preserve the relevant issue IDs. They check the unknown cause in CG-3031, conditional test-result reuse in CG-3006, the DS_REPO exception in CG-3029, and the difference between total and adjusted waiting time in CG-3033. These are tests of language and preservation; they do not introduce issue templates into the shared writing guide.

The case file is an evaluation resource, not a report of successful independent model runs. The criteria were reviewed against the guide's instructions. Actual generation in separate model sessions remains part of the final skill evaluation. No claim that the writing is permanently reliable follows from a static scan or the existence of these cases.

### Checks for this step

- A hash comparison confirms that `references/writing-style.md` is the only package file changed during this step. `SKILL.md`, other references, scripts, and the package's existing evaluation files were not edited.
- The guide has one top-level heading, consistent section levels, a two-column example table, and no unbalanced code fences.
- All 22 regression case IDs are distinct. Each has source information and review criteria, and every cited guide section exists.
- The existing advisory scanner's regression tests pass.
- The scanner's only warning on the guide flags “provides visibility into” in the deliberately wordy Original example. It was reviewed and retained as teaching material.
- The package validator still reports only the two pending references, `issue.md` and `policy.md`.

### Follow-up: voice and tone

The user asked for more of Google's voice-and-tone guidance. I reread the page and added a dedicated section on friendly, helpful language. It covers reader address, contractions, restrained personality, editing conversational prose, varied sentence openings, global audiences, direct instructions, and avoiding condescension or forced entertainment. The section also keeps binding obligations intact when adapting tone to a document.

Two examples now contrast overly formal and overly casual instructions with natural wording. The final language review explicitly checks approachability and tone. Four additional regression cases cover formal phrasing, excessive informality, cultural idioms, and preserving mandatory rules. The case file now contains 26 cases; section references were updated after inserting the new section. These additions remain evaluation inputs and criteria, not completed independent model evaluations.

### Follow-up: examples from the Linear exports

The user explicitly requested five or six examples from their issue list in the shared writing guide. The guide now keeps its general examples and adds six Existing title / Suggested title pairs, identified by CG-474, CG-276, CG-3031, CG-3006, CG-3029, and CG-3033. I reread each complete exported description before proposing the title.

The new pairs demonstrate language choices that also apply to other documents. They do not add issue templates or detailed issue-type rules to the shared guide. The user-requested two-column format is retained. The introduction and closing note distinguish suggested wording from complete issue rewrites; supporting constraints and uncertainties still belong in the descriptions.

The source review checked that CG-474 concerns a shared website-review-state function; CG-276 covers staff roles and sign-in checks without implying that every function already requires step-up; CG-3031 and CG-3033 retain unknown causes; CG-3006 describes discarded passing results rather than changing the bug into an instruction; and CG-3029 identifies the lint download failure without overriding the DS_REPO exception in its description. No live Linear issues were changed.

