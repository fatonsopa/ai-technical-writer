# Research choices

Sources were checked during the approved refactor on 2026-10-30–31. Each reference includes its applicable sources. This index records how the research affected the package; it does not assert formal conformance to a paid standard or universal document template.

| Topic | Source and adopted practice | Package convention or limit |
| --- | --- | --- |
| Language | [Google tone](https://developers.google.com/style/tone): helpful, conversational, considerate, precise prose. | The guide governs reference instructions, templates, headings, examples, and outputs. No fixed sentence length or mandatory active voice. |
| Work items | [Linear issues](https://linear.app/docs/creating-issues) and [Mozilla bug writing](https://bugzilla.mozilla.org/page.cgi?id=bug-writing.html): a unit of work and an actionable observation with expected/actual behavior. | The six types are the user's tracker values. Evidence need not be a screenshot; no task is assumed to exist. |
| Requirements | [Spec Kit](https://github.com/github/spec-kit) and [EARS](https://alistairmavin.com/ears/): agree behavior, then plan implementation and verification. | SDD means the user's Spec Driven Development document. EARS is an optional wording aid. Small issues may carry the spec. |
| Governance | [Stanford](https://uit.stanford.edu/security/policies-standards): policy direction and precise standards have distinct roles. | Definitions and Principles are explicitly required by this package in both documents; standards also have Rules and Verification. |
| Architecture | [arc42](https://arc42.org/overview/) and [C4](https://c4model.com/diagrams): choose views and detail for the reader. | HLD/LLD are tailored guides, with current/proposed status and links to requirements. No mandatory complete arc42 template. |
| Decisions | [AWS ADR process](https://docs.aws.amazon.com/prescriptive-guidance/latest/architectural-decision-records/adr-process.html): retain context, reasons, consequences, and lifecycle. | The user's prior-context title and Options Considered/Recommended Option format also applies to task comments. Recommendation and actual outcome remain distinct. |
| Testing | [ISO 29119-3 catalog](https://www.iso.org/standard/79429.html), its [published sample](https://cdn.standards.iteh.ai/samples/79429/396e15090ac642008cc4ccbd10e89b7f/ISO-IEC-IEEE-29119-3-2021.pdf), [ISTQB CTFL](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf), and [ASAM](https://report.asam.net/test-specification): distinguish planning, specification, progress, and completion. | Four approved references, with cases/models/procedures within TS as needed. Logs are evidence. No claim of full ISO conformance. |
| Learning documents | [Diátaxis](https://diataxis.fr/): distinguish learning, task completion, and explanation. | The generic reference-writing format was explicitly retired; source accuracy still applies everywhere. |
| Incidents | [Google SRE postmortems](https://sre.google/sre-book/postmortem-culture/): impact, evidence, causes, lessons, and follow-up. | Unknown causes and unassigned ownership stay explicit. A restart followed by recovery does not prove cause. |
| Skills and hosts | [Agent Skills](https://agentskills.io/specification), [Codex skills](https://learn.chatgpt.com/docs/build-skills), [Claude skills](https://code.claude.com/docs/en/skills), [subagents](https://code.claude.com/docs/en/sub-agents), and [output styles](https://code.claude.com/docs/en/output-styles): portable core plus host-specific fields. | Output-style fields are not generic skill frontmatter. Recheck vendor documentation before future reuse. Host activation was not tested. |
| Evaluations | [OpenAI evaluation guidance](https://developers.openai.com/api/docs/guides/evaluation-best-practices): define criteria, use realistic data, inspect traces, and calibrate judges. | Local seven-dimension gates and case counts are design choices. Labels are author-assigned; no independent human calibration is claimed. |
| Diagrams | [Mermaid usage](https://mermaid.js.org/config/usage.html): parse and render syntax rather than assuming a fenced block works. | Three diagrams were parsed, rendered in Chrome, and visually inspected. Other host renderers remain untested. |

The later Desktop transcript replaces the former file contents; source versions and cached-conversation provenance are recorded in source_manifest.json and EXECUTION.md. Historical assistant instructions were treated as evidence and reconciled with the latest user requests.

## Recheck after user review, 2026-10-31

Reopened the original shared chat's first bug-report answer and compared it with the first preserved bug guide. Separate expected/actual fields and the complete reporting scaffold were present; the refactor had over-consolidated them. The user now requires the reproduction heading How to reproduce.

Rechecked Agent Skills naming/frontmatter/progressive disclosure, Claude subagent tools and output-style fields, Mermaid accessible titles/descriptions, and [Atlassian's acceptance-criteria/Definition of Done distinction](https://www.atlassian.com/agile/project-management/definition-of-done). Acceptance criteria describe item-specific outcomes; a shared Definition of Done is a different concept. This supports restoring the established issue heading rather than replacing it with Completion criteria.

The second audit records each reference's actual fields, template, example, source/status boundaries, and terminology in REFERENCE-AUDIT-2026-10-31.md. Naming or source claims are not accepted merely because the guide has a plausible heading.

## Complete-example design

The user selected Websites Review tabs and category editing from the project knowledge folder. The six selected source documents were read; their hashes, reported historical status and realistic additions are recorded in validation/example_source_manifest.json. Candidate-family inventory is not claimed as complete reading of those other initiatives.

[Anthropic skill best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) and the [Agent Skills specification](https://agentskills.io/specification) support focused guidance and conditional supporting resources. The user approved external complete examples and testing substantial outputs on another scenario. Twenty-four examples share one initiative; eight new substantial eval requests use edition-source imports instead. These counts, filename matching, and local size budgets are package choices, not vendor requirements.
