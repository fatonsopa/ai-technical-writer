# Write and review project documents

Use these examples in Codex with `$specdev`. In Claude Code, start with `/specdev`. Give the writer the facts, project files, or draft it should use.

## Create a complete document

> $specdev Write a PRD from the attached product brief. Use the PRD reference and output contract. Separate agreed scope, proposed capabilities, and unresolved goals. Save the accepted document to the requested project path.

You receive a complete product document with the required sections and source-supported content. A heading check cannot replace the review of its purpose, facts, and scope.

## Work through an incomplete architecture brief

> $specdev Prepare an HLD for this feature. Inspect the existing code, schema and workflows first. Research missing technical information, then guide me through unresolved scope, behavior and design choices using the available question interface. Use diagrams only where they help explain the design.

The skill uses reliable project facts without asking you to repeat them. It asks focused questions in dependency order, explains meaningful options, and accepts written answers. Material unanswered choices remain open; an early document stays a draft. A complete brief needs no questionnaire. Diagrams carry their visible title, scope subtitle and symbol legend inside the image, with detailed element explanations below it. Sequence numbering expresses order; hierarchical IDs require actual decomposition.

## Explain a flow with controlled colors and background

> $specdev Explain this user flow using the shared flowchart style. Use the light dotted canvas and appropriate pastel shapes, export an SVG, retain its editable Mermaid source, and explain its elements below the diagram.

The [flowchart workflow](../workflows/flowcharts.md) uses a shared palette and a background built into the SVG, so a Markdown theme cannot turn the canvas transparent or dark. Shapes and labels preserve meaning without color. Only needed diagrams are created. Their sources and exports are checked together before accepted delivery.

## Make a focused edit

> $specdev Change only this task's title to describe the observed failure. Preserve the description and every other field.

You receive the requested title change. A file edit preserves content outside its declared title or excerpt; it does not expand into a complete document rewrite.

## Review a document

> $specdev Review this implementation plan against the supplied SDD. Return located gaps and recommended corrections. Do not rewrite the plan.

You receive findings tied to the source requirements. A review does not overwrite the document being reviewed or authorize implementation.

## Rewrite while preserving obligations

> $specdev Rewrite this technical standard for clarity. Preserve every obligation, exception, limit, and identifier. Explain any unresolved contradiction before changing its meaning.

The result retains the required governance structure and is checked against the original text. The preservation tools assist the comparison; semantic review is still required.

## Edit an OpenSpec document

Open the existing change and name the passage you want edited. For example, ask SpecDev to clarify who approves a refund in the change specification and give it the policy to use. SpecDev edits the existing file and preserves its requirement headings, scenario markers and task checkboxes. Check the wording against the policy and use OpenSpec validation to check the format.

## Improve after a failed output

> $specdev This output omitted a required PRD section. Correct the draft and identify the reusable guidance or check responsible for the miss. Keep the failing input and output as a regression case; preserve unrelated guidance.

The failure remains recorded. A repaired draft needs new checks and review; a previous receipt does not transfer to changed content. Persistent skill maintenance follows the authorized scope.

## Check the result

The host normally runs this workflow for you. Use [the document-gate commands](../workflows/rewrite.md#validate-the-actual-output) to inspect it or run it yourself. A request identifies the document type, operation, scope, source inputs, destination, explicit requirements, and material values to preserve.

1. `prepare` captures the source, destination baseline, selected guides, contract, and validator identity.
2. `check` validates structure, declared readiness, data constraints and selected visual requirements. Embedded Mermaid also needs a passing syntax check.
3. `packet` supplies the actual draft and frozen evidence for review.
4. `review` validates the submitted judgment, including every explicit requirement.
5. `finalize` delivers only the exact reviewed bytes when the applicable gates pass.

Missing sections, incorrect hierarchy, failed requirements, stale reviews, changed inputs, and newer destination edits block accepted delivery. Required structure does not authorize inventing content to fill a gap. Narrow edits and reviews use their own scope.

Complete Product Requirements Document (PRD), Spec Driven Development document (SDD), High Level Document (HLD), Low Level Design (LLD) and implementation-plan requests include a source-bound discovery record. See [discovery](../workflows/discover.md) for its format. An empty decision list is valid when the sources settle the choices. A known unanswered blocking decision prevents ready delivery.

## Limits and help

- **The skill is missing:** confirm the installed folder contains `SKILL.md` and use your host's explicit invocation. Refresh the session if needed.
- **A Python import fails:** run the environment setup with the installed `scripts/requirements-lock.txt` and use `.venv/bin/python`.
- **Checks reject a draft:** read the actual findings. Correct missing structure or data; do not add unsupported facts or weaken the contract.
- **An input, guide, or evaluator changed:** preserve the old evidence and prepare a new versioned session.
- **A result remains pending:** obtain the required review. A high aggregate score cannot waive critical failures or missing coverage.

For support, [open a GitHub issue](https://github.com/fatonsopa/ai-technical-writer/issues) with the skill version, host, sanitized input, expected result, actual result, and reproduction steps. Keep credentials and private project data out of public reports.
