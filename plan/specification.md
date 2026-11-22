# Spec Writer improvement specification

Status: Approved behavioral scope, revision 20. Applies to Codex and Claude Code. [Audit](./audit.md)

Source: The owner’s approved scope and the [comparative audit](./audit.md).

## Purpose and scope

A person should be able to decide what they are approving, and an implementer should be able to recover the agreed behavior and its proof without the original conversation. This specification proposes changes to Technical Writer’s guidance, examples and affected checks. The target is the existing skill, released as Spec Writer after the compatibility migration. Technical Writer authors every requested specification-driven artifact in full, including the Product Requirements Document (PRD), behavioral specification, design, decisions, plans, stories, issues and verification documents. Mirai and other projects supply evidence and consume the results. Deployment, external tracker writes and publication require separate authority.

The owner approved the optional workflow integration and the skill name **Spec Writer** (`spec-writer`). Claude implements the live rename on the handoff computer. The existing GitHub repository and clone URL remain the integration target. Spec Writer remains usable without the optional workflow. Deliver the rename after Skill Builder B5/T50. W47 selects a feature, W48 lets the implementing agent select eligible work from the feature list and recover acceptance from each Issue, and W49–W50 prove execution and recovery on one authorized local feature. Establish that connection before adding W51–W52 and the versioned W53 distribution. Reuse host evidence where inputs match. Use the project-selected provider for execution. Keep remote publication outside implementation authority.

Use **Spec Writer** (`spec-writer`) as the sole product identity in the skill, repository documentation, installation text, examples, command descriptions and session replies. Describe the optional workflow by its function. Preserve exact technical identifiers needed to run it, source destinations for the audit and applicable copyright notices.

## Definitions

An **owning source** is the project-approved location and revision for a claim. A **consumer** is a particular document, person, or workflow that needs it. A **criterion** is a checkable statement of expected behavior under stated conditions. A **safeguard** is a necessary constraint on delivery, such as retaining a historical approval. A **handoff** makes the source, applicable criterion and intended use clear to the consumer.

## Scenarios

- A reviewer requests a small issue edit. The writer preserves fixture keys, leaves project terms intact and returns only the requested change.
- An owner is considering a feature with an unknown baseline. The writer distinguishes the observed problem from a proposed target, identifies any decision that changes scope, and prepares a brief or decision summary at the appropriate scale.
- A delivery team takes a governed feature into implementation. Given only the linked work item and its declared inputs, the implementer can identify permitted behavior, exclusions, blocking decisions and proof. When a reference has gone stale, the affected work stays open.
- A session resumes after context loss. The user can identify the last confirmed result, what remains unknown, and who can resolve it. A checked delivery preserves its binding to the reviewed bytes.

### F1 · Preserve the project’s literal identifiers

As a maintainer, I want a naming rule that protects consumed values, so that examples remain executable.

#### Acceptance criteria

- **F1.1** Given the mixed fixture and a real document reference, edit them and derive the domain from the result. The fixture and quote keep their bytes and the document name follows the adopted convention. Save the input, output and derived value. <a id="f1-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: maintainer. Child: [S01](#s01--edit-a-mixed-passage-without-corrupting-its-fixture). R1/A1. Covers the demonstrated fixture defect and the writing rule. [Audit finding F1](./audit.md#f1--high--a-documented-naming-convention-corrupted-a-test-fixture)

#### S01 · Edit a mixed passage without corrupting its fixture

As a writer, I want to distinguish a name from a literal, so that I can improve prose safely.

##### Acceptance criteria

- **S01.1** The consuming fixture produces the original domain after the edit. A genuine document label is still recognised. Reuse W01 and W02 evidence. <a id="s01-1"></a>

##### Scope and sources

Parent: [F1](#f1--preserve-the-projects-literal-identifiers). Owner role: writer. [W01](./tasks.md#w01--repair-the-websites-review-fixture-and-its-consumers) and [W02](./tasks.md#w02--protect-literal-values-during-ordinary-edits). D1 authorizes the first-use convention.

### F2 · Trace assigned work back to its real source

As a plan reviewer, I want to resolve requirements and parent links, so that unsupported work is found before implementation.

#### Acceptance criteria

- **F2.1** Follow a real requirement to its story, task and proof. Removing an owner, inventing an ID or filing a child without its parent produces a located gap. A justified safeguard and a genuine standalone fix remain eligible. <a id="f2-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: plan reviewer. Child: [S02](#s02--commission-a-task-from-a-reviewed-requirement). R2/R3/R10/R11; A2/A3/A10g/A11. Scope includes the review artifact that an implementer consumes. [Boundary enforcement, 06:10–06:53](https://www.youtube.com/watch?v=O_zcc6Xl12g&t=370s) [Audit finding F2](./audit.md#f2--high--a-valid-plan-can-name-a-nonexistent-requirement)

#### S02 · Commission a task from a reviewed requirement

As a plan author, I want to expose broken links before commissioning work, so that the implementer can recover authority from the packet.

##### Acceptance criteria

- **S02.1** Open the work packet without the original chat. Resolve the intended parent and revision, identify the review verdict, and detect an altered mapping. Retain the packet and located diagnostics. <a id="s02-1"></a>

##### Scope and sources

Parent: [F2](#f2--trace-assigned-work-back-to-its-real-source). Owner role: plan author. [W03](./tasks.md#w03--resolve-coverage-in-both-directions), [W20](./tasks.md#w20--resolve-feature-story-and-task-ancestry-before-drafting) and [W11](./tasks.md#w11--write-an-epic-whose-stories-prove-a-usable-outcome). Reuse the requirements-quality verdict from [F19](#f19--decide-whether-a-requirement-is-ready) when required.

### F3 · Prove behavior at the surface the user reaches

As a verifier, I want to connect a named feature to an observable outcome, so that a valid ID cannot hide weaker behavior.

#### Acceptance criteria

- **F3.1** Follow a named surface through a critical journey into a real criterion. The proof rejects a reachable but incorrect result and preserves uncertainty when the available record does not establish the result. <a id="f3-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: verifier. Child: [S03](#s03--verify-one-critical-journey-against-its-source). R3/R8/R10; A3/A8/A10e/A10f. [Feature mapping, 09:58–10:52](https://www.youtube.com/watch?v=PaPpyQocMww&t=598s) [Audit finding F3](./audit.md#f3--high--even-a-resolved-id-can-conceal-weaker-behavior)

#### S03 · Verify one critical journey against its source

As a test author, I want a feature map and linked journey with a falsifiable check, so that I can tell what actually happened.

##### Acceptance criteria

- **S03.1** Resolve every step to a surface, exercise the stated boundary in the written verification case and distinguish the expected observation from its closest false positive. Save the linked documents and judgments. <a id="s03-1"></a>

##### Scope and sources

Parent: [F3](#f3--prove-behavior-at-the-surface-the-user-reaches). Owner role: test author. [W21](./tasks.md#w21--preserve-conditions-and-reopen-stale-evidence) consumes the outputs of [F17](#f17--locate-the-feature-from-its-map) and [F18](#f18--follow-the-critical-journey-to-its-observable-result). The assignment authors documentation; application behavior needs its own execution evidence.

### F4 · Make the approval decision intelligible from its opening

As a product owner, I want a decision summary derived from the detailed evidence, so that I know what my approval would authorize.

#### Acceptance criteria

- **F4.1** Give an independent reader the opening alone. They identify beneficiary, change, exclusion and unresolved choice and can support each from the text. <a id="f4-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: product owner. Child: [S04](#s04--distinguish-a-prototype-from-approval-to-include-it). R4/A4. [Prototype and roadmap decision, 52:33–53:19](https://www.youtube.com/watch?v=y1-9yeYLJUo&t=3153s) [Audit finding F4](./audit.md#f4--medium--the-approval-reader-gets-less-help-than-the-implementing-reader)

#### S04 · Distinguish a prototype from approval to include it

As a decision owner, I want to read the proposed choice and its limits, so that I can decide without inferring approval from code.

##### Acceptance criteria

- **S04.1** The reader distinguishes what the prototype showed from the pending owner decision. A superficially supporting quote cannot justify the wrong answer. <a id="s04-1"></a>

##### Scope and sources

Parent: [F4](#f4--make-the-approval-decision-intelligible-from-its-opening). Owner role: decision owner. [W07](./tasks.md#w07--write-the-approval-opening-from-the-detailed-product-evidence) and [W08](./tasks.md#w08--judge-the-readers-decision-against-the-owning-detail). Use a sourced product example with one exclusion.

### F5 · Write a brief for a product decision

As a product lead, I want a brief grounded in the problem and available evidence, so that I can decide whether to pursue the opportunity.

#### Acceptance criteria

- **F5.1** From the supplied opportunity, read the brief and identify the affected person, desired outcome, exclusion and unknown baseline. An invented target fails A10b. <a id="f5-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: product lead. Child: [S05](#s05--decide-whether-an-opportunity-warrants-product-definition). R2/R10, A2/A10b. The complete seven-output acceptance remains a plan-level obligation. [Related reports, 43:45–44:29](https://www.youtube.com/watch?v=6hxp0SpGxz8&t=2625s) [Audit finding F5](./audit.md#f5--high--the-product-guide-mentions-a-brief-without-defining-its-complete-handoff)

#### S05 · Decide whether an opportunity warrants product definition

As a product planner, I want a short account of the beneficiary, outcome and known constraints, so that the owner can decide whether a fuller product definition is useful.

##### Acceptance criteria

- **S05.1** Read the authored brief without the original conversation. Recover the problem, proposed outcome and uncertainty from the words on the page. Compare with A10b. <a id="s05-1"></a>

##### Scope and sources

Parent: [F5](#f5--write-a-brief-for-a-product-decision). Owner role: product planner. [W09](./tasks.md#w09--author-a-brief-from-opportunity-evidence). Use an interview record from [F14](#f14--read-the-owners-interview-answers) when needed. A request with enough evidence can enter directly.

### F6 · Ground discovery and research in actual evidence

As a requirements owner, I want to distinguish sourced answers, hypotheses and delegated choices, so that the specification reflects what is known and what I still need to decide.

#### Acceptance criteria

- **F6.1** Given an ambiguous request, the first question identifies the consequential unknown. Given settled evidence, the writer proceeds. An answer changes the next requirement or proof only within the owner’s authority. <a id="f6-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: requirements owner. Child: [S06](#s06--carry-discovery-evidence-into-the-next-authoring-decision). R5/R10; A5/A10a/A10d. [Diagnosis without the governing source, 14:53–15:20](https://www.youtube.com/watch?v=vFYVF7IC8Zw&t=893s) [Audit finding F6](./audit.md#f6--medium--the-discovery-process-is-sound-but-its-best-lessons-are-difficult-to-imitate)

#### S06 · Carry discovery evidence into the next authoring decision

As a writer, I want a reviewable record of what was said and what was investigated, so that the brief and design can cite evidence separately.

##### Acceptance criteria

- **S06.1** Inspect the writer’s first question, the owner’s answer and the resulting criterion. The answer settles one branch. Supplied evidence can settle it without an interview. <a id="s06-1"></a>

##### Scope and sources

Parent: [F6](#f6--ground-discovery-and-research-in-actual-evidence). Owner role: writer. [W28](./tasks.md#w28--ask-the-question-that-changes-the-requirement). [F14](#f14--read-the-owners-interview-answers) owns the deliverable interview record and [F16](#f16--use-research-to-resolve-a-design-question) owns the research record.

### F7 · Speak plainly about results, blockers and decisions in the session

As a project owner, I want a clear update and a traceable final handoff, so that I know what changed and whether a decision needs me.

#### Acceptance criteria

- **F7.1** Observe a progress update, a real blocker, a decision request and a checked delivery. The delivery agrees with the accepted bytes; a modified decision sentence fails verification while an old receipt still verifies. <a id="f7-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: project owner. Child: [S07](#s07--receive-the-right-next-action-and-a-checked-result). R6/A6. Shared wording rules apply to both hosts. [Audit finding F7](./audit.md#f7--medium--session-messages-report-validation-more-reliably-than-the-users-result)

#### S07 · Receive the right next action and a checked result

As a reader, I want the fact or decision relevant to this moment, so that I can proceed without guessing.

##### Acceptance criteria

- **S07.1** Compare each public message to its observed state or reviewed content. Preserve the decision owner and the version-specific exact-message guarantee. <a id="s07-1"></a>

##### Scope and sources

Parent: [F7](#f7--speak-plainly-about-results-blockers-and-decisions-in-the-session). Owner role: reader. [W14](./tasks.md#w14--write-progress-decision-and-blocker-messages-from-evidence) and [W15](./tasks.md#w15--deliver-an-optional-reviewed-decision-with-a-verifiable-receipt). Manual instructions apply only when there is an action the user must perform.

### F8 · Reach the right guidance from an ordinary request

As a skill user, I want the same writing behavior on Codex and Claude Code, so that I can request a small edit or a connected specification without naming a reference file.

#### Acceptance criteria

- **F8.1** Use both normal hosts for one small edit and one connected assignment per host, or qualifying retained evidence. Preserve literal, governing meaning and requested scope. Keep document and routing verdicts distinct. <a id="f8-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: skill user. Child: [S08](#s08--follow-the-portable-entry-without-grader-hints). R7/A7. [Neutral evaluation, 19:13–20:15](https://www.youtube.com/watch?v=04FAVmmLSGc&t=1153s) [Audit finding F8](./audit.md#f8--medium--the-entry-point-spends-attention-on-the-catalog-before-the-task)

#### S08 · Follow the portable entry without grader hints

As a host evaluator, I want to observe which sources the task actually uses, so that I can distinguish compliance from prompted performance.

##### Acceptance criteria

- **S08.1** The inputs omit the expected guide and answers. Each host delivers assessable output on the identified candidate. Missing public routing evidence stays Not demonstrated. <a id="s08-1"></a>

##### Scope and sources

Parent: [F8](#f8--reach-the-right-guidance-from-an-ordinary-request). Owner role: host evaluator. [W16](./tasks.md#w16--put-task-routing-before-optional-diagram-detail) and [W17](./tasks.md#w17--ship-neutral-cross-host-assignments-for-the-connected-handoff). Package invocation, aliases, catalog consumers and relevant visual accessibility are compatibility obligations.

### F9 · Author complete documents independently of the application

As a project owner, I want Technical Writer to author every requested specification-driven file, so that my project supplies facts and retains decision authority without needing its own writer.

#### Acceptance criteria

- **F9.1** From a blank start, deliver a complete product document and linked behavioral specification for Mirai and a complete product document for a second project. Preserve sources, IDs and pending owner approval. Record any consumer incompatibility separately. <a id="f9-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: project owner. Child: [S09](#s09--create-a-projects-first-governed-documents-from-facts). R9/A9. The audit correction assigns document structure, prose and checked delivery to Technical Writer. [Audit finding F9](./audit.md#f9--high--the-proposed-integration-gave-document-authorship-to-the-wrong-component)

#### S09 · Create a project’s first governed documents from facts

As a product author, I want to start without an application template, so that I can deliver a versioned specification and hand it to a real consumer.

##### Acceptance criteria

- **S09.1** The writer uses its own form in both projects. Follow one downstream criterion back to a source decision; withheld approval remains open. No claim of live application ingestion follows from document delivery. <a id="s09-1"></a>

##### Scope and sources

Parent: [F9](#f9--author-complete-documents-independently-of-the-application). Owner role: product author. [W18](./tasks.md#w18--author-a-complete-product-document-from-project-facts) and [W19](./tasks.md#w19--hand-an-authored-product-requirement-to-the-downstream-specification). Covers project-independent authoring and compatibility at the consuming boundary.

### F10 · Write stories and tasks that a reader can act on

As a product owner, I want the text to tell me what a person will see and who can act, so that I can spot a wrong implementation without decoding abstract phrases.

#### Acceptance criteria

- **F10.1** Given the original partial-write wording and its governing source, an edited issue lets a reader explain the visible result, stop condition and retry authority. A fluent but weaker paraphrase fails. Preserve accurate story wording and compare the reader’s answer with A12. <a id="f10-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: writing-guidance maintainer. Child: [S10](#s10--read-a-work-item-without-guessing-what-success-means). R12/A12. The supported defect is one worked example that teaches a vague abstraction. Keep the existing clear examples and shared writing principles. [Audit finding F10](./audit.md#f10--medium--some-worked-acceptance-criteria-hide-what-the-user-should-see)

#### S10 · Read a work item without guessing what success means

As an implementer, I want a short story and task that preserve the governing rule in concrete language, so that I can build and verify the requested behavior.

##### Acceptance criteria

- **S10.1** W22 delivers the corrected issue and a before/after example. W23 delivers the corresponding review method. Give the reader the edited task without its answer key. They recover the actor, observable result, permission and failure condition from the text. A source-grounded alternative can pass. Retain the passage, reader response and contrary example. <a id="s10-1"></a>

##### Scope and sources

Parent: [F10](#f10--write-stories-and-tasks-that-a-reader-can-act-on). Owner role: issue-guidance maintainer. [W22](./tasks.md#w22--replace-vague-acceptance-text-with-the-visible-result) and [W23](./tasks.md#w23--review-markdown-by-what-the-reader-can-recover). Use [F7](#f7--speak-plainly-about-results-blockers-and-decisions-in-the-session)’s cases for public session messages. Assess prose against its actual audience and writing task.

### F11 · Show a complete child task for one story criterion

As a implementer, I want a child task I can use as a model, so that I can commission a bounded change.

#### Acceptance criteria

- **F11.1** Open the linked task from the worked story and recover one failed-save criterion, its governing source and proof. Assigning the whole Feature fails A13. <a id="f11-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: implementer. Child: [S11](#s11--follow-a-failed-save-from-story-to-child-issue). R13/A13. [Audit finding F11](./audit.md#f11--medium--the-worked-issue-demonstrates-a-parent-feature-when-a-child-task-is-requested)

#### S11 · Follow a failed save from story to child Issue

As a writer, I want a worked child example on the ordinary Issue route, so that I can distinguish its scope from the parent Feature.

##### Acceptance criteria

- **S11.1** Follow both links and inspect the child’s actual acceptance text against WEB-06. Retain the task and located comparison. <a id="s11-1"></a>

##### Scope and sources

Parent: [F11](#f11--show-a-complete-child-task-for-one-story-criterion). Owner role: writer. [W24](./tasks.md#w24--publish-a-child-issue-for-the-storys-failed-save). Use the evidence and boundaries in the linked finding.

### F12 · Make session explanations usable from the owner’s starting point

As a project owner, I want instructions and explanations grounded in my situation, so that I can act without guessing.

#### Acceptance criteria

- **F12.1** Given a necessary handoff and a misunderstood role, a reader can name the next action or decision from the replies alone. A guessed branch or invented assignment fails. <a id="f12-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: project owner. Child: [S12](#s12--act-on-a-handoff-and-resolve-a-misunderstood-role). R14/A14. [Audit finding F12](./audit.md#f12--medium--the-session-guidance-does-not-show-how-to-unblock-a-person-who-has-to-act)

#### S12 · Act on a handoff and resolve a misunderstood role

As a session user, I want a concrete starting point and clear responsibility, so that I can do the right thing.

##### Acceptance criteria

- **S12.1** Use W25’s read-only handoff and W26’s role clarification. Compare the owner’s action and role with the supplied facts. <a id="s12-1"></a>

##### Scope and sources

Parent: [F12](#f12--make-session-explanations-usable-from-the-owners-starting-point). Owner role: session user. [W25](./tasks.md#w25--guide-the-owner-through-one-necessary-manual-action), [W26](./tasks.md#w26--clarify-who-acts-when-an-explanation-was-misunderstood). Use the evidence and boundaries in the linked finding.

### F13 · Keep checks proportionate for routine updates

As a session user, I want timely factual progress, so that I can see what changed.

#### Acceptance criteria

- **F13.1** Inspect the ordinary progress trace and applicable naming control. Removing a required artifact or exact-delivery check fails. <a id="f13-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: session user. Child: [S13](#s13--send-a-routine-update-with-the-appropriate-checks). R15/A15. [Audit finding F13](./audit.md#f13--medium--the-entry-requires-a-file-check-even-for-routine-session-updates)

#### S13 · Send a routine update with the appropriate checks

As a writer, I want a clear condition for running a file check, so that I can preserve evidence where the checker applies.

##### Acceptance criteria

- **S13.1** Compare the written rule and actual ordinary update with the named violation. Reuse accepted receipt evidence for unchanged behavior. <a id="s13-1"></a>

##### Scope and sources

Parent: [F13](#f13--keep-checks-proportionate-for-routine-updates). Owner role: writer. [W27](./tasks.md#w27--limit-routine-message-checks-to-applicable-claims). Use the evidence and boundaries in the linked finding.

### F14 · Read the owner’s interview answers

As a product author, I want a usable discovery interview record, so that another writer can reuse the agreed scope.

#### Acceptance criteria

- **F14.1** Use the [S14.1 acceptance scenario](#s14-1) for the epic’s integrated check. <a id="f14-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: product author. Child: [S14](#s14--use-the-discovery-interview-record-at-its-handoff). R10/A10a. [Audit finding F14](./audit.md#f14--high--discovery-answers-lack-a-deliverable-interview-record)

#### S14 · Use the discovery interview record at its handoff

As a product author, I want the relevant facts with their source, so that another writer can reuse the agreed scope.

##### Acceptance criteria

- **S14.1** A question changes scope or intent. Capture question, answer, source, unresolved choice, restatement and actual confirmation status. Brief or product author can distinguish an owner answer from a suggestion. A silent owner leaves the restatement open. Retain the output, the governing source and the consumer’s located evidence on the candidate. <a id="s14-1"></a>

##### Scope and sources

Parent: [F14](#f14--read-the-owners-interview-answers). Owner role: product author. [W12](./tasks.md#w12--author-the-discovery-interview-record). Use the evidence and boundaries in the linked finding.

### F15 · Select the capability to specify next

As a specification author, I want a usable capability map, so that I can specify one independent capability.

#### Acceptance criteria

- **F15.1** Use the [S15.1 acceptance scenario](#s15-1) for the epic’s integrated check. <a id="f15-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: specification author. Child: [S15](#s15--use-the-capability-map-at-its-handoff). R10/A10c. [Audit finding F15](./audit.md#f15--high--capability-boundaries-lack-a-route-before-feature-specification)

#### S15 · Use the capability map at its handoff

As a specification author, I want the relevant facts with their source, so that I can specify one independent capability.

##### Acceptance criteria

- **S15.1** When an initiative has several independent outcomes, name stable capability IDs, responsibilities, actual dependencies and a justified build order. The spec author selects the intended capability. Independent capabilities can be parallel. A cycle is surfaced for resolution. Retain the output, the governing source and the consumer’s located evidence on the candidate. <a id="s15-1"></a>

##### Scope and sources

Parent: [F15](#f15--select-the-capability-to-specify-next). Owner role: specification author. [W10](./tasks.md#w10--map-independent-capabilities-before-specifying-each-one). Use the evidence and boundaries in the linked finding.

### F16 · Use research to resolve a design question

As a designer, I want a usable research record, so that I can distinguish evidence from a pending choice.

#### Acceptance criteria

- **F16.1** Use the [S16.1 acceptance scenario](#s16-1) for the epic’s integrated check. <a id="f16-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: designer. Child: [S16](#s16--use-the-research-record-at-its-handoff). R10/A10d. [Audit finding F16](./audit.md#f16--high--research-findings-lack-a-handoff-before-a-design-decision)

#### S16 · Use the research record at its handoff

As a designer, I want the relevant facts with their source, so that I can distinguish evidence from a pending choice.

##### Acceptance criteria

- **S16.1** When evidence is needed before design, identify the question, sources, findings, uncertainty, supported recommendation and actual decision status. Designer can cite the finding and identify who must decide. A study or working prototype cannot silently approve a choice. Retain the output, the governing source and the consumer’s located evidence on the candidate. <a id="s16-1"></a>

##### Scope and sources

Parent: [F16](#f16--use-research-to-resolve-a-design-question). Owner role: designer. [W13](./tasks.md#w13--author-the-research-record-that-informs-a-design-choice). Use the evidence and boundaries in the linked finding.

### F17 · Locate the feature from its map

As a verifier, I want a usable feature map, so that I can locate the feature a check must reach.

#### Acceptance criteria

- **F17.1** Use the [S17.1 acceptance scenario](#s17-1) for the epic’s integrated check. <a id="f17-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: verifier. Child: [S17](#s17--use-the-feature-map-at-its-handoff). R10/A10e. [Audit finding F17](./audit.md#f17--high--a-verifier-cannot-request-a-complete-map-of-reachable-features)

#### S17 · Use the feature map at its handoff

As a verifier, I want the relevant facts with their source, so that I can locate the feature a check must reach.

##### Acceptance criteria

- **S17.1** For an observed surface, record its user-facing name, entry or route, verifiable control/handle, source revision and observable end state. Mark proposed surfaces explicitly. Journey author or verifier can locate the surface. A guessed route/handle or app launch alone cannot establish that it was reached. Retain the output, the governing source and the consumer’s located evidence on the candidate. <a id="s17-1"></a>

##### Scope and sources

Parent: [F17](#f17--locate-the-feature-from-its-map). Owner role: verifier. [W05](./tasks.md#w05--author-a-feature-map-from-verified-surfaces). Use the evidence and boundaries in the linked finding.

### F18 · Follow the critical journey to its observable result

As a verification author, I want a usable set of critical journeys, so that I can check the user’s whole journey.

#### Acceptance criteria

- **F18.1** Use the [S18.1 acceptance scenario](#s18-1) for the epic’s integrated check. <a id="f18-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: verification author. Child: [S18](#s18--use-the-critical-journeys-at-its-handoff). R10/A10f. [Audit finding F18](./audit.md#f18--high--a-critical-journey-lacks-a-checked-handoff-to-its-verifier)

#### S18 · Use the critical journeys at its handoff

As a verification author, I want the relevant facts with their source, so that I can check the user’s whole journey.

##### Acceptance criteria

- **S18.1** Given a mapped surface and sourced risk, record a journey ID, actor, ordered steps, observable result, why failure matters, source and test reference or explicit gap. Verifier resolves each referenced surface and finds the named check. An unknown screen or unrun test cannot count as verified. Retain the output, the governing source and the consumer’s located evidence on the candidate. <a id="s18-1"></a>

##### Scope and sources

Parent: [F18](#f18--follow-the-critical-journey-to-its-observable-result). Owner role: verification author. [W06](./tasks.md#w06--author-a-critical-journey-that-consumes-the-feature-map). Use the evidence and boundaries in the linked finding.

### F19 · Decide whether a requirement is ready

As a implementer, I want a usable requirements-quality checklist, so that I can find ambiguous requirements before starting.

#### Acceptance criteria

- **F19.1** Use the [S19.1 acceptance scenario](#s19-1) for the epic’s integrated check. <a id="f19-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: implementer. Child: [S19](#s19--use-the-requirements-quality-checklist-at-its-handoff). R10/A10g. [Audit finding F19](./audit.md#f19--high--requirements-review-lacks-a-deliverable-checklist-with-located-verdicts)

#### S19 · Use the requirements-quality checklist at its handoff

As a implementer, I want the relevant facts with their source, so that I can find ambiguous requirements before starting.

##### Acceptance criteria

- **S19.1** After a candidate specification exists, identify the revision, criterion under review, quality question, located evidence, verdict and unresolved correction. Implementer sees whether scope, permission and observable proof are determinate. A checked box alone cannot establish implementation or test success. Retain the output, the governing source and the consumer’s located evidence on the candidate. <a id="s19-1"></a>

##### Scope and sources

Parent: [F19](#f19--decide-whether-a-requirement-is-ready). Owner role: implementer. [W04](./tasks.md#w04--author-a-requirements-quality-checklist-for-the-implementer). Use the evidence and boundaries in the linked finding.

### F20 · Explain the document sequence in the `README.md` file

As a contributor, I want the document sequence at the project entry, so that I can start with the right inputs.

#### Acceptance criteria

- **F20.1** Starting at the `README.md` file, route one product change and one standalone fix, identify the required parents and find the applicable guides. An unqualified mandatory chain or a dead route fails. <a id="f20-1"></a>
- **F20.2** From the public introduction, explain how a request becomes an observable acceptance check and choose the appropriate entry for one small change. Use the W42 reader answers and resolved examples. <a id="f20-2"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: contributor. Child: [S20](#s20--choose-the-next-document-from-the-quick-start). R16/A16. [Audit finding F20](./audit.md#f20--medium--the-readmemd-file-leaves-document-order-to-the-skill-internals)

#### S20 · Choose the next document from the quick start

As a first-time user, I want a numbered path with conditional branches, so that I know which input I need.

##### Acceptance criteria

- **S20.1** Use the `README.md` file alone for the routing decision. Follow the links to check destinations. A new reader can identify where proof is defined and where it is recorded. <a id="s20-1"></a>
- **S20.2** A reader starting above setup can recover one behavior, the source that defines it, a bounded task and its failure check. The public overview distinguishes a planned check from evidence that it passed. <a id="s20-2"></a>

##### Scope and sources

Parent: [F20](#f20--explain-the-document-sequence-in-the-readmemd-file). Owner role: first-time user. [W29](./tasks.md#w29--publish-the-numbered-document-sequence-in-the-readmemd-file) supports [S20.1](#s20-1); [W42](./tasks.md#w42--explain-spec-driven-writing-at-the-public-entry) supports [S20.2](#s20-2). Use the evidence and boundaries in the linked finding.

### F21 · Choose how much planning an improvement needs

As a delivery owner, I want the writer to identify the smallest record that preserves scope, authority and proof, so that a small improvement can ship directly and coordinated work has an accountable parent.

#### Acceptance criteria

- **F21.1** Given A17’s contrasting requests, a reader can choose an independent Issue, an independent or governed story, a grouping record or a delivery plan and identify the input that justified that choice. Preserve project-required parents and unresolved blockers. <a id="f21-1"></a>
- **F21.2** From A17b’s governed and independent design outputs, a developer can recover the source of the permission rule and the component boundary. A declared child with a missing governing criterion remains blocked. Reuse S21.2 evidence. <a id="f21-2"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: writing-guidance maintainer. Child: [S21](#s21--route-an-improvement-from-its-actual-scope). R17/A17 and A17b. [Audit finding F21](./audit.md#f21--medium--the-guides-explain-what-a-record-contains-better-than-when-to-add-a-parent)

#### S21 · Route an improvement from its actual scope

As a writer, I want to decide which record owns the outcome and which dependencies need coordination, so that readers can implement the work without guessing or inventing a parent.

##### Acceptance criteria

- **S21.1** Route the paired A17 requests through the ordinary writing entry. From the chosen record and its referenced input, recover why the work can stand alone or why it needs its particular parent or plan. Reuse W20 evidence for stale and missing declared parents. <a id="s21-1"></a>
- **S21.2** At the ordinary writing entry, carry the manager-only refund rule into a component design and its planned denial check. When a contract supplies the approved rule and boundary, the independent design can proceed without a separate High Level Document (HLD). Use W62’s paired outputs and reuse W20 for the unresolved child. <a id="s21-2"></a>

##### Scope and sources

Parent: [F21](#f21--choose-how-much-planning-an-improvement-needs). Owner role: workflow maintainer. [W30](./tasks.md#w30--choose-a-task-or-story-for-an-improvement) and [W31](./tasks.md#w31--choose-a-feature-epic-or-delivery-plan) support [S21.1](#s21-1). [W62](./tasks.md#w62--link-a-design-to-the-records-that-govern-it) supports [S21.2](#s21-2). [W29](./tasks.md#w29--publish-the-numbered-document-sequence-in-the-readmemd-file) links the rules from the public chronology. Apply explicit user or project tracking requirements first.

### F22 · Resolve material gaps without needless questions

As a document owner, I want the writer to ask only when my answer changes the work, so that the specification preserves my intent and I can trust its stated decisions.

#### Acceptance criteria

- **F22.1** From the supported writing entry, the two A18 requests preserve or clarify export ownership as their evidence permits. An invented decision or an unnecessary permission question fails. A draft can still expose an unresolved rule. <a id="f22-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: writing-workflow maintainer. Child: [S22](#s22--write-from-incomplete-project-context). R18/A18. [Audit finding F22](./audit.md#f22--high--a-valid-source-reference-can-conceal-an-invented-answer)

#### S22 · Write from incomplete project context

As a developer, I want the writer to use the project’s evidence and identify what only I can settle, so that I can act on the document without rechecking every assumption.

##### Acceptance criteria

- **S22.1** Inspect the two A18 documents, actual questions, sources, readiness outcomes and review verdicts on the same candidate. A decision is attributable to the source or the actual owner response. An unresolved topic stays provisional. The source-settled case incurs no interview. <a id="s22-1"></a>

##### Scope and sources

Parent: [F22](#f22--resolve-material-gaps-without-needless-questions). Owner role: discovery maintainer. [W32](./tasks.md#w32--detect-an-omitted-material-permission) establishes coverage on one route, [W33](./tasks.md#w33--ask-only-the-question-that-changes-the-requirement) connects the question and response, and [W34](./tasks.md#w34--apply-discovery-checks-at-the-right-document-scope) applies the contract across the catalog. Reuse [F6](#f6--ground-discovery-and-research-in-actual-evidence)’s discovery guidance, [W17](./tasks.md#w17--ship-neutral-cross-host-assignments-for-the-connected-handoff)’s host handoff and the private JSON execution records.

### F23 · Start documents from native shortcuts

As a developer, I want to give the document name and brief in one message, so that I can obtain the same checked document as through the normal route.

#### Acceptance criteria

- **F23.1** Use the [S23.1 acceptance scenario](#s23-1) for the epic’s integrated check. For a multi-task feature, use W40’s linked Issues and refund list to recover the first usable story and safe task order. <a id="f23-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: writing-workflow maintainer. Child: [S23](#s23--write-the-intended-artifact-from-a-short-request). R19/A19. [Audit finding F23](./audit.md#f23--medium--start-documents-from-native-shortcuts)

#### S23 · Write the intended artifact from a short request

As a developer, I want to give the document name and brief in one message, so that I can obtain the same checked document as through the normal route.

##### Acceptance criteria

- **S23.1** Observe real host dispatch with the supplied brief and the intended checked document; verify an occupied name keeps its existing handler and the qualified entry remains usable. Retain the identified candidate, actual request, output and consumer observation. For the refund breakdown, reuse W40.3 to show the first independent story and its task dependencies. <a id="s23-1"></a>

##### Scope and sources

Parent: [F23](#f23--start-documents-from-native-shortcuts). Owner role: writing-workflow maintainer. [W35](./tasks.md#w35--launch-three-document-types-in-claude-code)–[W37](./tasks.md#w37--expose-the-authorable-document-catalog) and [W40](./tasks.md#w40--write-the-feature-task-list-and-its-linked-issues)–[W41](./tasks.md#w41--route-quality-and-consistency-reviews). Use the scope boundaries in A19 and the shared Definition of Done.

### F24 · Guide the next document from project evidence

As a project owner, I want a short recommendation grounded in the initiative, so that I can decide what to write next or stop.

#### Acceptance criteria

- **F24.1** Use the [S24.1 acceptance scenario](#s24-1) for the epic’s integrated check. <a id="f24-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: writing-workflow maintainer. Child: [S24](#s24--choose-and-continue-one-eligible-document). R20/A20. [Audit finding F24](./audit.md#f24--medium--guide-the-next-document-from-project-evidence)

#### S24 · Choose and continue one eligible document

As a project owner, I want a short recommendation grounded in the initiative, so that I can decide what to write next or stop.

##### Acceptance criteria

- **S24.1** For one feature, a blocked decision and a standalone fix, distinguish the eligible document, missing prerequisite and completed scope. Continuing creates one attributable successor and resumption reuses existing work. Retain the identified candidate, actual request, output and consumer observation. <a id="s24-1"></a>

##### Scope and sources

Parent: [F24](#f24--guide-the-next-document-from-project-evidence). Owner role: writing-workflow maintainer. [W38](./tasks.md#w38--show-the-next-useful-document) and [W39](./tasks.md#w39--continue-a-checked-document-handoff). Use the scope boundaries in A20 and the shared Definition of Done.

### F25 · Find the governing specification after delivery

As a maintainer returning to a delivered feature, I want to find which agreement governs the next change, so that an old delivery snapshot cannot silently reinstate retired behavior.

#### Acceptance criteria

- **F25.1** Use the [S25.1 acceptance scenario](#s25-1) for the epic’s integrated check. Capture the two draft excerpts or the focused question, source revisions and before/after identities of the inputs. Reuse existing discovery and rewrite evidence for unchanged behavior. <a id="f25-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: documentation maintainer. Child: [S25](#s25--guide-selection-of-a-specification-after-delivery). R21/A21. [Technical Writer baseline](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/spec_driven_development.md#L13-L16) · [comparison source](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/how-to/persisting-specs.md#two-separate-questions)

#### S25 · Guide selection of a specification after delivery

As a maintainer returning to a delivered feature, I want to find which agreement governs the next change, so that an old delivery snapshot cannot silently reinstate retired behavior.

##### Acceptance criteria

- **S25.1** At the normal edit entry, supply a frozen launch specification allowing seven days and an approved maintained policy allowing thirty days. Ask to update the feature. The draft cites the maintained rule and labels the seven-day value historical. Both source files remain intact. Remove the maintenance decision while keeping two plausible values. The writer identifies the conflict and asks which governs before committing to a value. It can draft unrelated sections. Use the same outputs for story and epic closure. <a id="s25-1"></a>

##### Scope and sources

Parent: [F25](#f25--find-the-governing-specification-after-delivery). Responsible role: skill maintainer. [W43](./tasks.md#w43--guide-selection-of-a-specification-after-delivery) supports [S25.1](#s25-1). Limit the change to the named writing route and the affected review.

### F26 · Carry exact field constraints into the implementing Issue

As an implementer reading an Issue, I want to trace a field constraint to its precise definition, so that two similar names cannot lead me to implement the wrong rule.

#### Acceptance criteria

- **F26.1** Use the [S26.1 acceptance scenario](#s26-1) for the epic’s integrated check. Retain the authored Issue, read-only review excerpt and the unchanged source definitions. Use this same pair at W40/W41 if available. <a id="f26-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: documentation maintainer. Child: [S26](#s26--resolve-constrained-fields-in-issue-handoffs). R22/A22. [Technical Writer baseline](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/issue.md#L13-L18) · [comparison source](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/commands/tasks.md#task-organization)

#### S26 · Resolve constrained fields in Issue handoffs

As an implementer reading an Issue, I want to trace a field constraint to its precise definition, so that two similar names cannot lead me to implement the wrong rule.

##### Acceptance criteria

- **S26.1** From a contract where Order.code is optional and Return.code is required, request the task for Return.code. The Issue points to the exact Return.code definition and preserves the required behavior. An unambiguous existing field pointer is sufficient. Review a variant citing Order.code for the return requirement. The review identifies the Issue, wrong field and missing coverage. An unrelated prose-only Issue requires no field citations. Use the same outputs for story and epic closure. <a id="s26-1"></a>

##### Scope and sources

Parent: [F26](#f26--carry-exact-field-constraints-into-the-implementing-issue). Responsible role: skill maintainer. [W44](./tasks.md#w44--resolve-constrained-fields-in-issue-handoffs) supports [S26.1](#s26-1). Limit the change to the named writing route and the affected review.

### F27 · Resolve the contract shared by separate repositories

As a developer integrating a consumer with a provider, I want to identify the governing contract and supported version, so that a local edit cannot silently change the release agreement.

#### Acceptance criteria

- **F27.1** Use the [S27.1 acceptance scenario](#s27-1) for the epic’s integrated check. Keep the cited owner revision, consumer pin and resulting compatibility passage; inspect the copy identity. No service deployment or provider test is needed to assess this writing change. <a id="f27-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: documentation maintainer. Child: [S27](#s27--document-the-owner-and-consumer-version-of-a-shared-contract). R23/A23. [Technical Writer baseline](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/references/interface_contract.md#L3-L17) · [comparison source](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/how-to/contract-driven-development.md#one-authoritative-owner)

#### S27 · Document the owner and consumer version of a shared contract

As a developer integrating a consumer with a provider, I want to identify the governing contract and supported version, so that a local edit cannot silently change the release agreement.

##### Acceptance criteria

- **S27.1** Given an owner contract at v1, a divergent consumer copy and a proposed v2, ask for an Interface Contract update. It identifies the source revision, pins the consumer to v1, names the discrepancy and directs the proposed change to the owner. The consumer copy is untouched. Provide only the v1 pin and mock results, with no deployed-provider evidence. The handoff distinguishes the agreed version from unknown runtime support. One shared file used by both components requires no synchronized copy. Use the same outputs for story and epic closure. <a id="s27-1"></a>

##### Scope and sources

Parent: [F27](#f27--resolve-the-contract-shared-by-separate-repositories). Responsible role: skill maintainer. [W45](./tasks.md#w45--document-the-owner-and-consumer-version-of-a-shared-contract) supports [S27.1](#s27-1). Limit the change to the named writing route and the affected review.

### F28 · Keep existing users working through the Spec Writer rename

As a developer, I want to invoke Spec Writer from a new or existing installation, so that my writing workflow survives the rename.

#### Acceptance criteria

- **F28.1** Use the [S28.1 acceptance scenario](#s28-1) for the epic’s integrated check. Use the integrated readback at S28.1. <a id="f28-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: skill maintainer. Child: [S28](#s28--release-the-spec-writer-identity-and-legacy-entry). R24/A24. [Evidence](https://github.com/fatonsopa/ai-technical-writer/blob/4a8e7c92e20404f05e68708c1a3ea26c6961b178/scripts/install_skill.py)

#### S28 · Release the Spec Writer identity and legacy entry

As a developer, I want to invoke Spec Writer from a new or existing installation, so that my writing workflow survives the rename.

##### Acceptance criteria

- **S28.1** Fresh and existing users reach the same checked writer through their supported host. A pre-existing unrelated skill remains untouched. The accepted Builder validates a real document using the renamed release. Preserve observed failures and identify the candidate for each verdict. <a id="s28-1"></a>

##### Scope and sources

Parent: [F28](#f28--keep-existing-users-working-through-the-spec-writer-rename). Owner role: skill maintainer. [W46](./tasks.md#w46--release-the-spec-writer-identity-and-legacy-entry) support [S28.1](#s28-1). Use task evidence for the story when it proves the integrated outcome.

### F29 · Start a checked feature in an initialized workflow project

As a developer adopting the toolkit, I want the writing command to use the intended project and feature, so that it records my change under the right rules.

#### Acceptance criteria

- **F29.1** Use the [S29.1 acceptance scenario](#s29-1) for the epic’s integrated check. Use the integrated readback at S29.1. <a id="f29-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: skill maintainer. Child: [S29](#s29--start-one-feature-through-an-optional-workflow-extension). R25/A25. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/extensions/developing.md)

#### S29 · Start one feature through an optional workflow extension

As a developer adopting the toolkit, I want the writing command to use the intended project and feature, so that it records my change under the right rules.

##### Acceptance criteria

- **S29.1** From an existing project, the installed command produces a checked spec for the selected feature on each supported host. Repeat setup preserves the edited project document. The standalone writer remains usable. Preserve observed failures and identify the candidate for each verdict. <a id="s29-1"></a>

##### Scope and sources

Parent: [F29](#f29--start-a-checked-feature-in-an-initialized-workflow-project). Owner role: skill maintainer. [W47](./tasks.md#w47--start-one-feature-through-an-optional-workflow-extension) support [S29.1](#s29-1). Use task evidence for the story when it proves the integrated outcome.

### F30 · Give the implementing agent the complete task contract

As an implementer, I want the active feature’s task entry to carry the original criterion, so that I can implement it without the authoring conversation.

#### Acceptance criteria

- **F30.1** Use the [S30.1 acceptance scenario](#s30-1) for the epic’s integrated check. Use the integrated readback at S30.1. Use W48.3 to show the actual consumer selects eligible work and observes the API dependency before offering the dashboard filter. <a id="f30-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: skill maintainer. Child: [S30](#s30--select-eligible-feature-work-and-recover-its-issue-criteria). R26/A26. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/commands/implement.md#L143-L153)

#### S30 · Select eligible feature work and recover its Issue criteria

As an implementer, I want the active feature’s task entry to carry the original criterion, so that I can implement it without the authoring conversation.

##### Acceptance criteria

- **S30.1** With two features using the same short upstream task number, the actual selected consumer reads the refund Issue, its authorized actor and denial criterion. A stale view stops the affected dispatch. Preserve observed failures and identify the candidate for each verdict. For the two-story refund list, recover both parallel status tasks, the first usable story, and the condition that releases the dependent filter. Reuse W48.3. <a id="s30-1"></a>

##### Scope and sources

Parent: [F30](#f30--give-the-implementing-agent-the-complete-task-contract). Owner role: skill maintainer. [W48](./tasks.md#w48--select-eligible-tasks-from-the-feature-list) support [S30.1](#s30-1). Use task evidence for the story when it proves the integrated outcome.

### F31 · Verify and resume one authorized implementation

As a developer, I want to hand one approved Issue to a coding agent and resume its verification, so that the verdict refers to the original task and the candidate actually run.

#### Acceptance criteria

- **F31.1** Use the [S31.1 acceptance scenario](#s31-1) for the epic’s integrated check. Use the integrated readback at S31.1. <a id="f31-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: skill maintainer. Child: [S31](#s31--verify-and-resume-one-authorized-implementation). R27/A27. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/workflows/overview.md#run-review-and-resume)

#### S31 · Verify and resume one authorized implementation

As a developer, I want to hand one approved Issue to a coding agent and resume its verification, so that the verdict refers to the original task and the candidate actually run.

##### Acceptance criteria

- **S31.1** Follow one refund task from dispatch to an observed permission failure, correction and evidence-backed verdict. Resume at the same task and candidate boundary after interruption; uncertain effects cannot be replayed on guesswork. Preserve observed failures and identify the candidate for each verdict. <a id="s31-1"></a>

##### Scope and sources

Parent: [F31](#f31--verify-and-resume-one-authorized-implementation). Owner role: skill maintainer. [W49](./tasks.md#w49--hand-one-approved-task-to-the-selected-implementation-provider), [W50](./tasks.md#w50--resume-the-same-task-after-an-interrupted-run) support [S31.1](#s31-1). Use task evidence for the story when it proves the integrated outcome.

### F32 · Route an idea or bug to the right upstream workflow

As a project contributor, I want to enter with an uncertain idea or an observed defect, so that I receive the decision or repair record my situation needs.

#### Acceptance criteria

- **F32.1** Use the [S32.1 acceptance scenario](#s32-1) for the epic’s integrated check. Use the integrated readback at S32.1. <a id="f32-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: skill maintainer. Child: [S32](#s32--route-an-idea-or-bug-to-the-right-upstream-workflow). R28/A28. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/guides/assessment.md)

#### S32 · Route an idea or bug to the right upstream workflow

As a project contributor, I want to enter with an uncertain idea or an observed defect, so that I receive the decision or repair record my situation needs.

##### Acceptance criteria

- **S32.1** An idea lacking decision evidence ends with a supported question or stop recommendation; a bounded defect reaches a scoped repair and expected check. Neither input silently starts coding. Preserve observed failures and identify the candidate for each verdict. <a id="s32-1"></a>

##### Scope and sources

Parent: [F32](#f32--route-an-idea-or-bug-to-the-right-upstream-workflow). Owner role: skill maintainer. [W51](./tasks.md#w51--end-idea-assessment-at-a-supported-decision), [W52](./tasks.md#w52--turn-a-reported-defect-into-one-bounded-repair) support [S32.1](#s32-1). Use task evidence for the story when it proves the integrated outcome.

### F33 · Maintain a versioned workflow integration

As a maintainer, I want to install, inspect, upgrade and remove the integration, so that I can adopt it without losing project documents.

#### Acceptance criteria

- **F33.1** Use the [S33.1 acceptance scenario](#s33-1) for the epic’s integrated check. Use the integrated readback at S33.1. <a id="f33-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: skill maintainer. Child: [S33](#s33--distribute-and-safely-update-the-versioned-integration). R29/A29. [Evidence](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/docs/bundles/overview.md)

#### S33 · Distribute and safely update the versioned integration

As a maintainer, I want to install, inspect, upgrade and remove the integration, so that I can adopt it without losing project documents.

##### Acceptance criteria

- **S33.1** Using a versioned local release and a declared upstream version, inspect the effective command, upgrade the managed integration, then remove it. Project-authored documents and other installed commands survive. Preserve observed failures and identify the candidate for each verdict. <a id="s33-1"></a>

##### Scope and sources

Parent: [F33](#f33--maintain-a-versioned-workflow-integration). Owner role: skill maintainer. [W53](./tasks.md#w53--distribute-and-safely-update-the-versioned-integration) support [S33.1](#s33-1). Use task evidence for the story when it proves the integrated outcome.

### F37 · Use the full writing catalog in the optional workflow

As a project maintainer, I want the workflow to use the same document types as the standalone writer, so that a team can adopt it without giving up the documents it relies on.

#### Acceptance criteria

- **F37.1** Given the candidate catalog and an authorized feature with a reviewed design, a user can request a catalog document through the optional entry and a later task can recover the relevant design constraint. A document-only request ends at delivery. Retain the catalog comparison and the observations from S37.1 on the same release. <a id="f37-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: skill maintainer. Child: [S37](#s37--write-the-requested-document-and-pass-it-to-the-right-consumer). R33/A33. Apply the existing writing rules, source requirements, host authority and shared Definition of Done. The borrowed workflow definition continues to own its execution steps.

#### S37 · Write the requested document and pass it to the right consumer

As a developer, I want to request a specific document and have later work use its reviewed version, so that I can move from writing into development when my project needs it.

##### Acceptance criteria

- **S37.1** From the supported workflow entry, request a tutorial and observe its checked delivery without provider dispatch. For an authorized feature, pass a reviewed low-level design to a child task and observe its exact source and boundary in the task. A stale reference blocks dependent dispatch. Retain the W58 and W59 outputs and verdicts on the candidate. Reuse the same observations for F37.1. <a id="s37-1"></a>

##### Scope and sources

Parent: [F37](#f37--use-the-full-writing-catalog-in-the-optional-workflow). Owner role: skill maintainer. [W58](./tasks.md#w58--request-any-supported-writing-format-through-the-workflow) covers document selection and the stopping point. [W59](./tasks.md#w59--carry-a-reviewed-document-into-a-dependent-task) covers the consuming task and stale-input boundary. R33/A33 owns both. Use [W47](./tasks.md#w47--start-one-feature-through-an-optional-workflow-extension)’s settled project selection and the existing conditional hierarchy.

### F38 · Write feature guidance and session replies around the reader’s decision

As a reader, I want guidance and session replies to tell me what I can do and what happened, so that I can act without guessing.

#### Acceptance criteria

- **F38.1** Given the reviewed guide and refund example, a reader can identify where to act, the actor allowed to approve and the open retry decision. A completed document cannot establish that a refund ran. Reuse S38.1. <a id="f38-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Child: [S38](#s38--explain-the-feature-and-report-the-checked-result). R34/A34. Owner role: writing maintainer. Covers the shared guide; live host performance remains under the existing host tasks.

#### S38 · Explain the feature and report the checked result

As a writer, I want the procedure and the session reply to use the same facts, so that the reader can follow the procedure and the owner can see which decision is still open.

##### Acceptance criteria

- **S38.1** Apply the guide to the sourced refund example. Recover the reviewed rule and open question from the reply, and the source and next action from the example procedure. Reject an invented runtime outcome. Reuse W60.1. <a id="s38-1"></a>

##### Scope and sources

Parent: [F38](#f38--write-feature-guidance-and-session-replies-around-the-readers-decision). [W60](./tasks.md#w60--teach-feature-page-and-session-wording-in-the-live-style-guide) supports [S38.1](#s38-1). Owner role: writing maintainer.

### F39 · Make every released feature and supported document type findable

As a developer, I want to find the instructions for a feature or document type from the public index, so that I know when to use it, what to supply and what to expect.

#### Acceptance criteria

- **F39.1** Given the candidate’s public capabilities and supported document catalog, follow their index entries from the repository README. Each resolves to usable instructions on a page or at a named section. Aliases and variants may share a destination that covers them. An omitted entry, irrelevant destination or unshipped feature presented as ready fails. Save the candidate revision, coverage comparison and representative destinations. <a id="f39-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Child: [S39](#s39--find-instructions-for-a-feature-or-document-type-from-the-index). R35/A35. Owner role: documentation maintainer. Covers existing and newly released features and supported document types.

#### S39 · Find instructions for a feature or document type from the index

As a new user, I want the index to take me to the instructions for my request, so that I can start the right task.

##### Acceptance criteria

- **S39.1** From the same index, open the focused-edit and document-review entries. The first explains how to change only the selected text. The second explains how to obtain located findings. Both may resolve to sections in the same file. Use one supported Issue variant to show that a shared section can explain its specific inputs. Reuse the release comparison and observations from W54 and W61. <a id="s39-1"></a>

##### Scope and sources

Parent: [F39](#f39--make-every-released-feature-and-supported-document-type-findable). [W54](./tasks.md#w54--publish-the-public-index-with-a-usable-focused-edit-entry) owns the first usable route. [W61](./tasks.md#w61--complete-index-coverage-for-the-existing-release) owns existing release coverage. The task that delivers a new feature or document type owns its guidance and index link. Owner role: documentation maintainer.

## Requirements and business rules

| ID | Required behavior |
| --- | --- |
| R1 | Preserve meaning, obligation strength, exact literals and project vocabulary on every writing surface. Accept the full document name or its acronym in any user request, including the first mention. In authored prose introduce the full name and acronym once, then use the acronym where clear. Preserve project-required labels. |
| R2 | Choose the smallest document or native record suited to the decision. Support a shaping brief and an epic view as variants. Assign one owner to each requirement even when the project assigns that role to a differently named document. |
| R3 | For material multi-document work, identify the owning source, stable criterion or exact section, consuming work and expected proof. Bind the source revision when approval, compatibility, verification or project governance depends on it. Identify uncovered requirements, unjustified work, unresolved citations and altered conditions. Record only genuine dependencies. |
| R4 | Derive an approval opening from the detailed evidence. It must communicate who is affected, what changes, what is excluded and the actual choice or absence of an outstanding choice. Include material cost, uncertainty or risks when sourced. |
| R5 | Inspect available facts before asking. Ask about decisions that change the outcome, group only independent choices, and preserve unresolved authority. Stop when the available input settles the writing task. |
| R6 | Tailor the session response to progress, a decision, a blocker, or delivery. Every material claim in a checked delivery must be attributable to the exact reviewed content or an observed check. |
| R7 | Expose one portable writing contract. Route optional references by reader need and preserve existing supported invocation names and aliases. Demonstrate the changed behavior on both declared hosts before claiming it works on both. |
| R8 | Distinguish implementation, verification and acceptance. Preserve previous evidence, failures and approvals when a source or candidate changes. Mark each affected criterion Met, Failed or Not demonstrated against its actual candidate. |
| R9 | Technical Writer authors each requested specification-driven file from its own reference and output contract on any project. Projects supply facts, governing sources, permissions, IDs and decisions. The writer can start from a blank document. Existing documents may supply evidence or be edited when requested. Preserve authority and historical approvals. A consumer-format conflict must be identified explicitly. |
| R10 | Author all seven named artifacts through the normal skill entry on explicit request. Support a complete standalone deliverable when requested and a linked section when sufficient. Each route includes accepted inputs, writing guidance, consumer, representative example and a compatible checked-output path. Use an existing type only when its full contract fits; a named variant may carry distinct structure. Technical Writer owns those forms. |
| R11 | Resolve a child story to its governing feature or epic, and a child task to its story and criterion before drafting it as ready for implementation. An independent issue, including a bounded improvement, may carry its source, scope, observable outcome and proof inline. Never reclassify an orphaned child as standalone to bypass the missing parent. |
| R12 | Use reader-appropriate plain language across Markdown and session messages. Name the actor, action and observable consequence where they affect the reader’s decision. Preserve sourced meaning, uncertainty, obligation strength, exact identifiers, numbers and authority. Keep clear prose as written. Match the vocabulary to the owner, implementer or reviewer using the artifact. |
| R13 | Give writers a complete child Issue that can be reached from its story and the Issue guide. Preserve the distinct parent Feature example. |
| R14 | Put portable session instructions for necessary manual actions and misunderstood explanations in one named section of Writing Style (WS). Link the existing procedure guidance and preserve the checked-delivery boundary. |
| R15 | Require the file-based wording check where its predicates or an existing artifact obligation apply. Every message still receives source-grounded editorial review. |
| R16 | Introduce spec-driven technical writing in the public README before setup. Connect one user request to the agreed behavior, bounded work and planned proof. Help readers choose their entry by need. Publish the numbered production order in the Technical Writer `README.md` file. Explain prerequisites, conditional artifacts, supported entry points, the child-parent rule and the independent-issue exception. Link the owning references. |
| R17 | Choose the smallest sufficient work record using the project’s real governance, the user-visible outcome, the ownership of scope and the need to coordinate delivery. Make a child link mandatory when its authority comes from a parent. Allow an independent improvement or story to proceed from its own authority. State the reason for grouping or planning in the existing record when material. For designs, contracts, plans and tests, link the governing source that the reader needs. A design reference alone establishes no work-item parent. |
| R18 | Use the document type and requested scope to identify material information needed at the checked writing entry. Resolve each applicable topic from evidence or actual authority, or keep it visibly open. Before asking, identify the affected requirement or section, source inspected and the consequence of an answer. Preserve the lightweight route for narrow edits. |
| R19 | Provide opt-in native document shortcuts and route writing and review actions through existing Technical Writer references and contracts. One catalog owns the mapping. Preserve the original brief, explicit operation, other installed commands and qualified fallback. For a multi-task feature, write one story-grouped `tasks.md` and link its rows to the Issues that own acceptance. The spec owns story outcomes and acceptance or resolves their existing owner. The implementation plan references the stories and owns the delivery approach. Each task has one owning record for its scope, criterion and proof. |
| R20 | Offer guided entry, read-only next-document advice and one-document continuation using actual prerequisites and revisions. In one line name the next document, the specific gap and its benefit, or the real blocker or completed endpoint. |
| R21 | For a change to a delivered feature, identify the active source under the project’s maintenance policy and distinguish historic delivery evidence. Resolve a material authority conflict before settling the affected requirement. |
| R22 | For a task that implements a constrained field, bind the exact field to its authoritative definition. Check the resulting Issue for missing or misattributed constraints in scope. |
| R23 | For independently released providers and consumers, distinguish the authoritative contract revision, the consumer’s supported or pinned version, and the evidence for actual runtime compatibility. |
| R24 | Ship Spec Writer with one writing implementation and a compatible legacy entry, after Skill Builder accepts both identities. |
| R25 | Provide an optional namespaced integration that reaches the same checked authoring route on both hosts. |
| R26 | Present the active feature’s `tasks.md` to the implementing agent at its supported entry. Bind each selected row to its Issue, applicable criterion and source revision within that feature. Honor story phases, parallel eligibility and real prerequisites before dispatch. |
| R27 | Use the selected provider’s existing execution and resume contract, keep observed proof with the originating criterion, and report unexpected scope for decision. |
| R28 | Connect the existing brief, decision, bug and Issue formats to independent intake routes. Keep a bounded repair small. |
| R29 | Ship a versioned integration with documented compatibility, ownership and recovery. Assemble a bundle only when the chosen components can be resolved. |
| R33 | Extend borrowed document operations to every supported writing route. Preserve each format, its own prerequisites, authority, checked delivery and handoff to its actual consumer. |
| R34 | Give procedures, references and session replies wording suited to the reader’s decision and the evidence available. |
| R35 | The public index must lead readers directly to usable guidance for every released feature and supported document type. A guide or a named section can satisfy the requirement. Create a separate guide when readers need a distinct procedure or reference. |

## Production order

1. **Discover the need.** Record an interview when stakeholder answers matter. Use existing authoritative answers when available. A brief consumes those facts to frame the opportunity. A complete request may enter at the product definition.
2. **Define the product and features.** The Product Requirements Document (PRD) identifies users, intended outcomes, in-scope features, exclusions and decision authority. For several independently deliverable capabilities, produce a capability map before deriving their individual specifications. A single capability can proceed directly.
3. **Specify each capability and its stories.** The Spec Driven Development document (SDD) identifies the feature or epic and states its behavioral rules, boundaries, user-visible outcomes and observable acceptance scenarios. If the project already owns a story elsewhere, reference that version and criterion. Resolve the governing outcome before writing a child story. Research material unknowns before any design or criterion that depends on the answer. An unresolved material question blocks only its dependents. Record an actual choice in the decision record.
4. **Design and review.** Use architecture, internal design and interface contracts as needed. Produce the requirements-quality checklist against the identified specification before implementation readiness. For a critical user flow, link its steps to the feature map, its purpose to the product requirement, and its proof to a test or explicit gap. Existing surfaces can be mapped earlier. Proposed designs stay identified as proposed.
5. **Plan delivery from the reviewed stories.** Link to the applicable story and criterion. Explain the approach, interfaces, stages, dependencies and recovery. When coordinated delivery needs one, the Implementation Plan (IP) consumes the applicable specification, settled constraints and decisions. When a feature or epic governs the work, identify it and its integrated acceptance. Otherwise use the directly authorized scope and outcome. A feature may be the direct parent of stories; introduce an epic only where grouping adds value.
6. **Break the reviewed stories into shippable tasks.** For a child User Story (US), use the parent outcome established in the specification. Preserve its revision when authority or proof depends on it. A directly authorized independent story can carry its source, value, scope and proof inline. Resolve that story and its acceptance criterion before writing a child Issue. Include dependencies, permitted effects and required proof. If a parent is missing, stale, ambiguous or contradicts the current scope, locate it, author it first when authorized and sufficiently sourced, or report the unresolved dependency. An independent improvement, bug or chore can use one Issue as specified in R11.
7. **Assemble and use the feature task list.** For a multi-task feature, Tasks reads the reviewed spec and plan, resolves or writes the Issues from step 6, and writes one `tasks.md` that links them in execution order. Stop at document delivery for a writing request. For an authorized build, Implement reads the plan, list and selected Issue, then returns to the list as work completes. See the [command and document sequence](#when-to-write-and-read-tasksmd).
8. **Verify and close.** Define proof before implementation. Record observed results only after execution. A changed parent reopens affected children; retain applicable evidence for unaffected work. Close each parent on its usable outcome.

### Link work to its parent and designs to their sources

Use the project’s existing tracking and document conventions. A parent identifies the larger outcome a child was commissioned to deliver. A source link identifies the rule, constraint or decision the reader needs to use. The public index helps people find writing instructions. An index entry grants no authority to undertake project work.

| Document being written | What the reader should be able to follow |
| --- | --- |
| Product Requirements Document (PRD) or feature specification | Link the brief, product objective or approved requirement that defines this scope, if one exists. A directly authorized request with sufficient scope and evidence can start here. |
| High Level Document (HLD) | Link the requirements, quality goals and constraints that explain the architecture. A shared architecture can serve several features without belonging to an epic. |
| Low Level Design (LLD) | Link the component section of an applicable HLD and any requirement, decision or interface contract the implementer relies on. If a bounded design is already authorized and a contract settles its component boundary, the contract can supply that context directly. |
| Interface Contract (IC) or Decision Record (DR) | For a contract, identify the provider, consumers and observable obligations at their boundary. For a decision, identify its drivers and the accepted choice or pending status. In either case, link the specific governing source where one exists. Other documents point back to the contract or decision that owns the detail. |
| User Story (US) or Issue | A child story points to the feature or epic that assigned its outcome. A child task points to the story and the acceptance criterion it delivers. An independently authorized Issue or story can carry its scope, outcome and proof inline. |
| Implementation Plan (IP) | Link the specification or approved record that defines what to deliver. Link design constraints, dependencies or rollout decisions where a delivery step relies on them. A bounded change may keep its steps in the Issue. |
| Test or verification record | Link to the behavior or acceptance criterion the check can prove. Record the observed result against the candidate when the check runs. A planned test describes expected behavior. |

Use a native parent field, a stable requirement ID or a link to the exact section. Keep each rule with its owner and use native backlinks where available. One resolvable link suffices unless the project requires another. Add an explicit revision when approval, compatibility or verification depends on the version, or when project governance requires it. A missing declared parent, contradictory governing rule or unresolved contract holds only the dependent work. An absent optional document creates no blocker.

#### Refund approval

Suppose the approved refund specification says only a manager may approve a refund. The HLD identifies the service that owns authorization. The LLD points to that service’s section and the manager-only rule. A child Issue for denying an employee’s attempt links to its story’s denial criterion and the LLD section if the implementer needs it. The test targets that criterion and checks the employee’s request is denied. The test result stays open until somebody runs it on the candidate.

For the same design request in a smaller project, suppose the authorized scope, manager-only rule and owner of the authorization check are already explicit in the approved interface contract. The writer can produce the LLD from that contract without creating an HLD or epic. If the team later assigns an Issue to a specific story and its denial criterion cannot be located, that child stays open until the reference is resolved.

### When the writer may ask the owner

Apply R18 at the supported writing entry on either host. Inspect the smallest authoritative input that can settle the issue. Ignore details immaterial to this document. Keep current behavior, required future behavior and design discretion distinguishable.

| Basis | Required behavior |
| --- | --- |
| Observed fact | Cite the applicable code, configuration or other observation at its revision. Write what that evidence establishes. |
| Governing requirement | If the request preserves an existing rule or an applicable standard determines the answer, cite that authority and use it without asking. |
| Delegated choice | Within granted discretion use a fitting project convention or supported practice. Record the rationale when it affects the design. General advice can inform a recommendation. |
| Open decision | Ask only when a material consequence remains outside the writer’s authority. State the unresolved difference, or identify the one missing owner-held fact. Never manufacture alternatives. Continue independent writing; an early draft exposes the open decision and its consequence. |

Python checks applicable coverage, valid source and answer references, and permissible readiness transitions. The supported host workflow asks and receives the actual question and reply. Semantic review determines whether the evidence supports the claim and whether a question was necessary. An unverifiable reply, preselected option or silence cannot confer authority.

### How upstream templates map to the writer

Technical Writer owns the published forms, examples and checked-output contracts. A shortcut selects the same owning reference as an ordinary writing request. The following is the implementation decision for all five top-level document templates in the inspected upstream revision.

| Upstream source | Useful structure to adopt | Technical Writer owner and boundary |
| --- | --- | --- |
| [spec](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/spec-template.md) | A valuable user scenario, an independent demonstration, meaningful edge cases, requirements, outcomes and stated assumptions | Use the behavioral specification for feature rules. Product purpose, users and success measures belong in the Product Requirements Document (PRD). Reuse the story reference for a separately shippable slice. Keep each feature story and its observable acceptance in the governing specification, or link its existing project-owned story record there. Keep permissions, failure behavior, IDs, source authority and unresolved decisions. Include targets and priorities only when supported. |
| [tasks](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/tasks-template.md) | Group child work by story, identify real dependencies and give each slice a demonstrable outcome | One task uses the existing Issue template. For a multi-task feature, produce one `tasks.md` and linked Issue records. Preserve their story-criterion mappings. Each task has bounded scope, acceptance and smallest sufficient proof. Mark parallel work only when contracts and ownership allow it. A standalone Issue remains eligible. Setup, foundational and polish phases appear only when real work needs them. |
| [plan](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/plan-template.md) | Record applicable technical constraints, governing principles and affected project structure | The Implementation Plan (IP) owns delivery strategy, milestone sequence, requirement coverage, rollout and recovery. Link each in-scope story and its criteria. Put the detailed order and checkbox progress in the feature’s task list. Put architecture, internals and shared interfaces in their existing design or contract records when needed. Link them. Use verified project paths. A template example cannot establish a new platform, file or mandatory phase. |
| [checklist](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/checklist-template.md) | Derive review questions from the actual requirements and group them by relevant concern | Reuse the requirements-quality checklist in A10g. Record the specification revision, located evidence, verdict and correction. A checked item about requirement quality cannot establish that the feature passed a runtime test. |
| [constitution](https://github.com/github/spec-kit/blob/a4d571229e164e440f8950cac034607bae7b7518/templates/constitution-template.md) | Read project principles and their governance before planning | Reuse the project’s adopted Policy (POL) or Technical Standard (STD). Write policy only on request. A suggested principle, such as test-first development, requires actual authority before it becomes binding. |

For the Low Level Design (LLD), use the existing design template and its component, data, interface and failure contracts. The upstream feature specification and plan provide context. Preserve the current User Story (US) template for stories and epics, and the Issue template for tasks. Add a missing useful distinction to its owning guide or example only when the existing guidance does not already supply it. Link upstream sources as prior art. No vendored template tree, upstream installation or generated second set of specifications is required.

### Feature task lists and Issue acceptance

For a feature with several independently shippable tasks, produce one `tasks.md` in the feature workspace. Each task maps to an Issue that owns its scope, acceptance criteria and required proof. A small change with several ordinary steps can keep those steps in a single Issue. Generate the same feature list for a normal writing request on either host. Using the optional implementation workflow requires separate authority.

| Record | Question it answers | What to maintain here |
| --- | --- | --- |
| Behavioral specification | What must the user be able to do? | Own the feature’s stories, their acceptance scenarios and independent demonstrations, or resolve the authoritative project story. |
| Implementation Plan (IP) | Why take this delivery approach? | Record the governing specification, technical approach, milestone order, constraints, rollout and recovery as applicable. Explain material ordering decisions once. Use the project’s existing plan. The upstream implementation command reads the active feature’s `plan.md`. |
| Feature `tasks.md` | What can the implementing agent start or resume? | Group rows by story in delivery order. Identify the first usable result, the observable demonstration for each story, genuine blockers and safe parallel work. Link each row to the stable Issue and its applicable criterion. Keep checkbox progress here. |
| Issue | What change is authorized and what proves it? | Maintain the task’s scope, acceptance criteria, boundary cases and evidence in its owning record. If scope or criteria change, refresh the affected row before dispatch. A checked box alone establishes neither task nor story acceptance. |

Reuse the project’s authoritative Issue. Where work lives in Markdown, keep the bounded task record at its row or link an existing Issue section. Maintain each task criterion in one place. The default plan links the stories and task list and contains the delivery detail it owns. For standalone authoring, a separate plan is useful when the approach, rollout or recovery needs its own explanation, or project governance requires one. For the optional upstream workflow, make the governing plan available at the feature’s required `plan.md` entry. Keep the detailed checklist in `tasks.md`.

Use the shipped task-list template and generation instructions as the starting point. Keep their checklist syntax, feature-local IDs, story labels and verified paths. A row’s short ID resolves within its feature. Carry or resolve the authoritative Issue ID, criterion and source revision at handoff. Use `[P]` only for work in the eligible phase with settled interfaces, independent changes and no outstanding dependency between the tasks. Write an actual blocker beside the affected task. The priority of two stories can set their delivery order without implying a technical dependency. Include setup, test or cleanup tasks only when the feature needs a separate deliverable.

#### When to write and read `tasks.md`

The operation names below describe intent on either host. Use the installed command or normal writing request that serves that intent. All file lookups stay within the selected feature. The optional upstream workflow uses the filenames shown.

| Operation | Read first | Produce or select | Next consumer or stopping point |
| --- | --- | --- | --- |
| Specify | The authorized request, governing requirements and project context | `spec.md` with feature behavior, stories and their observable acceptance scenarios | Plan reads the reviewed specification. |
| Plan | `spec.md` and applicable constraints or contracts | `plan.md` with story references, delivery approach and material ordering decisions | Tasks reads the reviewed spec and plan together. |
| Tasks (feature breakdown) | The active feature’s `spec.md`, `plan.md`, applicable design and existing Issues | Resolve or author one Issue per shippable task within the request’s authority. Publish one checked `tasks.md` with rows pointing to the correct Issues and criteria. | For a writing-only request, deliver the list and stop. When implementation is authorized, Implement consumes the list. |
| Implement | The active feature’s `tasks.md`, `plan.md`, the eligible row’s Issue and criterion, and relevant spec or design | Make the authorized change. Attach the observed proof to the Issue and update that row’s progress. | Return to the same list to select the next eligible Issue. When the work is exhausted, assess the integrated story and feature outcomes against the governing specification. |

**Single task.** A singular `task` request writes or edits one Issue, which may be a tracker record, a project-named file, or an addressable section in an existing Markdown document. For an independent fix this can be the entire handoff. There is no required singular `task.md` between Tasks and Implement. If an Issue is missing or its revision is stale, resolve the affected reference before dispatch. An existing Issue keeps its identity when the list is refreshed. Writing a breakdown grants no authority to post to a tracker or execute code.

**Guided continuation.** A read-only next-step request after the reviewed plan can say “Next: feature task list (`tasks.md`), so the implementer can see which Issues can start.” If a requested one-document continuation still needs an Issue, name that specific prerequisite and continue with it only under the existing writing authority. An explicit request for the whole breakdown may author the Issues and list together. After the checked list, a writing-only session reports delivery. Only an authorized implementation request crosses into execution.

#### Refund status and filtering

The following example assumes two approved stories, an API that already stores and exposes a refund’s decision, and separate dashboard and CLI code. The paths and Issue numbers are illustrative. Resolve paths and Issue references against the real project when generating a list.

```markdown
## Phase 1 — User Story 1: View a refund decision (P1)

**Goal:** Support can see the recorded decision from either tool. This is the first usable story.
**Independent test:** Look up the same refund in the dashboard and CLI. Both show its recorded decision.

- [ ] T001 [P] [US1] Show the stored decision in dashboard/refund-status.ts (Issue #81, AC1).
- [ ] T002 [P] [US1] Show the stored decision in cli/refund-status.ts (Issue #82, AC1).

## Phase 2 — User Story 2: Filter refunds by decision (P2)

**Goal:** Support can find refunds by their decision.
**Independent test:** Choose Denied with both approved and denied refunds present. Only denied refunds appear.

- [ ] T003 [US2] Add decision filtering to api/refunds.ts (Issue #83, AC1).
- [ ] T004 [US2] Connect the dashboard filter in dashboard/refund-filters.ts (Issue #84, AC1). Depends on T003.
```

T001 and T002 can start together against the settled read contract. Each delivers a usable change. US1 can ship after both surfaces demonstrate the expected result, before filtering exists. Within US2, T003 can ship as a usable API filter. T004 waits for evidence that the filter works under Issue #83’s criterion. For example, a request for denied refunds against mixed input returns only denied records. The implementing agent recovers #84’s own acceptance from that Issue when T004 becomes eligible.

### How the optional workflow uses the full catalog

Start from the writer’s live [format catalog](../SKILL.md) and [output contracts](../contracts/documents.json). Where the catalog groups several contract kinds, retain each supported kind and its aliases. Include the seven approved forms in A10a–g as their owning routes ship. Apply the writing rules to each artifact and use Visual Guidance (VG) when it includes a diagram. Keep reference-only guidance and native host file formats in their existing roles.

| Request or feature input | What the workflow does with it |
| --- | --- |
| Discovery interview, brief, capability map, research record or product requirements | Carry sourced intent, scope, open decisions or research to the document that needs them. Select the relevant capability before writing its feature specification. |
| Requirement, behavioral specification, requirements-quality checklist, story, Issue or implementation plan | Preserve exact requirement and criterion references. Apply the project’s parent rules and standalone exception. Dispatch implementation only for an authorized task. |
| High- or low-level design, interface contract, threat model, service objectives, decision record, policy or technical standard | Link the owning document and relevant section or revision when a later decision depends on it. Preserve project terminology, permissions and unresolved choices. |
| Feature map, critical journeys, test plan, test specification, test status or completion report | Link surfaces to journeys and criteria to checks. Retain observed results separately from proposed checks. |
| Bug report, incident report or any supported Issue subtype | Accept the requested record directly. Carry it into repair or follow-up only if that work is authorized. |
| Tutorial, how-to guide, explanation, repository README, agent instructions, reusable skill or output style | Write the requested format through its own entry and apply its format-specific checks. A guide or host file can be the final deliverable. |

For a direct request, select the canonical type, use its own discovery, writing, editing and review rules, and deliver the checked result. For a feature, reuse an appropriate existing document, or request the missing input according to R18. Recommend one eligible next document under R20. Preserve the actual project location, revision and relevant section when passing a document to the next consumer. Operators may initiate a document independently when its own prerequisites allow it. A borrowed command, template, checklist, assessment or workflow uses this same rule wherever it handles documents. A provider can consume a link or a scoped view without taking ownership of the document.

### Find features and document types from the public index

Link the public index from the repository README. Cover the released user-facing capabilities and supported document catalog, including standalone writing, discovery, editing, review, rewriting, visuals, checked delivery, documented maintenance operations, shortcuts, guided handoffs and each shipped optional workflow. Aliases, command spellings and small variants can share guidance when readers can identify the behavior that applies to their request.

Link to the page or specific heading that explains when to use the feature or format, what to provide and what result to expect. For instance, the focused-edit and review entries can point to different headings in the same README. An Issue variant can point to the section that explains its fields. Give readers a separate guide when they need a distinct procedure or reference. Include prerequisites, recovery or the next action where these affect the reader’s task.

The task that releases or changes a feature owns the guidance and its direct index link in the same increment. As examples, W35 owns shortcuts, W38 owns next-document guidance, W47 owns project-aware writing, W49–W50 own execution and resumption, and W51 and W52 own assessment and repair respectively. The owner of each A10a–g route makes its instructions findable from the index. W54 establishes the public entry. W61 covers already released features and supported types with missing or inadequate index destinations. The guide for an optional workflow describes its available behavior even if a separate tutorial or runtime demonstration is still proposed.

## Quality and interface constraints

Use Technical Writer’s document references and output contracts for form. Preserve verified project terminology, literal IDs and applicable native tracker metadata. Allow exact sections for projects without stable IDs and keep small self-contained work inline. For externally consumed data or output text, identify callers and compatibility before changing the contract. An existing approved document or delivery receipt must remain auditable under the version that produced it. The writer can recommend a scope change. Only the authorised decision-maker may adopt it.

## Acceptance criteria

These are the approved release criteria. The inputs and expected distinctions below precede implementation. Exact prose, host UI and choice of supported command syntax may vary without changing the verdict.

| ID | Starting state and action | Required observable result and safe boundary | Required proof |
| --- | --- | --- | --- |
| A1 · R1 | Edit an excerpt containing the `US` fixture key, a genuine document reference and a quoted value. | The fixture still derives the original domain, the quote retains its bytes, and the real reference follows the project’s naming rule. A correctly scoped synonym or prose edit remains possible. | Compare input and output at the consuming fixture rule. Review the edited sentence and an unchanged literal. |
| A2 · R2 | Supply a small self-contained issue, an unresolved opportunity and an approved multi-slice initiative with native parent tracking. Request the smallest useful output in each case. | The issue stays inline. The brief records problem evidence, outcome and unknowns. The parent view names the integrated outcome, dependencies and proof. A local budget, owner or new product claim appears only with authority. | Inspect the three routing decisions and resulting sections. Open the explicit product-to-behavior link. |
| A3 · R3 | Follow a connected feature from source revision to plan, task and proof. In copies, displace one ID, add unsupported work, then weaken a material condition while retaining valid IDs. | Each altered case identifies the offending location, its consequence and the affected criterion. The unaltered case resolves. A task justified by a necessary safeguard remains eligible. | Check explicit links where possible. Name the supported entry, visible result, authoritative side effect and a misleading shortcut. Compare the consumer’s observation with the source. Retain the baseline and defective examples. |
| A4 · R4 | Give the writer detailed evidence with a material exclusion and an open decision. Give another reader only the resulting approval opening. | The reader can state the change, beneficiary, exclusion and decision without guessing. Each answer is supported by the opening and its owning detail. An incorrect answer with a real quotation fails. | Save the two texts, reader response and source-grounded judgment. Do this for the representative case, without adding a reader run to routine writing. |
| A5 · R5 | Give one ambiguous request with a dependent choice and another with complete sources. | The first question can change the outcome. Its answer determines which branch follows. In the complete case the writer proceeds. Unknown thresholds and silent users never acquire an invented answer. | Inspect the public exchange, captured decision and resulting criterion. |
| A6 · R6 | Present a confirmed intermediate result, a genuine external blocker, and a checked document containing a material choice. | Progress explains the change. The blocker identifies the last confirmed fact and required action. Checked delivery exposes the reviewed choice, file, status and provenance. A changed or unreviewed decision sentence fails the exact-message check. | Compare the actual messages with the observed results, reviewed artifact and delivery receipt. Include a delivery requiring no owner action. |
| A7 · R7 | Use a routine editing request and the integrated handoff case through the supported skill on Codex and Claude Code. | Both route to the same governing rules and preserve the same required behavior. A small edit avoids unrelated workflow material. Host-specific permission or tool limits stay explicit. | Retain per-host observations on the identified artifact, with the case inputs, actual outputs, public evidence and model/settings when exposed. |
| A8 · R8 | Change an upstream rule after downstream work was reviewed. Supply one unaffected criterion and one previously failed attempt. | The changed criterion loses current acceptance until newly proved. Unaffected evidence retains its original identity and scope. The historical failure remains available. A completed task count cannot close the integrated outcome. | Inspect the before/after source, affected references, candidate identity, evidence and criterion verdicts. |
| A9 · R9 | Give the writer Mirai facts, stable IDs, an open approval and no prior document or application template. Request a complete Product Requirements Document (PRD) and one linked behavioral specification. Give it a second project’s facts and request a new product document through the same entry. | The writer produces each whole artifact using its own type contract. Project facts stay attributable, unresolved choices stay open, and the downstream requirement resolves to its source. A misleading legacy heading cannot replace the writer’s template. A consumer conflict identifies the incompatible field and owner. | Inspect the actual documents, normal Technical Writer checks, source links, decision status and version-bound evidence. Reuse the first product document across both tasks. Record document acceptance separately from application ingestion. |

### Seven authoring cases and hierarchy acceptance

Each A10 case starts with source facts and a request for the named artifact through Technical Writer. Keep the actual output, its checked document/version binding and the downstream observation. One linked example set can supply all seven cases. A heading check alone is insufficient.

| ID / artifact | Inputs and required content | Consumer verdict and safe failure |
| --- | --- | --- |
| A10a · Discovery interview record | A question changes scope or intent. Capture question, answer, source, unresolved choice, restatement and actual confirmation status. | Brief or product author can distinguish an owner answer from a suggestion. A silent owner leaves the restatement open. |
| A10b · Brief | Given problem evidence or an interview, record beneficiary, desired outcome, exclusions, unknowns and any owner-supplied appetite. | Product owner can decide whether to develop the opportunity. A missing baseline stays unknown; no budget is invented. |
| A10c · Capability map | When an initiative has several independent outcomes, name stable capability IDs, responsibilities, actual dependencies and a justified build order. | The spec author selects the intended capability. Independent capabilities can be parallel. A cycle is surfaced for resolution. |
| A10d · Research record | When evidence is needed before design, identify the question, sources, findings, uncertainty, supported recommendation and actual decision status. | Designer can cite the finding and identify who must decide. A study or working prototype cannot silently approve a choice. |
| A10e · Feature map | For an observed surface, record its user-facing name, entry or route, verifiable control/handle, source revision and observable end state. Mark proposed surfaces explicitly. | Journey author or verifier can locate the surface. A guessed route/handle or app launch alone cannot establish that it was reached. |
| A10f · Critical journeys | Given a mapped surface and sourced risk, record a journey ID, actor, ordered steps, observable result, why failure matters, source and test reference or explicit gap. | Verifier resolves each referenced surface and finds the named check. An unknown screen or unrun test cannot count as verified. |
| A10g · Requirements-quality checklist | After a candidate specification exists, identify the revision, criterion under review, quality question, located evidence, verdict and unresolved correction. | Implementer sees whether scope, permission and observable proof are determinate. A checked box alone cannot establish implementation or test success. |

**A11 · R11.** Given a known feature or epic, create a story linked to its outcome and a task linked to a specific story criterion. Resolve both links at the declared revisions. Remove the story parent, remove the task parent, then supply a stale or wrong parent. In each case identify the broken edge and withhold ready status for the dependent work. A legitimate standalone broken-link fix with its own source, expected destination and link check remains eligible. Retain the valid chain, rejection locations and standalone result. A task must not acquire a fictional story or switch to standalone merely to pass.

**A12 · R12.** Give the writer the worked issue’s vague partial-write clause, the governing WEB-09–WEB-10 details and a clear story sentence. Request an edit for an implementer that an owner can also understand. From the revised passage a reader can identify the three row states, when submissions stop, the prerequisite to offering a retry and who can choose it. The full issue preserves the 500-ID limit and refresh of confirmed rows and counts. Preserve the clear story’s meaning and literals. A smooth rewrite that requires a retry, invents a guarantee or drops the limit fails. Save the source, edited passage, reader answer and reviewer’s located reason. In the session, use A6 to assess a direct result, a real blocker and a reviewed owner decision. A plain sentence, necessary technical term or alternative wording may pass. Punctuation frequency and word-count targets cannot settle this test.

**A13 · R13.** Given the worked story and the Issue guide, follow their links to the child assigned the failed-save criterion. Recover its scope, observable failure state and source. Follow its parent link back. A task that assigns bulk editing or links only to the broad Feature fails. Keep the child and the located reader answer.

**A14 · R14.** Give the user a read-only manual handoff from a known starting location. The writer’s reply must identify the exact action, expected result and safe recovery for the supplied failure. If the user already has the document, answer the question directly. When the user misunderstands who writes the reader answers, clarify who acts and which decision remains theirs with a concrete example. An unknown role stays open. Retain source, actual replies and the reader’s recovered action or role.

**A15 · R15.** Observe a routine progress reply with no label or absence claim and an applicable message with a wrong canonical label. The first can be sent after editorial review without the file check. The second produces a located naming finding. Retain the actual trace and comparison. Preserve existing artifact checks and version-bound finalization.

**A16 · R16.** Before installation, read one plain-language explanation, choose the right entry for an idea, an agreed feature or a small fix, and trace WEB-06 through a story and illustrative task to its specified failure check T10. The passage identifies what a developer supplies and what the writer returns. A planned check stays visibly distinct from an observed result. From the `README.md` file quick start, use the numbered sequence to route one governed feature to its story and child task, and one independent broken-link fix to a standalone Issue. The reader can locate each conditional artifact in A10, say what has to exist first, and distinguish planned verification from observed evidence. A missing story blocks only the dependent child. Keep the two reader answers, the relevant passage and its resolved links. From Quick start, locate the reviewed plan, the Issues and the feature list in order. Identify Implement’s actual inputs, the writing-only endpoint, and how the agent selects another task. Creating a mandatory `task.md` after the list fails.

**A17 · R17.** Use the same improvement in three contexts. An independently authorized small change with inline scope and proof can ship in one Issue. A contribution assigned to a story must resolve that story and criterion. A directly authorized user outcome may be written as a standalone story if its value, boundary and proof are clear. Then compare two deliveries for the same feature. A single, bounded delivery can keep its steps inline. A migration requiring the old and new readers to coexist needs rollout order, compatibility evidence and recovery before the dependent switch. A project-mandated parent or planning step remains binding. Retain the selected records, governing input and reason at the first point where the choice differs. Reuse A11 for the broken-parent case and A16 for README discoverability.

**A17b · R17.** Use the refund example at the ordinary writing entry. Given a governing specification and HLD, the LLD identifies the manager-only rule and the service that enforces it. The task and test lead to the employee-denial criterion. Given direct authorization and a contract that supplies the same facts, the LLD can be ready without an HLD, story or epic. An invented parent, missing governing rule treated as settled, or mandatory duplicate backlink fails. For a declared child whose parent or criterion cannot be resolved, reuse A11’s dependent-only refusal. W62 owns the two design cases.

**A18 · R18.** Use the two export requests with the same current staff-only route and compare the actual documents and public questions. (a) “Add CSV to the existing download; only the format changes” produces zero permission questions and preserves existing access. (b) “Let customers download their own reports,” with individual versus organization ownership unresolved, produces exactly one targeted ownership question before the dependent requirement becomes ready. Silence leaves the ownership open in a draft. A genuine answer bound to that question unblocks only the supported permission. Omitting the material topic blocks readiness. A cited passage saying permission is undecided cannot justify an administrator-only rule. Reuse those passages and verdicts for the negative cases. Check one missing owner-held fact without invented options, one delegated routine choice without an interview, a lightweight story or Issue, and the narrow-edit exception only where existing evidence is insufficient. Preserve historical receipts. Host-specific claims require an observed exchange on that host.

**A19 · R19.** On their actual hosts, Claude Code’s /prd, /lld and /task and Codex CLI’s $prd, $lld and $task select the existing writing routes when available. Observe one actual checked artifact per host, mechanically resolve the rest of the catalog, and exercise a collision, repeat install and owned-only removal. The brief survives intact. The spec selector produces a behavior specification; task produces one Issue and tasks decomposes approved scope into applicable Issue records. Checklist and analyze have their distinct review outcomes. The host entries neither replace writing templates nor confer implementation authority. For the refund-status feature, W40’s output identifies the first shippable story, both independent demonstrations, the T001/T002 parallel pair and the T003 prerequisite for T004. Each row resolves to the corresponding Issue and criterion. A standalone fix stays in one Issue. From an ordinary feature request, recover story acceptance before opening the delivery plan. Follow the plan’s story reference and the task row to their owners. Reuse an existing Issue when supplied. With Markdown alone, accept a bounded record at the task without an external tracker. A second editable definition or an unresolved criterion fails for that task. A matching ID or link does not excuse a second editable copy of the case. For an existing owner, keep the case there and use a reference plus any distinct proof in the consuming document.

**A20 · R20.** Given a reviewed feature, an unresolved dependency and a completed standalone fix, guide or next returns respectively one useful recommendation, one blocked decision, or completion. For example, “**Interface Contract (IC)** — agree on refund error codes so both clients handle failed refunds consistently.” The recommendation alone writes nothing. Continue produces one grounded document; repeating the same request after resumption cannot duplicate that result. A changed parent revision reopens only affected work. An unbound suggestion cannot alter the checked final message. For a settled multi-task plan with linked Issues ready, next names the feature task list. After its checked delivery, a writing-only request finishes. A request for one independent task routes directly to an Issue.

### Acceptance for maintained specifications, fields and shared contracts

Use the same task evidence at the requirement, story and epic when it proves their outcomes. Both hosts use these criteria.

- **A21 · R21 (F25, W43).** Use the team’s declared maintenance convention. Link a retained snapshot to its maintained successor or other approved source when known. With no authority for a material difference, preserve both and ask one focused question. At the normal edit entry, supply a frozen launch specification allowing seven days and an approved maintained policy allowing thirty days. Ask to update the feature. The draft cites the maintained rule and labels the seven-day value historical. Both source files remain intact. Remove the maintenance decision while keeping two plausible values. The writer identifies the conflict and asks which governs before committing to a value. It can draft unrelated sections. Capture the two draft excerpts or the focused question, source revisions and before/after identities of the inputs. Reuse existing discovery and rewrite evidence for unchanged behavior.
- **A22 · R22 (F26, W44).** When a task implements a constrained field, link its exact owner and field, preserve relevant semantics and flag uncovered or misattributed fields when reviewing the requested scope. Reuse the project’s schema, Interface Contract or Low Level Design as appropriate. From a contract where Order.code is optional and Return.code is required, request the task for Return.code. The Issue points to the exact Return.code definition and preserves the required behavior. An unambiguous existing field pointer is sufficient. Review a variant citing Order.code for the return requirement. The review identifies the Issue, wrong field and missing coverage. An unrelated prose-only Issue requires no field citations. Retain the authored Issue, read-only review excerpt and the unchanged source definitions. Use this same pair at W40/W41 if available.
- **A23 · R23 (F27, W45).** For independently released components, identify the authoritative source and immutable revision, the consumer’s copy or pin, and the evidence for deployed compatibility when claimed. Resolve disagreements at the owner. Leave deployment support unknown when there is no observation. Given an owner contract at v1, a divergent consumer copy and a proposed v2, ask for an Interface Contract update. It identifies the source revision, pins the consumer to v1, names the discrepancy and directs the proposed change to the owner. The consumer copy is untouched. Provide only the v1 pin and mock results, with no deployed-provider evidence. The handoff distinguishes the agreed version from unknown runtime support. One shared file used by both components requires no synchronized copy. Keep the cited owner revision, consumer pin and resulting compatibility passage; inspect the copy identity. No service deployment or provider test is needed to assess this writing change.

**A24 · R24.** F28/S28. Fresh and existing users reach the same checked writer through their supported host. A pre-existing unrelated skill remains untouched. The accepted Builder validates a real document using the renamed release. Use W46 for the required proof.

**A25 · R25.** F29/S29. From an existing project, the installed command produces a checked spec for the selected feature on each supported host. Repeat setup preserves the edited project document. The standalone writer remains usable. Use W47 for the required proof.

**A26 · R26.** F30/S30. With two features using the same short upstream task number, the actual selected consumer reads the refund Issue, its authorized actor and denial criterion. A stale view stops the affected dispatch. Use W48 for the required proof. Give the real implementing agent the same W40 list. It identifies T001 and T002 as eligible together and the first story’s independent demonstration. Within US2 it can select T003 and holds T004 until the API criterion is met. Then it can select T004 and recover Issue #84’s criterion. Preserve the observations on the identified candidate.

**A27 · R27.** F31/S31. Follow one refund task from dispatch to an observed permission failure, correction and evidence-backed verdict. Resume at the same task and candidate boundary after interruption; uncertain effects cannot be replayed on guesswork. Use W49, W50 for the required proof. Routine closure uses the existing acceptance evidence. A broader Converge review requires a user request.

**A28 · R28.** F32/S32. An idea lacking decision evidence ends with a supported question or stop recommendation; a bounded defect reaches a scoped repair and expected check. Neither input silently starts coding. Use W51, W52 for the required proof.

**A29 · R29.** F33/S33. Using a versioned local release and a declared upstream version, inspect the effective command, upgrade the managed integration, then remove it. Project-authored documents and other installed commands survive. Use W53 for the required proof.

**A33 · R33.** F37/S37. Resolve each eligible catalog type and alias to its canonical owner at the integrated entry, including A10a–g. A tutorial request returns a checked tutorial and ends. An authorized child Issue carries its reviewed design constraint and exact source. A stale design reference holds that dispatch. Use W58–W59 evidence.

**A34 · R34.** F38/S38/W60. Use the [committed guide](https://github.com/fatonsopa/ai-technical-writer/blob/d8bf859f0eec178aa34b24e29aef10290e984c3b/references/writing_style.md#write-a-feature-page-people-can-use) and its worked case. The feature example identifies the action and source. The session identifies the reviewed approval rule and the unresolved decision.

**A35 · R35.** F39/S39/W54/W61. Compare the release’s public features and supported document types with the index. Each entry opens on guidance that explains when to use it, its input and expected result. A direct link to a useful section passes, including one shared by variants it covers. For focused editing and review, the respective destinations must distinguish a bounded change from findings. An omitted entry, broken anchor, unrelated section, empty stub or general overview that leaves the reader searching fails. Reuse the candidate and link observations from the owning tasks.

## Open decisions

**D7.** For approved capabilities borrowed from the upstream project, use its pinned first-party implementation directly or adapt its source as described in the [upstream reuse instructions](./implementation-plan.md#reuse-the-upstream-implementation). Preserve the Spec Writer document contracts and standalone entry. This implementation choice adds no work items.

**D6.** For an authorized feature build, use the bundled workflow when the project selects it. It runs Specify, Plan, Tasks and Implement, with separate reviews after the specification and the plan. Close routine delivery when the existing task and story acceptance criteria and applicable Definition of Done are demonstrated on the identified candidate. Invoke upstream Converge manually only when the user requests a broader review of that feature. Its findings may identify work to propose; they grant no additional implementation authority. A request to write a document ends at its checked handoff unless implementation is separately authorized. The decision covers documenting the handoff within existing W49.

**D5.** The owner approved the optional workflow integration and the skill name **Spec Writer** (`spec-writer`). Claude implements the live rename on the handoff computer. The existing GitHub repository and clone URL remain the integration target. Spec Writer remains usable without the optional workflow. Implement the approved five toolkit stages within R25–R29. R24 owns the rename.

**D4.** The owner approved F25–F27 under R21–R23. The subsequent D5 decision adds the toolkit and selects its canonical identity.

**D3.** The owner approved R19–R20, their short handoff wording and host-specific entries. Implement the adopted upstream structures within Technical Writer’s owning forms as set out in the template mapping.

**D2.** The owner approved R18/A18 and its bounded implementation in F22.

**D1.** The owner approved the original revision 6 scope, including the conditional hierarchy, first-use naming convention and reviewed-delivery sentence. A user may name a document by acronym or full name at any turn. In ordinary authored prose, introduce the full name with its acronym and use the acronym when clear thereafter. Preserve contractual labels, literals and quotations. A checked handoff may include one useful result or open decision from reviewed content. Bind that sentence to the same reviewed version and keep older receipts verifiable.

## Related design and work

Use this specification as the behavior source for the Spec Writer change itself. The [Scenarios](#scenarios) section owns the stories and their acceptance. The [implementation plan](./implementation-plan.md) explains the delivery approach. The [task list](./tasks.md) contains the ordered work and its bounded Issue records, and the [handoff test specification](./test.md) checks whether a reader can use them. Each Issue owns its acceptance criteria and the evidence needed to close it. When the writing entry is available, generate the three-Issue sample from this plan and give that output to its real consumer as described in W-PACKET.

The implementation plan maps each finding to an epic and each criterion to bounded work and proof. This approved revision is the behavioral baseline. Amend affected clauses through the same decision record or work item that records the owner’s instruction. [Proposed implementation](./implementation-plan.md)

## Proposals awaiting owner approval

The approved work comprises F1–F33 and F37–F39, their 36 child stories, and W01–W54 plus W58–W62. W60’s guide edit shipped on the handoff branch before the remaining implementation. W46 covers the public identity, W49 covers on-request Converge, and W58–W59 cover the full writing catalog. The additional worked walkthrough and demonstrations in F34–F36 (W55–W57), and the additional assessment criterion W51.3, await the owner’s approval. F39 now owns the approved index task W54 and index coverage for every released feature and supported document type. Exclude only the pending proposals from execution and completion counts. The following material is retained for a future decision. The on-request Converge policy in D6 governs these proposals too.

| Proposed ID | Candidate behavior |
| --- | --- |
| R30 | Use the approved capability index and add one worked quickstart linked from the root README. Reuse the existing README, Tutorial (TUT) and How-to Guide (HTG) formats. Publish as repository-readable Markdown. |
| R31 | Document and exercise the read-only upstream list and info operations. Keep feature-output discovery in the quickstart and use existing upstream provenance for installed assets. |
| R32 | Use the unmodified upstream workflow, identify its run and active feature, and document Converge as a user-requested review. Reconcile any appended tasks with the original Issue and permitted change. |

**A30 · R30.** F34/S34. From the root README, a new reader chooses an existing-document request or the optional feature route, then identifies the input, output and next consumer for the complete refund example. Each advertised capability has a reachable entry on the identified release. Use W55 for the proposed walkthrough. Reuse the approved W54 index.

**A31 · R31.** F35/S35. From a project with one known override, locate its contribution and the lower layer with the native inventory; find the generated feature spec separately. Inspection leaves the project content unchanged. Use W56 for the proof.

**A32 · R32.** F36/S36. Use the shipped upstream workflow on the authorized feature. A spec verdict leaves the plan gate independent. After Implement, the operator closes against acceptance evidence and, if the user requests a broader review, runs Converge manually for that same feature and candidate. A remaining gap stays open until the underlying criterion is proved. Use W57 for the proof.

### Default feature route and its outputs

Use the feature route for an authorized software change. A direct document request may end with one checked document. Follow the project’s governing principles; the upstream quickstart establishes a constitution once per project. Keep the optional assessment and defect routes separate from the feature prerequisites.

| Phase | Input | Output and next consumer |
| --- | --- | --- |
| Specify | User intent, governing rules and located sources | The feature’s `spec.md` states the observable behavior. Clarify consequential ambiguity here before the planner uses it. |
| Plan | The governing spec and project constraints | `plan.md` records the approach. Link relevant design, research, model or interface details to the tasks that depend on them. Use the quality checklist when the adequacy of the requirements needs review. |
| Tasks | Spec, plan and applicable design | Resolve or author the Issues and then write `tasks.md` with their execution order and criterion links. The list is the input to authorized implementation. Read-only Analyze can locate a cross-document conflict before dispatch. Correct the owning record first. |
| Implement | The approved scope, selected task and its proof | The provider changes the candidate. Preserve the candidate identity, observation and task progress. A checked requirement-quality item or task marker alone cannot establish delivery. |
| Converge (on request) | The actual candidate and the same feature’s spec, plan and tasks | If the user requests a broader review, the operator invokes Converge in the agent on the same feature. A clean comparison leaves the task list unchanged. When gaps produce appended tasks, preserve them, reconcile each against the authoritative Issue and obtain authority for any new scope. Record the verdict and outstanding proof. |

For the manual path, the longer upstream sequence inserts Clarify after Specify, Checklist after Plan, and Analyze after Tasks. Use those steps when they address a real decision or coverage gap. In the automated `speckit` path the installed definition and its actual gates determine what runs. A guide must mark any supplemental checks it asks the operator to run separately. A terminal workflow exit is evidence only for the steps observed in that run.

### Capability reference and artifact inventory

Use a short root README linked to a public capability index, feature tutorial, installed-artifact reference and workflow guide. In repository docs, label standalone writing, optional workflow integration and the chosen implementation provider. For each advertised capability name the user need, supported entry and host, required input, output location and next action. Upstream integrates hosts, adds operations through extensions, changes existing behavior through presets, sequences steps with workflows, adjusts installed sequences with overlays, and distributes components as bundles. Link upstream for third-party tooling. Describe only the components the Spec Writer release supports.

A generated project document and an installed workflow asset use different lookup paths. Resolve the active feature from supported project state to find its spec, plan or tasks. Run the read-only upstream CLI to list command, template, script and hook contributions or inspect one returned ID. Named assets have a precedence stack; composing layers may still contribute below the winner. Hook registrations can be additive. An inventory row does not establish invocation, hook execution or document acceptance.

### Idea assessment in workflow mode

In workflow mode the optional assessment uses one idea slug, ordinarily progressing from intake to research, problem definition, concept comparison and decision. The upstream outputs are `intake.md`, `research.md`, `problem.md`, `concept.md` and `decision.md` under `.specify/assessments/<slug>/`. Use those artifacts when integrating the extension. Their contents reuse the writer’s existing interview, brief, research and decision guidance. The standalone writer can keep a small decision in its existing format.

| Step | Assessment file | What the next reader needs |
| --- | --- | --- |
| Intake | `intake.md` | Original idea, its source and the shared assessment slug. |
| Research | `research.md` | Supporting and contrary evidence, with citations, confidence and labeled assumptions. |
| Define | `problem.md` | Affected users, problem, goals, exclusions, success measures and the cost of leaving things as they are. |
| Shape | `concept.md` | Viable options, constraints, how much time or effort is worth spending, and trade-offs. |
| Decide | `decision.md` | Evidence-based scorecard and rationale. For an authorized handoff, supply the recommended option, scope, success measures and unresolved questions. |

Define can start from supplied intent. Shape and Decide require the problem definition. A `go` additionally needs adequate problem validity and evidence strength and a recommended concept. Include evidence for and against the idea, cite the source and confidence, and preserve assumptions as such. A `needs-clarification` verdict names the missing fact and affected record. A `kill` verdict retains the decisive reason and ends the assessment. Refine the affected artifact and decision when new evidence arrives. Only a separate choice to pursue the software idea passes the decision summary to Specify. [Assessment guide](https://github.github.io/spec-kit/guides/assessment.html) · [Command and verdict contract](https://github.github.io/spec-kit/reference/agentic-assessment.html)

### Proposed story records

These stories await the owner’s decision. They do not enter the execution list.

### F34 · Find a capability and follow a feature from request to evidence

As a developer using Spec Writer for the first time, I want to choose a supported capability and follow one feature through its documents, so that I know what to supply, inspect and do next.

#### Acceptance criteria

- **F34.1** Use the [S34.1 acceptance scenario](#s34-1) for the epic’s integrated check. Use S34.1 evidence on the candidate. <a id="f34-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: integration documentation maintainer. Child: [S34](#s34--find-a-capability-and-follow-a-feature-from-request-to-evidence). R30/A30. [Upstream guide](https://github.github.io/spec-kit/index.html)

#### S34 · Find a capability and follow a feature from request to evidence

As a developer using Spec Writer for the first time, I want to choose a supported capability and follow one feature through its documents, so that I know what to supply, inspect and do next.

##### Acceptance criteria

- **S34.1** From the root README, a new reader chooses an existing-document request or the optional feature route, then identifies the input, output and next consumer for the complete refund example. Each advertised capability has a reachable entry on the identified release. Record what the reader or operator actually found. <a id="s34-1"></a>

##### Scope and sources

Parent: [F34](#f34--find-a-capability-and-follow-a-feature-from-request-to-evidence). Owner role: integration documentation maintainer. [W55](./tasks.md#w55--walk-a-reader-through-the-default-feature-path) supports [S34.1](#s34-1) and consumes the approved [W54](./tasks.md#w54--publish-the-public-index-with-a-usable-focused-edit-entry) index. Use the shared Definition of Done.

### F35 · Inspect what the installed integration exposes

As a maintainer, I want to see which command or template is active in this project, so that I can explain an unexpected result without guessing from filenames.

#### Acceptance criteria

- **F35.1** Use the [S35.1 acceptance scenario](#s35-1) for the epic’s integrated check. Use S35.1 evidence on the candidate. <a id="f35-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: integration documentation maintainer. Child: [S35](#s35--inspect-what-the-installed-integration-exposes). R31/A31. [Upstream guide](https://github.github.io/spec-kit/overview/artifacts.html)

#### S35 · Inspect what the installed integration exposes

As a maintainer, I want to see which command or template is active in this project, so that I can explain an unexpected result without guessing from filenames.

##### Acceptance criteria

- **S35.1** From a project with one known override, locate its contribution and the lower layer with the native inventory; find the generated feature spec separately. Inspection leaves the project content unchanged. Record what the reader or operator actually found. <a id="s35-1"></a>

##### Scope and sources

Parent: [F35](#f35--inspect-what-the-installed-integration-exposes). Owner role: integration documentation maintainer. [W56](./tasks.md#w56--explain-an-installed-override-from-native-artifact-readback) support [S35.1](#s35-1). Use the shared Definition of Done.

### F36 · Document an on-request convergence review after the upstream workflow

As a developer running the optional integration, I want to know when automation stops and how to check the candidate, so that a successful workflow exit cannot silently become a feature acceptance claim.

#### Acceptance criteria

- **F36.1** Use the [S36.1 acceptance scenario](#s36-1) for the epic’s integrated check. Use S36.1 evidence on the candidate. <a id="f36-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: integration documentation maintainer. Child: [S36](#s36--document-an-on-request-convergence-review-after-the-upstream-workflow). R32/A32. [Upstream guide](https://github.github.io/spec-kit/workflows/overview.html)

#### S36 · Document an on-request convergence review after the upstream workflow

As a developer running the optional integration, I want to know when automation stops and how to check the candidate, so that a successful workflow exit cannot silently become a feature acceptance claim.

##### Acceptance criteria

- **S36.1** Use the shipped upstream workflow on the authorized feature. A spec verdict leaves the plan gate independent. After Implement, the operator closes against acceptance evidence and, if the user requests a broader review, runs Converge manually for that same feature and candidate. A remaining gap stays open until the underlying criterion is proved. Record what the reader or operator actually found. <a id="s36-1"></a>

##### Scope and sources

Parent: [F36](#f36--document-an-on-request-convergence-review-after-the-upstream-workflow). Owner role: integration documentation maintainer. [W57](./tasks.md#w57--explain-how-to-request-a-convergence-review-on-a-built-feature) support [S36.1](#s36-1). Use the shared Definition of Done.
