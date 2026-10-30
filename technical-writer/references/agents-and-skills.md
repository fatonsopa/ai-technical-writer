# Claude Code agents, reusable skills, and output styles

These are three different kinds of instructions. An **agent** defines a specialized assistant and its tools. A **skill** describes work the assistant can perform when a task matches its description. An **output style** changes the main session's communication style. Choose the right file before writing. Verify the target Claude Code version and documentation before using fields beyond the common minimum.

## Shared principles

1. Give each file a narrow, understandable purpose and a description that says when to use it. Activation depends heavily on the description.
2. Write instructions in the order the agent will perform them. Define concrete inputs, actions, boundaries, and checks.
3. Keep the main file short. Move large examples and specialized rules into references that the main file tells the agent when to read.
4. Use the least tools and authority the task needs. Specify safety constraints when actions can affect code, production data, or external services.
5. Avoid explaining basic model behavior. Focus on the conventions and decisions the agent cannot infer safely.
6. Test the file with real requests, including cases where it should not activate.
7. Treat platform-specific frontmatter fields as version-dependent. Check the current vendor docs before adding them; do not guess supported model names or options.

## Agent definition

Use an agent when a task benefits from separate context, a focused role, or particular tools. In Claude Code, project agent definitions commonly live in `.claude/agents/`. The body is its working instruction. Specify allowed or denied tools only when the feature is supported by the installed version.

### Agent template

```md
---
name: code-reviewer
description: Reviews changed code for correctness, risks, and missing tests.
---

# Code reviewer

Inspect the changed code and relevant nearby behavior.
Report concrete findings with file paths and evidence.
Do not modify code unless the user asks for fixes.

## Review
1. Read the change and its context.
2. Check likely failure cases and existing tests.
3. Report issues in order of impact.

## Result
For each finding: affected file, observed risk, evidence, and a way to verify it.
State when no verified issue was found and which checks were not run.
```

## Skill

A skill is a folder with `SKILL.md` containing YAML frontmatter and Markdown instructions. Its name and description should be short and specific. Keep supporting references one level deep from `SKILL.md` when possible, and tell the assistant exactly when to read them. Scripts can perform repeatable checks without copying their code into the main context.

### Skill template and completed example

```md
---
name: changelog-writer
description: Creates human-readable release notes from verified changes and issue records.
---

# Changelog writer

Document user-visible changes for a specified release. Verify the
release version, merged changes, and issue links before writing.

## Steps
1. Find the release boundary and confirmed changes.
2. Group changes by added, changed, fixed, removed, or security impact.
3. Explain each change in words users understand.
4. Link verified issues or pull requests; omit unverified claims.

## Validation
Confirm that every item shipped in the release and describes a real change.
```

Save it as `.claude/skills/changelog-writer/SKILL.md` in a compatible Claude Code project. If the skill grows, add a reference for release note format and tell the main file when to load it. This is an instructional example; current activation behavior should be checked in the target environment.

## Output style

Use an output style when the goal is to set communication conventions for the main conversation. Keep instructions about tone, detail, and formatting there. Do not use an output style to define development processes that agents must follow independently.

### Output style example

```md
---
name: clear-technical
description: Writes technical explanations in direct, familiar language.
---

# Clear technical

Use everyday words, explain unfamiliar project terms, and give complete
answers with examples when they help. Keep facts and assumptions separate.
```

## Quality check

Check frontmatter syntax and required fields, file path, tool permissions, platform compatibility, selection description, reference links, and actual activation with a small test set. A human should understand the purpose and limits of the file without reading the conversation that led to it.

## Sources

- Agent Skills specification: https://github.com/agentskills/agentskills/blob/main/docs/specification.mdx
- Claude Code documentation: https://code.claude.com/docs/en/skills
- Claude Code subagents: https://code.claude.com/docs/en/sub-agents
- Claude Code output styles: https://code.claude.com/docs/en/output-styles
