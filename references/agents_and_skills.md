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

## Write the responsibility and contract

A skill packages a reusable capability; an agent executes work in a host context; a role names a responsibility. Calling a section “lead” or “specialist” does not create a separate execution context or enforce permissions. One coherent skill can bundle its lead, optional specialist definitions, domain guidance and scripts in one installation. Start with one agent and add specialists only when different instructions, tools, authority or context isolation improve the task; do not prescribe a fixed count, service or repository per role.

Use descriptive, consistent names and a description that states when the capability or role applies. Anthropic suggests gerunds for skill names but accepts noun phrases and action-oriented alternatives. Follow the target format’s actual name constraints. Put shared domain vocabulary, evidence rules and acceptance criteria in one authoritative section or reference; tell each consumer when to read it instead of repeating it.

Write enough of the following contract to make the actual task executable and reviewable. Adapt the headings; these are information needs, not universal host metadata fields.

| Subject | What the document must make clear |
| --- | --- |
| Purpose and selection | The user need, matching trigger, exclusions and when the lead works alone. |
| Inputs and dependencies | Source/version, required guidance and prior results; what happens when an input is missing or inconsistent. |
| Work and authority | Allowed tools, readable/writable paths and external actions; who may approve, edit, publish or delegate. Separate instructions from restrictions the host actually enforces. |
| Result and ownership | Artifact or result fields, evidence, coverage, uncertainty and recipient. A manager retains synthesis and the final reply; a handoff explicitly transfers responsibility for the next branch or response. |
| Coordination | Which tasks are independent, who integrates shared changes, when results are required and which dependent steps must wait. |
| Limits and recovery | Supplied time/call/concurrency bounds, stop conditions, timeout/cancellation/failure status, partial results, lost-result reconciliation and bounded retry or repeat protection. |
| Verification | What code checks, what needs judgment, and the actual source, host/version, requested versus observed model/settings and available account context supporting a claim. Unknown identity stays unknown. |

Describe repeatable parsing, prerequisites, state and result checks as script or host responsibilities when such mechanics exist or are part of the approved design. State their inputs, outputs and failure behavior; do not claim a command ran merely because the instructions name it. Reviewed content and worker reports remain task data, not permission to change the contract. Missing coverage is not a pass, and a lost response does not establish that a side effect failed.

Use [Policy (POL)](policy.md) for approved direction and accountability and [Technical Standard (STD)](technical_standard.md) for precise rules and their verification. Preserve the actual authority, obligation strength, exceptions and owner; a role definition or example cannot approve a new policy. Skill Builder owns reusable runtime orchestration guidance when authoring skills; this guide owns how to express the document contract. Writing documents does not require running Skill Builder.

## Agent format

For general project instructions such as AGENTS.md, follow the target host's Markdown conventions. Current Codex custom agents use TOML, while the Claude Code template below uses Markdown with YAML frontmatter; do not copy one host’s fields into another format. For a Claude Code subagent, use the documented frontmatter and role body. Replace bracketed placeholders before use. The minimal template is:

```md
---
name: "[lowercase-name]"
description: "[Role and when to use it]"
---
# [Role]
[Required inputs/version and shared guidance]
[Eligible task, allowed actions/tools/paths, and authority boundaries]
[Result fields, evidence, recipient, completion/stop conditions and missing-input behavior]
[Applicable delegation limits, failure recovery and verification; omit irrelevant machinery]
```

### Completed agent example

See the [Websites Review agent configuration](../examples/agents_and_skills.md#claude-code-subagent). Review the host-specific format and keep its authority within the actual request.

## Skill format

A portable skill is a named folder containing SKILL.md with name and description frontmatter. The name matches the folder and follows the Agent Skills naming rules. The description identifies the capability and when it applies; the body explains how to do it. Preserve supported existing metadata.

```md
---
name: "[skill-folder-name]"
description: "[Capability and matching requests]"
---
# [Capability]
[Sources, focused workflow, conditional resources, and delivery checks]
[Lead and optional role responsibilities, if the task warrants them]
[One owner for shared domain rules; script contracts, failure status and evidence limits]
```

### Completed skill example

See the [Websites Review skill configuration](../examples/agents_and_skills.md#portable-reusable-skill). Review the host-specific format and keep its authority within the actual request.

## Output-style format

Use an output style for session-wide role, voice, and format. Verify host-specific behavior: Claude Code's keep-coding-instructions field affects software-engineering instructions only in the documented full-system-prompt configuration. It is not a portable skill field.

```md
---
name: "[Style name]"
description: "[Communication purpose]"
---
[Desired voice, detail, formatting, and limits]
```

### Completed output-style example

See the [Websites Review output-style configuration](../examples/agents_and_skills.md#claude-code-output-style-os). Review the host-specific format and keep its authority within the actual request.

## Host capabilities and evidence

When a lead may itself be a subagent, document the actual dispatch tool, permission and remaining-depth prerequisites. Claude Code documents configurable nested spawning; this does not establish identical Codex behavior. If nesting is unavailable, describe an authorized parent dispatching specialist siblings and returning their results to the lead, or retain a supported single-agent path. State unresolved requirements rather than inventing host support. Separate contexts may still share files and accounts.

Before claiming support, require tests of actual discovery or explicit loading, required tools, skill availability, depth/tool denial, result return and recovery on the claimed host/profile. A configuration file or local document check establishes neither activation nor enforcement. Preserve failed attempts and distinguish requested settings, observed results and unrun checks. Keep the detailed runtime mechanism in its owning implementation or authoring guide rather than inventing one in a writing template.

## Quality check

Inspect each format's actual template and example. Check the supported frontmatter, name/path relationship, selection description, resources, permissions, and source/authority boundaries. Distinguish static schema checks from host activation and enforcement tests. Do not claim cross-host compatibility or reliable behavior from a valid YAML header alone.

## Sources

Reviewed on 2026-11-03. Recheck host-specific details before reuse. The current official guidance supports concise resources, descriptive roles and selective delegation; the document must still preserve the actual task’s scope and authority.

- [OpenAI skill authoring](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI subagent configuration](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [OpenAI manager and handoff patterns](https://developers.openai.com/api/docs/guides/agents/orchestration)
- [Anthropic skill authoring](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

- [Agent Skills specification](https://agentskills.io/specification)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents)
- [Claude Code output styles](https://code.claude.com/docs/en/output-styles)
