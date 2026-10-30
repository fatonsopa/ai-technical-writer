# Explanation (EXP)

An explanation helps a reader understand a concept, causal relationship, or design choice. Create it when the subject needs context; update it when evidence, the design, or the intended audience changes. Use [How-to Guide](how_to_guide.md) for procedures and [Tutorial](tutorial.md) for a learning exercise.

## Principles

- Answer a clear central question and give the reader enough project context to follow it.
- Explain relationships: what causes what, which assumptions matter, and where the reasoning stops.
- Separate observed behavior, requirements, design choices, and hypotheses. Attribute project decisions to their real sources.
- Use a concrete example when it clarifies a relationship. Explain unfamiliar terms before relying on them.
- Discuss meaningful benefits, costs, and limits. Avoid slogans that merely repeat the choice.
- Link detailed procedures and contracts instead of turning the explanation into a runbook or catalog.

## Structure and template

Give a direct answer, relevant background, causal explanation/example, reasons and tradeoffs, limits, and source links. A diagram is useful only if it helps readers follow the relationships.

```md
# Why / How [subject]
[Direct answer]
## Context
[Terms, current system, source/status]
## How it works and why
[Cause/effect, example, decision reasoning]
## Tradeoffs and limits
[Costs, assumptions, failure behavior, unknowns]
## Related sources
[Verified design/decision/procedure links]
```

## Completed example

General hypothetical explanation, not a claim about an existing implementation.

```md
# Why an API sends email through a worker

A worker lets the API accept mail work without keeping the original request open while an outside provider responds. A queue holds the work until a worker can process it.

## Context
The API receives the user's request. The mail provider is an external service whose response time and availability are outside the API's direct control. This example assumes the product distinguishes accepting work from completing delivery.

## How it works and why
After recording an accepted job, the API can respond. The worker retrieves the job, contacts the provider, and records the outcome. If the provider is temporarily unavailable, a defined retry policy can allow later attempts. The example has no agreed retry limit.

## Tradeoffs and limits
The API no longer waits for the provider, but the team must operate the queue, detect stuck jobs, and handle duplicate delivery attempts. Queueing does not prove the provider accepted the message or that the recipient read it. The behavioral specification must define which outcome the product promises.

## Related sources
Use the project's HLD and accepted mail-delivery decision to explain its actual arrangement. This hypothetical example supplies no verified project links.
```

## Quality check

Can a new colleague explain the mechanism, reasons, assumptions, and limits? Check source support and uncertainty. Clear prose should make the causal relationship easier to understand, not conceal missing evidence with a confident story.

## Source

- [Diátaxis: explanation](https://diataxis.fr/explanation/)
