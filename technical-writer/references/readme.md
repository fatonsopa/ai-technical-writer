# Repository readme (README)

A README is the entry point for a repository or component. Create it when that entry point is needed; update it when purpose, setup, commands, supported environments, or documentation links change.

## Principles

- Say what the project does, who uses it, and where to start.
- Verify prerequisites and commands against the repository's actual scripts and configuration.
- Explain necessary local configuration without exposing credentials. Distinguish required setup from optional capabilities.
- Include a working start and a way to check success. A list of commands that might exist is not a complete example.
- Link maintained requirements, architecture, usage, and contribution information when they exist. Do not invent files or license claims.
- Keep the entry point concise. Move a long learning path to a [tutorial](tutorial.md), operations to a [how-to](how_to_guide.md), and design to the relevant HLD/LLD.

## Structure and template

Use identity/purpose, prerequisites, getting started, verification/tests, useful structure, and further documentation. Adapt to a library, application, skill, or component rather than forcing server instructions on every repository.

```md
# [Project]
[Purpose and intended users]
## Start
[Verified prerequisites, setup, first command, expected result]
## Check the result
[Tests or success check]
## Find your way around
[Important real files/folders and maintained links]
## Limits and help
[Relevant constraints and known support resources]
```

## Completed example

Fictional repository contract: Python 3, no external packages; report.py reads sample.json and prints its project field; tests/test_report.py checks that behavior. These names and commands are assumptions of this example.

```md
# Project name reader

This small Python command reads a project's name from JSON and prints it. It demonstrates a local report without a server or database.

## Start
Install Python 3 and open a terminal in the repository folder. The supplied sample.json contains {"project": "Example App"}. Run:

    python3 report.py sample.json

The command prints Example App.

## Check the result
Run the supplied tests:

    python3 -m unittest discover -s tests

## Find your way around
report.py contains the command. sample.json is the starting input. tests/test_report.py checks the expected output.

## Limits and help
The input must contain the project field. This example makes no license or support-channel claim. Its maintained behavior source is the command contract described above.
```

## Quality check

Can someone new understand the purpose, run the first command, check success, and locate deeper information? Confirm that every claimed command/path/link exists in the actual project. Report checks that were not run.

## Sources

- [GitHub: repository READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [Google: documentation best practices](https://google.github.io/styleguide/docguide/best_practices.html)
