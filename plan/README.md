# Implement Technical Writer

Open this file in the checkout you will work on. It contains the starting prompt and the execution rules for Claude or Codex. The [specification](./specification.md) owns behavior and acceptance. The [implementation plan](./implementation-plan.md) owns the work, its boundaries, dependencies and checks. The [audit](./audit.md) explains the findings and their evidence.

The owner approved specification and implementation plan revision 6, covering 21 findings, 21 child stories and 31 tasks. Users may ask for a document by full name or acronym at any turn. In authored prose, introduce a document name once and retain required literal labels. A checked delivery may include one useful statement from the reviewed document, bound to its reviewed version. The handoff branch contains the audited Technical Writer source at `4a8e7c92e20404f05e68708c1a3ea26c6961b178` and the planning packet. Implementation begins on the other computer. Use the accepted Skill Builder implementation from the first handoff. Record its commit. Start with W01 and W03 as their dependencies allow. [Skill Builder handoff](https://github.com/fatonsopa/ai-skill-builder/blob/docs/autonomous-implementation/plan/README.md)

## Starting prompt

> Use Skill Builder to implement the approved Technical Writer changes in this repository. Read `plan/README.md`, the linked specification, the implementation plan and the repository instructions. Follow the execution rules below. Work on a local implementation branch from this handoff. Start or resume at the first eligible task. For each task, deliver its scoped result and prove its acceptance criteria on the actual candidate. Commit the usable increment and continue. Keep a private structured JSON execution log. Before another test or review, record the criterion, why existing evidence is insufficient and which result would change your next action. Use the log to correct your work and resume after interruption. Put only decisions awaiting the owner in the plan’s pending section. Complete the integrated acceptance checks before reporting delivery.

## Execution rules

1. **Bind the work.** Identify the handoff commit, governing specification, applicable repository instructions, candidate and skill dependencies. On resumption, read the existing task’s last accepted commit, evidence, open criteria and next eligible task. Protect existing work on all branches.
2. **Select one deliverable.** Resolve the task, parent outcome, supported criterion, affected interface, prerequisites, allowed change and required proof. Work from the reviewed record. Stop only affected work if a required decision or dependency is missing. Continue eligible independent tasks.
3. **Implement within scope.** Inspect the real entry point and keep the increment independently usable. Choose internal details within the agreed contract. Keep the original acceptance criteria and source authority. A new deliverable, new external action, changed permission or weaker criterion requires the owner’s explicit decision.
4. **Use evidence to limit verification.** Reuse applicable results. Run the smallest check that can disprove the candidate against the task’s criterion. A rare extra verification is appropriate when a concrete failure, changed input or missing evidence makes the approved result uncertain. Record the criterion, what the check established and the action it changes. Apply a supported better technique directly when it remains inside the task’s behavior, authority and quality obligations. General best-practice advice alone cannot enlarge scope.
5. **Defer other discoveries.** Append a brief entry to [Pending owner decisions](./implementation-plan.md#pending-owner-decisions). Record evidence, impact, proposed change and any blocked task. Leave the change pending and move to eligible work. A material blocker can keep a criterion open without erasing prior results.
6. **Close and resume.** In the existing task, record each criterion as Met, Failed or Not demonstrated, with the exact candidate and evidence. Retain failures through correction. Commit each accepted increment on the local implementation branch, record the next task and continue. Reuse task evidence for story acceptance where it actually proves the integrated result. Report host-specific results separately. Remote integration, releases and deployment require separate authority.

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

## How to choose a work record

Apply the project’s explicit governance first. These are the approved rules for the skill itself. Deliver them through R17/A17 and W30–W31, then publish the numbered sequence through W29.

| When | Record to use |
| --- | --- |
| A bounded improvement has direct authority, a clear change and observable proof | One standalone Issue can carry all three. A misleading label with an agreed replacement is enough for a task. |
| Several contributions deliver an independently acceptable user outcome | Use a story, or reuse the existing record that already owns the outcome. A directly authorized story with its own scope and proof may stand alone. A declared child task must resolve its story and criterion. |
| Several slices deliver one named capability | Reuse its feature and acceptance. Add an epic when a broader initiative has shared ownership, scope and an integrated outcome, or when project governance requires it. A declared child story must resolve its governing parent. |
| Delivery depends on order, handoffs, compatibility, rollout or recovery | Use an implementation plan when those decisions need coordination. A contained change can keep its steps and proof in the existing record. A missing declared parent blocks the dependent work. |
