# SpecDev implementation tasks

<a id="spec-writer-implementation-tasks"></a>

The numbered checkboxes are the apply list for this change. Their links lead to the existing Tasks that own detailed acceptance and evidence. Local T numbers preserve earlier references. [Behavioral baseline](./specs/spec-driven-authoring/spec.md) · [Delivery approach and shared Definition of Done](./design.md#requirement-coverage)

Writer implementation starts after the accepted Skill Builder candidate and commit are available. W01 and W03 can then start in parallel. W60 retains its accepted evidence. W55–W57 and W51.3 remain proposals without execution rows. W46’s live rename requires accepted B5/T50.

Follow dependencies and stable Task IDs. W46 and W47 establish the installed runtime before W40 proves its native consumer. During authorized implementation, open the eligible Task and record each criterion’s verdict, candidate and evidence there. Mark its checkbox only after acceptance. Preserve failures and missing proof. Unproven criteria begin **Not demonstrated**. Ship the change with its affected guidance and direct consumer. A writing-only request ends at checked document delivery. [Read-only handoff test](../../../plan/test.md)

<a id="s01--edit-a-mixed-passage-without-corrupting-its-fixture"></a>

## 1. S01 · Edit a mixed passage without corrupting its fixture

Derive the fixture domain from its literal value and recognize the genuine document label. [Story criteria](./specs/spec-driven-authoring/spec.md#s01--edit-a-mixed-passage-without-corrupting-its-fixture)

- [x] 1.1 [W01](#w01--repair-the-websites-review-fixture-and-its-consumers) (T001). Repair the fixture and derive `__test_wrs-us.co.uk` from its literal. The cited consumers must select the same row. May start in parallel.

### W01 · Repair the Websites Review fixture and its consumers

#### Description

The worked example expanded the key US into a document name.

#### Expected outcome

An administrator can use the published fixture table and its dependent cases again.

Restore the key and all affected references within the worked example. Preserve legitimate document labels.

Example maintainer · R1/A1. [S01.1](./specs/spec-driven-authoring/spec.md#s01-1) and [F1.1](./specs/spec-driven-authoring/spec.md#f1-1). Use the audited fixture and its domain rule.

#### Acceptance criteria

- **W01.1** Read the corrected row and apply the documented lowercase rule. The emitted domain is `__test_wrs-us.co.uk`, and the cited tests select that same row. Save the row and derived domain. <a id="w01-1"></a>
- **W01.2** A genuine document reference in the example retains its agreed meaning. Compare the scoped diff and the consuming cases. <a id="w01-2"></a>

[examples/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/test_specification.md) · [references/writing_style.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md)

One fixture derivation and affected reference lookup suffice. No application deployment is involved.

#### Verdicts

Candidate: the W01 commit on `implementation/ship-specdev`. Reviewer: implementing agent, comparing the scoped diff and consuming cases with this Task and [S01.1](./specs/spec-driven-authoring/spec.md#s01-1).

- **W01.1 Met.** The fixture row is again `| US | co.uk | … | Review |`. The documented rule, `__test_wrs-` plus the lowercase key and the row's ending, derives `__test_wrs-us.co.uk`. T02, T03, T04 and T11 in `examples/test_specification.md`, and the T03 expectation in `examples/bug_report.md`, now select that same `US` row.
- **W01.2 Met.** The diff changes only the six fixture references. The genuine link `[User Story (US)](user_story.md)` in `examples/task.md` keeps its meaning, and the integrity and example checks pass.

<a id="s02--commission-a-task-from-a-reviewed-requirement"></a>

## 2. S02 · Commission a task from a reviewed requirement

Trace a commissioned task from its authority to the behavior and proof the implementer receives. [Story criteria](./specs/spec-driven-authoring/spec.md#s02--commission-a-task-from-a-reviewed-requirement)

- [x] 2.1 [W03](#w03--resolve-coverage-in-both-directions) (T002). Trace work to its source in both directions. Flag the displaced requirement and orphaned criterion while admitting a justified safeguard. May start in parallel.

### W03 · Resolve coverage in both directions

#### Description

A structural pass accepted WEB-999 when it displaced WEB-09.

#### Expected outcome

A plan reviewer can locate a broken citation, an uncovered requirement and unjustified work in the current work record.

Bind explicit references to a declared source. Allow exact sections and documented safeguards. Self-contained documents keep their existing route. For an OpenSpec change, trace from tasks and design to the capability requirement and scenario in the selected change or maintained specification. Keep delivery choices in the native design.

Plan maintainer · R3/A3. [S02.1](./specs/spec-driven-authoring/spec.md#s02-1) and [F2.1](./specs/spec-driven-authoring/spec.md#f2-1). Use the retained mutation and its valid original.

#### Acceptance criteria

- **W03.1** Submit the correct and displaced rows. Report the consumer row, missing ID, searched revision, lost coverage and correction. An unavailable source is identified separately. <a id="w03-1"></a>
- **W03.2** Inspect the reverse mapping: an unowned criterion remains open; work with a supported safeguard remains eligible. For a project without IDs, an exact section link resolves. For an OpenSpec change, inspect the design and native tasks against the capability scenario. For a standalone Implementation Plan (IP), inspect its cited source. The delivery approach must resolve its governing criterion without a second editable definition. <a id="w03-2"></a>

[references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md) · [examples/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/implementation_plan.md) · [scripts/check_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/check_document.py) · [scripts/document_contracts.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/document_contracts.py)

Use the existing comparison; add a mechanical check only for decidable references. Human review assesses meaning. [Actionable diagnostics, 08:55–09:11](https://www.youtube.com/watch?v=O_zcc6Xl12g&t=535s)

#### Verdicts

Candidate: the W03 commit on `implementation/ship-specdev`. Reviewer: implementing agent, comparing checker output on the audit's control with this Task and [S02.1](./specs/spec-driven-authoring/spec.md#s02-1).

- **W03.1 Met.** With `coverage` declared, `scripts/check_document.py --kind plan` passes the example Implementation Plan (IP) against its Spec Driven Development document (SDD). It fails the audit's mutation, in which `WEB-999` replaces `WEB-09`. The two findings name the consumer row on line 87, the missing `WEB-999`, the searched source and revision, the lost `WEB-09` coverage and the correction. An unavailable source is reported as its own finding, without row findings. Regression: `CoverageResolutionTests`.
- **W03.2 Met.** The reverse mapping reports a source requirement without a coverage row as open. A `Safeguard` row with its reason and work stays eligible, and one without a reason is reported. For a project without IDs, an exact section link resolves and a changed anchor is reported. For this OpenSpec change, `design.md` resolves every coverage link against the capability specification, and all 123 distinct specification links in the native `tasks.md` resolve. The delivery approach stays in the design and each criterion stays in the specification. The example IP is checked against its cited SDD. Reviewers still judge meaning, as `references/implementation_plan.md` now states.

- [x] 2.2 [W20](#w20--resolve-feature-story-and-task-ancestry-before-drafting) (T003). Recover the child’s story, criterion and governing revision. Hold a broken parent link while letting a sourced standalone fix proceed. After W03.

### W20 · Resolve feature, story and task ancestry before drafting

#### Description

A task can look ready even when nobody can say which story it supports.

#### Expected outcome

An ordinary request for a child task first resolves the story, its criterion and the feature or epic that owns its outcome.

Teach the order at discovery and task/story entry. Preserve stable independent IDs on reparenting. An expressly standalone task may establish scope inline.

Workflow maintainer · R2/R11/A2/A11. [S02.1](./specs/spec-driven-authoring/spec.md#s02-1) and [F2.1](./specs/spec-driven-authoring/spec.md#f2-1). Use [W03](#w03--resolve-coverage-in-both-directions)’s declared references.

#### Acceptance criteria

- **W20.1** Create a child story for an identified epic, then a task for one story criterion. The reader recovers both source revisions and the shared outcome. <a id="w20-1"></a>
- **W20.2** With the story absent, the epic absent, or a stale or contradictory parent, locate the broken edge and withhold dependent readiness. An explicitly independent broken-link fix can proceed with its own source and expected destination. A missing child parent never silently becomes standalone. <a id="w20-2"></a>

[workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [references/user_story.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/user_story.md) · [references/task.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md)

Use the valid chain and mutations on that chain; test the standalone branch once. No external tracker write.

#### Verdicts

Candidate: the W20 commit on `implementation/ship-specdev`. Reviewers: the implementing agent, and a separate fresh-context reader for W20.1. The chain is an illustrative Websites Review epic, child story and task kept with the private run evidence.

- **W20.1 Met.** Following the new order, the story links the epic's outcome and states epic r3, and the task links story criterion BULK-1 and states story r2 and epic r3. `check_document.py` with declared `parents` passes both. Starting from the task, the reader recovered BULK-1, both revisions with their quoted locations and the epic's shared outcome, and found nothing missing or contradictory.
- **W20.2 Met.** With the story absent or the epic absent, the task is held as not ready. A stale parent anchor is reported as a broken edge, and a parent revised past the task's stated revision is reported. None of these passes as standalone work. A task declared explicitly standalone, with its own source and expected destination, passes without a parent. A contradiction between parent and child is a judgment of meaning; `workflows/discover.md` and `references/task.md` direct the writer to hold the child and report the edge. Regression: `ParentEdgeTests`.

- [x] 2.3 [W11](#w11--write-an-epic-whose-stories-prove-a-usable-outcome) (T004). Connect an epic, story and task to one usable outcome. Withhold epic acceptance if its integrated result is missing after all children close. After W20. If the scope spans capabilities, use W10 first.

### W11 · Write an epic whose stories prove a usable outcome

#### Description

A list of closed tickets can hide an incomplete delivery.

#### Expected outcome

A planner can write a parent epic with linked stories, bounded child tasks and its own integrated proof.

Use the project’s governing outcome or link its existing User Story (US). In a native change, capture the observable behavior once in the capability requirement and scenarios. For an OpenSpec change, keep task scope and proof with the numbered checkbox. Link an existing Task where it independently owns the criterion. Preserve related observations before assigning independent work.

Story-guidance maintainer · R2/R11/A2/A11. [S02.1](./specs/spec-driven-authoring/spec.md#s02-1) and [F2.1](./specs/spec-driven-authoring/spec.md#f2-1). Use [W20](#w20--resolve-feature-story-and-task-ancestry-before-drafting) and a known feature outcome; use [W10](#w10--map-independent-capabilities-before-specifying-each-one) if scope spans capabilities.

#### Acceptance criteria

- **W11.1** For an initiative with related reports, write a parent epic, a usable child story and a scoped task. The parent exposes non-goals, dependencies, integrated proof and ownership. Each child inherits the right criterion. <a id="w11-1"></a>
- **W11.2** Close all child tasks while withholding the parent’s integrated observation. The epic stays unaccepted. A plausible common cause remains provisional; preserve both original observations. <a id="w11-2"></a>

[references/user_story.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/user_story.md) · [references/task.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md) · [examples/user_story.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/user_story.md)

Use the same chain used in W20 when compatible. Check the parent outcome once rather than recreating each child test.

#### Verdicts

Candidate: the W11 commit on `implementation/ship-specdev`. Reviewers: the implementing agent, and a separate fresh-context reviewer who applied the new "Epics" section of `references/user_story.md` to the illustrative epic, story and task kept with the private run evidence.

- **W11.1 Met.** The epic, written from the two related bulk-edit reports, states its outcome with WEB-09 and WEB-10, non-goals, dependencies, the integrated T16 proof, the acceptance owner and each story owner. The reviewer recovered all of them. The story inherits the epic's three-state outcome, and the task delivers story criterion BULK-1. Its parent edges pass W20's check.
- **W11.2 Met.** With all three child tasks closed and the integrated proof unobserved, the reviewer judged the epic unaccepted, citing the guidance that closed children show progress, not delivery. Both original reports keep their sources, and the shared cause stays "plausible" and "not confirmed". A contrasting epic that claimed acceptance from closed children and a confirmed root cause was rejected on both statements.

<a id="s01--edit-a-mixed-passage-without-corrupting-its-fixture-continued"></a>

## 3. S01 · Edit a mixed passage without corrupting its fixture (continued)

- [x] 3.1 [W02](#w02--protect-literal-values-during-ordinary-edits) (T005). Edit the mixed passage. Compare literal fixture and quotation bytes, and accept valid alternative prose that preserves their meaning. After W01.

### W02 · Protect literal values during ordinary edits

#### Description

A naming convention can alter data even when the prose looks better.

#### Expected outcome

An editor can handle a literal, quoted text and a genuine document name in one passage.

Update the owning guidance and its naming check together if the agreed rule changes. Keep consumed full labels and aliases.

Style maintainer · R1/A1. [S01.1](./specs/spec-driven-authoring/spec.md#s01-1) and [F1.1](./specs/spec-driven-authoring/spec.md#f1-1). Use [W01](#w01--repair-the-websites-review-fixture-and-its-consumers). D1 authorizes first-use expansion in authored prose. User requests may use either spelling at any turn.

#### Acceptance criteria

- **W02.1** Edit the mixed passage through the normal route. The fixture and quoted bytes survive while the genuine label matches the adopted rule. Retain the excerpt and checker result. <a id="w02-1"></a>
- **W02.2** Change only prose phrasing to a valid alternative. It remains eligible; deliberately altering the fixture fails the consumer comparison. <a id="w02-2"></a>

[references/writing_style.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md) · [scripts/writing_style_contract.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/writing_style_contract.py) · [scripts/test_document_names.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/test_document_names.py)

Use the W01 fixture as the counterexample. Stop when literal preservation and legitimate editing are both observed.

#### Verdicts

Candidate: the W02 commit on `implementation/ship-specdev`. Reviewer: implementing agent, comparing session checks and the consumer derivation with this Task and [S01.1](./specs/spec-driven-authoring/spec.md#s01-1). D1's first-use convention is now the rule in `references/writing_style.md` and in `writing_style_contract.py`'s naming check, which reports a bare name or acronym only before the first full "Name (ACRONYM)" use.

- **W02.1 Met.** The mixed passage holds the `US` fixture row, a quotation and a genuine `[User Story (US)](user_story.md)` link. It was edited through `validate_document.py` (`edit`, `excerpt`) with the row and quotation declared as required literals. The session check passed with no findings. The row, quotation and label survive byte for byte, and the consumer still derives `__test_wrs-us.co.uk`.
- **W02.2 Met.** A second, prose-only alternative also passed and derived the same domain. Expanding the key to `User Story (US)` failed the session check on the missing literal and made the consumer derive `__test_wrs-user story (us).co.uk`. Regressions: `test_first_use_expands_the_name_and_later_mentions_may_use_the_acronym` and `test_fixture_keys_and_quoted_bytes_keep_their_value_beside_a_document_label`.

<a id="s14--use-the-discovery-interview-record-at-its-handoff"></a>

## 4. S14 · Use the discovery interview record at its handoff

Recover a stakeholder decision and an unresolved question from the interview. [Story criteria](./specs/spec-driven-authoring/spec.md#s14--use-the-discovery-interview-record-at-its-handoff)

- [x] 4.1 [W12](#w12--author-the-discovery-interview-record) (T006). Capture the actual delay the owner identifies. With complete sources, proceed directly. Leave an unspecified latency target open.

### W12 · Author the discovery interview record

#### Description

Existing questions can be useful while the next author has no durable restatement to consume.

#### Expected outcome

The requester can ask for the complete interview record; a brief author can cite it.

Extend discovery with the interview output, grounded dialogue, confirmation state and conditional checked delivery. Keep small independent questions together.

Discovery maintainer · R5/R10/A5/A10a. [S14.1](./specs/spec-driven-authoring/spec.md#s14-1) and [F14.1](./specs/spec-driven-authoring/spec.md#f14-1). Needs the supplied conversation and explicit decisions, if any.

#### Acceptance criteria

- **W12.1** Given “make reviews faster”, ask which delay matters if evidence does not settle it. Record the answer, source, restatement and open decisions; use actual owner confirmation only. <a id="w12-1"></a>
- **W12.2** With complete sources, proceed without a new interview. If the owner is silent or a latency target is absent, preserve that uncertainty and withhold the invented target from the brief. <a id="w12-2"></a>

[workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [scripts/planning_readiness.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/planning_readiness.py) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

One ambiguous exchange and one complete-input control; reuse the interview as W09 input. Preserve exact owner expressions when they change scope.

#### Verdicts

Candidate: the W12/W09 commit on `implementation/ship-specdev`. The new `references/discovery_interview.md` and its example define the record; `workflows/discover.md` links it; contract kind `interview` gives checked delivery. Performers were fresh-context agents that followed the installed skill; the owner's words came from supplied conversations. Reviewer: implementing agent.

- **W12.1 Met.** Given "make reviews faster" and the Websites Review specification, the performer explained the competing delays from WEB-06, WEB-09 and WEB-12, asked which one mattered and stopped without drafting or inventing an answer. With the owner's reply supplied, it wrote a record that keeps the question, the owner's exact words and their source, and the restatement as "awaiting the owner's reply" because the owner had not confirmed it. Open decisions are listed. The record passes the `interview` contract.
- **W12.2 Met.** With a conversation that already settled the delay and contained the owner's "Yes, exactly", a second performer wrote the record without asking, recorded that reply as confirmation, and recorded the unanswered target question as "No reply" with no number. The W09 brief built from an interview record also kept the target and baseline open.

<a id="s05--decide-whether-an-opportunity-warrants-product-definition"></a>

## 5. S05 · Decide whether an opportunity warrants product definition

Decide from the sourced brief whether the opportunity warrants product definition. [Story criteria](./specs/spec-driven-authoring/spec.md#s05--decide-whether-an-opportunity-warrants-product-definition)

- [x] 5.1 [W09](#w09--author-a-brief-from-opportunity-evidence) (T007). Write a sourced brief whose reader can recover the beneficiary, decision and missing baseline without an invented target or budget. Use sourced intent. If intent is missing, use W12 first.

### W09 · Author a brief from opportunity evidence

#### Description

Requiring a full product definition during shaping makes unknowns look settled.

#### Expected outcome

An owner can request and receive a complete brief directly from SpecDev.

Use a compact product-guidance variant with its own sufficient content and checked delivery. An existing interview is an input when intent needed elicitation.

Product-guidance maintainer · R2/R10/A2/A10b. [S05.1](./specs/spec-driven-authoring/spec.md#s05-1) and [F5.1](./specs/spec-driven-authoring/spec.md#f5-1). Use sourced intent or an interview record from [W12](#w12--author-the-discovery-interview-record).

#### Acceptance criteria

- **W09.1** From a supplied need and an unknown baseline, author problem, beneficiary, desired outcome, non-goals and unresolved choices. Identify the source and any supplied appetite. <a id="w09-1"></a>
- **W09.2** Give the brief to the product author. They can recover the decision and missing baseline. An invented budget, target or approval fails. <a id="w09-2"></a>

[references/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/product_requirements_document.md) · [examples/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/product_requirements_document.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

One brief with an explicit unknown proves the distinction; retain its checked output for downstream use.

#### Verdicts

Candidate: the W12/W09 commit on `implementation/ship-specdev`. The new `references/product_brief.md` and its example define the compact brief, and contract kind `brief` checks it. Reviewers: the implementing agent, and a fresh-context product author for W09.2.

- **W09.1 Met.** From the interview record and the specification, the performer wrote a brief with the decision, problem and affected administrators, desired outcome, non-goals, unknowns and sources. It names the interview as its source, says that no appetite was supplied and keeps the current queue time and target unknown. It passes the `brief` contract. The performer also found that the interview example's "three failed checks" was not in the specification; both examples now use the specification's "parked" wording.
- **W09.2 Met.** The product author recovered the beneficiary, the decision and the missing baseline from the brief alone and found no invented figure. A variant adding a 45-to-10-minute queue time and an approved two-sprint budget was rejected on each invented claim.

<a id="s04--distinguish-a-prototype-from-approval-to-include-it"></a>

## 6. S04 · Distinguish a prototype from approval to include it

Have a reader recover the decision and distinguish prototype evidence from approval. [Story criteria](./specs/spec-driven-authoring/spec.md#s04--distinguish-a-prototype-from-approval-to-include-it)

- [x] 6.1 [W07](#w07--write-the-approval-opening-from-the-detailed-product-evidence) (T008). Write the approval opening. Its reader must identify the user, proposed change, exclusion and pending choice from the detailed evidence.

### W07 · Write the approval opening from the detailed product evidence

#### Description

The opening currently names the problem without necessarily exposing the choice.

#### Expected outcome

The product author can draft the detail, then present a decision-first opening with sourced tradeoffs.

Extend the product guide and example. Only use this opening where approval matters.

Product-guidance maintainer · R4/A4. [S04.1](./specs/spec-driven-authoring/spec.md#s04-1) and [F4.1](./specs/spec-driven-authoring/spec.md#f4-1). Use prototype evidence and an unresolved inclusion decision.

#### Acceptance criteria

- **W07.1** Read only the opening; identify the affected user, proposed change, excluded behavior and actual choice. Each matches the detail. <a id="w07-1"></a>
- **W07.2** A working prototype remains evidence of feasibility. The opening must leave inclusion pending until the owner decides. <a id="w07-2"></a>

[references/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/product_requirements_document.md) · [examples/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/product_requirements_document.md)

Keep the opening and detailed baseline. No invented cost, budget or new executive summary for a routine task.

#### Verdicts

Candidate: the W07/W08 commit on `implementation/ship-specdev`. `references/product_requirements_document.md` now teaches an optional "Decision needed" opening, used only when approval is pending and written after the detail. The contract accepts the section, and the example opens with the pending Reason-filter decision. Reviewer: implementing agent, with W08's cold reader.

- **W07.1 Met.** A reader given only the opening named the affected administrators, the Reason filter, the exclusion and the open decision with its owner. Each matches the example's detail: the scope section lists "adding a Reason filter" outside the release, and the decisions section keeps it for later.
- **W07.2 Met.** The opening calls the staging prototype evidence that the filter is feasible and states that the filter stays outside the release until the product owner decides. The baseline and its detail are unchanged, and no cost or budget is added.

- [x] 6.2 [W08](#w08--judge-the-readers-decision-against-the-owning-detail) (T009). Check the opening with an independent reader. Reject a wrong decision backed by a real quote and accept equivalent correct wording. After W07.

### W08 · Judge the reader’s decision against the owning detail

#### Description

Finding a real quotation can still support an incorrect answer.

#### Expected outcome

A reviewer can assess an approval opening using a cold reader and source-grounded judgments.

Ship the reader task and review guidance together. Keep expected answers outside the reader’s assignment.

Evaluation maintainer · R4/A4. [S04.1](./specs/spec-driven-authoring/spec.md#s04-1) and [F4.1](./specs/spec-driven-authoring/spec.md#f4-1). Consume [W07](#w07--write-the-approval-opening-from-the-detailed-product-evidence)’s opening and its original detail.

#### Acceptance criteria

- **W08.1** An independent reader given only the opening identifies the four W07 elements. Save the opening, response and comparison to detail. <a id="w08-1"></a>
- **W08.2** Use a wrong decision paired with a genuine quote and a correct alternative phrasing. The rubric rejects the former and accepts the latter for the stated reasons. <a id="w08-2"></a>

[workflows/improve_references.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/improve_references.md) · [evals/grades.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/evals/grades.py) · [references/decision_record.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/decision_record.md)

One cold read for the representative material decision. Reuse it at release; no reader run on every document.

#### Verdicts

Candidate: the W07/W08 commit on `implementation/ship-specdev`. `workflows/improve_references.md` now carries the cold-reader task and its review guidance; the reader's task contains no expected answers. Reviewers: a fresh-context reader given only the opening, and a separate fresh-context reviewer applying the guidance.

- **W08.1 Met.** The cold reader, given only W07's opening, identified all four elements with quotations. The comparison with the detail, kept with the private run evidence, found each one correct.
- **W08.2 Met.** The reviewer rejected an answer that called the filter approved while quoting the opening's real prototype sentence. The reason given: the detail says the first release excludes the filter and the owner still decides. It accepted a differently worded answer that matched all four points.

<a id="s09--create-a-projects-first-governed-documents-from-facts"></a>

## 7. S09 · Create a project’s first governed documents from facts

Follow an authored product requirement into the downstream specification. [Story criteria](./specs/spec-driven-authoring/spec.md#s09--create-a-projects-first-governed-documents-from-facts)

- [x] 7.1 [W18](#w18--author-a-complete-product-document-from-project-facts) (T010). Create complete product documents from two projects’ verified facts. Check each document’s scope, authority and sources against its own project.

### W18 · Author a complete product document from project facts

#### Description

The superseded proposal treated an existing Mirai document as a prerequisite.

#### Expected outcome

Using the normal skill, the owner receives a complete Product Requirements Document (PRD) from facts and decisions alone.

Make the existing integration rule actionable in the entry, product guide and worked invocation. Preserve verified terms and owners. No application-specific authoring branch.

Product-guidance maintainer · R9/A9. [S09.1](./specs/spec-driven-authoring/spec.md#s09-1) and [F9.1](./specs/spec-driven-authoring/spec.md#f9-1). Use Mirai inputs with stable IDs and one open approval; no source document template.

#### Acceptance criteria

- **W18.1** From an empty destination produce the whole product document through SpecDev. Check its required sections, facts, scope, sources and actual owner status. <a id="w18-1"></a>
- **W18.2** Use a second project’s verified facts through the same route. It gets its own accurate content; a legacy heading or missing application template cannot prevent normal authoring. <a id="w18-2"></a>

[SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md) · [references/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/product_requirements_document.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json) · [examples/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/product_requirements_document.md)

Two project inputs answer portability. Keep the first reviewed artifact for W19. Legacy forms may supply source facts only.

#### Verdicts

Candidate: the W18 commit on `implementation/ship-specdev`. The integration rule in `SKILL.md` and a new "Write from project facts" passage, with a worked `/prd` invocation, in `references/product_requirements_document.md` make authoring from facts the normal route; a project's own template is source evidence only. Performers were fresh-context agents following the installed skill. Reviewer: implementing agent.

- **W18.1 Met.** From the Mirai due-dates PRD at `ddd183a`, read as facts only, the performer wrote a complete PRD into an empty destination. It passes the `prd` contract. FR-1 to FR-9 and their criteria, SM-1's 70% target with the baseline undecided, NG-1 to NG-4, A-1 and Q-1 are carried over, and owner `mirai-product-manager` is kept. The status line says approval is open and no source shows it was given; the "Decision needed" opening leaves inclusion pending. The reviewed bytes have SHA-256 `5f3b94e5…52e7` and are kept for W19.
- **W18.2 Met.** Through the same route, the Nacre workspace-renaming facts produced their own PRD with CONF-01 to CONF-03 and AUD-01. It passes the contract and keeps naming length, concurrency, targets and approval open, with no Mirai content. The Mirai source's own front matter and "Summary for approval" layout did not block authoring.

- [x] 7.2 [W19](#w19--hand-an-authored-product-requirement-to-the-downstream-specification) (T011). Carry the product obligation, exclusion and unresolved decision into the governing behavior document. Locate an incompatible consumer field at its owner. After W18.

### W19 · Hand an authored product requirement to the downstream specification

#### Description

A complete product document can still lose its authority or meaning at the next boundary.

#### Expected outcome

SpecDev authors the selected capability specification or independent requested document from the W18 artifact and reports compatibility at the actual consumer.

Carry criterion IDs, scope, permission and source revision into the new document. Preserve historical approvals. Surface an incompatible external field at its owner.

Integration maintainer · R9/R3/A9/A3. [S09.1](./specs/spec-driven-authoring/spec.md#s09-1) and [F9.1](./specs/spec-driven-authoring/spec.md#f9-1). Requires [W18](#w18--author-a-complete-product-document-from-project-facts)’s reviewed output and actual source revision.

#### Acceptance criteria

- **W19.1** From W18’s reviewed product requirement, recover the obligation, exclusion and unresolved decision in the resulting behavior specification and save both source bindings. For an OpenSpec change, write the behavior once in its capability delta using requirements and scenarios, or link the governing criterion if it already has an owner. For an independent document request, use its selected writing contract. The reader can recover the user outcome and acceptance before design or task selection. <a id="w19-1"></a>
- **W19.2** Supply a conflicting consumer-format demand. Identify the incompatible field and owning interface. Preserve reviewed bytes and withhold a live-compatibility claim unless the actual consumer accepted them. <a id="w19-2"></a>

[references/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md) · [examples/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/spec_driven_development.md) · [workflows/validation_review.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/validation_review.md) · [scripts/validate_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/validate_document.py)

One linked document and one conflict are sufficient. App migration, signing, external publication and runtime changes require separate authority.

#### Verdicts

Candidate: the W18 candidate (`8518f03`); W19 needed no further skill change. Reviewer: implementing agent, comparing the performer's output with the reviewed PRD and this Task.

- **W19.1 Met.** This was an independent request, so the specification used the Spec Driven Development document (SDD) contract. From W18's reviewed PRD (SHA-256 `5f3b94e5…52e7`, recorded in the specification with its path), the performer wrote a draft specification that passes the `sdd` contract (SHA-256 `84311b86…8089`). It carries FR-1 to FR-9 with their BR links and criteria, NFR-1 and NFR-2, the permission rule, NG-1 to NG-4 and open decisions Q-1 and approval. Purpose, scope, scenarios and acceptance precede any design or task. An OpenSpec capability delta was not exercised here; W40 and W47 cover the native route.
- **W19.2 Met.** Asked to add `template: sdd@v1` front matter and a `## Summary for approval` section for the Mirai loader, the performer kept the reviewed file byte for byte. It named the conflicting fields and the loader as the owning interface, proposed an adapter or a decision by the format's owners, and claimed no compatibility with the loader.

<a id="s15--use-the-capability-map-at-its-handoff"></a>

## 8. S15 · Use the capability map at its handoff

Identify independent capabilities and select the next one to specify. [Story criteria](./specs/spec-driven-authoring/spec.md#s15--use-the-capability-map-at-its-handoff)

- [x] 8.1 [W10](#w10--map-independent-capabilities-before-specifying-each-one) (T012). Map two independent capabilities and their dependent one. Verify both starters are eligible and that a cycle blocks the affected order. Requires an identified initiative from a brief or product definition.

### W10 · Map independent capabilities before specifying each one

#### Description

A broad initiative can mix separate outcomes and introduce imaginary dependencies.

#### Expected outcome

A spec author can select one stable capability, identify its scope and start its specification in the right order.

Author the capability map as an independently requestable planning artifact. Distinguish capability boundaries from runtime surface names.

Planning-guidance maintainer · R2/R10/A2/A10c. [S15.1](./specs/spec-driven-authoring/spec.md#s15-1) and [F15.1](./specs/spec-driven-authoring/spec.md#f15-1). Requires an identified initiative; can consume the brief or product definition.

#### Acceptance criteria

- **W10.1** Given two independent capabilities and one dependent capability, write IDs, responsibilities, dependency edges and build order. Either independent starting point is eligible. The child specification cites the selected ID. <a id="w10-1"></a>
- **W10.2** Introduce a cycle. Locate it and withhold the affected order. On a single-capability request proceed directly without manufacturing a map. <a id="w10-2"></a>

[references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md) · [references/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

Reuse one three-capability example. No permutation suite or formal graph service.

#### Verdicts

Candidate: the W10/W13 commit on `implementation/ship-specdev`. The new `references/capability_map.md`, its example and contract kind `capability_map` make the map an independently requestable artifact that names capabilities by what users can do. The performer was a fresh-context agent following the installed skill. Reviewer: implementing agent.

- **W10.1 Met.** For a team-calendar initiative with two independent capabilities and one dependent capability, the performer wrote CAP-1 to CAP-3, gave the single dependency (CAP-2 on CAP-1) its reason, and let CAP-1 and CAP-3 start in parallel. The map passes the contract, and the child specification's opening cites "CAP-1".
- **W10.2 Met.** When the owner's launch condition made CAP-1 depend on CAP-2, the performer named the cycle and held both capabilities' order. CAP-3 stayed startable, IDs stayed stable and the resolution was left to the owner. A single dark-mode request got no map and was routed to direct specification.

<a id="s16--use-the-research-record-at-its-handoff"></a>

## 9. S16 · Use the research record at its handoff

Trace the design choice to a source or an explicit research gap. [Story criteria](./specs/spec-driven-authoring/spec.md#s16--use-the-research-record-at-its-handoff)

- [x] 9.1 [W13](#w13--author-the-research-record-that-informs-a-design-choice) (T013). Write the sourced WEB-09 research finding and retry condition. Removing the governing passage must leave its dependent conclusion open.

### W13 · Author the research record that informs a design choice

#### Description

A task can paraphrase a retry rule and imply a cause its evidence never established.

#### Expected outcome

A designer can follow the research record to the governing passage and see what decision is still open.

Use the decision guide for alternatives and authority, with an explicit research form for questions, sources, findings and limits. Keep confirmation and supersession with the actual decision owner.

Research-guidance maintainer · R5/R10/A5/A10d. [S16.1](./specs/spec-driven-authoring/spec.md#s16-1) and [F16.1](./specs/spec-driven-authoring/spec.md#f16-1). Requires a material question and the supplied primary source or a recorded access gap.

#### Acceptance criteria

- **W13.1** Read the source for WEB-09, compare it with a paraphrased symptom report, then author the research record. It cites the governing retry condition, alternatives and supported finding. The designer can follow the link. <a id="w13-1"></a>
- **W13.2** Remove the governing passage. The specific gap and its affected conclusion stay open. A recommendation or prototype cannot become an accepted decision. <a id="w13-2"></a>

[references/decision_record.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/decision_record.md) · [workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [examples/decision_record.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/decision_record.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

Use actual supplied content or observed source access. A writer’s assertion of a read alone cannot establish it.

#### Verdicts

Candidate: the W10/W13 commit on `implementation/ship-specdev`. The new `references/research_record.md`, its example and contract kind `research` define the record and point decisions to the Decision Record (DR). The performer was a fresh-context agent with only the supplied files. Reviewer: implementing agent.

- **W13.1 Met.** Given the reviewer's paraphrase ("just retry it automatically") and the specification and test example, the record quotes WEB-09's governing retry passage and T16's 500/500/1 outcome. It compares automatic retry, reconcile-then-explicit-retry and stop-and-report against them, and labels its reading of "timeout" as an inference. It recommends no automatic retry and leaves the decision open. It passes the `research` contract, and each finding links its specification section.
- **W13.2 Met.** With WEB-09 removed from the supplied specification, the record named the missing passage, kept every dependent conclusion open and asked for the text from its owner. Asked to mark an uninspected, reportedly working prototype as accepted, it kept the decision open and recorded the prototype claim as unverified.

<a id="s17--use-the-feature-map-at-its-handoff"></a>

## 10. S17 · Use the feature map at its handoff

Locate the named feature at its actual entry point. [Story criteria](./specs/spec-driven-authoring/spec.md#s17--use-the-feature-map-at-its-handoff)

- [x] 10.1 [W05](#w05--author-a-feature-map-from-verified-surfaces) (T014). Map the evidenced surface, action and end state so a verifier can locate them. Mark a missing handle or proposed surface as unverified.

### W05 · Author a feature map from verified surfaces

#### Description

A feature name alone does not tell a verifier how to reach it.

#### Expected outcome

A verifier can use a complete feature map to locate the named screen or operation and its observable result.

Add the authoring route, stable surface references, a worked example and checked output through SpecDev.

Verification-guidance maintainer · R10/A10e. [S17.1](./specs/spec-driven-authoring/spec.md#s17-1) and [F17.1](./specs/spec-driven-authoring/spec.md#f17-1). Requires a source exposing at least one actual entry or operation.

#### Acceptance criteria

- **W05.1** From supplied surface evidence, write the map with name, entry, handle/action, source revision and observable end state. A verifier locates the intended surface from the row. <a id="w05-1"></a>
- **W05.2** Withhold a handle or supply an unverified future surface. The artifact marks it unverified or proposed. Launching the app cannot certify that feature. <a id="w05-2"></a>

[references/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/test_specification.md) · [examples/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/test_specification.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

Use one grounded surface and one missing detail. A fabricated selector fails; a real consumer observation may be reused.

#### Verdicts

Candidate: `6bb4652`, which adds `references/feature_map.md`, its example and contract kind `feature_map`. The performer was a fresh-context agent following the installed skill with a captured Nacre settings page as evidence. Reviewer: implementing agent.

- **W05.1 Met.** The map's rows give the user-facing name, the route `/settings/workspace`, the handles (the "Rename workspace" form, the "Workspace name" field, the "Save name" button with `data-testid="save-workspace-name"`, and the `rename-status` element), the capture's build and commit, and the end state. Every handle the map names occurs in the captured page, so a verifier can locate it. The map passes the contract.
- **W05.2 Met.** The status message's text, which the capture doesn't show, and the end state, which comes from the product specification, are marked unverified, and no wording was invented. The planned Transfer ownership page is listed as proposed, with no route or handle. A QA report that the app launched was recorded, but no row was marked verified because of it.

<a id="s18--use-the-critical-journeys-at-its-handoff"></a>

## 11. S18 · Use the critical journeys at its handoff

Follow the mapped journey to its observable result. [Story criteria](./specs/spec-driven-authoring/spec.md#s18--use-the-critical-journeys-at-its-handoff)

- [x] 11.1 [W06](#w06--author-a-critical-journey-that-consumes-the-feature-map) (T015). Write a critical journey with the sourced actor, steps, screen and end check. Expose the missing screen or check without claiming a pass. Requires the W05 map or compatible existing evidence.

### W06 · Author a critical journey that consumes the feature map

#### Description

User journeys in the product guide do not establish a connection to a verifiable surface.

#### Expected outcome

A downstream tester receives a standalone journey with resolvable steps, sourced risk and evidence status.

Connect the journey to the map, governing requirement and test reference. Keep the original business need in the product source.

Journey-guidance maintainer · R3/R10/A3/A10f. [S18.1](./specs/spec-driven-authoring/spec.md#s18-1) and [F18.1](./specs/spec-driven-authoring/spec.md#f18-1). Requires a mapped surface from [W05](#w05--author-a-feature-map-from-verified-surfaces) or compatible existing evidence.

#### Acceptance criteria

- **W06.1** Author a journey from W05. Its ID, actor, ordered steps, sourced criticality and end state are present; the tester resolves the screen and check. <a id="w06-1"></a>
- **W06.2** Use an unknown screen or remove the test. Locate the unresolved reference or state that a check is missing. The document cannot report that the journey passed. <a id="w06-2"></a>

[references/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/product_requirements_document.md) · [references/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/test_specification.md) · [examples/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/test_specification.md)

Reuse the map. A declared test path can establish a reference; only an executed observation establishes the result.

#### Verdicts

Candidate: `6bb4652`, which adds `references/critical_journeys.md`, its example and contract kind `journeys`. The performer was a fresh-context agent using the committed Websites Review feature map and test specification as compatible existing evidence. Reviewer: implementing agent.

- **W06.1 Met.** CJ-1, "Resolve one parked website inline", names the administrator, four ordered steps on mapped surfaces, WEB-06 as its criticality source and the end state. Its checks are T09 and T11, which a tester can find in the test specification. The journeys pass the contract.
- **W06.2 Met.** The CSV-export journey, whose screen isn't in the feature map, marks that step unresolved and its check as missing. Its criticality is recorded as a support report with no requirement behind it. Asked to mark the journeys passed after "a good QA cycle", the performer recorded CJ-1 as not run and CJ-2 as unable to pass yet.

<a id="s03--verify-one-critical-journey-against-its-source"></a>

## 12. S03 · Verify one critical journey against its source

Follow the approved journey to a user-visible result and distinguish stale evidence. [Story criteria](./specs/spec-driven-authoring/spec.md#s03--verify-one-critical-journey-against-its-source)

- [x] 12.1 [W21](#w21--preserve-conditions-and-reopen-stale-evidence) (T016). Check response loss across 1,001 rows. Distinguish 500 confirmed, 500 unresolved and one unattempted, and retain prior failures on revision. After W03, with a reachable journey such as W06.

### W21 · Preserve conditions and reopen stale evidence

#### Description

A valid requirement ID can survive while a permission, limit or operation disappears.

#### Expected outcome

A reviewer can reject a weakened case and invalidate only evidence affected by a changed source.

Extend the connected Websites Review example and review method, including meaningful negative cases, lifecycle verdicts and candidate binding.

Verification maintainer · R3/R8/A3/A8. [S03.1](./specs/spec-driven-authoring/spec.md#s03-1) and [F3.1](./specs/spec-driven-authoring/spec.md#f3-1). Use [W03](#w03--resolve-coverage-in-both-directions) and a reachable example; [W06](#w06--author-a-critical-journey-that-consumes-the-feature-map) supplies one.

#### Acceptance criteria

- **W21.1** Given T16 and 1,001 rows, the written check distinguishes 500 confirmed, 500 unresolved and one unattempted after response loss. A fresh read precedes any offered retry, and only the administrator chooses it. A request count or automatic retry fails. <a id="w21-1"></a>
- **W21.2** Keep an ID but weaken a material condition; the reviewer rejects it. Change its governing revision and retain the old failure and unrelated valid evidence. Compare before/after verdicts. A valid paraphrase remains eligible. <a id="w21-2"></a>

[references/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md) · [references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md) · [examples/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/test_specification.md) · [examples/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/spec_driven_development.md)

The corresponding change-in-place counterexample starts with an existing value and observes the replacement. Stop at proof about the authored example. Formal verification would establish only the property it models. [Verification scope, 10:50–11:30](https://www.youtube.com/watch?v=O_zcc6Xl12g&t=650s)

#### Verdicts

Candidate: the W21 commit on `implementation/ship-specdev`. `references/test_specification.md` gains a "Review a case against its source" method covering weakened conditions, paraphrases, change-in-place cases and candidate-bound verdict lifecycles. T16 in the example now states who starts the retry and which outcomes fail it. Reviewer: a fresh-context reviewer applying that section, compared by the implementing agent with WEB-09.

- **W21.1 Met.** T16 distinguishes 500 confirmed, 500 unresolved and 1 unattempted after response loss. It requires reconciliation before any retry is offered, lets only the administrator start one and fails a bare request count or an automatic retry. The reviewer accepted it on each of those conditions.
- **W21.2 Met.** A contributor's version that kept `T16 / WEB-09` but reported "1 of 3 requests completed" and resubmitted automatically was rejected, with each dropped condition named. A paraphrase keeping every condition was accepted. When WEB-09 moved to version 2, only T14 to T16 reopened as Not demonstrated, while their build-41 verdicts, including T16's failure, stayed in history. T11's unrelated Met verdict was kept with its candidate and date. The reviewer also noted that T16's figures would change under the new limit.

<a id="s19--use-the-requirements-quality-checklist-at-its-handoff"></a>

## 13. S19 · Use the requirements-quality checklist at its handoff

Identify the requirement that needs clarification before work starts. [Story criteria](./specs/spec-driven-authoring/spec.md#s19--use-the-requirements-quality-checklist-at-its-handoff)

- [x] 13.1 [W04](#w04--author-a-requirements-quality-checklist-for-the-implementer) (T017). Evaluate ambiguous retry authority in the requirements checklist. After clarification update only the affected judgment and retain both verdicts. After W03, with a drafted specification.

### W04 · Author a requirements-quality checklist for the implementer

#### Description

A completed checklist can be mistaken for successful implementation.

#### Expected outcome

SpecDev produces a complete reviewer-owned checklist tied to the candidate specification.

Author the standalone form and its checked delivery path. Existing review guidance owns the judgments; avoid a second acceptance registry.

Review-guidance maintainer · R3/R10/A3/A10g. [S19.1](./specs/spec-driven-authoring/spec.md#s19-1) and [F19.1](./specs/spec-driven-authoring/spec.md#f19-1). Requires a candidate specification and [W03](#w03--resolve-coverage-in-both-directions) references.

#### Acceptance criteria

- **W04.1** Request a requirements-quality checklist on a requirement with ambiguous retry authority. Its row gives the revision, quality question, located evidence, verdict and required correction. <a id="w04-1"></a>
- **W04.2** After clarification, update only that judgment. The implementer can see the resolved rule; no checkmark claims code was built or tested. Retain both verdicts and the checked artifact. <a id="w04-2"></a>

[workflows/validation_review.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/validation_review.md) · [references/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

One reviewed requirement before and after clarification proves this increment. Reuse the same checklist for release evidence.

#### Verdicts

Candidate: `6bb4652`, which adds `references/requirements_checklist.md`, its example and contract kind `requirements_checklist`. The performer was a fresh-context agent following the installed skill. Reviewer: implementing agent.

- **W04.1 Met.** For a bulk-export specification at revision r3 whose EXP-2 says only "it can be retried", the checklist rows name the revision, ask "Who may retry?" and "Does a retry start automatically or on request?", quote the passage and record Defect with the correction needed. Other rows record Ready or Needs decision with their evidence. It passes the contract.
- **W04.2 Met.** After the owner's r4 clarification, only the two EXP-2 rows changed, to Ready, citing the quoted rule. The retry-limit question stays open, the r3 checklist is kept unchanged and its verdicts are listed in History. A request to mark EXP-1 done because a developer built it was declined: the checklist records requirement quality, not build or test status.

<a id="s10--read-a-work-item-without-guessing-what-success-means"></a>

## 14. S10 · Read a work item without guessing what success means

Have a reader recover the visible outcome and permission from the revised work item. [Story criteria](./specs/spec-driven-authoring/spec.md#s10--read-a-work-item-without-guessing-what-success-means)

- [x] 14.1 [W22](#w22--replace-vague-acceptance-text-with-the-visible-result) (T018). Rewrite the acceptance clause so an administrator can distinguish confirmed, uncertain and unattempted work and retain the 500-ID boundary.

### W22 · Replace vague acceptance text with the visible result

#### Description

The task tells the implementer that uncertain writes are reported honestly. The source says what the administrator sees and who may choose a retry.

#### Expected outcome

The published task is usable on its own for this criterion. A writer can follow the before/after example in the task guide when editing another story or task.

Correct the worked clause, keep the surrounding limit and count refresh, and add a short contrast to the owning guide. Keep source terms where a synonym would change an ID, permission or technical meaning. Offer one plain-language rendering without prescribing identical prose.

Task-guidance maintainer · R12/A12. [S10.1](./specs/spec-driven-authoring/spec.md#s10-1) and [F10.1](./specs/spec-driven-authoring/spec.md#f10-1). Requires WEB-09–WEB-10 and the existing task and story examples.

#### Acceptance criteria

- **W22.1** Read the original clause and governing source. Edit the task so the administrator can distinguish confirmed, uncertain and unattempted rows. It says when to stop and preserves the fresh read before offering an optional administrator retry. Save the changed passage with the source. <a id="w22-1"></a>
- **W22.2** Compare the full edited criterion with its neighbors. The 500-ID bound, refresh of confirmed rows and counts and permission survive. A clear existing story about a site leaving Review remains understandable. No invented guarantee or forced stylistic change is needed. <a id="w22-2"></a>

[Worked task](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/issue.md#L19) · [Clear story](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/user_story.md#L18) · [Task guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [Writing guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md)

One usable example and its guidance ship in this commit. The first signal is whether the original phrase allows both an informative summary and a generic error. Reuse W21’s requirement evidence.

#### Verdicts

Candidate: the W22/W23 commit on `implementation/ship-specdev`. The original clause "partial or uncertain writes stop and are reported honestly" allowed both an informative summary and a generic error. Reviewer: implementing agent, with W23's reader.

- **W22.1 Met.** The WEB-09–WEB-10 criterion in `examples/task.md` now says that no further batches are sent after the first failed or unanswered request. It says the administrator sees separate confirmed, unresolved and unattempted counts, that the saved state is read before any retry is offered, and that the administrator decides whether to retry. `references/task.md` carries the before and after as a worked example with WEB-09 as its source.
- **W22.2 Met.** The 500-ID bound, the refresh of confirmed rows and counts and the separate WEB-05–WEB-08 permission criterion are unchanged in meaning. The story example about a site leaving Review needed no change, and nothing beyond WEB-09 and WEB-10 was promised. The task passes the `task_feature` contract.

- [x] 14.2 [W23](#w23--review-markdown-by-what-the-reader-can-recover) (T019). Have a reader recover who may retry after response loss. Reject mandatory retry wording and accept a source-supported alternative. After W22.

### W23 · Review Markdown by what the reader can recover

#### Description

A fluent rewrite can omit an essential condition. A mechanical style check cannot tell whether a reader knows when to stop or who owns the next action.

#### Expected outcome

A reviewer can use a source-grounded reader question and a wrong paraphrase to accept a clear work item or return a specific correction.

Ship the review guidance, an ordinary editing request and the grader’s private comparison. Use the existing evaluation route. Keep all valid wordings eligible.

Evaluation maintainer · R12/A12. [S10.1](./specs/spec-driven-authoring/spec.md#s10-1) and [F10.1](./specs/spec-driven-authoring/spec.md#f10-1). Use the corrected [W22](#w22--replace-vague-acceptance-text-with-the-visible-result) task and the actual upstream obligations.

#### Acceptance criteria

- **W23.1** Give a reader only the edited task. Ask what happens after a response is lost and who may retry. Compare the answer with A12 and cite the words carrying each obligation. Missing or incorrect answers identify the exact ambiguity to fix. <a id="w23-1"></a>
- **W23.2** Present two candidate passages with similar tone. One preserves the optional retry and the other requires it. The rubric accepts the first and identifies the changed obligation in the second. A different clear wording receives the same verdict. <a id="w23-2"></a>

[Reference review workflow](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/improve_references.md) · [Existing style cases](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/evals/style_cases.json) · [Governing source](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/spec_driven_development.md#L118)

Share the reader’s packet with W08 if both independently graded results can be observed without revealing either answer. Stop after a supported reader result and the wrong-meaning control. No style benchmark across the entire catalog.

#### Verdicts

Candidate: the W22/W23 commit on `implementation/ship-specdev`. The Task guide's quality check now carries the reader-based review guidance. The acceptance case `accept-task-retry-edit` holds the ordinary editing request, its fixture and the grader's private expected properties. Reviewers: a fresh-context reader given only the edited task, and a separate fresh-context reviewer applying the guidance.

- **W23.1 Met.** Asked what happens after a lost response and who may retry, the reader quoted that no further batches are sent and that the administrator sees separate confirmed, unresolved and unattempted counts. It also quoted that "the page reads the saved state of the unresolved rows" before any retry is offered and that "the administrator decides whether to retry". Each answer matches WEB-09, so no ambiguity remained to fix.
- **W23.2 Met.** Of two passages in a similar tone, the reviewer accepted the one with the optional retry. It rejected the other and named the changed obligation, quoting "the administrator must retry them before closing the dialog". A third, differently worded passage that kept every obligation was accepted.

<a id="s11--follow-a-failed-save-from-story-to-child-task"></a>

<a id="15-s11--follow-a-failed-save-from-story-to-child-issue"></a>

## 15. S11 · Follow a failed save from story to child Task

Follow the failed-save condition from the story to its child Task. [Story criteria](./specs/spec-driven-authoring/spec.md#s11--follow-a-failed-save-from-story-to-child-task)

- [ ] 15.1 [W24](#w24--publish-a-child-task-for-the-storys-failed-save) (T020). Trace the child Task to the failed-save story. Verify visible error, retained selection and absence of success, with bulk edits outside scope. After W20.

<a id="w24--publish-a-child-issue-for-the-storys-failed-save"></a>

### W24 · Publish a child Task for the story’s failed save

#### Description

The existing Task shows a whole Feature.

#### Expected outcome

The approved story and Task references lead to a complete child for one criterion.

Add a worked child under the normal Task route and link it from the relevant story and guide. Preserve the parent Feature and its incoming links.

Examples maintainer · R13/A13. [S11.1](./specs/spec-driven-authoring/spec.md#s11-1) and [F11.1](./specs/spec-driven-authoring/spec.md#f11-1). Use the worked single-site story, WEB-06 and the parent from [W20](#w20--resolve-feature-story-and-task-ancestry-before-drafting).

#### Acceptance criteria

- **W24.1** Follow the normal Task guide to the child. It identifies the source story, the failed-save criterion and the visible error, retained selection and absence of a success message. The proof observes those effects. <a id="w24-1"></a>
- **W24.2** Follow the child’s parent link and the story’s return link. Both resolve. Comparing scope with the story rejects assignment of bulk editing to the child. Retain the linked examples and reader observation. <a id="w24-2"></a>

[Task guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [Worked story](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/user_story.md) · [Parent Feature](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/issue.md)

Commit the connected example and links together. Reuse W20’s ancestry check for unchanged edges.

<a id="s06--carry-discovery-evidence-into-the-next-authoring-decision"></a>

## 16. S06 · Carry discovery evidence into the next authoring decision

Use the source to decide whether one missing answer changes the requirement. [Story criteria](./specs/spec-driven-authoring/spec.md#s06--carry-discovery-evidence-into-the-next-authoring-decision)

- [ ] 16.1 [W28](#w28--ask-the-question-that-changes-the-requirement) (T021). Ask about the unresolved delay, then use the answer in the criterion. A settled request must proceed without another question.

### W28 · Ask the question that changes the requirement

#### Description

A generic interview can anchor a decision the owner has yet to make.

#### Expected outcome

The discovery guide shows how to follow an open answer or proceed with complete evidence.

Ship one contrast at the existing discovery entry. Keep capture of a requested interview record in W12.

Discovery maintainer · R5/A5. [S06.1](./specs/spec-driven-authoring/spec.md#s06-1) and [F6.1](./specs/spec-driven-authoring/spec.md#f6-1). Use the documented ambiguous review-delay request and an otherwise identical request with the delay already identified.

#### Acceptance criteria

- **W28.1** With the delay unspecified, the first question can distinguish two delays. Given the owner’s answer, the next criterion uses the identified delay without inventing a target. Save the exchange and criterion. <a id="w28-1"></a>
- **W28.2** With the delay and acceptance already supplied, the writer proceeds without asking again. Inspect the resulting criterion and stop. <a id="w28-2"></a>

[Discovery](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [Interview-me](https://github.com/addyosmani/agent-skills/blob/8c99fa36d90068c82d547f7c12a9d67a3e95f4ee/skills/interview-me/SKILL.md#L53-L90) · [Grilling](https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/productivity/grilling/SKILL.md)

One commit ships the guidance and its worked contrast.

<a id="s12--act-on-a-handoff-and-resolve-a-misunderstood-role"></a>

## 17. S12 · Act on a handoff and resolve a misunderstood role

Use the handoff to perform the necessary manual action and identify who answers the next question. [Story criteria](./specs/spec-driven-authoring/spec.md#s12--act-on-a-handoff-and-resolve-a-misunderstood-role)

- [ ] 17.1 [W25](#w25--guide-the-owner-through-one-necessary-manual-action) (T022). Give the owner the exact read action and expected title for the necessary handoff. Answer directly when the document is already open.

### W25 · Guide the owner through one necessary manual action

#### Description

A link that works in the writer’s checkout may fail in the owner’s starting state.

#### Expected outcome

A user can perform an authorized read from their actual starting point and recognize success or a wrong reference.

Add the Session replies section to the shared style guide and link it from the skill entry. Reuse existing how-to instructions. Apply to an ordinary reply outside checked finalization.

Style maintainer · R14/A14. [S12.1](./specs/spec-driven-authoring/spec.md#s12-1) and [F12.1](./specs/spec-driven-authoring/spec.md#f12-1). Use a supplied read-only handoff with known location, available reference, expected title and a known missing-reference response.

#### Acceptance criteria

- **W25.1** Given the owner must open the supplied document, the reply names the starting location, exact read action, expected title and safe next action for the supplied failure. A reader can follow it from that starting state. <a id="w25-1"></a>
- **W25.2** If the owner already has the document and only asks what it says, answer directly. Supplying redundant commands, guessing a path or asking the owner to make a write fails. Retain the replies and the source. <a id="w25-2"></a>

[Style guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md) · [Procedure guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/how_to_guide.md) · [Mirai session guide](https://github.com/jetmirhaxhisefa/mirai/blob/ddd183a3728d3fdd9f776755de47d4d314c8925c/registry/skills/mirai-write/guides/session.md)

Ship one portable route and its usable example in one commit.

- [ ] 17.2 [W26](#w26--clarify-who-acts-when-an-explanation-was-misunderstood) (T023). Clarify who supplies reader answers. Cite the source for an assigned role or preserve the choice when it is unsettled. After W25.

### W26 · Clarify who acts when an explanation was misunderstood

#### Description

The owner can hear “reader” as an assignment to do the work personally.

#### Expected outcome

The owner can tell who answers, who decides and what remains open.

Extend the same session section with one clarification example. Keep supported permission and role names.

Style maintainer · R14/A14. [S12.1](./specs/spec-driven-authoring/spec.md#s12-1) and [F12.1](./specs/spec-driven-authoring/spec.md#f12-1). Requires [W25](#w25--guide-the-owner-through-one-necessary-manual-action)’s section and a supplied choice about who answers reader questions.

#### Acceptance criteria

- **W26.1** When the owner asks whether they must write the reader answers, the first sentence resolves the misunderstanding from the supplied source. A different concrete example explains the decision still theirs. Save the reply and source passage. <a id="w26-1"></a>
- **W26.2** If the source leaves the answering role open, the reply identifies the open choice. Repeating the original unexplained role, assigning the owner new work or promising a check that never ran fails. <a id="w26-2"></a>

[Style guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md) · [Mirai session guide](https://github.com/jetmirhaxhisefa/mirai/blob/ddd183a3728d3fdd9f776755de47d4d314c8925c/registry/skills/mirai-write/guides/session.md#L77-L111)

Ship the repair example and its acceptance comparison. Reuse W25’s route.

<a id="s07--receive-the-right-next-action-and-a-checked-result"></a>

## 18. S07 · Receive the right next action and a checked result

Read the checked handoff and identify the result, blocker or decision. [Story criteria](./specs/spec-driven-authoring/spec.md#s07--receive-the-right-next-action-and-a-checked-result)

- [ ] 18.1 [W14](#w14--write-progress-decision-and-blocker-messages-from-evidence) (T024). Write updates, blockers and decisions from their evidence. The reader can identify the consequence, missing input or actual choice. Reuse W22 where available.

### W14 · Write progress, decision and blocker messages from evidence

#### Description

A generic status can leave the user unsure what to do.

#### Expected outcome

The writer gives a concise public update that matches the observed state and any required action.

Ship contrasting session examples through shared style guidance. F13 owns the scope of the file-based check.

Style maintainer · R6/A6. [S07.1](./specs/spec-driven-authoring/spec.md#s07-1) and [F7.1](./specs/spec-driven-authoring/spec.md#f7-1). Use a confirmed result, unresolved choice and genuine external blocker. Use [W22](#w22--replace-vague-acceptance-text-with-the-visible-result)’s source-preservation rule where available.

#### Acceptance criteria

- **W14.1** For a confirmed intermediate result, the message names the change and consequence. For a blocker it gives the last confirmed fact, missing input and responsible party. <a id="w14-1"></a>
- **W14.2** For a decision, give supported options, tradeoff and recommendation. Routine delivery with no user action contains no invented manual steps. Compare actual messages to facts. <a id="w14-2"></a>

[references/writing_style.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md) · [evals/style_cases.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/evals/style_cases.json) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md)

For example, given a checked draft and one open owner decision, “The draft is ready. You still need to decide who can retry a failed batch” is useful only if that choice really is open. For the supplied WEB-09 case the rule is already settled; asking again fails. Inspect the existing session cases first. Add only distinctions the cases cannot demonstrate; keep source-grounded review of wording.

- [ ] 18.2 [W15](#w15--deliver-an-optional-reviewed-decision-with-a-verifiable-receipt) (T025). Verify a finalized decision sentence and link against reviewed bytes. Reject altered wording and validate the legacy receipt under its original format.

### W15 · Deliver an optional reviewed decision with a verifiable receipt

#### Description

The checked handoff can force the owner to reopen the file merely to learn the decision.

#### Expected outcome

The delivery renderer and verifier support a reviewed result or choice on a new compatible path.

Change authored contract, renderer, verifier and affected consumers together. Preserve old messages and version identity; apply the approved D1 convention.

Delivery maintainer · R6/A6. [S07.1](./specs/spec-driven-authoring/spec.md#s07-1) and [F7.1](./specs/spec-driven-authoring/spec.md#f7-1). Requires exact reviewed bytes, current delivery contract and one historical receipt.

#### Acceptance criteria

- **W15.1** Finalize a reviewed document containing a pending choice. The emitted sentence and link match reviewed content. Verification rejects an altered or unreviewed sentence. <a id="w15-1"></a>
- **W15.2** Verify an old receipt using its original format and deliver a document with no substantive action. The old record still validates and the new message adds no unsupported claim. <a id="w15-2"></a>

[contracts/delivery_message.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/delivery_message.json) · [scripts/validate_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/validate_document.py) · [scripts/test_document_delivery.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/test_document_delivery.py)

Use one new handoff and one historical receipt. A renderer pass without the user-visible message is incomplete evidence.

<a id="s13--send-a-routine-update-with-the-appropriate-checks"></a>

## 19. S13 · Send a routine update with the appropriate checks

Deliver a routine update with proof for the claims it makes. [Story criteria](./specs/spec-driven-authoring/spec.md#s13--send-a-routine-update-with-the-appropriate-checks)

- [ ] 19.1 [W27](#w27--limit-routine-message-checks-to-applicable-claims) (T026). Deliver a routine update after source review and identify an applicable naming error through the selected check. Preserve document receipt obligations.

### W27 · Limit routine-message checks to applicable claims

#### Description

The entry asks for a named file even when the check has nothing to assess.

#### Expected outcome

A normal update can be sent after editorial review while applicable naming and absence claims retain their checks.

Change the entry instruction and affected progress evaluation. Protect artifact and checked-message paths. Keep F7’s substantive delivery change separate.

Workflow maintainer · R15/A15. [S13.1](./specs/spec-driven-authoring/spec.md#s13-1) and [F13.1](./specs/spec-driven-authoring/spec.md#f13-1). Use the entry, current checker’s actual predicates and existing progress case.

#### Acceptance criteria

- **W27.1** For an ordinary update with neither a document label nor absence claim, the rule permits direct delivery after source review. On the observed host the public trace shows no named-file style check for that update. <a id="w27-1"></a>
- **W27.2** For an applicable wrong canonical label, the selected check flags the offending text. Preserve the previous artifact and receipt obligations. Reuse their current evidence unless an affected path changed. <a id="w27-2"></a>

[Entry](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md#L15) · [Style checker](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/writing_style_contract.py) · [Progress case](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/evals/style_cases.json#L72)

Ship the rule and affected evaluation in one commit. Claim observed operation only for the host exercised.

<a id="s08--follow-the-portable-entry-without-grader-hints"></a>

## 20. S08 · Follow the portable entry without grader hints

Reach the intended writing route from a normal request on the identified host. [Story criteria](./specs/spec-driven-authoring/spec.md#s08--follow-the-portable-entry-without-grader-hints)

- [ ] 20.1 [W16](#w16--put-task-routing-before-optional-diagram-detail) (T027). Route abbreviated and full-name requests to the same owner. From the portable entry, locate the short-edit path and accessible diagram source.

### W16 · Put task routing before optional diagram detail

#### Description

The entry repeats the catalog relationships and the name parser consumes part of that same file.

#### Expected outcome

Users reach the appropriate rule from the ordinary entry; catalog consumers and diagram readers retain a working route.

Move the complete explanatory relationship view and its accessible source together if needed. Keep the canonical catalog reachable by the naming parser.

Skill-entry maintainer · R7/A7. [S08.1](./specs/spec-driven-authoring/spec.md#s08-1) and [F8.1](./specs/spec-driven-authoring/spec.md#f8-1). Inspect current catalog reader and diagram links before moving text.

#### Acceptance criteria

- **W16.1** Resolve an existing alias and real document name through the usual parser. An ordinary request using “PRD” first and another using “Product Requirements Document” both reach the same reference. The user can alternate forms across turns without being asked to restate the name. Save the resolved reference and reuse the same two inputs across checks. <a id="w16-1"></a>
- **W16.2** From the entry, find the short-edit route and reach the full diagram with title, accessibility information and source. Link checks target the moved content. <a id="w16-2"></a>

[SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md) · [references/writing_style.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md) · [scripts/writing_style_contract.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/writing_style_contract.py) · [scripts/test_document_names.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/test_document_names.py)

Verify the changed navigation and parser once. Word count alone cannot prove the route works for users.

<a id="s21--route-an-improvement-from-its-actual-scope"></a>

## 21. S21 · Route an improvement from its actual scope

Select the smallest governed work record and follow the source of a design constraint. [Story criteria](./specs/spec-driven-authoring/spec.md#s21--route-an-improvement-from-its-actual-scope)

- [ ] 21.1 [W30](#w30--choose-a-task-or-story-for-an-improvement) (T028). Route a single label repair directly and a user capability to a story. Hold an unresolved declared child without inventing ancestry. After W20.

### W30 · Choose a task or story for an improvement

#### Description

An improvement label alone cannot tell the writer whether a story owns the requested work.

#### Expected outcome

The writer can commission an independent improvement, an independent story or a contribution to an existing story without inventing a parent.

Place the routing rules at the existing discovery entry. Link the existing Task and story references. Preserve the declared-child checks and use the existing tracker format.

Workflow maintainer · R11/R17 and A11/A17. [S21.1](./specs/spec-driven-authoring/spec.md#s21-1) and [F21.1](./specs/spec-driven-authoring/spec.md#f21-1). Requires [W20](#w20--resolve-feature-story-and-task-ancestry-before-drafting)’s settled child-parent contract.

#### Acceptance criteria

- **W30.1** Given an authorized change to a single misleading label with its exact replacement, scope and proof, use one Task. Given an independent request that an administrator can recover an unsaved selection, capture the actor, benefit, boundary and observable result in a story or an existing equivalent record. Neither case invents a parent. <a id="w30-1"></a>
- **W30.2** When the same label correction is explicitly assigned to a story criterion, resolve that parent and criterion. A missing parent blocks readiness for the child. Retain the two outputs and the observation that distinguishes them. Reuse A11 for an already demonstrated missing-parent verdict. <a id="w30-2"></a>

[Discovery](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [Task guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [Story guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/user_story.md)

Ship the ordinary writing route, guidance and example in one commit.

- [ ] 21.2 [W31](#w31--choose-a-feature-epic-or-delivery-plan) (T029). Group independently shippable slices under their capability. Verify the mixed-version rollout has ordering and recovery while a contained change can keep steps inline. After W30.

### W31 · Choose a feature, epic or delivery plan

#### Description

A useful grouping and a delivery sequence answer different questions. The writer needs to distinguish them.

#### Expected outcome

A reader knows which capability owns the slices, whether broader coordination needs an epic, and whether delivery needs a separate plan.

Extend W30’s decision table. Reuse a feature for independently acceptable slices of one capability. Use an epic where several slices or capabilities share an initiative, owner and integrated outcome. A project may use either label for the same level. Add a plan only when delivery decisions need an explicit sequence, handoff, compatibility or recovery agreement, or when required by the project.

Planning-guidance maintainer · R2/R17 and A17. [S21.1](./specs/spec-driven-authoring/spec.md#s21-1) and [F21.1](./specs/spec-driven-authoring/spec.md#f21-1). Requires [W30](#w30--choose-a-task-or-story-for-an-improvement). [W29](#w29--publish-the-numbered-document-sequence-in-the-readmemd-file) consumes this route.

#### Acceptance criteria

- **W31.1** Given one independently shippable story, preserve its direct source. Given several usable slices of one capability, group them under the named feature. Add an epic only when the request supplies a broader governed outcome or the project requires one. Retain the chosen records and source for each distinction. <a id="w31-1"></a>
- **W31.2** With the feature and business scope held fixed, compare a single contained delivery with a rollout where old and new readers must coexist. The first can keep steps inline. The second identifies ordering, compatibility proof, owner of the switch and recovery in a delivery plan. A mandated project plan takes precedence. Save the paired result and the governing condition. <a id="w31-2"></a>

[Planning guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md) · [Discovery](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [Skill entry](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md)

Ship the completed decision table, normal route and contrasting examples together. Reuse these choices in the `README.md` review. Stop when the reader can distinguish the cases on the identified candidate.

- [ ] 21.3 [W62](#w62--link-a-design-to-the-records-that-govern-it) (T030). Follow the refund design to the manager-only rule and employee-denial check. A standalone design can cite a complete governing contract directly. After W30.

### W62 · Link a design to the records that govern it

#### Description

The ordinary writing route can distinguish a child task from an independent Task. Its design guidance also needs to show which record supplies a component boundary, governing rule or acceptance criterion when no work-item parent applies.

#### Expected outcome

A developer can open a refund design and recover both the authorization owner and the manager-only rule. A directly authorized design can draw those facts from an existing contract.

Apply the specification’s [linking table and refund example](./specs/spec-driven-authoring/spec.md#link-work-to-its-parent-and-designs-to-their-sources) at the ordinary writing entry. Keep the shared rule at one maintained location and link it from the affected architecture, Low Level Design (LLD), contract, planning and testing guides where a reader needs it. Use the project’s existing parent fields, IDs, section links and backlinks. Preserve any explicit governance and applicable evidence bindings.

Parent: [S21](./specs/spec-driven-authoring/spec.md#s21--route-an-improvement-from-its-actual-scope). Supports [S21.2](./specs/spec-driven-authoring/spec.md#s21-2) and [F21.2](./specs/spec-driven-authoring/spec.md#f21-2) under R17/A17b. Responsible role: writing-guidance maintainer. Reuse [W30](#w30--choose-a-task-or-story-for-an-improvement)’s record-selection rules. [W20](#w20--resolve-feature-story-and-task-ancestry-before-drafting) already owns the missing-parent case. [W59](#w59--carry-a-reviewed-document-into-a-dependent-task) can reuse matching evidence when it exercises its native change consumer.

#### Acceptance criteria

- **W62.1** Given the approved refund rule, a High Level Document (HLD) naming the authorization service and a worked story, child Task and planned denial test, request the Low Level Design (LLD) through the ordinary writing entry. From its links, recover the manager-only rule and the owning component. In the worked records, follow the native parent link to the story’s employee-denial criterion and the planned test to the behavior it checks. One resolvable relationship passes without a manually maintained reverse link. A link to an unrelated service, a copied rule with altered permission, or a claim that the unrun test passed fails. Retain the source sections, output and reader’s observations on the candidate. <a id="w62-1"></a>
- **W62.2** For the same Low Level Design (LLD) request, supply direct authorization and an approved contract that settles the rule and component boundary. Supply no High Level Document (HLD), story or epic and no project rule requiring one. The checked design cites the applicable contract and proceeds without creating or requesting a parent. For a declared child whose governing criterion is unresolved, withhold readiness for that child. Reuse W20’s missing-parent evidence where it covers that boundary. Keep the two dispositions and their reasons. <a id="w62-2"></a>

`SKILL.md`, the owning references in `references/` for architecture, component design, contracts, work items, plans and tests, and the existing linked examples. Start with `references/high_level_document.md` and `references/low_level_design.md`.

Ship the ordinary writing route, maintained guidance and worked example together. Use the two specified scenarios and reuse existing evidence for unchanged behavior.

<a id="s22--write-from-incomplete-project-context"></a>

## 22. S22 · Write from incomplete project context

Compare an undecided permission with the same permission already settled by a source. [Story criteria](./specs/spec-driven-authoring/spec.md#s22--write-from-incomplete-project-context)

- [ ] 22.1 [W32](#w32--detect-an-omitted-material-permission) (T031). Identify the omitted permission in the export brief. An explicitly unresolved draft may pass as a draft. Reject unsupported resolution against an irrelevant source.

### W32 · Detect an omitted material permission

#### Description

A writer can omit the question from the discovery record and still pass the current check.

#### Expected outcome

A complete product document can expose its unresolved permission in a draft and cannot be marked ready until the material topic is settled.

Extend the existing document contract and readiness check on the product route. Derive applicable topics from the format and task scope, independently of the writer’s list. Accept a supported answer, a provisional proposal, an open item or a justified inapplicable topic according to its effect on readiness. Preserve old records at their original version.

Contract maintainer · R18/A18. [S22.1](./specs/spec-driven-authoring/spec.md#s22-1) and [F22.1](./specs/spec-driven-authoring/spec.md#f22-1). Inputs are the existing Product Requirements Document (PRD) contract, declared permission controls and [F22](./specs/spec-driven-authoring/spec.md#f22--resolve-material-gaps-without-needless-questions)’s undecided brief.

#### Acceptance criteria

- **W32.1** On the undecided export brief, omit the material permission topic. Preparation or checked readiness gives the located missing topic and its affected section. A draft naming that open decision can pass as a draft. <a id="w32-1"></a>
- **W32.2** Mark the decision resolved against the undecided brief. A real but irrelevant source ID cannot pass the required semantic review. Retain the passage and verdict alongside the mechanical result. Reuse the existing open-blocker control. <a id="w32-2"></a>

[contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/contracts/documents.json) · [scripts/planning_readiness.py](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/scripts/planning_readiness.py) · [scripts/validate_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/scripts/validate_document.py)

One commit ships the product route, compatible contract, guidance and smallest affected regression.

- [ ] 22.2 [W33](#w33--ask-only-the-question-that-changes-the-requirement) (T032). Ask only for the material ownership decision the sources cannot settle. Resume the affected section after the answer and preserve unrelated work. After W32.

### W33 · Ask only the question that changes the requirement

#### Description

A writer can ask an owner to confirm existing policy or treat a plausible recommendation as authority.

#### Expected outcome

The supported workflow uses existing evidence where decisive, obtains a missing owner answer where necessary and resumes the dependent section.

Connect W32’s decision to the existing discovery and host question routes. Before asking, record the affected criterion, source inspected and unresolved consequence. Bind a returned answer or explicit delegation to the question through a trustworthy host reference where available. Leave unverifiable authority unresolved.

Discovery maintainer · R18/A18. [S22.1](./specs/spec-driven-authoring/spec.md#s22-1) and [F22.1](./specs/spec-driven-authoring/spec.md#f22-1). Requires [W32](#w32--detect-an-omitted-material-permission). Use A18’s same export route for both requests. The public exchange supplies behavioral proof.

#### Acceptance criteria

- **W33.1** For the format-only change, observe zero permission questions and the preserved permission. For self-service with ownership unresolved, observe one targeted ownership question. An unanswered request keeps the dependent section provisional while independent sections proceed. <a id="w33-1"></a>
- **W33.2** Supply the owner’s answer and confirm only the supported scope becomes ready. A single missing owner-held fact can be asked directly. A delegated routine choice proceeds without making the user confirm it. Use existing evidence for unchanged branches. <a id="w33-2"></a>

[workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/workflows/discover.md) · [scripts/planning_readiness.py](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/scripts/planning_readiness.py) · [scripts/validate_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/scripts/validate_document.py)

Ship one connected question-and-resumption route. Share its packet with W28 and the applicable host acceptance check.

- [ ] 22.3 [W34](#w34--apply-discovery-checks-at-the-right-document-scope) (T033). Exercise a material gap through the applicable authoring route. A title-only edit stays lightweight and old receipts retain their original meaning. After W32 and W33.

### W34 · Apply discovery checks at the right document scope

#### Description

A control for complete product documents alone leaves other formats exposed and can add friction to minor edits.

#### Expected outcome

The other applicable authoring routes use the same readiness distinction at a scale appropriate to the requested work.

Map applicability through the existing catalog for complete or substantial authoring, including low-level design, stories and tasks. Keep a title edit or a section with no material decision lightweight. Use shared rules when they are sufficient.

Document-contract maintainer · R18/A18. [S22.1](./specs/spec-driven-authoring/spec.md#s22-1) and [F22.1](./specs/spec-driven-authoring/spec.md#f22-1). Requires [W32](#w32--detect-an-omitted-material-permission) and [W33](#w33--ask-only-the-question-that-changes-the-requirement). Use the actual kind and operation mappings and historical receipt protections.

#### Acceptance criteria

- **W34.1** From actual routing, account for every supported document kind and scope. On the distinct story or Task path exercise one material missing fact through to draft or owner answer. For a source-settled design reuse compatible route evidence. <a id="w34-1"></a>
- **W34.2** A title-only edit with the same topic incurs no discovery questionnaire. Old receipts verify under their own version. Reuse A7/W17 for host differences, or add only the missing A18 observation to that handoff. <a id="w34-2"></a>

[contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/contracts/documents.json) · [references/task.md](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/references/issue.md) · [references/user_story.md](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/references/user_story.md) · [references/low_level_design.md](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/references/low_level_design.md) · [scripts/test_guided_discovery.py](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/scripts/test_guided_discovery.py)

Ship the remaining route coverage and its representative checks. Do not multiply all document kinds by all host and question variants.

<a id="s20--choose-the-next-document-from-the-quick-start"></a>

## 23. S20 · Choose the next document from the quick start

Choose the next document using the public entry and the numbered sequence. [Story criteria](./specs/spec-driven-authoring/spec.md#s20--choose-the-next-document-from-the-quick-start)

- [ ] 23.1 [W42](#w42--explain-spec-driven-writing-at-the-public-entry) (T034). Write the public introduction and feature comparison. A reader can select the right entry, identify the owner and release status, and trace the WEB-06 example.

### W42 · Explain spec-driven writing at the public entry

#### Description

The public `README.md` opens with a catalog and then lists installation requirements. A developer has to infer what a specification changes about the work.

#### Expected outcome

A first-time reader can start with one change request, choose a document and follow one behavior into a task and its planned proof.

Edit the repository-root `README.md` introduction. Put the plain-language introduction first, then installation and one usable example. Link the choices for an idea, an agreed change and a small fix beside that example. Use the current catalog and one existing feature example. W29 owns the detailed chronology.

Documentation maintainer · R16/A16. [S20.2](./specs/spec-driven-authoring/spec.md#s20-2) and [F20.2](./specs/spec-driven-authoring/spec.md#f20-2). Uses existing references and examples; can ship before [W29](#w29--publish-the-numbered-document-sequence-in-the-readmemd-file). Show only entry points available on the candidate.

#### Acceptance criteria

- **W42.1** Starting at the `README.md` title, a reader can identify the purpose, follow installation before the first runnable example and recognize the expected result. From that example, they can choose a brief for an idea, a specification for agreed behavior or a task for one bounded fix. A small authorized fix must route straight to a Task. From the repository-root `README.md`, locate the feature × OpenSpec / SpecDev checkmark table. Compare each row with its owning source and existing release evidence. Each feature has one owner, installed native operations retain precedence, and the release owner checks each advertised capability before publication. Reuse existing feature evidence for this documentation check. <a id="w42-1"></a>
- **W42.2** Follow one worked request through a named requirement, story criterion, a clearly labeled illustrative child Task and its planned observable check. Preserve the source behavior on failure, keep the record types distinct and avoid claiming the check ran. Record the passage, link targets and reader answers on the candidate. One document read covers both criteria. <a id="w42-2"></a>

Repository root `README.md` and its Quick start; [WEB-06](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/spec_driven_development.md#L102-L104) · [the story criterion](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/user_story.md#L20) · [T10](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/test_specification.md#L49) · [historical reader-guide comparison](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/README.md#choose-your-process) · [historical development-method comparison](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/README.md#spec-driven-development).

Suggested opening in the project’s own voice: “SpecDev helps developers and AI agents agree on what a change must do before anyone builds it. Give it a request and the project sources. It turns the agreed behavior into specifications, stories and tasks that say how to check the result.” Example: “If saving a category fails, keep my selection.” WEB-06 requires retaining it. The story expects an error and the selection still in edit mode. An illustrative child Task would implement that failure path. T10 defines its check, including the absence of a success message. Link the real examples and label the illustrative Task. Ship the `README.md` edit in one commit. Use the shared Definition of Done.

<a id="s39--find-instructions-for-a-feature-or-document-type-from-the-index"></a>

## 24. S39 · Find instructions for a feature or document type from the index

Find each released capability and document type from the public index. [Story criteria](./specs/spec-driven-authoring/spec.md#s39--find-instructions-for-a-feature-or-document-type-from-the-index)

- [ ] 24.1 [W54](#w54--publish-the-public-index-with-a-usable-focused-edit-entry) (T035). Publish the working index link to the focused-edit instructions. The destination must explain a title-only request and preserve the description.

### W54 · Publish the public index with a usable focused-edit entry

#### Description

The current `README.md` describes focused edits inside a list of scenarios.

#### Expected outcome

A reader can follow the index to the focused-edit instructions and request a change with a clear boundary.

Link the public index from `README.md`. Point the focused-edit entry at its existing named section and improve that section if the example omits a needed input or result. Link additional released routes as their guidance becomes usable.

Documentation maintainer · R35/A35. [S39.1](./specs/spec-driven-authoring/spec.md#s39-1) and [F39.1](./specs/spec-driven-authoring/spec.md#f39-1). Reuses the existing edit route. [W54](#w54--publish-the-public-index-with-a-usable-focused-edit-entry) was previously proposed under [S34](./specs/spec-driven-authoring/spec.md#s34--find-a-capability-and-follow-a-feature-from-request-to-evidence). Its revised scope is approved here.

#### Acceptance criteria

- **W54.1** From the candidate `README.md`, follow the index link for a focused edit. A direct link to “Make a focused edit” passes when it explains the title-only request, the preserved description and how to inspect the result. A working link to “Review a document” fails for that request. Keep the destination and the text that settles the distinction. <a id="w54-1"></a>
- **W54.2** Open the index links included in this increment. Each guide or named section resolves on the candidate. A missing heading, an empty stub or a planned feature presented as ready fails. Save the candidate and link results. <a id="w54-2"></a>

`README.md` (including its focused-edit section), planned `docs/README.md`, and `references/readme.md`.

Ship the index and its first usable link in one commit.

<a id="s20--choose-the-next-document-from-the-quick-start-continued"></a>

## 25. S20 · Choose the next document from the quick start (continued)

- [ ] 25.1 [W29](#w29--publish-the-numbered-document-sequence-in-the-readmemd-file) (T036). Publish the numbered sequence. A reader can trace one selected change through its native artifacts and route an independent broken-link fix directly. After W20, W30–W31 and the seven linked authoring routes (W04–W06, W09–W10, W12–W13).

### W29 · Publish the numbered document sequence in the `README.md` file

#### Description

New users see isolated prompts before learning what establishes the next document’s inputs.

#### Expected outcome

A contributor can choose what to write next from the `README.md` file alone and follow the link to the owning format.

From Quick start, explain when an ordinary document ends at checked delivery and when a project change uses OpenSpec. Link to the authoring guides for conditional documents and to the installed project route for native outputs. Name each input, result and next consumer on Codex and Claude Code.

Documentation maintainer · R16/A16. [S20.1](./specs/spec-driven-authoring/spec.md#s20-1) and [F20.1](./specs/spec-driven-authoring/spec.md#f20-1). Requires the adopted routes for the seven artifacts, [W20](#w20--resolve-feature-story-and-task-ancestry-before-drafting)’s parent rules, [W30](#w30--choose-a-task-or-story-for-an-improvement)–[W31](#w31--choose-a-feature-epic-or-delivery-plan)’s selection rules and the accepted production order.

#### Acceptance criteria

- **W29.1** From the `README.md`, follow sourced intent through any needed discovery or product definition to the selected OpenSpec change’s proposal, capability requirements and scenarios, design, numbered tasks, then authorized apply and candidate evidence. From a task-list entry, locate the separately owned Task if one exists. Explain where a writing-only request ends and why it creates no companion plan, task file or ticket. <a id="w29-1"></a>
- **W29.2** Using the same section, route an independent broken-link fix directly, with inline scope and proof. Identify why an orphaned child must wait. Locate all seven conditional artifacts at their dependency points and distinguish planned proof from observed results. Retain the `README.md` file passage, resolved links and both reader answers. <a id="w29-2"></a>

[Repository entry](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/README.md#L56) · [Relationship guidance](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md#L116) · [Required production order](./specs/spec-driven-authoring/spec.md#production-order)

One commit ships the section, quick-start link and necessary cross-references. Reuse W20 evidence for runtime routing.

<a id="s23--write-the-intended-artifact-from-a-short-request"></a>

## 26. S23 · Write the intended artifact from a short request

Use the supported shortcut to reach the right format and its checked output. [Story criteria](./specs/spec-driven-authoring/spec.md#s23--write-the-intended-artifact-from-a-short-request)

- [ ] 26.1 [W35](#w35--launch-three-document-types-in-claude-code) (T037). Offer a Claude entry for each released document in the catalog. Observe one checked result, resolve the other names and preserve a foreign command on collision.

<a id="w35--launch-three-document-types-in-claude-code"></a>

### W35 · Start any supported document in Claude Code

#### Description

A bare slash command needs host-level discovery.

#### Expected outcome

Claude Code users can select any released document through its catalog command.

Generate opt-in document shortcuts from the README’s source catalog. For example, `/dr` selects a decision record, `/task` selects one assignment and `/tasks` selects the change’s task list. Preserve explicit edit scope, user-owned commands, and qualified invocation. Each document also resolves through its qualified selector or full name. A shortcut cannot override a native OpenSpec operation or configured artifact in the selected change.

Integration maintainer · R19/A19. [S23.1](./specs/spec-driven-authoring/spec.md#s23-1) and [F23.1](./specs/spec-driven-authoring/spec.md#f23-1). Use the installed skill, existing catalog and current installer.

#### Acceptance criteria

- **W35.1** In a real Claude Code session, dispatch an opted-in shortcut and inspect its brief, selected contract and checked output. Resolve every other released document through the same mapping. Without opt-in the writer still accepts the full name and setup creates none of the shortcuts. <a id="w35-1"></a>
- **W35.2** Supply an occupied name and repeat installation. Existing foreign content remains intact, a working qualified alternative is reported, and removal affects only owned entries. <a id="w35-2"></a>

[scripts/install_skill.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/install_skill.py) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/documents.json)

- [ ] 26.2 [W36](#w36--launch-the-same-documents-in-codex) (T038). Exercise a real Codex entry and inspect the brief, destination and checked result. Resolve the remaining aliases and verify owned-only removal. After W35.

### W36 · Launch the same documents in Codex

#### Description

Codex has a different native skill invocation.

#### Expected outcome

Codex users can reach the same document catalog through the host’s supported invocation and can always use the qualified writer.

Reuse W35’s mapping and writing entry. Document short Codex spellings only where the host discovers them. Verify the actual host spelling. The qualified selector and full document name remain available for each format.

Integration maintainer · R19/A19. [S23.1](./specs/spec-driven-authoring/spec.md#s23-1) and [F23.1](./specs/spec-driven-authoring/spec.md#f23-1). Requires [W35](#w35--launch-three-document-types-in-claude-code)’s common mapping.

#### Acceptance criteria

- **W36.1** Capture a real Codex invocation and checked result for one catalog command. The brief retains its context and literals; the destination and format agree with the existing writer. <a id="w36-1"></a>
- **W36.2** Resolve the other names, preserve the qualified fallback and verify the Codex-specific install/removal boundary. Reuse shared collision checks if their inputs and path are unchanged. <a id="w36-2"></a>

[scripts/install_skill.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/install_skill.py) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/documents.json)

- [ ] 26.3 [W37](#w37--expose-the-authorable-document-catalog) (T039). Compare the complete qualified catalog to its owning contracts. Resolve an occupied shortcut and verify a review request preserves its source. After W35 and W36.

### W37 · Expose the authorable document catalog

#### Description

A user needs to find which names are installed.

#### Expected outcome

A user can request every supported writing format by full name or through the qualified SpecDev selector.

Generate catalog help and document commands from the same source. Expose each planned command as its owning format ships. Preserve full-name requests, aliases, reviews and literals.

Integration maintainer · R19/A19. [S23.1](./specs/spec-driven-authoring/spec.md#s23-1) and [F23.1](./specs/spec-driven-authoring/spec.md#f23-1). Use [W35](#w35--launch-three-document-types-in-claude-code)–[W36](#w36--launch-the-same-documents-in-codex) and the registered output contracts.

#### Acceptance criteria

- **W37.1** Resolve every supported authorable kind and approved variant by qualified selector or full name. Compare the active global writing aliases with the documented opt-ins for released formats, exercise an occupied alias via the qualified fallback, and verify each advertised host spelling against its installed handler. <a id="w37-1"></a>
- **W37.2** A settled behavior request selects the governing specification route. A standalone document request uses its own format. Review of an existing artifact preserves the original and returns the requested findings. Inspect the selected contract and output in each case. <a id="w37-2"></a>

[scripts/install_skill.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/install_skill.py) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/documents.json) · [README.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/README.md)

<a id="s28--release-the-spec-writer-identity-and-legacy-entry"></a>

<a id="s28--release-the-specdev-identity-and-legacy-entry"></a>

## 27. S28 · Release the SpecDev identity and legacy entry

Discover the canonical writer and use its shipped legacy entry. [Story criteria](./specs/spec-driven-authoring/spec.md#s28--release-the-spec-writer-identity-and-legacy-entry)

- [ ] 27.1 [W46](#w46--release-the-specdev-identity-and-legacy-entry) (T047). Discover `specdev` on both hosts and validate the renamed package through Builder. Preserve the `technical-writer` entry and a foreign installation. Requires accepted Skill Builder B5/T50 before changing the live identity.

<a id="w46--release-the-spec-writer-identity-and-legacy-entry"></a>

### W46 · Release the SpecDev identity and legacy entry

#### Description

The shipped name, discovery and examples use Technical Writer. The shipped Builder resolves the legacy dependency identity. A metadata-only rename can break both discovery and document acceptance.

#### Expected outcome

A new installation advertises SpecDev with skill ID `specdev`. The previously shipped `technical-writer` invocation reaches the same writing workflow.

Publish one canonical `specdev` entry and preserve the shipped `technical-writer` invocation, historical receipt identifiers, repository URL and user-owned destinations. Interim planning names carry no compatibility alias.

Skill maintainer · R24/A24. [S28.1](./specs/spec-driven-authoring/spec.md#s28-1) and [F28.1](./specs/spec-driven-authoring/spec.md#f28-1). Requires accepted Skill Builder B5/T50; coordinate host evidence with [W17](#w17--ship-neutral-cross-host-assignments-for-the-connected-handoff) and shortcut ownership with [W35](#w35--launch-three-document-types-in-claude-code)–[W37](#w37--expose-the-authorable-document-catalog).

#### Acceptance criteria

- **W46.1** On Codex and Claude Code, discover the new canonical skill and complete a checked writing request. On the existing-install path, invoke the former name and bind its result to the same writer. Keep one observed invocation per changed host path and reuse W17 when it proves that path. Inspect the release’s public names and link labels, including the existing source labels in `references/task.md`, `references/implementation_plan.md` and `references/spec_driven_development.md`. Check the changed examples and session replies. The sole product name is SpecDev. Use OpenSpec as the technical name for the native change workflow. Retain the source links and required notices. <a id="w46-1"></a>
- **W46.2** On a machine with an unrelated `specdev` installation, setup reports the collision and preserves it. Run one real Builder document validation against the renamed release with the accepted B5 resolver; retain the package revision and receipt. <a id="w46-2"></a>

SKILL.md, README.md and scripts/install_skill.py; Skill Builder scripts/runtime/technical_writer.py. [Evidence](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/install_skill.py)

<a id="s29--start-one-feature-through-an-optional-workflow-extension"></a>

<a id="s29--select-an-openspec-change-in-the-intended-project"></a>

## 28. S29 · Select an OpenSpec change in the intended project

Write the intended change on each host and preserve its sibling and the standalone route. [Story criteria](./specs/spec-driven-authoring/spec.md#s29--start-one-feature-through-an-optional-workflow-extension)

- [ ] 28.1 [W47](#w47--install-the-locked-openspec-cli-and-select-a-change) (T048). Run explicit `/specdev init` with the locked 2.1.1 CLI in the selected checkout. Read native state on both hosts and preserve sibling and standalone work. After W46 and the checked writing route. Supplies the CLI needed by W40.

<a id="w47--start-one-feature-through-an-optional-workflow-extension"></a>

### W47 · Install the locked OpenSpec CLI and select a change

#### Description

Codex and Claude Code need the same OpenSpec runtime and an unambiguous project and change before writing native artifacts.

#### Expected outcome

One SpecDev installation resolves its own locked OpenSpec CLI and uses it in the selected project on either host. An independent document request reaches the same writer without a change.

Ship the two supplied npm files through the normal runtime installer and archive path. Exclude local node_modules from version control and redistribution of source files. Use the private npm manifest and lockfile at `tools/openspec/package.json` and `tools/openspec/package-lock.json` in the distributed writer. Pin `@fission-ai/openspec` exactly to `2.1.1`, require Node `>=22.20.0`, and run `npm ci` in the installed tool directory. Resolve and invoke its local `node_modules/.bin/openspec` with the selected project as working directory. Preserve existing user-wide installations and project-authored artifacts. Expose `/specdev init` through the single SpecDev entry. An explicit initialization request calls the private, pinned OpenSpec binary in the selected target project. For a fresh default, pass `--tools none` so initialization creates no additional host commands. Preserve explicitly requested native initialization options. The user needs no separate `/init` or second tool. Reuse OpenSpec’s schema, CLI instructions, validation and root selection. Do not copy its engine, schemas or generated host workflows into the writer. Expose every installed OpenSpec operation, including explore, verify, update, sync, archive and configured profile or schema operations, through the same SpecDev entry. Discover the available surface from the installed release and effective project/tool configuration. Native OpenSpec owns every overlap. Preserve its inputs, permissions and confirmation boundaries.

Skill maintainer · R25/A25. [S29.1](./specs/spec-driven-authoring/spec.md#s29-1) and [F29.1](./specs/spec-driven-authoring/spec.md#f29-1). Requires W46 and the checked writing route. The live identity transition still requires accepted Skill Builder B5/T50 on the owner’s designated host. W53 maintains releases after this first install.

#### Acceptance criteria

- **W47.1** From a clean local install, confirm the lockfile, executable path, supported Node and reported CLI version. From a fresh authorized target checkout, invoke `/specdev init` and retain the real native invocation, target root and resulting project readback. Verify that default initialization installed no host commands and that explicitly supplied native options reach the CLI. On Codex and Claude Code select the intended refund change and observe native status, artifact instructions and a checked requirement/scenario at the returned path. Record the root, change, writer revision and host entry. A standalone request uses its own contract without creating a change. Reuse matching W46 host evidence. With no local shortcut for `templates`, enter `/specdev templates --schema spec-driven --json`. Capture discovery from the installed CLI and the forwarded argument list; compare the resolved template paths with the pinned executable on the same project. The test must pass with no SpecDev mapping for the verb. Use the same discovery for any other installed OpenSpec command or workflow. <a id="w47-1"></a>
- **W47.2** Repeat setup with an edited project document and a sibling change. Honor explicit root/change selection and preserve edited or foreign files. With materially ambiguous authority or destination, ask only for that choice before writing. With a missing runtime, failed install or missing initialization authority, report the failed prerequisite and the last confirmed state. For an unrecognized verb, check both inventories, return an unknown-command result, and observe no write or shell execution. An installed but disabled native capability reports its native prerequisite. Preserve user-wide settings. A standalone writing request, an error or a missing change must never trigger implicit initialization or fabrication. <a id="w47-2"></a>

`tools/openspec/{package.json,package-lock.json}`, `scripts/install_skill.py`, the writer’s host entries and source-selection guidance. [OpenSpec package manifest](https://github.com/Fission-AI/OpenSpec/blob/v2.1.1/package.json) · [OpenSpec CLI reference](https://openspec.dev/docs/cli)

<a id="s23--write-the-intended-artifact-from-a-short-request-continued"></a>

## 29. S23 · Write the intended artifact from a short request (continued)

- [ ] 29.1 [W40](#w40--write-native-numbered-tasks-for-a-selected-change) (T040). Replace the competing template and per-row Task rules. Inspect native task readback and check that the change produces one design and task list. Both refund status tasks can start together. The dashboard filter waits for the verified API filter. After W47, W35, W11 and W20.

<a id="w40--write-the-feature-task-list-and-its-linked-tasks"></a>

### W40 · Write native numbered tasks for a selected change

#### Description

An implementer needs to see the bounded work, its governing scenario and what establishes completion directly from the selected change.

#### Expected outcome

The change has one native `tasks.md` with usable, ordered numbered checkboxes. A standalone `/task` request can still end with one checked Task.

Use the task artifact returned by the installed OpenSpec schema. Keep each item’s distinct scope, dependency and proof with its native number (for example, `1.1`). Reference an existing Markdown or tracker Task only where it independently owns work or a criterion. Preserve its authority there. Make the first usable result, safe parallel work and each blocking dependency clear in ordinary prose.

At the source, retire the two integration rules in `SKILL.md` that require all document structures to come from the writer and every task row to resolve a separate Task. Update the relevant sections of `references/spec_driven_development.md`, `references/high_level_document.md`, `references/low_level_design.md`, `references/implementation_plan.md` and `references/task.md`. Scope `contracts/documents.json` and its selection and validation in `scripts/document_contracts.py` and `scripts/validate_document.py` to the routes they still own. For a native change, OpenSpec supplies the governing behavior, design and task formats. Put relevant high-level or low-level detail in the one native design, or cite an independently owned source where needed. Retain the supported independent-document routes, legacy reads and historical receipt verification.

Integration maintainer · R19/A19. [S23.1](./specs/spec-driven-authoring/spec.md#s23-1) and [F23.1](./specs/spec-driven-authoring/spec.md#f23-1). Requires W47’s installed native CLI and selected change, W35’s selector, W11’s outcome and W20’s ancestry rules.

#### Acceptance criteria

- **W40.1** For an authorized change with a reviewed proposal, capability delta and applicable design, write the single native task artifact. Each numbered checkbox identifies the governing scenario and the evidence its implementer needs. Where the checkbox owns the work, it suffices on its own. Capture native apply-instructions readback recognizing the items. Do not dispatch implementation. On the release candidate, inspect the affected source rules and consumer selection against the W40 refund packet. Follow the ordinary entry to one native specification per affected capability, one design and one task list. An enforced companion specification, design, plan or Task per checkbox fails. Reuse W62’s independent-design and W15’s original-format receipt evidence where bindings match. For a changed route, check only its missing proof. <a id="w40-1"></a>
- **W40.2** A standalone bounded maintenance request can end with one Task. A declared child with an unresolved governing criterion remains blocked. An unrequested Task, mirror of a native artifact, blanket setup phase or invented test obligation fails. <a id="w40-2"></a>
- **W40.3** Write the two refund stories using the supplied existing Tasks #81–#84. In the first group, dashboard 1.1 and CLI 1.2 can proceed together against the settled read contract. Check the same refund on both surfaces before the filtering story ships. In the second group, API filter 2.1 precedes dashboard 2.2. Demonstrate the filter with mixed refund decisions. Link each independent Task once from its task without copying its criterion. Retain the native list, references and candidate for W48. In the Markdown-only W-PACKET case, resolve the three existing Tasks and keep their exact criteria with their owners. A new tracker, new file per task, missing source, or a duplicate editable definition fails. <a id="w40-3"></a>

`references/task.md`, `references/implementation_plan.md`, the W47 CLI and its task consumer. [Native task template](https://github.com/Fission-AI/OpenSpec/blob/v2.1.1/schemas/spec-driven/templates/tasks.md) · [OpenSpec CLI reference](https://openspec.dev/docs/cli)

Reuse the same authoring output for [W-PACKET and W-CONSUME](../../../plan/test.md#cases).

- [ ] 29.2 [W41](#w41--route-quality-and-consistency-reviews) (T041). Review one vague criterion and one weakened permission. Locate each defect through the appropriate route and preserve candidate and source bytes. After W35, with the relevant review route.

### W41 · Route quality and consistency reviews

#### Description

Requirement quality, cross-document agreement and executed checks answer different questions.

#### Expected outcome

A reviewer can request a requirement checklist or a read-only consistency analysis grounded in the owning documents.

For a native change, use OpenSpec’s available review or verification operation. Add the requested editorial check against the named policy or source. For a standalone document, use the qualified writing review. Preserve the review-only scope in both cases. Use W04 for requirement quality and W03/W21 for traceability. A review may identify an uncovered obligation. Writing and read-only review stop before native apply. When OpenSpec supplies the requested review or verification operation, use it with its native semantics. Add a grounded editorial finding only where it adds value.

Integration maintainer · R19/A19. [S23.1](./specs/spec-driven-authoring/spec.md#s23-1) and [F23.1](./specs/spec-driven-authoring/spec.md#f23-1). Requires the relevant existing route and [W35](#w35--launch-three-document-types-in-claude-code)’s common entry mechanism.

#### Acceptance criteria

- **W41.1** On a packet containing a vague criterion and a task that weakens a sourced permission, the requirements-quality review locates the vague criterion and the consistency review identifies the permission disagreement. Both run through the qualified writing route. <a id="w41-1"></a>
- **W41.2** Inspect before and after the read-only analysis: the reviewed source, tasks and candidate are unchanged. Findings do not claim runtime proof. A request for code implementation routes to the authorized implementing workflow. <a id="w41-2"></a>

[scripts/install_skill.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/install_skill.py) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/documents.json) · [workflows/validation_review.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/workflows/validation_review.md)

<a id="s24--choose-and-continue-one-eligible-document"></a>

## 30. S24 · Choose and continue one eligible document

Identify one useful next document and continue only when requested. [Story criteria](./specs/spec-driven-authoring/spec.md#s24--choose-and-continue-one-eligible-document)

- [ ] 30.1 [W38](#w38--show-the-next-useful-document) (T042). Identify the next useful artifact from current sources. Repeating the request leaves state intact and a completed standalone request needs no extra document. After W20 and W30–W31, with the approved production order.

### W38 · Show the next useful document

#### Description

A static sequence cannot account for current scope and reviewed sources.

#### Expected outcome

Guide and next can explain the right next action without creating a file.

Support starting from a goal or existing artifact. Inspect current initiative and source revisions. For eligible work show document type, specific gap and benefit in one line. If choice matters, identify the decision. Stop at the requested endpoint.

Workflow maintainer · R20/A20. [S24.1](./specs/spec-driven-authoring/spec.md#s24-1) and [F24.1](./specs/spec-driven-authoring/spec.md#f24-1). Requires [W20](#w20--resolve-feature-story-and-task-ancestry-before-drafting), [W30](#w30--choose-a-task-or-story-for-an-improvement)–[W31](#w31--choose-a-feature-epic-or-delivery-plan) and the approved production order.

#### Acceptance criteria

- **W38.1** From a feature with a settled prerequisite, next names one eligible document and the specific benefit in one line; repeated next leaves the initiative unchanged. With two plausible initiatives ask which only if evidence cannot settle it. <a id="w38-1"></a>
- **W38.2** For a blocked child name the missing prerequisite. For a standalone fix with sufficient acceptance say documentation is complete. Recommend no extra document in either case; reuse A17 and A18 evidence. Reuse W40’s refund case to check that next recommends `tasks.md` once its inputs exist and reports document delivery after the checked list. A complete list ends the writing request. A separate task record is needed only when separately owned scope or evidence calls for it. Implementation requires its own authority. <a id="w38-2"></a>

[SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/workflows/discover.md) · [README.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/README.md)

- [ ] 30.2 [W39](#w39--continue-a-checked-document-handoff) (T043). Continue only the selected checked artifact. Recognize prior delivery and reopen affected readiness if its governing revision changes. After W38 and W15.

### W39 · Continue a checked document handoff

#### Description

A suggested next step can duplicate prior work or outlive its source revision.

#### Expected outcome

The owner can continue one document at a time and resume from the current project state.

Use W38’s selected initiative, existing records and the normal writing workflow. Bind any suggested successor included in a checked final message to W15’s reviewed delivery. Respect a single-document request.

Workflow maintainer · R20/A20. [S24.1](./specs/spec-driven-authoring/spec.md#s24-1) and [F24.1](./specs/spec-driven-authoring/spec.md#f24-1). Requires [W38](#w38--show-the-next-useful-document) and [W15](#w15--deliver-an-optional-reviewed-decision-with-a-verifiable-receipt) for checked delivery text.

#### Acceptance criteria

- **W39.1** On continue, write exactly the selected eligible artifact; the source revision, governing criterion and shared terms survive. Resume from the same starting request after delivery and identify the completed result without duplicating it. <a id="w39-1"></a>
- **W39.2** Change a governing revision before continuing. Re-evaluate affected readiness and keep unaffected evidence. A stale handoff or altered checked suggestion fails; when a suggestion cannot be bound to the receipt, keep exact finalization and offer guidance on request. <a id="w39-2"></a>

[SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/workflows/discover.md) · [contracts/delivery_message.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/delivery_message.json) · [scripts/validate_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/validate_document.py)

<a id="s25--guide-selection-of-a-specification-after-delivery"></a>

## 31. S25 · Guide selection of a specification after delivery

Identify which specification governs work after delivery. [Story criteria](./specs/spec-driven-authoring/spec.md#s25--guide-selection-of-a-specification-after-delivery)

- [ ] 31.1 [W43](#w43--guide-selection-of-a-specification-after-delivery) (T044). Use the maintained thirty-day rule over a seven-day snapshot. If authority is removed, identify the conflict before choosing a value. Use W32–W34 when authority is ambiguous.

### W43 · Guide selection of a specification after delivery

#### Description

The behavioral specification guide covers revisions. Decision records cover supersession. Neither tells a writer resuming a delivered feature how to distinguish the maintained behavior source from a frozen delivery snapshot when both are available. R18 classifies evidence, but does not settle this post-delivery choice.

#### Expected outcome

Find which agreement governs the next change.

For OpenSpec, resolve current behavior from `openspec/specs/<capability>/spec.md`, proposed changes from the selected change’s deltas, and past decisions from the archive. For independent documents, use the team’s declared maintenance convention. Link a retained snapshot to its maintained successor or other approved source when known. With no authority for a material difference, preserve both and ask one focused question.

Skill maintainer · R21/A21. [S25.1](./specs/spec-driven-authoring/spec.md#s25-1) and [F25.1](./specs/spec-driven-authoring/spec.md#f25-1). Use existing source and review contracts. Reuse [W32](#w32--detect-an-omitted-material-permission)–[W34](#w34--apply-discovery-checks-at-the-right-document-scope) for ambiguous authority.

#### Acceptance criteria

- **W43.1** At the normal edit entry, supply a frozen launch specification allowing seven days and an approved maintained policy allowing thirty days. Ask to update the feature. The draft cites the maintained rule and labels the seven-day value historical. Both source files remain intact. <a id="w43-1"></a>
- **W43.2** Remove the maintenance decision while keeping two plausible values. The writer identifies the conflict and asks which governs before committing to a value. It can draft unrelated sections. Capture the two draft excerpts or the focused question, source revisions and before/after identities of the inputs. Reuse existing discovery and rewrite evidence for unchanged behavior. <a id="w43-2"></a>

[Writing guidance](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md) · [Affected handoff](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md)

<a id="s26--resolve-constrained-fields-in-task-handoffs"></a>

<a id="32-s26--resolve-constrained-fields-in-issue-handoffs"></a>

## 32. S26 · Resolve constrained fields in Task handoffs

Recover field-specific constraints from the Task the implementer receives. [Story criteria](./specs/spec-driven-authoring/spec.md#s26--resolve-constrained-fields-in-task-handoffs)

- [ ] 32.1 [W44](#w44--resolve-constrained-fields-in-task-handoffs) (T045). Link the requirement to `Return.code`. Reject a task citing `Order.code` and preserve the field’s required semantics. After W40 and W41.

<a id="w44--resolve-constrained-fields-in-issue-handoffs"></a>

### W44 · Resolve constrained fields in Task handoffs

#### Description

The Task guide names requirement-level coverage. The Interface Contract (IC) already distinguishes absence, null and exact field names. The task handoff and its planned consistency review do not explicitly require the owner and field to resolve together when one requirement covers several similarly named fields. A document-level link alone can hide the wrong field.

#### Expected outcome

Trace a field constraint to its precise definition.

When a task implements a constrained field, link its exact owner and field, preserve relevant semantics and flag uncovered or misattributed fields when reviewing the requested scope. Reuse the project’s schema, Interface Contract (IC) or Low Level Design (LLD) as appropriate.

Skill maintainer · R22/A22. [S26.1](./specs/spec-driven-authoring/spec.md#s26-1) and [F26.1](./specs/spec-driven-authoring/spec.md#f26-1). Use existing source and review contracts. Build on [W40](#w40--write-native-numbered-tasks-for-a-selected-change) and [W41](#w41--route-quality-and-consistency-reviews) for generation and read-only analysis.

#### Acceptance criteria

- **W44.1** From a contract where Order.code is optional and Return.code is required, request the task for Return.code. The Task points to the exact Return.code definition and preserves the required behavior. An unambiguous existing field pointer is sufficient. <a id="w44-1"></a>
- **W44.2** Review a variant citing Order.code for the return requirement. The review identifies the Task, wrong field and missing coverage. An unrelated prose-only Task requires no field citations. Retain the authored Task, read-only review excerpt and the unchanged source definitions. Use this same pair at W40/W41 if available. <a id="w44-2"></a>

[Writing guidance](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [Affected handoff](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/interface_contract.md)

<a id="s27--document-the-owner-and-consumer-version-of-a-shared-contract"></a>

## 33. S27 · Document the owner and consumer version of a shared contract

Locate the owner and version of a shared contract from the consumer. [Story criteria](./specs/spec-driven-authoring/spec.md#s27--document-the-owner-and-consumer-version-of-a-shared-contract)

- [ ] 33.1 [W45](#w45--document-the-owner-and-consumer-version-of-a-shared-contract) (T046). Trace the consumer’s v1 pin and proposed v2 change to the contract owner. Keep unknown deployed support separate from mock evidence.

### W45 · Document the owner and consumer version of a shared contract

#### Description

The Interface Contract (IC) guide names the provider, consumers, version and source authority. Its worked handoff does not tell a consumer how to handle a locally edited copy, or how to distinguish a version pinned by the consumer from the version supported by the deployed provider.

#### Expected outcome

Identify the governing contract and supported version.

For independently released components, identify the authoritative source and immutable revision, the consumer’s copy or pin, and the evidence for deployed compatibility when claimed. Resolve disagreements at the owner. Leave deployment support unknown when there is no observation.

Skill maintainer · R23/A23. [S27.1](./specs/spec-driven-authoring/spec.md#s27-1) and [F27.1](./specs/spec-driven-authoring/spec.md#f27-1). Use existing source and review contracts. Use the existing Interface Contract (IC) route.

#### Acceptance criteria

- **W45.1** Given an owner contract at v1, a divergent consumer copy and a proposed v2, ask for an Interface Contract (IC) update. It identifies the source revision, pins the consumer to v1, names the discrepancy and directs the proposed change to the owner. The consumer copy is untouched. <a id="w45-1"></a>
- **W45.2** Provide only the v1 pin and mock results, with no deployed-provider evidence. The handoff distinguishes the agreed version from unknown runtime support. One shared file used by both components requires no synchronized copy. Keep the cited owner revision, consumer pin and resulting compatibility passage; inspect the copy identity. No service deployment or provider test is needed to assess this writing change. <a id="w45-2"></a>

[Writing guidance](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/interface_contract.md) · [Affected handoff](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/interface_contract.md)

<a id="s30--select-eligible-feature-work-and-recover-its-task-criteria"></a>

<a id="s30--select-eligible-numbered-work-from-a-change"></a>

## 34. S30 · Select eligible numbered work from a change

Read native apply inputs, distinguish eligible and blocked tasks, and recover the criterion at its owner. [Story criteria](./specs/spec-driven-authoring/spec.md#s30--select-eligible-feature-work-and-recover-its-task-criteria)

- [ ] 34.1 [W48](#w48--read-eligible-work-from-native-apply-instructions) (T049). Read the selected change’s native apply inputs. Hold the stale or sibling task and release refund task 2.2 only after 2.1 has candidate evidence. After W47, W40 and W44.

<a id="w48--select-eligible-tasks-from-the-feature-list"></a>

### W48 · Read eligible work from native apply instructions

#### Description

Native task progress alone cannot establish an unmet prerequisite, verify a candidate or identify the correct source in a sibling change.

#### Expected outcome

The actual implementing agent can identify eligible numbered work in the selected change and recover the exact requirement, actor, scope, criterion and proof from its owner.

Read native status and `openspec instructions apply --change <id> --json` from W47’s local CLI, then open the listed context files. Follow only the relevant numbered checkbox and its governing scenario, plus an independently owned Task or reviewed input where linked. Inspect the change, source revisions, dependencies and existing evidence before selection. Reading the instructions is a read-only handoff.

Skill maintainer · R26/A26. [S30.1](./specs/spec-driven-authoring/spec.md#s30-1) and [F30.1](./specs/spec-driven-authoring/spec.md#f30-1). Requires [W47](#w47--install-the-locked-openspec-cli-and-select-a-change), [W40](#w40--write-native-numbered-tasks-for-a-selected-change) and [W44](#w44--resolve-constrained-fields-in-task-handoffs). Prove actual consumption before designing more document commands.

#### Acceptance criteria

- **W48.1** From the selected refund change, recover the manager-only rule and employee-denial criterion using the native context and the linked source. Observe what the actual consumer sees. A self-contained task resolves its own scope and proof without another Task. <a id="w48-1"></a>
- **W48.2** Give a sibling change the same task number and revise a referenced criterion after the handoff. The consumer holds the stale task, identifies the selected root, change, task and affected revision, and preserves valid evidence. After reconciliation it uses the current owner. A sibling task or stale dispatch fails. <a id="w48-2"></a>
- **W48.3** Without coaching, the consumer reads W40’s actual output and identifies 1.1 and 1.2 as eligible together. It explains their first usable result, selects 2.1 and holds 2.2 until the API filter works on the candidate. On that evidence it returns to the same list, selects 2.2 and recovers #84’s own criterion. Retain selection readback and prerequisite evidence. No concurrent workers or four new builds are required. In W-PACKET, follow the three existing Tasks to their exact task and story criteria and show how W01 evidence releases W02. Keep this rehearsal read-only. <a id="w48-3"></a>

`references/task.md`, the selected native `tasks.md`, and the context files and instructions returned by the installed CLI. [OpenSpec CLI reference](https://openspec.dev/docs/cli)

Reuse W40’s actual outputs in [W-PACKET and W-CONSUME](../../../plan/test.md#cases).

<a id="s31--verify-and-resume-one-authorized-implementation"></a>

## 35. S31 · Verify and resume one authorized implementation

Resume the same authorized task after interruption without replaying an uncertain effect. [Story criteria](./specs/spec-driven-authoring/spec.md#s31--verify-and-resume-one-authorized-implementation)

- [ ] 35.1 [W49](#w49--apply-one-authorized-native-task) (T050). Dispatch the authorized refund task once. Retain the employee-permission failure and verify denial on the corrected candidate before checking the task. After W48, with authority for the selected provider.

<a id="w49--hand-one-approved-task-to-the-selected-implementation-provider"></a>

### W49 · Apply one authorized native task

#### Description

Reading native instructions and changing a checkbox are different from dispatching a coding session and observing a candidate.

#### Expected outcome

One authorized coding session receives the selected task and returns a verdict bound to the actual candidate and governing criterion.

Use native apply instructions and the selected coding provider in a disposable authorized project. Keep the same task available to the existing Mirai owner in Mirai projects. Preserve its authority boundary. Writing alone ends before dispatch, candidate edits, sync or archive.

Skill maintainer · R27/A27. [S31.1](./specs/spec-driven-authoring/spec.md#s31-1) and [F31.1](./specs/spec-driven-authoring/spec.md#f31-1). Requires [W48](#w48--read-eligible-work-from-native-apply-instructions). Name the authority, provider and candidate in the task. No second provider may act on the same assignment.

#### Acceptance criteria

- **W49.1** With explicit implementation authority, hand the manager-only refund task to the selected coding agent. Record actual dispatch, root, change, criterion revision and observed candidate. A candidate permitting an employee refund fails the denial criterion. Retain that failure. With writing-only authority, stop at the documents without dispatch or project effects. <a id="w49-1"></a>
- **W49.2** Correct the scoped defect and observe employee denial on the new candidate through the relevant entry point. Preserve the original failure. Check off the native task only against accepted evidence. Ordinary completion or a checked box cannot authorize extra scope, another provider, remote publication, synchronization or archiving. <a id="w49-2"></a>

Selected native `tasks.md`, its governing scenarios, W48’s apply inputs and the provider’s actual dispatch and candidate records. [OpenSpec CLI reference](https://openspec.dev/docs/cli)

- [ ] 35.2 [W50](#w50--resume-authorized-apply-from-the-confirmed-boundary) (T051). Recover the original change, task, provider and candidate after interruption. Reconcile uncertainty before action and demonstrate no duplicate effect. After W49.

<a id="w50--resume-the-same-task-after-an-interrupted-run"></a>

### W50 · Resume authorized apply from the confirmed boundary

#### Description

An interrupted apply may leave an unchecked task whose effect already occurred.

#### Expected outcome

The developer can recover the last confirmed execution or evidence boundary without duplicate task effects.

Re-read native status, apply instructions and the selected task in the same change. Match the provider’s original run and candidate evidence, authority, source revision and recorded progress. Leave unresolved external effects uncertain until reconciled.

Skill maintainer · R27/A27. [S31.1](./specs/spec-driven-authoring/spec.md#s31-1) and [F31.1](./specs/spec-driven-authoring/spec.md#f31-1). Requires [W49](#w49--apply-one-authorized-native-task). Reuse its task packet and candidate evidence; interrupt only the boundary needed for this check.

#### Acceptance criteria

- **W50.1** Interrupt the authorized task before its result is recorded. Under the same authority, recover its original root, change, task, provider identity, criterion revision and last observed candidate. Identify and take only the next safe action supported by native and provider evidence. <a id="w50-1"></a>
- **W50.2** If the earlier dispatch might have taken effect, consult authoritative provider or target state. Preserve confirmed work and the original failure. Hold the affected action when uncertainty remains. Capture evidence that resumption caused no duplicate dispatch or write. <a id="w50-2"></a>

Native status and apply instructions for the original change, plus the original provider’s dispatch, candidate and target readback. [OpenSpec CLI reference](https://openspec.dev/docs/cli)

<a id="s32--route-an-idea-or-bug-to-the-right-upstream-workflow"></a>

<a id="s32--document-an-idea-or-a-reported-defect"></a>

## 36. S32 · Document an idea or a reported defect

Finish an idea assessment at a decision or document an observed bug with its bounded repair check. [Story criteria](./specs/spec-driven-authoring/spec.md#s32--route-an-idea-or-bug-to-the-right-upstream-workflow)

- [ ] 36.1 [W51](#w51--end-idea-assessment-at-a-supported-decision) (T052). Turn the idea into a supported recommendation or identify its missing evidence. A recommendation alone must end before task creation or dispatch. After the connected W47–W50 path, with brief and interview routes. Only W51.1 and W51.2 are approved.

### W51 · End idea assessment at a supported decision

#### Description

An unshaped idea needs a writing decision before anyone can determine whether it merits a project change.

#### Expected outcome

An unshaped idea produces a grounded brief, decision recommendation or focused question.

Use SpecDev’s existing brief, interview and Decision Record (DR) routes directly, inside or outside a selected project. Source evidence can settle the choice. Ask only about a material unresolved decision. If the request selects a native explore operation, preserve that native route.

Skill maintainer · R28/A28. [S32.1](./specs/spec-driven-authoring/spec.md#s32-1) and [F32.1](./specs/spec-driven-authoring/spec.md#f32-1). Sequence after the connected W47–W50 path for this delivery. Use the existing brief and interview routes. An idea request does not require an OpenSpec change.

#### Acceptance criteria

- **W51.1** Supply an idea with a consequential evidence gap. The assessment names that gap, identifies who can decide and recommends clarification or stopping. Preserve source and output. <a id="w51-1"></a>
- **W51.2** On a supported decision to proceed, identify the next document and its benefit. A recommendation alone cannot create a task or dispatch an implementation. <a id="w51-2"></a>

`references/decision_record.md`, `workflows/discover.md` and the existing brief and interview routes.

- [ ] 36.2 [W52](#w52--turn-a-reported-defect-into-one-bounded-repair) (T053). Document the observed save defect, expected result and smallest distinguishing check. Keep a suspected cause provisional and leave execution unstarted. After the connected W47–W50 path and W30–W31.

### W52 · Turn a reported defect into one bounded repair

#### Description

A reported defect can support an observed symptom while leaving its cause uncertain.

#### Expected outcome

A defect reaches a source-grounded bug report or independent repair Task with its expected observable check.

Use the writer’s Bug Report (BR) or standalone repair Task. Preserve the project’s established parent rules. Distinguish observation, expected behavior and suspected cause. Route an authorized change through OpenSpec when the user requests that separate action. A matching configured native artifact takes precedence in the selected change.

Skill maintainer · R28/A28. [S32.1](./specs/spec-driven-authoring/spec.md#s32-1) and [F32.1](./specs/spec-driven-authoring/spec.md#f32-1). Sequence after the connected W47–W50 path for this delivery and use W30–W31’s existing scope rules. A request to document a defect needs no initialized change.

#### Acceptance criteria

- **W52.1** Given one observed save failure with a known expected outcome, produce a repair record with the observation, the expected result and the smallest check that distinguishes them. <a id="w52-1"></a>
- **W52.2** Given only a suspected cause, keep it provisional. A bounded independent repair needs no fabricated story or Product Requirements Document (PRD) and writing it cannot authorize execution. <a id="w52-2"></a>

`references/bug_report.md` and `references/task.md`.

<a id="s37--write-the-requested-document-and-pass-it-to-the-right-consumer"></a>

<a id="s37--write-an-independent-document-and-use-its-reviewed-content"></a>

## 37. S37 · Write an independent document and use its reviewed content

Write a standalone document through the catalog. Follow its reviewed constraints when a selected task consumes it. [Story criteria](./specs/spec-driven-authoring/spec.md#s37--write-the-requested-document-and-pass-it-to-the-right-consumer)

- [ ] 37.1 [W58](#w58--reach-the-writing-catalog-without-starting-a-project-change) (T054). Resolve a configured native document ahead of an overlapping writing guide. A standalone tutorial must end with its checked output and no new change. After W35 and W47, with the supported routes on the candidate.

<a id="w58--request-any-supported-writing-format-through-the-workflow"></a>

### W58 · Reach the writing catalog without starting a project change

#### Description

A user requesting an independent document needs its registered writing contract even when the current directory contains OpenSpec changes.

#### Expected outcome

The same SpecDev returns the requested document in its own format on either host, with or without a selected project.

Resolve supported document names and aliases through the qualified selector or full name. Use W35’s document-command mapping and occupied-name fallback. Preserve edit scope, discovery and checked delivery. A standalone Tutorial (TUT), Low Level Design (LLD) or Bug Report (BR) does not require creating or modifying a change. Where the installed schema or workflow supports the requested artifact or operation, use that native contract, including configured extra formats. Use the writer catalog for uncovered writing needs and complementary editorial review only.

Skill maintainer · R33/A33. [S37.1](./specs/spec-driven-authoring/spec.md#s37-1) and [F37.1](./specs/spec-driven-authoring/spec.md#f37-1). Requires the [W47](#w47--install-the-locked-openspec-cli-and-select-a-change) entry, [W35](#w35--launch-three-document-types-in-claude-code) routing, and the approved document routes whose coverage is being accepted. This increment can ship independently of [W59](#w59--carry-a-reviewed-document-into-a-dependent-task).

#### Acceptance criteria

- **W58.1** Compare the candidate’s catalog, contracts and A10a–g with the qualified entry on each supported host. Every advertised kind and alias resolves to its own contract or named variant, and guidance-only entries keep their role. Retain the differences and candidate. This mapping needs no generated document per alias. Exercise a configured schema document whose name overlaps a writing guide. Confirm native instructions, inputs, path and permissions win without creating a second document. Inspect the advertised operation catalog for omissions. <a id="w58-1"></a>
- **W58.2** With verified inputs and a project containing an active change, request a standalone Tutorial (TUT). Retain its checked output and receipt. Confirm no unrelated change artifact, task, global shortcut or provider dispatch was created. Reuse unchanged host-routing evidence from W35–W37 and W47. <a id="w58-2"></a>

`SKILL.md`, `contracts/documents.json`, `references/tutorial.md` and the existing host writing selectors.

- [ ] 37.2 [W59](#w59--carry-a-reviewed-document-into-a-dependent-task) (T055). Read the exact reviewed design revision through the native refund task. A stale permission source must hold only the dependent action. After W58, W48 and W38–W39.

### W59 · Carry a reviewed document into a dependent task

#### Description

A native task may depend on a reviewed document whose permission rule can change independently of the native checkbox.

#### Expected outcome

A task author receives the selected document’s relevant constraint and can see when a source revision needs attention.

Link the reviewed source revision and relevant section only at its actual consumer. Preserve checked-document evidence, scope, prerequisites and authority. Reuse W48’s native task and W38–W39’s handoff. Unrelated tasks retain their existing inputs.

Skill maintainer · R33/A33. [S37.1](./specs/spec-driven-authoring/spec.md#s37-1) and [F37.1](./specs/spec-driven-authoring/spec.md#f37-1). Requires W58, W48 and W38–W39. Use the project’s exact reviewed Low Level Design (LLD), its governing scenario and the native checkbox that consumes it.

#### Acceptance criteria

- **W59.1** Given a reviewed Low Level Design (LLD) limiting refund approval to managers, read its reference through the selected native task. Observe the implementing agent recover the governing scenario, exact design revision and section, and employee-denial criterion. A generic permission check or a sibling change’s design fails. Keep the actual source and consumer readback. <a id="w59-1"></a>
- **W59.2** Revise the linked design with its approval unresolved. The next dependent action identifies the changed source and holds only the affected task. Prior evidence, documents and unrelated work survive. Keep the refusal and revision IDs. Reuse W48 where its evidence exercises this same boundary. <a id="w59-2"></a>

`references/low_level_design.md`, the W38–W39 checked handoff and W48’s selected native task consumer.

- [ ] 37.3 [W63](#w63--use-the-writing-guide-for-native-artifacts) (T060). Write and edit native refund wording through SpecDev. Check the saved text against the permission source and OpenSpec’s selected format. After W58.

### W63 · Use the writing guide for native artifacts

#### Description

A developer should be able to read an OpenSpec proposal, specification, design or task list in the same plain language as other SpecDev documents. The active OpenSpec schema owns the structure of each file.

#### Expected outcome

Through the normal SpecDev entry, the author reads the installed [Writing Style (WS) guide](../../../references/writing_style.md) alongside the native instructions before drafting or editing prose. Apply this to any Markdown artifact the selected schema supplies. Keep project-specific terminology, rules, required syntax and literal values intact. Deliver the reviewed text at its native path. Existing files outside the requested edit stay untouched.

Skill maintainer · R33/A33b · [S37.2](./specs/spec-driven-authoring/spec.md#s37-2). Requires [W58](#w58--request-any-supported-writing-format-through-the-workflow). Reuse W40’s refund source and W58’s custom artifact routing evidence. W17 owns host coverage.

#### Acceptance criteria

- **W63.1** Given the approved manager-only refund rule, use the ordinary authoring entry to draft a native task. From the saved row, a reader must be able to say what to build and who can approve. “Allow only managers to approve refunds” is one acceptable wording. Use the task number assigned in this change. Retain the source, final passage, candidate and native task readback showing its number and state. Inspect the common create/edit route for the four built-in artifact kinds and the configured Markdown kind from W58. <a id="w63-1"></a>
- **W63.2** Request a wording edit to one native refund specification. Its source names the approver but leaves retry authority open. Compare the changed passage with the source and original file. A reader must recover both facts. The required heading, `SHALL`, scenario markers and unrelated text survive. Reject an invented retry owner, a weaker permission or an extra file. Keep the before/after passage and criterion verdict with the candidate. A prompt or structural validation alone cannot establish either wording result. <a id="w63-2"></a>

Use the shared guide and the native authoring route established by W47/W58. Apply the [shared Definition of Done](./design.md#requirement-coverage). Record each verdict and the accepted commit in this Task. Reuse W17’s host observations where they cover the same behavior.

<a id="s33--distribute-and-safely-update-the-versioned-integration"></a>

## 38. S33 · Distribute and safely update the versioned integration

Update and remove the installed integration while preserving project-authored work. [Story criteria](./specs/spec-driven-authoring/spec.md#s33--distribute-and-safely-update-the-versioned-integration)

- [ ] 38.1 [W53](#w53--maintain-and-upgrade-the-locked-openspec-dependency) (T056). Reproduce the locked install and inspect the Dependabot update path. Detect version drift and demonstrate owned-only update and recovery. After W47–W50, W58–W59 and the entries included in the release.

<a id="w53--distribute-and-safely-update-the-versioned-integration"></a>

### W53 · Maintain and upgrade the locked OpenSpec dependency

#### Description

W47 owns the initial locked install. Subsequent releases must detect dependency drift and preserve user-owned content across upgrades and removal.

#### Expected outcome

A maintainer can reproduce the tested runtime, evaluate a proposed upgrade and recover the prior supported installation.

Maintain the private `tools/openspec` npm manifest, lockfile, compatibility evidence and owned host integration. Configure GitHub Dependabot for the npm ecosystem in `/tools/openspec` to propose dependency updates. Review proposals against upstream release notes and the checked consumer contract. Package publication requires separate authority.

Skill maintainer · R29/A29. [S33.1](./specs/spec-driven-authoring/spec.md#s33-1) and [F33.1](./specs/spec-driven-authoring/spec.md#f33-1). Requires W47–W50’s connected path, W58–W59 and the host entries included in the release. Reuse matching evidence on the same candidate.

#### Acceptance criteria

- **W53.1** On a local release candidate, inspect the exact dependency constraint, lockfile resolution, executable path and installed CLI version. Exercise reproducible `npm ci`, declared compatibility and the affected native artifact/apply readback. Inspect Dependabot’s npm directory and a representative proposed manifest/lock change. An update proposal alone cannot advance the accepted pin. <a id="w53-1"></a>
- **W53.2** Detect a manifest/lock/CLI mismatch, unsupported Node or incompatible changed schema/CLI before publishing compatibility. Preview the affected managed paths, preserve edited and foreign content, and demonstrate owned-only update/removal with the prior known-good package and lock available for recovery. Retain version, ownership and before/after evidence. Publishing, automerging or editing a user's global installation requires separate authority. <a id="w53-2"></a>

`tools/openspec/package.json`, `tools/openspec/package-lock.json`, `.github/dependabot.yml`, installer and public usage guidance. [OpenSpec package manifest](https://github.com/Fission-AI/OpenSpec/blob/v2.1.1/package.json) · [OpenSpec CLI reference](https://openspec.dev/docs/cli)

<a id="s39--find-instructions-for-a-feature-or-document-type-from-the-index-continued"></a>

## 39. S39 · Find instructions for a feature or document type from the index (continued)

- [ ] 39.1 [W61](#w61--complete-index-coverage-for-the-existing-release) (T057). Check every released index destination against its intended instructions. Reuse valid focused-edit evidence and verify that review preserves its source. After W54, on the identified release.

### W61 · Complete index coverage for the existing release

#### Description

Creating a new index does not make the existing feature set discoverable.

#### Expected outcome

A reader can locate instructions for each feature and document format that the release already supports.

Compare released entry points, `README.md` scenarios and supported document types against the public index. Link to useful existing sections first. Fill a gap in the owning guidance or write a separate guide when the reader needs a distinct procedure or reference. Keep each correction with its index link.

Documentation maintainer · R35/A35. [S39.1](./specs/spec-driven-authoring/spec.md#s39-1) and [F39.1](./specs/spec-driven-authoring/spec.md#f39-1). Requires [W54](#w54--publish-the-public-index-with-a-usable-focused-edit-entry) and the identified release. Use the existing catalog and index as the record.

#### Acceptance criteria

- **W61.1** Compare the feature index and the document table in `README.md` with the released catalog and output contracts, grouping the six kinds of Task under one document. Show one requirement and a diagram as things a writer can add to a document. Require exactly three document columns: command, linked document title with its abbreviation in parentheses, and plain-language purpose and use. Confirm the core chart has only the four native documents and the expanded chart distinguishes optional paths. Every node must show just the table title and abbreviation. Identify native OpenSpec files. Write the handoff README for the completed release. At publication, include only formats verified for that release. Check that each link opens at reader instructions. Put longer user guides in `docs/` and use the existing specification for requirements. A link into implementation acceptance criteria cannot serve as a usage guide. For a chore Task, a link to “Task types and titles” can pass when it identifies the chore’s inputs and the Task guide gives the expected result. An absent type or a link that leaves the reader searching fails. Retain the candidate, coverage differences and their disposition. <a id="w61-1"></a>
- **W61.2** Reuse W54’s focused-edit evidence and open the review entry on the same release. The review guidance returns located findings and preserves the reviewed document. Distinct, useful headings in one file pass. A broken heading or a link to the focused-edit instructions fails even when the file exists. Retain the observed destinations. Recheck only changed links or uncovered entries. <a id="w61-2"></a>

`README.md`, `SKILL.md`, `contracts/documents.json`, the public index and the existing pages or sections it links to.

Record Met, Failed or Not demonstrated per criterion and identified release. Reuse accepted increments after interruption. Initial verdicts: Not demonstrated.

<a id="s38--explain-the-feature-and-report-the-checked-result"></a>

## 40. S38 · Explain the feature and report the checked result

Read the feature page and session handoff against the approved rule and open decision. [Story criteria](./specs/spec-driven-authoring/spec.md#s38--explain-the-feature-and-report-the-checked-result)

- [x] 40.1 [W60](#w60--teach-feature-page-and-session-wording-in-the-live-style-guide) (T058). Reuse the accepted guide and example. They preserve manager-only approval and the open retry decision without claiming an observed refund. Reuse the accepted guide and example at `d8bf859`.

### W60 · Teach feature-page and session wording in the live style guide

#### Description

The owner authorized an immediate guide edit following the comparative audit.

#### Expected outcome

A writer can use the shared guide for a procedure, reference lookup and checked session reply.

Change the feature-page and session guidance. Preserve existing format ownership, source authority and factual status.

Writing maintainer · R34/A34. [S38.1](./specs/spec-driven-authoring/spec.md#s38-1) and [F38.1](./specs/spec-driven-authoring/spec.md#f38-1). Uses the completed source audit.

#### Acceptance criteria

- **W60.1** Given a manager-only approval rule and an unresolved retry decision, apply the revised guidance to a feature page and a session handoff. The two passages identify the source or decision as appropriate, retain the manager-only rule and leave runtime success unclaimed. Keep the exact guide revision and example comparison. <a id="w60-1"></a>

`references/writing_style.md` and its links to the owning format guides.

Met on d8bf859f0eec178aa34b24e29aef10290e984c3b for the guide and author-applied example. The writing-style contract, repository and layout integrity checks passed. Reuse the [committed guide](https://github.com/fatonsopa/ai-technical-writer/blob/d8bf859f0eec178aa34b24e29aef10290e984c3b/references/writing_style.md#write-a-feature-page-people-can-use). The checkout layout now identifies the owner-requested plan directory. W60 needs no repeat implementation. Cross-host performance is assessed in W17.

<a id="s08--follow-the-portable-entry-without-grader-hints-continued"></a>

## 41. S08 · Follow the portable entry without grader hints (continued)

- [ ] 41.1 [W17](#w17--ship-neutral-cross-host-assignments-for-the-connected-handoff) (T059). Observe the same neutral edit and feature handoff separately on Codex and Claude Code. Record candidate-bound host results and missing visibility. At release, after W16 and the affected increments are integrated on the frozen candidate.

### W17 · Ship neutral cross-host assignments for the connected handoff

#### Description

An assignment that names the expected guide can hide a routing failure.

#### Expected outcome

The evaluator can use ordinary requests and the same rubric to assess each supported host separately.

Deliver portable case inputs, reviewer-only expectations and candidate-bound evidence through the existing host workflow.

Evaluation maintainer · R7/A7. [S08.1](./specs/spec-driven-authoring/spec.md#s08-1) and [F8.1](./specs/spec-driven-authoring/spec.md#f8-1). Requires the integrated candidate and frozen source/host settings; use [W16](#w16--put-task-routing-before-optional-diagram-detail) and affected earlier increments.

#### Acceptance criteria

- **W17.1** Run a routine edit and the integrated feature-to-task handoff on Codex and Claude Code with the same request, sources and rubric. Record actual text, available public source-use evidence and exposed model/settings per host. <a id="w17-1"></a>
- **W17.2** Accept source-grounded equivalent wording. Reject the weakened retry or an invented parent. If routing is unobservable, record that specific limit. A pass on one host cannot satisfy the other. <a id="w17-2"></a>

[config/host_validation.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/config/host_validation.json) · [evals/host_validation_cases.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/evals/host_validation_cases.json) · [scripts/host_coverage.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/host_coverage.py) · [workflows/improve_references.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/improve_references.md)

Stop at the frozen host/case selection. Reuse compatible observations. No full seven-artifact-by-host matrix or performance ranking is required.

## 42. S40 · Install the release and connect a host

A developer can install the release on a second computer, reach the skill from a selected host, and maintain it without disturbing an existing project. [Story acceptance](specs/spec-driven-authoring/spec.md#install-the-release-and-connect-a-host)

- [ ] 42.1 [W64](#w64-task) (T061). Install the GitHub release and connect the chosen host. After W46 and W47 on the identified candidate.

<a id="w64-task"></a>

### W64 · Install the GitHub release and connect the chosen host

#### Description

A user can acquire SpecDev without cloning, check its version, select a host and use the skill. Reuse the existing source installer for the packaged resources. Ship the candidate installer, checksum manifest, launcher, host setup and matching GitHub installation section together.

#### Expected outcome

A developer can follow the [SpecDev installation instructions](../../../README.md#installation) against the packaged candidate from outside its source tree.

#### Scope

Use the supported runtime and existing host destinations. Limit writes to the chosen install and host paths. Preserve local edits and unrelated software. Public distribution requires release-owner authority.

#### Specification

Release maintainer · [S40](specs/spec-driven-authoring/spec.md#install-the-release-and-connect-a-host) · R36/A36a. Requires W46 and W47 on the identified candidate.

#### Acceptance criteria

- **W64.1** From an isolated user directory without a checkout, install the tagged candidate through the documented release installer. Verify `specdev --version` and its PATH location. Use `specdev host init --tools codex` and request a checked independent document, then reuse W47 to demonstrate that project initialization goes through the pinned OpenSpec runtime only on request. Keep the tag, digest, actual host invocation, result and selected path. Inspect that the sibling host and an untouched project were not modified. <a id="w64-1"></a>
- **W64.2** Give the same installer an asset that disagrees with its release checksum. It must identify the mismatch and leave the prior usable version and unrelated files intact. If a prerequisite is absent, report the required prerequisite and recovery. Limit platform claims to release assets with compatible install evidence. <a id="w64-2"></a>

#### Relevant files

Current `scripts/install_skill.py`, `scripts/requirements-lock.txt`, root `README.md` and the candidate’s release entry. Record the candidate, each verdict and its evidence in this Task. [Shared Definition of Done](design.md#requirement-coverage)

- [ ] 42.2 [W65](#w65-task) (T062). Install with npm and refresh the same skill. After W64 and its accepted payload plus W53 for update recovery.

<a id="w65-task"></a>

### W65 · Install with npm and refresh the same skill

#### Description

An npm user can reach the same SpecDev version, update it through npm and remove owned files safely. Use the same host setup and payload as the GitHub installer. Ship the package manifest, CLI entry and npm/update/removal steps in the `README.md` together.

#### Expected outcome

A developer can follow the [SpecDev installation instructions](../../../README.md#installation) against the packaged candidate from outside its source tree.

#### Scope

Use the supported runtime and existing host destinations. Limit writes to the chosen install and host paths. Preserve local edits and unrelated software. Public distribution requires release-owner authority.

#### Specification

Release maintainer · [S40](specs/spec-driven-authoring/spec.md#install-the-release-and-connect-a-host) · R36/A36b. Requires W64 and its accepted payload plus W53 for update recovery.

#### Acceptance criteria

- **W65.1** Install the candidate `npm pack` tarball in an empty npm prefix. Run `specdev --version` from that prefix and `specdev host init --tools claude`. Verify the release revision and actual Claude Code invocation. Repeat setup and observe one owned entry. Reuse the first channel’s product evidence when the payload and interface match. <a id="w65-1"></a>
- **W65.2** With a prior staged version, upgrade through the same channel and run `specdev host update`. Observe the new version at the selected host. Exercise a local edit at a managed destination and retain its content on conflict. Run the documented host removal and channel-specific uninstall in the disposable environment. Check that the other skill, project file and foreign entry survive. Record what each channel owns; reuse equivalent update and removal evidence. <a id="w65-2"></a>

#### Relevant files

Current `scripts/install_skill.py`, `scripts/requirements-lock.txt`, root `README.md` and the candidate’s release entry. Record the candidate, each verdict and its evidence in this Task. [Shared Definition of Done](design.md#requirement-coverage)

## Finish the delivery

Verify the affected story and feature outcomes on the identified candidate. W17 owns the cross-host demonstration. Preserve the accepted W60 proof and record any missing host observation separately. [Coverage and shared Definition of Done](./design.md#requirement-coverage)

## Proposals awaiting owner approval

These proposals have no execution rows. Their original examples and candidate checks remain in the [prior handoff](https://github.com/fatonsopa/ai-technical-writer/blob/8742dce257d21113ed3db3b6e70f6c001253fecc/plan/tasks.md#proposals-awaiting-owner-approval). Revival requires an owner decision and a scope grounded in the installed OpenSpec release.

### Proposed additional criterion for W51

- **W51.3** In one initialized project, follow one idea slug to its decision. With weak evidence or a missing concept, the decision identifies the blocker. Supply the missing sourced fact and recommended concept for the same idea, retain opposing evidence and confidence, and revise only the affected records. A supported go contains a handoff summary without writing a feature spec or starting implementation. For a stop, retain the decisive reason and close the assessment. Use the same records to inspect the verdict boundaries; do not repeat five live stages per verdict. <a id="w51-3"></a>

### W55 · Walk a reader through the default feature path

#### Description

A walkthrough could show how an approved requirement reaches candidate evidence.

#### Expected outcome

A reader traces one manager-only refund from authority through its native change and verified implementation.

If approved, distinguish terminal setup, host actions, standalone writing and review in one worked Tutorial (TUT).

Integration documentation maintainer · R30/A30. [S34.1](./specs/spec-driven-authoring/spec.md#s34-1) and [F34.1](./specs/spec-driven-authoring/spec.md#f34-1).

#### Acceptance criteria

- **W55.1** Follow the refund from the public index to its selected change, governing scenario, design decision, task and candidate evidence. A requested follow-up review can leave tasks untouched. <a id="w55-1"></a>
- **W55.2** For an unresolved permission, locate discovery. For a vague criterion or contradiction, locate the applicable read-only review. Identify the writing-only endpoint and reuse prior evidence. <a id="w55-2"></a>

Proposed quickstart and worked refund example.

### W56 · Explain an installed override from native artifact readback

#### Description

A maintainer may need to distinguish installed guidance from a generated change artifact.

#### Expected outcome

A reader can identify both the installed component and the change artifact at their respective sources.

If approved, identify which inventory and resolution observations the selected OpenSpec release supports. Resolve unsupported assumptions with the proposal owner.

Integration documentation maintainer · R31/A31. [S35.1](./specs/spec-driven-authoring/spec.md#s35-1) and [F35.1](./specs/spec-driven-authoring/spec.md#f35-1).

#### Acceptance criteria

- **W56.1** Using a returned identity where supported, show the effective component source, visible composition and relevant resolution evidence. Registration alone cannot prove execution. <a id="w56-1"></a>
- **W56.2** Distinguish the supported unresolved lookup from locating the native artifact. Retain actual read-only before/after evidence. <a id="w56-2"></a>

Proposed artifact guide, the selected release and installed guidance.

### W57 · Explain how to request a convergence review on a built feature

#### Description

A user may request a follow-up consistency review after scoped implementation.

#### Expected outcome

An operator can distinguish the authorized implementation outcome from a later requested review.

If approved, ground the review in native task and candidate evidence, retaining source ownership, failures and provider authority.

Integration documentation maintainer · R32/A32. [S36.1](./specs/spec-driven-authoring/spec.md#s36-1) and [F36.1](./specs/spec-driven-authoring/spec.md#f36-1).

#### Acceptance criteria

- **W57.1** In the existing refund case, identify the original task, candidate and implementation verdict. Record a separate review only on request. Reuse the original interruption and recovery evidence. <a id="w57-1"></a>
- **W57.2** Reconcile a gap with its governing source before further implementation. Preserve earlier failures, return extra scope to the owner and leave the list alone if the review finds no gap. <a id="w57-2"></a>

Proposed workflow guide and W49/W50 implementation and recovery evidence.
