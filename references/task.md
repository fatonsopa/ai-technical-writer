# Task

Use this reference to write a unit of development work in Linear, GitHub Issues, Jira, or a Markdown document. Use `task.md` for one standalone Markdown task and `tasks.md` for the ordered list of work on a change. “Issue” and “work item” remain accepted request names. A task explains what needs attention, why it matters, and how acceptance will be checked. Apply `references/writing_style.md` to its language.

Create a task when work needs tracking; update its scope, progress, and evidence as the work changes. The six types below are this package's convention, not a universal tracker schema. A task need not already exist, and writing a task does not authorize posting it or changing its status.

A task may trigger a specification, or a specification and plan may produce several tasks. For a small change, the task's expected behavior and acceptance criteria can be the specification. Larger work links to the governing spec and plan instead of copying them.

For a multi-task feature in an OpenSpec change, the native `tasks.md` is the task list: each numbered checkbox names its scope, governing scenario and proof, and needs no separate Task. Reference an existing Markdown or tracker Task from its checkbox only where it independently owns work or a criterion, and keep that criterion with its owner. Outside a change, a bounded standalone request can end with one Task, and each Task identifies its governing story criterion and owns its scope, acceptance criteria and required proof. An external tracker is optional. If the task proves an existing story criterion exactly, reference it and specify the task’s own scope, evidence and candidate. Give a new criterion ID only to a distinct task obligation. In a feature task list, use a checkbox, feature-local ID, story reference and link to the owning Task. Add `[P]` only when the tasks can safely run together. The implementing agent opens the eligible Task from that list. A standalone task can end with this Task. Its filename follows the project convention. [Feature task flow](../README.md#where-tasksmd-fits)

Before drafting a child task, resolve its ancestry in order: the feature or epic outcome, the story, the story criterion the task delivers, and the revision of each source. Link the exact criterion and state those revisions in the Task, so a reader can recover the shared outcome. If the story or epic is missing, stale or contradicts the task, name the broken edge and hold the task and any work that depends on it. A task that is explicitly standalone, such as one broken-link fix, can go ahead with its own source and expected destination. A child whose parent can't be found doesn't become standalone. When work moves to a different parent, keep its existing ID and update the link. `scripts/check_document.py` checks declared parent edges when the context lists them in `parents`. For a complete child, read the [failed-save Task example](../examples/task_failed_save.md), which delivers one criterion of the [User Story (US) example](../examples/user_story.md).

When editing an existing excerpt, use the current request's task type and destination if an older draft contains conflicting drafting directions. Remove author-facing drafting instructions from finished task prose. Keep meaningful headings within the edited excerpt clear without expanding it into a full task.

## Principles

- Understand the full description before writing the title. Keep the problem, requested outcome, current status, and unresolved decisions distinct.
- Keep independently deliverable work separate. Retain related symptoms together when they describe one failure; link dependencies rather than adding unrelated tasks.
- Explain the need before the implementation. Include technical instructions when they are confirmed constraints or useful investigation findings.
- Define observable acceptance criteria. Identify which specification requirements or task acceptance criteria the work satisfies.
- When a task implements a constrained field, link the exact owner and field together, such as `Return.code` in the schema, Interface Contract (IC) or Low Level Design (LLD) that defines it. Keep its semantics: required or optional, null or absent, format. A link to the whole document can hide the wrong field when several share a name. An unambiguous existing field pointer is enough, and a prose-only task needs no field citations.
- Preserve existing scope, conditions, evidence, and uncertainty when editing. A title change does not authorize changing the work.
- Leave status, assignment, priority, and release approvals to the project's task-management process.
- Keep task type in tracker metadata. In Linear, use the existing `Type` label group. Do not repeat a `Type: …` field in the title or description; preserve unrelated labels and native status fields.

### Write acceptance as the visible result

An acceptance criterion should let the implementer and the tester picture the same outcome. Replace a judgment word, such as "honestly", "gracefully" or "properly", with what the user sees and who decides the next step, from the governing requirement. For example:

- Before: "partial or uncertain writes stop and are reported honestly."
- After: "After the first request that fails or returns no response, no further batches are sent, and the administrator sees separate counts of confirmed, unresolved and unattempted rows. Before any retry is offered, the page reads the saved state of the unresolved rows; the administrator decides whether to retry."

Keep the neighboring conditions, such as limits, permissions and refreshes, and don't add guarantees the source doesn't make. A criterion that is already clear needs no rewrite.

## Task types and titles

| Type | Title and description |
| --- | --- |
| Bug | Name the observed failure and important condition. Also read `references/bug_report.md`. |
| Chore | Name the maintenance work, its reason, relevant constraints, and acceptance criteria. |
| Decision | Name the situation requiring a choice; use [Decision Record (DR)](decision_record.md) for proposals and outcomes. |
| Feature | Name the new capability. Describe its users, behavior, limits, and acceptance criteria or governing spec. |
| Improvement | Name the change to existing behavior. Explain the current limitation and desired result; use measurements when available. |
| Release | Name the release and destination when known. Link its contents, preparation, deployment procedure, verification, and recovery requirements. |

A title should distinguish this task in a list. Retain a useful technical term or condition when it makes the work identifiable. Avoid plan codes as the only context and generic titles shared by unrelated tests. Do not turn a bug into an instruction or claim a suspected cause is established.

## Document structure

Include a title, description, expected outcome, and verifiable acceptance criteria. Record the task type as tracker metadata, outside the task text. For change work, identify the governing spec requirement or give the intended behavior and acceptance criteria inline. Add scope, evidence, dependencies, and relevant files when they help.

Relevant files must be verified or clearly attributed to a supplied source; distinguish a reported path from a file you inspected. Keep the current decision or status understandable without reproducing the whole conversation.

Route specialized content rather than copying its structure here: [Bug Report (BR)](bug_report.md), [User Story (US)](user_story.md), and [Decision Record (DR)](decision_record.md). A choice inside a Bug or plan usually needs a comment, not a separate Decision task. For a Release, identify which checks remain before it can be called deployed.

Tests and verification can be sections or comments in the task: use [Test Specification (TS)](test_specification.md) for checks and [Test Completion Report (TCR)](test_completion_report.md) for outcomes. Larger efforts can link a [Test Plan (TP)](test_plan.md) or [Test Status Report (TSR)](test_status_report.md). Keep the task focused; those references own the specialized formats.

## Template

```md
# [Specific problem, change, or decision]

## Description
[Current problem or opportunity, who is affected, and why the work matters.]

## Expected outcome
[What should be true when the task is accepted.]

## Scope
[Included work and important limits.]

## Specification
[For a child task, link the governing story criterion. For standalone work, give its direct authority and intended behavior.]

## Acceptance criteria
- [Observable result tied to the specification.]
- [A relevant failure or boundary case.]

## Relevant files
[Verified or attributed paths and why they matter, when useful.]

## Additional context
[Useful evidence, dependencies, and open questions.]
```

Adapt optional sections to the task. One concise paragraph can be enough for a small task. Do not create empty sections or duplicate the bug template.

## Completed example

Read the [complete Websites Review example](../examples/task.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Can a developer identify the work from the title, understand the need, find its governing behavior, and assess its acceptance criteria? Confirm that facts, technical constraints, and open decisions survived the rewrite. A Decision remains open until decided; a Release remains unverified until its checks actually run.

When reviewing a task against a contract, check that each cited field resolves to the owner and field the requirement names. Report the task, the wrong field and the requirement left uncovered, such as a task that cites the optional `Order.code` for the required `Return.code`.

To review an edited criterion, give a reader only the edited task and ask the question its source answers, such as "What happens after a response is lost, and who may retry?". Compare the answer with the governing requirement and cite the words that carry each obligation. A missing or wrong answer points to the exact ambiguity to fix. A rewrite in a similar tone can still change an obligation, for example by making an optional retry required; reject it and name the changed obligation. Accept any clear wording that keeps every obligation.

## Sources

- [Linear’s guide to creating issues](https://linear.app/docs/creating-issues)
- [Mozilla: clear bug summaries](https://bugzilla.mozilla.org/page.cgi?id=bug-writing.html)
- [GitHub Spec Kit: specifications, plans, and tasks](https://github.com/github/spec-kit)

