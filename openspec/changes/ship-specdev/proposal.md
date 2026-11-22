# SpecDev change proposal

## Why

Teams need to hand an agent a clear, source-backed change and keep that change usable as requirements evolve. The existing writer can produce documents, but the handoff relies on local conventions where OpenSpec already provides the workflow.

## What Changes

- Keep one writing entry and a catalog command for every supported document. Preserve the legacy `technical-writer` entry when shipping `specdev`.
- Delegate overlapping change operations to the project's installed OpenSpec capabilities. Discover upstream commands dynamically, preserve the caller's permissions, and keep one editable artifact per decision.
- Improve source-backed authoring, session communication and evidence handoff. Update the public feature index and comparison with OpenSpec.
- Distribute SpecDev as a verified GitHub release and an npm package, with one documented path for connecting Codex and Claude Code.

## Capabilities

### New Capabilities

- `spec-driven-authoring` records the proposed source-grounded authoring and native change workflow exposed by SpecDev. This is the first native specification for this capability in this repository.

### Modified Capabilities

There is no previous OpenSpec capability baseline in this repository.

## Impact

Affected consumers include existing writer users, the Skill Builder dependency resolver and both supported coding hosts. The accepted Skill Builder result precedes SpecDev implementation. This proposal authorizes the bounded handoff already agreed with the owner. Execution, external publication and archive keep their existing authority boundaries. [Audit](../../../plan/audit.md) · [Design and delivery plan](design.md) · [Ordered work](tasks.md)
