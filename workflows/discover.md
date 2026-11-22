# Discover what the document needs

Use this workflow before creating or substantially changing a document. Scale it to the request: a spelling correction needs its surrounding context; an architecture proposal needs requirements and system evidence. Discovery does not require a questionnaire, a separate document, or approval of routine writing choices.

## Investigate before asking

Before claiming inspection, identify the required source sections and confirm their complete content is available in this context. A successful file read can still be truncated in transport. Recover an omitted middle or tail using bounded section reads from the same revision, checking its path and byte hash before and after recovery. Restart inspection or disclose incomplete evidence when the source changes; never combine revisions into one claimed complete read. Reuse a small complete input without rereading it. Load conditional sources only when relevant.

Read the request, relevant conversation, supplied material, and maintained project documents. For an existing system, inspect the available code, database schema or migrations, configuration, tests, and workflows needed to understand the subject. Use authorized read-only tools when available. Writing does not authorize migrations, application changes, or production access.

Treat an answer already established by reliable sources as known. Do not ask the user to name the framework, describe a schema you can inspect, repeat an agreed workflow, or select an existing decision again. Cite the evidence and continue. If sources are unavailable or contradictory, explain the specific gap and ask only for what affects the result.

Separate current behavior, agreed requirements, constraints, proposals, and unresolved choices. Code establishes what is implemented; it does not automatically establish what a requested change should do. A known defect must not become a requirement by copying the code's behavior.

Research a genuine knowledge gap before recommending a solution. Prefer authoritative documentation appropriate to the project's versions and constraints. Investigate local facts locally; external research cannot decide a product priority, budget, permission policy, or acceptable data loss. Record useful findings and their limits instead of presenting a general best practice as the user's decision.

## Ask in dependency order

Start at the first unresolved material topic, then adapt the next question to the answer. Skip topics the evidence already answers; revisit an earlier one only when a contradiction or change affects it.

| Order | Establish | Typical owner |
| --- | --- | --- |
| 1 | Reader, problem, users, desired outcome, included and excluded scope | Product Requirements Document (PRD) or source task |
| 2 | Required behavior, roles, errors, business rules, acceptance | Spec Driven Development document (SDD) or a small task's specification |
| 3 | Constraints, data ownership, quality targets, compatibility, risk | Spec Driven Development document (SDD) and existing architecture |
| 4 | Unresolved architecture, component design, operational and delivery tradeoffs | High Level Document (HLD), Low Level Design (LLD), decision record, plan |
| 5 | Whether a visual would clarify a difficult relationship or scenario | Owning reference with visual guidance |

For a child story or task, resolve its ancestry before any of these topics. Find the epic or feature outcome it belongs to, the story, the exact criterion and each source's revision. If one of them is missing, stale or contradicts the child, report that broken edge instead of drafting around it. Work that depends on the edge waits; independent research can continue. A request that is explicitly standalone, such as fixing one broken link, can proceed with its own source and expected destination. An unresolved parent never turns the child into standalone work.

This is a question dependency order, not a requirement to create all those documents. Do not ask a deployment question while the feature's scope is unknown, unless that constraint determines the scope.

Use the host's structured question tool when available and permitted in the current mode. Present one focused decision, or a small group of independent questions, with meaningful alternatives and consequences. Recommend an option when evidence supports it and explain why. Allow a written answer; use free text when a meaningful choice cannot capture the information. If no usable question tool exists, ask concisely in chat. Do not invent a tool or require a particular host or mode.

For example, "make reviews faster" for Websites Review could mean two different delays: the automated checking before a website is parked and enters Review, or the time administrators spend assigning categories once it's there. Ask one question that tells them apart. If the owner answers "the second one", write the criterion about that delay, for instance "an administrator can assign a category to several Review rows at once", and leave the target open if the owner gave none. If the request already says "administrators should assign categories to several Review rows at once; no target yet", write the criterion directly without asking again.

Explain the evidence before asking. For example: “The current client records each committed batch. Resuming after an uncertain response would require reconciliation. Should recovery remain explicit, or should we propose automatic recovery?” Ask this only if recovery is genuinely undecided or an improvement is being considered. A confirmed policy needs no new vote.

When the answers need to outlive the session, or someone asks for them, write a [Discovery Interview Record (DIR)](../references/discovery_interview.md). It keeps each question, answer and source, the restatement and whether the owner confirmed it.

Wait for answers before dependent work; continue independent research or drafting where useful. A preselected option, silence, tool timeout, or elapsed time is not an answer. Accept explicit delegation to choose, record its scope, and justify the choice. Do not infer delegation from “continue.” Routine wording, headings, and equivalent notation choices remain the writer's responsibility.

## Record material topics

Some formats name topics that a complete document must settle, whatever the writer's own list says. For a Product Requirements Document (PRD), that topic is permissions: who may perform each new or changed action, and who owns the data it exposes. Record each such topic in the discovery decisions with `topic` set and one of these statuses:

- `resolved`, with the answer and the source that supports it;
- `provisional`, with a proposed answer that still lacks authority;
- `open`, with no answer yet;
- `inapplicable`, with the reason it doesn't apply.

An open or provisional topic keeps the document a draft, and the draft names it. The checker reports a missing topic with the section it affects. Whether a cited source actually supports an answer is for the reviewer to judge; a real source ID about something else doesn't settle the topic.

## Choose the smallest record

Pick the record from what the request actually covers, and don't invent a parent.

| Situation | Record |
| --- | --- |
| An independently authorized, bounded change, such as replacing one misleading label with an exact new one | One [Task](../references/task.md) with its scope and proof |
| An independent user outcome, such as letting an administrator recover an unsaved selection | A [User Story (US)](../references/user_story.md), or the project's equivalent record, with the actor, benefit, boundary and observable result |
| A change assigned to a criterion of an existing story | A child Task; resolve the parent story and criterion first, and hold the child if the parent is missing |
| Several usable slices of one capability | A feature that groups them |
| Several slices or capabilities that share an initiative, an owner and an integrated outcome | An epic, or whatever label the project uses for that level |
| Delivery that needs an agreed order, handoff, compatibility proof or recovery, such as a rollout where old and new readers must coexist | An [Implementation Plan (IP)](../references/implementation_plan.md) naming the order, compatibility proof, who switches over and how to recover |

A single contained delivery keeps its steps inline in the Task or design. A plan the project requires takes precedence over this table.

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
