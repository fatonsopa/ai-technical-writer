# Explanation: how a system works and why

An explanation helps someone understand concepts, choices, causes, and tradeoffs. It connects related facts into a useful mental model. Follow Diátaxis: start with the reader's question, give the relevant context, explain the relationships, and acknowledge what is uncertain.

## Principles

1. **Answer one central question.** The title should identify the concept or question clearly.
2. **Start with a plain description.** Explain what the subject is and why a reader would care before discussing internals.
3. **Connect causes and effects.** Explain why a choice exists, how components interact, and what changes when an assumption changes.
4. **Distinguish evidence from interpretation.** A historical decision needs a source. A possible explanation must be marked as a hypothesis.
5. **Use a small example when useful.** A concrete scenario often explains the concept better than additional definitions.
6. **Discuss tradeoffs fairly.** Explain what a choice gains, what it costs, and where its limits are.
7. **Avoid a hidden tutorial or reference manual.** Link to exact procedures and field definitions when the reader needs them.
8. **Give the reader enough context to follow the argument.** Define project-specific terms once and use them consistently.

## Template

```md
# Why / How [subject]

[Direct answer in one paragraph.]

## Background
[What readers need to know about the system.]

## How it works
[Main parts and relationships, with an example or diagram if useful.]

## Why this approach
[Reasoning and tradeoffs supported by known decisions.]

## Limits and open questions
[Where this explanation stops; uncertainties.]

## Related documentation
[How-to guides, reference, decisions, sources.]
```

## Completed example: why a queue sits between an API and an email service

This is a general architecture example.

### Why background jobs use a queue

Sending email can be slow or fail temporarily because the mail service is outside the application. A queue allows the API to accept a request and hand the email job to a worker, which sends the message separately.

**Background.** Without a queue, the request may remain open until the mail service replies. Slow delivery can cause timeouts even when the application itself works normally.

**How it works.** When a user requests a password reset, the API creates a job containing the information needed to send the message. A worker reads the job, contacts the mail service, and records success or failure. If delivery fails temporarily, the worker can retry according to a defined policy.

**Why this approach.** Moving delivery to a worker can reduce how long the user waits for the API. It also introduces new responsibilities: monitoring the queue, handling duplicate jobs, deciding how many times to retry, and making sure jobs do not disappear silently.

**Limits.** The queue does not guarantee that the recipient reads the email or that the mail provider accepts every request. The team's chosen delivery and retry contract determines what a successful operation means.

## Quality check

A new colleague can describe the concept in plain language and explain the significant reasons, consequences, and limits. The explanation neither invents architectural decisions nor buries the reader in field-by-field reference material.

## Source

- Diátaxis, explanation: https://diataxis.fr/explanation/
