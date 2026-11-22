# SpecDev implementation handoff

<a id="spec-writer-implementation-handoff"></a>

Implement revision 21 on a local branch with the accepted [Skill Builder handoff](https://github.com/fatonsopa/ai-skill-builder/blob/docs/autonomous-implementation/plan/README.md). The source skill is still `technical-writer`. The release name is **SpecDev** (`specdev`). The existing GitHub repository URL stays valid.

## Start

Give Claude or Codex this file on the handoff branch. Read the prompt in place.

### Starting prompt

> Deliver the approved [specification](./specification.md) using the [implementation plan](./implementation-plan.md) and [ordered tasks](./tasks.md). Record the handoff commit and accepted Builder commit. Confirm B5/T50 before W46 renames the skill. W01 and W03 can start independently. W60 already has evidence. W55–W57 and W51.3 are outside execution scope. Use the released OpenSpec dependency for every capability it supplies. Keep one user-facing skill, edit each artifact at its owner and preserve existing user commands. A request to write or review ends at document delivery. Implement only an eligible task, verify its criteria on the candidate, commit the increment locally and continue. Return the integrated result and any unproven criteria. Read the rules below before starting.

<a id="when-the-writer-should-ask"></a><a id="how-to-choose-a-work-record"></a>

## Execution rules

1. Establish the required result and proof from the task before editing. Inspect the actual entry point. Resolve routine choices within scope and ask only about a material choice the project cannot settle.
2. Reuse applicable checks and evidence. An extra check needs an unmet criterion, changed input or observed failure. Keep failures and their recovery evidence. Hold only work affected by a blocker.
3. Record each criterion as Met, Failed or Not demonstrated against its exact candidate. Use the existing Issue and evidence links. Close a story when the usable outcome is demonstrated. Local integration is authorized. External publication and deployment have their own authority.
4. Record a new out-of-scope finding once under [pending owner decisions](./implementation-plan.md#pending-owner-decisions). Continue eligible work.

<a id="limits-and-help"></a>

## Check the result

Use [test.md](./test.md) for the handoff and connected refund cases. The [shared Definition of Done](./implementation-plan.md#shared-definition-of-done) sets the common release obligations.

## Find your way around

The [audit](./audit.md) gives the evidence behind the change. The [specification](./specification.md) owns story acceptance, the [plan](./implementation-plan.md) owns delivery decisions, and [tasks.md](./tasks.md) owns this handoff’s ordered Issues. Use the criteria at their source.

## JSON execution log

Use existing private run JSON first. For a decision or manual step the run does not capture, append one event to `execution.jsonl` in the private run directory. Record UTC time, run and task IDs, criterion, candidate, observed result or blocker, evidence reference and next action. For an extra test or retry, record what changed and how the result affects the decision. Resume from the last confirmed boundary. Preserve failures. Exclude secrets, customer data and private reasoning. Link evidence once.

<a id="approved-rename-and-toolkit"></a><a id="public-readme-and-approved-workflow-findings"></a><a id="workflow-decision-and-proposals"></a>

## Shortcuts and document handoffs

Use `/specdev init` to set up the current project through the pinned OpenSpec CLI. Codex uses its native skill invocation, `$specdev init`. A standalone writing request needs no project initialization. Any other `/specdev <command>` can discover and run a matching installed OpenSpec operation without its own shortcut. Upstream wins on a name collision. The [production order](./specification.md#production-order) governs shortcuts and documents. The [dependency and ownership plan](./implementation-plan.md#reuse-the-upstream-implementation) governs upstream operations. The [refund example](./specification.md#refund-status-and-filtering) shows the native file and its consumer.
