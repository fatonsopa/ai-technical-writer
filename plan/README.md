# Spec Writer implementation handoff

Use this handoff to implement Spec Writer on a local branch. It contains the starting prompt for Claude or Codex and the approved work for this repository.

The execution baseline is revision 20, covering 36 approved findings, 36 child stories and 59 tasks. Users may ask for a document by full name or acronym at any turn. In authored prose, introduce a document name once and retain required literal labels. A checked delivery may include one useful statement from the reviewed document, bound to its reviewed version. The handoff branch contains the audited Technical Writer source at `4a8e7c92e20404f05e68708c1a3ea26c6961b178` and the planning packet. Implementation begins on the other computer. Use the accepted Skill Builder implementation from the first handoff. Record its commit. Start with W01 and W03 as their dependencies allow. [Skill Builder handoff](https://github.com/fatonsopa/ai-skill-builder/blob/docs/autonomous-implementation/plan/README.md)

## Start

Open this handoff in the checkout you will use. Give the implementing agent the path to this file. It can read the starting prompt here. For a read-only rehearsal, give it only the checkout and the assessor’s question.

### Starting prompt

> Use the accepted Skill Builder candidate to implement the approved Spec Writer changes and rename on a local branch. Record the Builder commit and confirm B5/T50 before the live rename. Run the existing workflow integration tasks against the pinned upstream source. W60 already has accepted evidence. W55–W57 and W51.3 are pending owner decisions. Read the repository instructions, then follow this guide: read `plan/specification.md` and `plan/implementation-plan.md`, open `plan/tasks.md` and follow the next eligible row to its Issue. Implement only its scope. Verify its criteria on the candidate, record the evidence in the Issue and the private JSON log, commit the increment, and update its checkbox. Resume from the evidence on the next eligible row. Use `plan/test.md` for the handoff checks. Finish the approved integrated checks and report the local result.


## Execution rules

1. **Bind the work.** Identify the handoff commit, governing specification, applicable repository instructions, candidate and skill dependencies. On resumption, read the existing task’s last accepted commit, evidence, open criteria and next eligible task. Protect existing work on all branches.
2. **Select one deliverable.** Resolve the task, parent outcome, supported criterion, affected interface, prerequisites, allowed change and required proof. Work from the reviewed record. Stop only affected work if a required decision or dependency is missing. Continue eligible independent tasks.
3. **Implement within scope.** Inspect the real entry point and keep the increment independently usable. Choose internal details within the agreed contract. Keep the original acceptance criteria and source authority. A new deliverable, new external action, changed permission or weaker criterion requires the owner’s explicit decision.
4. **Use evidence to limit verification.** Reuse applicable results. Run the smallest check that can disprove the candidate against the task’s criterion. A rare extra verification is appropriate when a concrete failure, changed input or missing evidence makes the approved result uncertain. Record the criterion, what the check established and the action it changes. Apply a supported better technique directly when it remains inside the task’s behavior, authority and quality obligations. General best-practice advice alone cannot enlarge scope.
5. **Defer other discoveries.** Append a brief entry to [Pending owner decisions](./implementation-plan.md#pending-owner-decisions). Record evidence, impact, proposed change and any blocked task. Leave the change pending and move to eligible work. A material blocker can keep a criterion open without erasing prior results.
6. **Close and resume.** In the existing task, record each criterion as Met, Failed or Not demonstrated, with the exact candidate and evidence. Retain failures through correction. Commit each accepted increment on the local implementation branch, record the next task and continue. Reuse task evidence for story acceptance where it actually proves the integrated result. Report host-specific results separately. Remote integration, releases and deployment require separate authority.

## Check the result

For a read-only rehearsal, compare the reader’s choices with the [test specification](./test.md). During implementation, record each criterion’s verdict and evidence in the linked Issue. Close the delivery when its integrated checks and shared Definition of Done pass on the identified candidate.

## Find your way around

1. Read the [audit](./audit.md) for the source of a finding and the [specification](./specification.md) for the agreed behavior, stories and acceptance scenarios.
2. Open the [implementation plan](./implementation-plan.md) for the approach, material dependencies, rollout and recovery.
3. Use [tasks.md](./tasks.md) to select the next eligible Issue. Its scope, acceptance criteria and proof live at that row. Follow its parent link to the story criterion in the specification. A separate `task.md` is optional.
4. Use [test.md](./test.md) for the read-only rehearsal and the later implementation case.

## Limits and help

A rehearsal authorizes reading only. During a build, record an out-of-scope discovery under [Pending owner decisions](./implementation-plan.md#pending-owner-decisions) and continue eligible work. If an Issue conflicts with the governing specification or its proof is stale, hold the affected row and use the plan’s [recovery instructions](./implementation-plan.md#rollout-and-recovery).

## JSON execution log

Use the run’s existing JSON records first. Skill Builder’s behavioral harness already writes `public-events.json` during execution. Keep it in its native format. For task decisions or manual actions it does not capture, append one JSON object per line to `execution.jsonl` in the private run directory outside the repository. Link existing event IDs or evidence paths instead of copying full traces. On resumption, locate the same run and read the last confirmed checkpoint. Record observed actions and decisions when they happen.

| When | What to record |
| --- | --- |
| Choose work | UTC timestamp, run ID, task ID, criterion ID, candidate or source revision, intended action, and the clause that puts it in scope. |
| Before an extra test, review or retry | The unresolved criterion, changed input or observed failure, existing evidence inspected, the smallest useful check, and how pass or failure would change the next action. If neither outcome changes the decision, skip the check and record the reuse decision once. |
| Receive a result | Actual observation, outcome or error, evidence reference and candidate. Preserve failed attempts. For a correction, reference the original failure and resume from the last confirmed boundary. Record an unobserved result as unknown. |
| Defer or close | Scope decision, owner question if needed, criterion verdict, commit or candidate, evidence reused and next eligible task. Record a lesson only when evidence supports it, and change the current work only within its approved scope. |

A decision entry might look like the following. The values are illustrative.

```json
{"time":"2026-11-22T10:00:00Z","run_id":"example-run","task_id":"example-task","criterion_id":"example-criterion","candidate":"example-commit","event":"verification_decision","action":"reuse","reason":"The accepted result covers this criterion on the same candidate and the relevant input is unchanged.","evidence_ref":"task-evidence/observed-result.json","next":"Close this criterion"}
```

At task closure, read the task’s entries once. Check that every implemented change serves an approved criterion or necessary safeguard, and that each extra verification had a reason that could change the decision. Use any discrepancy to correct the current task or defer a new proposal. A JSON entry points to the evidence that proves the result. Keep the log metadata small. Exclude secrets, private reasoning and raw personal or customer content. The Markdown pending section holds owner decisions. Run events and the private JSON log stay outside the published handoff. [Skill Builder’s execution records](https://github.com/fatonsopa/ai-skill-builder/blob/222b356fd5ac7a2df9fd9621e3744db883ecede0/references/maintenance.md#diagnose-and-recover-stalled-work) · [OpenTelemetry log fields](https://opentelemetry.io/docs/specs/otel/logs/data-model/)

## When the writer should ask

Implement R18/A18 through W32–W34. Before asking, identify the affected criterion or section, the authoritative source inspected and what the answer changes. If the source settles the matter, proceed. Use delegated judgment for routine choices within scope. A general best practice can support a recommendation. A material product choice still requires its owner. One missing owner-held fact can warrant a direct question without invented alternatives. If the owner is silent, keep the dependent text provisional. Preserve narrow edits. A source reference alone cannot establish that its words support the claim.

## Shortcuts and document handoffs

Ship opt-in native shortcuts and a one-line next-document recommendation. Use the [upstream template mapping](./specification.md#how-upstream-templates-map-to-the-writer) when implementing W35–W41. Every shortcut must reach the existing Technical Writer reference and checked output contract. The walkthrough recommends, then waits for the user to continue. See F23 and F24 in the [specification](./specification.md#scenarios). Use the [feature task-list rules and refund example](./specification.md#feature-task-lists-and-issue-acceptance) for the W40-to-W48 handoff. Use the [command and document sequence](./specification.md#when-to-write-and-read-tasksmd) in the public README, the owning format guides and each applicable command’s handoff.

## Approved rename and toolkit

Use **Spec Writer** (`spec-writer`) as the sole product identity in the skill, repository documentation, installation text, examples, command descriptions and session replies. Describe the optional workflow by its function. Preserve exact technical identifiers needed to run it, source destinations for the audit and applicable copyright notices.

The owner approved the optional workflow integration and the skill name **Spec Writer** (`spec-writer`). Claude implements the live rename on the handoff computer. The existing GitHub repository and clone URL remain the integration target. Spec Writer remains usable without the optional workflow. Deliver the rename after Skill Builder B5/T50. W47 selects a feature, W48 lets the implementing agent select eligible work from the feature list and recover acceptance from each Issue, and W49–W50 prove execution and recovery on one authorized local feature. Establish that connection before adding W51–W52 and the versioned W53 distribution. Reuse host evidence where inputs match. Use the project-selected provider for execution. Keep remote publication outside implementation authority.

## Public README and approved workflow findings

W42 introduces the skill as a spec-driven technical writer in the repository-root README. W29 owns its detailed document sequence. The [repository-wide comparison](./audit.md#what-to-reuse-from-the-upstream-project) informs the approved F25–F27 work on governing specifications, field-level task evidence and shared contract versions. The [toolkit scope](./audit.md#product-direction-for-a-complete-spec-driven-toolkit) is approved under R24–R29.

Follow the [upstream reuse instructions](./implementation-plan.md#reuse-the-upstream-implementation) when implementing borrowed capabilities.

## Workflow decision and proposals

For an authorized feature build, use the bundled workflow when the project selects it. It runs Specify, Plan, Tasks and Implement, with separate reviews after the specification and the plan. Close routine delivery when the existing task and story acceptance criteria and applicable Definition of Done are demonstrated on the identified candidate. Invoke upstream Converge manually only when the user requests a broader review of that feature. Its findings may identify work to propose; they grant no additional implementation authority. A request to write a document ends at its checked handoff unless implementation is separately authorized. See the [pending owner decisions](./implementation-plan.md#pending-owner-decisions) for the proposed public guides and additional assessment work.

## How to choose a work record

Apply the project’s explicit governance first. These are the approved rules for the skill itself. W30–W31 cover R17/A17. W62 owns A17b and the [linking table and refund example](./specification.md#link-work-to-its-parent-and-designs-to-their-sources). W29 publishes the numbered sequence.

| When | Record to use |
| --- | --- |
| A bounded improvement has direct authority, a clear change and observable proof | One standalone Issue can carry all three. A misleading label with an agreed replacement is enough for a task. |
| Several contributions deliver an independently acceptable user outcome | Use a story, or reuse the existing record that already owns the outcome. A directly authorized story with its own scope and proof may stand alone. A declared child task must resolve its story and criterion. |
| Several slices deliver one named capability | Reuse its feature and acceptance. Add an epic when a broader initiative has shared ownership, scope and an integrated outcome, or when project governance requires it. A declared child story must resolve its governing parent. |
| Delivery depends on order, handoffs, compatibility, rollout or recovery | Use an implementation plan when those decisions need coordination. A contained change can keep its steps and proof in the existing record. A missing declared parent blocks the dependent work. |
