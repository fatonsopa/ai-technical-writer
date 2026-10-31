# User Story (US)

A user story describes a small, useful outcome from a person's perspective. Create one to clarify or track a user need; update it when the need, scope, value, or acceptance criteria change. It can live in a Feature/Improvement [issue](issue.md) or a [PRD](product_requirements_document.md)/[SDD](spec_driven_development.md) before tasks exist. Its reference filename does not require a standalone story file or a new tracker type.

## Principles

- Identify a meaningful role, the capability needed, and the benefit. Avoid invented personas and benefits that merely repeat the capability.
- Keep a story focused on a user outcome. Technical implementation tasks can support it without pretending every database migration is itself a user story.
- Treat the story as a starting point for discussion. Record unresolved product choices; the familiar sentence formula is optional.
- Make acceptance observable and consistent with the governing behavior. Link detailed rules rather than copying a whole specification. For a small task, record the expected behavior and acceptance criteria in the issue.
- Preserve permissions, failure conditions, and limits when refining or splitting stories. Do not assign estimates or workflow status without a source.

## Structure

Use a specific title, user/need/value statement, scope, acceptance criteria, and relevant requirement links or open questions. The [SDD](spec_driven_development.md) owns detailed behavior; the [plan](implementation_plan.md) owns delivery. Common task metadata belongs to the issue containing the story.

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

Read the [complete Websites Review example](../examples/user_story.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Can a reader name the user, need, and benefit and determine whether the criteria are met? Check that the story adds useful context, preserves governing rules, and leaves unresolved choices visible. A Chore or Release should not be forced into this format.

## Sources

- [Agile Alliance: user stories](https://agilealliance.org/glossary/user-stories/)
- [Agile Alliance: card, conversation, confirmation](https://agilealliance.org/glossary/three-cs/)
