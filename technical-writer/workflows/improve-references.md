# Improve the reference library

Use this workflow when the user asks to audit or improve this skill's references. Normal document writing uses the main skill and the relevant document reference.

## Establish the specification

Read the user's current requirements and supplied history. Record the intended behavior, scope, acceptance checks, and source versions before changing the library. Recheck source files that the user updates during the work. Current instructions take precedence over old proposals.

Map each reference to the document it teaches. Decide which file owns shared writing guidance, issue content, bug additions, governance rules, and rewrite safeguards. Keep project workflow rules in the project.

## Work on one reference at a time

1. Research the document type using primary sources. Identify its reader, purpose, common practices, and genuinely binding constraints. Record source links and the date checked.
2. Audit the complete reference, its template, and its completed example. Compare them with the specification and research. Identify missing content, contradictions, duplicate responsibilities, factual gaps, and unclear language. Inspect callers before changing paths, markers, or sections.
3. Research the specific questions exposed by the audit. Distinguish an external requirement from an organizational convention and an editorial choice. Do not keep searching merely to repeat what is already established.
4. Propose the change in a review ledger: the target structure, important content to preserve, additions, removals, and reasons. Resolve choices within the user's authorized scope. Ask only for a material decision that cannot be inferred or left explicitly open.
5. Revise the reference. Keep its purpose, principles, structure, adaptable template, useful completed example, and quality checks. Apply the writing guide to all of them. Give governance templates real Definitions and Principles sections, not just instructions mentioning those words.
6. Validate the revised file, then use it for a realistic writing request. Check the resulting document's meaning, structure, sources, and preservation. Record actual findings and revise the instruction responsible for each failure.

Repeat steps 3–6 while a concrete failure remains. After three unsuccessful attempts on the same unresolved problem, document what prevents verification and continue unaffected work. Do not invent evidence, weaken criteria, or claim completion for the affected requirement.

## Validate the whole skill

Run `python3 scripts/validate_skill.py`, the validator's tests, and the existing wording and preservation regression suites from the skill directory. Test executable examples in isolated temporary folders. Check relative links, routing, deleted references, and consistency between shared and specialized guidance.

Use realistic source fixtures to evaluate language, document structure, missing information, requirement traceability, and changes of operation. For substantial changes, use an independent evaluator when delegation is authorized and available; provide the skill, the request, and raw inputs without the expected answer. Keep generated evaluation artifacts isolated. Evaluate any failures against the source before changing the reference.

A static check can enforce structure and literal preservation; it cannot prove clarity, semantic equivalence, or future model reliability. Record which kind of check produced each result. Do not confuse an example's hypothetical scenario with a verified project fact.

## Finish

Report the requirement coverage, changed references, important removed or relocated content, checks performed, observed failures and repairs, and remaining limitations. Keep the reusable instructions free of the maintenance log. Update the specification and acceptance cases when the user changes the intended behavior.
