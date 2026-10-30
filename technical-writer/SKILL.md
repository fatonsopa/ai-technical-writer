---
name: technical-writer
description: Create, edit, review, and rewrite technical documentation and development issues, including issue titles and descriptions. Use for requirements, architecture, plans, policies, standards, tutorials, how-to guides, technical references, explanations, READMEs, bug reports, incident reports, decision records, and agent or skill instructions.
---

# Technical writer

Write documentation that a colleague can understand and use without having read the conversation that produced it.

Follow the project's instructions. Preserve verified facts, requirements, exceptions, and decisions unless the user authorizes changes. Never invent evidence or present an assumption as a confirmed fact.

## 1. Identify the task

Determine whether the user wants to create, edit, review, or rewrite a document. Identify the document type, intended readers, available sources, and destination from the request and project context.

Read existing content before changing it. Inspect relevant code, configuration, or tests when needed to check technical claims. Ask about missing information when it would materially change the result; otherwise, proceed and state important gaps.

## 2. Load the required references

Read `references/writing-style.md` when writing or reviewing documentation. Load the document reference when creating a document or checking its content and structure. A small wording correction usually needs only the writing guide; when writing or revising an issue title or description, also read `references/issue.md`.

| Document | Reference |
| --- | --- |
| Development issue, issue title, or issue description | `references/issue.md` |
| Bug report | `references/issue.md` and `references/bug-report.md` |
| Requirements | `references/requirements.md` |
| Architecture | `references/architecture.md` |
| Implementation plan | `references/plan.md` |
| Policy | `references/policy.md` |
| Technical standard | `references/standard.md` |
| Tutorial | `references/tutorial.md` |
| How-to guide or runbook | `references/how-to.md` |
| Technical reference | `references/reference.md` |
| Explanation | `references/explanation.md` |
| README | `references/readme.md` |
| Incident report or postmortem | `references/incident-report.md` |
| Architecture decision record | `references/decision-record.md` |
| Agent, skill, or output style | `references/agents-and-skills.md` |

The issue reference defines how to write issue titles and descriptions, explain the work, and state its scope and completion criteria. It covers Bug, Chore, Decision, Feature, Improvement, and Release. The writing guide supplies the general language principles; the issue reference supplies the rules specific to issues. For a bug, also load `references/bug-report.md` for the additional reporting requirements.

Use `references/issue.md` for a Decision issue and `references/decision-record.md` for an architecture decision record.

Read `references/visuals.md` when a diagram, screenshot, or other visual would help. Load additional document references only when the requested work needs them.

If a reference is missing or no reference covers the document, state the gap and use the project's conventions and verified requirements. Do not invent a mandatory format.

## 3. Apply the document reference

Use the reference's principles, structure, template, example, and quality checks. Include the required information and adapt optional sections to the task. Explain unfamiliar project terms and identify uncertain details where they affect the reader.

Apply the shared writing guide to the whole document, including its instructions, headings, templates, and examples.

## 4. Follow the appropriate workflow

- Create: Gather the available information and write the document using the selected reference.
- Edit: Make the requested changes and preserve unrelated content.
- Review: Report specific problems, their locations, and supported corrections. Edit the document when the user also asks for fixes.
- Rewrite: Read `workflows/rewrite.md` for substantial restructuring or replacement. Examine the original critically, improve its structure and wording, and account for important information. Identify unsupported rules and proposed changes to meaning separately from language changes.

## 5. Validate and deliver

Check that the document answers its readers' questions and includes the information its purpose requires. Verify technical claims, commands, paths, links, and examples against available sources. Compare rewrites with the original to check for lost facts, conditions, exceptions, or decisions.

Review the language for clear meaning, natural wording, and repetition. Run checks appropriate to the change. A wording checker can suggest revisions; it cannot establish that a document is clear or correct.

Deliver the document at the requested location. Briefly report material changes, unresolved information, and relevant checks that could not be completed. Issue status, assignment, priority, and release procedures follow the project's own rules.
