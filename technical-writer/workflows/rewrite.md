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
