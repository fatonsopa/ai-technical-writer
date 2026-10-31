# How-to Guide (HTG; runbook)

A how-to guide helps someone complete a task. An operational runbook adds the checks and recovery needed for its environment. Create one when a procedure needs documenting; update it when commands, prerequisites, environment, or recovery change.

## Principles

- State the goal, required access, starting state, and impact before the actions.
- Give ordered steps with exact verified inputs, commands, and expected observations.
- Explain choices where a reader must branch. Include stop conditions and recovery when failure could leave the system in a worse state.
- Keep placeholders recognizable and distinguish examples from project commands. Do not invent a rollback mechanism.
- Include an observable success check. Link background to [Explanation](explanation.md) rather than interrupting the procedure with a full lesson.
- Execute only actions authorized by the user's task; writing a runbook does not authorize performing its production steps.

## Structure and template

Use a goal-oriented title, prerequisites, ordered actions, success checks, and applicable failure/recovery instructions.

```md
# How to [goal]
## Before you begin
[Environment, access, starting data, impact]
## Steps
1. [Action/command and expected observation]
## Confirm success
[Check and expected result]
## If it fails
[Stop, diagnose, recover, or escalate using known procedures]
```

## Completed example

Read the [complete Websites Review example](../examples/how_to_guide.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Can a competent reader perform the procedure without guessing a command or missing check? Verify the setup, command effects, relevant failure branches, and recovery. A stated expected result must not be reported as a result you observed unless you ran the check.

## Sources

- [Diátaxis: how-to guides](https://diataxis.fr/how-to-guides/)
- [Google: procedures](https://developers.google.com/style/procedures)
