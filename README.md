# SpecDev

SpecDev helps you and your AI coding agent agree in writing on what to build before anyone builds it. It is a skill for Codex and Claude Code that writes a project's requirements, designs, tasks and test plans from what the project already says, and asks you about the rest.

## Why it exists

An AI agent builds whatever you describe. When the description is vague, the agent fills the gaps with guesses, and you learn which guesses were wrong after the code is written. Spec-driven development avoids this by settling the decisions first: what the software must do, how it will be built, what work that takes and how you'll know it works. The agent then builds from those documents.

An AI asked to write those documents guesses in the same way. A requirements document with invented details does more harm than a missing one, because it looks finished and people build from it. SpecDev exists to write these documents without the guessing.

## How it works

Say you ask for the requirements for letting customers cancel a paid order.

1. It reads first. SpecDev uses what your files, code and earlier documents already settle, and doesn't ask you to repeat it.
2. It asks about what is missing. If two files disagree, or your policy is silent on orders that have shipped, it asks you before it writes. Decisions nobody has made yet are listed as open.
3. It writes the document in a set structure and saves it as a new file. The files it read stay as they were.
4. It checks the document against your sources and your request before you get it.
5. It stops there. SpecDev builds a task only when you tell it to.

## The documents

Each document answers one question, and most projects need only a few of them. Fixing a broken link takes a single task. A new product area might need most of this list.

| Question | Document |
| --- | --- |
| Is this problem worth solving? | [Product Brief (PB)](docs/choosing-documents.md#product-brief) |
| Who is it for, and what must it achieve? | [Product Requirements Document (PRD)](references/product_requirements_document.md) |
| What must the software do? | [Spec Driven Development document (SDD)](references/spec_driven_development.md) |
| How will we build it, and why that way? | [Technical Design (TD)](docs/choosing-documents.md#plan-an-openspec-change) and [Decision Record (DR)](references/decision_record.md) |
| What work does it take? | [Task List (TL)](docs/choosing-documents.md#plan-an-openspec-change) and [Task (TASK)](references/task.md) |
| How will we prove it works? | [Test Specification (TS)](references/test_specification.md) |
| Did it work? | [Test Completion Report (TCR)](references/test_completion_report.md) |
| What went wrong? | [Bug Report (BR)](references/bug_report.md) and [Incident Report (IR)](references/incident_report.md) |
| How do people use it? | [How-to Guide (HTG)](references/how_to_guide.md) and [Tutorial (TUT)](references/tutorial.md) |

If you don't know which one you need, ask "what should I write next?". SpecDev looks at what exists and names the one document that fills the next gap. The [full list](#supported-document-types) has 37 types.

## SpecDev and OpenSpec

[OpenSpec](https://github.com/Fission-AI/OpenSpec) is an open-source tool for planning changes to a project. Each change gets a short plan that covers why it's needed, what will be different, how it will be done and the work involved. OpenSpec keeps that plan in one place and tracks progress until the change ships.

SpecDev comes with OpenSpec built in, so there is nothing extra to install. OpenSpec keeps the plan organized. SpecDev writes what goes into it, asks the questions and checks the result.

| You want to | OpenSpec | SpecDev |
| --- | :---: | :---: |
| Keep a change's proposal, specifications, design and tasks together | ✓ | |
| Use [your team's templates](https://openspec.dev/docs/customize-schemas) | ✓ | |
| Track tasks and archive a finished change | ✓ | |
| Be asked about the [decisions your files leave open](workflows/discover.md) | | ✓ |
| Write the documents around a change, from product briefs to test reports | | ✓ |
| [Edit or rewrite](docs/writing.md) a document without changing what it requires | | ✓ |
| Have a document [checked against its sources](docs/writing.md#review-a-document) before you receive it | | ✓ |

<a id="where-tasksmd-fits"></a>

### How a requirement becomes a task

Inside a change, the task list is one file, `tasks.md`. Each numbered item names its scope, the requirement it satisfies and the evidence that completes it, so most items need no document of their own. A separate Task (TASK) is for work tracked on its own, or for a small fix that belongs to no change. [See an example](docs/choosing-documents.md#plan-an-openspec-change)

## Installation

You need macOS, Linux or WSL, with Python 3.11 or later and Node.js 22.20.0 or later.

```sh
curl -fsSL https://github.com/fatonsopa/ai-technical-writer/releases/latest/download/install.sh | sh
specdev host init --tools codex,claude
```

The first line installs SpecDev after checking the download against the release checksums. The second adds it to Codex and Claude Code; leave out the one you don't use. [Update or remove SpecDev](docs/installation.md#update-or-remove-specdev)

## Using it

Open your project in a new session and describe what you need. Start with `$specdev` in Codex or `/specdev` in Claude Code.

> /specdev Write the requirements for cancelling a paid order. Use docs/cancellation-policy.md.

To have OpenSpec manage changes in the project, run `/specdev init` once. A single document needs no setup.

## Supported document types

Ask for a document by name, by acronym or by command, as in `/specdev doc dr` for a Decision Record (DR). Commands such as `/dr` work on their own once you install them as shortcuts. From the installed skill folder, run the line below with the commands you want, or `all` for every one. Use `--host codex` for Codex. Setup skips any name another tool already uses.

```sh
.venv/bin/python scripts/shortcuts.py install --host claude-code dr task tasks
```

<details>
<summary>All 37 document types</summary>

| Command | Document | Use it when |
| --- | --- | --- |
| `/interview` | [Discovery Interview Record (DIR)](docs/choosing-documents.md#discovery-interview) | The owner's answers would change the scope. |
| `/brief` | [Product Brief (PB)](docs/choosing-documents.md#product-brief) | You need to decide whether a problem is worth solving. |
| `/prd` | [Product Requirements Document (PRD)](references/product_requirements_document.md) | People need to agree on who the product serves and what it must achieve. |
| `/capability-map` | [Capability Map (CM)](docs/choosing-documents.md#capability-map) | A large initiative needs splitting into parts that can ship separately. |
| `/epic` | [Epic (EPIC)](docs/choosing-documents.md#epic) | Several stories serve one larger outcome. |
| `/proposal` | [Change Proposal (CP)](docs/choosing-documents.md#plan-an-openspec-change) | You're starting an OpenSpec change. |
| `/story`, `/us` | [User Story (US)](references/user_story.md) | One person needs to do something, and success needs a definition. |
| `/sdd`, `/spec` | [Spec Driven Development document (SDD)](references/spec_driven_development.md) | People need to agree on what the software must do. |
| `/research` | [Research Record (RR)](docs/choosing-documents.md#research-record) | A design question needs evidence before anyone decides. |
| `/dr` | [Decision Record (DR)](references/decision_record.md) | A choice and the reasons for it need to be on record. |
| `/hld` | [High Level Document (HLD)](references/high_level_document.md) | The way a system's parts fit together is changing. |
| `/lld` | [Low Level Design (LLD)](references/low_level_design.md) | One component needs its data, interfaces and failure handling designed. |
| `/ic` | [Interface Contract (IC)](references/interface_contract.md) | Two components need an agreed exchange, errors included. |
| `/tm` | [Threat Model (TM)](references/threat_model.md) | You need to know what could go wrong and how each risk is handled. |
| `/sod` | [Service Objectives Document (SOD)](references/service_objectives.md) | A service needs reliability targets and a way to measure them. |
| `/pol` | [Policy (POL)](references/policy.md) | People need rules on what they may or must do. |
| `/std` | [Technical Standard (STD)](references/technical_standard.md) | A technical rule needs a compliance check. |
| `/design` | [Technical Design (TD)](docs/choosing-documents.md#plan-an-openspec-change) | An OpenSpec change needs its approach and trade-offs written down. |
| `/ip` | [Implementation Plan (IP)](references/implementation_plan.md) | Work across several changes needs a delivery plan. |
| `/requirements-checklist` | [Requirements-Quality Checklist (RQC)](docs/choosing-documents.md#requirements-checklist) | You need to know which requirements are ready to build. |
| `/feature-map` | [Feature Map (FM)](docs/choosing-documents.md#feature-map) | A tester needs to find a feature and check it. |
| `/journeys` | [Critical Journeys (CJ)](docs/choosing-documents.md#critical-journeys) | The most important user paths need end-to-end checks. |
| `/tp` | [Test Plan (TP)](references/test_plan.md) | Testing needs a scope and a finish line. |
| `/ts` | [Test Specification (TS)](references/test_specification.md) | A requirement needs inputs, steps and an expected result. |
| `/tasks` | [Task List (TL)](docs/choosing-documents.md#plan-an-openspec-change) | An OpenSpec change needs its work listed. |
| `/task` | [Task (TASK)](references/task.md) | One piece of work needs a scope and acceptance criteria. |
| `/tsr` | [Test Status Report (TSR)](references/test_status_report.md) | Testing is underway and people need its status. |
| `/tcr` | [Test Completion Report (TCR)](references/test_completion_report.md) | Testing has ended and people need its results and remaining risk. |
| `/br` | [Bug Report (BR)](references/bug_report.md) | Something failed and someone needs to investigate it. |
| `/ir` | [Incident Report (IR)](references/incident_report.md) | An incident's impact, recovery and follow-up need to be on record. |
| `/readme` | [Repository readme (README)](references/readme.md) | A repository needs an entry point. |
| `/tut` | [Tutorial (TUT)](references/tutorial.md) | A learner needs a guided exercise. |
| `/htg` | [How-to Guide (HTG)](references/how_to_guide.md) | Someone needs the steps for a task and a way to recover when one fails. |
| `/exp` | [Explanation (EXP)](references/explanation.md) | Someone needs to understand how something works and why. |
| `/agent` | [Agent Instructions (AI)](references/agents_and_skills.md#agent-format) | An AI agent needs a role and limits. |
| `/skill` | [Reusable Skill (SKILL)](references/agents_and_skills.md#skill-format) | An agent needs instructions for a repeatable task. |
| `/output-style` | [Claude Code Output Style (OS)](references/agents_and_skills.md#output-style-format) | Claude Code's replies need a set wording and format. |

The Change Proposal (CP), Spec Driven Development document (SDD), Technical Design (TD) and Task List (TL) are OpenSpec files, so OpenSpec sets their format and location.

Two more commands add to any document:

- `/requirement`: one [Individual Requirement (REQ)](references/spec_driven_development.md#writing-an-individual-requirement) that adds or clarifies a single rule.
- `/diagram`: a [Diagram (VIS)](references/visuals.md) for a flow or relationship that reads better as a picture.

</details>

## Documentation

- [Choose a document](docs/choosing-documents.md)
- [Write, edit and review documents](docs/writing.md)
- [Install, update or remove SpecDev](docs/installation.md)

## Support

[Fix a setup or writing problem](docs/writing.md#limits-and-help) or [report an issue](https://github.com/fatonsopa/ai-technical-writer/issues).

## Development

[Contributor guide](docs/development.md) · [MIT license](LICENSE)
