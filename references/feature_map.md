# Feature Map (FM)

A feature map tells a verifier where a feature lives and how to reach it: the user-facing name, the entry or route, the control or handle to use, and what a person sees when it worked. Write one when someone has to find and check a feature they didn't build, such as a tester, reviewer or agent.

## Principles

- Map only what the sources show. Each observed surface records the source and its revision: a running build, a screenshot, the code or a specification.
- Give each surface a user-facing name, its entry or route, the control or handle that starts the action, and the observable end state.
- Never guess a handle. If a source names the control but not its selector or accessible name, say what is known and mark the rest unverified.
- Mark proposed surfaces as proposed. A planned screen is not a place a verifier can reach.
- Launching the app, or reaching a page, doesn't show the feature works. Only the observable end state does.

## Structure

List each surface as one row, then note proposed surfaces and gaps. A critical journey can cite a row by its name.

## Template

```md
# [Product area] feature map

## Surfaces
| Surface | Entry or route | Control or handle | End state | Source and status |
| --- | --- | --- | --- | --- |
| [User-facing name] | [Where it starts] | [Label, role or selector, as known] | [What the user sees when it worked] | [Source, revision; observed, source-reported or proposed] |

## Gaps
- [Missing route, handle or end state, and how to find it.]
```

## Completed example

Read the [Feature Map (FM) example for Websites Review](../examples/feature_map.md). It maps surfaces named in the specification and marks what hasn't been observed in a running build.

## Quality check

Can a verifier who has never seen the product reach each observed surface from its row and recognize the end state? Check that no handle is invented and every proposed surface is marked.

## Sources

- [Testing Library: queries by accessible role and name](https://testing-library.com/docs/queries/about/)
