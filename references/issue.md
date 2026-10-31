# Issue

Use this reference to write a unit of development work in Linear, GitHub Issues, Jira, or a Markdown document. An issue explains what needs attention, why it matters, and how acceptance will be checked. Apply `references/writing_style.md` to its language.

Create a task when work needs tracking; update its scope, progress, and evidence as the work changes. The six types below are this package's convention, not a universal tracker schema. A task need not already exist, and writing a task does not authorize posting it or changing its status.

An issue may trigger a specification, or a specification and plan may produce several issues. For a small change, the issue's expected behavior and acceptance criteria can be the specification. Larger work links to the governing spec and plan instead of copying them.

When editing an existing excerpt, use the current request's task type and destination if an older draft contains conflicting drafting directions. Remove author-facing drafting instructions from finished issue prose. Keep meaningful headings within the edited excerpt clear without expanding it into a full task.

## Principles

- Understand the full description before writing the title. Keep the problem, requested outcome, current status, and unresolved decisions distinct.
- Keep independently deliverable work separate. Retain related symptoms together when they describe one failure; link dependencies rather than adding unrelated tasks.
- Explain the need before the implementation. Include technical instructions when they are confirmed constraints or useful investigation findings.
- Define observable acceptance criteria. Identify which specification requirements or issue acceptance criteria the work satisfies.
- Preserve existing scope, conditions, evidence, and uncertainty when editing. A title change does not authorize changing the work.
- Leave status, assignment, priority, and release approvals to the project's task-management process.

## Issue types and titles

| Type | Title and description |
| --- | --- |
| Bug | Name the observed failure and important condition. Also read `references/bug_report.md`. |
| Chore | Name the maintenance work, its reason, relevant constraints, and acceptance criteria. |
| Decision | Name the situation requiring a choice; use [Decision records](decision_record.md) for proposals and outcomes. |
| Feature | Name the new capability. Describe its users, behavior, limits, and acceptance criteria or governing spec. |
| Improvement | Name the change to existing behavior. Explain the current limitation and desired result; use measurements when available. |
| Release | Name the release and destination when known. Link its contents, preparation, deployment procedure, verification, and recovery requirements. |

A title should distinguish this issue in a list. Retain a useful technical term or condition when it makes the work identifiable. Avoid plan codes as the only context and generic titles shared by unrelated tests. Do not turn a bug into an instruction or claim a suspected cause is established.

## Document structure

Include a title, issue type, description, expected outcome, and verifiable acceptance criteria. For change work, identify the governing spec requirement or give the intended behavior and acceptance criteria inline. Add scope, evidence, dependencies, and relevant files when they help.

Relevant files must be verified or clearly attributed to a supplied source; distinguish a reported path from a file you inspected. Keep the current decision or status understandable without reproducing the whole conversation.

Route specialized content rather than copying its structure here: [Bug reports](bug_report.md), [User stories](user_story.md), and [Decision records](decision_record.md), with [ADR](architecture_decision_record.md)/[DDR](design_decision_record.md) guidance when appropriate. A choice inside a Bug or plan usually needs a comment, not a separate Decision task. For a Release, identify which checks remain before it can be called deployed.

Tests and verification can be sections or comments in the task: use [Test specification](test_specification.md) for checks and [Test completion report](test_completion_report.md) for outcomes. Larger efforts can link a [test plan](test_plan.md) or [status report](test_status_report.md). Keep the task focused; those references own the specialized formats.

## Template

```md
# [Specific problem, change, or decision]

Type: [Bug / Chore / Decision / Feature / Improvement / Release]

## Description
[Current problem or opportunity, who is affected, and why the work matters.]

## Expected outcome
[What should be true when the issue is accepted.]

## Scope
[Included work and important limits.]

## Specification
[Requirement IDs or exact spec sections; alternatively, intended behavior here.]

## Acceptance criteria
- [Observable result tied to the specification.]
- [A relevant failure or boundary case.]

## Relevant files
[Verified or attributed paths and why they matter, when useful.]

## Additional context
[Useful evidence, dependencies, and open questions.]
```

Adapt optional sections to the issue. One concise paragraph can be enough for a small task. Do not create empty sections or duplicate the bug template.

## Completed example

Read the [complete Websites Review example](../examples/issue.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Can a developer identify the work from the title, understand the need, find its governing behavior, and assess its acceptance criteria? Confirm that facts, technical constraints, and open decisions survived the rewrite. A Decision remains open until decided; a Release remains unverified until its checks actually run.

## Sources

- [Linear: issues as units of work](https://linear.app/docs/creating-issues)
- [Mozilla: clear bug summaries](https://bugzilla.mozilla.org/page.cgi?id=bug-writing.html)
- [GitHub Spec Kit: specifications, plans, and tasks](https://github.com/github/spec-kit)

