# Discover what the document needs

Use this workflow before creating or substantially changing a document. Scale it to the request: a spelling correction needs its surrounding context; an architecture proposal needs requirements and system evidence. Discovery does not require a questionnaire, a separate document, or approval of routine writing choices.

## Investigate before asking

Read the request, relevant conversation, supplied material, and maintained project documents. For an existing system, inspect the available code, database schema or migrations, configuration, tests, and workflows needed to understand the subject. Use authorized read-only tools when available. Writing does not authorize migrations, application changes, or production access.

Treat an answer already established by reliable sources as known. Do not ask the user to name the framework, describe a schema you can inspect, repeat an agreed workflow, or select an existing decision again. Cite the evidence and continue. If sources are unavailable or contradictory, explain the specific gap and ask only for what affects the result.

Separate current behavior, agreed requirements, constraints, proposals, and unresolved choices. Code establishes what is implemented; it does not automatically establish what a requested change should do. A known defect must not become a requirement by copying the code's behavior.

Research a genuine knowledge gap before recommending a solution. Prefer authoritative documentation appropriate to the project's versions and constraints. Investigate local facts locally; external research cannot decide a product priority, budget, permission policy, or acceptable data loss. Record useful findings and their limits instead of presenting a general best practice as the user's decision.

## Ask in dependency order

Start at the first unresolved material topic, then adapt the next question to the answer. Skip topics the evidence already answers; revisit an earlier one only when a contradiction or change affects it.

| Order | Establish | Typical owner |
| --- | --- | --- |
| 1 | Reader, problem, users, desired outcome, included and excluded scope | Product Requirements Document (PRD) or source issue |
| 2 | Required behavior, roles, errors, business rules, acceptance | Spec Driven Development document (SDD) or a small issue's specification |
| 3 | Constraints, data ownership, quality targets, compatibility, risk | Spec Driven Development document (SDD) and existing architecture |
| 4 | Unresolved architecture, component design, operational and delivery tradeoffs | High Level Document (HLD), Low Level Design (LLD), decision record, plan |
| 5 | Whether a visual would clarify a difficult relationship or scenario | Owning reference with visual guidance |

This is a question dependency order, not a requirement to create all those documents. Do not ask a deployment question while the feature's scope is unknown, unless that constraint determines the scope.

Use the host's structured question tool when available and permitted in the current mode. Present one focused decision, or a small group of independent questions, with meaningful alternatives and consequences. Recommend an option when evidence supports it and explain why. Allow a written answer; use free text when a meaningful choice cannot capture the information. If no usable question tool exists, ask concisely in chat. Do not invent a tool or require a particular host or mode.

Explain the evidence before asking. For example: “The current client records each committed batch. Resuming after an uncertain response would require reconciliation. Should recovery remain explicit, or should we propose automatic recovery?” Ask this only if recovery is genuinely undecided or an improvement is being considered. A confirmed policy needs no new vote.

Wait for answers before dependent work; continue independent research or drafting where useful. A preselected option, silence, tool timeout, or elapsed time is not an answer. Accept explicit delegation to choose, record its scope, and justify the choice. Do not infer delegation from “continue.” Routine wording, headings, and equivalent notation choices remain the writer's responsibility.

## Draft or deliver

Resolve choices that change scope, required behavior, architecture commitments, permissions, cost, data safety, or acceptance before presenting them as settled. Alternatives can remain proposals while those choices are open. For an early draft, use `Status: Draft`, identify open decisions and their consequences, and keep dependent sections provisional.

When the sources already provide everything needed, write without ceremonial questions or another approval. Do not mark a document agreed or approved unless evidence establishes that status.

For complete Product Requirements Document (PRD), Spec Driven Development document (SDD), High Level Document (HLD), Low Level Design (LLD), and implementation-plan delivery, record discovery in the checked-delivery request's `context`. Keep this working record outside the skill, with source IDs matching captured sources:

```json
{
  "discovery": {
    "status": "ready",
    "source_ids": ["brief", "existing-architecture"],
    "decisions": []
  },
  "visuals": []
}
```

An empty decision list is correct when sources settle the material choices. For a question that arose, record `id`, `question`, `status` (`open` or `resolved`), boolean `blocking`, `answer`, and `source_ids`. Open entries have an empty answer and source list. Resolved entries contain the actual answer or delegated choice and its captured evidence. Ready records cannot contain open blocking decisions. Drafts must identify their open decision IDs. Questions, answers, source inspection and authority still need honest semantic review; the script cannot infer their truth.

Use [checked delivery](rewrite.md#validate-the-actual-output) after discovery. Capture a new request version when an answer or requirement changes; preserve earlier evidence. For a needed visual, select its heading, notation and reason using [Visual Guidance (VG)](../references/visuals.md). Do not add diagrams to fill a template.

## Sources

- [NASA: stakeholder expectations](https://www.nasa.gov/reference/4-1-stakeholder-expectations-definition/)
- [NASA: technical requirements definition](https://www.nasa.gov/reference/4-2-technical-requirements-definition/)
- [Anthropic: concise guidance and appropriate degrees of freedom](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)

The sequence and record above are this skill's procedure; they do not impose NASA's document set or requirement wording on software projects.
