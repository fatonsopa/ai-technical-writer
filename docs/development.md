# Develop and check the skill

Preview the checks affected by the current changes, then execute that selection:

```sh
.venv/bin/python scripts/run_tests.py
.venv/bin/python scripts/run_tests.py --execute
```

The runner compares the last successfully tested checkpoint or Git HEAD and explains each selection. In a folder without Git or a checkpoint, supply exact `--changed PATH` arguments. New or unmapped paths require an impact rule; they do not trigger the full suite. Changed test files select changed methods, and overlapping selections run once.

Full testing follows the author's verification that every planned implementation change is delivered and no implementation work remains, with a completion record bound to the current artifact. User batch approval is not required. See [repository testing](../workflows/improve_references.md#scope-repository-tests). A test authorization does not authorize a GitHub push.

Test actual output contracts and invalid-output controls as well as package integrity. Installation uses the same public repository files, including its tests. Private records, run snapshots and local environments stay outside the installed copy.

For Mermaid source diagnostics, install the parser dependencies outside the repository. Match the target version; the examples use 11.16.0:

```sh
npm install --prefix ../writer-diagram-tools --no-audit --no-fund mermaid@11.16.0 jsdom@26.1.0
export TECHNICAL_WRITER_MERMAID_MODULE_ROOT="$(cd ../writer-diagram-tools && pwd)"
.venv/bin/python scripts/visual_contracts.py WORK/source_draft.md --require-syntax
```

Use a Markdown source draft containing the Mermaid block for that diagnostic command. A parser pass establishes syntax only. Final diagrams require the rendered export with visible context; unrendered outputs remain drafts. Syntax, rendering and semantic review are separate results. The checker installs nothing.

Final diagrams use the shared SVG renderer. It preserves each notation and adds visible title/subtitle and a symbol legend. All supported diagram exports use the light dotted canvas. Install Mermaid CLI in the same external tool folder:

```sh
npm install --prefix ../writer-diagram-tools --no-audit --no-fund @mermaid-js/mermaid-cli@11.16.0
export TECHNICAL_WRITER_MERMAID_CLI="$TECHNICAL_WRITER_MERMAID_MODULE_ROOT/node_modules/.bin/mmdc"
.venv/bin/python scripts/render_diagram.py WORK/flow.mmd --out WORK/flow.svg
```

Use `--check` with the same arguments to check an existing export without rendering it again. If a browser configuration is needed, set `TECHNICAL_WRITER_PUPPETEER_CONFIG` to its JSON path. The [shared style](../config/diagram_style.json) owns colors, contrast thresholds and dotted canvas. Every exported diagram includes its title/subtitle and legend. Its Mermaid code appears in a `text` code block below the explanation table, so readers can copy and edit it. See [diagram rendering](../workflows/diagram_rendering.md). For accepted delivery, use `diagram_svg` (or `flowchart_svg`) in `context.visuals` and capture the SVG and same-named `.mmd` as sources before `prepare`; assets live beside the destination document. Changes invalidate their frozen review.


For diagram checks, run `.venv/bin/python scripts/check_diagram_collection.py`. The [diagram evaluation guide](../evals/README.md#test-diagram-delivery) explains the real user-flow and sequence tasks, acceptance criteria, mechanical controls and evidence to retain.

## Repository layout

`SKILL.md` coordinates writing. `references/` owns document and language guidance; `examples/` demonstrates it. `contracts/` owns output structures. `scripts/` handles validation, accepted delivery and installation. `evals/` owns behavioral cases and assessment; its `adapters/` folder contains optional provider transport. `config/` records layout and component ownership. These components share contracts and preserve the distinction between mechanical checks and source-grounded judgment.
