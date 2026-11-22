# Spec-driven authoring · [Design](../../design.md) · [Tasks](../../tasks.md) · [Audit](../../../../../plan/audit.md) · [Handoff checks](../../../../../plan/test.md)

## Purpose

SpecDev helps project teams write, review and deliver source-grounded documents and native OpenSpec changes through one entry, with clear ownership of requirements, work and observed results.

## ADDED Requirements

### Requirement: R1 · Literal values and document names

SpecDev SHALL preserve meaning, obligation strength, exact literals and project vocabulary on every writing surface. Accept the full document name or its acronym in any user request, including the first mention. In authored prose introduce the full name and acronym once, then use the acronym where clear. Preserve project-required labels.

#### Scenario: Edit a literal and a document reference together (A1, F1.1, S01.1)

<a id="specdev-improvement-specification"></a><a id="spec-writer-improvement-specification"></a><a id="purpose-and-scope"></a><a id="scenarios"></a><a id="f1--preserve-the-projects-literal-identifiers"></a><a id="acceptance-criteria"></a><a id="f1-1"></a><a id="scope-and-sources"></a><a id="s01--edit-a-mixed-passage-without-corrupting-its-fixture"></a><a id="acceptance-criteria-1"></a><a id="s01-1"></a><a id="scope-and-sources-1"></a><a id="requirements-and-business-rules"></a>

- **WHEN** a request names a document by its full name or acronym, including on first mention, and the passage contains the `US` fixture key, quoted bytes and a genuine document label
- **THEN** the edit preserves the key, quote, required labels and project vocabulary. The real reference uses the agreed first-use convention and a valid alternative phrasing remains eligible. The consuming rule still yields `__test_wrs-us.co.uk` from the same row; retain the passage, row and derived value.

### Requirement: R2 · Proportionate records for product decisions

SpecDev SHALL choose the smallest document or native record suited to the decision. Support a shaping brief and an epic view as variants. Assign one owner to each requirement even when the project assigns that role to a differently named document.

#### Scenario: Choose a record for the decision (A2)

- **WHEN** a small self-contained fix, an unresolved opportunity and an approved multi-slice initiative with native parent tracking each need a work record
- **THEN** the fix stays inline, the brief describes the beneficiary, observed problem, outcome, exclusion and uncertainty, and the parent view identifies the integrated outcome, dependencies and proof. Each requirement has one owner. An appetite, budget, target or assignee appears only where its source grants that authority.

### Requirement: R3 · Source, constraint and work traceability

For material multi-document work, SpecDev SHALL identify the owning source, stable criterion or exact section, consuming work and expected proof. Bind the source revision when approval, compatibility, verification or project governance depends on it. Identify uncovered requirements, unjustified work, unresolved citations and altered conditions. Record only genuine dependencies.

#### Scenario: Trace a work packet in both directions (A3, F2.1, S02.1)

<a id="definitions"></a><a id="f2--trace-assigned-work-back-to-its-real-source"></a><a id="acceptance-criteria-2"></a><a id="f2-1"></a><a id="scope-and-sources-2"></a><a id="s02--commission-a-task-from-a-reviewed-requirement"></a><a id="acceptance-criteria-3"></a><a id="s02-1"></a><a id="scope-and-sources-3"></a>

- **WHEN** an implementer receives a reviewed feature packet without the authoring conversation
- **THEN** they can trace the requirement, revision, parent outcome, bounded task, criterion, expected proof and review verdict in either direction. Review locates the exact broken edge and consequence when an owner or citation is missing, a real criterion is weakened, an ID is invented or unrelated work cites a real ID. A justified safeguard and an independent authorized fix remain eligible. Retain the packet and affected comparisons.

#### Scenario: Distinguish the actual result of a critical journey (F3.1, S03.1)

<a id="f3--prove-behavior-at-the-surface-the-user-reaches"></a><a id="acceptance-criteria-4"></a><a id="f3-1"></a><a id="scope-and-sources-4"></a><a id="s03--verify-one-critical-journey-against-its-source"></a><a id="acceptance-criteria-5"></a><a id="s03-1"></a><a id="scope-and-sources-5"></a>

- **WHEN** a verifier follows a mapped surface through the written critical journey to the requirement and its check
- **THEN** each step resolves to a real surface. The case identifies the supported entry, visible result, authoritative effect and closest false positive. Reaching the wrong result fails; an unresolved underlying effect stays unknown. The linked case distinguishes expected and observed behavior.

### Requirement: R4 · Evidence in approval decisions

SpecDev SHALL derive an approval opening from the detailed evidence. It must communicate who is affected, what changes, what is excluded and the actual choice or absence of an outstanding choice. Include material cost, uncertainty or risks when sourced.

#### Scenario: Read the decision from the opening (A4, F4.1, S04.1)

<a id="f4--make-the-approval-decision-intelligible-from-its-opening"></a><a id="acceptance-criteria-6"></a><a id="f4-1"></a><a id="scope-and-sources-6"></a><a id="s04--distinguish-a-prototype-from-approval-to-include-it"></a><a id="acceptance-criteria-7"></a><a id="s04-1"></a><a id="scope-and-sources-7"></a>

- **WHEN** an independent reader sees only the proposed approval opening for a prototype, with a material exclusion and an unresolved choice
- **THEN** they can identify the beneficiary, change, exclusion, what the prototype demonstrated and what the owner still has to decide. Each answer agrees with both the opening and its source. A real quotation attached to the wrong conclusion fails. Use the two texts and reader response for this representative case.

### Requirement: R5 · Evidence-led discovery

SpecDev SHALL inspect available facts before asking. Ask about decisions that change the outcome, group only independent choices, and preserve unresolved authority. Stop when the available input settles the writing task.

#### Scenario: Ask only the question that changes the next requirement (A5, F6.1, S06.1)

<a id="f6--ground-discovery-and-research-in-actual-evidence"></a><a id="acceptance-criteria-10"></a><a id="f6-1"></a><a id="scope-and-sources-10"></a><a id="s06--carry-discovery-evidence-into-the-next-authoring-decision"></a><a id="acceptance-criteria-11"></a><a id="s06-1"></a><a id="scope-and-sources-11"></a>

- **WHEN** a request leaves a material choice open and a second request supplies authoritative evidence for the same choice
- **THEN** the first public question identifies the relevant unknown. The actual owner’s answer determines the dependent criterion within their authority. In the settled case the writer proceeds. Silence and unknown targets stay unresolved. Retain the exchange and resulting criterion when this distinction is assessed.

### Requirement: R6 · Truthful session messages and checked delivery

SpecDev SHALL tailor the session response to progress, a decision, a blocker, or delivery. Every material claim in a checked delivery must be attributable to the exact reviewed content or an observed check.

#### Scenario: State progress, decisions and reviewed results (A6, F7.1, S07.1)

<a id="f7--speak-plainly-about-results-blockers-and-decisions-in-the-session"></a><a id="acceptance-criteria-12"></a><a id="f7-1"></a><a id="scope-and-sources-12"></a><a id="s07--receive-the-right-next-action-and-a-checked-result"></a><a id="acceptance-criteria-13"></a><a id="s07-1"></a><a id="scope-and-sources-13"></a>

- **WHEN** a session has a confirmed intermediate result, needs an owner choice, reaches an external blocker or delivers a checked document
- **THEN** the reply states the relevant observation, choice or last confirmed boundary and necessary action. A checked delivery identifies the reviewed file, version and status and may carry one useful decision or open question from those exact bytes. Altering the decision sentence fails verification, the prior receipt stays verifiable, and delivery with no owner action ends there.

### Requirement: R7 · Portable host behavior

SpecDev SHALL expose one portable writing contract. Route optional references by reader need and preserve existing supported invocation names and aliases. Demonstrate the changed behavior on both declared hosts before claiming it works on both.

#### Scenario: Use the normal writing entry on both declared hosts (A7, F8.1, S08.1)

<a id="f8--reach-the-right-guidance-from-an-ordinary-request"></a><a id="acceptance-criteria-14"></a><a id="f8-1"></a><a id="scope-and-sources-14"></a><a id="s08--follow-the-portable-entry-without-grader-hints"></a><a id="acceptance-criteria-15"></a><a id="s08-1"></a><a id="scope-and-sources-15"></a><a id="quality-and-interface-constraints"></a><a id="acceptance-criteria-48"></a>

- **WHEN** Codex and Claude Code each receive an ordinary small edit and a connected handoff without expected guide names or grader answers
- **THEN** each host selects the relevant guidance, respects scope and literal meaning, and delivers assessable output through its supported entry. Record the actual inputs, routing or its evidence limit, received output, host, candidate and available model/settings. A host claim remains Not demonstrated when its evidence is missing. Reuse applicable evidence for unchanged behavior.

### Requirement: R8 · Candidate-bound acceptance and recovery

SpecDev SHALL distinguish implementation, verification and acceptance. Preserve previous evidence, failures and approvals when a source or candidate changes. Mark each affected criterion Met, Failed or Not demonstrated against its actual candidate.

#### Scenario: Retain applicable acceptance when an input changes (A8)

- **WHEN** an upstream source changes after a downstream review and the record contains one unaffected criterion and an earlier failure
- **THEN** only dependent acceptance reopens. Unaffected evidence retains its original identity and scope, the historical failure remains available, and each verdict names the actual candidate. A task count cannot close an unobserved story or feature.

#### Scenario: Retain decision authority when reusing historical material

<a id="open-decisions"></a><a id="proposals-awaiting-owner-approval"></a><a id="default-feature-route-and-its-outputs"></a><a id="capability-reference-and-artifact-inventory"></a><a id="idea-assessment-in-workflow-mode"></a><a id="proposed-story-records"></a><a id="f34--find-a-capability-and-follow-a-feature-from-request-to-evidence"></a><a id="f34-1"></a><a id="s34--find-a-capability-and-follow-a-feature-from-request-to-evidence"></a><a id="s34-1"></a><a id="f35--inspect-what-the-installed-integration-exposes"></a><a id="f35-1"></a><a id="s35--inspect-what-the-installed-integration-exposes"></a><a id="s35-1"></a><a id="f36--document-an-on-request-convergence-review-after-the-upstream-workflow"></a><a id="f36-1"></a><a id="s36--document-an-on-request-convergence-review-after-the-upstream-workflow"></a><a id="s36-1"></a>

- **WHEN** an implementer encounters earlier decisions or proposed work while selecting a task
- **THEN** D1 preserves literal and first-use naming and the optional version-bound delivery sentence. D2 covers the bounded discovery change; D3 covers opt-in shortcuts and grounded next advice; D4 covers source, field and contract ownership. D5 names SpecDev with deployed legacy compatibility. D6 preserves writing/implementation authority and existing project reviews. D7 selects the private pinned OpenSpec integration. Remote publication, deployment, external tracker writes and changes in product scope require separate authority. F34.1/S34.1 (R30/A30, W55), F35.1/S35.1 (R31/A31, W56), F36.1/S36.1 (R32/A32, W57) and W51.3 remain unapproved. Historical proposals for an extra walkthrough, installed-artifact inventory, convergence demonstration or longer assessment do not authorize execution. W51.1–W51.2 and the approved W54/W61 index retain their scope.

### Requirement: R9 · Project-independent document authoring

SpecDev SHALL author requested documents from project facts, sources and actual decisions. For an OpenSpec change the active native schema owns the artifact, its path and its structure. Standalone writing uses the applicable format contract. Preserve approved versions and identify consumer-format conflicts.

#### Scenario: Author from project facts without an application template (A9, F9.1, S09.1)

<a id="f9--author-complete-documents-independently-of-the-application"></a><a id="acceptance-criteria-16"></a><a id="f9-1"></a><a id="scope-and-sources-16"></a><a id="s09--create-a-projects-first-governed-documents-from-facts"></a><a id="acceptance-criteria-17"></a><a id="s09-1"></a><a id="scope-and-sources-17"></a>

- **WHEN** Mirai supplies facts, stable IDs and an unresolved decision but no product document, and a second project supplies its own facts
- **THEN** the ordinary writer produces a complete Product Requirements Document (PRD) and linked behavior specification for Mirai and a second complete product document for the other project. The downstream criterion resolves to its source, pending authority remains open and a conflicting consumer field identifies its owner. A legacy heading cannot displace the relevant format. Acceptance of the document does not establish application ingestion.

### Requirement: R10 · Requested supporting documents and their consumers

SpecDev SHALL author all seven named artifacts through the normal skill entry on explicit request. Support a complete standalone deliverable when requested and a linked section when sufficient. Each route includes accepted inputs, writing guidance, consumer, representative example and a compatible checked-output path. Use an existing type only when its full contract fits; a named variant may carry distinct structure. SpecDev owns those additional writing forms.

#### Scenario: Hand an interview to the product author (A10a, F14.1, S14.1)

<a id="f14--read-the-owners-interview-answers"></a><a id="acceptance-criteria-26"></a><a id="f14-1"></a><a id="scope-and-sources-26"></a><a id="s14--use-the-discovery-interview-record-at-its-handoff"></a><a id="acceptance-criteria-27"></a><a id="s14-1"></a><a id="scope-and-sources-27"></a><a id="seven-authoring-cases-and-hierarchy-acceptance"></a>

- **WHEN** stakeholder answers affect intent or scope and the user requests an interview record
- **THEN** the next author can distinguish the question, its source, the owner’s answer, unresolved choice, restatement and actual confirmation from suggestions. Silence leaves the restatement open.

#### Scenario: Decide whether to define an opportunity (A10b, F5.1, S05.1)

<a id="f5--write-a-brief-for-a-product-decision"></a><a id="acceptance-criteria-8"></a><a id="f5-1"></a><a id="scope-and-sources-8"></a><a id="s05--decide-whether-an-opportunity-warrants-product-definition"></a><a id="acceptance-criteria-9"></a><a id="s05-1"></a><a id="scope-and-sources-9"></a>

- **WHEN** a product owner requests a shaping brief from observed opportunity evidence or an interview
- **THEN** the brief identifies the affected person, problem, desired outcome, exclusions, unknown baseline and any owner-supplied appetite. A reader can decide whether to proceed without the original conversation. Inventing a budget, baseline or target fails.

#### Scenario: Select an independently deliverable capability (A10c, F15.1, S15.1)

<a id="f15--select-the-capability-to-specify-next"></a><a id="acceptance-criteria-28"></a><a id="f15-1"></a><a id="scope-and-sources-28"></a><a id="s15--use-the-capability-map-at-its-handoff"></a><a id="acceptance-criteria-29"></a><a id="s15-1"></a><a id="scope-and-sources-29"></a>

- **WHEN** an initiative has several independently deliverable outcomes and its capability map is requested
- **THEN** the map identifies stable capability IDs, responsibilities, actual dependencies and reasons for order. The spec author can select the intended capability, parallelize independent work and identify a cycle needing resolution.

#### Scenario: Use research at a design decision (A10d, F16.1, S16.1)

<a id="f16--use-research-to-resolve-a-design-question"></a><a id="acceptance-criteria-30"></a><a id="f16-1"></a><a id="scope-and-sources-30"></a><a id="s16--use-the-research-record-at-its-handoff"></a><a id="acceptance-criteria-31"></a><a id="s16-1"></a><a id="scope-and-sources-31"></a>

- **WHEN** a design depends on an unanswered question and research is requested
- **THEN** the record states the question, sources, findings, uncertainty, supported recommendation and who has approved or still owns the decision. A designer can cite the relevant finding. A study or working prototype alone confers no approval.

#### Scenario: Locate a user-facing surface (A10e, F17.1, S17.1)

<a id="f17--locate-the-feature-from-its-map"></a><a id="acceptance-criteria-32"></a><a id="f17-1"></a><a id="scope-and-sources-32"></a><a id="s17--use-the-feature-map-at-its-handoff"></a><a id="acceptance-criteria-33"></a><a id="s17-1"></a><a id="scope-and-sources-33"></a>

- **WHEN** a verifier receives a feature map for observed and proposed surfaces
- **THEN** each observed surface has a user-facing name, entry or route, verifiable control or handle, source revision and observable end state. Proposed surfaces are marked. The verifier can locate the entry; a guessed handle or an app launch does not establish that they reached it.

#### Scenario: Follow a risk to its journey and proof (A10f, F18.1, S18.1)

<a id="f18--follow-the-critical-journey-to-its-observable-result"></a><a id="acceptance-criteria-34"></a><a id="f18-1"></a><a id="scope-and-sources-34"></a><a id="s18--use-the-critical-journeys-at-its-handoff"></a><a id="acceptance-criteria-35"></a><a id="s18-1"></a><a id="scope-and-sources-35"></a>

- **WHEN** a mapped surface and a sourced risk are supplied for a critical journey
- **THEN** the result identifies the journey, actor, ordered steps, observable end state, significance, source and test reference or explicit gap. The verifier can find the named surface and check. An unknown screen or unrun test stays unverified.

#### Scenario: Check whether a requirement is ready (A10g, F19.1, S19.1)

<a id="f19--decide-whether-a-requirement-is-ready"></a><a id="acceptance-criteria-36"></a><a id="f19-1"></a><a id="scope-and-sources-36"></a><a id="s19--use-the-requirements-quality-checklist-at-its-handoff"></a><a id="acceptance-criteria-37"></a><a id="s19-1"></a><a id="scope-and-sources-37"></a>

- **WHEN** a candidate specification exists and its requirements need a quality review
- **THEN** the checklist identifies the revision, criterion, relevant quality question, located evidence, verdict and unresolved correction. The implementer can determine whether scope, permission and observable proof are settled. A review checkbox does not prove runtime behavior. For the seven requested formats, one linked example set may supply each checked output and its actual consumer observation.

### Requirement: R11 · Authority for child and independent work

SpecDev SHALL resolve each declared child story or task to the outcome and criterion from which it derives authority. A native task may reference its governing capability requirement and scenario directly. Add a separate story only where independently needed or required by the project. An independent task, including a bounded improvement, may carry its source, scope, observable outcome and proof inline. Never reclassify an orphaned child as standalone to bypass the missing parent.

#### Scenario: Resolve a declared child without manufacturing parents (A11)

- **WHEN** a governed feature commissions a child story and a task, and an unrelated broken-link fix has independent authority
- **THEN** the declared child traces to its parent outcome and criterion at the applicable revision; a native row may name its governing scenario directly. A missing, stale or wrong parent blocks only its dependent work. The independent fix may carry the source, expected destination and link check inline. Reclassifying an orphan as independent fails.

### Requirement: R12 · Readable work records and session explanations

SpecDev SHALL use reader-appropriate plain language across Markdown and session messages. Name the actor, action and observable consequence where they affect the reader’s decision. Preserve sourced meaning, uncertainty, obligation strength, exact identifiers, numbers and authority. Keep clear prose as written. Match the vocabulary to the owner, implementer or reviewer using the artifact.

#### Scenario: Recover the safe action after a partial write (A12, F10.1, S10.1)

<a id="f10--write-stories-and-tasks-that-a-reader-can-act-on"></a><a id="acceptance-criteria-18"></a><a id="f10-1"></a><a id="scope-and-sources-18"></a><a id="s10--read-a-work-item-without-guessing-what-success-means"></a><a id="acceptance-criteria-19"></a><a id="s10-1"></a><a id="scope-and-sources-19"></a>

- **WHEN** a writer edits the WEB-09–WEB-10 partial-write Task for an implementer and an owner and the supplied story sentence is already clear
- **THEN** a reader without the answer key recovers the three row states, stop condition, retry prerequisite and decision owner. The 500-ID limit, refreshing confirmed rows and counts, literal identifiers and the clear story meaning survive. An alternative wording can pass. A forced retry, invented guarantee or omitted limit fails. Retain the source, edited passage, reader response and located review reason.

<a id="requirement-r13--worked-child-issue-for-a-failed-save"></a>

### Requirement: R13 · Worked child Task for a failed save

SpecDev SHALL give writers a complete child Task that can be reached from its story and the Task guide. Preserve the distinct parent Feature example.

<a id="scenario-locate-one-worked-child-issue-a13-f111-s111"></a>

#### Scenario: Locate one worked child Task (A13, F11.1, S11.1)

<a id="f11--show-a-complete-child-task-for-one-story-criterion"></a><a id="acceptance-criteria-20"></a><a id="f11-1"></a><a id="scope-and-sources-20"></a><a id="s11--follow-a-failed-save-from-story-to-child-task"></a><a id="acceptance-criteria-21"></a><a id="s11-1"></a><a id="scope-and-sources-21"></a>

- **WHEN** a reader follows the worked story and Task guide to the child assigned the WEB-06 failed-save criterion
- **THEN** the child identifies the bounded failure condition, observable result, source and proof and links back to its parent. Assigning the broader Feature or bulk editing fails. The separate parent example remains available.

### Requirement: R14 · Actionable manual handoffs

SpecDev SHALL put portable session instructions for necessary manual actions and misunderstood explanations in one named section of Writing Style (WS). Link the existing procedure guidance and preserve the checked-delivery boundary.

#### Scenario: Guide a user through an actual manual handoff (A14, F12.1, S12.1)

<a id="f12--make-session-explanations-usable-from-the-owners-starting-point"></a><a id="acceptance-criteria-22"></a><a id="f12-1"></a><a id="scope-and-sources-22"></a><a id="s12--act-on-a-handoff-and-resolve-a-misunderstood-role"></a><a id="acceptance-criteria-23"></a><a id="s12-1"></a><a id="scope-and-sources-23"></a>

- **WHEN** the owner needs a manual handoff from a known starting location or misunderstands who supplies a reader answer
- **THEN** the reply states the exact action, expected result and appropriate recovery, or clarifies the two roles and outstanding decision using the supplied facts. An owner who already has the document receives the requested answer directly. An unresolved role stays open. Compare the actual reply to the owner’s recovered next action.

### Requirement: R15 · Proportionate wording checks

SpecDev SHALL require the file-based wording check where its predicates or an existing artifact obligation apply. Every message still receives source-grounded editorial review.

#### Scenario: Apply the wording check where it can find a defect (A15, F13.1, S13.1)

<a id="f13--keep-checks-proportionate-for-routine-updates"></a><a id="acceptance-criteria-24"></a><a id="f13-1"></a><a id="scope-and-sources-24"></a><a id="s13--send-a-routine-update-with-the-appropriate-checks"></a><a id="acceptance-criteria-25"></a><a id="s13-1"></a><a id="scope-and-sources-25"></a>

- **WHEN** a routine progress message contains no applicable naming or absence claim and a separate message uses an incorrect canonical label
- **THEN** the first receives source-grounded editorial review without a file check. The second produces a located naming finding. Existing required artifact checks and version-bound finalization continue to apply. Use the observed trace and reuse unchanged receipt evidence.

### Requirement: R16 · Public entry and document selection

SpecDev SHALL in the public `README.md`, show how a request becomes observable behavior, a bounded change and a check. Distinguish an ordinary document, an independent fix and an OpenSpec change. Show readers where to find the governing scenario, the design decision where needed, the task and its proof. Link the owning instructions for conditional documents.

#### Scenario: Choose the route from the public introduction (A16, F20.1, S20.1)

<a id="f20--explain-the-document-sequence-in-the-readmemd-file"></a><a id="acceptance-criteria-38"></a><a id="f20-1"></a><a id="scope-and-sources-38"></a><a id="s20--choose-the-next-document-from-the-quick-start"></a><a id="acceptance-criteria-39"></a><a id="s20-1"></a><a id="scope-and-sources-39"></a><a id="production-order"></a>

- **WHEN** a reader starts above setup in the repository’s `README.md` with an idea, an agreed project change, an ordinary writing request or a broken-link fix
- **THEN** the reader can select the right entry, locate the governing scenario and required parents, design where applicable, task, the point where proof is defined and where it is observed. Conditional A10 formats are findable on request. A native change uses its own artifacts, an independent fix uses its own record, and a writing-only request ends at delivery. The core diagram shows the four native documents. The expanded diagram adds optional paths with dotted arrows. Both label nodes with only the document title and abbreviation. A missing declared parent blocks only dependent work. A standalone Markdown assignment can use `task.md`; `tasks.md` orders a change’s work. Link an existing task only when it owns separate criteria or evidence.

#### Scenario: Trace an illustrative change to a check (F20.2, S20.2)

<a id="f20-2"></a><a id="s20-2"></a>

- **WHEN** a new user follows WEB-06 from the public introduction through the story and worked task
- **THEN** they recover the intended behavior, bounded change and specified failure check T10, can distinguish planned proof from an observed result, and know what is needed before authorized implementation selects further work.

### Requirement: R17 · Work ownership and a single design standard

SpecDev SHALL use the smallest record that preserves scope, authority and proof under the project’s governance. Resolve declared parent criteria. An independently authorized fix may use one Task. Use the same OpenSpec design structure for standalone and change designs. Add architecture, component, interface, migration or recovery detail only where a decision needs it. Link existing decisions and contracts at their owner.

#### Scenario: Choose the smallest record and coordinate only real dependencies (A17, F21.1, S21.1)

<a id="f21--choose-how-much-planning-an-improvement-needs"></a><a id="acceptance-criteria-40"></a><a id="f21-1"></a><a id="scope-and-sources-40"></a><a id="s21--route-an-improvement-from-its-actual-scope"></a><a id="acceptance-criteria-41"></a><a id="s21-1"></a><a id="scope-and-sources-41"></a><a id="link-work-to-its-parent-and-designs-to-their-sources"></a><a id="refund-approval"></a>

- **WHEN** the same improvement is independently authorized, assigned to an existing story, or itself an independently acceptable user outcome
- **THEN** the first can use one Task, the second resolves its parent and criterion, and the third can use its directly authorized story with value, boundary and proof. Grouping work or introducing a plan requires an actual dependency, governing rule or integrated outcome. A migration with coexisting readers identifies rollout order, compatibility proof and recovery. Keep routine steps inline.

#### Scenario: Use one design at the depth the refund change needs (A17b, F21.2, S21.2)

<a id="f21-2"></a><a id="s21-2"></a>

- **WHEN** a project asks for a component design for manager-only refund approval and a separate standalone request supplies an authorized contract naming that same service and rule
- **THEN** the change edits its one native `design.md`; the standalone design uses the same baseline of context, goals and exclusions, decisions with rationale, and risks or trade-offs. Add architectural, interface, migration or recovery detail only where needed. Link the existing decision owner and the employee-denial check. The standalone contract can suffice without a separate High Level Document (HLD), story or epic. Duplicating the design or inventing a parent fails; a declared child with a missing criterion remains blocked.

### Requirement: R18 · Material questions and authority

SpecDev SHALL use the document type and requested scope to identify material information needed at the checked writing entry. Resolve each applicable topic from evidence or actual authority, or keep it visibly open. Before asking, identify the affected requirement or section, source inspected and the consequence of an answer. Preserve the lightweight route for narrow edits.

#### Scenario: Preserve decided access; ask about a new permission (A18, F22.1, S22.1)

<a id="f22--resolve-material-gaps-without-needless-questions"></a><a id="acceptance-criteria-42"></a><a id="f22-1"></a><a id="scope-and-sources-42"></a><a id="s22--write-from-incomplete-project-context"></a><a id="acceptance-criteria-43"></a><a id="s22-1"></a><a id="scope-and-sources-43"></a><a id="when-the-writer-may-ask-the-owner"></a>

- **WHEN** the current download is staff-only and two requests say “Add CSV to the existing download; only the format changes” and “Let customers download their own reports,” with individual versus organization ownership unresolved
- **THEN** the first produces zero permission questions and preserves existing access. The second produces one focused question about the affected ownership rule. An attributable answer enables only the authorized choice. Silence, a preselected answer and a citation showing ownership is undecided leave it provisional. The writer can continue unaffected sections.

#### Scenario: Use evidence before asking the owner

- **WHEN** the writer encounters an observed fact, a governing requirement, a choice within delegated discretion or an owner-held material fact
- **THEN** the writer cites the relevant source at its revision, applies settled rules, makes routine authorized choices and asks only for material missing authority. The question identifies the affected section and what the answer changes. Checks can establish coverage and valid references; semantic review judges whether the evidence supports the claim. Neither best practice nor a syntactically valid answer creates authority.

### Requirement: R19 · Qualified document selection and optional shortcuts

SpecDev SHALL use one qualified entry and select the installed upstream operation or schema first. Preserve the brief, requested operation, host handlers and qualified fallback. Give each document in the README catalog its own command. Resolve the same document by its full name or qualified selector. Offer a short host entry wherever it is available. Reference-only guides inform authoring.

#### Scenario: Select a document or a review through its supported entry (A19, F23.1, S23.1)

<a id="f23--start-documents-from-native-shortcuts"></a><a id="f23--select-a-document-from-the-supported-host"></a><a id="f23-1"></a><a id="s23--write-the-intended-artifact-from-a-short-request"></a><a id="s23-1"></a>

- **WHEN** a user gives either host a document brief, uses a catalog command such as `/dr`, `/lld` or `/task`, or its supported host equivalent, or requests another authorable type by full name or qualified selector
- **THEN** each route preserves the operation and original brief, reaches the same owning writer and yields the intended checked artifact. A review returns located findings. An occupied shortcut retains its original handler and the qualified entry remains usable. Repeated setup and owned-only removal preserve unrelated commands. Resolve the catalog once and observe an actual document per host. Each released document has a catalog command. The planned formats gain their handlers when they ship. Installed native operations retain precedence.

### Requirement: R20 · Guided continuation

SpecDev SHALL use OpenSpec’s discovery or next-artifact guidance where available. For standalone writing, offer guided entry, read-only next-document advice and one-document continuation using actual prerequisites and revisions. In one line name the next document, the specific gap and its benefit, or the real blocker or completed endpoint.

#### Scenario: Recommend and continue one eligible document (A20, F24.1, S24.1)

<a id="f24--guide-the-next-document-from-project-evidence"></a><a id="f24-1"></a><a id="s24--choose-and-continue-one-eligible-document"></a><a id="s24-1"></a>

- **WHEN** the owner asks what comes next for a reviewed feature, a blocked decision or a completed standalone fix
- **THEN** the reply gives one grounded recommendation and benefit, identifies the actual blocker, or reports completion. Native status and prerequisites drive change advice. The suggestion makes no edits. An authorized one-document continuation creates one attributable successor; resumption reuses it. A changed source reopens only affected work. A writing-only request stops and an independent task can stay in one Task.

### Requirement: R21 · Maintained and historical specifications

For a change to a delivered feature, SpecDev SHALL identify the active source under the project’s maintenance policy and distinguish historic delivery evidence. Resolve a material authority conflict before settling the affected requirement.

#### Scenario: Use the maintained rule after delivery (A21, F25.1, S25.1)

<a id="f25--find-the-governing-specification-after-delivery"></a><a id="f25-1"></a><a id="s25--guide-selection-of-a-specification-after-delivery"></a><a id="s25-1"></a><a id="acceptance-for-maintained-specifications-fields-and-shared-contracts"></a>

- **WHEN** an edit is requested with a frozen seven-day launch spec and an approved maintained thirty-day policy, or with both values and no source-selection decision
- **THEN** in the first case the draft uses the thirty-day rule and identifies the seven-day value as historical. Both input files retain their identities. In the second, the owner is asked which governs before that requirement is settled; independent sections can proceed. After archive, distinguish the durable `openspec/specs/<capability>/spec.md` from the historical change. Retain the affected draft excerpts or question and source revisions.

### Requirement: R22 · Field-level constraints

For work on a constrained field, SpecDev SHALL link the exact field definition from the native task or its independently owned Task. Check the receiving task for missing or misattributed constraints.

#### Scenario: Trace a constrained field to its precise owner (A22, F26.1, S26.1)

<a id="f26--carry-exact-field-constraints-into-the-implementing-task"></a><a id="f26-1"></a><a id="s26--resolve-constrained-fields-in-task-handoffs"></a><a id="s26-1"></a>

- **WHEN** a task implements required `Return.code` in a contract where `Order.code` is optional, and a review variant points to `Order.code`
- **THEN** the owning task references the correct field, and review locates the wrong reference, task and missing requirement. An unambiguous existing pointer suffices. An unrelated prose task needs no field reference. The two source definitions stay unchanged.

### Requirement: R23 · Contracts shared by separate releases

For independently released providers and consumers, SpecDev SHALL distinguish the authoritative contract revision, the consumer’s supported or pinned version, and the evidence for actual runtime compatibility.

#### Scenario: Resolve a cross-repository contract and its consumer pin (A23, F27.1, S27.1)

<a id="f27--resolve-the-contract-shared-by-separate-repositories"></a><a id="f27-1"></a><a id="s27--document-the-owner-and-consumer-version-of-a-shared-contract"></a><a id="s27-1"></a>

- **WHEN** the owner contract is v1, the consumer’s copy diverges, v2 is proposed and only mock and v1 pin evidence is available
- **THEN** the Interface Contract (IC) identifies its owner revision and supported consumer pin, explains the discrepancy and sends the proposed change to the owner. The copy is untouched and deployed compatibility stays unknown. Components consuming one shared file need no synchronized duplicate.

### Requirement: R24 · Canonical and legacy skill identity

SpecDev SHALL ship SpecDev with one writing implementation and a compatible legacy entry, after Skill Builder accepts both identities.

#### Scenario: Retain the deployed writer identity through the rename (A24, F28.1, S28.1)

<a id="f28--keep-existing-users-working-through-the-spec-writer-rename"></a><a id="f28--keep-existing-users-working-through-the-specdev-rename"></a><a id="f28-1"></a><a id="s28--release-the-spec-writer-identity-and-legacy-entry"></a><a id="s28--release-specdev-with-a-compatible-technical-writer-entry"></a><a id="s28-1"></a>

- **WHEN** Skill Builder B5/T50 has accepted both identities and an existing Technical Writer user and a fresh SpecDev user invoke their supported hosts
- **THEN** both reach one checked writer using the deployed `technical-writer` legacy entry or the canonical `specdev` identity. Existing documents and receipts retain their original identities. An unrelated occupied name survives. The accepted Builder validates a real document against the renamed candidate. Unreleased planning names require no alias. Retain per-host readback and failures.

### Requirement: R25 · Native OpenSpec integration and discovery

SpecDev SHALL use the privately locked `@fission-ai/openspec@2.1.1` runtime. Resolve the installed native capability before local alternatives, including capabilities outside the default workflow. Use the selected root, change, schema, status and instructions, protect project files and review or edit native artifacts in place on each supported host.

#### Scenario: Initialize only the user’s selected project (A25, F29.1, S29.1)

<a id="f29--start-a-checked-feature-in-an-initialized-workflow-project"></a><a id="f29--open-and-edit-a-native-change-from-specdev"></a><a id="f29-1"></a><a id="s29--start-one-feature-through-an-optional-workflow-extension"></a><a id="s29--connect-the-privately-pinned-openspec-to-a-selected-change"></a><a id="s29-1"></a><a id="how-upstream-templates-map-to-the-writer"></a><a id="which-artifact-owns-each-part-of-an-openspec-change"></a>

- **WHEN** the user requests `/specdev init` on Claude Code or `$specdev init` (or its documented equivalent) on Codex for the current selected project
- **THEN** SpecDev delegates to the private native OpenSpec `init` at that root. A fresh SpecDev-only setup uses `--tools none`; explicitly requested supported flags and tool choices are forwarded. Repeat setup protects user edits, unrelated handlers and other projects. The operation ends at initialization with no independent global `/init`, feature creation or apply.

#### Scenario: Write or review the artifact the selected schema actually owns

- **WHEN** a registered project has a selected change and the pinned native runtime returns `openspec status --change <change> --json` and `openspec instructions <artifact-id> --change <change> --json`
- **THEN** SpecDev uses the reported schema, paths and prerequisites to author or review the actual native artifact in place. The default schema uses `proposal.md` for purpose/impact and affected capabilities, `specs/<capability>/spec.md` for changed requirements and scenarios, `design.md` for applicable decisions, and `tasks.md` for verified work. Inspect relevant existing capabilities before naming new ones. Other installed schemas may supply different artifacts. On the release candidate, submit a valid native artifact whose headings differ from the former writer template. It must reach the native consumer. Inspect the active `SKILL.md`, overlapping format references and validation entry: retire the competing mandatory headings and checks there. A second adapter forcing native output through the former schema fails. Preserve the standalone document contracts and historical receipt verification. Missing or ambiguous required root, change, runtime or provider stops the affected operation; ordinary document writing remains available without OpenSpec.

#### Scenario: Resolve commands from the installed OpenSpec surface

- **WHEN** a qualified request is an OpenSpec verb or workflow, including one without a local shortcut, a naming overlap, an unknown verb, or a known native operation that is unavailable
- **THEN** the entry looks up installed CLI help and installed skill/profile metadata. A matching native operation wins every overlap, including discovery/explore, review/verify, update/sync/archive, profiles, custom schemas and specialist artifacts. Forward its supported options under the user’s effect authority. Use a local-only command only after a lookup with no matching upstream operation. If neither supplies it, report that and leave state untouched. A missing runtime or disabled workflow is a prerequisite failure and stays distinct from unknown input. Treat unrecognized text as data; never execute it as shell. Observe one installed non-core operation such as `openspec templates --schema <name> --json` and compare the returned paths with upstream on the pinned release. No second command catalog, schema copy or engine may restrict other native operations.

### Requirement: R26 · A single native task list

SpecDev SHALL use the selected change’s native `tasks.md`. Each numbered checkbox describes bounded work and how to verify it. Resolve its governing scenario and any material design, dependency or existing Task. A separate Task is warranted for independently owned, externally assigned or project-required work. Maintain each criterion at one owner.

#### Scenario: Select the verified refund task in the intended change (A26, F30.1, S30.1)

<a id="f30--give-the-implementing-agent-the-complete-task-contract"></a><a id="f30--select-native-work-with-its-verification"></a><a id="f30-1"></a><a id="s30--select-eligible-feature-work-and-recover-its-task-criteria"></a><a id="s30--read-the-eligible-row-and-its-source-in-the-selected-change"></a><a id="s30-1"></a><a id="feature-task-lists-and-task-acceptance"></a><a id="native-tasks-and-separately-owned-tasks"></a><a id="when-to-write-and-read-tasksmd"></a><a id="refund-status-and-filtering"></a><a id="related-design-and-work"></a>

- **WHEN** two changes share a local task number and the selected refund change supplies a settled API read contract, independently editable dashboard and CLI, and a dependent filter
- **THEN** the consumer resolves the selected change, its governing scenario, actor, permitted work and check. Rows 1.1 and 1.2 can independently verify the stored decision in the dashboard and CLI; both results demonstrate the first usable story. Row 2.1 requests denied refunds from mixed input and verifies every result is denied. Row 2.2 connects the dashboard and checks the filtered view only after 2.1 establishes that API behavior. A stale source blocks only its dependent work.

#### Scenario: Keep one owner for a task and its proof

- **WHEN** a bounded change task or a separately owned API Task already provides its governing criterion
- **THEN** the native numbered `- [ ]` checkbox states the action and how to verify completion. It resolves the relevant scenario, material design and true prerequisites. Ordinary substeps stay inline. An externally assigned or project-required Task such as #83 keeps its own criterion, and the row verifies its applicable result by reference. Extra task files, per-row Task exports and duplicate editable criteria are unnecessary. The actual implementer can select eligible work from the native list and its declared inputs. Verify through the live skill and Task guidance that the former mandatory Task-per-row rule has been removed.

### Requirement: R27 · Authorized implementation, verification and archive

SpecDev SHALL stop at checked delivery for a writing request. For an authorized build, use OpenSpec’s apply instructions and the selected provider. Keep the task, original criterion, candidate and observed result attributable through recovery. Use native archive only within authorized scope after applicable acceptance and verification.

#### Scenario: Stop, execute or resume at the authorized boundary (A27, F31.1, S31.1)

<a id="f31--verify-and-resume-one-authorized-implementation"></a><a id="f31-1"></a><a id="s31--verify-and-resume-one-authorized-implementation"></a><a id="s31-1"></a>

- **WHEN** the user requests writing only, or separately authorizes local implementation of a refund task that fails a permission check and is interrupted during recovery
- **THEN** writing ends at checked delivery. For the build the selected provider consumes native apply instructions, preserves task and criterion identity and the original failure, and binds the corrected outcome to the actual candidate. Reconcile existing effects before resuming; uncertain effects stay open without replay. Only mark completed work whose proof was observed. Keep structural validation, native review, semantic judgment and actual product behavior distinct, reusing evidence for what it proves.

#### Scenario: Archive the authorized accepted change

- **WHEN** the change’s requirements have applicable acceptance evidence and the user authorizes archive
- **THEN** the upstream archive preserves the change history and updates durable capability specs under `openspec/specs/`. A structurally valid delta, checked box, writing approval or routine request cannot authorize archive, a new external effect, or a claim that an unobserved product outcome passed.

### Requirement: R28 · Idea and defect intake

For an OpenSpec discovery or exploration request, SpecDev SHALL use the installed upstream operation. Otherwise use the smallest intake appropriate to the request. A material idea can use a brief or decision record. An observed bounded defect can use one repair task with its check. Resolve substantive uncertainty before undertaking dependent work.

#### Scenario: Treat an idea and a bounded defect according to their evidence (A28, F32.1, S32.1)

<a id="f32--route-an-idea-or-bug-to-the-right-upstream-workflow"></a><a id="f32--choose-a-suitable-record-for-an-idea-or-defect"></a><a id="f32-1"></a><a id="s32--route-an-idea-or-bug-to-the-right-upstream-workflow"></a><a id="s32--resolve-an-idea-or-describe-a-bounded-repair"></a><a id="s32-1"></a>

- **WHEN** a contributor has an idea missing decision evidence or reports a bounded observable defect
- **THEN** the idea yields a supported question, recommendation or stop decision. The repair record identifies the actual failure, bounded scope and check. Native exploration owns a request for that operation. A direct writing request ends at the record and produces no implementation or automatic intake document set.

### Requirement: R29 · Versioned private installation and recovery

SpecDev SHALL distribute a versioned SpecDev integration with a private exact OpenSpec npm dependency. Upgrades identify the proposed pin, verify native inputs and project preservation and support recovery to the prior working pin. Remove only owned files.

#### Scenario: Upgrade or recover the exact private dependency (A29, F33.1, S33.1)

<a id="f33--maintain-a-versioned-workflow-integration"></a><a id="f33-1"></a><a id="s33--distribute-and-safely-update-the-versioned-integration"></a><a id="s33-1"></a>

- **WHEN** a maintainer takes the W47 working pin and lock, proposes a supported exact upgrade, then exercises recovery and removal
- **THEN** the resolved executable, versions and native contract remain identifiable. An incompatible update preserves or restores the working pin and lock. Compare edited project artifacts and unrelated installation entries before and after. Removal affects only owned installation files. Preserve any failed attempt with its candidate.

### Requirement: R33 · Supplementary document selection

SpecDev SHALL make each authorable format available on explicit request. When the installed operation or schema owns the requested output, including a specialist type, use its native artifact in place. Add a supplementary document only when requested or when a real consumer needs it. Reference-only guides support authoring.

#### Scenario: Use a supplementary document only when requested or consumed (A33, F37.1, S37.1)

<a id="f37--use-the-full-writing-catalog-in-the-optional-workflow"></a><a id="f37--use-supplementary-documents-when-a-change-needs-them"></a><a id="f37-1"></a><a id="s37--write-the-requested-document-and-pass-it-to-the-right-consumer"></a><a id="s37--write-a-requested-document-and-pass-a-needed-source-to-its-consumer"></a><a id="s37-1"></a><a id="how-the-optional-workflow-uses-the-full-catalog"></a><a id="request-a-document-by-name"></a>

- **WHEN** the user requests a Tutorial (TUT), or an authorized native change task consumes a reviewed design or specialist artifact already defined by its schema
- **THEN** the tutorial receives its format-specific checked handoff and no provider dispatch. The change uses the native artifact at its actual location, links its exact decision and source to the task and holds stale dependent input. The catalog includes eligible authorable types and A10 variants as released. Writing Style (WS), Visual Guidance (VG) and other reference-only guides inform writing. A catalog entry alone creates no requirement for a companion file, extra alias or export.

#### Scenario: Write and edit native artifacts in the shared style (A33b, F37.2, S37.2)

<a id="a33b"></a><a id="f37-2"></a><a id="s37-2"></a>

- **WHEN** SpecDev drafts or edits prose in an OpenSpec proposal, specification, design, task list or other Markdown artifact supplied by the active schema
- **THEN** SpecDev SHALL use its installed Writing Style (WS) guide and review the finished passage against the governing source. OpenSpec and the selected project retain their headings, requirement keywords, paths, identifiers, numbering, checkboxes and applicable rules. A reader can identify the action and its conditions. An unresolved permission stays open until a source or an authorized person settles it. The writing request produces only the requested artifact or edit.

### Requirement: R34 · Reader-facing feature guidance

SpecDev SHALL give procedures, references and session replies wording suited to the reader’s decision and the evidence available.

#### Scenario: Explain the refund rule and the actual open decision (A34, F38.1, S38.1)

<a id="f38--write-feature-guidance-and-session-replies-around-the-readers-decision"></a><a id="acceptance-criteria-44"></a><a id="f38-1"></a><a id="scope-and-sources-44"></a><a id="s38--explain-the-feature-and-report-the-checked-result"></a><a id="acceptance-criteria-45"></a><a id="s38-1"></a><a id="scope-and-sources-45"></a>

- **WHEN** a reader receives the reviewed refund procedure and its session reply
- **THEN** the procedure identifies where to act, who may approve and the source; the reply identifies the reviewed rule and who still owns the retry decision. An authored document cannot establish that a refund ran. Reuse the accepted [W60 guide evidence](https://github.com/fatonsopa/ai-technical-writer/blob/d8bf859f0eec178aa34b24e29aef10290e984c3b/references/writing_style.md#write-a-feature-page-people-can-use) within its original scope.

### Requirement: R35 · Public feature ownership and instructions

The root `README.md` SHALL show who supplies each feature and distinguish released features from planned ones. Link each released feature to usable guidance. List documents by the names users request, explain each in plain language and link its guide. One section may cover related variants. Add a separate guide only for a distinct reader need.

#### Scenario: Identify the owner of each feature from the public `README.md` (A35, F39.1, S39.1)

<a id="f39--make-every-released-feature-and-supported-document-type-findable"></a><a id="acceptance-criteria-46"></a><a id="f39-1"></a><a id="scope-and-sources-46"></a><a id="s39--find-instructions-for-a-feature-or-document-type-from-the-index"></a><a id="acceptance-criteria-47"></a><a id="s39-1"></a><a id="scope-and-sources-47"></a><a id="find-features-and-document-types-from-the-public-index"></a>

- **WHEN** a reader opens the repository-root `README.md` before deciding whether to use the product
- **THEN** a feature-by-feature table has separate OpenSpec and SpecDev columns and checkmarks indicating which tool owns each feature. Its caption explains how the single SpecDev entry uses upstream OpenSpec. The reader can distinguish shipped behavior from planned integration and find the owning instructions. An unshipped capability presented as ready or a checkmark implying duplicate ownership where upstream governs fails.

#### Scenario: Find each released capability and supported type

- **WHEN** a new user follows the public index to focused editing, document review, a Task variant or another released type or operation
- **THEN** the destination is a usable page or named section explaining when to use it, inputs and expected result, including the needed action or recovery where applicable. The focused-edit entry preserves the selected scope; the review entry returns located findings. Shared destinations may serve variants they actually explain. An omission, empty stub, broken anchor or irrelevant overview fails. Compare the release catalog to the index; use representative actual destinations. Each changed feature ships its own usable guidance and link. Use one document table with the command, the linked title in Full Name (ABBREVIATION) form, and a plain-language description of when to use it. Mark planned formats in the description.

### Requirement: R36 · Install SpecDev from a release

<a id="install-the-release-and-connect-a-host"></a>

SpecDev SHALL install from a versioned GitHub release or npm package without a source checkout. The installed CLI SHALL report its own version and connect the chosen hosts to the same skill. Published instructions SHALL identify prerequisites, verification, update and removal for each channel.

#### Scenario: Install and use the selected host (A36a, S40.1)

- **WHEN** a developer on a supported platform follows the release instructions in a clean user environment, verifies the version, selects Codex or Claude Code and invokes the installed skill
- **THEN** the release and executable are identifiable, the selected host reaches the skill and the user can complete a bounded request. Setup leaves unrelated tools and projects alone. A mismatched release checksum or unsupported prerequisite identifies the blocker before replacing a working installation.

#### Scenario: Upgrade or remove only what the installer owns (A36b, S40.2)

- **WHEN** a user updates through the original channel, repeats host setup or removes an installation beside the other skill, with a locally edited entry and a project document
- **THEN** a clean update exposes the intended version without duplicate entries. A conflict identifies the affected path and preserves the edit and prior working version. Removal preserves the other skill, project documents and foreign files. The `README.md` distinguishes a tested release candidate from a publicly available release.
