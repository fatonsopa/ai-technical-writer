# Technical Writer implementation plan

Status: Scope approved for implementation on the handoff computer. Revision 7. The [behavioral specification, revision 7](./specification.md) owns the requirements. The [audit](./audit.md) owns the twenty-two findings. This plan assigns each finding one epic, identifies its child story and commissions individually shippable tasks against that story.

## Goal and specification

Deliver one local Technical Writer candidate that can author complete specification-driven documents for any project and pass meaningful requirements from one document to the next. Mirai is one source of examples and facts. Technical Writer owns document structure and authoring. A project owner approves product decisions and any application change. Confirm or reconcile the audited skill baseline `4a8e7c92e20404f05e68708c1a3ea26c6961b178` before freezing implementation scope.

## Current context and approach

Use the actual [User Story (US) template](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/user_story.md) for the parent outcome and child story, and the [Issue template](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) for each task. Titles below preserve independent task IDs. Each story’s scope identifies its epic; each task’s Specification names its story criterion. One child story is sufficient for each finding’s first usable outcome.

**Artifact production order.** Use the [numbered dependency rules](./specification.md#production-order) and [seven artifact acceptance cases](./specification.md#seven-authoring-cases-and-hierarchy-acceptance). With unresolved intent, interview → brief → product definition. Separate independently deliverable capabilities before writing their individual specifications. Research precedes any dependent design choice. Requirements review needs an identified specification; critical journey verification needs a mapped surface. From an established feature or epic, write the story first and its child tasks second. A standalone issue states its own authority and proof. Verification criteria are written before implementation; evidence is attached after execution.

**One task, one releasable change.** Include the working entry point, necessary consumers, guidance, example and affected checks in the same commit. A task that introduces an artifact must ship a route from an ordinary request to complete reviewed output. Use a section or existing document contract when it can faithfully deliver the requested form. If it cannot, extend the existing routing and validation mechanism with the smallest compatible named variant. Preserve old receipts by version. Never certify a fragment as a complete standalone document.

**Short feedback loop.** Before changing the skill, try the task’s named counterexample at its actual boundary or reuse the audit observation when its inputs still match. Fix the first demonstrated mismatch, inspect the same outcome and stop when its criteria and relevant shared obligations pass. A new input, failed boundary or missing criterion is the reason for another check. An unrelated failure gets its own disposition. Keep the original failure. On acceptance, record the exact commit, evidence and reviewer in the issue and hand the usable increment to its consumer.

The owner approved the work order, scope and local integration authority. Start with the execution prompt in the repository’s [execution guide](./README.md). Use this plan for dependencies, task boundaries, required evidence and closure. Keep the private JSON execution log described in the starting prompt. Reuse native run records and document the reason for each extra verification before it runs.

## Work sequence

Use the accepted Skill Builder candidate from its implementation plan. Begin with W01 and W03 to get a literal and a source reference through a real consumer. W20 makes the parent chain usable. The seven document routes can then draw on one initiative’s source packet: where intent is unknown, use W12 before W09; W10 precedes dependent feature specifications; W13 precedes design that depends on its research; W05 precedes W06; W04 reviews a drafted specification. Other stories may proceed once their named inputs and shared interfaces are settled. The order below groups by finding for lookup. W24 uses the W20 parent contract. W25 precedes W26. W30 and W31 settle the selection rules before W29 publishes the sequence after its linked routes exist. W32 precedes W33, then W34 applies the route across the catalog. W17 is the final integrated host check and reuses these assignment inputs where applicable. Plan-level A10 requires all seven outputs and their consumer observations. Each has one owning epic and task. All epic, story and task implementation verdicts are currently **Not demonstrated**.

### F1 · Preserve the project’s literal identifiers

As a maintainer, I want a naming rule that protects consumed values, so that examples remain executable.

#### Acceptance criteria

- **F1.1** Given the mixed fixture and a real document reference, edit them and derive the domain from the result. The fixture and quote keep their bytes and the document name follows the adopted convention. Save the input, output and derived value.

#### Scope and sources

Parent: this plan. Owner role: maintainer. Child: S01. R1/A1. Covers the demonstrated fixture defect and the writing rule. [Audit finding F1](./audit.md#f1--high--a-documented-naming-convention-corrupted-a-test-fixture)

#### S01 · Edit a mixed passage without corrupting its fixture

As a writer, I want to distinguish a name from a literal, so that I can improve prose safely.

##### Acceptance criteria

- **S01.1** The consuming fixture produces the original domain after the edit. A genuine document label is still recognised. Reuse W01 and W02 evidence.

##### Scope and sources

Parent: F1. Owner role: writer. W01 and W02. D1 authorizes the first-use convention.

##### W01 · Repair the Websites Review fixture and its consumers

###### Description

The worked example expanded the key US into a document name.

###### Expected outcome

An administrator can use the published fixture table and its dependent cases again.

###### Scope

Restore the key and all affected references within the worked example. Preserve legitimate document labels.

###### Specification

Parent: S01. Supports S01.1 and F1.1. R1/A1. Responsible role: example maintainer. Use the audited fixture and its domain rule.

###### Acceptance criteria

- **W01.1** Read the corrected row and apply the documented lowercase rule. The emitted domain is `__test_wrs-us.co.uk`, and the cited tests select that same row. Save the row and derived domain.
- **W01.2** A genuine document reference in the example retains its agreed meaning. Compare the scoped diff and the consuming cases.

###### Relevant files

[examples/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/test_specification.md) · [references/writing_style.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md)

###### Additional context

One fixture derivation and affected reference lookup suffice. No application deployment is involved.

##### W02 · Protect literal values during ordinary edits

###### Description

A naming convention can alter data even when the prose looks better.

###### Expected outcome

An editor can handle a literal, quoted text and a genuine document name in one passage.

###### Scope

Update the owning guidance and its naming check together if the agreed rule changes. Keep consumed full labels and aliases.

###### Specification

Parent: S01. Supports S01.1 and F1.1. R1/A1. Responsible role: style maintainer. Use W01. D1 authorizes first-use expansion in authored prose. User requests may use either spelling at any turn.

###### Acceptance criteria

- **W02.1** Edit the mixed passage through the normal route. The fixture and quoted bytes survive while the genuine label matches the adopted rule. Retain the excerpt and checker result.
- **W02.2** Change only prose phrasing to a valid alternative. It remains eligible; deliberately altering the fixture fails the consumer comparison.

###### Relevant files

[references/writing_style.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md) · [scripts/writing_style_contract.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/writing_style_contract.py) · [scripts/test_document_names.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/test_document_names.py)

###### Additional context

Use the W01 fixture as the counterexample. Stop when literal preservation and legitimate editing are both observed.

### F2 · Trace assigned work back to its real source

As a plan reviewer, I want to resolve requirements and parent links, so that unsupported work is found before implementation.

#### Acceptance criteria

- **F2.1** Follow a real requirement to its story, task and proof. Removing an owner, inventing an ID or filing a child without its parent produces a located gap. A justified safeguard and a genuine standalone fix remain eligible.

#### Scope and sources

Parent: this plan. Owner role: plan reviewer. Child: S02. R2/R3/R10/R11; A2/A3/A10g/A11. Scope includes the review artifact that an implementer consumes. [Boundary enforcement, 06:10–06:53](https://www.youtube.com/watch?v=O_zcc6Xl12g&t=370s) [Audit finding F2](./audit.md#f2--high--a-valid-plan-can-name-a-nonexistent-requirement)

#### S02 · Commission a task from a reviewed requirement

As a plan author, I want to expose broken links before commissioning work, so that the implementer can recover authority from the packet.

##### Acceptance criteria

- **S02.1** Open the work packet without the original chat. Resolve the intended parent and revision, identify the review verdict, and detect an altered mapping. Retain the packet and located diagnostics.

##### Scope and sources

Parent: F2. Owner role: plan author. W03, W20 and W11. Reuse the requirements-quality verdict from F19 when required.

##### W03 · Resolve coverage in both directions

###### Description

A structural pass accepted WEB-999 when it displaced WEB-09.

###### Expected outcome

A plan reviewer can locate a broken citation, an uncovered requirement and unjustified work in the current work record.

###### Scope

Bind explicit references to a declared source. Allow exact sections and documented safeguards. Self-contained documents keep their existing route.

###### Specification

Parent: S02. Supports S02.1 and F2.1. R3/A3. Responsible role: plan maintainer. Use the retained mutation and its valid original.

###### Acceptance criteria

- **W03.1** Submit the correct and displaced rows. Report the consumer row, missing ID, searched revision, lost coverage and correction. An unavailable source is identified separately.
- **W03.2** Inspect the reverse mapping: an unowned criterion remains open; work with a supported safeguard remains eligible. For a project without IDs, an exact section link resolves.

###### Relevant files

[references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md) · [examples/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/implementation_plan.md) · [scripts/check_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/check_document.py) · [scripts/document_contracts.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/document_contracts.py)

###### Additional context

Use the existing comparison; add a mechanical check only for decidable references. Human review assesses meaning. [Actionable diagnostics, 08:55–09:11](https://www.youtube.com/watch?v=O_zcc6Xl12g&t=535s)

##### W20 · Resolve feature, story and task ancestry before drafting

###### Description

A task can look ready even when nobody can say which story it supports.

###### Expected outcome

An ordinary request for a child task first resolves the story, its criterion and the feature or epic that owns its outcome.

###### Scope

Teach the order at discovery and issue/story entry. Preserve stable independent IDs on reparenting. An expressly standalone task may establish scope inline.

###### Specification

Parent: S02. Supports S02.1 and F2.1. R2/R11/A2/A11. Responsible role: workflow maintainer. Use W03’s declared references.

###### Acceptance criteria

- **W20.1** Create a child story for an identified epic, then a task for one story criterion. The reader recovers both source revisions and the shared outcome.
- **W20.2** With the story absent, the epic absent, or a stale or contradictory parent, locate the broken edge and withhold dependent readiness. An explicitly independent broken-link fix can proceed with its own source and expected destination. A missing child parent never silently becomes standalone.

###### Relevant files

[workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [references/user_story.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/user_story.md) · [references/issue.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md)

###### Additional context

Use the valid chain and mutations on that chain; test the standalone branch once. No external tracker write.

##### W11 · Write an epic whose stories prove a usable outcome

###### Description

A list of closed tickets can hide an incomplete delivery.

###### Expected outcome

A planner can write a parent epic with linked stories, bounded child issues and its own integrated proof.

###### Scope

Use the existing User Story (US) and Issue templates in the plan or tracker. Preserve related observations before assigning independent work.

###### Specification

Parent: S02. Supports S02.1 and F2.1. R2/R11/A2/A11. Responsible role: story-guidance maintainer. Use W20 and a known feature outcome; use W10 if scope spans capabilities.

###### Acceptance criteria

- **W11.1** For an initiative with related reports, write a parent epic, a usable child story and a scoped task. The parent exposes non-goals, dependencies, integrated proof and ownership. Each child inherits the right criterion.
- **W11.2** Close all child tasks while withholding the parent’s integrated observation. The epic stays unaccepted. A plausible common cause remains provisional; preserve both original observations.

###### Relevant files

[references/user_story.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/user_story.md) · [references/issue.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md) · [examples/user_story.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/user_story.md)

###### Additional context

Use the same chain used in W20 when compatible. Check the parent outcome once rather than recreating each child test.

### F3 · Prove behavior at the surface the user reaches

As a verifier, I want to connect a named feature to an observable outcome, so that a valid ID cannot hide weaker behavior.

#### Acceptance criteria

- **F3.1** Follow a named surface through a critical journey into a real criterion. The proof rejects a reachable but incorrect result and preserves uncertainty when the available record does not establish the result.

#### Scope and sources

Parent: this plan. Owner role: verifier. Child: S03. R3/R8/R10; A3/A8/A10e/A10f. [Feature mapping, 09:58–10:52](https://www.youtube.com/watch?v=PaPpyQocMww&t=598s) [Audit finding F3](./audit.md#f3--high--even-a-resolved-id-can-conceal-weaker-behavior)

#### S03 · Verify one critical journey against its source

As a test author, I want a feature map and linked journey with a falsifiable check, so that I can tell what actually happened.

##### Acceptance criteria

- **S03.1** Resolve every step to a surface, exercise the stated boundary in the written verification case and distinguish the expected observation from its closest false positive. Save the linked documents and judgments.

##### Scope and sources

Parent: F3. Owner role: test author. W21 consumes the outputs of F17 and F18. The assignment authors documentation; application behavior needs its own execution evidence.

##### W21 · Preserve conditions and reopen stale evidence

###### Description

A valid requirement ID can survive while a permission, limit or operation disappears.

###### Expected outcome

A reviewer can reject a weakened case and invalidate only evidence affected by a changed source.

###### Scope

Extend the connected Websites Review example and review method, including meaningful negative cases, lifecycle verdicts and candidate binding.

###### Specification

Parent: S03. Supports S03.1 and F3.1. R3/R8/A3/A8. Responsible role: verification maintainer. Use W03 and a reachable example; W06 supplies one.

###### Acceptance criteria

- **W21.1** Given T16 and 1,001 rows, the written check distinguishes 500 confirmed, 500 unresolved and one unattempted after response loss. A fresh read precedes any offered retry, and only the administrator chooses it. A request count or automatic retry fails.
- **W21.2** Keep an ID but weaken a material condition; the reviewer rejects it. Change its governing revision and retain the old failure and unrelated valid evidence. Compare before/after verdicts. A valid paraphrase remains eligible.

###### Relevant files

[references/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md) · [references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md) · [examples/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/test_specification.md) · [examples/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/spec_driven_development.md)

###### Additional context

The corresponding change-in-place counterexample starts with an existing value and observes the replacement. Stop at proof about the authored example. Formal verification would establish only the property it models. [Verification scope, 10:50–11:30](https://www.youtube.com/watch?v=O_zcc6Xl12g&t=650s)

### F4 · Make the approval decision intelligible from its opening

As a product owner, I want a decision summary derived from the detailed evidence, so that I know what my approval would authorize.

#### Acceptance criteria

- **F4.1** Give an independent reader the opening alone. They identify beneficiary, change, exclusion and unresolved choice and can support each from the text.

#### Scope and sources

Parent: this plan. Owner role: product owner. Child: S04. R4/A4. [Prototype and roadmap decision, 52:33–53:19](https://www.youtube.com/watch?v=y1-9yeYLJUo&t=3153s) [Audit finding F4](./audit.md#f4--medium--the-approval-reader-gets-less-help-than-the-implementing-reader)

#### S04 · Distinguish a prototype from approval to include it

As a decision owner, I want to read the proposed choice and its limits, so that I can decide without inferring approval from code.

##### Acceptance criteria

- **S04.1** The reader distinguishes what the prototype showed from the pending owner decision. A superficially supporting quote cannot justify the wrong answer.

##### Scope and sources

Parent: F4. Owner role: decision owner. W07 and W08. Use a sourced product example with one exclusion.

##### W07 · Write the approval opening from the detailed product evidence

###### Description

The opening currently names the problem without necessarily exposing the choice.

###### Expected outcome

The product author can draft the detail, then present a decision-first opening with sourced tradeoffs.

###### Scope

Extend the product guide and example. Only use this opening where approval matters.

###### Specification

Parent: S04. Supports S04.1 and F4.1. R4/A4. Responsible role: product-guidance maintainer. Use prototype evidence and an unresolved inclusion decision.

###### Acceptance criteria

- **W07.1** Read only the opening; identify the affected user, proposed change, excluded behavior and actual choice. Each matches the detail.
- **W07.2** A working prototype remains evidence of feasibility. The opening must leave inclusion pending until the owner decides.

###### Relevant files

[references/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/product_requirements_document.md) · [examples/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/product_requirements_document.md)

###### Additional context

Keep the opening and detailed baseline. No invented cost, budget or new executive summary for a routine issue.

##### W08 · Judge the reader’s decision against the owning detail

###### Description

Finding a real quotation can still support an incorrect answer.

###### Expected outcome

A reviewer can assess an approval opening using a cold reader and source-grounded judgments.

###### Scope

Ship the reader task and review guidance together. Keep expected answers outside the reader’s assignment.

###### Specification

Parent: S04. Supports S04.1 and F4.1. R4/A4. Responsible role: evaluation maintainer. Consume W07’s opening and its original detail.

###### Acceptance criteria

- **W08.1** An independent reader given only the opening identifies the four W07 elements. Save the opening, response and comparison to detail.
- **W08.2** Use a wrong decision paired with a genuine quote and a correct alternative phrasing. The rubric rejects the former and accepts the latter for the stated reasons.

###### Relevant files

[workflows/improve_references.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/improve_references.md) · [evals/grades.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/evals/grades.py) · [references/decision_record.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/decision_record.md)

###### Additional context

One cold read for the representative material decision. Reuse it at release; no reader run on every document.

### F5 · Write a brief for a product decision

As a product lead, I want a brief grounded in the problem and available evidence, so that I can decide whether to pursue the opportunity.

#### Acceptance criteria

- **F5.1** From the supplied opportunity, read the brief and identify the affected person, desired outcome, exclusion and unknown baseline. An invented target fails A10b.

#### Scope and sources

Parent: this plan. Owner role: product lead. Child: S05. R2/R10, A2/A10b. The complete seven-output acceptance remains a plan-level obligation. [Related reports, 43:45–44:29](https://www.youtube.com/watch?v=6hxp0SpGxz8&t=2625s) [Audit finding F5](./audit.md#f5--high--the-product-guide-mentions-a-brief-without-defining-its-complete-handoff)

#### S05 · Decide whether an opportunity warrants product definition

As a product planner, I want a short account of the beneficiary, outcome and known constraints, so that the owner can decide whether a fuller product definition is useful.

##### Acceptance criteria

- **S05.1** Read the authored brief without the original conversation. Recover the problem, proposed outcome and uncertainty from the words on the page. Compare with A10b.

##### Scope and sources

Parent: F5. Owner role: product planner. W09. Use an interview record from F14 when needed. A request with enough evidence can enter directly.

##### W09 · Author a brief from opportunity evidence

###### Description

Requiring a full product definition during shaping makes unknowns look settled.

###### Expected outcome

An owner can request and receive a complete brief directly from Technical Writer.

###### Scope

Use a compact product-guidance variant with its own sufficient content and checked delivery. An existing interview is an input when intent needed elicitation.

###### Specification

Parent: S05. Supports S05.1 and F5.1. R2/R10/A2/A10b. Responsible role: product-guidance maintainer. Use sourced intent or an interview record from W12.

###### Acceptance criteria

- **W09.1** From a supplied need and an unknown baseline, author problem, beneficiary, desired outcome, non-goals and unresolved choices. Identify the source and any supplied appetite.
- **W09.2** Give the brief to the product author. They can recover the decision and missing baseline. An invented budget, target or approval fails.

###### Relevant files

[references/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/product_requirements_document.md) · [examples/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/product_requirements_document.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

###### Additional context

One brief with an explicit unknown proves the distinction; retain its checked output for downstream use.

### F6 · Ground discovery and research in actual evidence

As a requirements owner, I want to distinguish sourced answers, hypotheses and delegated choices, so that the specification reflects what is known and what I still need to decide.

#### Acceptance criteria

- **F6.1** Given an ambiguous request, the first question identifies the consequential unknown. Given settled evidence, the writer proceeds. An answer changes the next requirement or proof only within the owner’s authority.

#### Scope and sources

Parent: this plan. Owner role: requirements owner. Child: S06. R5/R10; A5/A10a/A10d. [Diagnosis without the governing source, 14:53–15:20](https://www.youtube.com/watch?v=vFYVF7IC8Zw&t=893s) [Audit finding F6](./audit.md#f6--medium--the-discovery-process-is-sound-but-its-best-lessons-are-difficult-to-imitate)

#### S06 · Carry discovery evidence into the next authoring decision

As a writer, I want a reviewable record of what was said and what was investigated, so that the brief and design can cite evidence separately.

##### Acceptance criteria

- **S06.1** Inspect the writer’s first question, the owner’s answer and the resulting criterion. The answer settles one branch. Supplied evidence can settle it without an interview.

##### Scope and sources

Parent: F6. Owner role: writer. W28. F14 owns the deliverable interview record and F16 owns the research record.

##### W28 · Ask the question that changes the requirement

###### Description

A generic interview can anchor a decision the owner has yet to make.

###### Expected outcome

The discovery guide shows how to follow an open answer or proceed with complete evidence.

###### Scope

Ship one contrast at the existing discovery entry. Keep capture of a requested interview record in W12.

###### Specification

Parent: S06. Supports S06.1 and F6.1. R5/A5. Responsible role: discovery maintainer. Use the documented ambiguous review-delay request and an otherwise identical request with the delay already identified.

###### Acceptance criteria

- **W28.1** With the delay unspecified, the first question can distinguish two delays. Given the owner’s answer, the next criterion uses the identified delay without inventing a target. Save the exchange and criterion.
- **W28.2** With the delay and acceptance already supplied, the writer proceeds without asking again. Inspect the resulting criterion and stop.

###### Relevant files

[Discovery](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [Interview-me](https://github.com/addyosmani/agent-skills/blob/8c99fa36d90068c82d547f7c12a9d67a3e95f4ee/skills/interview-me/SKILL.md#L53-L90) · [Grilling](https://github.com/mattpocock/skills/blob/abeeaf95660ba9e8b7c753eb38f441ca707a8823/skills/productivity/grilling/SKILL.md)

###### Additional context

One commit ships the guidance and its worked contrast. Record verdict and evidence against the exact candidate under the shared Definition of Done.

### F7 · Speak plainly about results, blockers and decisions in the session

As a project owner, I want a clear update and a traceable final handoff, so that I know what changed and whether a decision needs me.

#### Acceptance criteria

- **F7.1** Observe a progress update, a real blocker, a decision request and a checked delivery. The delivery agrees with the accepted bytes; a modified decision sentence fails verification while an old receipt still verifies.

#### Scope and sources

Parent: this plan. Owner role: project owner. Child: S07. R6/A6. Shared wording rules apply to both hosts. [Audit finding F7](./audit.md#f7--medium--session-messages-report-validation-more-reliably-than-the-users-result)

#### S07 · Receive the right next action and a checked result

As a reader, I want the fact or decision relevant to this moment, so that I can proceed without guessing.

##### Acceptance criteria

- **S07.1** Compare each public message to its observed state or reviewed content. Preserve the decision owner and the version-specific exact-message guarantee.

##### Scope and sources

Parent: F7. Owner role: reader. W14 and W15. Manual instructions apply only when there is an action the user must perform.

##### W14 · Write progress, decision and blocker messages from evidence

###### Description

A generic status can leave the user unsure what to do.

###### Expected outcome

The writer gives a concise public update that matches the observed state and any required action.

###### Scope

Ship contrasting session examples through shared style guidance. F13 owns the scope of the file-based check.

###### Specification

Parent: S07. Supports S07.1 and F7.1. R6/A6. Responsible role: style maintainer. Use a confirmed result, unresolved choice and genuine external blocker. Use W22’s source-preservation rule where available.

###### Acceptance criteria

- **W14.1** For a confirmed intermediate result, the message names the change and consequence. For a blocker it gives the last confirmed fact, missing input and responsible party.
- **W14.2** For a decision, give supported options, tradeoff and recommendation. Routine delivery with no user action contains no invented manual steps. Compare actual messages to facts.

###### Relevant files

[references/writing_style.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md) · [evals/style_cases.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/evals/style_cases.json) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md)

###### Additional context

For example, given a checked draft and one open owner decision, “The draft is ready. You still need to decide who can retry a failed batch” is useful only if that choice really is open. For the supplied WEB-09 case the rule is already settled; asking again fails. Inspect the existing session cases first. Add only distinctions the cases cannot demonstrate; keep source-grounded review of wording.

##### W15 · Deliver an optional reviewed decision with a verifiable receipt

###### Description

The checked handoff can force the owner to reopen the file merely to learn the decision.

###### Expected outcome

The delivery renderer and verifier support a reviewed result or choice on a new compatible path.

###### Scope

Change authored contract, renderer, verifier and affected consumers together. Preserve old messages and version identity; apply the approved D1 convention.

###### Specification

Parent: S07. Supports S07.1 and F7.1. R6/A6. Responsible role: delivery maintainer. Requires exact reviewed bytes, current delivery contract and one historical receipt.

###### Acceptance criteria

- **W15.1** Finalize a reviewed document containing a pending choice. The emitted sentence and link match reviewed content. Verification rejects an altered or unreviewed sentence.
- **W15.2** Verify an old receipt using its original format and deliver a document with no substantive action. The old record still validates and the new message adds no unsupported claim.

###### Relevant files

[contracts/delivery_message.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/delivery_message.json) · [scripts/validate_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/validate_document.py) · [scripts/test_document_delivery.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/test_document_delivery.py)

###### Additional context

Use one new handoff and one historical receipt. A renderer pass without the user-visible message is incomplete evidence.

### F8 · Reach the right guidance from an ordinary request

As a skill user, I want the same writing behavior on Codex and Claude Code, so that I can request a small edit or a connected specification without naming a reference file.

#### Acceptance criteria

- **F8.1** Use both normal hosts for one small edit and one connected assignment per host, or qualifying retained evidence. Preserve literal, governing meaning and requested scope. Keep document and routing verdicts distinct.

#### Scope and sources

Parent: this plan. Owner role: skill user. Child: S08. R7/A7. [Neutral evaluation, 19:13–20:15](https://www.youtube.com/watch?v=04FAVmmLSGc&t=1153s) [Audit finding F8](./audit.md#f8--medium--the-entry-point-spends-attention-on-the-catalog-before-the-task)

#### S08 · Follow the portable entry without grader hints

As a host evaluator, I want to observe which sources the task actually uses, so that I can distinguish compliance from prompted performance.

##### Acceptance criteria

- **S08.1** The inputs omit the expected guide and answers. Each host delivers assessable output on the identified candidate. Missing public routing evidence stays Not demonstrated.

##### Scope and sources

Parent: F8. Owner role: host evaluator. W16 and W17. Package invocation, aliases, catalog consumers and relevant visual accessibility are compatibility obligations.

##### W16 · Put task routing before optional diagram detail

###### Description

The entry repeats the catalog relationships and the name parser consumes part of that same file.

###### Expected outcome

Users reach the appropriate rule from the ordinary entry; catalog consumers and diagram readers retain a working route.

###### Scope

Move the complete explanatory relationship view and its accessible source together if needed. Keep the canonical catalog reachable by the naming parser.

###### Specification

Parent: S08. Supports S08.1 and F8.1. R7/A7. Responsible role: skill-entry maintainer. Inspect current catalog reader and diagram links before moving text.

###### Acceptance criteria

- **W16.1** Resolve an existing alias and real document name through the usual parser. An ordinary request using “PRD” first and another using “Product Requirements Document” both reach the same reference. The user can alternate forms across turns without being asked to restate the name. Save the resolved reference and reuse the same two inputs across checks.
- **W16.2** From the entry, find the short-edit route and reach the full diagram with title, accessibility information and source. Link checks target the moved content.

###### Relevant files

[SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md) · [references/writing_style.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md) · [scripts/writing_style_contract.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/writing_style_contract.py) · [scripts/test_document_names.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/test_document_names.py)

###### Additional context

Verify the changed navigation and parser once. Word count alone cannot prove the route works for users.

##### W17 · Ship neutral cross-host assignments for the connected handoff

###### Description

An assignment that names the expected guide can hide a routing failure.

###### Expected outcome

The evaluator can use ordinary requests and the same rubric to assess each supported host separately.

###### Scope

Deliver portable case inputs, reviewer-only expectations and candidate-bound evidence through the existing host workflow.

###### Specification

Parent: S08. Supports S08.1 and F8.1. R7/A7. Responsible role: evaluation maintainer. Requires the integrated candidate and frozen source/host settings; use W16 and affected earlier increments.

###### Acceptance criteria

- **W17.1** Run a routine edit and the integrated feature-to-task handoff on Codex and Claude Code with the same request, sources and rubric. Record actual text, available public source-use evidence and exposed model/settings per host.
- **W17.2** Accept source-grounded equivalent wording. Reject the weakened retry or an invented parent. If routing is unobservable, record that specific limit. A pass on one host cannot satisfy the other.

###### Relevant files

[config/host_validation.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/config/host_validation.json) · [evals/host_validation_cases.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/evals/host_validation_cases.json) · [scripts/host_coverage.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/host_coverage.py) · [workflows/improve_references.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/improve_references.md)

###### Additional context

Stop at the frozen host/case selection. Reuse compatible observations. No full seven-artifact-by-host matrix or performance ranking is required.

### F9 · Author complete documents independently of the application

As a project owner, I want Technical Writer to author every requested specification-driven file, so that my project supplies facts and retains decision authority without needing its own writer.

#### Acceptance criteria

- **F9.1** From a blank start, deliver a complete product document and linked behavioral specification for Mirai and a complete product document for a second project. Preserve sources, IDs and pending owner approval. Record any consumer incompatibility separately.

#### Scope and sources

Parent: this plan. Owner role: project owner. Child: S09. R9/A9. The audit correction assigns document structure, prose and checked delivery to Technical Writer. [Audit finding F9](./audit.md#f9--high--the-proposed-integration-gave-document-authorship-to-the-wrong-component)

#### S09 · Create a project’s first governed documents from facts

As a product author, I want to start without an application template, so that I can deliver a versioned specification and hand it to a real consumer.

##### Acceptance criteria

- **S09.1** The writer uses its own form in both projects. Follow one downstream criterion back to a source decision; withheld approval remains open. No claim of live application ingestion follows from document delivery.

##### Scope and sources

Parent: F9. Owner role: product author. W18 and W19. Covers project-independent authoring and compatibility at the consuming boundary.

##### W18 · Author a complete product document from project facts

###### Description

The superseded proposal treated an existing Mirai document as a prerequisite.

###### Expected outcome

Using the normal skill, the owner receives a complete Product Requirements Document (PRD) from facts and decisions alone.

###### Scope

Make the existing integration rule actionable in the entry, product guide and worked invocation. Preserve verified terms and owners. No application-specific authoring branch.

###### Specification

Parent: S09. Supports S09.1 and F9.1. R9/A9. Responsible role: product-guidance maintainer. Use Mirai inputs with stable IDs and one open approval; no source document template.

###### Acceptance criteria

- **W18.1** From an empty destination produce the whole product document through Technical Writer. Check its required sections, facts, scope, sources and actual owner status.
- **W18.2** Use a second project’s verified facts through the same route. It gets its own accurate content; a legacy heading or missing application template cannot prevent normal authoring.

###### Relevant files

[SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md) · [references/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/product_requirements_document.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json) · [examples/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/product_requirements_document.md)

###### Additional context

Two project inputs answer portability. Keep the first reviewed artifact for W19. Legacy forms may supply source facts only.

##### W19 · Hand an authored product requirement to the downstream specification

###### Description

A complete product document can still lose its authority or meaning at the next boundary.

###### Expected outcome

Technical Writer authors the linked behavioral specification from the W18 artifact and reports compatibility at the actual consumer.

###### Scope

Carry criterion IDs, scope, permission and source revision into the new document. Preserve historical approvals. Surface an incompatible external field at its owner.

###### Specification

Parent: S09. Supports S09.1 and F9.1. R9/R3/A9/A3. Responsible role: integration maintainer. Requires W18’s reviewed output and actual source revision.

###### Acceptance criteria

- **W19.1** From the W18 product document write a complete behavioral specification. A reader resolves the link and recovers the original obligation, exclusion and unresolved decision. Save both reviewed outputs and their bindings.
- **W19.2** Supply a conflicting consumer-format demand. Identify the incompatible field and owning interface. Preserve reviewed bytes and withhold a live-compatibility claim unless the actual consumer accepted them.

###### Relevant files

[references/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md) · [examples/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/spec_driven_development.md) · [workflows/validation_review.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/validation_review.md) · [scripts/validate_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/validate_document.py)

###### Additional context

One linked document and one conflict are sufficient. App migration, signing, external publication and runtime changes require separate authority.

### F10 · Write stories and tasks that a reader can act on

As a product owner, I want the text to tell me what a person will see and who can act, so that I can spot a wrong implementation without decoding abstract phrases.

#### Acceptance criteria

- **F10.1** Given the original partial-write wording and its governing source, an edited issue lets a reader explain the visible result, stop condition and retry authority. A fluent but weaker paraphrase fails. Preserve accurate story wording and compare the reader’s answer with A12.

#### Scope and sources

Parent: this plan. Owner role: writing-guidance maintainer. Child: S10. R12/A12. The supported defect is one worked example that teaches a vague abstraction. Keep the existing clear examples and shared writing principles. [Audit finding F10](./audit.md#f10--medium--some-worked-acceptance-criteria-hide-what-the-user-should-see)

#### S10 · Read a work item without guessing what success means

As an implementer, I want a short story and task that preserve the governing rule in concrete language, so that I can build and verify the requested behavior.

##### Acceptance criteria

- **S10.1** W22 delivers the corrected issue and a before/after example. W23 delivers the corresponding review method. Give the reader the edited task without its answer key. They recover the actor, observable result, permission and failure condition from the text. A source-grounded alternative can pass. Retain the passage, reader response and contrary example.

##### Scope and sources

Parent: F10. Owner role: issue-guidance maintainer. W22 and W23. Use F7’s cases for public session messages. Assess prose against its actual audience and writing task.

##### W22 · Replace vague acceptance text with the visible result

###### Description

The issue tells the implementer that uncertain writes are reported honestly. The source says what the administrator sees and who may choose a retry.

###### Expected outcome

The published issue is usable on its own for this criterion. A writer can follow the before/after example in the issue guide when editing another story or task.

###### Scope

Correct the worked clause, keep the surrounding limit and count refresh, and add a short contrast to the owning guide. Keep source terms where a synonym would change an ID, permission or technical meaning. Offer one plain-language rendering without prescribing identical prose.

###### Specification

Parent: S10. Supports S10.1 and F10.1. R12/A12. Responsible role: issue-guidance maintainer. Requires WEB-09–WEB-10 and the existing task and story examples.

###### Acceptance criteria

- **W22.1** Read the original clause and governing source. Edit the issue so the administrator can distinguish confirmed, uncertain and unattempted rows. It says when to stop and preserves the fresh read before offering an optional administrator retry. Save the changed passage with the source.
- **W22.2** Compare the full edited criterion with its neighbors. The 500-ID bound, refresh of confirmed rows and counts and permission survive. A clear existing story about a site leaving Review remains understandable. No invented guarantee or forced stylistic change is needed.

###### Relevant files

[Worked issue](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/issue.md#L19) · [Clear story](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/user_story.md#L18) · [Issue guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [Writing guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md)

###### Additional context

One usable example and its guidance ship in this commit. The first signal is whether the original phrase allows both an informative summary and a generic error. Reuse W21’s requirement evidence.

##### W23 · Review Markdown by what the reader can recover

###### Description

A fluent rewrite can omit an essential condition. A mechanical style check cannot tell whether a reader knows when to stop or who owns the next action.

###### Expected outcome

A reviewer can use a source-grounded reader question and a wrong paraphrase to accept a clear work item or return a specific correction.

###### Scope

Ship the review guidance, an ordinary editing request and the grader’s private comparison. Use the existing evaluation route. Keep all valid wordings eligible.

###### Specification

Parent: S10. Supports S10.1 and F10.1. R12/A12. Responsible role: evaluation maintainer. Use the corrected W22 issue and the actual upstream obligations.

###### Acceptance criteria

- **W23.1** Give a reader only the edited issue. Ask what happens after a response is lost and who may retry. Compare the answer with A12 and cite the words carrying each obligation. Missing or incorrect answers identify the exact ambiguity to fix.
- **W23.2** Present two candidate passages with similar tone. One preserves the optional retry and the other requires it. The rubric accepts the first and identifies the changed obligation in the second. A different clear wording receives the same verdict.

###### Relevant files

[Reference review workflow](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/improve_references.md) · [Existing style cases](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/evals/style_cases.json) · [Governing source](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/spec_driven_development.md#L118)

###### Additional context

Share the reader’s packet with W08 if both independently graded results can be observed without revealing either answer. Stop after a supported reader result and the wrong-meaning control. No style benchmark across the entire catalog.

### F11 · Show a complete child task for one story criterion

As a implementer, I want a child task I can use as a model, so that I can commission a bounded change.

#### Acceptance criteria

- **F11.1** Open the linked task from the worked story and recover one failed-save criterion, its governing source and proof. Assigning the whole Feature fails A13.

#### Scope and sources

Parent: this plan. Owner role: implementer. Child: S11. R13/A13. [Audit finding F11](./audit.md#f11--medium--the-worked-issue-demonstrates-a-parent-feature-when-a-child-task-is-requested)

#### S11 · Follow a failed save from story to child Issue

As a writer, I want a worked child example on the ordinary Issue route, so that I can distinguish its scope from the parent Feature.

##### Acceptance criteria

- **S11.1** Follow both links and inspect the child’s actual acceptance text against WEB-06. Retain the task and located comparison.

##### Scope and sources

Parent: F11. Owner role: writer. W24. Use the evidence and boundaries in the linked finding.

##### W24 · Publish a child Issue for the story’s failed save

###### Description

The existing Issue shows a whole Feature.

###### Expected outcome

The approved story and Issue references lead to a complete child for one criterion.

###### Scope

Add a worked child under the normal Issue route and link it from the relevant story and guide. Preserve the parent Feature and its incoming links.

###### Specification

Parent: S11. Supports S11.1 and F11.1. R13/A13. Responsible role: examples maintainer. Use the worked single-site story, WEB-06 and the parent from W20.

###### Acceptance criteria

- **W24.1** Follow the normal Issue guide to the child. It identifies the source story, the failed-save criterion and the visible error, retained selection and absence of a success message. The proof observes those effects.
- **W24.2** Follow the child’s parent link and the story’s return link. Both resolve. Comparing scope with the story rejects assignment of bulk editing to the child. Retain the linked examples and reader observation.

###### Relevant files

[Issue guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [Worked story](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/user_story.md) · [Parent Feature](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/issue.md)

###### Additional context

Commit the connected example and links together. Reuse W20’s ancestry check for unchanged edges. Record verdict and evidence against the exact candidate under the shared Definition of Done.

### F12 · Make session explanations usable from the owner’s starting point

As a project owner, I want instructions and explanations grounded in my situation, so that I can act without guessing.

#### Acceptance criteria

- **F12.1** Given a necessary handoff and a misunderstood role, a reader can name the next action or decision from the replies alone. A guessed branch or invented assignment fails.

#### Scope and sources

Parent: this plan. Owner role: project owner. Child: S12. R14/A14. [Audit finding F12](./audit.md#f12--medium--the-session-guidance-does-not-show-how-to-unblock-a-person-who-has-to-act)

#### S12 · Act on a handoff and resolve a misunderstood role

As a session user, I want a concrete starting point and clear responsibility, so that I can do the right thing.

##### Acceptance criteria

- **S12.1** Use W25’s read-only handoff and W26’s role clarification. Compare the owner’s action and role with the supplied facts.

##### Scope and sources

Parent: F12. Owner role: session user. W25, W26. Use the evidence and boundaries in the linked finding.

##### W25 · Guide the owner through one necessary manual action

###### Description

A link that works in the writer’s checkout may fail in the owner’s starting state.

###### Expected outcome

A user can perform an authorized read from their actual starting point and recognize success or a wrong reference.

###### Scope

Add the Session replies section to the shared style guide and link it from the skill entry. Reuse existing how-to instructions. Apply to an ordinary reply outside checked finalization.

###### Specification

Parent: S12. Supports S12.1 and F12.1. R14/A14. Responsible role: style maintainer. Use a supplied read-only handoff with known location, available reference, expected title and a known missing-reference response.

###### Acceptance criteria

- **W25.1** Given the owner must open the supplied document, the reply names the starting location, exact read action, expected title and safe next action for the supplied failure. A reader can follow it from that starting state.
- **W25.2** If the owner already has the document and only asks what it says, answer directly. Supplying redundant commands, guessing a path or asking the owner to make a write fails. Retain the replies and the source.

###### Relevant files

[Style guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md) · [Procedure guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/how_to_guide.md) · [Mirai session guide](https://github.com/jetmirhaxhisefa/mirai/blob/ddd183a3728d3fdd9f776755de47d4d314c8925c/registry/skills/mirai-write/guides/session.md)

###### Additional context

Ship one portable route and its usable example in one commit. Record verdict and evidence against the exact candidate under the shared Definition of Done.

##### W26 · Clarify who acts when an explanation was misunderstood

###### Description

The owner can hear “reader” as an assignment to do the work personally.

###### Expected outcome

The owner can tell who answers, who decides and what remains open.

###### Scope

Extend the same session section with one clarification example. Keep supported permission and role names.

###### Specification

Parent: S12. Supports S12.1 and F12.1. R14/A14. Responsible role: style maintainer. Requires W25’s section and a supplied choice about who answers reader questions.

###### Acceptance criteria

- **W26.1** When the owner asks whether they must write the reader answers, the first sentence resolves the misunderstanding from the supplied source. A different concrete example explains the decision still theirs. Save the reply and source passage.
- **W26.2** If the source leaves the answering role open, the reply identifies the open choice. Repeating the original unexplained role, assigning the owner new work or promising a check that never ran fails.

###### Relevant files

[Style guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/writing_style.md) · [Mirai session guide](https://github.com/jetmirhaxhisefa/mirai/blob/ddd183a3728d3fdd9f776755de47d4d314c8925c/registry/skills/mirai-write/guides/session.md#L77-L111)

###### Additional context

Ship the repair example and its acceptance comparison. Reuse W25’s route. Record verdict and evidence against the exact candidate under the shared Definition of Done.

### F13 · Keep checks proportionate for routine updates

As a session user, I want timely factual progress, so that I can see what changed.

#### Acceptance criteria

- **F13.1** Inspect the ordinary progress trace and applicable naming control. Removing a required artifact or exact-delivery check fails.

#### Scope and sources

Parent: this plan. Owner role: session user. Child: S13. R15/A15. [Audit finding F13](./audit.md#f13--medium--the-entry-requires-a-file-check-even-for-routine-session-updates)

#### S13 · Send a routine update with the appropriate checks

As a writer, I want a clear condition for running a file check, so that I can preserve evidence where the checker applies.

##### Acceptance criteria

- **S13.1** Compare the written rule and actual ordinary update with the named violation. Reuse accepted receipt evidence for unchanged behavior.

##### Scope and sources

Parent: F13. Owner role: writer. W27. Use the evidence and boundaries in the linked finding.

##### W27 · Limit routine-message checks to applicable claims

###### Description

The entry asks for a named file even when the check has nothing to assess.

###### Expected outcome

A normal update can be sent after editorial review while applicable naming and absence claims retain their checks.

###### Scope

Change the entry instruction and affected progress evaluation. Protect artifact and checked-message paths. Keep F7’s substantive delivery change separate.

###### Specification

Parent: S13. Supports S13.1 and F13.1. R15/A15. Responsible role: workflow maintainer. Use the entry, current checker’s actual predicates and existing progress case.

###### Acceptance criteria

- **W27.1** For an ordinary update with neither a document label nor absence claim, the rule permits direct delivery after source review. On the observed host the public trace shows no named-file style check for that update.
- **W27.2** For an applicable wrong canonical label, the selected check flags the offending text. Preserve the previous artifact and receipt obligations. Reuse their current evidence unless an affected path changed.

###### Relevant files

[Entry](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md#L15) · [Style checker](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/writing_style_contract.py) · [Progress case](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/evals/style_cases.json#L72)

###### Additional context

Ship the rule and affected evaluation in one commit. Claim observed operation only for the host exercised. Record verdict and evidence against the exact candidate under the shared Definition of Done.

### F14 · Read the owner’s interview answers

As a product author, I want a usable discovery interview record, so that another writer can reuse the agreed scope.

#### Acceptance criteria

- **F14.1** Brief or product author can distinguish an owner answer from a suggestion. A silent owner leaves the restatement open. Retain the output, the governing source and the consumer’s located evidence on the candidate.

#### Scope and sources

Parent: this plan. Owner role: product author. Child: S14. R10/A10a. [Audit finding F14](./audit.md#f14--high--discovery-answers-lack-a-deliverable-interview-record)

#### S14 · Use the discovery interview record at its handoff

As a product author, I want the relevant facts with their source, so that another writer can reuse the agreed scope.

##### Acceptance criteria

- **S14.1** A question changes scope or intent. Capture question, answer, source, unresolved choice, restatement and actual confirmation status. Brief or product author can distinguish an owner answer from a suggestion. A silent owner leaves the restatement open. Retain the output, the governing source and the consumer’s located evidence on the candidate.

##### Scope and sources

Parent: F14. Owner role: product author. W12. Use the evidence and boundaries in the linked finding.

##### W12 · Author the discovery interview record

###### Description

Existing questions can be useful while the next author has no durable restatement to consume.

###### Expected outcome

The requester can ask for the complete interview record; a brief author can cite it.

###### Scope

Extend discovery with the interview output, grounded dialogue, confirmation state and conditional checked delivery. Keep small independent questions together.

###### Specification

Parent: S14. Supports S14.1 and F14.1. R5/R10/A5/A10a. Responsible role: discovery maintainer. Needs the supplied conversation and explicit decisions, if any.

###### Acceptance criteria

- **W12.1** Given “make reviews faster”, ask which delay matters if evidence does not settle it. Record the answer, source, restatement and open decisions; use actual owner confirmation only.
- **W12.2** With complete sources, proceed without a new interview. If the owner is silent or a latency target is absent, preserve that uncertainty and withhold the invented target from the brief.

###### Relevant files

[workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [scripts/planning_readiness.py](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/planning_readiness.py) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

###### Additional context

One ambiguous exchange and one complete-input control; reuse the interview as W09 input. Preserve exact owner expressions when they change scope.

### F15 · Select the capability to specify next

As a specification author, I want a usable capability map, so that I can specify one independent capability.

#### Acceptance criteria

- **F15.1** The spec author selects the intended capability. Independent capabilities can be parallel. A cycle is surfaced for resolution. Retain the output, the governing source and the consumer’s located evidence on the candidate.

#### Scope and sources

Parent: this plan. Owner role: specification author. Child: S15. R10/A10c. [Audit finding F15](./audit.md#f15--high--capability-boundaries-lack-a-route-before-feature-specification)

#### S15 · Use the capability map at its handoff

As a specification author, I want the relevant facts with their source, so that I can specify one independent capability.

##### Acceptance criteria

- **S15.1** When an initiative has several independent outcomes, name stable capability IDs, responsibilities, actual dependencies and a justified build order. The spec author selects the intended capability. Independent capabilities can be parallel. A cycle is surfaced for resolution. Retain the output, the governing source and the consumer’s located evidence on the candidate.

##### Scope and sources

Parent: F15. Owner role: specification author. W10. Use the evidence and boundaries in the linked finding.

##### W10 · Map independent capabilities before specifying each one

###### Description

A broad initiative can mix separate outcomes and introduce imaginary dependencies.

###### Expected outcome

A spec author can select one stable capability, identify its scope and start its specification in the right order.

###### Scope

Author the capability map as an independently requestable planning artifact. Distinguish capability boundaries from runtime surface names.

###### Specification

Parent: S15. Supports S15.1 and F15.1. R2/R10/A2/A10c. Responsible role: planning-guidance maintainer. Requires an identified initiative; can consume the brief or product definition.

###### Acceptance criteria

- **W10.1** Given two independent capabilities and one dependent capability, write IDs, responsibilities, dependency edges and build order. Either independent starting point is eligible. The child specification cites the selected ID.
- **W10.2** Introduce a cycle. Locate it and withhold the affected order. On a single-capability request proceed directly without manufacturing a map.

###### Relevant files

[references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md) · [references/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

###### Additional context

Reuse one three-capability example. No permutation suite or formal graph service.

### F16 · Use research to resolve a design question

As a designer, I want a usable research record, so that I can distinguish evidence from a pending choice.

#### Acceptance criteria

- **F16.1** Designer can cite the finding and identify who must decide. A study or working prototype cannot silently approve a choice. Retain the output, the governing source and the consumer’s located evidence on the candidate.

#### Scope and sources

Parent: this plan. Owner role: designer. Child: S16. R10/A10d. [Audit finding F16](./audit.md#f16--high--research-findings-lack-a-handoff-before-a-design-decision)

#### S16 · Use the research record at its handoff

As a designer, I want the relevant facts with their source, so that I can distinguish evidence from a pending choice.

##### Acceptance criteria

- **S16.1** When evidence is needed before design, identify the question, sources, findings, uncertainty, supported recommendation and actual decision status. Designer can cite the finding and identify who must decide. A study or working prototype cannot silently approve a choice. Retain the output, the governing source and the consumer’s located evidence on the candidate.

##### Scope and sources

Parent: F16. Owner role: designer. W13. Use the evidence and boundaries in the linked finding.

##### W13 · Author the research record that informs a design choice

###### Description

An issue can paraphrase a retry rule and imply a cause its evidence never established.

###### Expected outcome

A designer can follow the research record to the governing passage and see what decision is still open.

###### Scope

Use the decision guide for alternatives and authority, with an explicit research form for questions, sources, findings and limits. Keep confirmation and supersession with the actual decision owner.

###### Specification

Parent: S16. Supports S16.1 and F16.1. R5/R10/A5/A10d. Responsible role: research-guidance maintainer. Requires a material question and the supplied primary source or a recorded access gap.

###### Acceptance criteria

- **W13.1** Read the source for WEB-09, compare it with a paraphrased symptom report, then author the research record. It cites the governing retry condition, alternatives and supported finding. The designer can follow the link.
- **W13.2** Remove the governing passage. The specific gap and its affected conclusion stay open. A recommendation or prototype cannot become an accepted decision.

###### Relevant files

[references/decision_record.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/decision_record.md) · [workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [examples/decision_record.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/decision_record.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

###### Additional context

Use actual supplied content or observed source access. A writer’s assertion of a read alone cannot establish it.

### F17 · Locate the feature from its map

As a verifier, I want a usable feature map, so that I can locate the feature a check must reach.

#### Acceptance criteria

- **F17.1** Journey author or verifier can locate the surface. A guessed route/handle or app launch alone cannot establish that it was reached. Retain the output, the governing source and the consumer’s located evidence on the candidate.

#### Scope and sources

Parent: this plan. Owner role: verifier. Child: S17. R10/A10e. [Audit finding F17](./audit.md#f17--high--a-verifier-cannot-request-a-complete-map-of-reachable-features)

#### S17 · Use the feature map at its handoff

As a verifier, I want the relevant facts with their source, so that I can locate the feature a check must reach.

##### Acceptance criteria

- **S17.1** For an observed surface, record its user-facing name, entry or route, verifiable control/handle, source revision and observable end state. Mark proposed surfaces explicitly. Journey author or verifier can locate the surface. A guessed route/handle or app launch alone cannot establish that it was reached. Retain the output, the governing source and the consumer’s located evidence on the candidate.

##### Scope and sources

Parent: F17. Owner role: verifier. W05. Use the evidence and boundaries in the linked finding.

##### W05 · Author a feature map from verified surfaces

###### Description

A feature name alone does not tell a verifier how to reach it.

###### Expected outcome

A verifier can use a complete feature map to locate the named screen or operation and its observable result.

###### Scope

Add the authoring route, stable surface references, a worked example and checked output through Technical Writer.

###### Specification

Parent: S17. Supports S17.1 and F17.1. R10/A10e. Responsible role: verification-guidance maintainer. Requires a source exposing at least one actual entry or operation.

###### Acceptance criteria

- **W05.1** From supplied surface evidence, write the map with name, entry, handle/action, source revision and observable end state. A verifier locates the intended surface from the row.
- **W05.2** Withhold a handle or supply an unverified future surface. The artifact marks it unverified or proposed. Launching the app cannot certify that feature.

###### Relevant files

[references/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/test_specification.md) · [examples/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/test_specification.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

###### Additional context

Use one grounded surface and one missing detail. A fabricated selector fails; a real consumer observation may be reused.

### F18 · Follow the critical journey to its observable result

As a verification author, I want a usable set of critical journeys, so that I can check the user’s whole journey.

#### Acceptance criteria

- **F18.1** Verifier resolves each referenced surface and finds the named check. An unknown screen or unrun test cannot count as verified. Retain the output, the governing source and the consumer’s located evidence on the candidate.

#### Scope and sources

Parent: this plan. Owner role: verification author. Child: S18. R10/A10f. [Audit finding F18](./audit.md#f18--high--a-critical-journey-lacks-a-checked-handoff-to-its-verifier)

#### S18 · Use the critical journeys at its handoff

As a verification author, I want the relevant facts with their source, so that I can check the user’s whole journey.

##### Acceptance criteria

- **S18.1** Given a mapped surface and sourced risk, record a journey ID, actor, ordered steps, observable result, why failure matters, source and test reference or explicit gap. Verifier resolves each referenced surface and finds the named check. An unknown screen or unrun test cannot count as verified. Retain the output, the governing source and the consumer’s located evidence on the candidate.

##### Scope and sources

Parent: F18. Owner role: verification author. W06. Use the evidence and boundaries in the linked finding.

##### W06 · Author a critical journey that consumes the feature map

###### Description

User journeys in the product guide do not establish a connection to a verifiable surface.

###### Expected outcome

A downstream tester receives a standalone journey with resolvable steps, sourced risk and evidence status.

###### Scope

Connect the journey to the map, governing requirement and test reference. Keep the original business need in the product source.

###### Specification

Parent: S18. Supports S18.1 and F18.1. R3/R10/A3/A10f. Responsible role: journey-guidance maintainer. Requires a mapped surface from W05 or compatible existing evidence.

###### Acceptance criteria

- **W06.1** Author a journey from W05. Its ID, actor, ordered steps, sourced criticality and end state are present; the tester resolves the screen and check.
- **W06.2** Use an unknown screen or remove the test. Locate the unresolved reference or state that a check is missing. The document cannot report that the journey passed.

###### Relevant files

[references/product_requirements_document.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/product_requirements_document.md) · [references/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/test_specification.md) · [examples/test_specification.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/test_specification.md)

###### Additional context

Reuse the map. A declared test path can establish a reference; only an executed observation establishes the result.

### F19 · Decide whether a requirement is ready

As a implementer, I want a usable requirements-quality checklist, so that I can find ambiguous requirements before starting.

#### Acceptance criteria

- **F19.1** Implementer sees whether scope, permission and observable proof are determinate. A checked box alone cannot establish implementation or test success. Retain the output, the governing source and the consumer’s located evidence on the candidate.

#### Scope and sources

Parent: this plan. Owner role: implementer. Child: S19. R10/A10g. [Audit finding F19](./audit.md#f19--high--requirements-review-lacks-a-deliverable-checklist-with-located-verdicts)

#### S19 · Use the requirements-quality checklist at its handoff

As a implementer, I want the relevant facts with their source, so that I can find ambiguous requirements before starting.

##### Acceptance criteria

- **S19.1** After a candidate specification exists, identify the revision, criterion under review, quality question, located evidence, verdict and unresolved correction. Implementer sees whether scope, permission and observable proof are determinate. A checked box alone cannot establish implementation or test success. Retain the output, the governing source and the consumer’s located evidence on the candidate.

##### Scope and sources

Parent: F19. Owner role: implementer. W04. Use the evidence and boundaries in the linked finding.

##### W04 · Author a requirements-quality checklist for the implementer

###### Description

A completed checklist can be mistaken for successful implementation.

###### Expected outcome

Technical Writer produces a complete reviewer-owned checklist tied to the candidate specification.

###### Scope

Author the standalone form and its checked delivery path. Existing review guidance owns the judgments; avoid a second acceptance registry.

###### Specification

Parent: S19. Supports S19.1 and F19.1. R3/R10/A3/A10g. Responsible role: review-guidance maintainer. Requires a candidate specification and W03 references.

###### Acceptance criteria

- **W04.1** Request a requirements-quality checklist on a requirement with ambiguous retry authority. Its row gives the revision, quality question, located evidence, verdict and required correction.
- **W04.2** After clarification, update only that judgment. The implementer can see the resolved rule; no checkmark claims code was built or tested. Retain both verdicts and the checked artifact.

###### Relevant files

[workflows/validation_review.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/validation_review.md) · [references/spec_driven_development.md](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/contracts/documents.json)

###### Additional context

One reviewed requirement before and after clarification proves this increment. Reuse the same checklist for release evidence.

### F20 · Explain the document sequence in the `README.md` file

As a contributor, I want the document sequence at the project entry, so that I can start with the right inputs.

#### Acceptance criteria

- **F20.1** Starting at the `README.md` file, route one product change and one standalone fix, identify the required parents and find the applicable guides. An unqualified mandatory chain or a dead route fails.

#### Scope and sources

Parent: this plan. Owner role: contributor. Child: S20. R16/A16. [Audit finding F20](./audit.md#f20--medium--the-readmemd-file-leaves-document-order-to-the-skill-internals)

#### S20 · Choose the next document from the quick start

As a first-time user, I want a numbered path with conditional branches, so that I know which input I need.

##### Acceptance criteria

- **S20.1** Use the `README.md` file alone for the routing decision. Follow the links to check destinations. A new reader can identify where proof is defined and where it is recorded.

##### Scope and sources

Parent: F20. Owner role: first-time user. W29. Use the evidence and boundaries in the linked finding.

##### W29 · Publish the numbered document sequence in the `README.md` file

###### Description

New users see isolated prompts before learning what establishes the next document’s inputs.

###### Expected outcome

A contributor can choose what to write next from the `README.md` file alone and follow the link to the owning format.

###### Scope

Add one numbered section linked from Quick start. Keep optional branches, checked-output rules and format definitions in their owning references. Include human-readable text for both hosts.

###### Specification

Parent: S20. Supports S20.1 and F20.1. R16/A16. Responsible role: documentation maintainer. Requires the adopted routes for the seven artifacts, W20’s parent rules, W30–W31’s selection rules and the accepted production order.

###### Acceptance criteria

- **W29.1** Starting at Quick start, a new reader can locate discovery or existing evidence → brief when useful → product definition → feature behavior → applicable design or decisions → delivery plan → feature or epic → story → child Issue → evidence and closure. The section says what feeds each step and links to the actual skill guidance.
- **W29.2** Using the same section, route an independent broken-link fix directly, with inline scope and proof. Identify why an orphaned child must wait. Locate all seven conditional artifacts at their dependency points and distinguish planned proof from observed results. Retain the `README.md` file passage, resolved links and both reader answers.

###### Relevant files

[Repository entry](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/README.md#L56) · [Relationship guidance](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md#L116) · [Required production order](./specification.md#production-order)

###### Additional context

One commit ships the section, quick-start link and necessary cross-references. Reuse W20 evidence for runtime routing. Record verdict and evidence against the exact candidate under the shared Definition of Done.

### F21 · Choose how much planning an improvement needs

As a delivery owner, I want the writer to identify the smallest record that preserves scope, authority and proof, so that a small improvement can ship directly and coordinated work has an accountable parent.

#### Acceptance criteria

- **F21.1** Given A17’s contrasting requests, a reader can choose an independent Issue, an independent or governed story, a grouping record or a delivery plan and identify the input that justified that choice. Preserve project-required parents and unresolved blockers.

#### Scope and sources

Parent: this plan. Owner role: writing-guidance maintainer. Child: S21. R17/A17. [Audit finding F21](./audit.md#f21--medium--the-guides-explain-what-a-record-contains-better-than-when-to-add-a-parent)

#### S21 · Route an improvement from its actual scope

As a writer, I want to decide which record owns the outcome and which dependencies need coordination, so that readers can implement the work without guessing or inventing a parent.

##### Acceptance criteria

- **S21.1** Route the paired A17 requests through the ordinary writing entry. From the chosen record and its referenced input, recover why the work can stand alone or why it needs its particular parent or plan. Reuse W20 evidence for stale and missing declared parents.

##### Scope and sources

Parent: F21. Owner role: workflow maintainer. W30 and W31. W29 links the rules from the public chronology. Apply explicit user or project tracking requirements first.

##### W30 · Choose a task or story for an improvement

###### Description

An improvement label alone cannot tell the writer whether a story owns the requested work.

###### Expected outcome

The writer can commission an independent improvement, an independent story or a contribution to an existing story without inventing a parent.

###### Scope

Place the routing rules at the existing discovery entry. Link the existing Issue and story references. Preserve the declared-child checks and use the existing tracker format.

###### Specification

Parent: S21. Supports S21.1 and F21.1. R11/R17 and A11/A17. Responsible role: workflow maintainer. Requires W20’s settled child-parent contract.

###### Acceptance criteria

- **W30.1** Given an authorized change to a single misleading label with its exact replacement, scope and proof, use one Issue. Given an independent request that an administrator can recover an unsaved selection, capture the actor, benefit, boundary and observable result in a story or an existing equivalent record. Neither case invents a parent.
- **W30.2** When the same label correction is explicitly assigned to a story criterion, resolve that parent and criterion. A missing parent blocks readiness for the child. Retain the two outputs and the observation that distinguishes them. Reuse A11 for an already demonstrated missing-parent verdict.

###### Relevant files

[Discovery](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [Issue guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [Story guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/user_story.md)

###### Additional context

Ship the ordinary writing route, guidance and example in one commit. Record the scoped verdict and candidate under the shared Definition of Done.

##### W31 · Choose a feature, epic or delivery plan

###### Description

A useful grouping and a delivery sequence answer different questions. The writer needs to distinguish them.

###### Expected outcome

A reader knows which capability owns the slices, whether broader coordination needs an epic, and whether delivery needs a separate plan.

###### Scope

Extend W30’s decision table. Reuse a feature for independently acceptable slices of one capability. Use an epic where several slices or capabilities share an initiative, owner and integrated outcome. A project may use either label for the same level. Add a plan only when delivery decisions need an explicit sequence, handoff, compatibility or recovery agreement, or when required by the project.

###### Specification

Parent: S21. Supports S21.1 and F21.1. R2/R17 and A17. Responsible role: planning-guidance maintainer. Requires W30. W29 consumes this route.

###### Acceptance criteria

- **W31.1** Given one independently shippable story, preserve its direct source. Given several usable slices of one capability, group them under the named feature. Add an epic only when the request supplies a broader governed outcome or the project requires one. Retain the chosen records and source for each distinction.
- **W31.2** With the feature and business scope held fixed, compare a single contained delivery with a rollout where old and new readers must coexist. The first can keep steps inline. The second identifies ordering, compatibility proof, owner of the switch and recovery in a delivery plan. A mandated project plan takes precedence. Save the paired result and the governing condition.

###### Relevant files

[Planning guide](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/implementation_plan.md) · [Discovery](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [Skill entry](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md)

###### Additional context

Ship the completed decision table, normal route and contrasting examples together. Reuse these choices in the README review. Stop when the reader can distinguish the cases on the identified candidate.

### F22 · Resolve material gaps without needless questions

As a document owner, I want the writer to ask only when my answer changes the work, so that the specification preserves my intent and I can trust its stated decisions.

#### Acceptance criteria

- **F22.1** From the supported writing entry, the two A18 requests preserve or clarify export ownership as their evidence permits. An invented decision or an unnecessary permission question fails. A draft can still expose an unresolved rule.

#### Scope and sources

Parent: this plan. Owner role: writing-workflow maintainer. Child: S22. R18/A18. [Audit finding F22](./audit.md#f22--high--a-valid-source-reference-can-conceal-an-invented-answer)

#### S22 · Write from incomplete project context

As a developer, I want the writer to use the project’s evidence and identify what only I can settle, so that I can act on the document without rechecking every assumption.

##### Acceptance criteria

- **S22.1** Inspect the two A18 documents, actual questions, sources, readiness outcomes and review verdicts on the same candidate. A decision is attributable to the source or the actual owner response. An unresolved topic stays provisional. The source-settled case incurs no interview.

##### Scope and sources

Parent: F22. Owner role: discovery maintainer. W32 establishes coverage on one route, W33 connects the question and response, and W34 applies the contract across the catalog. Reuse F6’s discovery guidance, W17’s host handoff and the private JSON execution records.

##### W32 · Detect an omitted material permission

###### Description

A writer can omit the question from the discovery record and still pass the current check.

###### Expected outcome

A complete product document can expose its unresolved permission in a draft and cannot be marked ready until the material topic is settled.

###### Scope

Extend the existing document contract and readiness check on the product route. Derive applicable topics from the format and task scope, independently of the writer’s list. Accept a supported answer, a provisional proposal, an open item or a justified inapplicable topic according to its effect on readiness. Preserve old records at their original version.

###### Specification

Parent: S22. Supports S22.1 and F22.1. R18/A18. Responsible role: Contract maintainer. Inputs are the existing PRD contract, declared permission controls and F22’s undecided brief.

###### Acceptance criteria

- **W32.1** On the undecided export brief, omit the material permission topic. Preparation or checked readiness gives the located missing topic and its affected section. A draft naming that open decision can pass as a draft.
- **W32.2** Mark the decision resolved against the undecided brief. A real but irrelevant source ID cannot pass the required semantic review. Retain the passage and verdict alongside the mechanical result. Reuse the existing open-blocker control.

###### Relevant files

[contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/contracts/documents.json) · [scripts/planning_readiness.py](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/scripts/planning_readiness.py) · [scripts/validate_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/scripts/validate_document.py)

###### Additional context

One commit ships the product route, compatible contract, guidance and smallest affected regression. Use the shared Definition of Done and record the exact candidate, evidence and verdict.

##### W33 · Ask only the question that changes the requirement

###### Description

A writer can ask an owner to confirm existing policy or treat a plausible recommendation as authority.

###### Expected outcome

The supported workflow uses existing evidence where decisive, obtains a missing owner answer where necessary and resumes the dependent section.

###### Scope

Connect W32’s decision to the existing discovery and host question routes. Before asking, record the affected criterion, source inspected and unresolved consequence. Bind a returned answer or explicit delegation to the question through a trustworthy host reference where available. Leave unverifiable authority unresolved.

###### Specification

Parent: S22. Supports S22.1 and F22.1. R18/A18. Responsible role: Discovery maintainer. Requires W32. Use A18’s same export route for both requests. The public exchange supplies behavioral proof.

###### Acceptance criteria

- **W33.1** For the format-only change, observe zero permission questions and the preserved permission. For self-service with ownership unresolved, observe one targeted ownership question. An unanswered request keeps the dependent section provisional while independent sections proceed.
- **W33.2** Supply the owner’s answer and confirm only the supported scope becomes ready. A single missing owner-held fact can be asked directly. A delegated routine choice proceeds without making the user confirm it. Use existing evidence for unchanged branches.

###### Relevant files

[workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/workflows/discover.md) · [scripts/planning_readiness.py](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/scripts/planning_readiness.py) · [scripts/validate_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/scripts/validate_document.py)

###### Additional context

Ship one connected question-and-resumption route. Share its packet with W28 and the applicable host acceptance check. Use the shared Definition of Done and record the exact candidate, evidence and verdict.

##### W34 · Apply discovery checks at the right document scope

###### Description

A control for complete product documents alone leaves other formats exposed and can add friction to minor edits.

###### Expected outcome

The other applicable authoring routes use the same readiness distinction at a scale appropriate to the requested work.

###### Scope

Map applicability through the existing catalog for complete or substantial authoring, including low-level design, stories and issues. Keep a title edit or a section with no material decision lightweight. Use shared rules when they are sufficient.

###### Specification

Parent: S22. Supports S22.1 and F22.1. R18/A18. Responsible role: Document-contract maintainer. Requires W32 and W33. Use the actual kind and operation mappings and historical receipt protections.

###### Acceptance criteria

- **W34.1** From actual routing, account for every supported document kind and scope. On the distinct story or Issue path exercise one material missing fact through to draft or owner answer. For a source-settled design reuse compatible route evidence.
- **W34.2** A title-only edit with the same topic incurs no discovery questionnaire. Old receipts verify under their own version. Reuse A7/W17 for host differences, or add only the missing A18 observation to that handoff.

###### Relevant files

[contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/contracts/documents.json) · [references/issue.md](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/references/issue.md) · [references/user_story.md](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/references/user_story.md) · [references/low_level_design.md](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/references/low_level_design.md) · [scripts/test_guided_discovery.py](https://github.com/fatonsopa/ai-technical-writer/blob/1720c51efeb4f8557f7774222cf3c66ba7f66a61/scripts/test_guided_discovery.py)

###### Additional context

Ship the remaining route coverage and its representative checks. Do not multiply all document kinds by all host and question variants. Use the shared Definition of Done and record the exact candidate, evidence and verdict.

## Requirement coverage

| Requirement and proof | Owning work | Evidence used at closure |
| --- | --- | --- |
| R1 / A1 | F1 → S01 → W01, W02 | Mixed passage and the literal’s real consumer. |
| R2 / A2 | F5 → S05 → W09, F15 → S15 → W10, F2 → S02 → W11, W20 | Shape a brief, decompose an initiative and retain the standalone issue path. |
| R3 / A3 | F2 → S02 → W03, F19 → S19 → W04, F3 → S03 → W21 | Correct and displaced references, justified safeguard, meaningful counterexample and consuming work. |
| R4 / A4 | F4 → S04 → W07, W08 | Independent reader’s decision and a source-grounded verdict. |
| R5 / A5 | F6 → S06 → W28, consuming F14/W12 or F16/W13 when needed | Ambiguous and complete inputs, source-backed answers and an unresolved cause. |
| R6 / A6 | F7 → S07 → W14, W15 | Public messages, checked result and historical receipt. |
| R7 / A7 | F8 → S08 → W16, W17 | Same natural edit and connected handoff on the two actual hosts. |
| R8 / A8 | F3 → S03 → W21 | Changed and unaffected sources, previous failure, candidate and resulting verdicts. |
| R9 / A9 | F9 → S09 → W18, W19 | Blank-start product and behavior documents on the same authoring contract. |
| R10 / A10a–g | See the seven rows below | All seven complete authored outputs with their own minimum content and consumer evidence. |
| R12 / A12 | F10 → S10 → W22, W23; F7 → S07 for A6 | Original and edited wording, source, cold reader’s answer and one fluent but wrong alternative. |
| R13 / A13 | F11 → S11 → W24 | Child Issue, parent links and one scoped failure criterion. |
| R14 / A14 | F12 → S12 → W25, W26 | Necessary manual action and clarified role recovered from the replies. |
| R15 / A15 | F13 → S13 → W27 | Routine update trace and relevant naming control. |
| R17 / A17 | F21 → S21 → W30, W31 | Paired routing choices, rationale and preserved project constraints. |
| R18 / A18 | F22 → S22 → W32, W33, W34 | Same export route, two requests, actual question counts, answer binding, review and readiness verdicts. |
| R16 / A16 | F20 → S20 → W29 | Two reader routes from the `README.md` file and resolved guide links. |
| R11 / A11 | F2 → S02 → W20 and W11 | Real parent links, broken edges and justified standalone work. |

| Requested deliverable | Acceptance | Task and next consumer |
| --- | --- | --- |
| Discovery interview record | A10a | F14 → W12 · Brief or product author can distinguish an owner answer from a suggestion. A silent owner leaves the restatement open. |
| Brief | A10b | F5 → W09 · Product owner can decide whether to develop the opportunity. A missing baseline stays unknown; no budget is invented. |
| Capability map | A10c | F15 → W10 · The spec author selects the intended capability. Independent capabilities can be parallel. A cycle is surfaced for resolution. |
| Research record | A10d | F16 → W13 · Designer can cite the finding and identify who must decide. A study or working prototype cannot silently approve a choice. |
| Feature map | A10e | F17 → W05 · Journey author or verifier can locate the surface. A guessed route/handle or app launch alone cannot establish that it was reached. |
| Critical journeys | A10f | F18 → W06 · Verifier resolves each referenced surface and finds the named check. An unknown screen or unrun test cannot count as verified. |
| Requirements-quality checklist | A10g | F19 → W04 · Implementer sees whether scope, permission and observable proof are determinate. A checked box alone cannot establish implementation or test success. |

**Independent handoff.** Give the implementer the packet, sources and normal skill entry. Keep the reviewer’s expected observations separate. The reader should recover WEB-09, its excluded automatic retry, its reconciliation requirement and evidence for the stored state. Record what the reader could recover and where a consequential guess remained. [Governing example](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/spec_driven_development.md#L118) · [T16](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/test_specification.md#L55)

**Shared Definition of Done.** After approval, use Skill Builder’s existing modify workflow with frozen source, authorized paths and necessary checks. Bind the Technical Writer dependency separately from the candidate. Follow the runner’s packets; import current document receipts with `validate-documents`. Use `scripts/run_tests.py --execute` for impacted changes. Reuse a structural check only within its demonstrated scope. A claim about the writer producing a usable artifact requires the actual output from its supported entry, its reviewed bytes and the stated consumer observation. A change to an existing route includes relevant compatibility coverage. [Builder workflow](https://github.com/fatonsopa/ai-skill-builder/blob/222b356fd5ac7a2df9fd9621e3744db883ecede0/SKILL.md) · [Repository rules](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/AGENTS.md)

**Close each task at the first sufficient evidence.** The implementer supplies the bounded result; the reviewer inspects the candidate against the same criterion. Record Met, Failed or Not demonstrated, evidence, candidate, reviewer and integration result in the issue. For seven-output coverage, reuse the same source packet across compatible cases and run only missing distinctions. Close a story and its epic on their stated usable outcome. If a source changes, preserve the old verdict and reopen only dependent claims. The final integrated reader must be able to recover scope, exclusions and proof without this conversation. For a claimed improvement compare baseline and candidate on equivalent inputs.

## Rollout and recovery

Keep previous contracts, reviewed documents and delivery receipts readable under their original versions. Halt the affected increment on changed authority, broken historical verification, a validator guessing a parent, or a host unable to produce required evidence. Resume at the first unresolved boundary. Use the repository’s full-suite gate once implementation completion is bound to the full candidate. Apply the accepted local package through Skill Builder within the authorized scope. Use its existing recovery mechanism if local application fails. Record independent consumer acceptance only when directly observed.

## Risks and open decisions

The owner approved specification and implementation plan revision 7, including the conditional hierarchy, first-use naming convention, reviewed-delivery sentence and evidence-based clarification under R18/A18. Internal file names and implementation choices are delegated within the approved scope. A missing host observation remains Not demonstrated.

## Pending owner decisions

Append out-of-scope discoveries here with their source, observed effect, proposed change, impact of deferral and any task actually blocked. Only an explicit owner decision can add them to implementation scope.
