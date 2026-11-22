# User Story (US)

A user story describes a small, useful outcome from a person's perspective. Create one to clarify or track a user need; update it when the need, scope, value, or acceptance criteria change. It can live in a Feature/Improvement [task](task.md) or a [Product Requirements Document (PRD)](product_requirements_document.md)/[Spec Driven Development document (SDD)](spec_driven_development.md) before tasks exist. Its reference filename does not require a standalone story file or a new tracker type.

## Principles

- Identify a meaningful role, the capability needed, and the benefit. Avoid invented personas and benefits that merely repeat the capability.
- Keep a story focused on a user outcome. Technical implementation tasks can support it without pretending every database migration is itself a user story.
- Treat the story as a starting point for discussion. Record unresolved product choices; the familiar sentence formula is optional.
- Make acceptance observable and consistent with the governing behavior. Link detailed rules rather than copying a whole specification. For a small task, record the expected behavior and acceptance criteria in the task.
- Preserve permissions, failure conditions, and limits when refining or splitting stories. Do not assign estimates or workflow status without a source.

## Structure

Use a specific title, user/need/value statement, scope, acceptance criteria, and relevant requirement links or open questions. The [Spec Driven Development document (SDD)](spec_driven_development.md) owns detailed behavior; the [Implementation Plan (IP)](implementation_plan.md) owns delivery. For a multi-task feature, author the story and its acceptance scenarios in the governing specification, or link to the project’s existing authoritative story. The delivery plan references its outcome. Child tasks identify the story criterion they deliver. Common task metadata belongs to the task containing the story. Before writing a child story for an epic, identify the epic's outcome and the revision you read, link that outcome, and state the revision in the story. If the epic is missing or contradicts the story, report the broken edge and hold the story rather than writing it as a standalone need.

## Epics

An Epic (EPIC) connects several stories that together deliver one usable outcome. Write it when the stories need coordination, and use the project's governing outcome or link an existing User Story (US) rather than restating it. The epic states:

- the outcome and who can use it, with the governing requirements;
- non-goals, so children don't absorb excluded work;
- dependencies between stories or on other teams, systems and decisions;
- the integrated proof: one observation of the whole outcome, such as an end-to-end check, that no child proves alone;
- who owns the epic's acceptance and who owns each child story.

Each child story links the epic's outcome and inherits the epic criterion it serves. Each child task links the one story criterion it delivers. The epic stays unaccepted until its own integrated proof is observed, even when every child task is closed. Closed children show progress, not delivery.

When related reports start an epic, keep each original observation with its source. A shared cause that seems likely stays provisional until evidence confirms it. Assign independent work only after deciding whether the reports describe one failure or several.

In an OpenSpec change, write the observable behavior once, in the capability's requirement and scenarios. Keep each task's scope and proof with its numbered checkbox in `tasks.md`, and link an existing Task only when it independently owns the criterion. If the scope spans independent capabilities, map them first and specify each one separately.

## Template

```md
# [User capability or outcome]

As a [role], I want [capability], so that [benefit].

## Acceptance criteria
- [Given the relevant state, an action produces an observable result.]
- [Important permission, boundary, or failure behavior.]

## Scope and sources
[Relevant requirement IDs; explicit limits and unresolved decisions.]
```

## Completed example

Read the [User Story (US) example for Websites Review](../examples/user_story.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Can a reader name the user, need, and benefit and determine whether the criteria are met? Check that the story adds useful context, preserves governing rules, and leaves unresolved choices visible. A Chore or Release should not be forced into this format.

## Sources

- [Agile Alliance: user stories](https://agilealliance.org/glossary/user-stories/)
- [Agile Alliance: card, conversation, confirmation](https://agilealliance.org/glossary/three-cs/)
