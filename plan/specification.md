# SpecDev improvement specification

<a id="spec-writer-improvement-specification"></a>

Status: Approved behavioral scope, revision 21. Applies to Codex and Claude Code. [Audit](./audit.md)

Source: The owner’s approved scope, the OpenSpec and naming decisions in D5–D7, and the [comparative audit](./audit.md).

## Purpose and scope

A person should be able to decide what they are approving, and an implementer should be able to recover the agreed behavior and its proof without the original conversation. This specification defines changes to the existing Technical Writer guidance, examples and affected checks. The planned public identity is SpecDev after the compatibility migration. SpecDev authors every requested specification-driven artifact in full, including the Product Requirements Document (PRD), behavioral specification, design, decisions, plans, stories, issues and verification documents. Mirai and other projects supply evidence and consume the results. Deployment, external tracker writes and publication require separate authority.

SpecDev (`specdev`) is the public entry, `/specdev` on Claude Code and `$specdev` or the documented native equivalent on Codex. Use it for both ordinary writing and a project’s OpenSpec changes. A direct document request uses the existing writing contracts without a project setup. To initialize the current project, ask for `/specdev init` (or the host equivalent). It delegates to the private OpenSpec executable’s native `init` at the selected root. A fresh setup requesting only SpecDev uses `--tools none`. Respect the user’s supported tool choices and flags. Initialization stops at project setup. For a change, the writer edits the selected project’s native artifacts in place. OpenSpec supplies structure, dependencies, validation, apply instructions and archive behavior. SpecDev supplies grounded prose, proportionate design depth and semantic review. Implementation and archive depend on the authority for those actions.

The existing repository and clone URL remain the delivery target. The rename on the handoff computer follows accepted Skill Builder B5/T50. W47 connects the writer to the privately pinned npm package `@fission-ai/openspec@2.1.1`; W48–W50 demonstrate task selection, authorized execution and recovery. W53 owns later upgrades and removal. These are planned changes. The [implementation plan](./implementation-plan.md) records rollout and evidence boundaries.

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

As a project owner, I want SpecDev to author the specification-driven documents I request, so that my project supplies facts and retains decision authority without needing its own writer.

#### Acceptance criteria

- **F9.1** From a blank start, deliver a complete product document and linked behavioral specification for Mirai and a complete product document for a second project. Preserve sources, IDs and pending owner approval. Record any consumer incompatibility separately. <a id="f9-1"></a>

#### Scope and sources

Delivery approach: [implementation plan](./implementation-plan.md). Owner role: project owner. Child: [S09](#s09--create-a-projects-first-governed-documents-from-facts). R9/A9. The original audit returned writing ownership to Technical Writer. For an OpenSpec change, the native schema now owns structure and SpecDev edits the content in place. [Audit finding F9](./audit.md#f9--high--the-proposed-integration-gave-document-authorship-to-the-wrong-component)

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

<a id="f23--start-documents-from-native-shortcuts"></a>

### F23 · Select a document from the supported host

A developer can keep the original brief and receive the same checked document through the qualified writer or an enabled shortcut.

**F23.1** Accept the integrated outcome against [S23.1](#s23-1) using its candidate-bound evidence. <a id="f23-1"></a>

#### S23 · Write the intended artifact from a short request

**S23.1** On the actual host, observe the original brief reach the right writer, inspect the checked output and verify its consumer. Exercise an occupied shortcut and repeated setup. The existing handler survives and the qualified entry remains usable. Use W40’s native refund list to recover the first usable outcome and true dependencies. <a id="s23-1"></a>

R19/A19. The writing-workflow maintainer owns this outcome. [W35](./tasks.md#w35--launch-three-document-types-in-claude-code) · [W36](./tasks.md#w36--launch-the-same-documents-in-codex) · [W37](./tasks.md#w37--expose-the-authorable-document-catalog) · [W40](./tasks.md#w40--write-the-feature-task-list-and-its-linked-issues) · [W41](./tasks.md#w41--route-quality-and-consistency-reviews)

### F24 · Guide the next document from project evidence

A project owner can ask what to write next, continue one authorized document or stop after a document-only delivery.

**F24.1** Accept the integrated outcome against [S24.1](#s24-1) using its candidate-bound evidence. <a id="f24-1"></a>

#### S24 · Choose and continue one eligible document

**S24.1** Use a feature, a blocked decision and a completed independent fix. Identify the next useful artifact, the missing prerequisite or completion. Continue only the requested writing and reuse its reviewed result on resumption. Retain the request, reviewed output and consumer observation. <a id="s24-1"></a>

R20/A20. The writing-workflow maintainer owns this outcome. [W38](./tasks.md#w38--show-the-next-useful-document) · [W39](./tasks.md#w39--continue-a-checked-document-handoff)

### F25 · Find the governing specification after delivery

As a maintainer returning to a delivered feature, I want to find which agreement governs the next change, so that an old delivery snapshot cannot silently reinstate retired behavior.

**F25.1** Accept the integrated outcome against [S25.1](#s25-1) using its candidate-bound evidence. <a id="f25-1"></a>

#### S25 · Guide selection of a specification after delivery

**S25.1** At the normal edit entry, supply a frozen launch specification allowing seven days and an approved maintained policy allowing thirty days. Ask to update the feature. The draft cites the maintained rule and labels the seven-day value historical. Both source files remain intact. Remove the maintenance decision while keeping two plausible values. The writer identifies the conflict and asks which governs before committing to a value. It can draft unrelated sections. Use the same outputs for story and epic closure. <a id="s25-1"></a>

R21/A21. The skill maintainer owns this outcome. [W43](./tasks.md#w43--guide-selection-of-a-specification-after-delivery)

### F26 · Carry exact field constraints into the implementing Issue

An implementer can recover the exact field constraint from the owning task, including an independently assigned Issue.

**F26.1** Accept the integrated outcome against [S26.1](#s26-1) using its candidate-bound evidence. <a id="f26-1"></a>

#### S26 · Resolve constrained fields in Issue handoffs

**S26.1** Given optional Order.code and required Return.code, write the task for Return.code. Its source points unambiguously to the required field. When reviewing a variant that cites Order.code, locate the wrong field, the affected task and the missing constraint. Reuse the task and review for both verdicts. An unrelated prose edit needs no field reference. <a id="s26-1"></a>

R22/A22. The skill maintainer owns this outcome. [W44](./tasks.md#w44--resolve-constrained-fields-in-issue-handoffs)

### F27 · Resolve the contract shared by separate repositories

As a developer integrating a consumer with a provider, I want to identify the governing contract and supported version, so that a local edit cannot silently change the release agreement.

**F27.1** Accept the integrated outcome against [S27.1](#s27-1) using its candidate-bound evidence. <a id="f27-1"></a>

#### S27 · Document the owner and consumer version of a shared contract

**S27.1** Given an owner contract at v1, a divergent consumer copy and a proposed v2, ask for an Interface Contract (IC) update. It identifies the source revision, pins the consumer to v1, names the discrepancy and directs the proposed change to the owner. The consumer copy is untouched. Provide only the v1 pin and mock results, with no deployed-provider evidence. The handoff distinguishes the agreed version from unknown runtime support. One shared file used by both components requires no synchronized copy. Use the same outputs for story and epic closure. <a id="s27-1"></a>

R23/A23. The skill maintainer owns this outcome. [W45](./tasks.md#w45--document-the-owner-and-consumer-version-of-a-shared-contract)

<a id="f28--keep-existing-users-working-through-the-spec-writer-rename"></a>

### F28 · Keep existing users working through the SpecDev rename

A new user can invoke SpecDev, and an existing Technical Writer installation can reach the same checked writing implementation.

**F28.1** Accept the integrated outcome against [S28.1](#s28-1) using its candidate-bound evidence. <a id="f28-1"></a>

<a id="s28--release-the-spec-writer-identity-and-legacy-entry"></a>

#### S28 · Release SpecDev with a compatible Technical Writer entry

**S28.1** On each supported host, prove the canonical entry and existing legacy invocation resolve to the same writer. Protect an unrelated occupied name. The accepted Builder validates a real document against the canonical release after B5/T50. Retain the candidate, host observation and any failure. <a id="s28-1"></a>

R24/A24. The skill maintainer owns this outcome. [W46](./tasks.md#w46--release-the-spec-writer-identity-and-legacy-entry)

<a id="f29--start-a-checked-feature-in-an-initialized-workflow-project"></a>

### F29 · Open and edit a native change from SpecDev

A developer can use the same writer to edit the intended native OpenSpec artifact in a registered project or to write a standalone document.

**F29.1** Accept the integrated outcome against [S29.1](#s29-1) using its candidate-bound evidence. <a id="f29-1"></a>

<a id="s29--start-one-feature-through-an-optional-workflow-extension"></a>

#### S29 · Connect the privately pinned OpenSpec to a selected change

**S29.1** From the supplied private npm manifest and lock, resolve the exact OpenSpec 2.1.1 executable, identify the intended root and change through native status and instructions, and write or review the native artifact in place. Retain per-host paths, artifact identity and observed content. From the same integration, use an installed operation beyond the core change flow, such as native template resolution for the selected schema, and compare its result with upstream. Repeat setup preserves user edits. A missing or ambiguous required target stops the change operation and leaves ordinary writing usable. <a id="s29-1"></a>

R25/A25. The skill maintainer owns this outcome. [W47](./tasks.md#w47--start-one-feature-through-an-optional-workflow-extension)

<a id="f30--give-the-implementing-agent-the-complete-task-contract"></a>

### F30 · Select native work with its verification

An implementing agent can identify the permitted work, required source and check directly from the selected change’s native task list.

**F30.1** Accept the integrated outcome against [S30.1](#s30-1) using its candidate-bound evidence. <a id="f30-1"></a>

<a id="s30--select-eligible-feature-work-and-recover-its-issue-criteria"></a>

#### S30 · Read the eligible row and its source in the selected change

**S30.1** Give two changes the same local row number. The consumer selects the refund row in the intended change and resolves its governing rule, actor and denial check. Read W40’s native example to identify the first usable outcome, rows 1.1 and 1.2 that can start together and the prerequisite 2.1 for 2.2. An independently assigned Issue is resolved where linked. A stale link holds only its dependent row. Preserve the candidate, selected change, task and readback. <a id="s30-1"></a>

R26/A26. The skill maintainer owns this outcome. [W48](./tasks.md#w48--select-eligible-tasks-from-the-feature-list)

### F31 · Verify and resume one authorized implementation

A developer can hand an approved native task to the selected coding provider and resume its verification against the same criterion.

**F31.1** Accept the integrated outcome against [S31.1](#s31-1) using its candidate-bound evidence. <a id="f31-1"></a>

#### S31 · Verify and resume one authorized implementation

**S31.1** Observe a refund task reach the provider only under implementation authority. Retain the original permission failure, correction, actual candidate, verification result and task identity. After interruption, reconcile the confirmed effects before resuming. Uncertain effects stay open. Confirm archive updates durable specifications only when archive is authorized and acceptance has been demonstrated. <a id="s31-1"></a>

R27/A27. The skill maintainer owns this outcome. [W49](./tasks.md#w49--hand-one-approved-task-to-the-selected-implementation-provider) · [W50](./tasks.md#w50--resume-the-same-task-after-an-interrupted-run)

<a id="f32--route-an-idea-or-bug-to-the-right-upstream-workflow"></a>

### F32 · Choose a suitable record for an idea or defect

A contributor with an uncertain idea can obtain a supported decision or question. A reporter with a bounded defect can obtain one repair task and its expected check.

**F32.1** Accept the integrated outcome against [S32.1](#s32-1) using its candidate-bound evidence. <a id="f32-1"></a>

<a id="s32--route-an-idea-or-bug-to-the-right-upstream-workflow"></a>

#### S32 · Resolve an idea or describe a bounded repair

**S32.1** Given an idea missing a material decision, capture its supported recommendation or focused question. Given a bounded defect, identify the actual failure, repair scope and verification in one task or existing Issue. A writing-only request ends at the resulting record. Retain the observed inputs and outputs. <a id="s32-1"></a>

R28/A28. The skill maintainer owns this outcome. [W51](./tasks.md#w51--end-idea-assessment-at-a-supported-decision) · [W52](./tasks.md#w52--turn-a-reported-defect-into-one-bounded-repair)

### F33 · Maintain a versioned workflow integration

A maintainer can update or remove the private integration while preserving project-authored files and unrelated host configuration.

**F33.1** Accept the integrated outcome against [S33.1](#s33-1) using its candidate-bound evidence. <a id="f33-1"></a>

#### S33 · Distribute and safely update the versioned integration

**S33.1** Starting from the W47 pin and an identified local release, inspect the selected package, exercise a controlled update and recovery, then remove owned installation files. Keep the previous exact pin and lock binding available for recovery. Compare user-edited artifacts and unrelated handlers before and after. Record the actual candidate, package versions, results and any failure. <a id="s33-1"></a>

R29/A29. The skill maintainer owns this outcome. [W53](./tasks.md#w53--distribute-and-safely-update-the-versioned-integration)

<a id="f37--use-the-full-writing-catalog-in-the-optional-workflow"></a>

### F37 · Use supplementary documents when a change needs them

A developer can request an authorable format directly, or use a change’s existing reviewed source when its tasks depend on that source.

**F37.1** Accept the integrated outcome against [S37.1](#s37-1) using its candidate-bound evidence. <a id="f37-1"></a>

<a id="s37--write-the-requested-document-and-pass-it-to-the-right-consumer"></a>

#### S37 · Write a requested document and pass a needed source to its consumer

**S37.1** Request a tutorial from the qualified writer and observe checked delivery without provider dispatch. For a change, review its existing native design in place, respect a selected schema that already defines a specialist artifact, then show the selected task recovers the applicable decision and source. A stale design holds the dependent row. Only an explicitly requested or independently necessary supplementary artifact is produced. Reuse the W58/W59 outputs. <a id="s37-1"></a>

R33/A33. The skill maintainer owns this outcome. [W58](./tasks.md#w58--request-any-supported-writing-format-through-the-workflow) · [W59](./tasks.md#w59--carry-a-reviewed-document-into-a-dependent-task) · [W47](./tasks.md#w47--start-one-feature-through-an-optional-workflow-extension)

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

- **F39.1** Given the candidate’s public capabilities and supported document catalog, follow their index entries from the repository’s `README.md`. Each resolves to usable instructions on a page or at a named section. Aliases and variants may share a destination that covers them. An omitted entry, irrelevant destination or unshipped feature presented as ready fails. Save the candidate revision, coverage comparison and representative destinations. <a id="f39-1"></a>

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
| R9 | SpecDev can author a requested document from verified project facts, sources, authority and decisions. For an OpenSpec change, review or edit the native artifact at its actual path and follow the project schema. Preserve approved versions and flag a consumer-format conflict. Ordinary writing uses the existing format contracts. |
| R10 | Author all seven named artifacts through the normal skill entry on explicit request. Support a complete standalone deliverable when requested and a linked section when sufficient. Each route includes accepted inputs, writing guidance, consumer, representative example and a compatible checked-output path. Use an existing type only when its full contract fits; a named variant may carry distinct structure. SpecDev owns those additional writing forms. |
| R11 | Resolve each declared child story or task to the outcome and criterion from which it derives authority. A native task may reference its governing capability requirement and scenario directly. Add a separate story only where independently needed or required by the project. An independent issue, including a bounded improvement, may carry its source, scope, observable outcome and proof inline. Never reclassify an orphaned child as standalone to bypass the missing parent. |
| R12 | Use reader-appropriate plain language across Markdown and session messages. Name the actor, action and observable consequence where they affect the reader’s decision. Preserve sourced meaning, uncertainty, obligation strength, exact identifiers, numbers and authority. Keep clear prose as written. Match the vocabulary to the owner, implementer or reviewer using the artifact. |
| R13 | Give writers a complete child Issue that can be reached from its story and the Issue guide. Preserve the distinct parent Feature example. |
| R14 | Put portable session instructions for necessary manual actions and misunderstood explanations in one named section of Writing Style (WS). Link the existing procedure guidance and preserve the checked-delivery boundary. |
| R15 | Require the file-based wording check where its predicates or an existing artifact obligation apply. Every message still receives source-grounded editorial review. |
| R16 | In the public `README.md`, show how a request becomes observable behavior, a bounded change and a check. Distinguish an ordinary document, an independent fix and an OpenSpec change. Show readers where to find the governing scenario, the design decision where needed, the task and its proof. Link the owning instructions for conditional documents. |
| R17 | Use the smallest record that preserves scope, authority and proof under the project’s governance. Resolve declared parent criteria. An independently authorized fix may use one Issue. Use the same OpenSpec design structure for standalone and change designs. Add architecture, component, interface, migration or recovery detail only where a decision needs it. Link existing decisions and contracts at their owner. |
| R18 | Use the document type and requested scope to identify material information needed at the checked writing entry. Resolve each applicable topic from evidence or actual authority, or keep it visibly open. Before asking, identify the affected requirement or section, source inspected and the consequence of an answer. Preserve the lightweight route for narrow edits. |
| R19 | Use the single `/specdev` entry or its host-native equivalent, including for `init`. For OpenSpec work, select its native operation or schema first. Use the writer’s format catalog for supplementary or standalone requests. Offer `/prd`, `/lld` and `/task` as explicit opt-ins with their supported host equivalents. The qualified selector or a full document name reaches every authorable type. Preserve the original brief, requested operation, existing host handlers and qualified fallback. Reference guides inform authoring. OpenSpec owns the selected change’s task syntax and progress. |
| R20 | Use OpenSpec’s discovery or next-artifact guidance where available. For standalone writing, offer guided entry, read-only next-document advice and one-document continuation using actual prerequisites and revisions. In one line name the next document, the specific gap and its benefit, or the real blocker or completed endpoint. |
| R21 | For a change to a delivered feature, identify the active source under the project’s maintenance policy and distinguish historic delivery evidence. Resolve a material authority conflict before settling the affected requirement. |
| R22 | For work on a constrained field, link the exact field definition from the native task or its independently owned Issue. Check the receiving task for missing or misattributed constraints. |
| R23 | For independently released providers and consumers, distinguish the authoritative contract revision, the consumer’s supported or pinned version, and the evidence for actual runtime compatibility. |
| R24 | Ship SpecDev with one writing implementation and a compatible legacy entry, after Skill Builder accepts both identities. |
| R25 | Connect SpecDev to OpenSpec using a private, exact npm dependency on `@fission-ai/openspec@2.1.1`. Route all supported upstream capabilities through the installed native operation or CLI. OpenSpec takes precedence on every overlap. Resolve the selected project and change where required and use the actual schema, status and instructions. Read, write and review the native artifacts in place on each supported host. Protect project files and other installations on setup and recovery. |
| R26 | Use the selected change’s native `tasks.md`. Each numbered checkbox describes bounded work and how to verify it. Resolve its governing scenario and any material design, dependency or existing Issue. A separate Issue is warranted for independently owned, externally assigned or project-required work. Maintain each criterion at one owner. |
| R27 | A writing request ends at checked document delivery. For an authorized build, use OpenSpec’s apply instructions and the selected provider. Keep the task, original criterion, candidate and observed result attributable through recovery. Use native archive only within authorized scope after applicable acceptance and verification. |
| R28 | For an OpenSpec discovery or exploration request, use the installed upstream operation. Otherwise use the smallest intake appropriate to the request. A material idea can use a brief or decision record. An observed bounded defect can use one repair task with its check. Resolve substantive uncertainty before undertaking dependent work. |
| R29 | Distribute a versioned SpecDev integration with a private exact OpenSpec npm dependency. Upgrades identify the proposed pin, verify native inputs and project preservation and support recovery to the prior working pin. Remove only owned files. |
| R33 | All authorable document types remain available from SpecDev on explicit request. When an upstream operation or the selected schema owns the requested output, including a specialist type, use its native operation and author or review that artifact in place. Only bring an extra document into a change when requested or when its consumer needs it. Distinguish authorable formats from instructions for writing and review. |
| R34 | Give procedures, references and session replies wording suited to the reader’s decision and the evidence available. |
| R35 | The public index must lead readers directly to usable guidance for every released feature and supported document type. A guide or a named section can satisfy the requirement. Create a separate guide when readers need a distinct procedure or reference. |

## Production order

Choose the route from the request and project.

1. For an ordinary writing request, use the named format, its sources and the requested scope. An already-owned Issue can carry a bounded fix and verification. A discovery interview, brief, product definition, capability map or research record is useful when the next decision needs those facts. The seven authoring cases in A10 are independently available.
2. For an OpenSpec change, use the upstream discovery or exploration operation when it serves the request. Establish the registered project root, selected change and active schema. Read the project’s durable capabilities and current change before proposing a new capability. The native proposal identifies purpose, scope and affected capabilities.
3. Write or review requirements and observable scenarios in the selected capability’s native change spec. Reference a project-owned story or criterion where it already defines the behavior. When the schema expects a design, place the approach and decisions in the change’s `design.md`. Follow the schema’s dependency graph to determine which artifact can proceed.
4. Break the approved behavior into deliverable changes in one native `tasks.md`. Each numbered checkbox includes its verification. Identify the scenario, genuine prerequisites and any external work record needed by the implementer. A writing-only request ends at delivery of the requested artifact.
5. With implementation authority, use the native apply instructions for that change and verify the result on the actual candidate before marking the row complete. Check integrated behavior against its scenario. Archive only when authorized and the applicable checks pass. Reuse the archived change and durable specifications when later work needs their distinct histories.

### Link work to its parent and designs to their sources

The change specification owns requirements and observable scenarios. A native task references the scenario it delivers. For an independently assigned Issue, identify its owner, scope and proof there and reference the Issue from the task. Project governance may require particular parents or records. A directly authorized standalone fix can keep its scope, outcome and check inline. A missing or stale declared parent stops the dependent task. Use existing record IDs or exact sections and bind revisions when authority, compatibility or proof depends on them.

Use one design standard in either route. Start with OpenSpec’s design structure for context, goals and exclusions, decisions with their rationale, and risks or trade-offs. Record migration, recovery or open questions where relevant. Add architectural or component-level details, data contracts and failure cases only where they change an implementer’s decision. Within an OpenSpec change, update the native `design.md`. Outside a change, use the standalone design’s requested location and the same structure. An existing shared architecture, interface contract or decision record can remain the owner of a decision. Link to the relevant section. A separately requested High Level Document (HLD) or Low Level Design (LLD) selects the needed depth and audience.

#### Refund approval

Suppose the refund capability permits only a manager to approve a refund. The design identifies the service that enforces the rule and cites the capability’s manager-only scenario. If a shared architecture already owns that service boundary, link it. A task to enforce employee denial cites the scenario and verifies the employee’s request leaves the refund unapproved. A standalone request for the same component design can start from an authorized interface contract naming the service and rule. The writer uses the same design structure at the requested depth.

### When the writer may ask the owner

Apply R18 at the supported writing entry on either host. Inspect the smallest authoritative input that can settle the issue. Ignore details immaterial to this document. Keep current behavior, required future behavior and design discretion distinguishable.

| Basis | Required behavior |
| --- | --- |
| Observed fact | Cite the applicable code, configuration or other observation at its revision. Write what that evidence establishes. |
| Governing requirement | If the request preserves an existing rule or an applicable standard determines the answer, cite that authority and use it without asking. |
| Delegated choice | Within granted discretion use a fitting project convention or supported practice. Record the rationale when it affects the design. General advice can inform a recommendation. |
| Open decision | Ask only when a material consequence remains outside the writer’s authority. State the unresolved difference, or identify the one missing owner-held fact. Never manufacture alternatives. Continue independent writing; an early draft exposes the open decision and its consequence. |

Python checks applicable coverage, valid source and answer references, and permissible readiness transitions. The supported host workflow asks and receives the actual question and reply. Semantic review determines whether the evidence supports the claim and whether a question was necessary. An unverifiable reply, preselected option or silence cannot confer authority.

<a id="how-upstream-templates-map-to-the-writer"></a>

### Which artifact owns each part of an OpenSpec change?

OpenSpec takes precedence wherever it provides the capability. From SpecDev, use the installed upstream operation or CLI with its own contract. This includes discovery and exploration, writing and reviewing artifacts, built-in verification, update and sync, archive, supported workflows and profiles, and installed custom schemas. For a command request through the qualified entry, resolve the verb or workflow against the installed OpenSpec CLI help and installed skill/profile metadata. A missing local shortcut always triggers this lookup. A matching upstream operation wins even when the local catalog has the same name. A local-only command works when the upstream lookup finds no applicable match. If neither supplies the command, say so and leave state untouched. An unavailable runtime or disabled native workflow is a prerequisite to report, never a reason to reinterpret a requested native command as a writing task. Treat unrecognized input as data, never as a shell command. Preserve its native options, supported outputs and authority boundaries. The writer adds source-grounded wording or specialist detail when it helps. If a custom schema defines a specialist artifact, edit that native artifact in place. The integration must preserve access to the complete installed upstream surface without maintaining another command list, schema copy or workflow engine.

The selected project’s OpenSpec schema determines each native artifact’s path, prerequisites and structure. For the default `spec-driven` schema, paths in the first four rows are relative to `openspec/changes/<change>/`. Use SpecDev’s writing and review guidance on the files the project already consumes. [Pinned OpenSpec package](https://www.npmjs.com/package/@fission-ai/openspec/v/2.1.1)

| Artifact | What the reader uses it for |
| --- | --- |
| `proposal.md` | Identify the reason for the change, its scope and affected capabilities. Reuse the names of existing capabilities when they govern the behavior. |
| `specs/<capability>/spec.md` | Review changed requirements and their observable scenarios. Keep permission, failure behavior and exclusions with the requirement they qualify. Use the native delta structure. |
| `design.md` | Record how to implement the change and why the design fits its constraints. Use the single [design standard](#link-work-to-its-parent-and-designs-to-their-sources) at the depth the change needs. Follow the active schema’s prerequisites. |
| `tasks.md` | See bounded work, its dependency and verification, and which checkboxes remain open. An existing independently owned Issue can supply its own task detail by reference. |
| `openspec/specs/<capability>/spec.md` | Read the durable capability after authorized archive. The archived proposal, change spec, design and task list preserve the change history. |

<a id="feature-task-lists-and-issue-acceptance"></a>

### Native tasks and separately owned Issues

Use one native task list for an OpenSpec change. Put the action and the smallest check that establishes completion in the same checkbox. Reference the scenario, design decision or contract needed to act. When a distinct team owns an Issue, another party is assigned the work, or the project requires a tracker record, link that Issue and its criterion. Reuse an existing Issue and keep independently maintained task acceptance there. Ordinary substeps share their task. A standalone fix can use a single existing Issue or bounded task.

#### When to write and read `tasks.md`

Read `openspec status --change <change> --json` and `openspec instructions <artifact-id> --change <change> --json` for the selected project. Follow the returned dependencies, paths and instructions. A writer can review an existing artifact at its path or edit just the requested content. If project resolution, change selection or a required provider fails, identify the failed boundary and stop the affected operation. A direct document request remains available without OpenSpec.

Use native validation and the applicable upstream review or verify operation first. Reuse its evidence for the aspects it covers. SpecDev adds semantic judgment only where source meaning, authority or writing quality still needs assessment. Actual product behavior requires an observation at the relevant consumer. For authorized implementation, the provider consumes the native apply instructions and actual context files, selects an eligible row, runs its check and records observed evidence. A checkbox records progress. The task result needs evidence on the candidate, and a story needs its observable outcome. Mark a stale dependency and continue other eligible work where authorized.

#### Refund status and filtering

Suppose support staff can already read the recorded refund decision through an API. The change adds dashboard and CLI views, then decision filtering. The capability spec owns the scenarios for showing the stored value and returning only matching refunds. The native task list can read as follows.

```markdown
## 1. Show the recorded decision

- [ ] 1.1 Show the stored decision in the dashboard. Check a known denied refund against the recorded value.
- [ ] 1.2 Show the same field in the CLI. Check the same refund against the API response.

## 2. Filter refunds by decision

- [ ] 2.1 Filter the API results by decision. Request denied refunds from mixed input and verify that every result is denied.
- [ ] 2.2 Connect the dashboard to the verified API filter from 2.1. Select Denied and verify that the view shows only denied refunds.
```

Rows 1.1 and 1.2 can start together when their interfaces and edit boundaries are settled. Together their observed results demonstrate the first usable capability. Row 2.2 waits for the API result from 2.1. If an API team already owns Issue #83, row 2.1 can point to #83 and its criterion, then verify that the referenced result applies to this change. Keep the detailed criterion and evidence with that Issue.

<a id="how-the-optional-workflow-uses-the-full-catalog"></a>

### Request a document by name

Use the qualified SpecDev entry or the document’s full name for any authorable format. SpecDev offers three opt-in writing shortcuts, `/prd`, `/lld` and `/task`, with their supported host equivalents. The choice leaves all installed native OpenSpec operations available. Each forwards the original brief to the same writer. Writing Style (WS), Visual Guidance (VG) and the other reference-only guides inform the output. A request to author a Tutorial (TUT) or How-to Guide (HTG) still selects its authorable format. Derive the distinction from the [format catalog](../SKILL.md) and [output contracts](../contracts/documents.json).

A tutorial, design, Issue or other requested document may be the complete result. A change reuses a related artifact or links an existing supplementary document when a real dependency warrants it. If the user asks for a native proposal, spec, design or task list, review or edit that native file in place. Do not generate companion documents, exports or additional host aliases as part of an ordinary change.

### Find features and document types from the public index

Link the public index from the repository’s `README.md`. Cover the released user-facing capabilities and supported document catalog, including standalone writing, discovery, editing, review, rewriting, visuals, checked delivery, documented maintenance operations, shortcuts, guided handoffs and each shipped optional workflow. Aliases, command spellings and small variants can share guidance when readers can identify the behavior that applies to their request.

Link to the page or specific heading that explains when to use the feature or format, what to provide and what result to expect. For instance, the focused-edit and review entries can point to different headings in the same `README.md`. An Issue variant can point to the section that explains its fields. Give readers a separate guide when they need a distinct procedure or reference. Include prerequisites, recovery or the next action where these affect the reader’s task.

The task that releases or changes a feature owns the guidance and its direct index link in the same increment. As examples, W35 owns shortcuts, W38 owns next-document guidance, W47 owns project-aware writing, W49–W50 own execution and resumption, and W51 and W52 own assessment and repair respectively. The owner of each A10a–g route makes its instructions findable from the index. W54 establishes the public entry. W61 covers already released features and supported types with missing or inadequate index destinations. Describe the released native operations at their upstream owner. Additional guides or demonstrations retain their own scope and approval status.

## Quality and interface constraints

For native changes use the active OpenSpec instructions. For supplementary or standalone writing, use the appropriate document reference and checked output contract. Preserve verified project terminology, literal IDs and applicable native tracker metadata. Allow exact sections for projects without stable IDs and keep small self-contained work inline. For externally consumed data or output text, identify callers and compatibility before changing the contract. An existing approved document or delivery receipt must remain auditable under the version that produced it. The writer can recommend a scope change. Only the authorised decision-maker may adopt it.

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
| A9 · R9 | Give the writer Mirai facts, stable IDs, an open approval and no prior document or application template. Request a complete Product Requirements Document (PRD) and one linked behavioral specification. Give it a second project’s facts and request a new product document through the same entry. | The writer produces each whole artifact using its own type contract. Project facts stay attributable, unresolved choices stay open, and the downstream requirement resolves to its source. A misleading legacy heading cannot replace the writer’s template. A consumer conflict identifies the incompatible field and owner. | Inspect the actual documents, normal writing checks, source links, decision status and version-bound evidence. Reuse the first product document across both tasks. Record document acceptance separately from application ingestion. |

### Seven authoring cases and hierarchy acceptance

Each A10 case starts with source facts and a request for the named artifact through SpecDev. Keep the actual output, its checked document/version binding and the downstream observation. One linked example set can supply all seven cases. A heading check alone is insufficient.

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

**A16 · R16.** From the public `README.md`, choose the entry for an idea, a native change or an independent broken-link fix. Locate an agreed requirement, its task and the planned proof, including WEB-06 and failure check T10 in the worked example. For the native change, identify where its scenario, applicable design and task verification live, when writing stops and how authorized apply selects another eligible row. For the independent fix, use its existing work record. A missing declared parent blocks dependent work. Retain the reader’s choices, passage and resolved links. Check the A10 formats are discoverable on individual request.

**A17 · R17.** Use the same improvement in three contexts. An independently authorized small change with inline scope and proof can ship in one Issue. A contribution assigned to a story must resolve that story and criterion. A directly authorized user outcome may be written as a standalone story if its value, boundary and proof are clear. Then compare two deliveries for the same feature. A single, bounded delivery can keep its steps inline. A migration requiring the old and new readers to coexist needs rollout order, compatibility evidence and recovery before the dependent switch. A project-mandated parent or planning step remains binding. Retain the selected records, governing input and reason at the first point where the choice differs. Reuse A11 for the broken-parent case and A16 to assess whether readers can find it from `README.md`.

**A17b · R17.** For the refund change, review or edit the one native design in place. Identify the service that enforces manager-only approval, its governing source and the planned employee-denial check. Request a standalone component design using only an authorized contract that provides the same inputs. It uses the same design structure at the depth needed. A duplicate design, invented parent, unresolved governing rule taken as settled or mandatory duplicate backlink fails. Reuse A11 for a declared child with a missing parent. W62 owns both cases.

**A18 · R18.** Use the two export requests with the same current staff-only route and compare the actual documents and public questions. (a) “Add CSV to the existing download; only the format changes” produces zero permission questions and preserves existing access. (b) “Let customers download their own reports,” with individual versus organization ownership unresolved, produces exactly one targeted ownership question before the dependent requirement becomes ready. Silence leaves the ownership open in a draft. A genuine answer bound to that question unblocks only the supported permission. Omitting the material topic blocks readiness. A cited passage saying permission is undecided cannot justify an administrator-only rule. Reuse those passages and verdicts for the negative cases. Check one missing owner-held fact without invented options, one delegated routine choice without an interview, a lightweight story or Issue, and the narrow-edit exception only where existing evidence is insufficient. Preserve historical receipts. Host-specific claims require an observed exchange on that host.

**A19 · R19.** On the actual supported hosts, enable only the three opt-in shortcuts for product requirements, detailed design and one task. Preserve the original brief. Confirm each shortcut maps to the same owner as the qualified selector, and retain one checked output per host. Exercise a name collision, repeat installation and owned-only removal. The qualified writer reaches other authorable types by selector or full name without installing additional global aliases. Reference-only guides stay out of the authorable catalog. A writing review returns located findings on the selected artifact.

For W40, use the [native refund example](#refund-status-and-filtering). Recover the first usable story, its two independent views and the API dependency for filtering. Verify every checkbox states how to check completion. A row can verify the relevant result of a linked, independently owned Issue without copying its criterion. An independent fix stays in its existing record. Duplicate editable criteria, an extra task file as a prerequisite, a missing governing criterion or automatically exporting tasks to a tracker fail.

**A20 · R20.** Given a reviewed change, a blocked decision and a completed standalone fix, next-step advice identifies one useful successor, the actual blocker or completion. Use the native status and instructions for a change. The recommendation writes nothing. When asked to continue one document, produce that document and retain its source binding. Repeating the request after resumption reuses the result. A changed source reopens only affected work. After a writing-only delivery, stop. One independent task can use an Issue.

### Acceptance for maintained specifications, fields and shared contracts

Use the same task evidence at the requirement, story and epic when it proves their outcomes. Both hosts use these criteria.

- **A21 · R21 (F25, W43).** Reuse [S25.1](#s25-1). Preserve both source identities, the retained historical value, the governing reviewed rule and the observed behavior when its authority is unclear. In an OpenSpec project distinguish durable capability specs from the archived change that introduced an earlier value.
- **A22 · R22 (F26, W44).** Reuse [S26.1](#s26-1). Retain the located field reference, authored task, review excerpt and unchanged source definitions. Reuse that task at W40/W41 where it provides the same proof.
- **A23 · R23 (F27, W45).** Reuse [S27.1](#s27-1). Retain the contract owner and revision, consumer pin, divergent copy, proposed change and observed compatibility statement. A local mock alone leaves deployed-provider support unknown.

**A24 · R24.** Reuse W46 and [S28.1](#s28-1). Bind existing installations and receipts to the identity that produced them. An unreleased working name creates no alias requirement.

**A25 · R25.** Reuse W47 and [S29.1](#s29-1). The supplied private manifest and lock resolve `@fission-ai/openspec@2.1.1`. From a fresh selected project, invoke `/specdev init` or its host equivalent. Observe native initialization at that root with `--tools none` for a SpecDev-only setup. Explicit supported tool selections and flags reach upstream. Preserve unrelated handlers and existing project content on repeat initialization. The result creates project setup only, with no separate global `/init` command, feature creation or apply. Native JSON status and artifact instructions identify the registered root’s change, expected output and dependencies. Observe each supported host’s writer use the same native file. Protect other changes and require a settled target before a project edit. Reuse the installed command inspection and invoke one supported non-core operation through SpecDev. For example, `openspec templates --schema <name> --json` returns the upstream resolved template paths. A hand-maintained subset that hides a supported operation fails.

**A26 · R26.** Reuse W48 and [S30.1](#s30-1). Give the actual consumer W40’s `tasks.md` and native change context. Verify it can recover scope, criterion and expected proof from a native row without a second record and from a row referencing an independently owned Issue. Identical row numbers in another change and a stale criterion cannot redirect dispatch.

**A27 · R27.** Reuse W49/W50 and [S31.1](#s31-1). Preserve the earlier failure, the actual corrected result and same-task recovery. Record the separate outcomes for native structural validation, semantic review and observed product behavior. An unchecked product criterion remains open regardless of the native validator’s result. Scope every native operation to the user’s request. A writing request stops before apply or archive. Resolve uncertain effects before any retry.

**A28 · R28.** Reuse W51/W52 and [S32.1](#s32-1). Compare the idea decision with the repair record and its actual input. Neither route adds routine intake documents or initiates coding from a writing request.

**A29 · R29.** Reuse W53 and [S33.1](#s33-1). Record the exact current and candidate dependency, resolved executable and native-contract comparison. A rejected update preserves or restores the known working install, project-authored files and existing host entries.

**A33 · R33.** Reuse W58/W59 and [S37.1](#s37-1). Map authorable formats and aliases, including the seven A10 forms as they ship, through the qualified writer. Apply reference-only writing guides as guidance. Observe the direct tutorial stop and a native design constraint reach its dependent task on the same change. A format in the catalog creates no requirement to produce it in every change.

**A34 · R34.** F38/S38/W60. Use the [committed guide](https://github.com/fatonsopa/ai-technical-writer/blob/d8bf859f0eec178aa34b24e29aef10290e984c3b/references/writing_style.md#write-a-feature-page-people-can-use) and its worked case. The feature example identifies the action and source. The session identifies the reviewed approval rule and the unresolved decision.

**A35 · R35.** F39/S39/W54/W61. Compare the release’s public features and supported document types with the index. Each entry opens on guidance that explains when to use it, its input and expected result. A direct link to a useful section passes, including one shared by variants it covers. For focused editing and review, the respective destinations must distinguish a bounded change from findings. An omitted entry, broken anchor, unrelated section, empty stub or general overview that leaves the reader searching fails. Reuse the candidate and link observations from the owning tasks.

## Open decisions

**D7.** Revision 21 replaces the previously selected integration with the privately installed OpenSpec npm dependency at exact version 2.1.1. Use its native artifact instructions, validation, apply context and archive behavior. The handoff supplies the private npm manifest and lock at `tools/openspec/`. W47 demonstrates the first usable connection. W53 owns upgrade and recovery.

**D6.** Use the writing and execution boundaries in [Production order](#production-order). The former upstream workflow, its phase gates and its convergence command are superseded. Applicable project reviews and requested broader reviews retain their original authority.

**D5.** The selected public identity is **SpecDev** (`specdev`), with compatibility for the deployed `technical-writer` entry. Unreleased planning names require no runtime aliases. Claude implements the rename on the handoff computer after B5/T50. The repository and clone URL stay the same.

**D4.** F25–F27 remain approved under R21–R23 for governing specifications, field constraints and cross-repository contracts.

**D3.** R19–R20 cover three opt-in host shortcuts, qualified selection for other authorable formats, and one grounded next-document recommendation. Use the [native artifact map](#how-upstream-templates-map-to-the-writer) for project changes.

**D2.** The owner approved R18/A18 and its bounded implementation in F22.

**D1.** The owner approved the original revision 6 scope, including the conditional hierarchy, first-use naming convention and reviewed-delivery sentence. A user may name a document by acronym or full name at any turn. In ordinary authored prose, introduce the full name with its acronym and use the acronym when clear thereafter. Preserve contractual labels, literals and quotations. A checked handoff may include one useful result or open decision from reviewed content. Bind that sentence to the same reviewed version and keep older receipts verifiable.

## Related design and work

The [scenarios](#scenarios) own this handoff’s stories and acceptance. The [implementation plan](./implementation-plan.md) owns delivery dependencies. Existing W records in the [task list](./tasks.md) retain their approved identities, scope, criteria and evidence. Their presence in this maintained packet creates no requirement to generate a separate Issue for each native change task. The [handoff test specification](./test.md) defines the reader and eventual implementation checks. Use W40’s representative native change list at its W48 consumer. Record a later material change at its established authority and update the affected criterion.

## Proposals awaiting owner approval

F34–F36 (W55–W57) and W51.3 were proposals in revision 20. They have no execution authority. The previous upstream-specific mechanisms are superseded. The approved W54/W61 index and W51.1–W51.2 intake work retain their existing scope. [Historical proposals in revision 20](https://github.com/fatonsopa/ai-technical-writer/blob/8742dce257d21113ed3db3b6e70f6c001253fecc/plan/specification.md#proposals-awaiting-owner-approval)

<a id="default-feature-route-and-its-outputs"></a>
<a id="capability-reference-and-artifact-inventory"></a>
<a id="idea-assessment-in-workflow-mode"></a>
<a id="proposed-story-records"></a>

| Proposed records | Historical scope |
| --- | --- |
| R30/A30 · <a id="f34--find-a-capability-and-follow-a-feature-from-request-to-evidence"></a><a id="f34-1"></a><a id="s34--find-a-capability-and-follow-a-feature-from-request-to-evidence"></a><a id="s34-1"></a>F34.1/S34.1 · W55 | An additional public walkthrough from the capability index to a complete feature example. |
| R31/A31 · <a id="f35--inspect-what-the-installed-integration-exposes"></a><a id="f35-1"></a><a id="s35--inspect-what-the-installed-integration-exposes"></a><a id="s35-1"></a>F35.1/S35.1 · W56 | A separate installed-artifact inventory guide and override demonstration for the former integration. |
| R32/A32 · <a id="f36--document-an-on-request-convergence-review-after-the-upstream-workflow"></a><a id="f36-1"></a><a id="s36--document-an-on-request-convergence-review-after-the-upstream-workflow"></a><a id="s36-1"></a>F36.1/S36.1 · W57 | A separate guide and demonstration of the former integration’s convergence command. |
| W51.3 | A longer idea-assessment demonstration. The approved intake uses the request’s evidence and the smallest adequate record. |
