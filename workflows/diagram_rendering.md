# Make each diagram self-contained

Use this procedure for diagrams selected by [Visual Guidance (VG)](../references/visuals.md). Every final diagram carries its type, title, subtitle and symbol legend inside the exported image. A screenshot must give readers enough context to understand its subject and distinguish its elements.

## Define the visible context

Keep the editable source beside its SVG. `accTitle` supplies the accessible and visible title; `%% Subtitle:` explains the scope, purpose or status. `accDescr` supplies the accessible description. Use [Writing Style (WS)](../references/writing_style.md) for all of them, including node and legend labels. Name the subject and describe what happens in natural sentences. Preserve uncertainty and distinguish proposals from deployed behavior.

```text
%% Diagram: Sequence diagram
%% Subtitle: The administrator sends a category change from the Websites page.
sequenceDiagram
    accTitle: Submit a website category change
    accDescr: The administrator submits the category through the Websites page.
    actor A as 1. Administrator
    participant UI as 2. Websites page
    A->>UI: 3. Save category
```

The renderer places the title and subtitle above the diagram and a section headed **Legend** below it, all inside the SVG. Each entry pairs a symbol with its meaning: a diamond with “Decision,” for example. Include the shapes and line styles used in that view. Colors, shapes and labels must agree with the diagram body. Reserve References for source links.

Use established terms for the selected notation. Flowcharts use Process, Decision, Document, Data and other applicable symbols; follow [Flowchart design](flowcharts.md) for their shapes, palette and dotted canvas. [Sequence diagrams](https://mermaid.js.org/syntax/sequenceDiagram.html) use actors, participants and messages. [State diagrams](https://mermaid.js.org/syntax/stateDiagram.html) use states and transitions. Choose `%% Diagram:` from the renderer's supported types; it must match the source notation. The renderer defaults to that notation's name when the comment is omitted.

Legends derive from flowchart classes or the sequence/state constructs present in the source. Use `%% Legend: flow_arrow | Relationship` to clarify a structural arrow. Supported types and glyphs live in `scripts/diagram_presentation.py`. A scenario-specific meaning needs an explicit explanation: the crossed response arrow in the recovery example means the response was lost, rather than claiming that all crossed arrows have that meaning. Extend and test a missing glyph, or use another suitable exporter with the same visible-context requirement.

## Render and check

Use Mermaid CLI from the [documented environment](../README.md#development). The renderer installs nothing. Set `TECHNICAL_WRITER_MERMAID_CLI` to its executable if absent from PATH set `TECHNICAL_WRITER_MERMAID_MODULE_ROOT` to the environment containing Mermaid, jsdom and Puppeteer, and optionally `TECHNICAL_WRITER_PUPPETEER_CONFIG` to the browser configuration.

```sh
python3 scripts/render_diagram.py WORK/category_save.mmd --out WORK/category_save.svg
python3 scripts/render_diagram.py WORK/category_save.mmd --out WORK/category_save.svg --check
```

The renderer preserves the notation, adds visible context and binds the export to its source, style and presentation code. Rerender after any changes. Inspect the export at the size readers will use. Check the wording, matching symbols, clipping and legibility. A parser pass cannot reveal every unintended node or misleading label; presence checks cannot judge the explanation's accuracy.

Embed the SVG with descriptive alternative text, followed by an overview and a table explaining its elements. Directly below the table, add **Mermaid source** and a `text` code block containing the same Mermaid source used to render the image. Keep the `.mmd` file for rendering and checks; the document must also include the code. A `mermaid` fence may render another diagram instead of showing editable code. The on-canvas legend explains notation; the prose explains the scenario and each meaningful element. External captions, tooltips and accessibility metadata alone cannot supply screenshot context.

For checked delivery, select `diagram_svg` or `flowchart_svg` in `context.visuals`. Generate the SVG beside the destination document and capture it and its same-named `.mmd` as request sources before `prepare`. The gate checks visible context, symbol/label pairs, canvas, source/version binding and the embedded code against the captured `.mmd`, then freezes those bytes with review. Unrendered excerpts remain drafts or source-only deliverables.

## Number and explain the components

Number every meaningful component visibly, including sequence participants/messages/notes/branch guards and state nodes/transitions/notes. Keep explicit numbers in labels; do not add `autonumber` as a second numbering system. For a state start/end symbol, add `%% Reference: PARSER_ID | NUMBER. LABEL`; the renderer keeps the symbol and places the label beside it. Use hierarchical numbers only for real containment. Component numbers identify elements rather than forcing a document sequence.

Below the exported image, provide an overview and one explanation row for each component. The first cell repeats the entire visible number and label exactly; sequence branch guards include their visible brackets. Explain important conditions, feedback, failure and next actions in natural language. Embed the exact source in a `text` code block directly below the table.

The renderer inventories the actual parsed components, renders them, then inspects computed colors, contrast and clipping in a browser. All three steps are required in that order. Exports bind the source, shared style, renderer code and component inventory; rerender after any change to those inputs. The verified inventory adapters cover flowcharts, sequence diagrams and state diagrams in the installed Mermaid version. Other notations need a verified adapter or suitable exporter before accepted delivery; a parser success alone does not establish a checked export.

Run `scripts/check_diagram_collection.py --package PACKAGE` to check every source/export pair and Markdown consumer recursively. It checks exact rows, visible labels, embedded source and export binding. It cannot establish that explanations are accurate or sufficient; review those against the sources and Writing Style (WS). A render is not a writing-quality acceptance.
