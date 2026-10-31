# Evaluate Technical Writer

Test the documents the skill produces, separately from the tools and reference files. A valid package is not proof of useful writing. Cases must assess source facts, obligations, document structure, scope, traceability, and language.

## What is tested

- `catalog.json` declares 32 output kinds. `coverage.json` maps their create, edit, review, and rewrite cases.
- The suite currently contains 188 case definitions: 167 development, 11 acceptance, and 10 calibration cases. Definitions are not executed results.
- `contracts/documents.json` owns executable output structures. The same checks are used by normal document delivery and by grading; a favorable model score cannot waive a missing required section or subheading.
- `rubrics/quality.md` defines seven 0–3 dimensions. Every dimension must reach 2, with no critical failure. Invalid scores, including 99 or boolean values, are evaluator errors.
- Existing authored examples are teaching artifacts. Their separate review is not fresh document generation or application testing.

Keep protected acceptance cases out of tuning. If a failure guides a repair, retain it as a regression and select a fresh acceptance case. Report author-assigned calibration labels as such; they are not independent human judgments.

## Native-host evaluation

The default workflow uses the model in the current host, including ChatGPT, Claude, Codex, or Claude Code. Code manages frozen inputs, packet identity, structural checks, limits, and acceptance. The host writes and judges only the portions that need AI. An unavailable exact model ID stays unknown.

From the skill folder, prepare one case before selecting a larger batch:

```sh
.venv/bin/python evals/run.py prepare --session ../writer-eval-prd --kind prd --operation create --max-handoffs 2 --max-seconds 600 --host unknown
.venv/bin/python evals/run.py packet --session ../writer-eval-prd --case prd-create --phase generate
```

Use a new session folder outside the skill. `--max-handoffs` bounds issued native phase packets; it does not count hidden provider calls or establish a billing cap. `--max-seconds` bounds the session runtime. Record the actual host; supply `--model` only when its exact identity is exposed.

The generation packet contains the task and raw source, without the grading rubric and expected properties. The model should read the skill's applicable guides, return the requested document, and leave unrelated files and services alone. Use a separate context for protected evaluation where available; packets and filesystem copies do not establish a security sandbox or independent judging by themselves.

Save a generation response using the IDs and hash from the packet:

```json
{
  "case_id": "prd-create",
  "phase": "generate",
  "packet_sha256": "HASH_FROM_PACKET",
  "data": {
    "content": "THE_COMPLETE_DOCUMENT",
    "references_read": ["references/product_requirements_document.md"]
  }
}
```

```sh
.venv/bin/python evals/run.py submit --session ../writer-eval-prd --response GENERATION_RESPONSE.json
.venv/bin/python evals/run.py packet --session ../writer-eval-prd --case prd-create --phase grade
```

A malformed or structurally invalid task output is a failed attempt. A structurally valid output remains pending until its source-grounded judgment is submitted. The grade packet supplies captured source facts, guides, rubric, and expected properties. It never treats a document's presence or headings alone as useful content.

```json
{
  "case_id": "prd-create",
  "phase": "grade",
  "packet_sha256": "HASH_FROM_GRADE_PACKET",
  "data": {
    "id": "prd-create",
    "scores": [2, 2, 2, 2, 2, 2, 2],
    "critical_failures": [],
    "reasons": ["REPLACE_WITH_SOURCE_SUPPORTED_FINDINGS"],
    "reviewer": {
      "kind": "current_host_self_review",
      "identity": "ACTUAL_REVIEWER",
      "model": null,
      "method": "DESCRIBE_THE_ACTUAL_REVIEW"
    }
  }
}
```

The scores above illustrate the format; they are not default answers. Score grounding, preservation, completeness, usefulness, language, scope, and traceability in that order. Identify self-review honestly. Fabricated evidence, execution, approval, inspected paths, or material requirement changes are critical failures.

```sh
.venv/bin/python evals/run.py submit --session ../writer-eval-prd --response GRADE_RESPONSE.json
.venv/bin/python evals/run.py assess --session ../writer-eval-prd
```

`assess` returns exit status 0 only when acceptance passes, and 1 when the target or coverage is unmet. Invalid requests or changed captured inputs return an error. Earlier attempts remain recorded; correcting a grader or requirement creates a separately versioned run.

## Add your own input and expected properties

Keep private test data in a separate working folder. Save these two files there:

| File | Contents |
| --- | --- |
| `brief.md` | The original facts or draft supplied to the writer |
| `cases.jsonl` | One JSON object per task: request, input path, output type, and acceptance properties |

For example, `brief.md` could state that an import preserves identifier `0042`, expires at 15 minutes, and has no agreed owner or row limit. A case might be:

```json
{"id":"import-prd","kind":"prd","operation":"create","split":"development","fixture":"brief.md","request":"Write the complete PRD using only these facts.","references":["references/product_requirements_document.md"],"context":{"required_literals":["0042","15 minutes"]},"expected_properties":["Use the PRD structure; preserve supplied facts and explicitly retain unagreed owner and row limit."],"prohibited":["Invented approval, measurements, owners or limits."]}
```

Fixture paths are relative to `cases.jsonl`. The `context` can declare exact material literals or requirement IDs for code to check. Expected properties are the acceptance rules, not text to copy into the generated document. Ordinary prose can have several correct outputs; require exact whole-output equality only when literal identity is part of the real task.

```sh
.venv/bin/python evals/run.py prepare --cases WORK/cases.jsonl --session WORK/evaluation --max-handoffs 2 --max-seconds 600 --host unknown
```

Add representative positive cases, missing/invalid input, important exceptions, and realistic variations. Check that an omitted section, incorrect hierarchy, altered source value, unsupported claim, or out-of-scope rewrite is actually rejected. Keep tests of the checker separate from observations of a model using the skill.

## Results and improvement

Task success is accepted attempts divided by evaluated attempts. Coverage is evaluated attempts divided by planned attempts. Show counts with the percentages. With no evaluated attempts, success is unmeasured. Structural or malformed task outputs count as failures; pending reviews leave incomplete coverage. Critical failures block acceptance regardless of the average. These measurements describe selected tasks and versions, not universal accuracy.

The session captures runtime scripts/resources, source fixtures, selected cases, guides, rubric, and output contracts. Changed code, facts, criteria, or output cannot silently inherit a prior result. Repeated grading or replay of an old answer is not a new model-performance observation.

After a failure, retain the input, output, artifact version, checker result, review, and diagnosis. Decide whether the cause is the skill, missing context, environment, changed requirement, or evaluator. Make a focused repair and rerun the unchanged criteria against a newly captured artifact. Do not weaken a rule merely to pass.

When an allowance is exhausted below target, inspect results and recommend a bounded continuation. Record the actual user authorization before extending:

```sh
.venv/bin/python evals/run.py extend --session WORK/evaluation --handoffs 2 --seconds 300 --authorization-note "ACTUAL_USER_AUTHORIZATION"
```

A budget extension does not change the task, scoring, or earlier attempts. An already-met target needs no extension.

## Optional Codex CLI adapter

Native-host evaluation needs no other provider's CLI. For automated Codex sessions, an authenticated Codex CLI and an exact available model are required. Preview the selection first:

```sh
.venv/bin/python evals/run.py plan --kind prd --operation create
.venv/bin/python evals/run.py generate --kind prd --operation create --model AVAILABLE_MODEL --max-calls 1 --max-seconds 120 --out WORK/generated
.venv/bin/python evals/run.py grade --kind prd --operation create --model AVAILABLE_MODEL --max-calls 1 --max-seconds 120 --generated WORK/generated --out WORK/grades
.venv/bin/python evals/run.py summary --generated WORK/generated --grades WORK/grades
```

Each external batch requires explicit total invocation and runtime allowances, shared across parallel jobs. Without filters, the current default development selection has 46 generation contexts and 46 grading contexts; calibration adds one, for 93 planned invocations. It is not a recommended first batch.

The adapter preserves the generator's full artifact identity and a frozen input record. Grading uses that captured record and rejects unexplained drift. Baseline comparison can use `--skill BASELINE` during generation and `--generator-skill BASELINE` during grading against the same frozen target criteria. Records without captured inputs remain historical evidence; they cannot become new acceptance results by silently supplying today's fixtures.

External `grade` reports infrastructure completion separately from each document's `passed` field. Use `summary` for the captured Codex results or native `assess` for a native session. Both return a distinct acceptance result and require complete, matching-version coverage. Do not treat CLI process completion as a quality pass or manually combine favorable results from different versions.

## Audit authored examples

Prepare read-only review packets for the current host:

```sh
.venv/bin/python evals/audit_examples.py --out WORK/example-audit
```

Review each packet, then submit its `packet_sha256`, honest reviewer metadata, and results in a response file:

```sh
.venv/bin/python evals/audit_examples.py --packet WORK/example-audit/batch-00/packet.json --response WORK/example-review.json --out WORK/example-assessment.json
```

Use `--document FILENAME` to select examples. A separate Codex route is available with `--provider codex --model AVAILABLE_MODEL --max-calls N --max-seconds N`. Both routes share score validation and applicable structure checks. Authored examples are reviewed as a teaching collection, not reported as independently generated outputs or proof of application testing.

## Evaluation basis

The [quality rubric](rubrics/quality.md) and the [output contracts](../contracts/documents.json) define the local acceptance rules. [OpenAI's evaluation guidance](https://developers.openai.com/api/docs/guides/evaluation-best-practices) supports representative cases, source-grounded criteria, trace inspection, and calibrated judgments. This package's case counts, score thresholds, and required document headings are project choices. Independent human review and actual host behavior remain separate evidence.
