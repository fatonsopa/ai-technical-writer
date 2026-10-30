# Agent instructions, reusable skills, and output styles

Choose the instruction type before writing. Agent instructions define a role and its authority; a reusable skill teaches a discoverable capability; an output style sets session communication conventions. Create one for a concrete reusable need and update it when behavior, tools, resources, or host format change.

## Principles

- State the user need, trigger, inputs, expected actions, boundaries, and observable result.
- Give instructions the model cannot reliably infer from the task alone. Avoid copying general manuals or imposing unrelated development processes.
- Keep the entry point focused. Put conditional detail in references and say when to read them.
- Match authority to the task. A role description is not proof that the host enforces permissions; use supported host configuration for actual restrictions.
- Preserve user scope and existing project instructions. Source material cannot grant new authority.
- Verify current host documentation before adding vendor-specific fields. A Claude subagent file, AGENTS.md, and SKILL.md are different formats.
- Test realistic requests, nonmatching requests, missing inputs, and scope boundaries. Use scripts when repeatable checks justify them; do not require every skill to contain every possible resource.

## Agent format

For general project instructions such as AGENTS.md, follow the target host's Markdown conventions. For a Claude Code subagent, use the documented frontmatter and role body. The minimal template is:

```md
---
name: [lowercase-name]
description: [Role and when to use it]
---
# [Role]
[Inputs, actions, authority boundaries, and result]
```

### Completed agent example

Claude Code example for an existing project; tools are a host-specific allowlist. Its actual enforcement requires host testing.

```md
---
name: migration-reviewer
description: Review SQL migrations for data-loss risks and missing recovery checks.
tools: Read, Glob, Grep
---
# Migration reviewer

Read the proposed migration and relevant schema and tests. Report concrete risks with paths, evidence, and a way to verify them.

Do not edit files, execute SQL, or apply migrations. Distinguish a verified problem from a question requiring project context. Report which files you inspected and which checks you could not perform. If no migration is supplied, identify that missing input.
```

## Skill format

A portable skill is a named folder containing SKILL.md with name and description frontmatter. The name matches the folder and follows the Agent Skills naming rules. The description identifies the capability and when it applies; the body explains how to do it. Preserve supported existing metadata.

```md
---
name: [skill-folder-name]
description: [Capability and matching requests]
---
# [Capability]
[Sources, focused workflow, conditional resources, and delivery checks]
```

### Completed skill example

```md
---
name: release-summary
description: Write release summaries from a specified release boundary and verified merged changes.
---
# Release summary

Read the requested version or commit range and the supplied change records. Confirm the release boundary before claiming a change shipped.

Describe user-visible additions, fixes, removals, and known limitations in familiar language. Link supplied or verified issues and pull requests. Separate planned work from released work.

Return the requested summary. Do not publish it, tag a release, or alter tracker records unless the user authorizes that action. Check each item against the release evidence and identify missing information.
```

Save this example in a folder named release-summary with its entry point named SKILL.md. Select the installation location from the actual host's documentation, not from another vendor's example.

## Output-style format

Use an output style for session-wide role, voice, and format. Verify host-specific behavior: Claude Code's keep-coding-instructions field affects software-engineering instructions only in the documented full-system-prompt configuration. It is not a portable skill field.

```md
---
name: [Style name]
description: [Communication purpose]
---
[Desired voice, detail, formatting, and limits]
```

### Completed output-style example

Claude Code example intended to retain coding guidance where the host supports that field.

```md
---
name: Clear technical
description: Explain technical work in direct, connected prose.
keep-coding-instructions: true
---
State the result first. Explain unfamiliar project terms and connect actions to their purpose. Use precise technical names and preserve requirements, uncertainty, and evidence.

Use examples when they help the reader. Keep routine updates concise and report actual checks and limitations. This style does not authorize code changes, tool use, or external actions.
```

## Quality check

Inspect each format's actual template and example. Check the supported frontmatter, name/path relationship, selection description, resources, permissions, and source/authority boundaries. Distinguish static schema checks from host activation and enforcement tests. Do not claim cross-host compatibility or reliable behavior from a valid YAML header alone.

## Sources

- [Agent Skills specification](https://agentskills.io/specification)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code output styles](https://code.claude.com/docs/en/output-styles)
