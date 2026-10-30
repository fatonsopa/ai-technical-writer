# Tutorial: learn by completing a small exercise

A tutorial is for someone learning a skill for the first time. It takes the learner through a controlled, successful exercise and explains what they have just learned. Follow Diátaxis: keep the lesson focused, make each step safe, and avoid turning the exercise into a reference manual.

## Principles

1. Pick one learning goal and a realistic small example. The reader should be able to finish within the stated environment.
2. Give a working starting point, prerequisites, and expected time when it is known. Avoid untested setup assumptions.
3. Present actions in the order they are performed. Show exact commands, file names, and expected results.
4. Explain one concept after the learner sees it in action. Keep deeper theory linked to an explanation page.
5. Build toward a visible success, then summarize what the learner now knows and where to go next.
6. Test the exercise from a clean starting environment, or mark it unverified.

## Structure and template

```md
# Create your first [small result]

[One paragraph: what you will build and learn.]

## Before you begin
- [Required tool and verified version]
- [Account, access, or sample files]

## 1. [First action]
[Exact action and command.]
[What the learner should see and why it matters.]

## 2. [Next action]
[Action, expected output, short explanation.]

## Check your result
[How to confirm the completed exercise works.]

## What you learned
[Two or three concrete takeaways and an appropriate next link.]
```

## Completed example: read a JSON file with Python

This example assumes Python 3 is installed. Commands are illustrative and should be tested in the user's environment before publication.

### Read your first JSON settings file

You will create a small settings file and read one value with Python. JSON stores structured information using named fields.

**Before you begin.** Open a terminal in an empty folder with Python 3 available.

**1. Create `settings.json`.** Save the following text:

```json
{"site_name": "Example App", "debug": false}
```

**2. Read the file.** Run:

```bash
python3 -c 'import json; print(json.load(open("settings.json"))["site_name"])'
```

**Check your result.** The terminal should print `Example App`. If it reports that the file cannot be found, check that the terminal is open in the folder containing `settings.json`.

**What you learned.** A JSON object stores named fields, and Python's `json` module can read those fields. Next, try adding a `port` field and printing its value.

## Quality check

A new learner should know where to start, what to do next, what success looks like, and what was learned. Every command and expected result must be checked or marked unverified.

## Source

- Diátaxis, tutorials: https://diataxis.fr/tutorials/
