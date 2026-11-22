# Spec Writer implementation tasks

Read the [specification](./specification.md) for the required behavior and the [implementation plan](./implementation-plan.md) for the delivery approach. In this Markdown handoff, each row links to its Issue immediately below. Expand its details for the scope, acceptance criteria, required proof and parent story criterion. The path in a row points to a starting file. The Issue identifies the full change. The short task number is local to this list. Use the linked Issue ID when handing work to another repository.

Start only after receiving the accepted Skill Builder candidate and its commit. W01 and W03 are the first two eligible Issues. W01 restores the usable fixture. W03 independently checks that assigned work traces back to its requirement. W60 already has accepted evidence. W55–W57 and W51.3 await an owner decision and cannot be selected.

Order expresses delivery preference. An Issue can start when its stated inputs, authority and dependencies are settled. `[P]` identifies the opening pair whose changes can run in parallel. A writing-only request ends at the reviewed list. During an authorized build, open the next eligible Issue, verify it, record the candidate and evidence there, mark its row, then return here. Verify each story at its linked acceptance criteria. [Read-only handoff test](./test.md)

## S01 · Edit a mixed passage without corrupting its fixture

**Demonstrate the story.** Derive the fixture domain from its literal value and recognize the genuine document label. [Story criteria](./specification.md#s01--edit-a-mixed-passage-without-corrupting-its-fixture)

- [ ] T001 [P] [US1] Repair the Websites Review fixture and its consumers. `examples/test_specification.md`. [W01 · W01.1, W01.2](#w01--repair-the-websites-review-fixture-and-its-consumers)

### W01 · Repair the Websites Review fixture and its consumers

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The worked example expanded the key US into a document name.

#### Expected outcome

An administrator can use the published fixture table and its dependent cases again.

#### Scope

Restore the key and all affected references within the worked example. Preserve legitimate document labels.

#### Specification

Parent: [S01](./specification.md#s01--edit-a-mixed-passage-without-corrupting-its-fixture). Supports [S01.1](./specification.md#s01-1) and [F1.1](./specification.md#f1-1). R1/A1. Responsible role: example maintainer. Use the audited fixture and its domain rule.

#### Acceptance criteria

- **W01.1** Read the corrected row and apply the documented lowercase rule. The emitted domain is `__test_wrs-us.co.uk`, and the cited tests select that same row. Save the row and derived domain. <a id="w01-1"></a>
- **W01.2** A genuine document reference in the example retains its agreed meaning. Compare the scoped diff and the consuming cases. <a id="w01-2"></a>

#### Relevant files

[examples/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/test_specification.md) · [references/writing_style.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md)

#### Additional context

One fixture derivation and affected reference lookup suffice. No application deployment is involved.

</details>

## S02 · Commission a task from a reviewed requirement

**Demonstrate the story.** Trace a commissioned task from its authority to the behavior and proof the implementer receives. [Story criteria](./specification.md#s02--commission-a-task-from-a-reviewed-requirement)

- [ ] T002 [P] [US2] Resolve coverage in both directions. `references/implementation_plan.md`. [W03 · W03.1, W03.2](#w03--resolve-coverage-in-both-directions)

### W03 · Resolve coverage in both directions

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A structural pass accepted WEB-999 when it displaced WEB-09.

#### Expected outcome

A plan reviewer can locate a broken citation, an uncovered requirement and unjustified work in the current work record.

#### Scope

Bind explicit references to a declared source. Allow exact sections and documented safeguards. Self-contained documents keep their existing route.

#### Specification

Parent: [S02](./specification.md#s02--commission-a-task-from-a-reviewed-requirement). Supports [S02.1](./specification.md#s02-1) and [F2.1](./specification.md#f2-1). R3/A3. Responsible role: plan maintainer. Use the retained mutation and its valid original.

#### Acceptance criteria

- **W03.1** Submit the correct and displaced rows. Report the consumer row, missing ID, searched revision, lost coverage and correction. An unavailable source is identified separately. <a id="w03-1"></a>
- **W03.2** Inspect the reverse mapping: an unowned criterion remains open; work with a supported safeguard remains eligible. For a project without IDs, an exact section link resolves. In the plan produced from a reviewed feature specification, retain the delivery approach and resolve the covered story criterion at its source. Inspect the ordinary planning output for a second editable story or task definition. <a id="w03-2"></a>

#### Relevant files

[references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md) · [examples/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/implementation_plan.md) · [scripts/check_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/check_document.py) · [scripts/document_contracts.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/document_contracts.py)

#### Additional context

Use the existing comparison; add a mechanical check only for decidable references. Human review assesses meaning. [Actionable diagnostics, 08:55–09:11](https://www.youtube.com/watch?v=O_zcc6Xl12g&t=535s)

</details>
- [ ] T003 [US2] Resolve feature, story and task ancestry before drafting. `workflows/discover.md`. [W20 · W20.1, W20.2](#w20--resolve-feature-story-and-task-ancestry-before-drafting) After W03.

### W20 · Resolve feature, story and task ancestry before drafting

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A task can look ready even when nobody can say which story it supports.

#### Expected outcome

An ordinary request for a child task first resolves the story, its criterion and the feature or epic that owns its outcome.

#### Scope

Teach the order at discovery and issue/story entry. Preserve stable independent IDs on reparenting. An expressly standalone task may establish scope inline.

#### Specification

Parent: [S02](./specification.md#s02--commission-a-task-from-a-reviewed-requirement). Supports [S02.1](./specification.md#s02-1) and [F2.1](./specification.md#f2-1). R2/R11/A2/A11. Responsible role: workflow maintainer. Use [W03](#w03--resolve-coverage-in-both-directions)’s declared references.

#### Acceptance criteria

- **W20.1** Create a child story for an identified epic, then a task for one story criterion. The reader recovers both source revisions and the shared outcome. <a id="w20-1"></a>
- **W20.2** With the story absent, the epic absent, or a stale or contradictory parent, locate the broken edge and withhold dependent readiness. An explicitly independent broken-link fix can proceed with its own source and expected destination. A missing child parent never silently becomes standalone. <a id="w20-2"></a>

#### Relevant files

[workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [references/user_story.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/user_story.md) · [references/issue.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md)

#### Additional context

Use the valid chain and mutations on that chain; test the standalone branch once. No external tracker write.

</details>
- [ ] T004 [US2] Write an epic whose stories prove a usable outcome. `references/user_story.md`. [W11 · W11.1, W11.2](#w11--write-an-epic-whose-stories-prove-a-usable-outcome) After W20. If the scope spans capabilities, use W10 first.

### W11 · Write an epic whose stories prove a usable outcome

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A list of closed tickets can hide an incomplete delivery.

#### Expected outcome

A planner can write a parent epic with linked stories, bounded child issues and its own integrated proof.

#### Scope

Use the existing User Story (US) format for the feature or epic and its stories in the specification, or link their authoritative project records there. Use the Issue format at each task or reference its tracked Issue. Preserve related observations before assigning independent work.

#### Specification

Parent: [S02](./specification.md#s02--commission-a-task-from-a-reviewed-requirement). Supports [S02.1](./specification.md#s02-1) and [F2.1](./specification.md#f2-1). R2/R11/A2/A11. Responsible role: story-guidance maintainer. Use [W20](#w20--resolve-feature-story-and-task-ancestry-before-drafting) and a known feature outcome; use [W10](#w10--map-independent-capabilities-before-specifying-each-one) if scope spans capabilities.

#### Acceptance criteria

- **W11.1** For an initiative with related reports, write a parent epic, a usable child story and a scoped task. The parent exposes non-goals, dependencies, integrated proof and ownership. Each child inherits the right criterion. <a id="w11-1"></a>
- **W11.2** Close all child tasks while withholding the parent’s integrated observation. The epic stays unaccepted. A plausible common cause remains provisional; preserve both original observations. <a id="w11-2"></a>

#### Relevant files

[references/user_story.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/user_story.md) · [references/issue.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md) · [examples/user_story.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/user_story.md)

#### Additional context

Use the same chain used in W20 when compatible. Check the parent outcome once rather than recreating each child test.

</details>

## S01 · Edit a mixed passage without corrupting its fixture (continued)

**Demonstrate the story.** Derive the fixture domain from its literal value and recognize the genuine document label. [Story criteria](./specification.md#s01--edit-a-mixed-passage-without-corrupting-its-fixture)

- [ ] T005 [US1] Protect literal values during ordinary edits. `references/writing_style.md`. [W02 · W02.1, W02.2](#w02--protect-literal-values-during-ordinary-edits) After W01.

### W02 · Protect literal values during ordinary edits

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A naming convention can alter data even when the prose looks better.

#### Expected outcome

An editor can handle a literal, quoted text and a genuine document name in one passage.

#### Scope

Update the owning guidance and its naming check together if the agreed rule changes. Keep consumed full labels and aliases.

#### Specification

Parent: [S01](./specification.md#s01--edit-a-mixed-passage-without-corrupting-its-fixture). Supports [S01.1](./specification.md#s01-1) and [F1.1](./specification.md#f1-1). R1/A1. Responsible role: style maintainer. Use [W01](#w01--repair-the-websites-review-fixture-and-its-consumers). D1 authorizes first-use expansion in authored prose. User requests may use either spelling at any turn.

#### Acceptance criteria

- **W02.1** Edit the mixed passage through the normal route. The fixture and quoted bytes survive while the genuine label matches the adopted rule. Retain the excerpt and checker result. <a id="w02-1"></a>
- **W02.2** Change only prose phrasing to a valid alternative. It remains eligible; deliberately altering the fixture fails the consumer comparison. <a id="w02-2"></a>

#### Relevant files

[references/writing_style.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md) · [scripts/writing_style_contract.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/writing_style_contract.py) · [scripts/test_document_names.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/test_document_names.py)

#### Additional context

Use the W01 fixture as the counterexample. Stop when literal preservation and legitimate editing are both observed.

</details>

## S14 · Use the discovery interview record at its handoff

**Demonstrate the story.** Recover a stakeholder decision and an unresolved question from the interview. [Story criteria](./specification.md#s14--use-the-discovery-interview-record-at-its-handoff)

- [ ] T006 [US14] Author the discovery interview record. `workflows/discover.md`. [W12 · W12.1, W12.2](#w12--author-the-discovery-interview-record)

### W12 · Author the discovery interview record

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

Existing questions can be useful while the next author has no durable restatement to consume.

#### Expected outcome

The requester can ask for the complete interview record; a brief author can cite it.

#### Scope

Extend discovery with the interview output, grounded dialogue, confirmation state and conditional checked delivery. Keep small independent questions together.

#### Specification

Parent: [S14](./specification.md#s14--use-the-discovery-interview-record-at-its-handoff). Supports [S14.1](./specification.md#s14-1) and [F14.1](./specification.md#f14-1). R5/R10/A5/A10a. Responsible role: discovery maintainer. Needs the supplied conversation and explicit decisions, if any.

#### Acceptance criteria

- **W12.1** Given “make reviews faster”, ask which delay matters if evidence does not settle it. Record the answer, source, restatement and open decisions; use actual owner confirmation only. <a id="w12-1"></a>
- **W12.2** With complete sources, proceed without a new interview. If the owner is silent or a latency target is absent, preserve that uncertainty and withhold the invented target from the brief. <a id="w12-2"></a>

#### Relevant files

[workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [scripts/planning_readiness.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/planning_readiness.py) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

#### Additional context

One ambiguous exchange and one complete-input control; reuse the interview as W09 input. Preserve exact owner expressions when they change scope.

</details>

## S05 · Decide whether an opportunity warrants product definition

**Demonstrate the story.** Decide from the sourced brief whether the opportunity warrants product definition. [Story criteria](./specification.md#s05--decide-whether-an-opportunity-warrants-product-definition)

- [ ] T007 [US5] Author a brief from opportunity evidence. `references/product_requirements_document.md`. [W09 · W09.1, W09.2](#w09--author-a-brief-from-opportunity-evidence) Use sourced intent. If intent is missing, use W12 first.

### W09 · Author a brief from opportunity evidence

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

Requiring a full product definition during shaping makes unknowns look settled.

#### Expected outcome

An owner can request and receive a complete brief directly from Technical Writer.

#### Scope

Use a compact product-guidance variant with its own sufficient content and checked delivery. An existing interview is an input when intent needed elicitation.

#### Specification

Parent: [S05](./specification.md#s05--decide-whether-an-opportunity-warrants-product-definition). Supports [S05.1](./specification.md#s05-1) and [F5.1](./specification.md#f5-1). R2/R10/A2/A10b. Responsible role: product-guidance maintainer. Use sourced intent or an interview record from [W12](#w12--author-the-discovery-interview-record).

#### Acceptance criteria

- **W09.1** From a supplied need and an unknown baseline, author problem, beneficiary, desired outcome, non-goals and unresolved choices. Identify the source and any supplied appetite. <a id="w09-1"></a>
- **W09.2** Give the brief to the product author. They can recover the decision and missing baseline. An invented budget, target or approval fails. <a id="w09-2"></a>

#### Relevant files

[references/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/product_requirements_document.md) · [examples/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/product_requirements_document.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

#### Additional context

One brief with an explicit unknown proves the distinction; retain its checked output for downstream use.

</details>

## S04 · Distinguish a prototype from approval to include it

**Demonstrate the story.** Have a reader recover the decision and distinguish prototype evidence from approval. [Story criteria](./specification.md#s04--distinguish-a-prototype-from-approval-to-include-it)

- [ ] T008 [US4] Write the approval opening from the detailed product evidence. `references/product_requirements_document.md`. [W07 · W07.1, W07.2](#w07--write-the-approval-opening-from-the-detailed-product-evidence)

### W07 · Write the approval opening from the detailed product evidence

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The opening currently names the problem without necessarily exposing the choice.

#### Expected outcome

The product author can draft the detail, then present a decision-first opening with sourced tradeoffs.

#### Scope

Extend the product guide and example. Only use this opening where approval matters.

#### Specification

Parent: [S04](./specification.md#s04--distinguish-a-prototype-from-approval-to-include-it). Supports [S04.1](./specification.md#s04-1) and [F4.1](./specification.md#f4-1). R4/A4. Responsible role: product-guidance maintainer. Use prototype evidence and an unresolved inclusion decision.

#### Acceptance criteria

- **W07.1** Read only the opening; identify the affected user, proposed change, excluded behavior and actual choice. Each matches the detail. <a id="w07-1"></a>
- **W07.2** A working prototype remains evidence of feasibility. The opening must leave inclusion pending until the owner decides. <a id="w07-2"></a>

#### Relevant files

[references/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/product_requirements_document.md) · [examples/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/product_requirements_document.md)

#### Additional context

Keep the opening and detailed baseline. No invented cost, budget or new executive summary for a routine issue.

</details>
- [ ] T009 [US4] Judge the reader’s decision against the owning detail. `workflows/improve_references.md`. [W08 · W08.1, W08.2](#w08--judge-the-readers-decision-against-the-owning-detail) After W07.

### W08 · Judge the reader’s decision against the owning detail

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

Finding a real quotation can still support an incorrect answer.

#### Expected outcome

A reviewer can assess an approval opening using a cold reader and source-grounded judgments.

#### Scope

Ship the reader task and review guidance together. Keep expected answers outside the reader’s assignment.

#### Specification

Parent: [S04](./specification.md#s04--distinguish-a-prototype-from-approval-to-include-it). Supports [S04.1](./specification.md#s04-1) and [F4.1](./specification.md#f4-1). R4/A4. Responsible role: evaluation maintainer. Consume [W07](#w07--write-the-approval-opening-from-the-detailed-product-evidence)’s opening and its original detail.

#### Acceptance criteria

- **W08.1** An independent reader given only the opening identifies the four W07 elements. Save the opening, response and comparison to detail. <a id="w08-1"></a>
- **W08.2** Use a wrong decision paired with a genuine quote and a correct alternative phrasing. The rubric rejects the former and accepts the latter for the stated reasons. <a id="w08-2"></a>

#### Relevant files

[workflows/improve_references.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/improve_references.md) · [evals/grades.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/evals/grades.py) · [references/decision_record.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/decision_record.md)

#### Additional context

One cold read for the representative material decision. Reuse it at release; no reader run on every document.

</details>

## S09 · Create a project’s first governed documents from facts

**Demonstrate the story.** Follow an authored product requirement into the downstream specification. [Story criteria](./specification.md#s09--create-a-projects-first-governed-documents-from-facts)

- [ ] T010 [US9] Author a complete product document from project facts. `SKILL.md`. [W18 · W18.1, W18.2](#w18--author-a-complete-product-document-from-project-facts)

### W18 · Author a complete product document from project facts

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The superseded proposal treated an existing Mirai document as a prerequisite.

#### Expected outcome

Using the normal skill, the owner receives a complete Product Requirements Document (PRD) from facts and decisions alone.

#### Scope

Make the existing integration rule actionable in the entry, product guide and worked invocation. Preserve verified terms and owners. No application-specific authoring branch.

#### Specification

Parent: [S09](./specification.md#s09--create-a-projects-first-governed-documents-from-facts). Supports [S09.1](./specification.md#s09-1) and [F9.1](./specification.md#f9-1). R9/A9. Responsible role: product-guidance maintainer. Use Mirai inputs with stable IDs and one open approval; no source document template.

#### Acceptance criteria

- **W18.1** From an empty destination produce the whole product document through Technical Writer. Check its required sections, facts, scope, sources and actual owner status. <a id="w18-1"></a>
- **W18.2** Use a second project’s verified facts through the same route. It gets its own accurate content; a legacy heading or missing application template cannot prevent normal authoring. <a id="w18-2"></a>

#### Relevant files

[SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md) · [references/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/product_requirements_document.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json) · [examples/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/product_requirements_document.md)

#### Additional context

Two project inputs answer portability. Keep the first reviewed artifact for W19. Legacy forms may supply source facts only.

</details>
- [ ] T011 [US9] Hand an authored product requirement to the downstream specification. `references/spec_driven_development.md`. [W19 · W19.1, W19.2](#w19--hand-an-authored-product-requirement-to-the-downstream-specification) After W18.

### W19 · Hand an authored product requirement to the downstream specification

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A complete product document can still lose its authority or meaning at the next boundary.

#### Expected outcome

Technical Writer authors the linked behavioral specification from the W18 artifact and reports compatibility at the actual consumer.

#### Scope

Carry criterion IDs, scope, permission and source revision into the new document. Preserve historical approvals. Surface an incompatible external field at its owner.

#### Specification

Parent: [S09](./specification.md#s09--create-a-projects-first-governed-documents-from-facts). Supports [S09.1](./specification.md#s09-1) and [F9.1](./specification.md#f9-1). R9/R3/A9/A3. Responsible role: integration maintainer. Requires [W18](#w18--author-a-complete-product-document-from-project-facts)’s reviewed output and actual source revision.

#### Acceptance criteria

- **W19.1** From the W18 product document write a complete behavioral specification. A reader resolves the link and recovers the original obligation, exclusion and unresolved decision. Save both reviewed outputs and their bindings. For a multi-task feature, use the existing User Story (US) format in the specification’s Scenarios section, or link its existing authoritative story and criterion there. A reader can recover the outcome and its observable acceptance before seeing a delivery plan. <a id="w19-1"></a>
- **W19.2** Supply a conflicting consumer-format demand. Identify the incompatible field and owning interface. Preserve reviewed bytes and withhold a live-compatibility claim unless the actual consumer accepted them. <a id="w19-2"></a>

#### Relevant files

[references/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md) · [examples/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/spec_driven_development.md) · [workflows/validation_review.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/validation_review.md) · [scripts/validate_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/validate_document.py)

#### Additional context

One linked document and one conflict are sufficient. App migration, signing, external publication and runtime changes require separate authority.

</details>

## S15 · Use the capability map at its handoff

**Demonstrate the story.** Identify independent capabilities and select the next one to specify. [Story criteria](./specification.md#s15--use-the-capability-map-at-its-handoff)

- [ ] T012 [US15] Map independent capabilities before specifying each one. `references/implementation_plan.md`. [W10 · W10.1, W10.2](#w10--map-independent-capabilities-before-specifying-each-one) Requires an identified initiative from a brief or product definition.

### W10 · Map independent capabilities before specifying each one

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A broad initiative can mix separate outcomes and introduce imaginary dependencies.

#### Expected outcome

A spec author can select one stable capability, identify its scope and start its specification in the right order.

#### Scope

Author the capability map as an independently requestable planning artifact. Distinguish capability boundaries from runtime surface names.

#### Specification

Parent: [S15](./specification.md#s15--use-the-capability-map-at-its-handoff). Supports [S15.1](./specification.md#s15-1) and [F15.1](./specification.md#f15-1). R2/R10/A2/A10c. Responsible role: planning-guidance maintainer. Requires an identified initiative; can consume the brief or product definition.

#### Acceptance criteria

- **W10.1** Given two independent capabilities and one dependent capability, write IDs, responsibilities, dependency edges and build order. Either independent starting point is eligible. The child specification cites the selected ID. <a id="w10-1"></a>
- **W10.2** Introduce a cycle. Locate it and withhold the affected order. On a single-capability request proceed directly without manufacturing a map. <a id="w10-2"></a>

#### Relevant files

[references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md) · [references/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

#### Additional context

Reuse one three-capability example. No permutation suite or formal graph service.

</details>

## S16 · Use the research record at its handoff

**Demonstrate the story.** Trace the design choice to a source or an explicit research gap. [Story criteria](./specification.md#s16--use-the-research-record-at-its-handoff)

- [ ] T013 [US16] Author the research record that informs a design choice. `references/decision_record.md`. [W13 · W13.1, W13.2](#w13--author-the-research-record-that-informs-a-design-choice)

### W13 · Author the research record that informs a design choice

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

An issue can paraphrase a retry rule and imply a cause its evidence never established.

#### Expected outcome

A designer can follow the research record to the governing passage and see what decision is still open.

#### Scope

Use the decision guide for alternatives and authority, with an explicit research form for questions, sources, findings and limits. Keep confirmation and supersession with the actual decision owner.

#### Specification

Parent: [S16](./specification.md#s16--use-the-research-record-at-its-handoff). Supports [S16.1](./specification.md#s16-1) and [F16.1](./specification.md#f16-1). R5/R10/A5/A10d. Responsible role: research-guidance maintainer. Requires a material question and the supplied primary source or a recorded access gap.

#### Acceptance criteria

- **W13.1** Read the source for WEB-09, compare it with a paraphrased symptom report, then author the research record. It cites the governing retry condition, alternatives and supported finding. The designer can follow the link. <a id="w13-1"></a>
- **W13.2** Remove the governing passage. The specific gap and its affected conclusion stay open. A recommendation or prototype cannot become an accepted decision. <a id="w13-2"></a>

#### Relevant files

[references/decision_record.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/decision_record.md) · [workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [examples/decision_record.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/decision_record.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

#### Additional context

Use actual supplied content or observed source access. A writer’s assertion of a read alone cannot establish it.

</details>

## S17 · Use the feature map at its handoff

**Demonstrate the story.** Locate the named feature at its actual entry point. [Story criteria](./specification.md#s17--use-the-feature-map-at-its-handoff)

- [ ] T014 [US17] Author a feature map from verified surfaces. `references/test_specification.md`. [W05 · W05.1, W05.2](#w05--author-a-feature-map-from-verified-surfaces)

### W05 · Author a feature map from verified surfaces

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A feature name alone does not tell a verifier how to reach it.

#### Expected outcome

A verifier can use a complete feature map to locate the named screen or operation and its observable result.

#### Scope

Add the authoring route, stable surface references, a worked example and checked output through Technical Writer.

#### Specification

Parent: [S17](./specification.md#s17--use-the-feature-map-at-its-handoff). Supports [S17.1](./specification.md#s17-1) and [F17.1](./specification.md#f17-1). R10/A10e. Responsible role: verification-guidance maintainer. Requires a source exposing at least one actual entry or operation.

#### Acceptance criteria

- **W05.1** From supplied surface evidence, write the map with name, entry, handle/action, source revision and observable end state. A verifier locates the intended surface from the row. <a id="w05-1"></a>
- **W05.2** Withhold a handle or supply an unverified future surface. The artifact marks it unverified or proposed. Launching the app cannot certify that feature. <a id="w05-2"></a>

#### Relevant files

[references/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/test_specification.md) · [examples/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/test_specification.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

#### Additional context

Use one grounded surface and one missing detail. A fabricated selector fails; a real consumer observation may be reused.

</details>

## S18 · Use the critical journeys at its handoff

**Demonstrate the story.** Follow the mapped journey to its observable result. [Story criteria](./specification.md#s18--use-the-critical-journeys-at-its-handoff)

- [ ] T015 [US18] Author a critical journey that consumes the feature map. `references/product_requirements_document.md`. [W06 · W06.1, W06.2](#w06--author-a-critical-journey-that-consumes-the-feature-map) Requires the W05 map or compatible existing evidence.

### W06 · Author a critical journey that consumes the feature map

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

User journeys in the product guide do not establish a connection to a verifiable surface.

#### Expected outcome

A downstream tester receives a standalone journey with resolvable steps, sourced risk and evidence status.

#### Scope

Connect the journey to the map, governing requirement and test reference. Keep the original business need in the product source.

#### Specification

Parent: [S18](./specification.md#s18--use-the-critical-journeys-at-its-handoff). Supports [S18.1](./specification.md#s18-1) and [F18.1](./specification.md#f18-1). R3/R10/A3/A10f. Responsible role: journey-guidance maintainer. Requires a mapped surface from [W05](#w05--author-a-feature-map-from-verified-surfaces) or compatible existing evidence.

#### Acceptance criteria

- **W06.1** Author a journey from W05. Its ID, actor, ordered steps, sourced criticality and end state are present; the tester resolves the screen and check. <a id="w06-1"></a>
- **W06.2** Use an unknown screen or remove the test. Locate the unresolved reference or state that a check is missing. The document cannot report that the journey passed. <a id="w06-2"></a>

#### Relevant files

[references/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/product_requirements_document.md) · [references/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/test_specification.md) · [examples/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/test_specification.md)

#### Additional context

Reuse the map. A declared test path can establish a reference; only an executed observation establishes the result.

</details>

## S03 · Verify one critical journey against its source

**Demonstrate the story.** Follow the approved journey to a user-visible result and distinguish stale evidence. [Story criteria](./specification.md#s03--verify-one-critical-journey-against-its-source)

- [ ] T016 [US3] Preserve conditions and reopen stale evidence. `references/spec_driven_development.md`. [W21 · W21.1, W21.2](#w21--preserve-conditions-and-reopen-stale-evidence) After W03, with a reachable journey such as W06.

### W21 · Preserve conditions and reopen stale evidence

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A valid requirement ID can survive while a permission, limit or operation disappears.

#### Expected outcome

A reviewer can reject a weakened case and invalidate only evidence affected by a changed source.

#### Scope

Extend the connected Websites Review example and review method, including meaningful negative cases, lifecycle verdicts and candidate binding.

#### Specification

Parent: [S03](./specification.md#s03--verify-one-critical-journey-against-its-source). Supports [S03.1](./specification.md#s03-1) and [F3.1](./specification.md#f3-1). R3/R8/A3/A8. Responsible role: verification maintainer. Use [W03](#w03--resolve-coverage-in-both-directions) and a reachable example; [W06](#w06--author-a-critical-journey-that-consumes-the-feature-map) supplies one.

#### Acceptance criteria

- **W21.1** Given T16 and 1,001 rows, the written check distinguishes 500 confirmed, 500 unresolved and one unattempted after response loss. A fresh read precedes any offered retry, and only the administrator chooses it. A request count or automatic retry fails. <a id="w21-1"></a>
- **W21.2** Keep an ID but weaken a material condition; the reviewer rejects it. Change its governing revision and retain the old failure and unrelated valid evidence. Compare before/after verdicts. A valid paraphrase remains eligible. <a id="w21-2"></a>

#### Relevant files

[references/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md) · [references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md) · [examples/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/test_specification.md) · [examples/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/spec_driven_development.md)

#### Additional context

The corresponding change-in-place counterexample starts with an existing value and observes the replacement. Stop at proof about the authored example. Formal verification would establish only the property it models. [Verification scope, 10:50–11:30](https://www.youtube.com/watch?v=O_zcc6Xl12g&t=650s)

</details>

## S19 · Use the requirements-quality checklist at its handoff

**Demonstrate the story.** Identify the requirement that needs clarification before work starts. [Story criteria](./specification.md#s19--use-the-requirements-quality-checklist-at-its-handoff)

- [ ] T017 [US19] Author a requirements-quality checklist for the implementer. `workflows/validation_review.md`. [W04 · W04.1, W04.2](#w04--author-a-requirements-quality-checklist-for-the-implementer) After W03, with a drafted specification.

### W04 · Author a requirements-quality checklist for the implementer

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A completed checklist can be mistaken for successful implementation.

#### Expected outcome

Technical Writer produces a complete reviewer-owned checklist tied to the candidate specification.

#### Scope

Author the standalone form and its checked delivery path. Existing review guidance owns the judgments; avoid a second acceptance registry.

#### Specification

Parent: [S19](./specification.md#s19--use-the-requirements-quality-checklist-at-its-handoff). Supports [S19.1](./specification.md#s19-1) and [F19.1](./specification.md#f19-1). R3/R10/A3/A10g. Responsible role: review-guidance maintainer. Requires a candidate specification and [W03](#w03--resolve-coverage-in-both-directions) references.

#### Acceptance criteria

- **W04.1** Request a requirements-quality checklist on a requirement with ambiguous retry authority. Its row gives the revision, quality question, located evidence, verdict and required correction. <a id="w04-1"></a>
- **W04.2** After clarification, update only that judgment. The implementer can see the resolved rule; no checkmark claims code was built or tested. Retain both verdicts and the checked artifact. <a id="w04-2"></a>

#### Relevant files

[workflows/validation_review.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/validation_review.md) · [references/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

#### Additional context

One reviewed requirement before and after clarification proves this increment. Reuse the same checklist for release evidence.

</details>

## S10 · Read a work item without guessing what success means

**Demonstrate the story.** Have a reader recover the visible outcome and permission from the revised work item. [Story criteria](./specification.md#s10--read-a-work-item-without-guessing-what-success-means)

- [ ] T018 [US10] Replace vague acceptance text with the visible result. `examples/issue.md`. [W22 · W22.1, W22.2](#w22--replace-vague-acceptance-text-with-the-visible-result)

### W22 · Replace vague acceptance text with the visible result

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The issue tells the implementer that uncertain writes are reported honestly. The source says what the administrator sees and who may choose a retry.

#### Expected outcome

The published issue is usable on its own for this criterion. A writer can follow the before/after example in the issue guide when editing another story or task.

#### Scope

Correct the worked clause, keep the surrounding limit and count refresh, and add a short contrast to the owning guide. Keep source terms where a synonym would change an ID, permission or technical meaning. Offer one plain-language rendering without prescribing identical prose.

#### Specification

Parent: [S10](./specification.md#s10--read-a-work-item-without-guessing-what-success-means). Supports [S10.1](./specification.md#s10-1) and [F10.1](./specification.md#f10-1). R12/A12. Responsible role: issue-guidance maintainer. Requires WEB-09–WEB-10 and the existing task and story examples.

#### Acceptance criteria

- **W22.1** Read the original clause and governing source. Edit the issue so the administrator can distinguish confirmed, uncertain and unattempted rows. It says when to stop and preserves the fresh read before offering an optional administrator retry. Save the changed passage with the source. <a id="w22-1"></a>
- **W22.2** Compare the full edited criterion with its neighbors. The 500-ID bound, refresh of confirmed rows and counts and permission survive. A clear existing story about a site leaving Review remains understandable. No invented guarantee or forced stylistic change is needed. <a id="w22-2"></a>

#### Relevant files

[Worked issue](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/issue.md#L19) · [Clear story](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/user_story.md#L18) · [Issue guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [Writing guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md)

#### Additional context

One usable example and its guidance ship in this commit. The first signal is whether the original phrase allows both an informative summary and a generic error. Reuse W21’s requirement evidence.

</details>
- [ ] T019 [US10] Review Markdown by what the reader can recover. `workflows/improve_references.md`. [W23 · W23.1, W23.2](#w23--review-markdown-by-what-the-reader-can-recover) After W22.

### W23 · Review Markdown by what the reader can recover

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A fluent rewrite can omit an essential condition. A mechanical style check cannot tell whether a reader knows when to stop or who owns the next action.

#### Expected outcome

A reviewer can use a source-grounded reader question and a wrong paraphrase to accept a clear work item or return a specific correction.

#### Scope

Ship the review guidance, an ordinary editing request and the grader’s private comparison. Use the existing evaluation route. Keep all valid wordings eligible.

#### Specification

Parent: [S10](./specification.md#s10--read-a-work-item-without-guessing-what-success-means). Supports [S10.1](./specification.md#s10-1) and [F10.1](./specification.md#f10-1). R12/A12. Responsible role: evaluation maintainer. Use the corrected [W22](#w22--replace-vague-acceptance-text-with-the-visible-result) issue and the actual upstream obligations.

#### Acceptance criteria

- **W23.1** Give a reader only the edited issue. Ask what happens after a response is lost and who may retry. Compare the answer with A12 and cite the words carrying each obligation. Missing or incorrect answers identify the exact ambiguity to fix. <a id="w23-1"></a>
- **W23.2** Present two candidate passages with similar tone. One preserves the optional retry and the other requires it. The rubric accepts the first and identifies the changed obligation in the second. A different clear wording receives the same verdict. <a id="w23-2"></a>

#### Relevant files

[Reference review workflow](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/improve_references.md) · [Existing style cases](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/evals/style_cases.json) · [Governing source](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/spec_driven_development.md#L118)

#### Additional context

Share the reader’s packet with W08 if both independently graded results can be observed without revealing either answer. Stop after a supported reader result and the wrong-meaning control. No style benchmark across the entire catalog.

</details>

## S11 · Follow a failed save from story to child Issue

**Demonstrate the story.** Follow the failed-save condition from the story to its child Issue. [Story criteria](./specification.md#s11--follow-a-failed-save-from-story-to-child-issue)

- [ ] T020 [US11] Publish a child Issue for the story’s failed save. `references/issue.md`. [W24 · W24.1, W24.2](#w24--publish-a-child-issue-for-the-storys-failed-save) After W20.

### W24 · Publish a child Issue for the story’s failed save

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The existing Issue shows a whole Feature.

#### Expected outcome

The approved story and Issue references lead to a complete child for one criterion.

#### Scope

Add a worked child under the normal Issue route and link it from the relevant story and guide. Preserve the parent Feature and its incoming links.

#### Specification

Parent: [S11](./specification.md#s11--follow-a-failed-save-from-story-to-child-issue). Supports [S11.1](./specification.md#s11-1) and [F11.1](./specification.md#f11-1). R13/A13. Responsible role: examples maintainer. Use the worked single-site story, WEB-06 and the parent from [W20](#w20--resolve-feature-story-and-task-ancestry-before-drafting).

#### Acceptance criteria

- **W24.1** Follow the normal Issue guide to the child. It identifies the source story, the failed-save criterion and the visible error, retained selection and absence of a success message. The proof observes those effects. <a id="w24-1"></a>
- **W24.2** Follow the child’s parent link and the story’s return link. Both resolve. Comparing scope with the story rejects assignment of bulk editing to the child. Retain the linked examples and reader observation. <a id="w24-2"></a>

#### Relevant files

[Issue guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [Worked story](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/user_story.md) · [Parent Feature](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/issue.md)

#### Additional context

Commit the connected example and links together. Reuse W20’s ancestry check for unchanged edges. Record verdict and evidence against the exact candidate under the shared Definition of Done.

</details>

## S06 · Carry discovery evidence into the next authoring decision

**Demonstrate the story.** Use the source to decide whether one missing answer changes the requirement. [Story criteria](./specification.md#s06--carry-discovery-evidence-into-the-next-authoring-decision)

- [ ] T021 [US6] Ask the question that changes the requirement. `workflows/discover.md`. [W28 · W28.1, W28.2](#w28--ask-the-question-that-changes-the-requirement)

### W28 · Ask the question that changes the requirement

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A generic interview can anchor a decision the owner has yet to make.

#### Expected outcome

The discovery guide shows how to follow an open answer or proceed with complete evidence.

#### Scope

Ship one contrast at the existing discovery entry. Keep capture of a requested interview record in W12.

#### Specification

Parent: [S06](./specification.md#s06--carry-discovery-evidence-into-the-next-authoring-decision). Supports [S06.1](./specification.md#s06-1) and [F6.1](./specification.md#f6-1). R5/A5. Responsible role: discovery maintainer. Use the documented ambiguous review-delay request and an otherwise identical request with the delay already identified.

#### Acceptance criteria

- **W28.1** With the delay unspecified, the first question can distinguish two delays. Given the owner’s answer, the next criterion uses the identified delay without inventing a target. Save the exchange and criterion. <a id="w28-1"></a>
- **W28.2** With the delay and acceptance already supplied, the writer proceeds without asking again. Inspect the resulting criterion and stop. <a id="w28-2"></a>

#### Relevant files

[Discovery](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [Interview-me](https://github.com/addyosmani/agent-skills/blob/8c99fa36d90068c82d547f7c12a9d67a3e95f4ee/skills/interview-me/SKILL.md#L53-L90) · [Grilling](https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/productivity/grilling/SKILL.md)

#### Additional context

One commit ships the guidance and its worked contrast. Record verdict and evidence against the exact candidate under the shared Definition of Done.

</details>

## S12 · Act on a handoff and resolve a misunderstood role

**Demonstrate the story.** Use the handoff to perform the necessary manual action and identify who answers the next question. [Story criteria](./specification.md#s12--act-on-a-handoff-and-resolve-a-misunderstood-role)

- [ ] T022 [US12] Guide the owner through one necessary manual action. `references/writing_style.md`. [W25 · W25.1, W25.2](#w25--guide-the-owner-through-one-necessary-manual-action)

### W25 · Guide the owner through one necessary manual action

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A link that works in the writer’s checkout may fail in the owner’s starting state.

#### Expected outcome

A user can perform an authorized read from their actual starting point and recognize success or a wrong reference.

#### Scope

Add the Session replies section to the shared style guide and link it from the skill entry. Reuse existing how-to instructions. Apply to an ordinary reply outside checked finalization.

#### Specification

Parent: [S12](./specification.md#s12--act-on-a-handoff-and-resolve-a-misunderstood-role). Supports [S12.1](./specification.md#s12-1) and [F12.1](./specification.md#f12-1). R14/A14. Responsible role: style maintainer. Use a supplied read-only handoff with known location, available reference, expected title and a known missing-reference response.

#### Acceptance criteria

- **W25.1** Given the owner must open the supplied document, the reply names the starting location, exact read action, expected title and safe next action for the supplied failure. A reader can follow it from that starting state. <a id="w25-1"></a>
- **W25.2** If the owner already has the document and only asks what it says, answer directly. Supplying redundant commands, guessing a path or asking the owner to make a write fails. Retain the replies and the source. <a id="w25-2"></a>

#### Relevant files

[Style guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md) · [Procedure guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/how_to_guide.md) · [Mirai session guide](https://github.com/jetmirhaxhisefa/mirai/blob/ddd183a3728d3fdd9f776755de47d4d314c8925c/registry/skills/mirai-write/guides/session.md)

#### Additional context

Ship one portable route and its usable example in one commit. Record verdict and evidence against the exact candidate under the shared Definition of Done.

</details>
- [ ] T023 [US12] Clarify who acts when an explanation was misunderstood. `references/writing_style.md`. [W26 · W26.1, W26.2](#w26--clarify-who-acts-when-an-explanation-was-misunderstood) After W25.

### W26 · Clarify who acts when an explanation was misunderstood

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The owner can hear “reader” as an assignment to do the work personally.

#### Expected outcome

The owner can tell who answers, who decides and what remains open.

#### Scope

Extend the same session section with one clarification example. Keep supported permission and role names.

#### Specification

Parent: [S12](./specification.md#s12--act-on-a-handoff-and-resolve-a-misunderstood-role). Supports [S12.1](./specification.md#s12-1) and [F12.1](./specification.md#f12-1). R14/A14. Responsible role: style maintainer. Requires [W25](#w25--guide-the-owner-through-one-necessary-manual-action)’s section and a supplied choice about who answers reader questions.

#### Acceptance criteria

- **W26.1** When the owner asks whether they must write the reader answers, the first sentence resolves the misunderstanding from the supplied source. A different concrete example explains the decision still theirs. Save the reply and source passage. <a id="w26-1"></a>
- **W26.2** If the source leaves the answering role open, the reply identifies the open choice. Repeating the original unexplained role, assigning the owner new work or promising a check that never ran fails. <a id="w26-2"></a>

#### Relevant files

[Style guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md) · [Mirai session guide](https://github.com/jetmirhaxhisefa/mirai/blob/ddd183a3728d3fdd9f776755de47d4d314c8925c/registry/skills/mirai-write/guides/session.md#L77-L111)

#### Additional context

Ship the repair example and its acceptance comparison. Reuse W25’s route. Record verdict and evidence against the exact candidate under the shared Definition of Done.

</details>

## S07 · Receive the right next action and a checked result

**Demonstrate the story.** Read the checked handoff and identify the result, blocker or decision. [Story criteria](./specification.md#s07--receive-the-right-next-action-and-a-checked-result)

- [ ] T024 [US7] Write progress, decision and blocker messages from evidence. `references/writing_style.md`. [W14 · W14.1, W14.2](#w14--write-progress-decision-and-blocker-messages-from-evidence) Reuse W22 where available.

### W14 · Write progress, decision and blocker messages from evidence

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A generic status can leave the user unsure what to do.

#### Expected outcome

The writer gives a concise public update that matches the observed state and any required action.

#### Scope

Ship contrasting session examples through shared style guidance. F13 owns the scope of the file-based check.

#### Specification

Parent: [S07](./specification.md#s07--receive-the-right-next-action-and-a-checked-result). Supports [S07.1](./specification.md#s07-1) and [F7.1](./specification.md#f7-1). R6/A6. Responsible role: style maintainer. Use a confirmed result, unresolved choice and genuine external blocker. Use [W22](#w22--replace-vague-acceptance-text-with-the-visible-result)’s source-preservation rule where available.

#### Acceptance criteria

- **W14.1** For a confirmed intermediate result, the message names the change and consequence. For a blocker it gives the last confirmed fact, missing input and responsible party. <a id="w14-1"></a>
- **W14.2** For a decision, give supported options, tradeoff and recommendation. Routine delivery with no user action contains no invented manual steps. Compare actual messages to facts. <a id="w14-2"></a>

#### Relevant files

[references/writing_style.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md) · [evals/style_cases.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/evals/style_cases.json) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md)

#### Additional context

For example, given a checked draft and one open owner decision, “The draft is ready. You still need to decide who can retry a failed batch” is useful only if that choice really is open. For the supplied WEB-09 case the rule is already settled; asking again fails. Inspect the existing session cases first. Add only distinctions the cases cannot demonstrate; keep source-grounded review of wording.

</details>
- [ ] T025 [US7] Deliver an optional reviewed decision with a verifiable receipt. `contracts/delivery_message.json`. [W15 · W15.1, W15.2](#w15--deliver-an-optional-reviewed-decision-with-a-verifiable-receipt)

### W15 · Deliver an optional reviewed decision with a verifiable receipt

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The checked handoff can force the owner to reopen the file merely to learn the decision.

#### Expected outcome

The delivery renderer and verifier support a reviewed result or choice on a new compatible path.

#### Scope

Change authored contract, renderer, verifier and affected consumers together. Preserve old messages and version identity; apply the approved D1 convention.

#### Specification

Parent: [S07](./specification.md#s07--receive-the-right-next-action-and-a-checked-result). Supports [S07.1](./specification.md#s07-1) and [F7.1](./specification.md#f7-1). R6/A6. Responsible role: delivery maintainer. Requires exact reviewed bytes, current delivery contract and one historical receipt.

#### Acceptance criteria

- **W15.1** Finalize a reviewed document containing a pending choice. The emitted sentence and link match reviewed content. Verification rejects an altered or unreviewed sentence. <a id="w15-1"></a>
- **W15.2** Verify an old receipt using its original format and deliver a document with no substantive action. The old record still validates and the new message adds no unsupported claim. <a id="w15-2"></a>

#### Relevant files

[contracts/delivery_message.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/delivery_message.json) · [scripts/validate_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/validate_document.py) · [scripts/test_document_delivery.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/test_document_delivery.py)

#### Additional context

Use one new handoff and one historical receipt. A renderer pass without the user-visible message is incomplete evidence.

</details>

## S13 · Send a routine update with the appropriate checks

**Demonstrate the story.** Deliver a routine update with proof for the claims it makes. [Story criteria](./specification.md#s13--send-a-routine-update-with-the-appropriate-checks)

- [ ] T026 [US13] Limit routine-message checks to applicable claims. `SKILL.md`. [W27 · W27.1, W27.2](#w27--limit-routine-message-checks-to-applicable-claims)

### W27 · Limit routine-message checks to applicable claims

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The entry asks for a named file even when the check has nothing to assess.

#### Expected outcome

A normal update can be sent after editorial review while applicable naming and absence claims retain their checks.

#### Scope

Change the entry instruction and affected progress evaluation. Protect artifact and checked-message paths. Keep F7’s substantive delivery change separate.

#### Specification

Parent: [S13](./specification.md#s13--send-a-routine-update-with-the-appropriate-checks). Supports [S13.1](./specification.md#s13-1) and [F13.1](./specification.md#f13-1). R15/A15. Responsible role: workflow maintainer. Use the entry, current checker’s actual predicates and existing progress case.

#### Acceptance criteria

- **W27.1** For an ordinary update with neither a document label nor absence claim, the rule permits direct delivery after source review. On the observed host the public trace shows no named-file style check for that update. <a id="w27-1"></a>
- **W27.2** For an applicable wrong canonical label, the selected check flags the offending text. Preserve the previous artifact and receipt obligations. Reuse their current evidence unless an affected path changed. <a id="w27-2"></a>

#### Relevant files

[Entry](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md#L15) · [Style checker](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/writing_style_contract.py) · [Progress case](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/evals/style_cases.json#L72)

#### Additional context

Ship the rule and affected evaluation in one commit. Claim observed operation only for the host exercised. Record verdict and evidence against the exact candidate under the shared Definition of Done.

</details>

## S08 · Follow the portable entry without grader hints

**Demonstrate the story.** Reach the intended writing route from a normal request on the identified host. [Story criteria](./specification.md#s08--follow-the-portable-entry-without-grader-hints)

- [ ] T027 [US8] Put task routing before optional diagram detail. `SKILL.md`. [W16 · W16.1, W16.2](#w16--put-task-routing-before-optional-diagram-detail)

### W16 · Put task routing before optional diagram detail

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The entry repeats the catalog relationships and the name parser consumes part of that same file.

#### Expected outcome

Users reach the appropriate rule from the ordinary entry; catalog consumers and diagram readers retain a working route.

#### Scope

Move the complete explanatory relationship view and its accessible source together if needed. Keep the canonical catalog reachable by the naming parser.

#### Specification

Parent: [S08](./specification.md#s08--follow-the-portable-entry-without-grader-hints). Supports [S08.1](./specification.md#s08-1) and [F8.1](./specification.md#f8-1). R7/A7. Responsible role: skill-entry maintainer. Inspect current catalog reader and diagram links before moving text.

#### Acceptance criteria

- **W16.1** Resolve an existing alias and real document name through the usual parser. An ordinary request using “PRD” first and another using “Product Requirements Document” both reach the same reference. The user can alternate forms across turns without being asked to restate the name. Save the resolved reference and reuse the same two inputs across checks. <a id="w16-1"></a>
- **W16.2** From the entry, find the short-edit route and reach the full diagram with title, accessibility information and source. Link checks target the moved content. <a id="w16-2"></a>

#### Relevant files

[SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md) · [references/writing_style.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md) · [scripts/writing_style_contract.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/writing_style_contract.py) · [scripts/test_document_names.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/test_document_names.py)

#### Additional context

Verify the changed navigation and parser once. Word count alone cannot prove the route works for users.

</details>

## S21 · Route an improvement from its actual scope

**Demonstrate the story.** Select the smallest governed work record and follow the source of a design constraint. [Story criteria](./specification.md#s21--route-an-improvement-from-its-actual-scope)

- [ ] T028 [US21] Choose a task or story for an improvement. `workflows/discover.md`. [W30 · W30.1, W30.2](#w30--choose-a-task-or-story-for-an-improvement) After W20.

### W30 · Choose a task or story for an improvement

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

An improvement label alone cannot tell the writer whether a story owns the requested work.

#### Expected outcome

The writer can commission an independent improvement, an independent story or a contribution to an existing story without inventing a parent.

#### Scope

Place the routing rules at the existing discovery entry. Link the existing Issue and story references. Preserve the declared-child checks and use the existing tracker format.

#### Specification

Parent: [S21](./specification.md#s21--route-an-improvement-from-its-actual-scope). Supports [S21.1](./specification.md#s21-1) and [F21.1](./specification.md#f21-1). R11/R17 and A11/A17. Responsible role: workflow maintainer. Requires [W20](#w20--resolve-feature-story-and-task-ancestry-before-drafting)’s settled child-parent contract.

#### Acceptance criteria

- **W30.1** Given an authorized change to a single misleading label with its exact replacement, scope and proof, use one Issue. Given an independent request that an administrator can recover an unsaved selection, capture the actor, benefit, boundary and observable result in a story or an existing equivalent record. Neither case invents a parent. <a id="w30-1"></a>
- **W30.2** When the same label correction is explicitly assigned to a story criterion, resolve that parent and criterion. A missing parent blocks readiness for the child. Retain the two outputs and the observation that distinguishes them. Reuse A11 for an already demonstrated missing-parent verdict. <a id="w30-2"></a>

#### Relevant files

[Discovery](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [Issue guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [Story guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/user_story.md)

#### Additional context

Ship the ordinary writing route, guidance and example in one commit. Record the scoped verdict and candidate under the shared Definition of Done.

</details>
- [ ] T029 [US21] Choose a feature, epic or delivery plan. `references/implementation_plan.md`. [W31 · W31.1, W31.2](#w31--choose-a-feature-epic-or-delivery-plan) After W30.

### W31 · Choose a feature, epic or delivery plan

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A useful grouping and a delivery sequence answer different questions. The writer needs to distinguish them.

#### Expected outcome

A reader knows which capability owns the slices, whether broader coordination needs an epic, and whether delivery needs a separate plan.

#### Scope

Extend W30’s decision table. Reuse a feature for independently acceptable slices of one capability. Use an epic where several slices or capabilities share an initiative, owner and integrated outcome. A project may use either label for the same level. Add a plan only when delivery decisions need an explicit sequence, handoff, compatibility or recovery agreement, or when required by the project.

#### Specification

Parent: [S21](./specification.md#s21--route-an-improvement-from-its-actual-scope). Supports [S21.1](./specification.md#s21-1) and [F21.1](./specification.md#f21-1). R2/R17 and A17. Responsible role: planning-guidance maintainer. Requires [W30](#w30--choose-a-task-or-story-for-an-improvement). [W29](#w29--publish-the-numbered-document-sequence-in-the-readmemd-file) consumes this route.

#### Acceptance criteria

- **W31.1** Given one independently shippable story, preserve its direct source. Given several usable slices of one capability, group them under the named feature. Add an epic only when the request supplies a broader governed outcome or the project requires one. Retain the chosen records and source for each distinction. <a id="w31-1"></a>
- **W31.2** With the feature and business scope held fixed, compare a single contained delivery with a rollout where old and new readers must coexist. The first can keep steps inline. The second identifies ordering, compatibility proof, owner of the switch and recovery in a delivery plan. A mandated project plan takes precedence. Save the paired result and the governing condition. <a id="w31-2"></a>

#### Relevant files

[Planning guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md) · [Discovery](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [Skill entry](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md)

#### Additional context

Ship the completed decision table, normal route and contrasting examples together. Reuse these choices in the README review. Stop when the reader can distinguish the cases on the identified candidate.

</details>
- [ ] T030 [US21] Link a design to the records that govern it. `references/high_level_document.md`. [W62 · W62.1, W62.2](#w62--link-a-design-to-the-records-that-govern-it) After W30.

### W62 · Link a design to the records that govern it

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The ordinary writing route can distinguish a child task from an independent Issue. Its design guidance also needs to show which record supplies a component boundary, governing rule or acceptance criterion when no work-item parent applies.

#### Expected outcome

A developer can open a refund design and recover both the authorization owner and the manager-only rule. A directly authorized design can draw those facts from an existing contract.

#### Scope

Apply the specification’s [linking table and refund example](./specification.md#link-work-to-its-parent-and-designs-to-their-sources) at the ordinary writing entry. Keep the shared rule at one maintained location and link it from the affected architecture, Low Level Design (LLD), contract, planning and testing guides where a reader needs it. Use the project’s existing parent fields, IDs, section links and backlinks. Preserve any explicit governance and applicable evidence bindings.

#### Specification

Parent: [S21](./specification.md#s21--route-an-improvement-from-its-actual-scope). Supports [S21.2](./specification.md#s21-2) and [F21.2](./specification.md#f21-2) under R17/A17b. Responsible role: writing-guidance maintainer. Reuse [W30](#w30--choose-a-task-or-story-for-an-improvement)’s record-selection rules. [W20](#w20--resolve-feature-story-and-task-ancestry-before-drafting) already owns the missing-parent case. [W59](#w59--carry-a-reviewed-document-into-a-dependent-task) can reuse matching evidence when it exercises its optional workflow consumer.

#### Acceptance criteria

- **W62.1** Given the approved refund rule, an HLD naming the authorization service and a worked story, child Issue and planned denial test, request the LLD through the ordinary writing entry. From its links, recover the manager-only rule and the owning component. In the worked records, follow the native parent link to the story’s employee-denial criterion and the planned test to the behavior it checks. One resolvable relationship passes without a manually maintained reverse link. A link to an unrelated service, a copied rule with altered permission, or a claim that the unrun test passed fails. Retain the source sections, output and reader’s observations on the candidate. <a id="w62-1"></a>
- **W62.2** For the same LLD request, supply direct authorization and an approved contract that settles the rule and component boundary. Supply no HLD, story or epic and no project rule requiring one. The checked design cites the applicable contract and proceeds without creating or requesting a parent. For a declared child whose governing criterion is unresolved, withhold readiness for that child. Reuse W20’s missing-parent evidence where it covers that boundary. Keep the two dispositions and their reasons. <a id="w62-2"></a>

#### Relevant files

`SKILL.md`, the owning references in `references/` for architecture, component design, contracts, work items, plans and tests, and the existing linked examples. Start with `references/high_level_document.md` and `references/low_level_design.md`.

#### Additional context

Ship the ordinary writing route, maintained guidance and worked example together. Use the two specified scenarios and reuse existing evidence for unchanged behavior. Record Met, Failed or Not demonstrated against the candidate under the shared Definition of Done. Initial status is Not demonstrated.

</details>

## S22 · Write from incomplete project context

**Demonstrate the story.** Compare an undecided permission with the same permission already settled by a source. [Story criteria](./specification.md#s22--write-from-incomplete-project-context)

- [ ] T031 [US22] Detect an omitted material permission. `contracts/documents.json`. [W32 · W32.1, W32.2](#w32--detect-an-omitted-material-permission)

### W32 · Detect an omitted material permission

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A writer can omit the question from the discovery record and still pass the current check.

#### Expected outcome

A complete product document can expose its unresolved permission in a draft and cannot be marked ready until the material topic is settled.

#### Scope

Extend the existing document contract and readiness check on the product route. Derive applicable topics from the format and task scope, independently of the writer’s list. Accept a supported answer, a provisional proposal, an open item or a justified inapplicable topic according to its effect on readiness. Preserve old records at their original version.

#### Specification

Parent: [S22](./specification.md#s22--write-from-incomplete-project-context). Supports [S22.1](./specification.md#s22-1) and [F22.1](./specification.md#f22-1). R18/A18. Responsible role: Contract maintainer. Inputs are the existing PRD contract, declared permission controls and [F22](./specification.md#f22--resolve-material-gaps-without-needless-questions)’s undecided brief.

#### Acceptance criteria

- **W32.1** On the undecided export brief, omit the material permission topic. Preparation or checked readiness gives the located missing topic and its affected section. A draft naming that open decision can pass as a draft. <a id="w32-1"></a>
- **W32.2** Mark the decision resolved against the undecided brief. A real but irrelevant source ID cannot pass the required semantic review. Retain the passage and verdict alongside the mechanical result. Reuse the existing open-blocker control. <a id="w32-2"></a>

#### Relevant files

[contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/contracts/documents.json) · [scripts/planning_readiness.py](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/scripts/planning_readiness.py) · [scripts/validate_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/scripts/validate_document.py)

#### Additional context

One commit ships the product route, compatible contract, guidance and smallest affected regression. Use the shared Definition of Done and record the exact candidate, evidence and verdict.

</details>
- [ ] T032 [US22] Ask only the question that changes the requirement. `workflows/discover.md`. [W33 · W33.1, W33.2](#w33--ask-only-the-question-that-changes-the-requirement) After W32.

### W33 · Ask only the question that changes the requirement

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A writer can ask an owner to confirm existing policy or treat a plausible recommendation as authority.

#### Expected outcome

The supported workflow uses existing evidence where decisive, obtains a missing owner answer where necessary and resumes the dependent section.

#### Scope

Connect W32’s decision to the existing discovery and host question routes. Before asking, record the affected criterion, source inspected and unresolved consequence. Bind a returned answer or explicit delegation to the question through a trustworthy host reference where available. Leave unverifiable authority unresolved.

#### Specification

Parent: [S22](./specification.md#s22--write-from-incomplete-project-context). Supports [S22.1](./specification.md#s22-1) and [F22.1](./specification.md#f22-1). R18/A18. Responsible role: Discovery maintainer. Requires [W32](#w32--detect-an-omitted-material-permission). Use A18’s same export route for both requests. The public exchange supplies behavioral proof.

#### Acceptance criteria

- **W33.1** For the format-only change, observe zero permission questions and the preserved permission. For self-service with ownership unresolved, observe one targeted ownership question. An unanswered request keeps the dependent section provisional while independent sections proceed. <a id="w33-1"></a>
- **W33.2** Supply the owner’s answer and confirm only the supported scope becomes ready. A single missing owner-held fact can be asked directly. A delegated routine choice proceeds without making the user confirm it. Use existing evidence for unchanged branches. <a id="w33-2"></a>

#### Relevant files

[workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/workflows/discover.md) · [scripts/planning_readiness.py](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/scripts/planning_readiness.py) · [scripts/validate_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/scripts/validate_document.py)

#### Additional context

Ship one connected question-and-resumption route. Share its packet with W28 and the applicable host acceptance check. Use the shared Definition of Done and record the exact candidate, evidence and verdict.

</details>
- [ ] T033 [US22] Apply discovery checks at the right document scope. `contracts/documents.json`. [W34 · W34.1, W34.2](#w34--apply-discovery-checks-at-the-right-document-scope) After W32 and W33.

### W34 · Apply discovery checks at the right document scope

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A control for complete product documents alone leaves other formats exposed and can add friction to minor edits.

#### Expected outcome

The other applicable authoring routes use the same readiness distinction at a scale appropriate to the requested work.

#### Scope

Map applicability through the existing catalog for complete or substantial authoring, including low-level design, stories and issues. Keep a title edit or a section with no material decision lightweight. Use shared rules when they are sufficient.

#### Specification

Parent: [S22](./specification.md#s22--write-from-incomplete-project-context). Supports [S22.1](./specification.md#s22-1) and [F22.1](./specification.md#f22-1). R18/A18. Responsible role: Document-contract maintainer. Requires [W32](#w32--detect-an-omitted-material-permission) and [W33](#w33--ask-only-the-question-that-changes-the-requirement). Use the actual kind and operation mappings and historical receipt protections.

#### Acceptance criteria

- **W34.1** From actual routing, account for every supported document kind and scope. On the distinct story or Issue path exercise one material missing fact through to draft or owner answer. For a source-settled design reuse compatible route evidence. <a id="w34-1"></a>
- **W34.2** A title-only edit with the same topic incurs no discovery questionnaire. Old receipts verify under their own version. Reuse A7/W17 for host differences, or add only the missing A18 observation to that handoff. <a id="w34-2"></a>

#### Relevant files

[contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/contracts/documents.json) · [references/issue.md](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/references/issue.md) · [references/user_story.md](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/references/user_story.md) · [references/low_level_design.md](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/references/low_level_design.md) · [scripts/test_guided_discovery.py](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/scripts/test_guided_discovery.py)

#### Additional context

Ship the remaining route coverage and its representative checks. Do not multiply all document kinds by all host and question variants. Use the shared Definition of Done and record the exact candidate, evidence and verdict.

</details>

## S20 · Choose the next document from the quick start

**Demonstrate the story.** Choose the next document using the public entry and the numbered sequence. [Story criteria](./specification.md#s20--choose-the-next-document-from-the-quick-start)

- [ ] T034 [US20] Explain spec-driven writing at the public entry. `examples/spec_driven_development.md`. [W42 · W42.1, W42.2](#w42--explain-spec-driven-writing-at-the-public-entry)

### W42 · Explain spec-driven writing at the public entry

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The public README opens with a catalog and then lists installation requirements. A developer has to infer what a specification changes about the work.

#### Expected outcome

A first-time reader can start with one change request, choose a document and follow one behavior into a task and its planned proof.

#### Scope

Edit the repository-root README introduction. Put a plain-language explanation and a compact need-to-output table before setup. Use the current catalog and one existing feature example. W29 owns the detailed chronology.

#### Specification

Parent: [S20](./specification.md#s20--choose-the-next-document-from-the-quick-start). Supports [S20.2](./specification.md#s20-2) and [F20.2](./specification.md#f20-2). R16/A16. Responsible role: documentation maintainer. Uses existing references and examples; can ship before [W29](#w29--publish-the-numbered-document-sequence-in-the-readmemd-file). Show only entry points available on the candidate.

#### Acceptance criteria

- **W42.1** Starting at the README title, before installation, a reader can identify the audience, what a spec settles before coding, what to supply and what the writer returns. The reader can choose among an unshaped idea, agreed feature behavior and one bounded fix from the need-to-output table. A small authorized fix must route straight to an Issue. <a id="w42-1"></a>
- **W42.2** Follow one worked request through a named requirement, story criterion, a clearly labeled illustrative child Issue and its planned observable check. Preserve the source behavior on failure, keep the record types distinct and avoid claiming the check ran. Record the passage, link targets and reader answers on the candidate. One document read covers both criteria. <a id="w42-2"></a>

#### Relevant files

Repository root README and its Quick start; [WEB-06](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/spec_driven_development.md#L102-L104) · [the story criterion](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/user_story.md#L20) · [T10](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/test_specification.md#L49) · [upstream reader guide](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/README.md#choose-your-process) · [upstream development method](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/README.md#spec-driven-development).

#### Additional context

Suggested opening in the project’s own voice: “Technical Writer helps developers and AI agents agree on what a change must do before anyone builds it. Give it a request and the project sources. It turns the agreed behavior into specifications, stories and tasks that say how to check the result.” Example: “If saving a category fails, keep my selection.” WEB-06 requires retaining it. The story expects an error and the selection still in edit mode. An illustrative child Issue would implement that failure path. T10 defines its check, including the absence of a success message. Link the real examples and label the illustrative Issue. Ship the README edit in one commit. Use the shared Definition of Done.

</details>

## S39 · Find instructions for a feature or document type from the index

**Demonstrate the story.** Find each released capability and document type from the public index. [Story criteria](./specification.md#s39--find-instructions-for-a-feature-or-document-type-from-the-index)

- [ ] T035 [US39] Publish the public index with a usable focused-edit entry. `README.md`. [W54 · W54.1, W54.2](#w54--publish-the-public-index-with-a-usable-focused-edit-entry)

### W54 · Publish the public index with a usable focused-edit entry

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The current README describes focused edits inside a list of scenarios.

#### Expected outcome

A reader can follow the index to the focused-edit instructions and request a change with a clear boundary.

#### Scope

Link the public index from the README. Point the focused-edit entry at its existing named section and improve that section if the example omits a needed input or result. Link additional released routes as their guidance becomes usable.

#### Specification

Parent: [S39](./specification.md#s39--find-instructions-for-a-feature-or-document-type-from-the-index). Supports [S39.1](./specification.md#s39-1) and [F39.1](./specification.md#f39-1). R35/A35. Owner role: documentation maintainer. Reuses the existing edit route. [W54](#w54--publish-the-public-index-with-a-usable-focused-edit-entry) was previously proposed under [S34](./specification.md#s34--find-a-capability-and-follow-a-feature-from-request-to-evidence). Its revised scope is approved here.

#### Acceptance criteria

- **W54.1** From the candidate README, follow the index link for a focused edit. A direct link to “Make a focused edit” passes when it explains the title-only request, the preserved description and how to inspect the result. A working link to “Review a document” fails for that request. Keep the destination and the text that settles the distinction. <a id="w54-1"></a>
- **W54.2** Open the index links included in this increment. Each guide or named section resolves on the candidate. A missing heading, an empty stub or a planned feature presented as ready fails. Save the candidate and link results. <a id="w54-2"></a>

#### Relevant files

`README.md` (including its focused-edit section), planned `docs/README.md`, and `references/readme.md`.

#### Additional context

Ship the index and its first usable link in one commit. Initial verdicts: Not demonstrated. Apply the shared Definition of Done.

</details>

## S20 · Choose the next document from the quick start (continued)

**Demonstrate the story.** Choose the next document using the public entry and the numbered sequence. [Story criteria](./specification.md#s20--choose-the-next-document-from-the-quick-start)

- [ ] T036 [US20] Publish the numbered document sequence in the `README.md` file. `README.md`. [W29 · W29.1, W29.2](#w29--publish-the-numbered-document-sequence-in-the-readmemd-file) After W20, W30–W31 and the seven linked authoring routes (W04–W06, W09–W10, W12–W13).

### W29 · Publish the numbered document sequence in the `README.md` file

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

New users see isolated prompts before learning what establishes the next document’s inputs.

#### Expected outcome

A contributor can choose what to write next from the `README.md` file alone and follow the link to the owning format.

#### Scope

Build on the Quick start section “Where `tasks.md` fits” when the implementation ships. Publish the full numbered chronology and replace its planned-status wording with verified host entries. Link to the owning format guides. The command instructions must identify their actual input, output and next reader for both hosts.

#### Specification

Parent: [S20](./specification.md#s20--choose-the-next-document-from-the-quick-start). Supports [S20.1](./specification.md#s20-1) and [F20.1](./specification.md#f20-1). R16/A16. Responsible role: documentation maintainer. Requires the adopted routes for the seven artifacts, [W20](#w20--resolve-feature-story-and-task-ancestry-before-drafting)’s parent rules, [W30](#w30--choose-a-task-or-story-for-an-improvement)–[W31](#w31--choose-a-feature-epic-or-delivery-plan)’s selection rules and the accepted production order.

#### Acceptance criteria

- **W29.1** Starting at Quick start, a new reader can locate discovery or existing evidence → brief when useful → product definition → feature or epic → specified stories and acceptance → applicable design or decisions → delivery plan → child Issue → evidence and closure. The section says what feeds each step and links to the actual skill guidance. Follow the multi-task branch through its reviewed spec and plan, Issues, `tasks.md`, eligible Issue, implementation evidence and next eligible row. Starting from the README, the reader can explain why the list is the last writing output and why no `task.md` follows it by default. <a id="w29-1"></a>
- **W29.2** Using the same section, route an independent broken-link fix directly, with inline scope and proof. Identify why an orphaned child must wait. Locate all seven conditional artifacts at their dependency points and distinguish planned proof from observed results. Retain the `README.md` file passage, resolved links and both reader answers. <a id="w29-2"></a>

#### Relevant files

[Repository entry](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/README.md#L56) · [Relationship guidance](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md#L116) · [Required production order](./specification.md#production-order)

#### Additional context

One commit ships the section, quick-start link and necessary cross-references. Reuse W20 evidence for runtime routing. Record verdict and evidence against the exact candidate under the shared Definition of Done.

</details>

## S23 · Write the intended artifact from a short request

**Demonstrate the story.** Use the supported shortcut to reach the right format and its checked output. [Story criteria](./specification.md#s23--write-the-intended-artifact-from-a-short-request)

- [ ] T037 [US23] Launch three document types in Claude Code. `scripts/install_skill.py`. [W35 · W35.1, W35.2](#w35--launch-three-document-types-in-claude-code)

### W35 · Launch three document types in Claude Code

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A bare slash command needs host-level discovery.

#### Expected outcome

Claude Code can start a PRD, LLD or single Issue directly.

#### Scope

Offer opt-in thin entries for /prd, /lld and /task through the current installer. Reuse one catalog and writing route. Preserve user material, explicit edit intent and existing commands.

#### Specification

Parent: [S23](./specification.md#s23--write-the-intended-artifact-from-a-short-request). Supports [S23.1](./specification.md#s23-1) and [F23.1](./specification.md#f23-1). R19/A19. Responsible role: integration maintainer. Use the installed skill, existing catalog and current installer.

#### Acceptance criteria

- **W35.1** From a real Claude Code session dispatch a short command and compare its checked artifact, brief and type to the owning contract. Resolve the other two names through the same mapping. <a id="w35-1"></a>
- **W35.2** Supply an occupied name and repeat installation. Existing foreign content remains intact, a working qualified alternative is reported, and removal affects only owned entries. <a id="w35-2"></a>

#### Relevant files

[scripts/install_skill.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/install_skill.py) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/documents.json)

#### Additional context

Ship the entry, affected guidance and necessary compatibility evidence together. Stop at the stated proof. Record the candidate and verdict under the shared Definition of Done.

</details>
- [ ] T038 [US23] Launch the same documents in Codex. `scripts/install_skill.py`. [W36 · W36.1, W36.2](#w36--launch-the-same-documents-in-codex) After W35.

### W36 · Launch the same documents in Codex

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

Codex has a different native skill invocation.

#### Expected outcome

Codex CLI users can invoke $prd, $lld or $task directly.

#### Scope

Reuse W35’s alias mapping and writing entry with Codex’s supported skill installation. Document copyable host examples.

#### Specification

Parent: [S23](./specification.md#s23--write-the-intended-artifact-from-a-short-request). Supports [S23.1](./specification.md#s23-1) and [F23.1](./specification.md#f23-1). R19/A19. Responsible role: integration maintainer. Requires [W35](#w35--launch-three-document-types-in-claude-code)’s common mapping.

#### Acceptance criteria

- **W36.1** Capture a real Codex invocation and checked result for one of the three kinds. The brief retains its context and literals; the destination and format agree with the existing writer. <a id="w36-1"></a>
- **W36.2** Resolve the other names, preserve the qualified fallback and verify the Codex-specific install/removal boundary. Reuse shared collision checks if their inputs and path are unchanged. <a id="w36-2"></a>

#### Relevant files

[scripts/install_skill.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/install_skill.py) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/documents.json)

#### Additional context

Ship the entry, affected guidance and necessary compatibility evidence together. Stop at the stated proof. Record the candidate and verdict under the shared Definition of Done.

</details>
- [ ] T039 [US23] Expose the authorable document catalog. `scripts/install_skill.py`. [W37 · W37.1, W37.2](#w37--expose-the-authorable-document-catalog) After W35 and W36.

### W37 · Expose the authorable document catalog

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A user needs to find which names are installed.

#### Expected outcome

Every supported authorable kind has a discoverable selector and opt-in shortcut or a documented qualified fallback for an occupied name.

#### Scope

Generate entries and quick-start help from the same catalog. Add ready variants as their complete contracts ship. Preserve full-name requests, aliases, reviews and literal text.

#### Specification

Parent: [S23](./specification.md#s23--write-the-intended-artifact-from-a-short-request). Supports [S23.1](./specification.md#s23-1) and [F23.1](./specification.md#f23-1). R19/A19. Responsible role: integration maintainer. Use [W35](#w35--launch-three-document-types-in-claude-code)–[W36](#w36--launch-the-same-documents-in-codex) and the registered output contracts.

#### Acceptance criteria

- **W37.1** Compare the catalog with generated entries. Every active authoring route resolves to its owning kind, including spec for behavioral specification, and every displayed host spelling corresponds to the installed entry. <a id="w37-1"></a>
- **W37.2** Use a source-settled request and a review request. Selecting a spec does not create a PRD; reviewing an existing artifact does not create a replacement. Use the template crosswalk for both. <a id="w37-2"></a>

#### Relevant files

[scripts/install_skill.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/install_skill.py) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/documents.json) · [README.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/README.md)

#### Additional context

Ship the entry, affected guidance and necessary compatibility evidence together. Stop at the stated proof. Record the candidate and verdict under the shared Definition of Done.

</details>
- [ ] T040 [US23] Write the feature task list and its linked Issues. `scripts/install_skill.py`. [W40 · W40.1, W40.2, W40.3](#w40--write-the-feature-task-list-and-its-linked-issues) After W35, W11 and W20.

### W40 · Write the feature task list and its linked Issues

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The upstream tasks template is a list, while a commissioned child needs its own acceptance record.

#### Expected outcome

A developer receives one Issue for a bounded change or one feature-level `tasks.md` with linked, independently shippable Issues for a multi-task feature.

#### Scope

Route task and tasks separately. Adapt the pinned task-list template and generation instructions. Group work by story, identify the first usable story and how each story can be demonstrated, and distinguish safe parallel work from prerequisites. Use the owning Issues for acceptance, stable IDs and proof. Apply W20 ancestry and R17’s standalone exception.

#### Specification

Parent: [S23](./specification.md#s23--write-the-intended-artifact-from-a-short-request). Supports [S23.1](./specification.md#s23-1) and [F23.1](./specification.md#f23-1). R19/A19. Responsible role: integration maintainer. Use [W35](#w35--launch-three-document-types-in-claude-code)’s selection mechanism, [W11](#w11--write-an-epic-whose-stories-prove-a-usable-outcome) and [W20](#w20--resolve-feature-story-and-task-ancestry-before-drafting).

#### Acceptance criteria

- **W40.1** From one approved story, task produces one Issue and tasks produces a justified breakdown with the same parent, criterion links, dependencies and observable proof for each child. A one-line upstream checklist entry alone fails. <a id="w40-1"></a>
- **W40.2** A single independent maintenance change stays one Issue. A missing parent for a declared child blocks readiness. Reuse the existing ancestry negatives and confirm no template-generated setup phase or invented test obligation appears. <a id="w40-2"></a>
- **W40.3** Given the two approved refund stories, settled read contract, verified fixture paths and Issue references in the [feature task-list rules and refund example](./specification.md#feature-task-lists-and-issue-acceptance), use the normal writing entry. Expect one `tasks.md` with four rows linked to #81–#84 and their criteria. In US1, only T001 and T002 carry `[P]` and the same refund can be checked on both surfaces before US2 ships. In US2, T004 explicitly depends on T003 and the story demonstration uses mixed refund decisions. A second editable copy of task acceptance, a blanket setup phase or a parallel marker on T004 fails. Retain the checked list and its linked Issues for W48. At the Tasks entry, consume the reviewed spec and plan, resolve or author the Issues before marking the list ready, and return the linked outputs. Reuse existing Issues on continuation. An unresolved row remains unready. Use the [command and document sequence](./specification.md#when-to-write-and-read-tasksmd) in the installed writing guidance. Reuse the supplied tracker Issues for the refund case. For the Markdown-only W-PACKET case, keep each task’s scope, criteria and proof at its row or link its existing record. Resolve the governing story criterion from each task. Requiring a tracker export or a new file per task fails the Markdown case. A consumer that restates an existing criterion’s full case under the same ID fails even when the text agrees. Where a task demonstrates the same story criterion, link to its definition and state the task-specific proof. <a id="w40-3"></a>

#### Relevant files

[scripts/install_skill.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/install_skill.py) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/documents.json) · [references/issue.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/references/issue.md) · [references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/references/implementation_plan.md)

#### Additional context

Use the three existing Issues in [W-PACKET](./test.md#cases) to generate a small list from this repository and retain the actual output for W48. The approved refund checks still apply.

Ship the entry, affected guidance and necessary compatibility evidence together. Stop at the stated proof. Record the candidate and verdict under the shared Definition of Done.

</details>
- [ ] T041 [US23] Route quality and consistency reviews. `scripts/install_skill.py`. [W41 · W41.1, W41.2](#w41--route-quality-and-consistency-reviews) After W35, with the relevant review route.

### W41 · Route quality and consistency reviews

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

Requirement quality, cross-document agreement and executed checks answer different questions.

#### Expected outcome

A reviewer can request a requirement checklist or a read-only consistency analysis grounded in the owning documents.

#### Scope

Expose checklist through W04 and analyze through W03/W21. Reuse policy for governance, discovery for clarify and existing plans for planning. A convergence-style report can identify gaps; it cannot commission uncovered scope or run implementation.

#### Specification

Parent: [S23](./specification.md#s23--write-the-intended-artifact-from-a-short-request). Supports [S23.1](./specification.md#s23-1) and [F23.1](./specification.md#f23-1). R19/A19. Responsible role: integration maintainer. Requires the relevant existing route and [W35](#w35--launch-three-document-types-in-claude-code)’s common entry mechanism.

#### Acceptance criteria

- **W41.1** Given one vague criterion and one task that weakens a sourced permission, checklist locates the requirement-quality defect and analyze locates the cross-document disagreement. Reuse the same packet. <a id="w41-1"></a>
- **W41.2** Inspect before and after the read-only analysis: the reviewed source, tasks and candidate are unchanged. Findings do not claim runtime proof. A request for code implementation routes to the authorized implementing workflow. <a id="w41-2"></a>

#### Relevant files

[scripts/install_skill.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/install_skill.py) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/documents.json) · [workflows/validation_review.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/workflows/validation_review.md)

#### Additional context

Ship the entry, affected guidance and necessary compatibility evidence together. Stop at the stated proof. Record the candidate and verdict under the shared Definition of Done.

</details>

## S24 · Choose and continue one eligible document

**Demonstrate the story.** Identify one useful next document and continue only when requested. [Story criteria](./specification.md#s24--choose-and-continue-one-eligible-document)

- [ ] T042 [US24] Show the next useful document. `SKILL.md`. [W38 · W38.1, W38.2](#w38--show-the-next-useful-document) After W20 and W30–W31, with the approved production order.

### W38 · Show the next useful document

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A static sequence cannot account for current scope and reviewed sources.

#### Expected outcome

Guide and next can explain the right next action without creating a file.

#### Scope

Support starting from a goal or existing artifact. Inspect current initiative and source revisions. For eligible work show document type, specific gap and benefit in one line. If choice matters, identify the decision. Stop at the requested endpoint.

#### Specification

Parent: [S24](./specification.md#s24--choose-and-continue-one-eligible-document). Supports [S24.1](./specification.md#s24-1) and [F24.1](./specification.md#f24-1). R20/A20. Responsible role: workflow maintainer. Requires [W20](#w20--resolve-feature-story-and-task-ancestry-before-drafting), [W30](#w30--choose-a-task-or-story-for-an-improvement)–[W31](#w31--choose-a-feature-epic-or-delivery-plan) and the approved production order.

#### Acceptance criteria

- **W38.1** From a feature with a settled prerequisite, next names one eligible document and the specific benefit in one line; repeated next leaves the initiative unchanged. With two plausible initiatives ask which only if evidence cannot settle it. <a id="w38-1"></a>
- **W38.2** For a blocked child name the missing prerequisite. For a standalone fix with sufficient acceptance say documentation is complete. Recommend no extra document in either case; reuse A17 and A18 evidence. Reuse W40’s refund case to check that next recommends `tasks.md` once its inputs exist and reports document delivery after the checked list. It must neither invent a singular document nor initiate implementation. <a id="w38-2"></a>

#### Relevant files

[SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/workflows/discover.md) · [README.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/README.md)

#### Additional context

Ship the entry, affected guidance and necessary compatibility evidence together. Stop at the stated proof. Record the candidate and verdict under the shared Definition of Done.

</details>
- [ ] T043 [US24] Continue a checked document handoff. `SKILL.md`. [W39 · W39.1, W39.2](#w39--continue-a-checked-document-handoff) After W38 and W15.

### W39 · Continue a checked document handoff

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

A suggested next step can duplicate prior work or outlive its source revision.

#### Expected outcome

The owner can continue one document at a time and resume from the current project state.

#### Scope

Use W38’s selected initiative, existing records and the normal writing workflow. Bind any suggested successor included in a checked final message to W15’s reviewed delivery. Respect a single-document request.

#### Specification

Parent: [S24](./specification.md#s24--choose-and-continue-one-eligible-document). Supports [S24.1](./specification.md#s24-1) and [F24.1](./specification.md#f24-1). R20/A20. Responsible role: workflow maintainer. Requires [W38](#w38--show-the-next-useful-document) and [W15](#w15--deliver-an-optional-reviewed-decision-with-a-verifiable-receipt) for checked delivery text.

#### Acceptance criteria

- **W39.1** On continue, write exactly the selected eligible artifact; the source revision, governing criterion and shared terms survive. Resume from the same starting request after delivery and identify the completed result without duplicating it. <a id="w39-1"></a>
- **W39.2** Change a governing revision before continuing. Re-evaluate affected readiness and keep unaffected evidence. A stale handoff or altered checked suggestion fails; when a suggestion cannot be bound to the receipt, keep exact finalization and offer guidance on request. <a id="w39-2"></a>

#### Relevant files

[SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/workflows/discover.md) · [contracts/delivery_message.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/delivery_message.json) · [scripts/validate_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/validate_document.py)

#### Additional context

Ship the entry, affected guidance and necessary compatibility evidence together. Stop at the stated proof. Record the candidate and verdict under the shared Definition of Done.

</details>

## S25 · Guide selection of a specification after delivery

**Demonstrate the story.** Identify which specification governs work after delivery. [Story criteria](./specification.md#s25--guide-selection-of-a-specification-after-delivery)

- [ ] T044 [US25] Guide selection of a specification after delivery. `references/spec_driven_development.md`. [W43 · W43.1, W43.2](#w43--guide-selection-of-a-specification-after-delivery) Use W32–W34 when authority is ambiguous.

### W43 · Guide selection of a specification after delivery

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The behavioral specification guide covers revisions. Decision records cover supersession. Neither tells a writer resuming a delivered feature how to distinguish the maintained behavior source from a frozen delivery snapshot when both are available. R18 classifies evidence, but does not settle this post-delivery choice.

#### Expected outcome

Find which agreement governs the next change.

#### Scope

Use the team’s declared maintenance convention. Link a retained snapshot to its maintained successor or other approved source when known. With no authority for a material difference, preserve both and ask one focused question.

#### Specification

Parent: [S25](./specification.md#s25--guide-selection-of-a-specification-after-delivery). Supports [S25.1](./specification.md#s25-1) and [F25.1](./specification.md#f25-1). R21/A21. Responsible role: skill maintainer. Use existing source and review contracts. Reuse [W32](#w32--detect-an-omitted-material-permission)–[W34](#w34--apply-discovery-checks-at-the-right-document-scope) for ambiguous authority.

#### Acceptance criteria

- **W43.1** At the normal edit entry, supply a frozen launch specification allowing seven days and an approved maintained policy allowing thirty days. Ask to update the feature. The draft cites the maintained rule and labels the seven-day value historical. Both source files remain intact. <a id="w43-1"></a>
- **W43.2** Remove the maintenance decision while keeping two plausible values. The writer identifies the conflict and asks which governs before committing to a value. It can draft unrelated sections. Capture the two draft excerpts or the focused question, source revisions and before/after identities of the inputs. Reuse existing discovery and rewrite evidence for unchanged behavior. <a id="w43-2"></a>

#### Relevant files

[Writing guidance](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md) · [Affected handoff](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [Upstream comparison](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/how-to/persisting-specs.md#two-separate-questions)

#### Additional context

One commit ships the guidance with the affected example and any necessary route adjustment. Apply the shared Definition of Done. Initially Not demonstrated. Retain each criterion verdict, evidence and candidate in the task.

</details>

## S26 · Resolve constrained fields in Issue handoffs

**Demonstrate the story.** Recover field-specific constraints from the Issue the implementer receives. [Story criteria](./specification.md#s26--resolve-constrained-fields-in-issue-handoffs)

- [ ] T045 [US26] Resolve constrained fields in Issue handoffs. `references/issue.md`. [W44 · W44.1, W44.2](#w44--resolve-constrained-fields-in-issue-handoffs) After W40 and W41.

### W44 · Resolve constrained fields in Issue handoffs

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The Issue guide names requirement-level coverage. The Interface Contract already distinguishes absence, null and exact field names. The task handoff and its planned consistency review do not explicitly require the owner and field to resolve together when one requirement covers several similarly named fields. A document-level link alone can hide the wrong field.

#### Expected outcome

Trace a field constraint to its precise definition.

#### Scope

When a task implements a constrained field, link its exact owner and field, preserve relevant semantics and flag uncovered or misattributed fields when reviewing the requested scope. Reuse the project’s schema, Interface Contract or Low Level Design as appropriate.

#### Specification

Parent: [S26](./specification.md#s26--resolve-constrained-fields-in-issue-handoffs). Supports [S26.1](./specification.md#s26-1) and [F26.1](./specification.md#f26-1). R22/A22. Responsible role: skill maintainer. Use existing source and review contracts. Build on [W40](#w40--write-the-feature-task-list-and-its-linked-issues) and [W41](#w41--route-quality-and-consistency-reviews) for generation and read-only analysis.

#### Acceptance criteria

- **W44.1** From a contract where Order.code is optional and Return.code is required, request the task for Return.code. The Issue points to the exact Return.code definition and preserves the required behavior. An unambiguous existing field pointer is sufficient. <a id="w44-1"></a>
- **W44.2** Review a variant citing Order.code for the return requirement. The review identifies the Issue, wrong field and missing coverage. An unrelated prose-only Issue requires no field citations. Retain the authored Issue, read-only review excerpt and the unchanged source definitions. Use this same pair at W40/W41 if available. <a id="w44-2"></a>

#### Relevant files

[Writing guidance](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [Affected handoff](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/interface_contract.md) · [Upstream comparison](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/commands/tasks.md#task-organization)

#### Additional context

One commit ships the guidance with the affected example and any necessary route adjustment. Apply the shared Definition of Done. Initially Not demonstrated. Retain each criterion verdict, evidence and candidate in the task.

</details>

## S27 · Document the owner and consumer version of a shared contract

**Demonstrate the story.** Locate the owner and version of a shared contract from the consumer. [Story criteria](./specification.md#s27--document-the-owner-and-consumer-version-of-a-shared-contract)

- [ ] T046 [US27] Document the owner and consumer version of a shared contract. `references/interface_contract.md`. [W45 · W45.1, W45.2](#w45--document-the-owner-and-consumer-version-of-a-shared-contract)

### W45 · Document the owner and consumer version of a shared contract

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The Interface Contract guide names the provider, consumers, version and source authority. Its worked handoff does not tell a consumer how to handle a locally edited copy, or how to distinguish a version pinned by the consumer from the version supported by the deployed provider.

#### Expected outcome

Identify the governing contract and supported version.

#### Scope

For independently released components, identify the authoritative source and immutable revision, the consumer’s copy or pin, and the evidence for deployed compatibility when claimed. Resolve disagreements at the owner. Leave deployment support unknown when there is no observation.

#### Specification

Parent: [S27](./specification.md#s27--document-the-owner-and-consumer-version-of-a-shared-contract). Supports [S27.1](./specification.md#s27-1) and [F27.1](./specification.md#f27-1). R23/A23. Responsible role: skill maintainer. Use existing source and review contracts. Use the existing Interface Contract route.

#### Acceptance criteria

- **W45.1** Given an owner contract at v1, a divergent consumer copy and a proposed v2, ask for an Interface Contract update. It identifies the source revision, pins the consumer to v1, names the discrepancy and directs the proposed change to the owner. The consumer copy is untouched. <a id="w45-1"></a>
- **W45.2** Provide only the v1 pin and mock results, with no deployed-provider evidence. The handoff distinguishes the agreed version from unknown runtime support. One shared file used by both components requires no synchronized copy. Keep the cited owner revision, consumer pin and resulting compatibility passage; inspect the copy identity. No service deployment or provider test is needed to assess this writing change. <a id="w45-2"></a>

#### Relevant files

[Writing guidance](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/interface_contract.md) · [Affected handoff](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/interface_contract.md) · [Upstream comparison](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/how-to/contract-driven-development.md#one-authoritative-owner)

#### Additional context

One commit ships the guidance with the affected example and any necessary route adjustment. Apply the shared Definition of Done. Initially Not demonstrated. Retain each criterion verdict, evidence and candidate in the task.

</details>

## S28 · Release the Spec Writer identity and legacy entry

**Demonstrate the story.** Reach the renamed skill and resolve an existing installation. [Story criteria](./specification.md#s28--release-the-spec-writer-identity-and-legacy-entry)

- [ ] T047 [US28] Release the Spec Writer identity and legacy entry. `SKILL.md`. [W46 · W46.1, W46.2](#w46--release-the-spec-writer-identity-and-legacy-entry) Requires accepted Skill Builder B5/T50 before changing the live identity.

### W46 · Release the Spec Writer identity and legacy entry

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The shipped name, discovery and examples use Technical Writer. Skill Builder also requires that literal dependency identity. A metadata-only rename can break both discovery and document acceptance.

#### Expected outcome

A new installation advertises Spec Writer with skill ID `spec-writer`. A previously supported invocation still reaches its writing workflow.

#### Scope

Canonical metadata, host entry points, installer, public README examples and existing aliases. Preserve historical receipt identifiers, the repository URL and user-owned destinations.

#### Specification

Parent: [S28](./specification.md#s28--release-the-spec-writer-identity-and-legacy-entry). Supports [S28.1](./specification.md#s28-1) and [F28.1](./specification.md#f28-1). R24/A24. Owner role: skill maintainer. Requires accepted Skill Builder B5/T50; coordinate host evidence with [W17](#w17--ship-neutral-cross-host-assignments-for-the-connected-handoff) and shortcut ownership with [W35](#w35--launch-three-document-types-in-claude-code)–[W37](#w37--expose-the-authorable-document-catalog).

#### Acceptance criteria

- **W46.1** On Codex and Claude Code, discover the new canonical skill and complete a checked writing request. On the existing-install path, invoke the former name and bind its result to the same writer. Keep one observed invocation per changed host path and reuse W17 when it proves that path. Inspect the release’s public names and link labels, including the existing source labels in `references/issue.md`, `references/implementation_plan.md` and `references/spec_driven_development.md`. Check the changed examples and session replies. The sole product name is Spec Writer. Use functional wording for the optional workflow. Retain the source links and required notices. <a id="w46-1"></a>
- **W46.2** On a machine with an unrelated `spec-writer` installation, setup reports the collision and preserves it. Run one real Builder document validation against the renamed release with the accepted B5 resolver; retain the package revision and receipt. <a id="w46-2"></a>

#### Relevant files

SKILL.md, README.md and scripts/install_skill.py; Skill Builder scripts/runtime/technical_writer.py. [Evidence](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/install_skill.py)

#### Additional context

Ship the working entry and its consumer in one commit. Record criterion verdicts, candidate and proof under the shared Definition of Done. Implementation initially Not demonstrated.

</details>

## S29 · Start one feature through an optional workflow extension

**Demonstrate the story.** Select the intended feature in an initialized project. [Story criteria](./specification.md#s29--start-one-feature-through-an-optional-workflow-extension)

- [ ] T048 [US29] Start one feature through an optional workflow extension. `scripts/install_skill.py`. [W47 · W47.1, W47.2](#w47--start-one-feature-through-an-optional-workflow-extension) After W46, with the checked specification route.

### W47 · Start one feature through an optional workflow extension

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

Standalone host shortcuts establish a document type. They do not by themselves establish an initialized workflow project, its active feature or the effective project override.

#### Expected outcome

The selected feature in an existing project receives a checked behavioral specification through a namespaced writing command.

#### Scope

Use upstream initialization and host integration. Read the active project and effective rule. Reuse the canonical writer; keep the workflow optional for standalone writing.

#### Specification

Parent: [S29](./specification.md#s29--start-one-feature-through-an-optional-workflow-extension). Supports [S29.1](./specification.md#s29-1) and [F29.1](./specification.md#f29-1). R25/A25. Owner role: skill maintainer. Requires [W46](#w46--release-the-spec-writer-identity-and-legacy-entry) and the checked behavioral-spec route. Use the upstream revision identified in the audit as the starting compatibility reference.

#### Acceptance criteria

- **W47.1** Initialize or reuse an existing project, select its refund feature, and issue a writing request on each target host. Capture the resulting checked feature path, project rule and command actually invoked. The existing standalone skill also accepts an ordinary request without the optional workflow; reuse W46 for this. <a id="w47-1"></a>
- **W47.2** Repeat setup with an edited feature document and two possible feature contexts. Preserve the edited document. Use an explicit selection or request the one missing choice; no write reaches the sibling feature. <a id="w47-2"></a>

#### Relevant files

scripts/install_skill.py and the behavioral-spec reference; upstream docs/extensions/developing.md and docs/presets/overview.md. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/extensions/developing.md)

#### Additional context

Ship the working entry and its consumer in one commit. Record criterion verdicts, candidate and proof under the shared Definition of Done. Implementation initially Not demonstrated.

</details>

## S30 · Select eligible feature work and recover its Issue criteria

**Demonstrate the story.** Use the feature list to select ready work and recover the chosen Issue’s criterion. [Story criteria](./specification.md#s30--select-eligible-feature-work-and-recover-its-issue-criteria)

- [ ] T049 [US30] Select eligible tasks from the feature list. `references/issue.md`. [W48 · W48.1, W48.2, W48.3](#w48--select-eligible-tasks-from-the-feature-list) After W47, W40 and W44.

### W48 · Select eligible tasks from the feature list

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The upstream implementation command reads a phased tasks.md. Our Issue holds the bounded task and its acceptance. Matching filenames or an Issue link alone cannot establish what the downstream agent actually receives.

#### Expected outcome

Through its supported inputs, the real implementing agent reads the active feature, recognizes eligible and blocked tasks, and recovers the selected Issue’s stable ID, criterion, allowed actor, scope and proof.

#### Scope

Use one authoritative Issue per task. Supply the active feature spec, plan and W40’s `tasks.md` at the pinned integration’s normal inputs. Resolve feature-local IDs to the current Issue and criterion. Use source revisions and existing progress records to make safe selections. Acceptance requires the Issue’s evidence.

#### Specification

Parent: [S30](./specification.md#s30--select-eligible-feature-work-and-recover-its-issue-criteria). Supports [S30.1](./specification.md#s30-1) and [F30.1](./specification.md#f30-1). R26/A26. Owner role: skill maintainer. Requires [W47](#w47--start-one-feature-through-an-optional-workflow-extension), [W40](#w40--write-the-feature-task-list-and-its-linked-issues) and [W44](#w44--resolve-constrained-fields-in-issue-handoffs). Prove actual consumption before designing more document commands.

#### Acceptance criteria

- **W48.1** Project an approved manager-only refund Issue into the selected feature. Observe the actual consumer extracting the scoped task and its denied-permission criterion from its normal inputs. Preserve the Issue as the editing authority. <a id="w48-1"></a>
- **W48.2** Give a sibling feature the same short task ID; revise the selected Issue after generating the view. The consumer must not take the sibling task or dispatch the stale revision. Reconcile against the governing Issue, retaining existing acceptance evidence. <a id="w48-2"></a>
- **W48.3** Give the actual implementing agent W40’s feature list and linked Issues through its normal entry, without coaching it on the order. Capture the consumer identifying both T001 and T002 as eligible together and explaining how their story can ship before filtering. At the start of US2, capture the consumer selecting T003 and identifying its working API as the reason T004 must wait. Once the approved API filter has evidence on the candidate, observe T004 become eligible and the agent recover #84’s governing criterion. A checkbox alone, an early dispatch or a wrong Issue fails. Retain the consumer’s selections, prerequisite evidence and source references. Reuse the same feature and applicable checkpoints. This check proves scheduling and handoff; it requires neither concurrent workers nor four fresh builds. At the implementation entry, observe that the agent opens the active plan, feature list and selected Issue. Reuse those selection observations to prove it returns to the same list for the next eligible row. A demand for a new `task.md` fails. In W-PACKET, follow the actual selected row to the task criterion and its parent story criterion. Record those two sources in the same readback. <a id="w48-3"></a>

#### Relevant files

references/issue.md, references/implementation_plan.md; upstream templates/commands/tasks.md and templates/commands/implement.md. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/commands/implement.md#L143-L153)

#### Additional context

Use the W40 output retained for [W-PACKET](./test.md#cases) to observe selection before and after W01 evidence is supplied. Keep the rehearsal read-only. The refund case still owns the story demonstration and blocked API dependency.

Ship the working entry and its consumer in one commit. Record criterion verdicts, candidate and proof under the shared Definition of Done. Implementation initially Not demonstrated.

</details>

## S31 · Verify and resume one authorized implementation

**Demonstrate the story.** Resume the same authorized task after interruption without replaying an uncertain effect. [Story criteria](./specification.md#s31--verify-and-resume-one-authorized-implementation)

- [ ] T050 [US31] Hand one approved task to the selected implementation provider. Upstream [`templates/commands/implement.md`](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/commands/implement.md). [W49 · W49.1, W49.2](#w49--hand-one-approved-task-to-the-selected-implementation-provider) After W48, with authority for the selected provider.

### W49 · Hand one approved task to the selected implementation provider

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

An authored task or checked box establishes intent or progress. It does not establish a dispatched provider, an observed candidate or the state of an interrupted write.

#### Expected outcome

One authorized coding session receives a bounded task and returns a verdict tied to its actual candidate and original criterion.

#### Scope

Connect the upstream implementation path in a disposable authorized project. In Mirai projects, preserve the project-selected owner and make the same packet available for its handoff. Product deployment or changes to Mirai are outside this task.

#### Specification

Parent: [S31](./specification.md#s31--verify-and-resume-one-authorized-implementation). Supports [S31.1](./specification.md#s31-1) and [F31.1](./specification.md#f31-1). R27/A27. Owner role: skill maintainer. Requires [W48](#w48--select-eligible-tasks-from-the-feature-list). Name the authority, provider and candidate in the task. No second provider may act on the same assignment.

#### Acceptance criteria

- **W49.1** Hand the manager-only refund Issue to the selected coding agent. Record the real dispatch and observed candidate. A candidate allowing an employee to refund fails the original denial criterion; retain the observed behavior and candidate. For the workflow integration, document that the bundled workflow ends at Implement. Use the existing criterion evidence to complete ordinary delivery without invoking Converge. Document Converge as available only on explicit user request. <a id="w49-1"></a>
- **W49.2** Use scoped correction and the smallest discriminating check to observe the required denial on the corrected candidate. Keep the earlier failure. A checkbox or suggested out-of-scope enhancement cannot change the criterion or authorize new work. <a id="w49-2"></a>

#### Relevant files

Upstream templates/commands/implement.md, templates/commands/converge.md and workflows/speckit/workflow.yml; writer verification and handoff references. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/workflows/overview.md#run-review-and-resume)

#### Additional context

Ship the working entry and its consumer in one commit. Record criterion verdicts, candidate and proof under the shared Definition of Done. Implementation initially Not demonstrated.

</details>
- [ ] T051 [US31] Resume the same task after an interrupted run. Upstream [`docs/workflows/cli.md`](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/workflows/cli.md). [W50 · W50.1, W50.2](#w50--resume-the-same-task-after-an-interrupted-run) After W49.

### W50 · Resume the same task after an interrupted run

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

An authored task or checked box establishes intent or progress. It does not establish a dispatched provider, an observed candidate or the state of an interrupted write.

#### Expected outcome

The developer can recover the last confirmed execution or evidence boundary without duplicate task effects.

#### Scope

Use the original run and provider status, revision and task bindings. Keep unresolved external effects uncertain until reconciled.

#### Specification

Parent: [S31](./specification.md#s31--verify-and-resume-one-authorized-implementation). Supports [S31.1](./specification.md#s31-1) and [F31.1](./specification.md#f31-1). R27/A27. Owner role: skill maintainer. Requires [W49](#w49--hand-one-approved-task-to-the-selected-implementation-provider). Reuse its task packet and candidate evidence; interrupt only the boundary needed for this check.

#### Acceptance criteria

- **W50.1** Interrupt one authorized task before its outcome is recorded. Resume the same feature and run, recover the task, criterion and last observed candidate, and identify the next safe action from provider evidence. <a id="w50-1"></a>
- **W50.2** When prior dispatch may have taken effect, consult available authoritative state. Preserve uncertainty if it cannot be resolved. Retain evidence that resumption caused no duplicate dispatch or application write. <a id="w50-2"></a>

#### Relevant files

Upstream docs/workflows/overview.md and docs/workflows/cli.md; existing writer recovery and evidence records. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/workflows/overview.md#run-review-and-resume)

#### Additional context

Ship the working entry and its consumer in one commit. Record criterion verdicts, candidate and proof under the shared Definition of Done. Implementation initially Not demonstrated.

</details>

## S32 · Route an idea or bug to the right upstream workflow

**Demonstrate the story.** Finish an idea assessment at a decision and route a reported defect to a bounded repair. [Story criteria](./specification.md#s32--route-an-idea-or-bug-to-the-right-upstream-workflow)

- [ ] T052 [US32] End idea assessment at a supported decision. `references/decision_record.md`. [W51 · W51.1, W51.2](#w51--end-idea-assessment-at-a-supported-decision) After the connected W47–W50 path, with brief and interview routes. Only W51.1 and W51.2 are approved.

### W51 · End idea assessment at a supported decision

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The approved writing routes describe relevant outputs. The optional upstream assessment and bug workflows also need a handoff that preserves their distinct starting points and authority.

#### Expected outcome

An unshaped idea produces a grounded brief, decision recommendation or focused question.

#### Scope

Adapt the optional idea assessment entry to existing formats and decision authority.

#### Specification

Parent: [S32](./specification.md#s32--route-an-idea-or-bug-to-the-right-upstream-workflow). Supports [S32.1](./specification.md#s32-1) and [F32.1](./specification.md#f32-1). R28/A28. Owner role: skill maintainer. Requires [W47](#w47--start-one-feature-through-an-optional-workflow-extension) and existing brief/interview routes. No coding or mandatory feature spec on intake.

#### Acceptance criteria

- **W51.1** Supply an idea with a consequential evidence gap. The assessment names that gap, identifies who can decide and recommends clarification or stopping. Preserve source and output. <a id="w51-1"></a>
- **W51.2** On a supported decision to proceed, identify the next document and its benefit. A recommendation alone cannot create a task or dispatch an implementation. <a id="w51-2"></a>

#### Relevant files

Upstream workflows/assess/workflow.yml; existing decision record, interview and brief routes. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/guides/assessment.md)

#### Additional context

Ship the working entry and its consumer in one commit. Record criterion verdicts, candidate and proof under the shared Definition of Done. Implementation initially Not demonstrated.

</details>
- [ ] T053 [US32] Turn a reported defect into one bounded repair. `references/bug_report.md`. [W52 · W52.1, W52.2](#w52--turn-a-reported-defect-into-one-bounded-repair) After the connected W47–W50 path and W30–W31.

### W52 · Turn a reported defect into one bounded repair

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The approved writing routes describe relevant outputs. The optional upstream assessment and bug workflows also need a handoff that preserves their distinct starting points and authority.

#### Expected outcome

A defect reaches a source-grounded bug report or independent repair Issue with its expected observable check.

#### Scope

Use the optional bug route and the project’s established parent rules. Separate observed symptom, expected behavior and unconfirmed cause.

#### Specification

Parent: [S32](./specification.md#s32--route-an-idea-or-bug-to-the-right-upstream-workflow). Supports [S32.1](./specification.md#s32-1) and [F32.1](./specification.md#f32-1). R28/A28. Owner role: skill maintainer. Requires [W47](#w47--start-one-feature-through-an-optional-workflow-extension) and [W30](#w30--choose-a-task-or-story-for-an-improvement)–[W31](#w31--choose-a-feature-epic-or-delivery-plan). Reuse the existing bug and Issue authoring routes.

#### Acceptance criteria

- **W52.1** Given one observed save failure with a known expected outcome, produce a repair record with the observation, the expected result and the smallest check that distinguishes them. <a id="w52-1"></a>
- **W52.2** Given only a suspected cause, keep it provisional. A bounded independent repair needs no fabricated story or PRD and writing it cannot authorize execution. <a id="w52-2"></a>

#### Relevant files

references/bug_report.md and references/issue.md; upstream workflows/bugfix/workflow.yml. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/guides/assessment.md)

#### Additional context

Ship the working entry and its consumer in one commit. Record criterion verdicts, candidate and proof under the shared Definition of Done. Implementation initially Not demonstrated.

</details>

## S37 · Write the requested document and pass it to the right consumer

**Demonstrate the story.** Request a supported format and follow its reviewed output into the task that needs it. [Story criteria](./specification.md#s37--write-the-requested-document-and-pass-it-to-the-right-consumer)

- [ ] T054 [US37] Request any supported writing format through the workflow. `contracts/documents.json`. [W58 · W58.1, W58.2](#w58--request-any-supported-writing-format-through-the-workflow) After W47 and W35, with the approved document routes on the candidate.

### W58 · Request any supported writing format through the workflow

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The existing workflow acceptance case exercises a feature specification. A developer also needs a direct entry to the writer’s other supported formats.

#### Expected outcome

A developer using the optional entry receives the requested document in its native format and can stop there.

#### Scope

Extend the borrowed command at the writer boundary to resolve full names and supported aliases using the existing catalog. Preserve edit scope, discovery, checked delivery, native format and host authority. Apply the same public naming rule as W46. Use the existing routing mechanism for the seven approved forms as they ship.

#### Specification

Parent: [S37](./specification.md#s37--write-the-requested-document-and-pass-it-to-the-right-consumer). Supports [S37.1](./specification.md#s37-1) and [F37.1](./specification.md#f37-1). R33/A33. Owner role: skill maintainer. Requires the [W47](#w47--start-one-feature-through-an-optional-workflow-extension) entry, [W35](#w35--launch-three-document-types-in-claude-code) routing, and the approved document routes whose coverage is being accepted. This increment can ship independently of [W59](#w59--carry-a-reviewed-document-into-a-dependent-task).

#### Acceptance criteria

- **W58.1** Given the candidate’s catalog, output contracts and A10a–g, resolve every supported kind and advertised alias through the optional entry. Compare the selected owner, contract or named variant to standalone routing. Documented guidance-only entries retain their role. A missing kind, generic fallback, wrongly shared contract or lost native format fails. Save the candidate and the catalog differences. This is a routing comparison, so it requires no generated document per alias. <a id="w58-1"></a>
- **W58.2** Given a project and enough verified input, request a Tutorial through the installed workflow and follow its normal checked-delivery path. Retain the tutorial, its own contract/receipt and the observed endpoint. An unrelated specification, work item or provider dispatch fails. Exercise the shared route once and reuse W47’s host observations wherever the adapter is unchanged. <a id="w58-2"></a>

#### Relevant files

`SKILL.md`, `contracts/documents.json`, `references/tutorial.md` and the installed command adapter introduced by W47. Use the [upstream source mapping](./implementation-plan.md#reuse-the-upstream-implementation).

#### Additional context

Commit the accepting entry and its catalog coverage together. Record each criterion’s verdict, candidate and proof under the shared Definition of Done. Initial status is Not demonstrated.

</details>
- [ ] T055 [US37] Carry a reviewed document into a dependent task. `references/low_level_design.md`. [W59 · W59.1, W59.2](#w59--carry-a-reviewed-document-into-a-dependent-task) After W58, W48 and W38–W39.

### W59 · Carry a reviewed document into a dependent task

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

Feature tasks need the actual rules in linked documents, including documents beyond the upstream feature templates.

#### Expected outcome

A task author receives the selected document’s relevant constraint and can see when a source revision needs attention.

#### Scope

Adapt the existing document handoff where the workflow prepares the next eligible document or task. Preserve the writer’s prerequisite, authority, revision and evidence rules. Use an exact link or scoped view. Keep W48’s task representation and the shipped execution sequence.

#### Specification

Parent: [S37](./specification.md#s37--write-the-requested-document-and-pass-it-to-the-right-consumer). Supports [S37.1](./specification.md#s37-1) and [F37.1](./specification.md#f37-1). R33/A33. Owner role: skill maintainer. Requires [W58](#w58--request-any-supported-writing-format-through-the-workflow), [W48](#w48--select-eligible-tasks-from-the-feature-list) and [W38](#w38--show-the-next-useful-document)–[W39](#w39--continue-a-checked-document-handoff). Use the project’s existing Issue, story and Low Level Design (LLD). An unrelated document has no new prerequisite.

#### Acceptance criteria

- **W59.1** Given an authorized refund feature, a story and a reviewed design stating that only a manager may approve a refund, use the workflow to prepare its child Issue. Inspect the Issue at the task consumer. It names the story, the exact design revision and section, and the employee-denial criterion. A generic “check permissions” or a sibling feature’s design fails. Keep the actual source and consumer view. <a id="w59-1"></a>
- **W59.2** Given the same task with an unresolved revision change in its referenced design, request the next dependent action. The workflow identifies the affected source and stops that dispatch while preserving the documents, prior evidence and unrelated work. Keep the observed refusal and source identifiers. Reuse W48 evidence if it already exercises this document boundary on this candidate. <a id="w59-2"></a>

#### Relevant files

`references/low_level_design.md`, `references/issue.md`, the W38–W39 handoff and W48’s actual task consumer.

#### Additional context

Commit the connected handoff and its safe failure together. Apply the shared Definition of Done and record each criterion’s verdict, candidate and proof. Initial status is Not demonstrated.

</details>

## S33 · Distribute and safely update the versioned integration

**Demonstrate the story.** Update and remove the installed integration while preserving project-authored work. [Story criteria](./specification.md#s33--distribute-and-safely-update-the-versioned-integration)

- [ ] T056 [US33] Distribute and safely update the versioned integration. `scripts/install_skill.py`. [W53 · W53.1, W53.2](#w53--distribute-and-safely-update-the-versioned-integration) After W47–W50, W58–W59 and the entry points included in the release.

### W53 · Distribute and safely update the versioned integration

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The standalone installer preserves an existing destination. The optional ecosystem integration also needs a declared compatible upstream version, identifiable managed components and a safe upgrade or removal path.

#### Expected outcome

A team can install a versioned artifact, see what won resolution, update owned components and remove them safely.

#### Scope

Create a testable local release and user instructions. Use an upstream bundle only if it adds value and components resolve. External registry submission and remote release are separate actions.

#### Specification

Parent: [S33](./specification.md#s33--distribute-and-safely-update-the-versioned-integration). Supports [S33.1](./specification.md#s33-1) and [F33.1](./specification.md#f33-1). R29/A29. Owner role: skill maintainer. Requires the connected [W47](#w47--start-one-feature-through-an-optional-workflow-extension)–[W50](#w50--resume-the-same-task-after-an-interrupted-run) path and the entry points included in the release. Reuse earlier host observations for unchanged behavior.

#### Acceptance criteria

- **W53.1** Install the release against its declared upstream version. Inspect the active command or template source, upgrade from the prior supported package and remove the owned integration. The working feature document and another command remain available. <a id="w53-1"></a>
- **W53.2** Supply an incompatible upstream version or a conflicting user-edited component. Identify the constraint and preserve user content. Retain the observed version, ownership decision and before/after paths; no registry publish is necessary. <a id="w53-2"></a>

#### Relevant files

Upstream docs/bundles/overview.md, docs/overview/artifacts.md and docs/upgrade.md; installer and public usage documentation. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/bundles/overview.md)

#### Additional context

Ship the working entry and its consumer in one commit. Record criterion verdicts, candidate and proof under the shared Definition of Done. Implementation initially Not demonstrated.

</details>

## S39 · Find instructions for a feature or document type from the index (continued)

**Demonstrate the story.** Find each released capability and document type from the public index. [Story criteria](./specification.md#s39--find-instructions-for-a-feature-or-document-type-from-the-index)

- [ ] T057 [US39] Complete index coverage for the existing release. `README.md`. [W61 · W61.1, W61.2](#w61--complete-index-coverage-for-the-existing-release) After W54, on the identified release.

### W61 · Complete index coverage for the existing release

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

Creating a new index does not make the existing feature set discoverable.

#### Expected outcome

A reader can locate instructions for each feature and document format that the release already supports.

#### Scope

Compare released entry points, README scenarios and supported document types against the public index. Link to useful existing sections first. Fill a gap in the owning guidance or write a separate guide when the reader needs a distinct procedure or reference. Keep each correction with its index link.

#### Specification

Parent: [S39](./specification.md#s39--find-instructions-for-a-feature-or-document-type-from-the-index). Supports [S39.1](./specification.md#s39-1) and [F39.1](./specification.md#f39-1). R35/A35. Owner role: documentation maintainer. Requires [W54](#w54--publish-the-public-index-with-a-usable-focused-edit-entry) and the identified release. Use the existing catalog and index as the record.

#### Acceptance criteria

- **W61.1** Compare every released user-facing feature and supported document type with the index. Check that each link opens at the intended instructions. For a chore Issue, a link to “Issue types and titles” can pass when it identifies the chore’s inputs and the Issue guide gives the expected result. An absent type or a link that leaves the reader searching fails. Retain the candidate, coverage differences and their disposition. <a id="w61-1"></a>
- **W61.2** Reuse W54’s focused-edit evidence and open the review entry on the same release. The review guidance returns located findings and preserves the reviewed document. Distinct, useful headings in one file pass. A broken heading or a link to the focused-edit instructions fails even when the file exists. Retain the observed destinations. Recheck only changed links or uncovered entries. <a id="w61-2"></a>

#### Relevant files

`README.md`, `SKILL.md`, `contracts/documents.json`, the public index and the existing pages or sections it links to.

#### Additional context

Record Met, Failed or Not demonstrated per criterion and identified release. Reuse accepted increments after interruption. Initial verdicts: Not demonstrated.

</details>

## S38 · Explain the feature and report the checked result

**Demonstrate the story.** Read the feature page and session handoff against the approved rule and open decision. [Story criteria](./specification.md#s38--explain-the-feature-and-report-the-checked-result)

- [x] T058 [US38] Teach feature-page and session wording in the live style guide. `references/writing_style.md`. [W60 · W60.1](#w60--teach-feature-page-and-session-wording-in-the-live-style-guide) Reuse the accepted guide and example at `d8bf859`.

### W60 · Teach feature-page and session wording in the live style guide

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

The owner authorized an immediate guide edit following the comparative audit.

#### Expected outcome

A writer can use the shared guide for a procedure, reference lookup and checked session reply.

#### Scope

Change the feature-page and session guidance. Preserve existing format ownership, source authority and factual status.

#### Specification

Parent: [S38](./specification.md#s38--explain-the-feature-and-report-the-checked-result). Supports [S38.1](./specification.md#s38-1) and [F38.1](./specification.md#f38-1). R34/A34. Owner role: writing maintainer. Uses the completed source audit.

#### Acceptance criteria

- **W60.1** Given a manager-only approval rule and an unresolved retry decision, apply the revised guidance to a feature page and a session handoff. The two passages identify the source or decision as appropriate, retain the manager-only rule and leave runtime success unclaimed. Keep the exact guide revision and example comparison. <a id="w60-1"></a>

#### Relevant files

`references/writing_style.md` and its links to the owning format guides.

#### Additional context

Met on d8bf859f0eec178aa34b24e29aef10290e984c3b for the guide and author-applied example. The writing-style contract, repository and layout integrity checks passed. Reuse the [committed guide](https://github.com/fatonsopa/ai-technical-writer/blob/d8bf859f0eec178aa34b24e29aef10290e984c3b/references/writing_style.md#write-a-feature-page-people-can-use). The checkout layout now identifies the owner-requested plan directory. W60 needs no repeat implementation. Cross-host performance is assessed in W17.

</details>

## S08 · Follow the portable entry without grader hints (continued)

**Demonstrate the story.** Reach the intended writing route from a normal request on the identified host. [Story criteria](./specification.md#s08--follow-the-portable-entry-without-grader-hints)

- [ ] T059 [US8] Ship neutral cross-host assignments for the connected handoff. `config/host_validation.json`. [W17 · W17.1, W17.2](#w17--ship-neutral-cross-host-assignments-for-the-connected-handoff) At release, after W16 and the affected increments are integrated on the frozen candidate.

### W17 · Ship neutral cross-host assignments for the connected handoff

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

An assignment that names the expected guide can hide a routing failure.

#### Expected outcome

The evaluator can use ordinary requests and the same rubric to assess each supported host separately.

#### Scope

Deliver portable case inputs, reviewer-only expectations and candidate-bound evidence through the existing host workflow.

#### Specification

Parent: [S08](./specification.md#s08--follow-the-portable-entry-without-grader-hints). Supports [S08.1](./specification.md#s08-1) and [F8.1](./specification.md#f8-1). R7/A7. Responsible role: evaluation maintainer. Requires the integrated candidate and frozen source/host settings; use [W16](#w16--put-task-routing-before-optional-diagram-detail) and affected earlier increments.

#### Acceptance criteria

- **W17.1** Run a routine edit and the integrated feature-to-task handoff on Codex and Claude Code with the same request, sources and rubric. Record actual text, available public source-use evidence and exposed model/settings per host. <a id="w17-1"></a>
- **W17.2** Accept source-grounded equivalent wording. Reject the weakened retry or an invented parent. If routing is unobservable, record that specific limit. A pass on one host cannot satisfy the other. <a id="w17-2"></a>

#### Relevant files

[config/host_validation.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/config/host_validation.json) · [evals/host_validation_cases.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/evals/host_validation_cases.json) · [scripts/host_coverage.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/host_coverage.py) · [workflows/improve_references.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/improve_references.md)

#### Additional context

Stop at the frozen host/case selection. Reuse compatible observations. No full seven-artifact-by-host matrix or performance ranking is required.

</details>

## Finish the delivery

Verify the affected story and feature outcomes on the identified candidate. W17 owns the cross-host demonstration. Preserve the accepted W60 proof and record any missing host observation separately. [Coverage and shared Definition of Done](./implementation-plan.md#requirement-coverage)

## Proposals awaiting owner approval

The following records have no execution rows. Only a new owner decision can add them to the delivery.

### Proposed additional criterion for W51

- **W51.3** In one initialized project, follow one idea slug to its decision. With weak evidence or a missing concept, the decision identifies the blocker. Supply the missing sourced fact and recommended concept for the same idea, retain opposing evidence and confidence, and revise only the affected records. A supported go contains a handoff summary without writing a feature spec or starting implementation. For a stop, retain the decisive reason and close the assessment. Use the same records to inspect the verdict boundaries; do not repeat five live stages per verdict. <a id="w51-3"></a>

### W55 · Walk a reader through the default feature path

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

W29 and W42 explain chronology and one example in the README. W53 covers installation and upgrade. None commissions a maintained capability reference and a worked quickstart that distinguishes terminal setup from agent actions, standalone writing from optional integration, or a planned check from an observed result.

#### Expected outcome

A developer can follow one refund requirement from source intent through its spec, plan and task to the observed candidate and its acceptance evidence, with a separate on-request convergence example.

#### Scope

Use one worked Tutorial in repository docs. Name each producer, concrete path or result, next consumer and evidence boundary. Show the shorter path and where clarify, checklist and analyze help an affected decision. Map host-specific syntax to the same steps. Link W57 for executing the upstream workflow.

#### Specification

Parent: [S34](./specification.md#s34--find-a-capability-and-follow-a-feature-from-request-to-evidence). Supports [S34.1](./specification.md#s34-1) and [F34.1](./specification.md#f34-1). R30/A30. Owner role: integration documentation maintainer. Uses [W47](#w47--start-one-feature-through-an-optional-workflow-extension)–[W49](#w49--hand-one-approved-task-to-the-selected-implementation-provider) and the accepted manual boundary. Publish with verified commands and actual candidate evidence; reuse [W49](#w49--hand-one-approved-task-to-the-selected-implementation-provider)/[W57](#w57--explain-how-to-request-a-convergence-review-on-a-built-feature) observations when compatible.

#### Acceptance criteria

- **W55.1** Follow a manager-only refund request from the README. Identify the selected feature, expected actor, owning spec clause, corresponding plan decision, Issue/criterion and upstream task entry. At each step name what is now available for the next action. Show code and candidate evidence at Implement; Converge can leave tasks.md unchanged. <a id="w55-1"></a>
- **W55.2** Use one unresolved permission choice to locate clarify before planning; a requirements-quality question is answered by checklist, and a contradiction across the three documents is reported by read-only analyze before dispatch. Identify where a small writing request ends without starting a delivery. Keep the walkthrough and the located answers; no second full implementation run. <a id="w55-2"></a>

#### Relevant files

Planned public page: `docs/quickstart.md`. README.md, references/tutorial.md, the worked feature sources and the selected release’s supported command reference. [Upstream guide](https://github.github.io/spec-kit/index.html)

#### Additional context

Commit the usable page with its entry link and necessary integration adjustment. Record criterion verdicts, candidate and proof in this task. Implementation initially Not demonstrated.

</details>

### W56 · Explain an installed override from native artifact readback

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

W47 and W53 ask for the effective command or rule. They do not specify how a user lists the installed command, template, script and hook inventory or distinguishes an override from a generated feature document.

#### Expected outcome

A maintainer can reproduce the winning contribution and distinguish it from the spec and tasks generated for a feature.

#### Scope

Ship a short reference or How-to Guide (HTG) using the existing upstream CLI. Explain kinds, layered composition and additive hook registration; describe nullable provenance as reported. Keep the generated file map with the feature guide.

#### Specification

Parent: [S35](./specification.md#s35--inspect-what-the-installed-integration-exposes). Supports [S35.1](./specification.md#s35-1) and [F35.1](./specification.md#f35-1). R31/A31. Owner role: integration documentation maintainer. Uses [W47](#w47--start-one-feature-through-an-optional-workflow-extension)’s installed test project and [W53](#w53--distribute-and-safely-update-the-versioned-integration)’s release evidence where compatible. Upstream inventory is optional with the integration.

#### Acceptance criteria

- **W56.1** Run `specify artifact list --json` and then `specify artifact info <id> --json` using a real returned ID in the project with an override. The guide identifies its kind, winning contribution and visible lower layer or suppression. Distinguish participation in composition from the winning layer. <a id="w56-1"></a>
- **W56.2** Use an unknown artifact ID to show the supported lookup error. Explain where to find that feature’s spec.md separately. For a documented hook, registration alone does not establish execution. Retain the JSON and before/after project state from these read-only lookups; no new scanner, hook execution or host matrix. <a id="w56-2"></a>

#### Relevant files

Planned public page: `docs/artifacts.md`. Upstream docs/overview/artifacts.md, src/specify_cli/artifacts and the existing integration installation instructions. [Upstream guide](https://github.github.io/spec-kit/overview/artifacts.html)

#### Additional context

Commit the usable page with its entry link and necessary integration adjustment. Record criterion verdicts, candidate and proof in this task. Implementation initially Not demonstrated.

</details>

### W57 · Explain how to request a convergence review on a built feature

<details>
<summary>Scope, acceptance criteria and evidence</summary>

#### Description

W49–W50 cover dispatch, verification and resume, but leave the public operator entry and the instructions for a user-requested Converge review unspecified. The pinned bundled YAML ends at Implement. Its spec and plan gates have separate verdicts.

#### Expected outcome

The operator can run the upstream definition, inspect or resume the correct run, and choose a separate convergence review upon user request.

#### Scope

Use upstream status, resume and gate behavior on the pinned release. State terminal versus agent actions. The writer does not ship a replacement YAML workflow, automatically loop, or give approval on the user’s behalf. Preserve documents, task IDs, history and provider ownership.

#### Specification

Parent: [S36](./specification.md#s36--document-an-on-request-convergence-review-after-the-upstream-workflow). Supports [S36.1](./specification.md#s36-1) and [F36.1](./specification.md#f36-1). R32/A32. Owner role: integration documentation maintainer. Uses [W47](#w47--start-one-feature-through-an-optional-workflow-extension)–[W50](#w50--resume-the-same-task-after-an-interrupted-run). Coordinate the same run and fixture with [W49](#w49--hand-one-approved-task-to-the-selected-implementation-provider)/[W50](#w50--resume-the-same-task-after-an-interrupted-run) and the [W55](#w55--walk-a-reader-through-the-default-feature-path) tutorial. [W53](#w53--distribute-and-safely-update-the-versioned-integration) distribution can link this guide as soon as the workflow is supported.

#### Acceptance criteria

- **W57.1** In the upstream run for the refund feature, observe separate spec and plan reviews. Use status and, at a genuine pause, resume the same run. Record the Implement result, active feature, Issue revision and candidate. When explicitly requested, manual Converge on the matching feature yields an observed outcome distinct from the workflow exit. <a id="w57-1"></a>
- **W57.2** For a named unmet criterion, an appended task is reconciled to its source Issue before another implementation. Preserve the append and original failure when refreshing a generated task view. Extra scope remains for the owner. With no gap, show no appended task. Reuse the failing and corrected W49 outcomes; demonstrate any unobserved branch at the smallest affected boundary. <a id="w57-2"></a>

#### Relevant files

Planned public page: `docs/workflows.md`. Upstream workflows/speckit/workflow.yml, docs/workflows/overview.md, templates/commands/converge.md and the existing implementation and recovery evidence. [Upstream guide](https://github.github.io/spec-kit/workflows/overview.html)

#### Additional context

Commit the usable page with its entry link and necessary integration adjustment. Record criterion verdicts, candidate and proof in this task. Implementation initially Not demonstrated.

</details>
