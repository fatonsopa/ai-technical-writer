# Reference review ledger

Checked on 2026-10-30 against TW-001–TW-034. Input drafts are preserved in commit 3a65c56 and the baseline manifest. Sources in the references identify relevant practices; adopted conventions are not universal mandates.

| Reference | Audit finding and proposed correction |
| --- | --- |
| SKILL.md | Stale/missing routes and excessive title-only loading. Add the complete compact catalog, lifecycle/relationship map, selective routing, and authority boundaries. |
| writing_style | Accepted tone and six Linear pairs are useful. Preserve them; repair paths and clarify intended versus observed behavior without adding workflow overhead. |
| issue | Decision structure duplicates specialized content. Own only common six-type task content and route specialized writing. |
| user_story | Missing owner. Add optional user/need/value format, acceptance criteria, full embedded example, and no seventh task type. |
| spec_driven_development | Incomplete acceptance mapping and duplicate requirements ownership. Consolidate individual entries and map every binding constraint to verification. |
| product_requirements_document | Missing. Define users, intent, scope, and outcomes without invented metrics or implementation design. |
| high_level_document | Missing specification/lifecycle links. Keep living verified/proposed architecture, flows, operations, and ADR links. |
| low_level_design | Missing. Cover component contracts/state/data/failure behavior with requirement/HLD/DDR links. |
| decision_record | ADR-only template presents proposed choices as decided. Rebuild around context title, actual options, recommendation, and separately confirmed outcome. |
| architecture_decision_record | Missing specialized overlay. Compose shared decisions with architectural drivers and HLD links. |
| design_decision_record | Missing. Compose shared decisions with component constraints and LLD links. |
| implementation_plan | Incomplete governing-source and test mapping. Add verified context, dependencies, acceptance coverage, rollout/recovery, and explicit unknowns. |
| policy | Missing and conflated with standard. Add direction/accountability with substantive Definitions and Principles. |
| technical_standard | Template/example omit Definitions/Principles and call a standard a policy. Add precise rules/checks and explicit authority/exception handling. |
| test_plan | Missing. Define testing approach and completion criteria, distinct from the build plan. |
| test_specification | Missing. Define coverage/cases/procedures and expected results without extra default files. |
| test_status_report | Missing. Describe ongoing period/build results, blockers, risks, and next work. |
| test_completion_report | Missing. Assess milestone evidence, coverage, deviations, defects, and residual risk without inventing approval. |
| tutorial | Useful but unverified exercise. Keep a complete executable Python lesson with visible success. |
| how_to_guide | Example assumes unverified Node behavior. Replace with a reproducible procedure and failure/recovery branches. |
| explanation | Preserve causal explanation and add explicit source/status boundaries and meaningful limits. |
| readme | Example is mostly conditional commands. Provide a complete stated fictional repository contract and check its commands. |
| incident_report | Example lacks substantive lessons and sourced rows. Add factual timeline/response/unknowns and owned verifiable follow-ups. |
| agents_and_skills | Vendor formats need clearer boundaries and complete templates/examples. Check current minimum schemas and preserve scoped authority. |
| visuals | Preserve conditional use/accessibility; verify consistency with requirements/prose and readable rendering. |

Primary research: Google tone; Linear/Mozilla tasks/bugs; EARS/Spec Kit requirements; arc42/C4 architecture; AWS decisions; Stanford governance; ISO 29119-3/ISTQB testing; Diátaxis learning/task/explanation; Google SRE postmortems; GitHub READMEs; Agent Skills and vendor instruction formats. The six task types, full-name filenames, SDD label, and governance headings are user-approved conventions.

## Observed validation

Baseline title-only probe completed in a fresh Codex CLI context, but loaded the bug-report reference unnecessarily. Proposed fixtures and author review do not count as completed behavioral evaluations. Append case results, repairs, and limitations as the work proceeds.

Language review during execution: the user reiterated that the shared writing guide applies to the reference prose itself. Replaced compressed instructions such as “compose the shared context/options/recommendation/outcome template” with connected explanations of what to write. This is an editorial correction, not a completed behavioral test.

Grader protocol repair: initial grading omitted actual tool actions and confused target guides with baseline resources. An HLD rewrite really ran the preservation inventory, while a baseline policy really lacked a policy guide. Added generator resource availability, tool-action records, and the fixture/source path mapping. Source-backed validation claims are assessed against their actual evidence; broad claims still need appropriate checks. Initial grades are retained locally and superseded, not counted as final results. Explicit governance section requirements also receive deterministic output checks.

## Failures and repairs

- HLD rewrite: the initial output claimed no incoming links existed, although the trace only listed files. The inventory claim was supported, but the backlink claim was not. Tightened the rewrite workflow to state the scope of performed checks. The targeted retest searched available file contents and passed all seven dimensions. Initial output and grade are retained in the result artifacts.
- First protected bug-review case: the output preserved facts and uncertainty, but returned a full replacement report. Strengthened the main operation guidance and bug quality check to require findings and focused suggestions for reviews. Moved that acceptance case to observed regressions, retained its initial failure, and selected a fresh incident-review acceptance case. Retests and remaining results are recorded in the validation report.

- Grader resource inventory initially listed Markdown only, so a TS rewrite's accurate description of the mapping command was called unsupported. Included script files and distinguished a documented command from a claim of execution. The unchanged TS output passed regrading. Added a tenth calibration sample for this distinction; all ten author-assigned pass/fail labels matched.
- Baseline SDD output was titled “software design document.” Its behavioral content received passing model scores, but that title contradicts the user's explicit SDD convention. Added a variant-independent title check for this known acronym confusion. This deterministic contract check is reported separately from the original model scores.

- Final naming audit: the issue links used the correct path but retained visible “Work items” labels and a Work Item catalog heading. Renamed the guide heading and active link labels to Issue, kept the accepted term only as an alias, and checked all active titles and paths. Added negative tests for a stale issue label and mismatched guide heading. Historical filenames remain only in migration/history records and deliberate negative tests.

## Bug structure correction from the user's review

The user found that the refactor merged expected and actual results, used an alternative reproduction heading, and omitted a dedicated Relevant files section. The original shared conversation's first answer and the preserved first bug guide were reread on 2026-10-31. The current Desktop file contains only the later taxonomy discussion, so the original shared page supplied the earlier structure. Historical proposals were reconciled with the user's current exact heading requirement.

The previous content-oriented evaluations accepted merged fields and therefore missed a required structure. Restored Description, Environment, Prerequisites when applicable, How to reproduce, separate Expected result and Actual result, Reproduction frequency, Severity and impact, Evidence, Relevant files, and Verification; Additional context remains optional. Both template and completed example use the structure. Added deterministic section gates and negative tests for merged results, missing Relevant files, and the reproduction heading. Added an attributed-file fixture as well as the repository-unavailable cases. Do not treat the earlier passing scores as evidence that these structural requirements were already satisfied.

## Connected examples and new observed failures

The user selected Websites Review and asked for finished examples without source/addition labels. Created the PRD first and plan second, then the other complete formats. References now load their matching external example for full writing while keeping narrow operations focused. Internal provenance is in validation/example_source_manifest.json.

Independent model audit found useful refinements: qualify the story with unverified status, include T13 in deleted-row verification, make LLD normalization/defaults explicit, improve bug reproduction and source context, add decision authorities/links, identify TS setup/M1, and report the actual offline tutorial check. These refinements were applied and the collection re-audited. Rendering found semicolon-sensitive Mermaid sequence syntax; the corrected diagram was rendered and visually inspected.

The new full regression run exposed two additional failures. issue_decision-edit retained an obsolete Feature-comment drafting direction despite the current Decision destination. The Issue guide now explains how to resolve stale author directions during a narrow edit. standard-rewrite left every verification method unspecified, so it did not produce a usable standard. The standard guide now permits clearly proposed checks derived from existing rules while preserving unknown tools, approval and execution. Retain the failed outputs and all targeted retests; do not replace the first scores with repaired ones.

### Grader correction for explicit review output format

The full run initially marked three language samples failed because they returned prose instead of findings. Direct inspection showed that all three requests explicitly said “Return the requested prose or title,” and the predefined properties/permitted actions also requested that form. The outputs preserved the valid passive sentence, valid heading and ordered instructions. This was a grader error, not a writing failure. Correct the grader to honor explicit requested response form before generic operation defaults, keep the first grades, regrade the saved 26 outputs, and recalibrate against all controls. No source or expected property was relaxed.

An initial local patch command failed before changing the grader; its following regrade/calibration commands had already started using the old prompt. Preserve those attempts and use new result directories after applying the actual correction.

The duplicate regrade that started before the patch also accepted all 26 saved style outputs. This exposes grader variance as well as the original instruction-precedence error; the later pass is not evidence that prompt wording alone caused a score improvement. The corrected grader explicitly matches the already defined request format, and all labeled controls were checked again. Original and duplicate attempts remain in the run registry.
