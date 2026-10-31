# Reference audit after user review

The user found structural and terminology problems after the initial delivery. This audit rereads every reference individually, using writing_style.md for the guide prose and comparing document responsibilities, required structure, templates, completed examples, source evidence, lifecycle, and file relationships. Earlier passing model scores do not establish that a lost structural requirement was preserved.

This first pass predates the connected Websites Review collection. Its example descriptions record that checkpoint; the collection audit below supersedes them.

## Findings

| Order | File | Finding and disposition |
| --- | --- | --- |
| 1 | writing_style.md | Reread all nine principles and examples. Retain natural prose, sentence-case headings, exact terminology, uncertainty, preservation, and the six accepted Linear pairs. Document-specific section names belong to their owning references. No substantive change needed. |
| 2 | issue.md | “Completion criteria” was an inappropriate replacement for the requested issue term. Renamed both template and completed example to Acceptance criteria, restored an explicit Expected outcome, and separated optional Relevant files from Additional context. Preserve six types, specification links, and scoped operations. |
| 3 | bug_report.md | Combined fields lost the original report structure. Restored separate Description/Environment/How to reproduce/Expected result/Actual result/Frequency/Severity and impact/Evidence/Relevant files/Verification, optional prerequisites/context, real numbered steps, and honest code-access limitations. Template and example now agree; deterministic and behavioral checks added. |

| 4 | product_requirements_document.md | Problem/users, goals and success measures, scope, journeys, dependencies/risks/decisions, status and SDD links are present in both template and complete example. Clarified the create trigger and source/assumption wording; removed an author aside from the example. Product intent remains separate from detailed behavior and technical design. |
| 5 | spec_driven_development.md | Requirement entries cover source/status, actor/condition/obligation/exception and verification; the complete example maps every REQ including permissions. Renamed the template/example heading Acceptance to Acceptance criteria. Keep SDD as the user-defined behavioral document, with design constraints sourced and unresolved limits blocking readiness explicitly. |

| 6 | high_level_document.md | Context, components, runtime/data flow, deployment/operations, decisions/risks, definitions and requirement drivers are present. Added the missing failure-preservation requirement link in the example; replaced an unsupported assumption about established tracing with an explicit operational gap. Current/proposed architecture and the living-document lifecycle remain clear. |
| 7 | low_level_design.md | Internal contracts/state/data, atomicity, failure behavior, permissions, unresolved concurrency/retries, DDR and verification are present. Proposed technical decisions are distinguished from behavioral requirements; unknown schema/function names are not invented. No change needed. |
| 8 | implementation_plan.md | Goal/spec links, verified versus proposed context, dependencies, work sequence, requirement coverage, rollout/recovery, risks and blocking choices are present. Added explicit status/source metadata to template/example and used acceptance criteria for the small-issue source. It remains a delivery plan, not a policy or standard. |

| 9 | decision_record.md | Context-first title, actual options, listed recommendation/reasons/tradeoffs, separate sourced outcome and supersession are present in template/example. Pending is not confused with acceptance or implementation, and task-comment placement stays the default. No change needed. |
| 10 | architecture_decision_record.md | Explicitly composes DR rather than duplicating its template; adds architectural drivers, HLD/SDD links, component/operational consequences and lifecycle. The example compares the current design with a proposed queue and leaves retry/duplicate behavior open. No change needed. |
| 11 | design_decision_record.md | DR composition is explicit; component internals, contracts, failure/compatibility tradeoffs, LLD/requirement links, and supersession are distinct from ADR scope. Its atomicity example states pending outcome and planned verification accurately. No change needed. |

| 12 | policy.md | Template/example contain substantive Definitions and Principles, purpose/scope, authority, broad obligations, accountable roles, compliance, exception limits and ownership/review. Proposed status and policy/standard responsibilities are distinct. No change needed. |
| 13 | technical_standard.md | Definitions/Principles/Rules/Verification are substantive and every LOG rule maps to a check. Clarified the conditional UTC rule and made its check inspect an actual timestamp rather than vacuously passing if none is present. Removed an author aside; preserved credential prohibition and exception limits. |
| 14 | user_story.md | Actor/capability/value, acceptance criteria, scope, requirement links and unresolved decisions appear in template/example. Removed awkward repeated “need needs” wording and clarified acceptance criteria inside a small issue. A story remains optional embedded content, not a seventh task type. |

| 15 | test_plan.md | Objectives/basis, risk/scope, levels/techniques, resources/dependencies, entry/exit criteria, reporting and follow-up are present. Replaced vague completion wording with exit criteria and renamed Results to Reporting so planned recordkeeping is not confused with observed results. |
| 16 | test_specification.md | Cases include IDs, requirement links, preconditions/actions, observable outcomes, setup/cleanup and missing facilities. Defined test basis and separated basis/item metadata. Cross-file audit found REN-03/04 meant different things in story/HLD versus testing examples; aligned them while preserving N3/N4 run evidence. |
| 17 | test_status_report.md | Counts/denominators reconcile; reporting period, build, environment, ongoing status, blockers/deviations, next work and evidence are present. Expanded compressed metadata and removed the unsupported assumption that a Bug task already exists. |
| 18 | test_completion_report.md | Cycle scope, actual results/coverage, unmet exit criteria, deviations, defects/risks, recommendation versus approval, evidence and follow-up are present. Expanded metadata and made the shared example period explicit; no passing results or sign-off added. |

Cross-reference correction: the shared rename examples now consistently use REN-01 persistence, REN-02 permissions, REN-03 failed-save preservation, and REN-04 empty-name rejection. Test case N3 covers REN-04 and N4 covers REN-03; case IDs and requirement IDs need not have matching numbers. The User Story example now includes the agreed empty-name condition as well.

| 19 | tutorial.md | One learning goal, clean prerequisites, complete executable exercise, expected output, troubleshooting, completion check and takeaway are present. Applied code formatting to literal filenames/keys; kept the self-contained exercise and verified commands. |
| 20 | how_to_guide.md | Goal/prerequisites, exact actions, success checks and recovery are present. Made the existing-backup stop condition explicit and formatted literal names/values. No live-service or invented rollback claim added. |
| 21 | explanation.md | Direct answer, context, causal mechanism, benefits/tradeoffs and limits are present. Removed an author instruction from inside the completed explanation; source-link sections are optional when no project links are supplied. Acceptance versus delivery and retry uncertainty remain clear. |
| 22 | readme.md | Purpose/audience, actual stated fictional contract, prerequisites/start, expected result, tests, structure and limits are present. Formatted literal files/values and removed writer-facing “no claim” commentary from the completed README. No license/support link invented. |

| 23 | incident_report.md | Status/impact, sourced timeline/timezones, response/recovery checks, cause uncertainty, lessons and actionable follow-up are present. Corrected backlog wording that conflicted with recovery timing, limited recovery claims to available delivery evidence, and used acceptance criteria for follow-up actions. |
| 24 | agents_and_skills.md | Rechecked Agent Skills and current Claude subagent/output-style documentation. All three formats have separate templates/examples, correct role/authority boundaries and supported fields. Quoted YAML placeholders to preserve scalar types and made replacement explicit. Host activation/enforcement remains untested. |
| 25 | visuals.md | Format selection, scope/status, labels, connectors, prose equivalence, accessibility and render checks are present. Aligned the queue connector with the worker-retrieval explanation and added supported Mermaid accessible-title/description metadata, also applied to the main workflow. |

All 25 references have now been reread individually. The main routing, workflows, examples and contracts are checked again alongside the final output suite. Verification results and subsequent changes are recorded in the final validation report.

## Complete Websites Review collection

The collection follows the user's chosen initiative. PRD was created first, the implementation plan second, followed by the remaining formats. Twenty-four worked files now accompany the 25 references; Writing Style retains its accepted language examples rather than a redundant separate artifact. Guides keep their principles, structure, template, and checks, and link the complete example.

| Reference/example | Individual audit focus and disposition |
| --- | --- |
| PRD | Full problem/users, goals/measures, priorities/exclusions, journeys, constraints, dependencies/risks, acceptance and follow-up. No invented adoption baseline. |
| Implementation plan | Prerequisite, migrations M1–M6, generated contracts, exact proposed UI paths, per-step checks, requirement mapping, compatibility, rollout and attributable recovery. |
| SDD | Twelve stable WEB requirements, terminology, scenarios, permission/error/boundary rules, performance units, acceptance mapping and explicit change control. |
| HLD | Existing foundation separated from target view; responsibilities, trust/data ownership, read/write flows, deployment, recovery and decisions. |
| LLD | Read/mutation contracts, SQLSTATE errors, transaction/concurrency semantics, browser states and uncertain writes. Made normalization, queue validation and sort defaults explicit after audit. |
| ADR | Prior-context title; three architectural alternatives; requirement drivers, consequences and accepted outcome. Added decision authority. |
| DDR | Three component alternatives; atomic request versus multi-request selection; definite rejection versus response loss; explicit retry and accepted outcome. Added governing links/authority. |
| DR | Toolbar context, two real options, recommendation, tradeoff, accepted outcome/date/roles and downstream links. |
| Policy | Substantive Definitions/Principles, authority, scope, obligations, accountability, compliance, bounded exceptions and review. |
| Technical standard | Eight precise CAT rules with checks. Added T13 to deleted-row verification mapping. Kept policy authority and rules distinct. |
| Issue | Parent Feature with Description, Expected outcome, Acceptance criteria, relevant files and exclusions. Six tracker types remain unchanged. |
| User Story | Focused one-website value slice, linked acceptance and scope. Added the required unverified qualification to the parked website condition. |
| Bug Report | Complete separate required sections, prerequisites, literal reproduction controls/search, observed result, expected target, frequency/impact, evidence/files and verification. Clarified baseline sources and workaround limits. |
| Test Plan | Risk-based levels, isolated resources/data, failure facilities, sequence/responsibilities, observable entry/exit and reporting. |
| Test Specification | All nine fixture states and T01–T20. Correct 3/4/6 active populations; explicit setup locator, migration link and measurement conditions. Added fixture domain namespace for reproducibility. |
| Test Status Report | R1 candidate boundary, reconciled 15 pass/2 fail/1 blocked/2 not run, evidence, risks and next work. |
| Test Completion Report | Separate full R2 rerun of 20 passes, closed R1 defects/gaps, coverage, measurements, residual limits and recommendation distinct from release decision. |
| Incident Report | Same staging partial-progress event, evidence-backed timeline, recovery, scoped cause, lessons and verifiable follow-up. |
| Tutorial | Complete offline nine-row exercise, two commands, actual expected outputs, troubleshooting and takeaway. Commands executed in an empty temporary folder. |
| How-to | Administrator prerequisites, filtering, one/bulk category changes, clearing, outcome checks and uncertain-write recovery. No application execution performed by this audit. |
| Explanation | Explains queue state versus deletion/citation visibility and why All is not the union; assignment versus clearing and central ownership. |
| README | Documentation entry point, audience starts, navigation, runnable first command and limits. Added and executed its working-start command. |
| Agent/skill/output style | Three separate host-appropriate examples, focused triggers/authority, missing-input behavior and host-schema links. No host activation claimed. |
| Visuals | Accessible partial-write sequence with 500 confirmed/500 unresolved/1 unattempted. Repaired semicolon syntax and participant label; rendered and visually inspected. |

A separate model audited all 24 examples, then re-audited the collection after changes and checked the three final repeatability refinements. Those judgments supplement author review and static contracts; they are not independent human acceptance or actual application tests. Results and first-attempt feedback are retained in validation/final_example_audits.json.
