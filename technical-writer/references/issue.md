# Issue

Use this reference to write a unit of development work in Linear, GitHub Issues, Jira, or a Markdown document. An issue explains what needs attention, why it matters, and how completion will be checked. Apply `references/writing_style.md` to its language.

Create a task when work needs tracking; update its scope, progress, and evidence as the work changes. The six types below are this package's convention, not a universal tracker schema. A task need not already exist, and writing a task does not authorize posting it or changing its status.

An issue may trigger a specification, or a specification and plan may produce several issues. For a small change, the issue's expected behavior and acceptance criteria can be the specification. Larger work links to the governing spec and plan instead of copying them.

## Principles

- Understand the full description before writing the title. Keep the problem, requested outcome, current status, and unresolved decisions distinct.
- Keep independently deliverable work separate. Retain related symptoms together when they describe one failure; link dependencies rather than adding unrelated tasks.
- Explain the need before the implementation. Include technical instructions when they are confirmed constraints or useful investigation findings.
- Make completion observable. Identify which specification requirements or issue acceptance criteria the work satisfies.
- Preserve existing scope, conditions, evidence, and uncertainty when editing. A title change does not authorize changing the work.
- Leave status, assignment, priority, and release approvals to the project's task-management process.

## Issue types and titles

| Type | Title and description |
| --- | --- |
| Bug | Name the observed failure and important condition. Also read `references/bug_report.md`. |
| Chore | Name the maintenance work, its reason, relevant constraints, and completion checks. |
| Decision | Name the situation requiring a choice; use [Decision records](decision_record.md) for proposals and outcomes. |
| Feature | Name the new capability. Describe its users, behavior, limits, and acceptance criteria or governing spec. |
| Improvement | Name the change to existing behavior. Explain the current limitation and desired result; use measurements when available. |
| Release | Name the release and destination when known. Link its contents, preparation, deployment procedure, verification, and recovery requirements. |

A title should distinguish this issue in a list. Retain a useful technical term or condition when it makes the work identifiable. Avoid plan codes as the only context and generic titles shared by unrelated tests. Do not turn a bug into an instruction or claim a suspected cause is established.

## Document structure

Include a title, issue type, description, and verifiable completion conditions. For change work, identify the governing spec requirement or give the intended behavior and acceptance criteria inline. Add scope, evidence, dependencies, and relevant files when they help.

Relevant files must be verified or clearly attributed to a supplied source; distinguish a reported path from a file you inspected. Keep the current decision or status understandable without reproducing the whole conversation.

Route specialized content rather than copying its structure here: [Bug reports](bug_report.md), [User stories](user_story.md), and [Decision records](decision_record.md), with [ADR](architecture_decision_record.md)/[DDR](design_decision_record.md) guidance when appropriate. A choice inside a Bug or plan usually needs a comment, not a separate Decision task. For a Release, identify which checks remain before it can be called deployed.

Tests and verification can be sections or comments in the task: use [Test specification](test_specification.md) for checks and [Test completion report](test_completion_report.md) for outcomes. Larger efforts can link a [test plan](test_plan.md) or [status report](test_status_report.md). Keep the task focused; those references own the specialized formats.

## Template

```md
# [Specific problem, change, or decision]

Type: [Bug / Chore / Decision / Feature / Improvement / Release]

## Description
[Current problem or opportunity, who is affected, and why the work matters.]

## Scope
[Included work and important limits.]

## Specification
[Requirement IDs or exact spec sections; alternatively, intended behavior here.]

## Completion criteria
- [Observable result tied to the specification.]
- [A relevant failure or boundary case.]

## Supporting information
[Useful evidence, verified or attributed files, dependencies, and open questions.]
```

Adapt optional sections to the issue. One concise paragraph can be enough for a small task. Do not create empty sections or duplicate the bug template.

## Completed example

This fictional feature assumes the three cited export requirements have been agreed. It illustrates issue content, not a verified feature or completed test.

```md
# Export the filtered results as a CSV file

Type: Feature

## Description
Analysts need to review the results outside the application. Add a CSV download for the records shown in the results table.

## Scope
Export the current results and selected columns. Exporting charts is outside this issue.

## Specification
Results export spec: REQ-01 preserves active filters; REQ-02 preserves selected columns and order; REQ-03 reports a failed export without presenting it as successful.

## Completion criteria
- With filters active, the CSV contains only matching records: REQ-01.
- CSV columns match the selected columns and their order: REQ-02.
- A failed export shows an error and no success confirmation: REQ-03.

## Supporting information
The repository has not been inspected. Locate the results table and existing export utilities before selecting implementation files. No implementation or test result is claimed.
```

## Quality check

Can a developer identify the work from the title, understand the need, find its governing behavior, and check completion? Confirm that facts, technical constraints, and open decisions survived the rewrite. A Decision remains open until decided; a Release remains unverified until its checks actually run.

## Sources

- [Linear: issues as units of work](https://linear.app/docs/creating-issues)
- [Mozilla: clear bug summaries](https://bugzilla.mozilla.org/page.cgi?id=bug-writing.html)
- [GitHub Spec Kit: specifications, plans, and tasks](https://github.com/github/spec-kit)

