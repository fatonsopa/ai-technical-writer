# Repository readme (README)

A Repository readme (README) is the entry point for a repository or component. Create it when that entry point is needed; update it when purpose, setup, commands, supported environments, or documentation links change.

## Principles

- Say what the project does, who uses it, and where to start.
- Verify prerequisites and commands against the repository's actual scripts and configuration.
- Explain necessary local configuration without exposing credentials. Distinguish required setup from optional capabilities.
- Include a working start and a way to check success. A list of commands that might exist is not a complete example.
- Link maintained requirements, architecture, usage, and contribution information when they exist. Do not invent files or license claims.
- Keep the entry point concise. Move a long learning path to a [Tutorial (TUT)](tutorial.md), operations to a [How-to Guide (HTG)](how_to_guide.md), and design to the relevant High Level Document (HLD)/Low Level Design (LLD).

## Decide what belongs in the README

Write for someone opening the repository for the first time. In the first paragraph name what the tool does, who would use it and one concrete reason to choose it. For a tool built on another project, say what the dependency handles and what the reader gains by using this one. Keep the definition short enough to stand on its own. Put the first worked example in Quick start.

Put prerequisites and installation before the first instruction that depends on them. If setup is unnecessary, start with the task. Give one realistic request or command, say where to enter it, and show the result the reader can recognize. Mark hypothetical results as examples. Use everyday verbs, name the actual output and cut claims that could describe almost any tool.

Keep a short answer in the README when it helps someone choose, start, check the result or get help. Put longer walkthroughs, command references, alternative setup methods, troubleshooting and contributor or evaluation procedures in `docs/` by default. Link directly to the page or section that answers the question. An existing maintained documentation site or project convention can serve the same purpose. A small skill with nothing more to explain needs no extra file or empty directory.

Keep requirements, acceptance criteria and live task status in their owning specification or tracker. A short example can explain what a spec looks like. Link the original for the complete rules. When an index or diagram must stay in the README, keep the common path visible and fold long catalogs or optional paths under a descriptive label. Never move required material merely to shorten the page.

## When the project is a reusable skill

Show the input someone supplies, the skill invocation in its actual host, and what they can inspect afterward. Include only the prerequisites for that path. Link other supported install methods, evaluation instructions, fixture preparation, coverage definitions and recovery steps where people use them. Separate a successful installation check from evidence of writing or task quality. Link the maintainer and known license when applicable.

Write a released README from observed behavior. If the owner requests copy for a future release, use the approved release design and voice. Record unverified commands and capabilities in the handoff and verify them before publishing the release. Writing documentation grants no installation or release authority.

## Structure and template

Adapt the headings to the reader. Combine a short setup and example when they naturally fit. Keep the order of actions a new user has to take.

```md
# [Project]
[What it does, who it helps, and one concrete use]

## Installation
[Prerequisites, primary setup, and where to run it]

## Quick start
[One real input and invocation]

## Check the result
[What the user should see]

## Documentation
[Direct links to the relevant guides in docs/ or the maintained documentation site]

## Support
[Where to get help or report a problem]
```

## Completed example

Read the [Repository readme (README) example for Websites Review](../examples/readme.md). It demonstrates this format's structure and depth within the shared initiative. Scale the result to the actual request; do not copy its project facts into another document.

## Quality check

Read it once in order as a newcomer. Can you tell why to use the project, follow setup before first use, recognize the result, and reach the next answer from the link text? Look for repeated procedures, marketing claims, internal task IDs and specifications copied into public instructions. Confirm that every claimed command/path/link exists in the actual project. Report checks that were not run.

## Sources

- [GitHub: repository READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [Google’s README guidance](https://google.github.io/styleguide/docguide/READMEs.html) and [voice and tone](https://developers.google.com/style/tone)
- [Diátaxis on choosing a document by reader need](https://diataxis.fr/start-here/)
- [OpenSpec’s worked example and links to detailed guides](https://github.com/Fission-AI/OpenSpec/blob/v2.1.1/README.md)
