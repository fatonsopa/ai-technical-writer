# How-to guide and runbook

A how-to guide helps a reader who already understands the basics complete a particular task. A runbook is a how-to used in operations, often with checks, rollback steps, and escalation conditions. Use the shortest safe path that works for the documented environment.

## Principles

1. Name the goal in the title: “Rotate a database password” is clearer than “Database credential operations.”
2. State prerequisites, permissions, environment, and impact before the steps. Make destructive actions conspicuous.
3. Use numbered, executable actions. Each step should identify what to do and what result should follow.
4. Show actual flags, paths, input examples, and commands verified for the system. Mark placeholders.
5. Explain decisions at branch points: what to do if a check fails, when to stop, and who to contact.
6. Include verification and rollback when failure would leave the system in a worse state. Do not invent a rollback mechanism.
7. Link detailed background and parameter listings to explanation and reference pages.

## Template

```md
# How to [specific goal]

[One sentence stating what this procedure achieves.]

## Before you begin
[Permissions, dependencies, environment, expected impact, safety notes.]

## Steps
1. [Command or action; expected confirmation.]
2. [Command or action; expected confirmation.]
3. [Check or branch if needed.]

## Confirm success
[Observable check, expected value, and where to look.]

## If it fails
[Safe stop point, troubleshooting, rollback, or escalation.]
```

## Completed example: change a local application's port

This example uses a fictional Node application that reads `PORT` from its environment. Verify this behavior in the real project's code before publishing it as project documentation.

### Change the local development port

Use these steps when port 3000 is already occupied on your computer.

**Before you begin.** Open a terminal in the application folder. Confirm that the project's start command is `npm run dev` and that it reads the `PORT` variable.

1. Stop the current development server with Ctrl+C.
2. In a new terminal, run `PORT=3100 npm run dev` on macOS or Linux.
3. Open `http://localhost:3100` in your browser.

**Confirm success.** The application loads on port 3100, and the terminal reports that it is listening on that port.

**If it fails.** Check for an existing process using port 3100 and read the terminal error. If the application does not honor `PORT`, consult its configuration reference. No production changes are involved in this example.

## Quality check

A competent reader can follow the steps without guessing a missing command, risk, input, or verification condition. The guide's stated environment must match the actual project.

## Sources

- Diátaxis, how-to guides: https://diataxis.fr/how-to-guides/
- Google documentation procedures: https://developers.google.com/style/procedures
- AWS runbook guidance: https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_runbooks.html
