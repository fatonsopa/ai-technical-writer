# SpecDev

SpecDev is a technical writing skill for developers who work with AI coding agents. Designed to extend OpenSpec’s workflow for planning and tracking changes, it turns your team’s decisions into requirements developers can implement, checks testers can run, and guides users can follow. [About OpenSpec](https://github.com/Fission-AI/OpenSpec)

## Quick start

Today the writing skill is available as **Technical Writer**. The planned SpecDev release will use OpenSpec’s own commands and write into your project’s existing change files. [Setup for Codex and Claude Code](docs/installation.md). In Codex, try this request. In Claude Code, use `/technical-writer` for the same request.

> $technical-writer We want support to refund duplicate charges. Read our refund policy and draft the requirements. Flag anything we still need to decide.

If the policy says only managers may approve refunds, the draft keeps that rule. If the policy is silent on repeat requests, the writer asks, “What should happen if someone requests the same refund twice?” Your answer gives the developer and tester a rule they can both use.

[See how SpecDev and OpenSpec work together](#how-specdev-and-openspec-work-together) · [Follow the document flow](#document-flow) · [Browse the documents](#supported-document-types)

<a id="what-specdev-adds-to-openspec"></a>

## How SpecDev and OpenSpec work together

Use OpenSpec directly to plan a change and track its tasks. Choose SpecDev when you also need to turn a rule like “only managers may approve refunds” into instructions for developers, testers and support.

A checkmark shows which tool does the work. **Planned** means it’s for a future release. You can ask for one document at any time.

| What you get | OpenSpec | SpecDev |
| --- | :---: | :---: |
| Give every change a familiar format with [your team’s templates or OpenSpec’s defaults](openspec/changes/ship-specdev/design.md#reuse-the-upstream-implementation). | ✓ | |
| See [where a change stands and what to do next](https://openspec.dev/docs/cli), whether you’re starting it or picking it back up. | ✓ | |
| Find the [proposal, requirements, design and tasks in one place](#core-document-flow). Spot gaps before coding starts. | ✓ | |
| See [which tasks are still open](#where-tasksmd-fits). Archive the finished change so the project’s requirements stay up to date. | ✓ | |
| Answer [only the questions your project leaves open](workflows/discover.md). The writer looks up the rest. | | ✓ |
| Decide [what to build first](#supported-document-types) and keep the [interview notes or research behind that choice](openspec/changes/ship-specdev/specs/spec-driven-authoring/spec.md#seven-authoring-cases-and-hierarchy-acceptance). | | ✓ Planned |
| Agree on [who needs the feature, what it should do and how you’ll know it helped](references/product_requirements_document.md). | | ✓ |
| Understand [why a design was chosen](references/decision_record.md), [how its parts fit together](docs/writing.md#explain-a-flow-with-controlled-colors-and-background) and [what data two services share](references/interface_contract.md). | | ✓ |
| See [which screens and user actions need testing](#supported-document-types) and where the expected result is still unclear. | | ✓ Planned |
| Give a developer [the user’s goal](references/user_story.md) and [a task with a clear way to check it](references/task.md). Small fixes can stand alone. | | ✓ |
| Know [how to test a rule](references/test_specification.md). Try approving a refund without manager access. The approval should be blocked. | | ✓ |
| See [what actually happened in testing](references/test_completion_report.md). Was the approval blocked, did it go through, or has nobody tested it yet? | | ✓ |
| Get [the document you need](#supported-document-types) with a command like `/prd`, or [find out what to write next and why](openspec/changes/ship-specdev/specs/spec-driven-authoring/spec.md#s24-1). | | ✓ Planned |
| Get [clear wording in OpenSpec documents](openspec/changes/ship-specdev/specs/spec-driven-authoring/spec.md#a33b) while keeping the headings and checkboxes your project expects. | | ✓ Planned |
| Help [operators finish a task](references/how_to_guide.md), [new teammates learn it](references/tutorial.md) and [AI assistants follow your rules](references/agents_and_skills.md). | | ✓ |
| Catch [claims your sources don’t support](docs/writing.md#review-a-document). [Fix one paragraph](docs/writing.md#make-a-focused-edit) or [clarify the whole draft](docs/writing.md#rewrite-while-preserving-obligations) while keeping its meaning. | | ✓ |
| See [which requirements the reviewed document covers](docs/writing.md#check-the-result) and which decisions are still open. | | ✓ |

## Document flow

### Core document flow

For a feature that changes product behavior and needs a design decision, OpenSpec uses four files. A proposal identifies the change. The specification and design can then be written in parallel. Both feed the task list.

```mermaid
flowchart TD
    accTitle: Core document flow
    accDescr: The proposal feeds the specification and design. Both feed the task list.
    CP@{ shape: doc, label: "Change Proposal (CP)" }
    SDD@{ shape: doc, label: "Behavioral Specification (SDD)" }
    TD@{ shape: doc, label: "Technical Design (TD)" }
    TL@{ shape: doc, label: "Task List (TL)" }
    CP --> SDD
    CP --> TD
    SDD --> TL
    TD --> TL
    classDef document fill:#D2D2D2,stroke:#4B5563,color:#17212B
    class CP,SDD,TD,TL document
```

### Expanded document flow

<details>
<summary>Show the optional documents and where they fit</summary>

Solid arrows show the same core flow. A dotted arrow means **optional** and points from a document to the work it informs. A story can live in the specification. A task can live in the task list, in its own `task.md`, or in a tracker. An independent fix can start and finish with one task.

```mermaid
flowchart LR
    accTitle: Expanded document flow
    accDescr: Solid arrows connect the four core documents. Dotted arrows link optional supporting documents to their consumers.
    DIR@{ shape: doc, label: "Discovery Interview Record (DIR)" }
    PB@{ shape: doc, label: "Product Brief (PB)" }
    PRD@{ shape: doc, label: "Product Requirements Document (PRD)" }
    CM@{ shape: doc, label: "Capability Map (CM)" }
    CP@{ shape: doc, label: "Change Proposal (CP)" }
    EPIC@{ shape: doc, label: "Epic (EPIC)" }
    US@{ shape: doc, label: "User Story (US)" }
    SDD@{ shape: doc, label: "Behavioral Specification (SDD)" }
    TASK@{ shape: doc, label: "Task (TASK)" }
    TD@{ shape: doc, label: "Technical Design (TD)" }
    REQ@{ shape: doc, label: "Individual Requirement (REQ)" }
    RR@{ shape: doc, label: "Research Record (RR)" }
    DR@{ shape: doc, label: "Decision Record (DR)" }
    HLD@{ shape: doc, label: "High-Level Design (HLD)" }
    LLD@{ shape: doc, label: "Low-Level Design (LLD)" }
    IC@{ shape: doc, label: "Interface Contract (IC)" }
    TM@{ shape: doc, label: "Threat Model (TM)" }
    SOD@{ shape: doc, label: "Service Objectives Document (SOD)" }
    POL@{ shape: doc, label: "Policy (POL)" }
    STD@{ shape: doc, label: "Technical Standard (STD)" }
    RQC@{ shape: doc, label: "Requirements-Quality Checklist (RQC)" }
    FM@{ shape: doc, label: "Feature Map (FM)" }
    CJ@{ shape: doc, label: "Critical Journeys (CJ)" }
    TS@{ shape: doc, label: "Test Specification (TS)" }
    TP@{ shape: doc, label: "Test Plan (TP)" }
    TL@{ shape: doc, label: "Task List (TL)" }
    IP@{ shape: doc, label: "Implementation Plan (IP)" }
    TSR@{ shape: doc, label: "Test Status Report (TSR)" }
    TCR@{ shape: doc, label: "Test Completion Report (TCR)" }
    BR@{ shape: doc, label: "Bug Report (BR)" }
    IR@{ shape: doc, label: "Incident Report (IR)" }
    README@{ shape: doc, label: "Repository Readme (README)" }
    TUT@{ shape: doc, label: "Tutorial (TUT)" }
    HTG@{ shape: doc, label: "How-to Guide (HTG)" }
    EXP@{ shape: doc, label: "Explanation (EXP)" }
    AI@{ shape: doc, label: "Agent Instructions (AI)" }
    SKILL@{ shape: doc, label: "Reusable Skill (SKILL)" }
    OS@{ shape: doc, label: "Claude Code Output Style (OS)" }
    VIS@{ shape: doc, label: "Diagram (VIS)" }
    DIR -.-> PB
    PB -.-> PRD
    PRD -.-> CM
    PRD -.-> CP
    CM -.-> EPIC
    EPIC -.-> US
    US -.-> SDD
    US -.-> TASK
    CP --> SDD
    CP --> TD
    REQ -.-> SDD
    RR -.-> DR
    DR -.-> TD
    HLD -.-> LLD
    LLD -.-> TD
    IC -.-> TD
    TM -.-> TD
    SOD -.-> TD
    POL -.-> STD
    STD -.-> TD
    SDD -.-> RQC
    FM -.-> CJ
    CJ -.-> TS
    TP -.-> TS
    TS -.-> TL
    RQC -.-> TL
    IP -.-> TL
    TASK -.-> TL
    SDD --> TL
    TD --> TL
    TL -.-> TSR
    TSR -.-> TCR
    BR -.-> TASK
    IR -.-> TASK
    TL -.-> README
    TL -.-> TUT
    TL -.-> HTG
    TL -.-> EXP
    TL -.-> AI
    TL -.-> SKILL
    TL -.-> OS
    TL -.-> VIS
    classDef document fill:#D2D2D2,stroke:#4B5563,color:#17212B
    class DIR,PB,PRD,CM,CP,EPIC,US,SDD,TASK,TD,REQ,RR,DR,HLD,LLD,IC,TM,SOD,POL,STD,RQC,FM,CJ,TS,TP,TL,IP,TSR,TCR,BR,IR,README,TUT,HTG,EXP,AI,SKILL,OS,VIS document
```

Tutorials, runbooks, repository guidance, diagrams and assistant instructions can be deliverables in their own right. Write them when someone needs them. Verification reports describe results after the corresponding checks have run.

</details>

### Where `tasks.md` fits

Once the requirements and any needed design are ready, list the work and its checks in `tasks.md`. Link a separate `task.md` or tracker task when it already owns its own acceptance criteria. During implementation the agent picks a ready task, checks the result, and updates its checkbox. A standalone fix can start and finish in one task. [See this project’s task list](openspec/changes/ship-specdev/tasks.md)

## Supported document types

Today, ask for a document by name. Each row links to its guide or marks the format as planned. The short commands are planned for the SpecDev release. If a command is taken, you’ll still be able to ask by name or use a command such as `/specdev doc dr` in Claude Code or `$specdev doc dr` in Codex.

<details>
<summary>Show all 39 documents and their commands</summary>

| Command | Document | What it answers and when you need it |
| --- | --- | --- |
| `/interview` | [Discovery Interview Record (DIR)](openspec/changes/ship-specdev/specs/spec-driven-authoring/spec.md#s14-1) | Planned format. What did the owner confirm, and what is still open? Use when answers affect scope. |
| `/brief` | [Product Brief (PB)](openspec/changes/ship-specdev/specs/spec-driven-authoring/spec.md#s05-1) | Planned format. Is this problem worth solving? Use before committing to a product direction. |
| `/prd` | [Product Requirements Document (PRD)](references/product_requirements_document.md) | Who needs what outcome? Use to agree on the product goal and scope. |
| `/capability-map` | [Capability Map (CM)](openspec/changes/ship-specdev/specs/spec-driven-authoring/spec.md#s15-1) | Planned format. Which capabilities can ship separately, and which depend on each other? |
| `/epic` | [Epic (EPIC)](openspec/changes/ship-specdev/specs/spec-driven-authoring/spec.md#s21-1) | Planned format. Which stories deliver one larger outcome? Use when they need coordination. |
| `/proposal` | [Change Proposal (CP)](openspec/changes/ship-specdev/proposal.md) | Why make this OpenSpec change, and what does it cover? |
| `/story`, `/us` | [User Story (US)](references/user_story.md) | What should one person be able to do, and what counts as success? |
| `/sdd`, `/spec` | [Behavioral Specification (SDD)](references/spec_driven_development.md) | What must the software do? Use for rules, exceptions, and observable outcomes. |
| `/requirement` | [Individual Requirement (REQ)](references/spec_driven_development.md#writing-an-individual-requirement) | Which single rule needs to be added or clarified? |
| `/research` | [Research Record (RR)](openspec/changes/ship-specdev/specs/spec-driven-authoring/spec.md#s16-1) | Planned format. What evidence settles a design question, and what remains unknown? |
| `/dr` | [Decision Record (DR)](references/decision_record.md) | Which option did we choose and why? Use when the rationale needs to survive. |
| `/hld` | [High-Level Design (HLD)](references/high_level_document.md) | Which parts of the system change, and how do they fit together? |
| `/lld` | [Low-Level Design (LLD)](references/low_level_design.md) | How will one component handle its data, interfaces, and failures? |
| `/ic` | [Interface Contract (IC)](references/interface_contract.md) | What do two components exchange, and how must each handle errors? |
| `/tm` | [Threat Model (TM)](references/threat_model.md) | What could go wrong, and which safeguards address each risk? |
| `/sod` | [Service Objectives Document (SOD)](references/service_objectives.md) | How reliable must the service be, and how will we measure it? |
| `/pol` | [Policy (POL)](references/policy.md) | What may or must people do, and who can approve exceptions? |
| `/std` | [Technical Standard (STD)](references/technical_standard.md) | Which technical rule applies, and how is compliance checked? |
| `/design` | [Technical Design (TD)](openspec/changes/ship-specdev/design.md) | How will we build this change? Record choices, trade-offs, and risks. |
| `/ip` | [Implementation Plan (IP)](references/implementation_plan.md) | How will we deliver and verify the work? Use the change design for one OpenSpec change or a separate plan for work coordinated across changes. |
| `/requirements-checklist` | [Requirements-Quality Checklist (RQC)](openspec/changes/ship-specdev/specs/spec-driven-authoring/spec.md#s19-1) | Planned format. Which requirements are ready to build, and which still need a decision? |
| `/feature-map` | [Feature Map (FM)](openspec/changes/ship-specdev/specs/spec-driven-authoring/spec.md#s17-1) | Planned format. Where can someone find a feature and check its behavior? |
| `/journeys` | [Critical Journeys (CJ)](openspec/changes/ship-specdev/specs/spec-driven-authoring/spec.md#s18-1) | Planned format. Which user paths matter most, and what outcome should each reach? |
| `/tp` | [Test Plan (TP)](references/test_plan.md) | What will testing cover, and when can it finish? |
| `/ts` | [Test Specification (TS)](references/test_specification.md) | What inputs, steps, and result will prove a requirement? |
| `/tasks` | [Task List (TL)](openspec/changes/ship-specdev/tasks.md) | What can start, what must wait, and how will each item be checked? Use for a multi-task change. |
| `/task` | [Task (TASK)](references/task.md) | What is this one assignment, and how will we know it is done? Use it for a bounded change or independently tracked work. |
| `/tsr` | [Test Status Report (TSR)](references/test_status_report.md) | While testing is underway, what passed, failed, or is blocked? |
| `/tcr` | [Test Completion Report (TCR)](references/test_completion_report.md) | When testing ends, what did it prove and what risks remain? |
| `/br` | [Bug Report (BR)](references/bug_report.md) | What failed, what should have happened, and how can someone investigate? |
| `/ir` | [Incident Report (IR)](references/incident_report.md) | Who was affected, how did the team recover, and what needs follow-up? |
| `/readme` | [Repository Readme (README)](references/readme.md) | What is this project, how do I start, and where can I find help? |
| `/tut` | [Tutorial (TUT)](references/tutorial.md) | How can a learner practice a skill and recognize a successful result? |
| `/htg` | [How-to Guide (HTG)](references/how_to_guide.md) | How do I complete this task or recover if a step fails? |
| `/exp` | [Explanation (EXP)](references/explanation.md) | How does this work, and why was it designed this way? |
| `/agent` | [Agent Instructions (AI)](references/agents_and_skills.md#agent-format) | When should this agent act, what may it do, and what must it return? |
| `/skill` | [Reusable Skill (SKILL)](references/agents_and_skills.md#skill-format) | How should an agent perform this repeatable task? |
| `/output-style` | [Claude Code Output Style (OS)](references/agents_and_skills.md#output-style-format) | How should Claude Code word and format its session replies? |
| `/diagram` | [Diagram (VIS)](references/visuals.md) | Which flow or relationship would a reader understand faster as a picture? |

</details>

## Guides

- [Installation](docs/installation.md) covers source setup, host selection, and the check to run after installation.
- [Writing examples](docs/writing.md) show how to create a document, edit a passage, and review a draft against its sources.
- [Troubleshooting](docs/writing.md#limits-and-help) covers missing skills, missing dependencies, and rejected drafts.

### How OpenSpec works behind SpecDev

In the planned release, you’ll be able to run the commands your installed OpenSpec supports from the same conversation. For example, `/specdev init` in Claude Code or `$specdev init` in Codex will ask OpenSpec to set up the current project. [OpenSpec commands](https://openspec.dev/docs/cli)

### Planned release installation

The SpecDev installer and npm package are planned. You can use the source installation today. [Release installation, updates and removal](docs/installation.md#planned-release-installation)

## Development

[Contributor guide](docs/development.md) · [Evaluate writing quality](evals/README.md) · [Implementation plan](plan/README.md) · [MIT license](LICENSE)
