# Substantial rewrite: protect meaning and requirements

Use this process when the user requests a major restructure, consolidation, simplification, or replacement of an existing document. A spelling change, small edit, or review does not require this workflow.

## 1. Audit the original

Read the complete original and linked documents needed to understand it. Record the audience, purpose, current sections, binding rules, factual claims, numbers, commands, file paths, decisions, source citations, examples, open questions, and references from other files. Identify required section names, field boundaries, and established document terminology as well as generated blocks and parser-dependent headings. Search for other files that link to the document when a repository is available.

Identify contradictions, obsolete material, duplicated content, and project-specific rules that belong elsewhere. Classify disputed facts as questions; do not silently resolve them by writing confidently.

## 2. Select the target structure

Load the destination document-type reference. Propose a structure suited to the reader and the content, mapping important existing sections and requirements to the new structure. Note content that will move, consolidate, be corrected, or be deleted. Check actual dependencies before moving files or changing section anchors.

**Approval:** For changes to binding standards, contracts, or other documents where restructuring could change obligations, present the proposed substantive changes and seek approval before applying them, unless the user has explicitly authorized the full restructure. For routine documentation, proceed when the request is clear. Never allow an unanswered question to become an invented decision.

## 3. Rewrite without losing information

Use the document reference for structure and `references/writing_style.md` for prose. Preserve required section boundaries and agreed terminology while shortening the content within them. Consolidate repetition, but keep each unique requirement, boundary, exception, measured claim, warning, and relevant example. Keep quotations and generated blocks byte-for-byte when their exact wording or bytes matter; otherwise preserve their substance and source. Use links when another maintained document is the source of truth.

Do not replace an accurate requirement with a shorter statement that changes its conditions. If the rewrite corrects an error, document the correction separately from the style changes.

## 4. Check preservation

For substantial rewrites, use `scripts/zero_loss.py` to build and review an inventory and a mapping between original and rewritten content. Typical commands:

```bash
python3 scripts/zero_loss.py inventory --all original.md
python3 scripts/zero_loss.py suggest --all --old original.md --new rewritten.md --out rewrite-map.json
python3 scripts/zero_loss.py check --all --old original.md --new rewritten.md --map rewrite-map.json
```

Read `python3 scripts/zero_loss.py --help` for the actual accepted flags before running them; remove unsupported flags and provide related files with `--also` when needed. The script checks coverage but cannot decide whether a rewrite retained the full meaning. Review every suggested mapping and every deliberate deletion manually. Check changed file paths, links, headings consumed by scripts, and exact literals. Run available project tests that cover generated sections or documentation parsing.

Describe each check at the scope it actually covered. Reading an inventory establishes that the source was inventoried; it does not establish that the rewrite preserves every meaning. Listing workspace files does not establish that none link to the document. Claim that links were searched only after searching their contents, and limit the claim to the files available. If a check was not run, say so.

If a dropped rule or changed decision lacks approval, stop and ask about that change. If verification cannot be run, state that limitation.

## 5. Deliver an accountable result

Provide the revised document plus a short summary of meaningful changes, preserved requirements, deliberate removals and reasons, corrected inaccuracies, validation performed, and unresolved questions. Keep this audit separate from the reader-facing document unless the document type explicitly calls for it.

## Validate the actual output

Use the selected type's contract for a full document. For a narrow edit or review, declare `scope: title` or `scope: excerpt` as appropriate. Keep sessions and drafts outside the writing skill. In the request JSON, supply:

```json
{
  "kind": "prd",
  "operation": "create",
  "scope": "complete",
  "sources": [{"id": "brief", "path": "brief.md"}],
  "destination": "accepted-prd.md",
  "context": {"required_literals": ["0042"]},
  "requirements": [{"id": "KEEP-ID", "text": "Preserve the supplied identifier 0042."}],
  "limits": {"max_attempts": 3, "max_seconds": 600}
}
```

Paths in this request are relative to the request file. Use real source requirements and literals; the values above illustrate the format. Inline source text can replace a source path. An edit of an existing excerpt also needs `context.edit_region: [START_LINE, END_LINE]` with its inclusive original line bounds. A title-only file edit may change only its H1; a review must not overwrite its source.

Run the installed Python environment from the skill folder. Replace `WORK` with a separate task folder containing the request, source and draft:

```sh
.venv/bin/python scripts/validate_document.py prepare --request WORK/request.json --session WORK/session
.venv/bin/python scripts/validate_document.py check --session WORK/session --draft WORK/draft.md
.venv/bin/python scripts/validate_document.py packet --session WORK/session --draft WORK/draft.md
```

Read the returned packet and review the actual draft against its frozen sources, guide, contract and each explicit requirement. Return `objective_sha256`, `output_sha256`, an honest `reviewer` object (`kind`, `identity`, `model`, `method`), seven 0–3 `scores` (grounding, preservation, completeness, usefulness, language, scope, traceability), `critical_failures` and `reasons` arrays, and one `requirements` judgment per ID with `accepted`, `rationale` and `source_ids`. Use `model: null` when the exact model is unavailable. Self-review must be identified as such.

```sh
.venv/bin/python scripts/validate_document.py review --session WORK/session --review WORK/review.json
.venv/bin/python scripts/validate_document.py finalize --session WORK/session --draft WORK/draft.md --review ACCEPTED_REVIEW_PATH
```

The review command returns the accepted review path. Finalization rechecks the actual bytes, requirements, destination baseline and source/guide versions. It refuses missing structure, stale judgments or newer user edits. A receipt describes this output and reviewer, not universal accuracy. If the allowance is exhausted below target, explain the failures and ask the user before `extend --session WORK/session --attempts N --seconds N --authorization-note "ACTUAL USER INSTRUCTION"`. Preserve earlier attempts and the frozen criteria.
