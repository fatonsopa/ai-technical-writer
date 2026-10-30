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

From the skill directory, run:

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/plain_words.test.py
python3 scripts/zero_loss.test.py
python3 scripts/check_examples.py
```

Check relative links, routing, retired paths, and consistency between shared and specialized guidance. Review each warning; a size budget prompts a content review rather than automatic deletion. Record bytes, words, and the method used to estimate tokens before and after revision. Measure the references actually read for representative requests as well as the total package.

Use the cases, fixtures, rubric, and coverage map described in [Evaluation instructions](../evals/README.md). Evaluate language, document structure, missing information, requirement traceability, and all supported operations. Keep expected properties and rubrics out of the generator's workspace. Calibrate grading with labeled good and flawed samples, including claims about tools and unavailable evidence. Record whether labels come from the author or independent reviewers.

After each substantive reference change, run its affected development cases and relevant shared regressions. Compare important cases with the preserved baseline using the same model and inputs. Use protected acceptance cases after the guidance is stable; if a failure informs a repair, retain it as a regression and add a fresh acceptance case. Record every attempt, including failures and infrastructure errors. A model grader's explanation must be checked against the source and actual tool evidence before it drives a revision.

Use the available independent evaluator only within the authorized scope. Keep raw tool logs and transient workspaces isolated from distributable results. Record model/settings, source and skill hashes, actual outputs, grades, and checks performed. Do not substitute author-written examples for claimed model runs.

A static check can enforce structure and literal preservation; it cannot prove clarity, semantic equivalence, or future model reliability. Record which kind of check produced each result. Do not confuse an example's hypothetical scenario with a verified project fact.

## Finish

Report requirement coverage, changed references, important removed or relocated content, checks performed, observed failures and repairs, and remaining limitations. Update the specification and cases when the user changes the intended behavior. Keep maintenance evidence and reusable lessons outside normal writing context. Distinguish design choices from improvements supported by observed results, and recheck vendor documentation before reusing platform-specific advice in a later skill.
