# Spec Writer implementation tasks

Read the [specification](./specification.md) for the required behavior and the [implementation plan](./implementation-plan.md) for the delivery approach. Each row links to the Issue that owns its scope, acceptance criteria and proof. The path in a row points to a starting file. The Issue identifies the full change. The short task number is local to this list. Use the linked Issue ID when handing work to another repository.

Start only after receiving the accepted Skill Builder candidate and its commit. W01 and W03 are the first two eligible Issues. W01 restores the usable fixture. W03 independently checks that assigned work traces back to its requirement. W60 already has accepted evidence. W55–W57 and W51.3 await an owner decision and cannot be selected.

Order expresses delivery preference. An Issue can start when its stated inputs, authority and dependencies are settled. `[P]` identifies the opening pair whose changes can run in parallel. A writing-only request ends at the reviewed list. During an authorized build, open the next eligible Issue, verify it, record the candidate and evidence there, mark its row, then return here. Verify each story at its linked acceptance criteria. [Read-only handoff test](./test.md)

## S01 · Edit a mixed passage without corrupting its fixture

**Demonstrate the story.** Derive the fixture domain from its literal value and recognize the genuine document label. [Story criteria](./implementation-plan.md#s01--edit-a-mixed-passage-without-corrupting-its-fixture)

- [ ] T001 [P] [US1] Repair the Websites Review fixture and its consumers. `examples/test_specification.md`. [W01 · W01.1, W01.2](./implementation-plan.md#w01--repair-the-websites-review-fixture-and-its-consumers)

## S02 · Commission a task from a reviewed requirement

**Demonstrate the story.** Trace a commissioned task from its authority to the behavior and proof the implementer receives. [Story criteria](./implementation-plan.md#s02--commission-a-task-from-a-reviewed-requirement)

- [ ] T002 [P] [US2] Resolve coverage in both directions. `references/implementation_plan.md`. [W03 · W03.1, W03.2](./implementation-plan.md#w03--resolve-coverage-in-both-directions)
- [ ] T003 [US2] Resolve feature, story and task ancestry before drafting. `workflows/discover.md`. [W20 · W20.1, W20.2](./implementation-plan.md#w20--resolve-feature-story-and-task-ancestry-before-drafting) After W03.
- [ ] T004 [US2] Write an epic whose stories prove a usable outcome. `references/user_story.md`. [W11 · W11.1, W11.2](./implementation-plan.md#w11--write-an-epic-whose-stories-prove-a-usable-outcome) After W20. If the scope spans capabilities, use W10 first.

## S01 · Edit a mixed passage without corrupting its fixture (continued)

**Demonstrate the story.** Derive the fixture domain from its literal value and recognize the genuine document label. [Story criteria](./implementation-plan.md#s01--edit-a-mixed-passage-without-corrupting-its-fixture)

- [ ] T005 [US1] Protect literal values during ordinary edits. `references/writing_style.md`. [W02 · W02.1, W02.2](./implementation-plan.md#w02--protect-literal-values-during-ordinary-edits) After W01.

## S14 · Use the discovery interview record at its handoff

**Demonstrate the story.** Recover a stakeholder decision and an unresolved question from the interview. [Story criteria](./implementation-plan.md#s14--use-the-discovery-interview-record-at-its-handoff)

- [ ] T006 [US14] Author the discovery interview record. `workflows/discover.md`. [W12 · W12.1, W12.2](./implementation-plan.md#w12--author-the-discovery-interview-record)

## S05 · Decide whether an opportunity warrants product definition

**Demonstrate the story.** Decide from the sourced brief whether the opportunity warrants product definition. [Story criteria](./implementation-plan.md#s05--decide-whether-an-opportunity-warrants-product-definition)

- [ ] T007 [US5] Author a brief from opportunity evidence. `references/product_requirements_document.md`. [W09 · W09.1, W09.2](./implementation-plan.md#w09--author-a-brief-from-opportunity-evidence) Use sourced intent. If intent is missing, use W12 first.

## S04 · Distinguish a prototype from approval to include it

**Demonstrate the story.** Have a reader recover the decision and distinguish prototype evidence from approval. [Story criteria](./implementation-plan.md#s04--distinguish-a-prototype-from-approval-to-include-it)

- [ ] T008 [US4] Write the approval opening from the detailed product evidence. `references/product_requirements_document.md`. [W07 · W07.1, W07.2](./implementation-plan.md#w07--write-the-approval-opening-from-the-detailed-product-evidence)
- [ ] T009 [US4] Judge the reader’s decision against the owning detail. `workflows/improve_references.md`. [W08 · W08.1, W08.2](./implementation-plan.md#w08--judge-the-readers-decision-against-the-owning-detail) After W07.

## S09 · Create a project’s first governed documents from facts

**Demonstrate the story.** Follow an authored product requirement into the downstream specification. [Story criteria](./implementation-plan.md#s09--create-a-projects-first-governed-documents-from-facts)

- [ ] T010 [US9] Author a complete product document from project facts. `SKILL.md`. [W18 · W18.1, W18.2](./implementation-plan.md#w18--author-a-complete-product-document-from-project-facts)
- [ ] T011 [US9] Hand an authored product requirement to the downstream specification. `references/spec_driven_development.md`. [W19 · W19.1, W19.2](./implementation-plan.md#w19--hand-an-authored-product-requirement-to-the-downstream-specification) After W18.

## S15 · Use the capability map at its handoff

**Demonstrate the story.** Identify independent capabilities and select the next one to specify. [Story criteria](./implementation-plan.md#s15--use-the-capability-map-at-its-handoff)

- [ ] T012 [US15] Map independent capabilities before specifying each one. `references/implementation_plan.md`. [W10 · W10.1, W10.2](./implementation-plan.md#w10--map-independent-capabilities-before-specifying-each-one) Requires an identified initiative from a brief or product definition.

## S16 · Use the research record at its handoff

**Demonstrate the story.** Trace the design choice to a source or an explicit research gap. [Story criteria](./implementation-plan.md#s16--use-the-research-record-at-its-handoff)

- [ ] T013 [US16] Author the research record that informs a design choice. `references/decision_record.md`. [W13 · W13.1, W13.2](./implementation-plan.md#w13--author-the-research-record-that-informs-a-design-choice)

## S17 · Use the feature map at its handoff

**Demonstrate the story.** Locate the named feature at its actual entry point. [Story criteria](./implementation-plan.md#s17--use-the-feature-map-at-its-handoff)

- [ ] T014 [US17] Author a feature map from verified surfaces. `references/test_specification.md`. [W05 · W05.1, W05.2](./implementation-plan.md#w05--author-a-feature-map-from-verified-surfaces)

## S18 · Use the critical journeys at its handoff

**Demonstrate the story.** Follow the mapped journey to its observable result. [Story criteria](./implementation-plan.md#s18--use-the-critical-journeys-at-its-handoff)

- [ ] T015 [US18] Author a critical journey that consumes the feature map. `references/product_requirements_document.md`. [W06 · W06.1, W06.2](./implementation-plan.md#w06--author-a-critical-journey-that-consumes-the-feature-map) Requires the W05 map or compatible existing evidence.

## S03 · Verify one critical journey against its source

**Demonstrate the story.** Follow the approved journey to a user-visible result and distinguish stale evidence. [Story criteria](./implementation-plan.md#s03--verify-one-critical-journey-against-its-source)

- [ ] T016 [US3] Preserve conditions and reopen stale evidence. `references/spec_driven_development.md`. [W21 · W21.1, W21.2](./implementation-plan.md#w21--preserve-conditions-and-reopen-stale-evidence) After W03, with a reachable journey such as W06.

## S19 · Use the requirements-quality checklist at its handoff

**Demonstrate the story.** Identify the requirement that needs clarification before work starts. [Story criteria](./implementation-plan.md#s19--use-the-requirements-quality-checklist-at-its-handoff)

- [ ] T017 [US19] Author a requirements-quality checklist for the implementer. `workflows/validation_review.md`. [W04 · W04.1, W04.2](./implementation-plan.md#w04--author-a-requirements-quality-checklist-for-the-implementer) After W03, with a drafted specification.

## S10 · Read a work item without guessing what success means

**Demonstrate the story.** Have a reader recover the visible outcome and permission from the revised work item. [Story criteria](./implementation-plan.md#s10--read-a-work-item-without-guessing-what-success-means)

- [ ] T018 [US10] Replace vague acceptance text with the visible result. `examples/issue.md`. [W22 · W22.1, W22.2](./implementation-plan.md#w22--replace-vague-acceptance-text-with-the-visible-result)
- [ ] T019 [US10] Review Markdown by what the reader can recover. `workflows/improve_references.md`. [W23 · W23.1, W23.2](./implementation-plan.md#w23--review-markdown-by-what-the-reader-can-recover) After W22.

## S11 · Follow a failed save from story to child Issue

**Demonstrate the story.** Follow the failed-save condition from the story to its child Issue. [Story criteria](./implementation-plan.md#s11--follow-a-failed-save-from-story-to-child-issue)

- [ ] T020 [US11] Publish a child Issue for the story’s failed save. `references/issue.md`. [W24 · W24.1, W24.2](./implementation-plan.md#w24--publish-a-child-issue-for-the-storys-failed-save) After W20.

## S06 · Carry discovery evidence into the next authoring decision

**Demonstrate the story.** Use the source to decide whether one missing answer changes the requirement. [Story criteria](./implementation-plan.md#s06--carry-discovery-evidence-into-the-next-authoring-decision)

- [ ] T021 [US6] Ask the question that changes the requirement. `workflows/discover.md`. [W28 · W28.1, W28.2](./implementation-plan.md#w28--ask-the-question-that-changes-the-requirement)

## S12 · Act on a handoff and resolve a misunderstood role

**Demonstrate the story.** Use the handoff to perform the necessary manual action and identify who answers the next question. [Story criteria](./implementation-plan.md#s12--act-on-a-handoff-and-resolve-a-misunderstood-role)

- [ ] T022 [US12] Guide the owner through one necessary manual action. `references/writing_style.md`. [W25 · W25.1, W25.2](./implementation-plan.md#w25--guide-the-owner-through-one-necessary-manual-action)
- [ ] T023 [US12] Clarify who acts when an explanation was misunderstood. `references/writing_style.md`. [W26 · W26.1, W26.2](./implementation-plan.md#w26--clarify-who-acts-when-an-explanation-was-misunderstood) After W25.

## S07 · Receive the right next action and a checked result

**Demonstrate the story.** Read the checked handoff and identify the result, blocker or decision. [Story criteria](./implementation-plan.md#s07--receive-the-right-next-action-and-a-checked-result)

- [ ] T024 [US7] Write progress, decision and blocker messages from evidence. `references/writing_style.md`. [W14 · W14.1, W14.2](./implementation-plan.md#w14--write-progress-decision-and-blocker-messages-from-evidence) Reuse W22 where available.
- [ ] T025 [US7] Deliver an optional reviewed decision with a verifiable receipt. `contracts/delivery_message.json`. [W15 · W15.1, W15.2](./implementation-plan.md#w15--deliver-an-optional-reviewed-decision-with-a-verifiable-receipt)

## S13 · Send a routine update with the appropriate checks

**Demonstrate the story.** Deliver a routine update with proof for the claims it makes. [Story criteria](./implementation-plan.md#s13--send-a-routine-update-with-the-appropriate-checks)

- [ ] T026 [US13] Limit routine-message checks to applicable claims. `SKILL.md`. [W27 · W27.1, W27.2](./implementation-plan.md#w27--limit-routine-message-checks-to-applicable-claims)

## S08 · Follow the portable entry without grader hints

**Demonstrate the story.** Reach the intended writing route from a normal request on the identified host. [Story criteria](./implementation-plan.md#s08--follow-the-portable-entry-without-grader-hints)

- [ ] T027 [US8] Put task routing before optional diagram detail. `SKILL.md`. [W16 · W16.1, W16.2](./implementation-plan.md#w16--put-task-routing-before-optional-diagram-detail)

## S21 · Route an improvement from its actual scope

**Demonstrate the story.** Select the smallest governed work record and follow the source of a design constraint. [Story criteria](./implementation-plan.md#s21--route-an-improvement-from-its-actual-scope)

- [ ] T028 [US21] Choose a task or story for an improvement. `workflows/discover.md`. [W30 · W30.1, W30.2](./implementation-plan.md#w30--choose-a-task-or-story-for-an-improvement) After W20.
- [ ] T029 [US21] Choose a feature, epic or delivery plan. `references/implementation_plan.md`. [W31 · W31.1, W31.2](./implementation-plan.md#w31--choose-a-feature-epic-or-delivery-plan) After W30.
- [ ] T030 [US21] Link a design to the records that govern it. `references/high_level_document.md`. [W62 · W62.1, W62.2](./implementation-plan.md#w62--link-a-design-to-the-records-that-govern-it) After W30.

## S22 · Write from incomplete project context

**Demonstrate the story.** Compare an undecided permission with the same permission already settled by a source. [Story criteria](./implementation-plan.md#s22--write-from-incomplete-project-context)

- [ ] T031 [US22] Detect an omitted material permission. `contracts/documents.json`. [W32 · W32.1, W32.2](./implementation-plan.md#w32--detect-an-omitted-material-permission)
- [ ] T032 [US22] Ask only the question that changes the requirement. `workflows/discover.md`. [W33 · W33.1, W33.2](./implementation-plan.md#w33--ask-only-the-question-that-changes-the-requirement) After W32.
- [ ] T033 [US22] Apply discovery checks at the right document scope. `contracts/documents.json`. [W34 · W34.1, W34.2](./implementation-plan.md#w34--apply-discovery-checks-at-the-right-document-scope) After W32 and W33.

## S20 · Choose the next document from the quick start

**Demonstrate the story.** Choose the next document using the public entry and the numbered sequence. [Story criteria](./implementation-plan.md#s20--choose-the-next-document-from-the-quick-start)

- [ ] T034 [US20] Explain spec-driven writing at the public entry. `examples/spec_driven_development.md`. [W42 · W42.1, W42.2](./implementation-plan.md#w42--explain-spec-driven-writing-at-the-public-entry)

## S39 · Find instructions for a feature or document type from the index

**Demonstrate the story.** Find each released capability and document type from the public index. [Story criteria](./implementation-plan.md#s39--find-instructions-for-a-feature-or-document-type-from-the-index)

- [ ] T035 [US39] Publish the public index with a usable focused-edit entry. `README.md`. [W54 · W54.1, W54.2](./implementation-plan.md#w54--publish-the-public-index-with-a-usable-focused-edit-entry)

## S20 · Choose the next document from the quick start (continued)

**Demonstrate the story.** Choose the next document using the public entry and the numbered sequence. [Story criteria](./implementation-plan.md#s20--choose-the-next-document-from-the-quick-start)

- [ ] T036 [US20] Publish the numbered document sequence in the `README.md` file. `README.md`. [W29 · W29.1, W29.2](./implementation-plan.md#w29--publish-the-numbered-document-sequence-in-the-readmemd-file) After W20, W30–W31 and the seven linked authoring routes (W04–W06, W09–W10, W12–W13).

## S23 · Write the intended artifact from a short request

**Demonstrate the story.** Use the supported shortcut to reach the right format and its checked output. [Story criteria](./implementation-plan.md#s23--write-the-intended-artifact-from-a-short-request)

- [ ] T037 [US23] Launch three document types in Claude Code. `scripts/install_skill.py`. [W35 · W35.1, W35.2](./implementation-plan.md#w35--launch-three-document-types-in-claude-code)
- [ ] T038 [US23] Launch the same documents in Codex. `scripts/install_skill.py`. [W36 · W36.1, W36.2](./implementation-plan.md#w36--launch-the-same-documents-in-codex) After W35.
- [ ] T039 [US23] Expose the authorable document catalog. `scripts/install_skill.py`. [W37 · W37.1, W37.2](./implementation-plan.md#w37--expose-the-authorable-document-catalog) After W35 and W36.
- [ ] T040 [US23] Write the feature task list and its linked Issues. `scripts/install_skill.py`. [W40 · W40.1, W40.2, W40.3](./implementation-plan.md#w40--write-the-feature-task-list-and-its-linked-issues) After W35, W11 and W20.
- [ ] T041 [US23] Route quality and consistency reviews. `scripts/install_skill.py`. [W41 · W41.1, W41.2](./implementation-plan.md#w41--route-quality-and-consistency-reviews) After W35, with the relevant review route.

## S24 · Choose and continue one eligible document

**Demonstrate the story.** Identify one useful next document and continue only when requested. [Story criteria](./implementation-plan.md#s24--choose-and-continue-one-eligible-document)

- [ ] T042 [US24] Show the next useful document. `SKILL.md`. [W38 · W38.1, W38.2](./implementation-plan.md#w38--show-the-next-useful-document) After W20 and W30–W31, with the approved production order.
- [ ] T043 [US24] Continue a checked document handoff. `SKILL.md`. [W39 · W39.1, W39.2](./implementation-plan.md#w39--continue-a-checked-document-handoff) After W38 and W15.

## S25 · Guide selection of a specification after delivery

**Demonstrate the story.** Identify which specification governs work after delivery. [Story criteria](./implementation-plan.md#s25--guide-selection-of-a-specification-after-delivery)

- [ ] T044 [US25] Guide selection of a specification after delivery. `references/spec_driven_development.md`. [W43 · W43.1, W43.2](./implementation-plan.md#w43--guide-selection-of-a-specification-after-delivery) Use W32–W34 when authority is ambiguous.

## S26 · Resolve constrained fields in Issue handoffs

**Demonstrate the story.** Recover field-specific constraints from the Issue the implementer receives. [Story criteria](./implementation-plan.md#s26--resolve-constrained-fields-in-issue-handoffs)

- [ ] T045 [US26] Resolve constrained fields in Issue handoffs. `references/issue.md`. [W44 · W44.1, W44.2](./implementation-plan.md#w44--resolve-constrained-fields-in-issue-handoffs) After W40 and W41.

## S27 · Document the owner and consumer version of a shared contract

**Demonstrate the story.** Locate the owner and version of a shared contract from the consumer. [Story criteria](./implementation-plan.md#s27--document-the-owner-and-consumer-version-of-a-shared-contract)

- [ ] T046 [US27] Document the owner and consumer version of a shared contract. `references/interface_contract.md`. [W45 · W45.1, W45.2](./implementation-plan.md#w45--document-the-owner-and-consumer-version-of-a-shared-contract)

## S28 · Release the Spec Writer identity and legacy entry

**Demonstrate the story.** Reach the renamed skill and resolve an existing installation. [Story criteria](./implementation-plan.md#s28--release-the-spec-writer-identity-and-legacy-entry)

- [ ] T047 [US28] Release the Spec Writer identity and legacy entry. `SKILL.md`. [W46 · W46.1, W46.2](./implementation-plan.md#w46--release-the-spec-writer-identity-and-legacy-entry) Requires accepted Skill Builder B5/T50 before changing the live identity.

## S29 · Start one feature through an optional workflow extension

**Demonstrate the story.** Select the intended feature in an initialized project. [Story criteria](./implementation-plan.md#s29--start-one-feature-through-an-optional-workflow-extension)

- [ ] T048 [US29] Start one feature through an optional workflow extension. `scripts/install_skill.py`. [W47 · W47.1, W47.2](./implementation-plan.md#w47--start-one-feature-through-an-optional-workflow-extension) After W46, with the checked specification route.

## S30 · Select eligible feature work and recover its Issue criteria

**Demonstrate the story.** Use the feature list to select ready work and recover the chosen Issue’s criterion. [Story criteria](./implementation-plan.md#s30--select-eligible-feature-work-and-recover-its-issue-criteria)

- [ ] T049 [US30] Select eligible tasks from the feature list. `references/issue.md`. [W48 · W48.1, W48.2, W48.3](./implementation-plan.md#w48--select-eligible-tasks-from-the-feature-list) After W47, W40 and W44.

## S31 · Verify and resume one authorized implementation

**Demonstrate the story.** Resume the same authorized task after interruption without replaying an uncertain effect. [Story criteria](./implementation-plan.md#s31--verify-and-resume-one-authorized-implementation)

- [ ] T050 [US31] Hand one approved task to the selected implementation provider. Upstream [`templates/commands/implement.md`](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/commands/implement.md). [W49 · W49.1, W49.2](./implementation-plan.md#w49--hand-one-approved-task-to-the-selected-implementation-provider) After W48, with authority for the selected provider.
- [ ] T051 [US31] Resume the same task after an interrupted run. Upstream [`docs/workflows/cli.md`](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/workflows/cli.md). [W50 · W50.1, W50.2](./implementation-plan.md#w50--resume-the-same-task-after-an-interrupted-run) After W49.

## S32 · Route an idea or bug to the right upstream workflow

**Demonstrate the story.** Finish an idea assessment at a decision and route a reported defect to a bounded repair. [Story criteria](./implementation-plan.md#s32--route-an-idea-or-bug-to-the-right-upstream-workflow)

- [ ] T052 [US32] End idea assessment at a supported decision. `references/decision_record.md`. [W51 · W51.1, W51.2](./implementation-plan.md#w51--end-idea-assessment-at-a-supported-decision) After the connected W47–W50 path, with brief and interview routes. Only W51.1 and W51.2 are approved.
- [ ] T053 [US32] Turn a reported defect into one bounded repair. `references/bug_report.md`. [W52 · W52.1, W52.2](./implementation-plan.md#w52--turn-a-reported-defect-into-one-bounded-repair) After the connected W47–W50 path and W30–W31.

## S37 · Write the requested document and pass it to the right consumer

**Demonstrate the story.** Request a supported format and follow its reviewed output into the task that needs it. [Story criteria](./implementation-plan.md#s37--write-the-requested-document-and-pass-it-to-the-right-consumer)

- [ ] T054 [US37] Request any supported writing format through the workflow. `contracts/documents.json`. [W58 · W58.1, W58.2](./implementation-plan.md#w58--request-any-supported-writing-format-through-the-workflow) After W47 and W35, with the approved document routes on the candidate.
- [ ] T055 [US37] Carry a reviewed document into a dependent task. `references/low_level_design.md`. [W59 · W59.1, W59.2](./implementation-plan.md#w59--carry-a-reviewed-document-into-a-dependent-task) After W58, W48 and W38–W39.

## S33 · Distribute and safely update the versioned integration

**Demonstrate the story.** Update and remove the installed integration while preserving project-authored work. [Story criteria](./implementation-plan.md#s33--distribute-and-safely-update-the-versioned-integration)

- [ ] T056 [US33] Distribute and safely update the versioned integration. `scripts/install_skill.py`. [W53 · W53.1, W53.2](./implementation-plan.md#w53--distribute-and-safely-update-the-versioned-integration) After W47–W50, W58–W59 and the entry points included in the release.

## S39 · Find instructions for a feature or document type from the index (continued)

**Demonstrate the story.** Find each released capability and document type from the public index. [Story criteria](./implementation-plan.md#s39--find-instructions-for-a-feature-or-document-type-from-the-index)

- [ ] T057 [US39] Complete index coverage for the existing release. `README.md`. [W61 · W61.1, W61.2](./implementation-plan.md#w61--complete-index-coverage-for-the-existing-release) After W54, on the identified release.

## S38 · Explain the feature and report the checked result

**Demonstrate the story.** Read the feature page and session handoff against the approved rule and open decision. [Story criteria](./implementation-plan.md#s38--explain-the-feature-and-report-the-checked-result)

- [x] T058 [US38] Teach feature-page and session wording in the live style guide. `references/writing_style.md`. [W60 · W60.1](./implementation-plan.md#w60--teach-feature-page-and-session-wording-in-the-live-style-guide) Reuse the accepted guide and example at `d8bf859`.

## S08 · Follow the portable entry without grader hints (continued)

**Demonstrate the story.** Reach the intended writing route from a normal request on the identified host. [Story criteria](./implementation-plan.md#s08--follow-the-portable-entry-without-grader-hints)

- [ ] T059 [US8] Ship neutral cross-host assignments for the connected handoff. `config/host_validation.json`. [W17 · W17.1, W17.2](./implementation-plan.md#w17--ship-neutral-cross-host-assignments-for-the-connected-handoff) At release, after W16 and the affected increments are integrated on the frozen candidate.

## Finish the delivery

Verify the affected story and feature outcomes on the identified candidate. W17 owns the cross-host demonstration. Preserve the accepted W60 proof and record any missing host observation separately. [Coverage and shared Definition of Done](./implementation-plan.md#requirement-coverage)
