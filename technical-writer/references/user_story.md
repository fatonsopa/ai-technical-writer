# User Story (US)

A user story describes a small, useful outcome from a person's perspective. Create one when a user need needs discussion or tracking; update it when the need, scope, value, or acceptance criteria change. It can live in a Feature/Improvement [work item](issue.md) or a [PRD](product_requirements_document.md)/[SDD](spec_driven_development.md) before tasks exist. Its reference filename does not require a standalone story file or a new tracker type.

## Principles

- Identify a meaningful role, the capability needed, and the benefit. Avoid invented personas and benefits that merely repeat the capability.
- Keep a story focused on a user outcome. Technical implementation tasks can support it without pretending every database migration is itself a user story.
- Treat the story as a starting point for discussion. Record unresolved product choices; the familiar sentence formula is optional.
- Make acceptance observable and consistent with the governing behavior. Link detailed rules rather than copying a whole specification. A small task can hold enough expected behavior and acceptance inline.
- Preserve permissions, failure conditions, and limits when refining or splitting stories. Do not assign estimates or workflow status without a source.

## Structure

Use a specific title, user/need/value statement, scope, acceptance criteria, and relevant requirement links or open questions. The [SDD](spec_driven_development.md) owns detailed behavior; the [plan](implementation_plan.md) owns delivery. Common task metadata belongs to the host work item.

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

Fictional story within a Feature task; the named requirements are agreed for this example.

```md
# Keep the workspace name current

As a workspace administrator, I want to rename my workspace so that colleagues can identify the team using it.

## Acceptance criteria
- After an authorized rename succeeds, a fresh workspace read returns the new name (REN-01).
- A member without administrator permission cannot change the name (REN-02).
- If saving fails, the previous name remains and the operation reports failure (REN-03).

## Scope and sources
Workspace rename SDD, REN-01–REN-03. This story covers renaming, not transferring workspace ownership. The permitted name length still needs a product decision; no limit is assumed here.
```

## Quality check

Can a reader name the user, need, and benefit and determine whether the criteria are met? Check that the story adds useful context, preserves governing rules, and leaves unresolved choices visible. A Chore or Release should not be forced into this format.

## Sources

- [Agile Alliance: user stories](https://agilealliance.org/glossary/user-stories/)
- [Agile Alliance: card, conversation, confirmation](https://agilealliance.org/glossary/three-cs/)
