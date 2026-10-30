# Tutorial (TUT)

A tutorial helps someone learn by completing a controlled exercise. Create it when a learning path is needed; update it when the tools, starting conditions, or exercise change. Use [How-to Guide](how_to_guide.md) for a reader trying to complete an existing task and [Explanation](explanation.md) for deeper understanding.

## Principles

- Choose one learning goal and a small result the learner can reach.
- State the required environment and starting files. Avoid unsupported time estimates.
- Present actions in executable order, with visible expected results.
- Explain a concept after the reader uses it; keep unrelated alternatives out of the lesson.
- Include a completion check and a useful next step.
- Test from a clean start, or identify what remains unverified.

## Structure and template

Include the learning goal, prerequisites, complete exercise, observed/expected results, completion check, and what the learner has learned.

```md
# Learn [skill] by creating [result]
[Learning goal and outcome]
## Before you begin
[Tools, access, starting files]
## Steps
1. [Action; expected result; short explanation]
## Check your result
[Observable completion check and relevant troubleshooting]
## What you learned
[Concrete takeaways and useful next step]
```

## Completed example

Self-contained Python 3 exercise with a terminal and an empty local folder.

````md
# Read a JSON setting with Python

Create a settings file and read its site name. You will learn how a JSON object stores named values.

## Before you begin
Use a terminal in an empty folder with Python 3 installed.

## Steps
1. Create settings.json containing:

```json
{"site_name": "Example App", "debug": false}
```

2. Run:

```sh
python3 -c 'import json; print(json.load(open("settings.json"))["site_name"])'
```

The terminal prints:

```text
Example App
```

Python's json module reads the object. The site_name key selects the value to print.

## Check your result
Confirm that the output is Example App. If the file cannot be found, check the terminal's folder and the filename.

## What you learned
You created a JSON object and read a named value. Next, add a port field and use the same approach to print it.
````

## Quality check

Can a learner start from the stated prerequisites, perform every step, observe success, and explain the concept learned? Check the commands in an isolated folder and keep validation results separate from expected output.

## Source

- [Diátaxis: tutorials](https://diataxis.fr/tutorials/)
