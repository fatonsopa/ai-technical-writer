# Evaluate the Technical Writer

Evaluate the reference instructions and the documents they produce separately. A valid package can still produce inaccurate or unhelpful writing. The [quality rubric](rubrics/quality.md) requires useful content and source support, with critical failures for invented facts, results, approval, or changed obligations.

## Cases and coverage

- `catalog.json` identifies 32 supported output kinds and their owning references.
- `coverage.json` maps output kinds to create, edit, review, and rewrite cases, and requirements to evidence.
- `cases/core.jsonl` contains 128 development cases: four operations per output kind.
- `cases/style_regressions.jsonl` retains 26 language regressions from the user's conversation and issue examples.
- `cases/acceptance.jsonl` contains separately selected acceptance requests. Once a failure informs a repair, retain that case as a regression and use a fresh case for acceptance.
- `cases/routing.jsonl` checks acronym/full-name/lifecycle routing and title-only context loading.
- `cases/observed_regressions.jsonl` retains acceptance failures used for repairs.
- `cases/calibration.jsonl` and `rubrics/calibration_labels.json` test the grader against labeled good and flawed outputs. Labels are author-assigned, not independent human judgments.
- `fixtures/` contains complete fictional or sanitized inputs. The six accepted Linear title pairs remain in the writing guide; raw exports and conversations are not distributed.
- `evals.json` records migration of the earlier 24 prompts. `cases/writing_style_legacy.json` preserves the earlier style-case provenance; the runner executes JSONL cases only.

Each executable case records its request, fixture, permitted actions, expected and prohibited properties, operation, references, and requirement IDs. Criteria are checked before generation. A narrowly scoped edit does not require a complete document template; a review returns findings. Full documents need the substance appropriate to their type.

## Run generation and grading

From the skill directory, replace `AVAILABLE_MODEL` with a model your authenticated CLI can use. Use the same pinned model and settings for baseline and revised runs.

```bash
python3 evals/run.py calibrate --model AVAILABLE_MODEL --out evals/runs/calibration
python3 evals/run.py list
python3 evals/run.py generate --model AVAILABLE_MODEL --out evals/runs/revised
python3 evals/run.py grade --model AVAILABLE_MODEL --generated evals/runs/revised --out evals/runs/revised-grades
```

Use `--kind sdd`, `--operation rewrite`, or `--split acceptance` to select cases. Defaults select development cases. `--jobs` controls simultaneous sessions. Use a new output directory for each attempt; the runner refuses to overwrite existing records. To compare a preserved baseline, generate with `--skill /path/to/baseline --variant baseline`; when grading, also pass `--generator-skill /path/to/baseline`. The common target guides remain the same, while actual baseline resource availability is supplied separately.

The runner copies runtime guidance and source fixtures into temporary workspaces. Requests exclude expected properties and rubrics. Generation is read-only and prohibits network access, tracker changes, and execution of the target project. One fresh context handles each selected output kind; its operations share that context. This is not one independent session per case. Read-only local checks can support validation claims, but cannot establish product outcomes.

Grading uses a separate context with the raw sources, common target guides, rubric, output, actual available resources, and tool-action evidence. Source paths are mapped explicitly. Seven dimensions receive 0–3 scores; each must reach 2, with no critical failure. A title check rejects the known SDD/Software Design Document confusion. Governance section checks also enforce the user's named-section convention. Inspect scores and failure reasons in `record.json`: a completed grading call can contain failed documents. The process exit code reports infrastructure completion, not quality acceptance.

## Review results

The `calibrate` command grades the committed author-written controls and checks agreement with their labels; it does not generate substitute controls. Calibrate the grader before trusting its scores. Inspect every flagged failure against source facts and tool evidence; a plausible judgment can be wrong. Keep the first attempt, any repair, and the retest. Do not weaken criteria or select only favorable trials. Define repetitions for high-risk behavior before seeing their results.

Run affected development cases after a change, relevant shared language/preservation regressions, and the supported-output suite for a substantial release. Compare baseline and revision on identical selected requests. Report sample counts and each operation, rather than calling a few examples universal coverage.

Run artifacts contain the selected model, settings, runtime Markdown hash, case IDs, outputs, grades, usage, reference traces, and errors. Keep raw CLI logs under ignored `runs/` or another private folder; publish sanitized outputs, scores, provenance hashes, and limitations. Usage counts describe host token accounting; file-size token estimates describe context size. They are different measurements.

A model score is evidence for the sampled requests, not proof of future reliability. Human acceptance and actual host integration need separate checks. See the repository's [validation report](../../analysis/VALIDATION.md) for observed results and limitations.

## Sources

The design follows [OpenAI evaluation guidance](https://developers.openai.com/api/docs/guides/evaluation-best-practices): define the objective and metrics, use representative data, inspect traces, and calibrate automated judgments. Our local case counts, seven-dimension threshold, and critical-failure gates are package choices. Independent human calibration remains a separate requirement when reviewers are available.
