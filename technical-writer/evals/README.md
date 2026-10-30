# Evaluating this skill

`evals.json` contains prompts and expected properties for comparing the previous and revised skill. The cases are proposed tests. A JSON file alone cannot prove how an AI agent behaves.

For a meaningful comparison, run the same cases with each skill in separate, clean sessions using the same model, source files, and project instructions. Inspect the produced document and any tool calls. Record which references were read, how many tokens were consumed, whether required facts were preserved, and whether the human reviewer would accept the result without rewriting it.

A document should fail its evaluation if it invents source files, data, evidence, decisions, or test outcomes, even when its formatting is correct. For rewrites, compare obligations and use `scripts/zero_loss.py` as an aid to manual review. For style, evaluate meaning, natural wording, completeness, and unnecessary repetition. Human review remains necessary because a word scanner cannot tell whether a sentence is useful.

The static test script in `scripts/validate_skill.py` verifies packaging and structural requirements. It does not run these behavioral evaluations or simulate Claude Code.
