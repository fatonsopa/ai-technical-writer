# Implementation plan and technical proposal

A plan explains the problem, the chosen approach, the work needed, and how the team will verify success. It is written before implementation or major changes. Give developers an actionable sequence and give reviewers enough information to challenge assumptions. A larger design proposal may use an RFC structure; ordinary work does not need every RFC section.

## Principles

1. **State the present problem and goal.** Explain what is happening today, who is affected, and what successful change will achieve. Support material claims with verified evidence.
2. **Separate facts, choices, and open questions.** Mark the current system, proposed changes, decisions already approved, and decisions still needed.
3. **Describe the full path.** Show which components, data, interfaces, or user actions change and how they connect. Include the relevant architecture or flow diagram when useful.
4. **Sequence implementation work.** Put dependencies first. Each phase or task should have a concrete result, relevant files or components when verified, and an acceptance check.
5. **Plan testing from the beginning.** Include unit, integration, end-to-end, migration, load, or security checks according to risk. State test data and environments when they matter.
6. **Address rollout and recovery.** Include backward compatibility, data migration, feature flags, monitoring, and rollback when the change could affect running users or stored data.
7. **Discuss meaningful alternatives and tradeoffs.** Explain why the approach was selected with known benefits, costs, and failure modes. Avoid invented benchmarks.
8. **Avoid unnecessary precision.** Do not invent estimates, implementation paths, ownership, or infrastructure capacity. Mark what needs confirmation.
9. **Keep the plan updateable.** Link to approved requirements and decisions; do not duplicate entire standards.

## Template

```md
# Implement [feature or change]

## Problem and goal
[Current behavior, users affected, desired outcome.]

## Current system
[Verified behavior, dependencies, relevant code and data.]

## Proposed approach
[How the new behavior works, major components and decisions.]

## Implementation steps
1. [Change and dependencies; result and acceptance condition.]
2. [Change and dependencies; result and acceptance condition.]

## Testing and acceptance
[Tests, scenarios, environments, data, pass conditions.]

## Rollout and rollback
[Deployment order, compatibility, monitoring, recovery; only if relevant.]

## Risks and alternatives
[Major risks, rejected options, reason, unresolved decisions.]
```

For a formal proposal, add motivation, detailed design, drawbacks, rationale and alternatives, unresolved questions, and future possibilities, following the project's adopted RFC format. Where a repository has script-consumed plan tables or file names, preserve those exact contracts.

## Completed example: add an audit log for workspace name changes

This is an illustrative plan. Its component and route names are examples, not confirmed repository files.

### Implement an audit log for workspace renames

**Problem and goal.** Administrators can change a workspace name, but other administrators cannot tell who made the change. The goal is to store a record of each successful rename and display it to authorized users.

**Current system.** The application has an update endpoint and a workspace table. The exact code and database schema require repository inspection before work begins.

**Proposed approach.** On successful rename, write an audit record containing workspace ID, actor ID, previous name, new name, and timestamp in the same transaction as the name update. A read endpoint returns records to authorized administrators.

**Implementation steps.**

1. Confirm the current update flow, transaction boundaries, permissions, and event naming.
2. Add a migration for an audit table with the required columns and suitable indexes. Test migration and rollback on a disposable database.
3. Update the workspace service so it writes the audit record in the same transaction as the successful rename.
4. Add an authorized read endpoint and a basic history view.
5. Add tests for valid updates, denied updates, failed transactions, and repeated requests.

**Testing and acceptance.** A successful rename creates exactly one audit record with the correct names and actor. A rejected rename creates none. A database failure must not leave the name updated without the audit record. Verify that unauthorized users cannot read the history.

**Rollout and rollback.** Apply the additive migration before deploying code that writes audit records. Confirm table size and write errors after release. Determine a safe rollback plan before deployment because removing the feature may require preserving its historical records.

**Risks and open decisions.** Storage growth, retention length, existing historical changes, and whether duplicate requests create duplicate records need approval.

## Quality check

A developer knows which parts change, which steps depend on earlier work, how to test them, and what could go wrong. The plan distinguishes verified current behavior from proposed behavior and unknowns.

## Sources

- Rust RFC process and example format: https://github.com/rust-lang/rfcs/blob/master/text/0002-rfc-process.md
- arc42 decision and architecture context: https://arc42.org/overview/
- AWS architectural decision records: https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/faq.html
