# Choose a document for your change

Start with the question you need to answer. You can ask for one document by name or use its shortcut. The [full document table](../README.md#supported-document-types) lists the commands.

## Plan an OpenSpec change

When a feature changes how the product works, give SpecDev the change you want to make and any existing rules. OpenSpec keeps the change together in your project.

| Document | What goes there |
| --- | --- |
| Change proposal (`proposal.md`) | The problem, why it matters and what the change covers. |
| Behavioral specification (`specs/`) | The behavior users should see, with a scenario for each rule or exception. |
| Technical design (`design.md`) | The design decisions, trade-offs and risks that affect implementation. |
| Task list (`tasks.md`) | The work in dependency order, what can run in parallel and how to check it. |

For a standalone fix, use `/task`. A broken link needs the current link, its intended destination and a check that the corrected link opens. Give it a parent when it contributes to an existing story or requirement. For writing alone, ask for the document and supply its sources.

For an example of a requirement carried into testing, see [the rule for saving a category](../examples/spec_driven_development.md#web-06-support-dependable-inline-assignment), [the story’s failure case](../examples/user_story.md#acceptance-criteria) and [the check for a rejected save, T10](../examples/test_specification.md#editing-and-mutation-cases). One task would be to keep the selected category visible if saving fails. T10 describes how to check it. A test report records what actually happened.

## Product brief

Use `/brief` when you know the problem and still need to decide whether to pursue it. Supply who is affected, the outcome you want and any time or scope limit. You get a short brief that marks missing figures or unresolved choices.

## Discovery interview

Use `/interview` when an answer will change the scope. Supply the question, existing project evidence and any answers already given. The record distinguishes what the owner confirmed from what still needs a decision.

## Capability map

Use `/capability-map` when several parts of a feature could ship separately. Give the goal and known dependencies. The map shows what each part delivers, what has to come first and what can start together.

## Epic

Use `/epic` when several stories contribute to one outcome. Supply that outcome and the stories or requirements that belong to it. The epic connects them and describes how to tell when they deliver the whole result.

## Research record

Use `/research` when a design decision depends on a question you can investigate. Give the question and available sources. The record shows what the evidence supports, what is uncertain and who owns the decision.

## Requirements checklist

Use `/requirements-checklist` before building if a rule or its acceptance check is unclear. Supply the specification revision. The checklist points to the relevant text, identifies what is clear and records the questions that still block work.

## Feature map

Use `/feature-map` to help someone find and check a feature. Supply the project revision and its known screens, routes or controls. The map shows where to start and what to look for. It identifies proposed features separately.

## Critical journeys

Use `/journeys` to choose which user paths to test. Supply the users, entry points and risks. Each journey names the steps, expected outcome and relevant check, including any gap where a test is still needed.
