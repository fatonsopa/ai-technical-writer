# Threat Model (TM)

A Threat Model (TM) explains what can harm a particular system and how its design addresses those threats. Create or update it when sensitive assets, trust boundaries, actors, dependencies or deployment change. It supports security and architecture review; it is not proof that controls are implemented or effective. Use an existing project format when it carries this information.

## Principles

Start from versioned requirements and the system actually in scope. Identify valuable assets, sensitive data, actors and capabilities, entry points, components, dependencies and trust boundaries. Include privileged operators and automated actors as well as external attackers. Explain data movement and authority changes; a boundary is a change in trust or control, not merely a box around a process. A table can describe a small flow; use a diagram only when it improves understanding, following [Visual Guidance (VG)](visuals.md).

For each relevant flow, reason about concrete abuse: who can do what to which asset, through which entry point, under what preconditions, with what consequence? STRIDE or another suitable method can prompt questions; a list of category names is not analysis. Consider identity/session misuse, cross-tenant access, parsing, injection, file or URL handling, exposed secrets, tampering, availability and dependency compromise where applicable. Explain exclusions rather than treating web controls as universal requirements.

Assign stable threat IDs and relate each to an asset, flow/boundary and requirement. Distinguish observed weaknesses, plausible design risks and missing evidence. Explain impact and likelihood assumptions; preserve the project's risk method instead of inventing numerical precision. A missing mitigation is not automatically an exploited vulnerability.

For each threat, record the proposed or verified control, responsible component/owner when known, remaining exposure and a verification method. Acceptance of residual risk requires an actual decision source and authority; an author cannot grant it. Link relevant [Decision Record (DR)](decision_record.md) entries and [Interface Contract (IC)](interface_contract.md) sections. Tests, design statements and executed results retain different evidentiary roles.

## Structure and template

Use [discovery](../workflows/discover.md) for material unknowns. Keep unresolved assumptions visible in a draft and identify source versions and review triggers. Adapt detail to risk; do not require this as a separate file for every change.

```md
# [System] threat model
Status/sources: [Draft or agreed, revision, scope and authority]
## Scope and sources
[Assets, intended use, exclusions, source versions and assumptions]
## System and trust boundaries
[Actors/capabilities, components, entry points, flows and changes in trust]
## Threat scenarios
[Threat ID, asset/flow, actor, preconditions, abuse, impact and risk rationale]
## Mitigations and residual risk
[Threat-to-control mapping, proposed/verified status, owner, residual exposure, decision authority]
## Verification and open decisions
[Threat-linked checks and evidence, unresolved choices, review triggers]
```

## Completed example

Read the [Threat Model (TM) example](../examples/threat_model.md). Its scenario and decisions are illustrative, not evidence about a live system.

## Quality check

Can a reviewer follow each threat from actor and boundary to consequence, control and verification? Challenge missing flows and attacker capabilities. Keep applicability, uncertainty and residual risk explicit. A threat inventory or passing template does not establish secure implementation.

## Sources

Reviewed 2026-11-04: [OWASP threat modeling](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html). Its system/threat/mitigation/validation process informs this guide; the headings are this skill's adaptable convention.
