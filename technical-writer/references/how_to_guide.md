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

Self-contained local-file example for macOS/Linux with Python 3. It changes a JSON setting; it makes no claim about an application's live port.

````md
# Change a port value in a local JSON file

## Before you begin
Work in a disposable local folder. Create settings.json containing:

```json
{"port": 3000, "debug": false}
```

Confirm settings.json.bak does not already contain a backup you need.

## Steps
1. Back up the file:

```sh
cp settings.json settings.json.bak
```

2. Change only the port:

```sh
python3 -c 'import json; from pathlib import Path; p=Path("settings.json"); d=json.loads(p.read_text()); d["port"]=3100; p.write_text(json.dumps(d)+chr(10))'
```

3. Check the saved value:

```sh
python3 -c 'import json; d=json.load(open("settings.json")); assert d["port"] == 3100; assert d["debug"] is False; print("Port updated")'
```

## Confirm success
The check prints Port updated. The file retains debug: false and contains port: 3100.

## If it fails
Stop and read the reported error. To restore this exercise's original file, run:

```sh
cp settings.json.bak settings.json
```

Verify the restored JSON before trying again.
````

## Quality check

Can a competent reader perform the procedure without guessing a command or missing check? Verify the setup, command effects, relevant failure branches, and recovery. A stated expected result must not be reported as a result you observed unless you ran the check.

## Sources

- [Diátaxis: how-to guides](https://diataxis.fr/how-to-guides/)
- [Google: procedures](https://developers.google.com/style/procedures)
