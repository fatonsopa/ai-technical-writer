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

Read the [complete Websites Review example](../examples/readme.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Can someone new understand the purpose, run the first command, check success, and locate deeper information? Confirm that every claimed command/path/link exists in the actual project. Report checks that were not run.

## Sources

- [GitHub: repository READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [Google: documentation best practices](https://google.github.io/styleguide/docguide/best_practices.html)
