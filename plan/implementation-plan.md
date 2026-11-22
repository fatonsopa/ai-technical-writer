# Spec Writer implementation plan

Status: Scope approved for implementation on the handoff computer. Revision 19. The [behavioral specification, revision 19](./specification.md) owns the requirements. The [audit](./audit.md) owns the 36 approved findings. This plan assigns each finding one epic, identifies its child story and commissions individually shippable tasks against that story.

## Goal and specification

Deliver one local Spec Writer candidate that can author complete specification-driven documents for any project and pass meaningful requirements from one document to the next. Mirai is one source of examples and facts. Technical Writer owns document structure and authoring. A project owner approves product decisions and any application change. Confirm or reconcile the audited skill baseline `4a8e7c92e20404f05e68708c1a3ea26c6961b178` before freezing implementation scope.

## Current context and approach

Use the actual [User Story (US) template](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/user_story.md) for the parent outcome and child story, and the [Issue template](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) for each task. Titles below preserve independent task IDs. Each story’s scope identifies its epic; each task’s Specification names its story criterion. One child story is sufficient for each finding’s first usable outcome.

**Artifact production order.** Use the [numbered dependency rules](./specification.md#production-order) and [seven artifact acceptance cases](./specification.md#seven-authoring-cases-and-hierarchy-acceptance). With unresolved intent, interview → brief → product definition. Separate independently deliverable capabilities before writing their individual specifications. Research precedes any dependent design choice. Requirements review needs an identified specification; critical journey verification needs a mapped surface. From an established feature or epic, write the story first and its child tasks second. A standalone issue states its own authority and proof. Verification criteria are written before implementation; evidence is attached after execution. For design, contracts and verification, use the [linking table and refund example](./specification.md#link-work-to-its-parent-and-designs-to-their-sources) to identify which record a reader needs. W62 implements these rules in the ordinary writing route. Use the [command and document sequence](./specification.md#when-to-write-and-read-tasksmd) for the transition from the plan to Issues, the feature task list and authorized implementation.

**One task, one releasable change.** Include the working entry point, necessary consumers, guidance, example and affected checks in the same commit. A task that introduces an artifact must ship a route from an ordinary request to complete reviewed output. Use a section or existing document contract when it can faithfully deliver the requested form. If it cannot, extend the existing routing and validation mechanism with the smallest compatible named variant. Preserve old receipts by version. Never certify a fragment as a complete standalone document.

**Feature documentation at delivery.** Follow R35. Ship each new or changed public capability or document type with its guidance and a direct index link in the same increment. W54 establishes the first usable route. Close F39 when the index covers the release’s public features and supported document types.

**Short feedback loop.** Before changing the skill, try the task’s named counterexample at its actual boundary or reuse the audit observation when its inputs still match. Fix the first demonstrated mismatch, inspect the same outcome and stop when its criteria and relevant shared obligations pass. A new input, failed boundary or missing criterion is the reason for another check. An unrelated failure gets its own disposition. Keep the original failure. On acceptance, record the exact commit, evidence and reviewer in the issue and hand the usable increment to its consumer.

The owner approved the work order, scope and local integration authority. Start with the execution prompt in the repository’s [execution guide](./README.md). Use this plan for dependencies, task boundaries, required evidence and closure. Keep the private JSON execution log described in the starting prompt. Reuse native run records and document the reason for each extra verification before it runs.

See the governing specification’s template mapping for shortcuts, task breakdown and reviews. Implement W35 before W36–W37. W40 and W41 reuse the relevant approved writing and review routes. W40 authors the refund task list. W48 consumes that exact output under the [feature task-list rules and refund example](./specification.md#feature-task-lists-and-issue-acceptance). W38 precedes W39. Coordinate their host demonstrations with W17.

## Reuse the upstream implementation

For each approved capability borrowed from the upstream project, inspect the actual first-party source at the selected release or commit. Begin with the audited revision `a4d571229e164e440f8950cac034607bae7b7518`. Use the shipped command, extension or workflow directly when it meets the criterion. When adaptation is needed, start from that upstream source or its supported scaffold and make the smallest Spec Writer change. Keep custom code to the part the existing writer and upstream implementation cannot supply. In the task’s existing record identify the source revision and path, the integration point and the reason for the difference. This applies on Codex and Claude.

| Approved work | Implementation to start from | Spec Writer’s responsibility |
| --- | --- | --- |
| W47 · Add a project-aware writing command | [extension manifest scaffold](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/extensions/template/extension.yml) and [example command](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/extensions/template/commands/example.md) | Adapt the scaffold to invoke the existing checked writer. Use the installed host integration and feature context. |
| W40/W48 · Author and consume the feature task list | [task-list template](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/tasks-template.md), [task generation](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/commands/tasks.md) and [task consumer](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/commands/implement.md) | Adapt the upstream list and generation rules. Give the real implementation command the feature’s ordered rows and access to each authoritative Issue. Observe the eligible tasks, the blocked task and its release condition. |
| W49–W50 · Execute and resume | [bundled workflow](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/workflows/speckit/workflow.yml) | Call the upstream workflow and its status/resume facilities. Bind provider results to the originating Issue and candidate. [Upstream Converge](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/commands/converge.md) is available on request. |
| W51–W52 · Assessment and defect repair | [assessment extension](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/extensions/assess/extension.yml) and [bug extension](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/extensions/bug/extension.yml) | Start with the first-party extension commands and manifests. Apply the approved writing formats, criteria and permissions to their inputs and outputs. |
| W53 · Version and distribute | [first-party bundle manifest](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/bundles/assess/bundle.yml) | If a bundle is needed, adapt the manifest to the components and versions that actually resolve. Use upstream install/update/remove where available. |

For source or templates copied into the deliverable, keep the upstream copyright and permission notice with the distributed material and preserve any applicable file-specific notices. Record the copied path, immutable revision and local changes in the existing change record. Exercise the adapted boundary with the task’s already-required check. A direct dependency or a document link does not require a second copy of the upstream implementation. [Upstream MIT license](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/LICENSE)

For each borrowed operation, determine which writing features it calls and which documents those features accept or produce. Use the full catalog rules in R33/A33. W58 extends W47’s borrowed command, and W59 extends the document handoff at W48. Ship W58 and W59 before accepting W53’s release. Working standalone document requests remain eligible throughout.

## Work sequence

Open the [task list](./tasks.md) to select work. Follow its row to the existing Issue below and use that Issue’s scope, criterion IDs and proof. The [handoff test specification](./test.md) exercises this same route on the actual packet. Reuse the earlier W60 result. W55–W57 and W51.3 have no executable row.

For an authorized feature build, use the bundled workflow when the project selects it. It runs Specify, Plan, Tasks and Implement, with separate reviews after the specification and the plan. Close routine delivery when the existing task and story acceptance criteria and applicable Definition of Done are demonstrated on the identified candidate. Invoke upstream Converge manually only when the user requests a broader review of that feature. Its findings may identify work to propose; they grant no additional implementation authority. A request to write a document ends at its checked handoff unless implementation is separately authorized.

Deliver the rename after Skill Builder B5/T50. W47 selects a feature, W48 lets the implementing agent select eligible work from the feature list and recover acceptance from each Issue, and W49–W50 prove execution and recovery on one authorized local feature. Establish that connection before adding W51–W52 and the versioned W53 distribution. Reuse host evidence where inputs match. Use the project-selected provider for execution. Keep remote publication outside implementation authority.

Use the accepted Skill Builder candidate from its implementation plan. Begin with W01 and W03 to get a literal and a source reference through a real consumer. W20 makes the parent chain usable. The seven document routes can then draw on one initiative’s source packet: where intent is unknown, use W12 before W09; W10 precedes dependent feature specifications; W13 precedes design that depends on its research; W05 precedes W06; W04 reviews a drafted specification. Other stories may proceed once their named inputs and shared interfaces are settled. The order below groups by finding for lookup. W24 uses the W20 parent contract. W25 precedes W26. W30 and W31 settle the selection rules before W29 publishes the sequence after its linked routes exist. W32 precedes W33, then W34 applies the route across the catalog. W43 uses W32–W34, W44 follows W40/W41, and W45 uses the existing Interface Contract (IC) route. W17 is the final integrated host check and reuses these assignment inputs where applicable. Plan-level A10 requires all seven outputs and their consumer observations. Each has one owning epic and task. W60 has accepted guide evidence. The remaining implementation verdicts start as **Not demonstrated**.

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
- **F20.2** From the public introduction, explain how a request becomes an observable acceptance check and choose the appropriate entry for one small change. Use the W42 reader answers and resolved examples.

#### Scope and sources

Parent: this plan. Owner role: contributor. Child: S20. R16/A16. [Audit finding F20](./audit.md#f20--medium--the-readmemd-file-leaves-document-order-to-the-skill-internals)

#### S20 · Choose the next document from the quick start

As a first-time user, I want a numbered path with conditional branches, so that I know which input I need.

##### Acceptance criteria

- **S20.1** Use the `README.md` file alone for the routing decision. Follow the links to check destinations. A new reader can identify where proof is defined and where it is recorded.
- **S20.2** A reader starting above setup can recover one behavior, the source that defines it, a bounded task and its failure check. The public overview distinguishes a planned check from evidence that it passed.

##### Scope and sources

Parent: F20. Owner role: first-time user. W29 supports S20.1; W42 supports S20.2. Use the evidence and boundaries in the linked finding.

##### W29 · Publish the numbered document sequence in the `README.md` file

###### Description

New users see isolated prompts before learning what establishes the next document’s inputs.

###### Expected outcome

A contributor can choose what to write next from the `README.md` file alone and follow the link to the owning format.

###### Scope

Build on the Quick start section “Where `tasks.md` fits” when the implementation ships. Publish the full numbered chronology and replace its planned-status wording with verified host entries. Link to the owning format guides. The command instructions must identify their actual input, output and next reader for both hosts.

###### Specification

Parent: S20. Supports S20.1 and F20.1. R16/A16. Responsible role: documentation maintainer. Requires the adopted routes for the seven artifacts, W20’s parent rules, W30–W31’s selection rules and the accepted production order.

###### Acceptance criteria

- **W29.1** Starting at Quick start, a new reader can locate discovery or existing evidence → brief when useful → product definition → feature behavior → applicable design or decisions → delivery plan → feature or epic → story → child Issue → evidence and closure. The section says what feeds each step and links to the actual skill guidance. Follow the multi-task branch through its reviewed spec and plan, Issues, `tasks.md`, eligible Issue, implementation evidence and next eligible row. Starting from the README, the reader can explain why the list is the last writing output and why no `task.md` follows it by default.
- **W29.2** Using the same section, route an independent broken-link fix directly, with inline scope and proof. Identify why an orphaned child must wait. Locate all seven conditional artifacts at their dependency points and distinguish planned proof from observed results. Retain the `README.md` file passage, resolved links and both reader answers.

###### Relevant files

[Repository entry](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/README.md#L56) · [Relationship guidance](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/SKILL.md#L116) · [Required production order](./specification.md#production-order)

###### Additional context

One commit ships the section, quick-start link and necessary cross-references. Reuse W20 evidence for runtime routing. Record verdict and evidence against the exact candidate under the shared Definition of Done.

##### W42 · Explain spec-driven writing at the public entry

###### Description

The public README opens with a catalog and then lists installation requirements. A developer has to infer what a specification changes about the work.

###### Expected outcome

A first-time reader can start with one change request, choose a document and follow one behavior into a task and its planned proof.

###### Scope

Edit the repository-root README introduction. Put a plain-language explanation and a compact need-to-output table before setup. Use the current catalog and one existing feature example. W29 owns the detailed chronology.

###### Specification

Parent: S20. Supports S20.2 and F20.2. R16/A16. Responsible role: documentation maintainer. Uses existing references and examples; can ship before W29. Show only entry points available on the candidate.

###### Acceptance criteria

- **W42.1** Starting at the README title, before installation, a reader can identify the audience, what a spec settles before coding, what to supply and what the writer returns. The reader can choose among an unshaped idea, agreed feature behavior and one bounded fix from the need-to-output table. A small authorized fix must route straight to an Issue.
- **W42.2** Follow one worked request through a named requirement, story criterion, a clearly labeled illustrative child Issue and its planned observable check. Preserve the source behavior on failure, keep the record types distinct and avoid claiming the check ran. Record the passage, link targets and reader answers on the candidate. One document read covers both criteria.

###### Relevant files

Repository root README and its Quick start; [WEB-06](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/spec_driven_development.md#L102-L104) · [the story criterion](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/user_story.md#L20) · [T10](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/test_specification.md#L49) · [upstream reader guide](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/README.md#choose-your-process) · [upstream development method](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/README.md#spec-driven-development).

###### Additional context

Suggested opening in the project’s own voice: “Technical Writer helps developers and AI agents agree on what a change must do before anyone builds it. Give it a request and the project sources. It turns the agreed behavior into specifications, stories and tasks that say how to check the result.” Example: “If saving a category fails, keep my selection.” WEB-06 requires retaining it. The story expects an error and the selection still in edit mode. An illustrative child Issue would implement that failure path. T10 defines its check, including the absence of a success message. Link the real examples and label the illustrative Issue. Ship the README edit in one commit. Use the shared Definition of Done.

### F21 · Choose how much planning an improvement needs

As a delivery owner, I want the writer to identify the smallest record that preserves scope, authority and proof, so that a small improvement can ship directly and coordinated work has an accountable parent.

#### Acceptance criteria

- **F21.1** Given A17’s contrasting requests, a reader can choose an independent Issue, an independent or governed story, a grouping record or a delivery plan and identify the input that justified that choice. Preserve project-required parents and unresolved blockers.
- **F21.2** From A17b’s governed and independent design outputs, a developer can recover the source of the permission rule and the component boundary. A declared child with a missing governing criterion remains blocked. Reuse S21.2 evidence.

#### Scope and sources

Parent: this plan. Owner role: writing-guidance maintainer. Child: S21. R17/A17 and A17b. [Audit finding F21](./audit.md#f21--medium--the-guides-explain-what-a-record-contains-better-than-when-to-add-a-parent)

#### S21 · Route an improvement from its actual scope

As a writer, I want to decide which record owns the outcome and which dependencies need coordination, so that readers can implement the work without guessing or inventing a parent.

##### Acceptance criteria

- **S21.1** Route the paired A17 requests through the ordinary writing entry. From the chosen record and its referenced input, recover why the work can stand alone or why it needs its particular parent or plan. Reuse W20 evidence for stale and missing declared parents.
- **S21.2** At the ordinary writing entry, carry the manager-only refund rule into a component design and its planned denial check. When a contract supplies the approved rule and boundary, the independent design can proceed without a separate High Level Document (HLD). Use W62’s paired outputs and reuse W20 for the unresolved child.

##### Scope and sources

Parent: F21. Owner role: workflow maintainer. W30 and W31 support S21.1. W62 supports S21.2. W29 links the rules from the public chronology. Apply explicit user or project tracking requirements first.

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

##### W62 · Link a design to the records that govern it

###### Description

The ordinary writing route can distinguish a child task from an independent Issue. Its design guidance also needs to show which record supplies a component boundary, governing rule or acceptance criterion when no work-item parent applies.

###### Expected outcome

A developer can open a refund design and recover both the authorization owner and the manager-only rule. A directly authorized design can draw those facts from an existing contract.

###### Scope

Apply the specification’s [linking table and refund example](./specification.md#link-work-to-its-parent-and-designs-to-their-sources) at the ordinary writing entry. Keep the shared rule at one maintained location and link it from the affected architecture, Low Level Design (LLD), contract, planning and testing guides where a reader needs it. Use the project’s existing parent fields, IDs, section links and backlinks. Preserve any explicit governance and applicable evidence bindings.

###### Specification

Parent: S21. Supports S21.2 and F21.2 under R17/A17b. Responsible role: writing-guidance maintainer. Reuse W30’s record-selection rules. W20 already owns the missing-parent case. W59 can reuse matching evidence when it exercises its optional workflow consumer.

###### Acceptance criteria

- **W62.1** Given the approved refund rule, an HLD naming the authorization service and a worked story, child Issue and planned denial test, request the LLD through the ordinary writing entry. From its links, recover the manager-only rule and the owning component. In the worked records, follow the native parent link to the story’s employee-denial criterion and the planned test to the behavior it checks. One resolvable relationship passes without a manually maintained reverse link. A link to an unrelated service, a copied rule with altered permission, or a claim that the unrun test passed fails. Retain the source sections, output and reader’s observations on the candidate.
- **W62.2** For the same LLD request, supply direct authorization and an approved contract that settles the rule and component boundary. Supply no HLD, story or epic and no project rule requiring one. The checked design cites the applicable contract and proceeds without creating or requesting a parent. For a declared child whose governing criterion is unresolved, withhold readiness for that child. Reuse W20’s missing-parent evidence where it covers that boundary. Keep the two dispositions and their reasons.

###### Relevant files

`SKILL.md`, the owning references in `references/` for architecture, component design, contracts, work items, plans and tests, and the existing linked examples. Start with `references/high_level_document.md` and `references/low_level_design.md`.

###### Additional context

Ship the ordinary writing route, maintained guidance and worked example together. Use the two specified scenarios and reuse existing evidence for unchanged behavior. Record Met, Failed or Not demonstrated against the candidate under the shared Definition of Done. Initial status is Not demonstrated.

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

### F23 · Start documents from native shortcuts

As a developer, I want to give the document name and brief in one message, so that I can obtain the same checked document as through the normal route.

#### Acceptance criteria

- **F23.1** Observe real host dispatch with the supplied brief and the intended checked document; verify an occupied name keeps its existing handler and the qualified entry remains usable. For a multi-task feature, use W40’s linked Issues and refund list to recover the first usable story and safe task order.

#### Scope and sources

Parent: this plan. Owner role: writing-workflow maintainer. Child: S23. R19/A19. [Audit finding F23](./audit.md#f23--medium--start-documents-from-native-shortcuts)

#### S23 · Write the intended artifact from a short request

As a developer, I want to give the document name and brief in one message, so that I can obtain the same checked document as through the normal route.

##### Acceptance criteria

- **S23.1** Observe real host dispatch with the supplied brief and the intended checked document; verify an occupied name keeps its existing handler and the qualified entry remains usable. Retain the identified candidate, actual request, output and consumer observation. For the refund breakdown, reuse W40.3 to show the first independent story and its task dependencies.

##### Scope and sources

Parent: F23. Owner role: writing-workflow maintainer. W35–W37 and W40–W41. Use the scope boundaries in A19 and the shared Definition of Done.

##### W35 · Launch three document types in Claude Code

###### Description

A bare slash command needs host-level discovery.

###### Expected outcome

Claude Code can start a PRD, LLD or single Issue directly.

###### Scope

Offer opt-in thin entries for /prd, /lld and /task through the current installer. Reuse one catalog and writing route. Preserve user material, explicit edit intent and existing commands.

###### Specification

Parent: S23. Supports S23.1 and F23.1. R19/A19. Responsible role: integration maintainer. Use the installed skill, existing catalog and current installer.

###### Acceptance criteria

- **W35.1** From a real Claude Code session dispatch a short command and compare its checked artifact, brief and type to the owning contract. Resolve the other two names through the same mapping.
- **W35.2** Supply an occupied name and repeat installation. Existing foreign content remains intact, a working qualified alternative is reported, and removal affects only owned entries.

###### Relevant files

[scripts/install_skill.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/install_skill.py) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/documents.json)

###### Additional context

Ship the entry, affected guidance and necessary compatibility evidence together. Stop at the stated proof. Record the candidate and verdict under the shared Definition of Done.

##### W36 · Launch the same documents in Codex

###### Description

Codex has a different native skill invocation.

###### Expected outcome

Codex CLI users can invoke $prd, $lld or $task directly.

###### Scope

Reuse W35’s alias mapping and writing entry with Codex’s supported skill installation. Document copyable host examples.

###### Specification

Parent: S23. Supports S23.1 and F23.1. R19/A19. Responsible role: integration maintainer. Requires W35’s common mapping.

###### Acceptance criteria

- **W36.1** Capture a real Codex invocation and checked result for one of the three kinds. The brief retains its context and literals; the destination and format agree with the existing writer.
- **W36.2** Resolve the other names, preserve the qualified fallback and verify the Codex-specific install/removal boundary. Reuse shared collision checks if their inputs and path are unchanged.

###### Relevant files

[scripts/install_skill.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/install_skill.py) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/documents.json)

###### Additional context

Ship the entry, affected guidance and necessary compatibility evidence together. Stop at the stated proof. Record the candidate and verdict under the shared Definition of Done.

##### W37 · Expose the authorable document catalog

###### Description

A user needs to find which names are installed.

###### Expected outcome

Every supported authorable kind has a discoverable selector and opt-in shortcut or a documented qualified fallback for an occupied name.

###### Scope

Generate entries and quick-start help from the same catalog. Add ready variants as their complete contracts ship. Preserve full-name requests, aliases, reviews and literal text.

###### Specification

Parent: S23. Supports S23.1 and F23.1. R19/A19. Responsible role: integration maintainer. Use W35–W36 and the registered output contracts.

###### Acceptance criteria

- **W37.1** Compare the catalog with generated entries. Every active authoring route resolves to its owning kind, including spec for behavioral specification, and every displayed host spelling corresponds to the installed entry.
- **W37.2** Use a source-settled request and a review request. Selecting a spec does not create a PRD; reviewing an existing artifact does not create a replacement. Use the template crosswalk for both.

###### Relevant files

[scripts/install_skill.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/install_skill.py) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/documents.json) · [README.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/README.md)

###### Additional context

Ship the entry, affected guidance and necessary compatibility evidence together. Stop at the stated proof. Record the candidate and verdict under the shared Definition of Done.

##### W40 · Write the feature task list and its linked Issues

###### Description

The upstream tasks template is a list, while a commissioned child needs its own acceptance record.

###### Expected outcome

A developer receives one Issue for a bounded change or one feature-level `tasks.md` with linked, independently shippable Issues for a multi-task feature.

###### Scope

Route task and tasks separately. Adapt the pinned task-list template and generation instructions. Group work by story, identify the first usable story and how each story can be demonstrated, and distinguish safe parallel work from prerequisites. Use the owning Issues for acceptance, stable IDs and proof. Apply W20 ancestry and R17’s standalone exception.

###### Specification

Parent: S23. Supports S23.1 and F23.1. R19/A19. Responsible role: integration maintainer. Use W35’s selection mechanism, W11 and W20.

###### Acceptance criteria

- **W40.1** From one approved story, task produces one Issue and tasks produces a justified breakdown with the same parent, criterion links, dependencies and observable proof for each child. A one-line upstream checklist entry alone fails.
- **W40.2** A single independent maintenance change stays one Issue. A missing parent for a declared child blocks readiness. Reuse the existing ancestry negatives and confirm no template-generated setup phase or invented test obligation appears.
- **W40.3** Given the two approved refund stories, settled read contract, verified fixture paths and Issue references in the [feature task-list rules and refund example](./specification.md#feature-task-lists-and-issue-acceptance), use the normal writing entry. Expect one `tasks.md` with four rows linked to #81–#84 and their criteria. In US1, only T001 and T002 carry `[P]` and the same refund can be checked on both surfaces before US2 ships. In US2, T004 explicitly depends on T003 and the story demonstration uses mixed refund decisions. A second editable copy of task acceptance, a blanket setup phase or a parallel marker on T004 fails. Retain the checked list and its linked Issues for W48. At the Tasks entry, consume the reviewed spec and plan, resolve or author the Issues before marking the list ready, and return the linked outputs. Reuse existing Issues on continuation. An unresolved row remains unready. Use the [command and document sequence](./specification.md#when-to-write-and-read-tasksmd) in the installed writing guidance.

###### Relevant files

[scripts/install_skill.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/install_skill.py) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/documents.json) · [references/issue.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/references/issue.md) · [references/implementation_plan.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/references/implementation_plan.md)

###### Additional context

Use the three existing Issues in [W-PACKET](./test.md#cases) to generate a small list from this repository and retain the actual output for W48. The approved refund checks still apply.

Ship the entry, affected guidance and necessary compatibility evidence together. Stop at the stated proof. Record the candidate and verdict under the shared Definition of Done.

##### W41 · Route quality and consistency reviews

###### Description

Requirement quality, cross-document agreement and executed checks answer different questions.

###### Expected outcome

A reviewer can request a requirement checklist or a read-only consistency analysis grounded in the owning documents.

###### Scope

Expose checklist through W04 and analyze through W03/W21. Reuse policy for governance, discovery for clarify and existing plans for planning. A convergence-style report can identify gaps; it cannot commission uncovered scope or run implementation.

###### Specification

Parent: S23. Supports S23.1 and F23.1. R19/A19. Responsible role: integration maintainer. Requires the relevant existing route and W35’s common entry mechanism.

###### Acceptance criteria

- **W41.1** Given one vague criterion and one task that weakens a sourced permission, checklist locates the requirement-quality defect and analyze locates the cross-document disagreement. Reuse the same packet.
- **W41.2** Inspect before and after the read-only analysis: the reviewed source, tasks and candidate are unchanged. Findings do not claim runtime proof. A request for code implementation routes to the authorized implementing workflow.

###### Relevant files

[scripts/install_skill.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/install_skill.py) · [SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [contracts/documents.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/documents.json) · [workflows/validation_review.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/workflows/validation_review.md)

###### Additional context

Ship the entry, affected guidance and necessary compatibility evidence together. Stop at the stated proof. Record the candidate and verdict under the shared Definition of Done.

### F24 · Guide the next document from project evidence

As a project owner, I want a short recommendation grounded in the initiative, so that I can decide what to write next or stop.

#### Acceptance criteria

- **F24.1** For one feature, a blocked decision and a standalone fix, distinguish the eligible document, missing prerequisite and completed scope. Continuing creates one attributable successor and resumption reuses existing work.

#### Scope and sources

Parent: this plan. Owner role: writing-workflow maintainer. Child: S24. R20/A20. [Audit finding F24](./audit.md#f24--medium--guide-the-next-document-from-project-evidence)

#### S24 · Choose and continue one eligible document

As a project owner, I want a short recommendation grounded in the initiative, so that I can decide what to write next or stop.

##### Acceptance criteria

- **S24.1** For one feature, a blocked decision and a standalone fix, distinguish the eligible document, missing prerequisite and completed scope. Continuing creates one attributable successor and resumption reuses existing work. Retain the identified candidate, actual request, output and consumer observation.

##### Scope and sources

Parent: F24. Owner role: writing-workflow maintainer. W38 and W39. Use the scope boundaries in A20 and the shared Definition of Done.

##### W38 · Show the next useful document

###### Description

A static sequence cannot account for current scope and reviewed sources.

###### Expected outcome

Guide and next can explain the right next action without creating a file.

###### Scope

Support starting from a goal or existing artifact. Inspect current initiative and source revisions. For eligible work show document type, specific gap and benefit in one line. If choice matters, identify the decision. Stop at the requested endpoint.

###### Specification

Parent: S24. Supports S24.1 and F24.1. R20/A20. Responsible role: workflow maintainer. Requires W20, W30–W31 and the approved production order.

###### Acceptance criteria

- **W38.1** From a feature with a settled prerequisite, next names one eligible document and the specific benefit in one line; repeated next leaves the initiative unchanged. With two plausible initiatives ask which only if evidence cannot settle it.
- **W38.2** For a blocked child name the missing prerequisite. For a standalone fix with sufficient acceptance say documentation is complete. Recommend no extra document in either case; reuse A17 and A18 evidence. Reuse W40’s refund case to check that next recommends `tasks.md` once its inputs exist and reports document delivery after the checked list. It must neither invent a singular document nor initiate implementation.

###### Relevant files

[SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/workflows/discover.md) · [README.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/README.md)

###### Additional context

Ship the entry, affected guidance and necessary compatibility evidence together. Stop at the stated proof. Record the candidate and verdict under the shared Definition of Done.

##### W39 · Continue a checked document handoff

###### Description

A suggested next step can duplicate prior work or outlive its source revision.

###### Expected outcome

The owner can continue one document at a time and resume from the current project state.

###### Scope

Use W38’s selected initiative, existing records and the normal writing workflow. Bind any suggested successor included in a checked final message to W15’s reviewed delivery. Respect a single-document request.

###### Specification

Parent: S24. Supports S24.1 and F24.1. R20/A20. Responsible role: workflow maintainer. Requires W38 and W15 for checked delivery text.

###### Acceptance criteria

- **W39.1** On continue, write exactly the selected eligible artifact; the source revision, governing criterion and shared terms survive. Resume from the same starting request after delivery and identify the completed result without duplicating it.
- **W39.2** Change a governing revision before continuing. Re-evaluate affected readiness and keep unaffected evidence. A stale handoff or altered checked suggestion fails; when a suggestion cannot be bound to the receipt, keep exact finalization and offer guidance on request.

###### Relevant files

[SKILL.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/SKILL.md) · [workflows/discover.md](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/workflows/discover.md) · [contracts/delivery_message.json](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/contracts/delivery_message.json) · [scripts/validate_document.py](https://github.com/fatonsopa/ai-technical-writer/blob/4794ee27af5603785e8c3613e474452b01350700/scripts/validate_document.py)

###### Additional context

Ship the entry, affected guidance and necessary compatibility evidence together. Stop at the stated proof. Record the candidate and verdict under the shared Definition of Done.

### F25 · Find the governing specification after delivery

As a maintainer returning to a delivered feature, I want to find which agreement governs the next change, so that an old delivery snapshot cannot silently reinstate retired behavior.

#### Acceptance criteria

- **F25.1** At the normal edit entry, supply a frozen launch specification allowing seven days and an approved maintained policy allowing thirty days. Ask to update the feature. The draft cites the maintained rule and labels the seven-day value historical. Both source files remain intact. Remove the maintenance decision while keeping two plausible values. The writer identifies the conflict and asks which governs before committing to a value. It can draft unrelated sections. Capture the two draft excerpts or the focused question, source revisions and before/after identities of the inputs. Reuse existing discovery and rewrite evidence for unchanged behavior.

#### Scope and sources

Parent: this plan. Owner role: documentation maintainer. Child: S25. R21/A21. [Technical Writer baseline](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md#L13-L16) · [comparison source](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/how-to/persisting-specs.md#two-separate-questions)

#### S25 · Guide selection of a specification after delivery

As a maintainer returning to a delivered feature, I want to find which agreement governs the next change, so that an old delivery snapshot cannot silently reinstate retired behavior.

##### Acceptance criteria

- **S25.1** At the normal edit entry, supply a frozen launch specification allowing seven days and an approved maintained policy allowing thirty days. Ask to update the feature. The draft cites the maintained rule and labels the seven-day value historical. Both source files remain intact. Remove the maintenance decision while keeping two plausible values. The writer identifies the conflict and asks which governs before committing to a value. It can draft unrelated sections. Use the same outputs for story and epic closure.

##### Scope and sources

Parent: F25. Responsible role: skill maintainer. W43 supports S25.1. Limit the change to the named writing route and the affected review.

##### W43 · Guide selection of a specification after delivery

###### Description

The behavioral specification guide covers revisions. Decision records cover supersession. Neither tells a writer resuming a delivered feature how to distinguish the maintained behavior source from a frozen delivery snapshot when both are available. R18 classifies evidence, but does not settle this post-delivery choice.

###### Expected outcome

Find which agreement governs the next change.

###### Scope

Use the team’s declared maintenance convention. Link a retained snapshot to its maintained successor or other approved source when known. With no authority for a material difference, preserve both and ask one focused question.

###### Specification

Parent: S25. Supports S25.1 and F25.1. R21/A21. Responsible role: skill maintainer. Use existing source and review contracts. Reuse W32–W34 for ambiguous authority.

###### Acceptance criteria

- **W43.1** At the normal edit entry, supply a frozen launch specification allowing seven days and an approved maintained policy allowing thirty days. Ask to update the feature. The draft cites the maintained rule and labels the seven-day value historical. Both source files remain intact.
- **W43.2** Remove the maintenance decision while keeping two plausible values. The writer identifies the conflict and asks which governs before committing to a value. It can draft unrelated sections. Capture the two draft excerpts or the focused question, source revisions and before/after identities of the inputs. Reuse existing discovery and rewrite evidence for unchanged behavior.

###### Relevant files

[Writing guidance](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md) · [Affected handoff](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/workflows/discover.md) · [Upstream comparison](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/how-to/persisting-specs.md#two-separate-questions)

###### Additional context

One commit ships the guidance with the affected example and any necessary route adjustment. Apply the shared Definition of Done. Initially Not demonstrated. Retain each criterion verdict, evidence and candidate in the task.

### F26 · Carry exact field constraints into the implementing Issue

As an implementer reading an Issue, I want to trace a field constraint to its precise definition, so that two similar names cannot lead me to implement the wrong rule.

#### Acceptance criteria

- **F26.1** From a contract where Order.code is optional and Return.code is required, request the task for Return.code. The Issue points to the exact Return.code definition and preserves the required behavior. An unambiguous existing field pointer is sufficient. Review a variant citing Order.code for the return requirement. The review identifies the Issue, wrong field and missing coverage. An unrelated prose-only Issue requires no field citations. Retain the authored Issue, read-only review excerpt and the unchanged source definitions. Use this same pair at W40/W41 if available.

#### Scope and sources

Parent: this plan. Owner role: documentation maintainer. Child: S26. R22/A22. [Technical Writer baseline](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md#L13-L18) · [comparison source](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/commands/tasks.md#task-organization)

#### S26 · Resolve constrained fields in Issue handoffs

As an implementer reading an Issue, I want to trace a field constraint to its precise definition, so that two similar names cannot lead me to implement the wrong rule.

##### Acceptance criteria

- **S26.1** From a contract where Order.code is optional and Return.code is required, request the task for Return.code. The Issue points to the exact Return.code definition and preserves the required behavior. An unambiguous existing field pointer is sufficient. Review a variant citing Order.code for the return requirement. The review identifies the Issue, wrong field and missing coverage. An unrelated prose-only Issue requires no field citations. Use the same outputs for story and epic closure.

##### Scope and sources

Parent: F26. Responsible role: skill maintainer. W44 supports S26.1. Limit the change to the named writing route and the affected review.

##### W44 · Resolve constrained fields in Issue handoffs

###### Description

The Issue guide names requirement-level coverage. The Interface Contract already distinguishes absence, null and exact field names. The task handoff and its planned consistency review do not explicitly require the owner and field to resolve together when one requirement covers several similarly named fields. A document-level link alone can hide the wrong field.

###### Expected outcome

Trace a field constraint to its precise definition.

###### Scope

When a task implements a constrained field, link its exact owner and field, preserve relevant semantics and flag uncovered or misattributed fields when reviewing the requested scope. Reuse the project’s schema, Interface Contract or Low Level Design as appropriate.

###### Specification

Parent: S26. Supports S26.1 and F26.1. R22/A22. Responsible role: skill maintainer. Use existing source and review contracts. Build on W40 and W41 for generation and read-only analysis.

###### Acceptance criteria

- **W44.1** From a contract where Order.code is optional and Return.code is required, request the task for Return.code. The Issue points to the exact Return.code definition and preserves the required behavior. An unambiguous existing field pointer is sufficient.
- **W44.2** Review a variant citing Order.code for the return requirement. The review identifies the Issue, wrong field and missing coverage. An unrelated prose-only Issue requires no field citations. Retain the authored Issue, read-only review excerpt and the unchanged source definitions. Use this same pair at W40/W41 if available.

###### Relevant files

[Writing guidance](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md) · [Affected handoff](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/interface_contract.md) · [Upstream comparison](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/commands/tasks.md#task-organization)

###### Additional context

One commit ships the guidance with the affected example and any necessary route adjustment. Apply the shared Definition of Done. Initially Not demonstrated. Retain each criterion verdict, evidence and candidate in the task.

### F27 · Resolve the contract shared by separate repositories

As a developer integrating a consumer with a provider, I want to identify the governing contract and supported version, so that a local edit cannot silently change the release agreement.

#### Acceptance criteria

- **F27.1** Given an owner contract at v1, a divergent consumer copy and a proposed v2, ask for an Interface Contract update. It identifies the source revision, pins the consumer to v1, names the discrepancy and directs the proposed change to the owner. The consumer copy is untouched. Provide only the v1 pin and mock results, with no deployed-provider evidence. The handoff distinguishes the agreed version from unknown runtime support. One shared file used by both components requires no synchronized copy. Keep the cited owner revision, consumer pin and resulting compatibility passage; inspect the copy identity. No service deployment or provider test is needed to assess this writing change.

#### Scope and sources

Parent: this plan. Owner role: documentation maintainer. Child: S27. R23/A23. [Technical Writer baseline](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/interface_contract.md#L3-L17) · [comparison source](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/how-to/contract-driven-development.md#one-authoritative-owner)

#### S27 · Document the owner and consumer version of a shared contract

As a developer integrating a consumer with a provider, I want to identify the governing contract and supported version, so that a local edit cannot silently change the release agreement.

##### Acceptance criteria

- **S27.1** Given an owner contract at v1, a divergent consumer copy and a proposed v2, ask for an Interface Contract update. It identifies the source revision, pins the consumer to v1, names the discrepancy and directs the proposed change to the owner. The consumer copy is untouched. Provide only the v1 pin and mock results, with no deployed-provider evidence. The handoff distinguishes the agreed version from unknown runtime support. One shared file used by both components requires no synchronized copy. Use the same outputs for story and epic closure.

##### Scope and sources

Parent: F27. Responsible role: skill maintainer. W45 supports S27.1. Limit the change to the named writing route and the affected review.

##### W45 · Document the owner and consumer version of a shared contract

###### Description

The Interface Contract guide names the provider, consumers, version and source authority. Its worked handoff does not tell a consumer how to handle a locally edited copy, or how to distinguish a version pinned by the consumer from the version supported by the deployed provider.

###### Expected outcome

Identify the governing contract and supported version.

###### Scope

For independently released components, identify the authoritative source and immutable revision, the consumer’s copy or pin, and the evidence for deployed compatibility when claimed. Resolve disagreements at the owner. Leave deployment support unknown when there is no observation.

###### Specification

Parent: S27. Supports S27.1 and F27.1. R23/A23. Responsible role: skill maintainer. Use existing source and review contracts. Use the existing Interface Contract route.

###### Acceptance criteria

- **W45.1** Given an owner contract at v1, a divergent consumer copy and a proposed v2, ask for an Interface Contract update. It identifies the source revision, pins the consumer to v1, names the discrepancy and directs the proposed change to the owner. The consumer copy is untouched.
- **W45.2** Provide only the v1 pin and mock results, with no deployed-provider evidence. The handoff distinguishes the agreed version from unknown runtime support. One shared file used by both components requires no synchronized copy. Keep the cited owner revision, consumer pin and resulting compatibility passage; inspect the copy identity. No service deployment or provider test is needed to assess this writing change.

###### Relevant files

[Writing guidance](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/interface_contract.md) · [Affected handoff](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/examples/interface_contract.md) · [Upstream comparison](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/how-to/contract-driven-development.md#one-authoritative-owner)

###### Additional context

One commit ships the guidance with the affected example and any necessary route adjustment. Apply the shared Definition of Done. Initially Not demonstrated. Retain each criterion verdict, evidence and candidate in the task.

### F28 · Keep existing users working through the Spec Writer rename

As a developer, I want to invoke Spec Writer from a new or existing installation, so that my writing workflow survives the rename.

#### Acceptance criteria

- **F28.1** Fresh and existing users reach the same checked writer through their supported host. A pre-existing unrelated skill remains untouched. The accepted Builder validates a real document using the renamed release. Use the integrated readback at S28.1.

#### Scope and sources

Parent: this plan. Owner role: skill maintainer. Child: S28. R24/A24. [Evidence](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/install_skill.py)

#### S28 · Release the Spec Writer identity and legacy entry

As a developer, I want to invoke Spec Writer from a new or existing installation, so that my writing workflow survives the rename.

##### Acceptance criteria

- **S28.1** Fresh and existing users reach the same checked writer through their supported host. A pre-existing unrelated skill remains untouched. The accepted Builder validates a real document using the renamed release. Preserve observed failures and identify the candidate for each verdict.

##### Scope and sources

Parent: F28. Owner role: skill maintainer. W46 support S28.1. Use task evidence for the story when it proves the integrated outcome.

##### W46 · Release the Spec Writer identity and legacy entry

###### Description

The shipped name, discovery and examples use Technical Writer. Skill Builder also requires that literal dependency identity. A metadata-only rename can break both discovery and document acceptance.

###### Expected outcome

A new installation advertises Spec Writer with skill ID `spec-writer`. A previously supported invocation still reaches its writing workflow.

###### Scope

Canonical metadata, host entry points, installer, public README examples and existing aliases. Preserve historical receipt identifiers, the repository URL and user-owned destinations.

###### Specification

Parent: S28. Supports S28.1 and F28.1. R24/A24. Owner role: skill maintainer. Requires accepted Skill Builder B5/T50; coordinate host evidence with W17 and shortcut ownership with W35–W37.

###### Acceptance criteria

- **W46.1** On Codex and Claude Code, discover the new canonical skill and complete a checked writing request. On the existing-install path, invoke the former name and bind its result to the same writer. Keep one observed invocation per changed host path and reuse W17 when it proves that path. Inspect the release’s public names and link labels, including the existing source labels in `references/issue.md`, `references/implementation_plan.md` and `references/spec_driven_development.md`. Check the changed examples and session replies. The sole product name is Spec Writer. Use functional wording for the optional workflow. Retain the source links and required notices.
- **W46.2** On a machine with an unrelated `spec-writer` installation, setup reports the collision and preserves it. Run one real Builder document validation against the renamed release with the accepted B5 resolver; retain the package revision and receipt.

###### Relevant files

SKILL.md, README.md and scripts/install_skill.py; Skill Builder scripts/runtime/technical_writer.py. [Evidence](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/install_skill.py)

###### Additional context

Ship the working entry and its consumer in one commit. Record criterion verdicts, candidate and proof under the shared Definition of Done. Implementation initially Not demonstrated.

### F29 · Start a checked feature in an initialized workflow project

As a developer adopting the toolkit, I want the writing command to use the intended project and feature, so that it records my change under the right rules.

#### Acceptance criteria

- **F29.1** From an existing project, the installed command produces a checked spec for the selected feature on each supported host. Repeat setup preserves the edited project document. The standalone writer remains usable. Use the integrated readback at S29.1.

#### Scope and sources

Parent: this plan. Owner role: skill maintainer. Child: S29. R25/A25. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/extensions/developing.md)

#### S29 · Start one feature through an optional workflow extension

As a developer adopting the toolkit, I want the writing command to use the intended project and feature, so that it records my change under the right rules.

##### Acceptance criteria

- **S29.1** From an existing project, the installed command produces a checked spec for the selected feature on each supported host. Repeat setup preserves the edited project document. The standalone writer remains usable. Preserve observed failures and identify the candidate for each verdict.

##### Scope and sources

Parent: F29. Owner role: skill maintainer. W47 support S29.1. Use task evidence for the story when it proves the integrated outcome.

##### W47 · Start one feature through an optional workflow extension

###### Description

Standalone host shortcuts establish a document type. They do not by themselves establish an initialized workflow project, its active feature or the effective project override.

###### Expected outcome

The selected feature in an existing project receives a checked behavioral specification through a namespaced writing command.

###### Scope

Use upstream initialization and host integration. Read the active project and effective rule. Reuse the canonical writer; keep the workflow optional for standalone writing.

###### Specification

Parent: S29. Supports S29.1 and F29.1. R25/A25. Owner role: skill maintainer. Requires W46 and the checked behavioral-spec route. Use the upstream revision identified in the audit as the starting compatibility reference.

###### Acceptance criteria

- **W47.1** Initialize or reuse an existing project, select its refund feature, and issue a writing request on each target host. Capture the resulting checked feature path, project rule and command actually invoked. The existing standalone skill also accepts an ordinary request without the optional workflow; reuse W46 for this.
- **W47.2** Repeat setup with an edited feature document and two possible feature contexts. Preserve the edited document. Use an explicit selection or request the one missing choice; no write reaches the sibling feature.

###### Relevant files

scripts/install_skill.py and the behavioral-spec reference; upstream docs/extensions/developing.md and docs/presets/overview.md. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/extensions/developing.md)

###### Additional context

Ship the working entry and its consumer in one commit. Record criterion verdicts, candidate and proof under the shared Definition of Done. Implementation initially Not demonstrated.

### F30 · Give the implementing agent the complete task contract

As an implementer, I want the active feature’s task entry to carry the original criterion, so that I can implement it without the authoring conversation.

#### Acceptance criteria

- **F30.1** With two features using the same short upstream task number, the actual selected consumer reads the refund Issue, its authorized actor and denial criterion. A stale view stops the affected dispatch. Use the integrated readback at S30.1. Use W48.3 to show the actual consumer selects eligible work and observes the API dependency before offering the dashboard filter.

#### Scope and sources

Parent: this plan. Owner role: skill maintainer. Child: S30. R26/A26. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/commands/implement.md#L143-L153)

#### S30 · Select eligible feature work and recover its Issue criteria

As an implementer, I want the active feature’s task entry to carry the original criterion, so that I can implement it without the authoring conversation.

##### Acceptance criteria

- **S30.1** With two features using the same short upstream task number, the actual selected consumer reads the refund Issue, its authorized actor and denial criterion. A stale view stops the affected dispatch. Preserve observed failures and identify the candidate for each verdict. For the two-story refund list, recover both parallel status tasks, the first usable story, and the condition that releases the dependent filter. Reuse W48.3.

##### Scope and sources

Parent: F30. Owner role: skill maintainer. W48 support S30.1. Use task evidence for the story when it proves the integrated outcome.

##### W48 · Select eligible tasks from the feature list

###### Description

The upstream implementation command reads a phased tasks.md. Our Issue holds the bounded task and its acceptance. Matching filenames or an Issue link alone cannot establish what the downstream agent actually receives.

###### Expected outcome

Through its supported inputs, the real implementing agent reads the active feature, recognizes eligible and blocked tasks, and recovers the selected Issue’s stable ID, criterion, allowed actor, scope and proof.

###### Scope

Use one authoritative Issue per task. Supply the active feature spec, plan and W40’s `tasks.md` at the pinned integration’s normal inputs. Resolve feature-local IDs to the current Issue and criterion. Use source revisions and existing progress records to make safe selections. Acceptance requires the Issue’s evidence.

###### Specification

Parent: S30. Supports S30.1 and F30.1. R26/A26. Owner role: skill maintainer. Requires W47, W40 and W44. Prove actual consumption before designing more document commands.

###### Acceptance criteria

- **W48.1** Project an approved manager-only refund Issue into the selected feature. Observe the actual consumer extracting the scoped task and its denied-permission criterion from its normal inputs. Preserve the Issue as the editing authority.
- **W48.2** Give a sibling feature the same short task ID; revise the selected Issue after generating the view. The consumer must not take the sibling task or dispatch the stale revision. Reconcile against the governing Issue, retaining existing acceptance evidence.
- **W48.3** Give the actual implementing agent W40’s feature list and linked Issues through its normal entry, without coaching it on the order. Capture the consumer identifying both T001 and T002 as eligible together and explaining how their story can ship before filtering. At the start of US2, capture the consumer selecting T003 and identifying its working API as the reason T004 must wait. Once the approved API filter has evidence on the candidate, observe T004 become eligible and the agent recover #84’s governing criterion. A checkbox alone, an early dispatch or a wrong Issue fails. Retain the consumer’s selections, prerequisite evidence and source references. Reuse the same feature and applicable checkpoints. This check proves scheduling and handoff; it requires neither concurrent workers nor four fresh builds. At the implementation entry, observe that the agent opens the active plan, feature list and selected Issue. Reuse those selection observations to prove it returns to the same list for the next eligible row. A demand for a new `task.md` fails.

###### Relevant files

references/issue.md, references/implementation_plan.md; upstream templates/commands/tasks.md and templates/commands/implement.md. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/commands/implement.md#L143-L153)

###### Additional context

Use the W40 output retained for [W-PACKET](./test.md#cases) to observe selection before and after W01 evidence is supplied. Keep the rehearsal read-only. The refund case still owns the story demonstration and blocked API dependency.

Ship the working entry and its consumer in one commit. Record criterion verdicts, candidate and proof under the shared Definition of Done. Implementation initially Not demonstrated.

### F31 · Verify and resume one authorized implementation

As a developer, I want to hand one approved Issue to a coding agent and resume its verification, so that the verdict refers to the original task and the candidate actually run.

#### Acceptance criteria

- **F31.1** Follow one refund task from dispatch to an observed permission failure, correction and evidence-backed verdict. Resume at the same task and candidate boundary after interruption; uncertain effects cannot be replayed on guesswork. Use the integrated readback at S31.1.

#### Scope and sources

Parent: this plan. Owner role: skill maintainer. Child: S31. R27/A27. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/workflows/overview.md#run-review-and-resume)

#### S31 · Verify and resume one authorized implementation

As a developer, I want to hand one approved Issue to a coding agent and resume its verification, so that the verdict refers to the original task and the candidate actually run.

##### Acceptance criteria

- **S31.1** Follow one refund task from dispatch to an observed permission failure, correction and evidence-backed verdict. Resume at the same task and candidate boundary after interruption; uncertain effects cannot be replayed on guesswork. Preserve observed failures and identify the candidate for each verdict.

##### Scope and sources

Parent: F31. Owner role: skill maintainer. W49, W50 support S31.1. Use task evidence for the story when it proves the integrated outcome.

##### W49 · Hand one approved task to the selected implementation provider

###### Description

An authored task or checked box establishes intent or progress. It does not establish a dispatched provider, an observed candidate or the state of an interrupted write.

###### Expected outcome

One authorized coding session receives a bounded task and returns a verdict tied to its actual candidate and original criterion.

###### Scope

Connect the upstream implementation path in a disposable authorized project. In Mirai projects, preserve the project-selected owner and make the same packet available for its handoff. Product deployment or changes to Mirai are outside this task.

###### Specification

Parent: S31. Supports S31.1 and F31.1. R27/A27. Owner role: skill maintainer. Requires W48. Name the authority, provider and candidate in the task. No second provider may act on the same assignment.

###### Acceptance criteria

- **W49.1** Hand the manager-only refund Issue to the selected coding agent. Record the real dispatch and observed candidate. A candidate allowing an employee to refund fails the original denial criterion; retain the observed behavior and candidate. For the workflow integration, document that the bundled workflow ends at Implement. Use the existing criterion evidence to complete ordinary delivery without invoking Converge. Document Converge as available only on explicit user request.
- **W49.2** Use scoped correction and the smallest discriminating check to observe the required denial on the corrected candidate. Keep the earlier failure. A checkbox or suggested out-of-scope enhancement cannot change the criterion or authorize new work.

###### Relevant files

Upstream templates/commands/implement.md, templates/commands/converge.md and workflows/speckit/workflow.yml; writer verification and handoff references. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/workflows/overview.md#run-review-and-resume)

###### Additional context

Ship the working entry and its consumer in one commit. Record criterion verdicts, candidate and proof under the shared Definition of Done. Implementation initially Not demonstrated.

##### W50 · Resume the same task after an interrupted run

###### Description

An authored task or checked box establishes intent or progress. It does not establish a dispatched provider, an observed candidate or the state of an interrupted write.

###### Expected outcome

The developer can recover the last confirmed execution or evidence boundary without duplicate task effects.

###### Scope

Use the original run and provider status, revision and task bindings. Keep unresolved external effects uncertain until reconciled.

###### Specification

Parent: S31. Supports S31.1 and F31.1. R27/A27. Owner role: skill maintainer. Requires W49. Reuse its task packet and candidate evidence; interrupt only the boundary needed for this check.

###### Acceptance criteria

- **W50.1** Interrupt one authorized task before its outcome is recorded. Resume the same feature and run, recover the task, criterion and last observed candidate, and identify the next safe action from provider evidence.
- **W50.2** When prior dispatch may have taken effect, consult available authoritative state. Preserve uncertainty if it cannot be resolved. Retain evidence that resumption caused no duplicate dispatch or application write.

###### Relevant files

Upstream docs/workflows/overview.md and docs/workflows/cli.md; existing writer recovery and evidence records. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/workflows/overview.md#run-review-and-resume)

###### Additional context

Ship the working entry and its consumer in one commit. Record criterion verdicts, candidate and proof under the shared Definition of Done. Implementation initially Not demonstrated.

### F32 · Route an idea or bug to the right upstream workflow

As a project contributor, I want to enter with an uncertain idea or an observed defect, so that I receive the decision or repair record my situation needs.

#### Acceptance criteria

- **F32.1** An idea lacking decision evidence ends with a supported question or stop recommendation; a bounded defect reaches a scoped repair and expected check. Neither input silently starts coding. Use the integrated readback at S32.1.

#### Scope and sources

Parent: this plan. Owner role: skill maintainer. Child: S32. R28/A28. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/guides/assessment.md)

#### S32 · Route an idea or bug to the right upstream workflow

As a project contributor, I want to enter with an uncertain idea or an observed defect, so that I receive the decision or repair record my situation needs.

##### Acceptance criteria

- **S32.1** An idea lacking decision evidence ends with a supported question or stop recommendation; a bounded defect reaches a scoped repair and expected check. Neither input silently starts coding. Preserve observed failures and identify the candidate for each verdict.

##### Scope and sources

Parent: F32. Owner role: skill maintainer. W51, W52 support S32.1. Use task evidence for the story when it proves the integrated outcome.

##### W51 · End idea assessment at a supported decision

###### Description

The approved writing routes describe relevant outputs. The optional upstream assessment and bug workflows also need a handoff that preserves their distinct starting points and authority.

###### Expected outcome

An unshaped idea produces a grounded brief, decision recommendation or focused question.

###### Scope

Adapt the optional idea assessment entry to existing formats and decision authority.

###### Specification

Parent: S32. Supports S32.1 and F32.1. R28/A28. Owner role: skill maintainer. Requires W47 and existing brief/interview routes. No coding or mandatory feature spec on intake.

###### Acceptance criteria

- **W51.1** Supply an idea with a consequential evidence gap. The assessment names that gap, identifies who can decide and recommends clarification or stopping. Preserve source and output.
- **W51.2** On a supported decision to proceed, identify the next document and its benefit. A recommendation alone cannot create a task or dispatch an implementation.

###### Relevant files

Upstream workflows/assess/workflow.yml; existing decision record, interview and brief routes. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/guides/assessment.md)

###### Additional context

Ship the working entry and its consumer in one commit. Record criterion verdicts, candidate and proof under the shared Definition of Done. Implementation initially Not demonstrated.

##### W52 · Turn a reported defect into one bounded repair

###### Description

The approved writing routes describe relevant outputs. The optional upstream assessment and bug workflows also need a handoff that preserves their distinct starting points and authority.

###### Expected outcome

A defect reaches a source-grounded bug report or independent repair Issue with its expected observable check.

###### Scope

Use the optional bug route and the project’s established parent rules. Separate observed symptom, expected behavior and unconfirmed cause.

###### Specification

Parent: S32. Supports S32.1 and F32.1. R28/A28. Owner role: skill maintainer. Requires W47 and W30–W31. Reuse the existing bug and Issue authoring routes.

###### Acceptance criteria

- **W52.1** Given one observed save failure with a known expected outcome, produce a repair record with the observation, the expected result and the smallest check that distinguishes them.
- **W52.2** Given only a suspected cause, keep it provisional. A bounded independent repair needs no fabricated story or PRD and writing it cannot authorize execution.

###### Relevant files

references/bug_report.md and references/issue.md; upstream workflows/bugfix/workflow.yml. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/guides/assessment.md)

###### Additional context

Ship the working entry and its consumer in one commit. Record criterion verdicts, candidate and proof under the shared Definition of Done. Implementation initially Not demonstrated.

### F33 · Maintain a versioned workflow integration

As a maintainer, I want to install, inspect, upgrade and remove the integration, so that I can adopt it without losing project documents.

#### Acceptance criteria

- **F33.1** Using a versioned local release and a declared upstream version, inspect the effective command, upgrade the managed integration, then remove it. Project-authored documents and other installed commands survive. Use the integrated readback at S33.1.

#### Scope and sources

Parent: this plan. Owner role: skill maintainer. Child: S33. R29/A29. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/bundles/overview.md)

#### S33 · Distribute and safely update the versioned integration

As a maintainer, I want to install, inspect, upgrade and remove the integration, so that I can adopt it without losing project documents.

##### Acceptance criteria

- **S33.1** Using a versioned local release and a declared upstream version, inspect the effective command, upgrade the managed integration, then remove it. Project-authored documents and other installed commands survive. Preserve observed failures and identify the candidate for each verdict.

##### Scope and sources

Parent: F33. Owner role: skill maintainer. W53 support S33.1. Use task evidence for the story when it proves the integrated outcome.

##### W53 · Distribute and safely update the versioned integration

###### Description

The standalone installer preserves an existing destination. The optional ecosystem integration also needs a declared compatible upstream version, identifiable managed components and a safe upgrade or removal path.

###### Expected outcome

A team can install a versioned artifact, see what won resolution, update owned components and remove them safely.

###### Scope

Create a testable local release and user instructions. Use an upstream bundle only if it adds value and components resolve. External registry submission and remote release are separate actions.

###### Specification

Parent: S33. Supports S33.1 and F33.1. R29/A29. Owner role: skill maintainer. Requires the connected W47–W50 path and the entry points included in the release. Reuse earlier host observations for unchanged behavior.

###### Acceptance criteria

- **W53.1** Install the release against its declared upstream version. Inspect the active command or template source, upgrade from the prior supported package and remove the owned integration. The working feature document and another command remain available.
- **W53.2** Supply an incompatible upstream version or a conflicting user-edited component. Identify the constraint and preserve user content. Retain the observed version, ownership decision and before/after paths; no registry publish is necessary.

###### Relevant files

Upstream docs/bundles/overview.md, docs/overview/artifacts.md and docs/upgrade.md; installer and public usage documentation. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/bundles/overview.md)

###### Additional context

Ship the working entry and its consumer in one commit. Record criterion verdicts, candidate and proof under the shared Definition of Done. Implementation initially Not demonstrated.

### F37 · Use the full writing catalog in the optional workflow

As a project maintainer, I want the workflow to use the same document types as the standalone writer, so that a team can adopt it without giving up the documents it relies on.

#### Acceptance criteria

- **F37.1** Given the candidate catalog and an authorized feature with a reviewed design, a user can request a catalog document through the optional entry and a later task can recover the relevant design constraint. A document-only request ends at delivery. Retain the catalog comparison and the observations from S37.1 on the same release.

#### Scope and sources

Parent: this plan. Owner role: skill maintainer. Child: S37. R33/A33. Apply the existing writing rules, source requirements, host authority and shared Definition of Done. The borrowed workflow definition continues to own its execution steps.

#### S37 · Write the requested document and pass it to the right consumer

As a developer, I want to request a specific document and have later work use its reviewed version, so that I can move from writing into development when my project needs it.

##### Acceptance criteria

- **S37.1** From the supported workflow entry, request a tutorial and observe its checked delivery without provider dispatch. For an authorized feature, pass a reviewed low-level design to a child task and observe its exact source and boundary in the task. A stale reference blocks dependent dispatch. Retain the W58 and W59 outputs and verdicts on the candidate. Reuse the same observations for F37.1.

##### Scope and sources

Parent: F37. Owner role: skill maintainer. W58 covers document selection and the stopping point. W59 covers the consuming task and stale-input boundary. R33/A33 owns both. Use W47’s settled project selection and the existing conditional hierarchy.

##### W58 · Request any supported writing format through the workflow

###### Description

The existing workflow acceptance case exercises a feature specification. A developer also needs a direct entry to the writer’s other supported formats.

###### Expected outcome

A developer using the optional entry receives the requested document in its native format and can stop there.

###### Scope

Extend the borrowed command at the writer boundary to resolve full names and supported aliases using the existing catalog. Preserve edit scope, discovery, checked delivery, native format and host authority. Apply the same public naming rule as W46. Use the existing routing mechanism for the seven approved forms as they ship.

###### Specification

Parent: S37. Supports S37.1 and F37.1. R33/A33. Owner role: skill maintainer. Requires the W47 entry, W35 routing, and the approved document routes whose coverage is being accepted. This increment can ship independently of W59.

###### Acceptance criteria

- **W58.1** Given the candidate’s catalog, output contracts and A10a–g, resolve every supported kind and advertised alias through the optional entry. Compare the selected owner, contract or named variant to standalone routing. Documented guidance-only entries retain their role. A missing kind, generic fallback, wrongly shared contract or lost native format fails. Save the candidate and the catalog differences. This is a routing comparison, so it requires no generated document per alias.
- **W58.2** Given a project and enough verified input, request a Tutorial through the installed workflow and follow its normal checked-delivery path. Retain the tutorial, its own contract/receipt and the observed endpoint. An unrelated specification, work item or provider dispatch fails. Exercise the shared route once and reuse W47’s host observations wherever the adapter is unchanged.

###### Relevant files

`SKILL.md`, `contracts/documents.json`, `references/tutorial.md` and the installed command adapter introduced by W47. Use the source mapping at the start of this plan.

###### Additional context

Commit the accepting entry and its catalog coverage together. Record each criterion’s verdict, candidate and proof under the shared Definition of Done. Initial status is Not demonstrated.

##### W59 · Carry a reviewed document into a dependent task

###### Description

Feature tasks need the actual rules in linked documents, including documents beyond the upstream feature templates.

###### Expected outcome

A task author receives the selected document’s relevant constraint and can see when a source revision needs attention.

###### Scope

Adapt the existing document handoff where the workflow prepares the next eligible document or task. Preserve the writer’s prerequisite, authority, revision and evidence rules. Use an exact link or scoped view. Keep W48’s task representation and the shipped execution sequence.

###### Specification

Parent: S37. Supports S37.1 and F37.1. R33/A33. Owner role: skill maintainer. Requires W58, W48 and W38–W39. Use the project’s existing Issue, story and Low Level Design (LLD). An unrelated document has no new prerequisite.

###### Acceptance criteria

- **W59.1** Given an authorized refund feature, a story and a reviewed design stating that only a manager may approve a refund, use the workflow to prepare its child Issue. Inspect the Issue at the task consumer. It names the story, the exact design revision and section, and the employee-denial criterion. A generic “check permissions” or a sibling feature’s design fails. Keep the actual source and consumer view.
- **W59.2** Given the same task with an unresolved revision change in its referenced design, request the next dependent action. The workflow identifies the affected source and stops that dispatch while preserving the documents, prior evidence and unrelated work. Keep the observed refusal and source identifiers. Reuse W48 evidence if it already exercises this document boundary on this candidate.

###### Relevant files

`references/low_level_design.md`, `references/issue.md`, the W38–W39 handoff and W48’s actual task consumer.

###### Additional context

Commit the connected handoff and its safe failure together. Apply the shared Definition of Done and record each criterion’s verdict, candidate and proof. Initial status is Not demonstrated.

### F38 · Write feature guidance and session replies around the reader’s decision

As a reader, I want guidance and session replies to tell me what I can do and what happened, so that I can act without guessing.

#### Acceptance criteria

- **F38.1** Given the reviewed guide and refund example, a reader can identify where to act, the actor allowed to approve and the open retry decision. A completed document cannot establish that a refund ran. Reuse S38.1.

#### Scope and sources

Parent: this plan. Child: S38. R34/A34. Owner role: writing maintainer. Covers the shared guide; live host performance remains under the existing host tasks.

#### S38 · Explain the feature and report the checked result

As a writer, I want the procedure and the session reply to use the same facts, so that the reader can follow the procedure and the owner can see which decision is still open.

##### Acceptance criteria

- **S38.1** Apply the guide to the sourced refund example. Recover the reviewed rule and open question from the reply, and the source and next action from the example procedure. Reject an invented runtime outcome. Reuse W60.1.

##### Scope and sources

Parent: F38. W60 supports S38.1. Owner role: writing maintainer.

##### W60 · Teach feature-page and session wording in the live style guide

###### Description

The owner authorized an immediate guide edit following the comparative audit.

###### Expected outcome

A writer can use the shared guide for a procedure, reference lookup and checked session reply.

###### Scope

Change the feature-page and session guidance. Preserve existing format ownership, source authority and factual status.

###### Specification

Parent: S38. Supports S38.1 and F38.1. R34/A34. Owner role: writing maintainer. Uses the completed source audit.

###### Acceptance criteria

- **W60.1** Given a manager-only approval rule and an unresolved retry decision, apply the revised guidance to a feature page and a session handoff. The two passages identify the source or decision as appropriate, retain the manager-only rule and leave runtime success unclaimed. Keep the exact guide revision and example comparison.

###### Relevant files

`references/writing_style.md` and its links to the owning format guides.

###### Additional context

Met on d8bf859f0eec178aa34b24e29aef10290e984c3b for the guide and author-applied example. The writing-style contract, repository and layout integrity checks passed. Reuse the [committed guide](https://github.com/fatonsopa/ai-technical-writer/blob/d8bf859f0eec178aa34b24e29aef10290e984c3b/references/writing_style.md#write-a-feature-page-people-can-use). The checkout layout now identifies the owner-requested plan directory. W60 needs no repeat implementation. Cross-host performance is assessed in W17.

### F39 · Make every released feature and supported document type findable

As a developer, I want to find the instructions for a feature or document type from the public index, so that I know when to use it, what to supply and what to expect.

#### Acceptance criteria

- **F39.1** Given the candidate’s public capabilities and supported document catalog, follow their index entries from the repository README. Each resolves to usable instructions on a page or at a named section. Aliases and variants may share a destination that covers them. An omitted entry, irrelevant destination or unshipped feature presented as ready fails. Save the candidate revision, coverage comparison and representative destinations.

#### Scope and sources

Parent: this plan. Child: S39. R35/A35. Owner role: documentation maintainer. Covers existing and newly released features and supported document types.

#### S39 · Find instructions for a feature or document type from the index

As a new user, I want the index to take me to the instructions for my request, so that I can start the right task.

##### Acceptance criteria

- **S39.1** From the same index, open the focused-edit and document-review entries. The first explains how to change only the selected text. The second explains how to obtain located findings. Both may resolve to sections in the same file. Use one supported Issue variant to show that a shared section can explain its specific inputs. Reuse the release comparison and observations from W54 and W61.

##### Scope and sources

Parent: F39. W54 owns the first usable route. W61 owns existing release coverage. The task that delivers a new feature or document type owns its guidance and index link. Owner role: documentation maintainer.

##### W54 · Publish the public index with a usable focused-edit entry

###### Description

The current README describes focused edits inside a list of scenarios.

###### Expected outcome

A reader can follow the index to the focused-edit instructions and request a change with a clear boundary.

###### Scope

Link the public index from the README. Point the focused-edit entry at its existing named section and improve that section if the example omits a needed input or result. Link additional released routes as their guidance becomes usable.

###### Specification

Parent: S39. Supports S39.1 and F39.1. R35/A35. Owner role: documentation maintainer. Reuses the existing edit route. W54 was previously proposed under S34. Its revised scope is approved here.

###### Acceptance criteria

- **W54.1** From the candidate README, follow the index link for a focused edit. A direct link to “Make a focused edit” passes when it explains the title-only request, the preserved description and how to inspect the result. A working link to “Review a document” fails for that request. Keep the destination and the text that settles the distinction.
- **W54.2** Open the index links included in this increment. Each guide or named section resolves on the candidate. A missing heading, an empty stub or a planned feature presented as ready fails. Save the candidate and link results.

###### Relevant files

`README.md` (including its focused-edit section), planned `docs/README.md`, and `references/readme.md`.

###### Additional context

Ship the index and its first usable link in one commit. Initial verdicts: Not demonstrated. Apply the shared Definition of Done.

##### W61 · Complete index coverage for the existing release

###### Description

Creating a new index does not make the existing feature set discoverable.

###### Expected outcome

A reader can locate instructions for each feature and document format that the release already supports.

###### Scope

Compare released entry points, README scenarios and supported document types against the public index. Link to useful existing sections first. Fill a gap in the owning guidance or write a separate guide when the reader needs a distinct procedure or reference. Keep each correction with its index link.

###### Specification

Parent: S39. Supports S39.1 and F39.1. R35/A35. Owner role: documentation maintainer. Requires W54 and the identified release. Use the existing catalog and index as the record.

###### Acceptance criteria

- **W61.1** Compare every released user-facing feature and supported document type with the index. Check that each link opens at the intended instructions. For a chore Issue, a link to “Issue types and titles” can pass when it identifies the chore’s inputs and the Issue guide gives the expected result. An absent type or a link that leaves the reader searching fails. Retain the candidate, coverage differences and their disposition.
- **W61.2** Reuse W54’s focused-edit evidence and open the review entry on the same release. The review guidance returns located findings and preserves the reviewed document. Distinct, useful headings in one file pass. A broken heading or a link to the focused-edit instructions fails even when the file exists. Retain the observed destinations. Recheck only changed links or uncovered entries.

###### Relevant files

`README.md`, `SKILL.md`, `contracts/documents.json`, the public index and the existing pages or sections it links to.

###### Additional context

Record Met, Failed or Not demonstrated per criterion and identified release. Reuse accepted increments after interruption. Initial verdicts: Not demonstrated.

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
| R17 / A17b | F21 → S21 → W62 | Resolve the refund rule and component, accept the contract-only design, and reuse A11 for the unresolved child. |
| R19 / A19 | F23 → S23 → W35–W37, W40–W41 | Actual host dispatch, canonical template, two-story refund list and linked Issue criteria and read-only review. |
| R20 / A20 | F24 → S24 → W38–W39 | Ready, blocked and complete cases; one checked successor, no duplicate or stale handoff. |
| R21 / A21 | F25 → S25 → W43 | Maintained rule versus a frozen launch snapshot, then a conflict with no governing decision. |
| R22 / A22 | F26 → S26 → W44 | Return.code versus Order.code, a misattributed field in review, and an unrelated prose Issue. |
| R23 / A23 | F27 → S27 → W45 | Versioned owner definition, divergent consumer copy and a pin without deployed-provider evidence. |
| R24 / A24 | F28 → S28 → W46 | Fresh and existing users reach the same checked writer through their supported host. A pre-existing unrelated skill remains untouched. The accepted Builder validates a real document using the renamed release. |
| R25 / A25 | F29 → S29 → W47 | From an existing project, the installed command produces a checked spec for the selected feature on each supported host. Repeat setup preserves the edited project document. The standalone writer remains usable. |
| R26 / A26 | F30 → S30 → W48 | With two features using the same short upstream task number, the actual selected consumer reads the refund Issue, its authorized actor and denial criterion. A stale view stops the affected dispatch. On the refund-status list, observe the parallel pair and the API prerequisite holding and releasing T004. |
| R27 / A27 | F31 → S31 → W49, W50 | Follow one refund task from dispatch to an observed permission failure, correction and evidence-backed verdict. Resume at the same task and candidate boundary after interruption; uncertain effects cannot be replayed on guesswork. |
| R28 / A28 | F32 → S32 → W51, W52 | An idea lacking decision evidence ends with a supported question or stop recommendation; a bounded defect reaches a scoped repair and expected check. Neither input silently starts coding. |
| R29 / A29 | F33 → S33 → W53 | Using a versioned local release and a declared upstream version, inspect the effective command, upgrade the managed integration, then remove it. Project-authored documents and other installed commands survive. |
| R33 / A33 | F37 → S37 → W58, W59 | Catalog route comparison, checked tutorial at the public entry, task consuming the reviewed design, and refusal on a stale revision. |
| R34 / A34 | F38 → S38 → W60 | Review the committed guide, its two reader situations and the sourced example. |
| R35 / A35 | F39 → S39 → W54, W61 | Compare all released features and supported types with direct index destinations. Use focused editing, review and a chore Issue to check that a useful page or section answers the request. |
| R18 / A18 | F22 → S22 → W32, W33, W34 | Same export route, two requests, actual question counts, answer binding, review and readiness verdicts. |
| R16 / A16 | F20 → S20 → W29, W42 | Worked WEB-06 trace before setup and two reader routes from the `README.md` file and resolved guide links. |
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

Revision 19 carries forward the approved scope, including the conditional hierarchy, first-use naming convention, reviewed-delivery sentence and evidence-based clarification under R18/A18. Internal file names and implementation choices are delegated within the approved scope. A missing host observation remains Not demonstrated.

## Pending owner decisions

Append out-of-scope discoveries here with their source, observed effect, proposed change, impact of deferral and any task actually blocked. Only an explicit owner decision can add them to implementation scope.

The approved work comprises F1–F33 and F37–F39, their 36 child stories, and W01–W54 plus W58–W62. W60’s guide edit shipped on the handoff branch before the remaining implementation. W46 covers the public identity, W49 covers on-request Converge, and W58–W59 cover the full writing catalog. The additional worked walkthrough and demonstrations in F34–F36 (W55–W57), and the additional assessment criterion W51.3, await the owner’s approval. F39 now owns the approved index task W54 and index coverage for every released feature and supported document type. Exclude only the pending proposals from execution and completion counts. W51.1–W51.2 remain the approved criteria for idea assessment. A proposed guide or extra demonstration is a separate decision from the selected upstream workflow.

### Proposed assessment refinement

Adapt the optional idea assessment entry to existing formats and decision authority. In workflow mode the optional assessment uses one idea slug, ordinarily progressing from intake to research, problem definition, concept comparison and decision. The upstream outputs are `intake.md`, `research.md`, `problem.md`, `concept.md` and `decision.md` under `.specify/assessments/<slug>/`. Use those artifacts when integrating the extension. Their contents reuse the writer’s existing interview, brief, research and decision guidance. The standalone writer can keep a small decision in its existing format.

Define can start from supplied intent. Shape and Decide require the problem definition. A `go` additionally needs adequate problem validity and evidence strength and a recommended concept. Include evidence for and against the idea, cite the source and confidence, and preserve assumptions as such. A `needs-clarification` verdict names the missing fact and affected record. A `kill` verdict retains the decisive reason and ends the assessment. Refine the affected artifact and decision when new evidence arrives. Only a separate choice to pursue the software idea passes the decision summary to Specify.

- **W51.3** In one initialized project, follow one idea slug to its decision. With weak evidence or a missing concept, the decision identifies the blocker. Supply the missing sourced fact and recommended concept for the same idea, retain opposing evidence and confidence, and revise only the affected records. A supported go contains a handoff summary without writing a feature spec or starting implementation. For a stop, retain the decisive reason and close the assessment. Use the same records to inspect the verdict boundaries; do not repeat five live stages per verdict.

### Proposed public guides and workflow checks

These records retain their stable IDs and original checks for review. Implementation authority is pending for each record below.

### F34 · Find a capability and follow a feature from request to evidence

As a developer using Spec Writer for the first time, I want to choose a supported capability and follow one feature through its documents, so that I know what to supply, inspect and do next.

#### Acceptance criteria

- **F34.1** From the root README, a new reader chooses an existing-document request or the optional feature route, then identifies the input, output and next consumer for the complete refund example. Each advertised capability has a reachable entry on the identified release. Use S34.1 evidence on the candidate.

#### Scope and sources

Parent: this plan. Owner role: integration documentation maintainer. Child: S34. R30/A30. [Upstream guide](https://github.github.io/spec-kit/index.html)

#### S34 · Find a capability and follow a feature from request to evidence

As a developer using Spec Writer for the first time, I want to choose a supported capability and follow one feature through its documents, so that I know what to supply, inspect and do next.

##### Acceptance criteria

- **S34.1** From the root README, a new reader chooses an existing-document request or the optional feature route, then identifies the input, output and next consumer for the complete refund example. Each advertised capability has a reachable entry on the identified release. Record what the reader or operator actually found.

##### Scope and sources

Parent: F34. Owner role: integration documentation maintainer. W55 supports S34.1 and consumes the approved W54 index. Use the shared Definition of Done.

##### W55 · Walk a reader through the default feature path

###### Description

W29 and W42 explain chronology and one example in the README. W53 covers installation and upgrade. None commissions a maintained capability reference and a worked quickstart that distinguishes terminal setup from agent actions, standalone writing from optional integration, or a planned check from an observed result.

###### Expected outcome

A developer can follow one refund requirement from source intent through its spec, plan and task to the observed candidate and its acceptance evidence, with a separate on-request convergence example.

###### Scope

Use one worked Tutorial in repository docs. Name each producer, concrete path or result, next consumer and evidence boundary. Show the shorter path and where clarify, checklist and analyze help an affected decision. Map host-specific syntax to the same steps. Link W57 for executing the upstream workflow.

###### Specification

Parent: S34. Supports S34.1 and F34.1. R30/A30. Owner role: integration documentation maintainer. Uses W47–W49 and the accepted manual boundary. Publish with verified commands and actual candidate evidence; reuse W49/W57 observations when compatible.

###### Acceptance criteria

- **W55.1** Follow a manager-only refund request from the README. Identify the selected feature, expected actor, owning spec clause, corresponding plan decision, Issue/criterion and upstream task entry. At each step name what is now available for the next action. Show code and candidate evidence at Implement; Converge can leave tasks.md unchanged.
- **W55.2** Use one unresolved permission choice to locate clarify before planning; a requirements-quality question is answered by checklist, and a contradiction across the three documents is reported by read-only analyze before dispatch. Identify where a small writing request ends without starting a delivery. Keep the walkthrough and the located answers; no second full implementation run.

###### Relevant files

Planned public page: `docs/quickstart.md`. README.md, references/tutorial.md, the worked feature sources and the selected release’s supported command reference. [Upstream guide](https://github.github.io/spec-kit/index.html)

###### Additional context

Commit the usable page with its entry link and necessary integration adjustment. Record criterion verdicts, candidate and proof in this task. Implementation initially Not demonstrated.

### F35 · Inspect what the installed integration exposes

As a maintainer, I want to see which command or template is active in this project, so that I can explain an unexpected result without guessing from filenames.

#### Acceptance criteria

- **F35.1** From a project with one known override, locate its contribution and the lower layer with the native inventory; find the generated feature spec separately. Inspection leaves the project content unchanged. Use S35.1 evidence on the candidate.

#### Scope and sources

Parent: this plan. Owner role: integration documentation maintainer. Child: S35. R31/A31. [Upstream guide](https://github.github.io/spec-kit/overview/artifacts.html)

#### S35 · Inspect what the installed integration exposes

As a maintainer, I want to see which command or template is active in this project, so that I can explain an unexpected result without guessing from filenames.

##### Acceptance criteria

- **S35.1** From a project with one known override, locate its contribution and the lower layer with the native inventory; find the generated feature spec separately. Inspection leaves the project content unchanged. Record what the reader or operator actually found.

##### Scope and sources

Parent: F35. Owner role: integration documentation maintainer. W56 support S35.1. Use the shared Definition of Done.

##### W56 · Explain an installed override from native artifact readback

###### Description

W47 and W53 ask for the effective command or rule. They do not specify how a user lists the installed command, template, script and hook inventory or distinguishes an override from a generated feature document.

###### Expected outcome

A maintainer can reproduce the winning contribution and distinguish it from the spec and tasks generated for a feature.

###### Scope

Ship a short reference or How-to Guide (HTG) using the existing upstream CLI. Explain kinds, layered composition and additive hook registration; describe nullable provenance as reported. Keep the generated file map with the feature guide.

###### Specification

Parent: S35. Supports S35.1 and F35.1. R31/A31. Owner role: integration documentation maintainer. Uses W47’s installed test project and W53’s release evidence where compatible. Upstream inventory is optional with the integration.

###### Acceptance criteria

- **W56.1** Run `specify artifact list --json` and then `specify artifact info <id> --json` using a real returned ID in the project with an override. The guide identifies its kind, winning contribution and visible lower layer or suppression. Distinguish participation in composition from the winning layer.
- **W56.2** Use an unknown artifact ID to show the supported lookup error. Explain where to find that feature’s spec.md separately. For a documented hook, registration alone does not establish execution. Retain the JSON and before/after project state from these read-only lookups; no new scanner, hook execution or host matrix.

###### Relevant files

Planned public page: `docs/artifacts.md`. Upstream docs/overview/artifacts.md, src/specify_cli/artifacts and the existing integration installation instructions. [Upstream guide](https://github.github.io/spec-kit/overview/artifacts.html)

###### Additional context

Commit the usable page with its entry link and necessary integration adjustment. Record criterion verdicts, candidate and proof in this task. Implementation initially Not demonstrated.

### F36 · Document an on-request convergence review after the upstream workflow

As a developer running the optional integration, I want to know when automation stops and how to check the candidate, so that a successful workflow exit cannot silently become a feature acceptance claim.

#### Acceptance criteria

- **F36.1** Use the shipped upstream workflow on the authorized feature. A spec verdict leaves the plan gate independent. After Implement, the operator closes against acceptance evidence and, if the user requests a broader review, runs Converge manually for that same feature and candidate. A remaining gap stays open until the underlying criterion is proved. Use S36.1 evidence on the candidate.

#### Scope and sources

Parent: this plan. Owner role: integration documentation maintainer. Child: S36. R32/A32. [Upstream guide](https://github.github.io/spec-kit/workflows/overview.html)

#### S36 · Document an on-request convergence review after the upstream workflow

As a developer running the optional integration, I want to know when automation stops and how to check the candidate, so that a successful workflow exit cannot silently become a feature acceptance claim.

##### Acceptance criteria

- **S36.1** Use the shipped upstream workflow on the authorized feature. A spec verdict leaves the plan gate independent. After Implement, the operator closes against acceptance evidence and, if the user requests a broader review, runs Converge manually for that same feature and candidate. A remaining gap stays open until the underlying criterion is proved. Record what the reader or operator actually found.

##### Scope and sources

Parent: F36. Owner role: integration documentation maintainer. W57 support S36.1. Use the shared Definition of Done.

##### W57 · Explain how to request a convergence review on a built feature

###### Description

W49–W50 cover dispatch, verification and resume, but leave the public operator entry and the instructions for a user-requested Converge review unspecified. The pinned bundled YAML ends at Implement. Its spec and plan gates have separate verdicts.

###### Expected outcome

The operator can run the upstream definition, inspect or resume the correct run, and choose a separate convergence review upon user request.

###### Scope

Use upstream status, resume and gate behavior on the pinned release. State terminal versus agent actions. The writer does not ship a replacement YAML workflow, automatically loop, or give approval on the user’s behalf. Preserve documents, task IDs, history and provider ownership.

###### Specification

Parent: S36. Supports S36.1 and F36.1. R32/A32. Owner role: integration documentation maintainer. Uses W47–W50. Coordinate the same run and fixture with W49/W50 and the W55 tutorial. W53 distribution can link this guide as soon as the workflow is supported.

###### Acceptance criteria

- **W57.1** In the upstream run for the refund feature, observe separate spec and plan reviews. Use status and, at a genuine pause, resume the same run. Record the Implement result, active feature, Issue revision and candidate. When explicitly requested, manual Converge on the matching feature yields an observed outcome distinct from the workflow exit.
- **W57.2** For a named unmet criterion, an appended task is reconciled to its source Issue before another implementation. Preserve the append and original failure when refreshing a generated task view. Extra scope remains for the owner. With no gap, show no appended task. Reuse the failing and corrected W49 outcomes; demonstrate any unobserved branch at the smallest affected boundary.

###### Relevant files

Planned public page: `docs/workflows.md`. Upstream workflows/speckit/workflow.yml, docs/workflows/overview.md, templates/commands/converge.md and the existing implementation and recovery evidence. [Upstream guide](https://github.github.io/spec-kit/workflows/overview.html)

###### Additional context

Commit the usable page with its entry link and necessary integration adjustment. Record criterion verdicts, candidate and proof in this task. Implementation initially Not demonstrated.
