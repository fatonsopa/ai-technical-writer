# Design and render a flowchart

Use this procedure when shared [Visual Guidance (VG)](../references/visuals.md) selects a flowchart or user flow. Keep sequence diagrams, state machines, ERDs and C4 views in their appropriate notation. A structural relationship view may use flowchart tooling, but must not imply execution order.

## Establish the flow

Use the verified behavior and decisions from [discovery](discover.md). Identify the reader's question, entry condition, actions, decisions, loops and outcomes. Include relevant error, permission and cancellation paths; leave unresolved behavior explicit. Create only the views needed to explain the work.

Apply the useful layout guidance from [Flowmapp](https://www.flowmapp.com/blog/qa/how-to-design-flowcharts): consistent symbols, spacing and alignment; short labels; a clear reading direction; identifiable starts/outcomes; readable branch paths; and restrained color. Prefer left-to-right or top-to-bottom according to the content and page. Reduce crossings and unnecessary bends. Split an oversized view into named, linked parts. Normally use no more than four or five fill colors in one view. Add statistics only when they answer the question and have sources; decorative numbers do not improve an engineering flow.

The article's visual-marketing advice does not require bright decoration, invented metrics, a particular commercial tool, or left-to-right layout in every context. Review a complex view with an intended reader when possible.

## Apply the shared visual style

[Diagram style](../config/diagram_style.json) owns the palette and canvas. Its fills follow the user-selected [Flowmapp shape illustration](https://cdn.prod.website-files.com/65084cba9d60b1182e9f0021/66e400fb9a7a20a9116c812f_6560ceea94e26f1ac1cc95c1_6.%2520Shapes%2520to%2520Use.webp). These colors are a project convention, not a universal software-engineering standard.

| Meaning | Shape / style role |
| --- | --- |
| Action or processing step | Rectangle, `process`: very light mint |
| Question or condition | Diamond, `decision`: pale yellow; label outgoing branches |
| Document | Wavy-bottom document, `document`: light gray |
| Input/output data | Parallelogram, `data`: lavender |
| Start/end of a process | Pill/terminator, `terminator`: lavender |
| Expanded subprocess | Named grouped detail, `subprocess`: peach |
| Predefined routine | Double-sided rectangle, `predefined`: mint green |
| Continuation connector | Circle, `connector`: neutral; label the continuation |
| Setup | Hexagon, `preparation`: very pale pink |
| Screen output | Display symbol, `display`: pale yellow |
| Delay, paper tape or manual operation | Use the matching conventional symbol and configured role only when relevant |
| Person in a relationship view | Labelled actor, `actor`: pale pink |
| Persistent store | Cylinder, `datastore`: lavender; distinguish storage from input/output |

Keep yes/no as decision-branch labels. A connector circle does not replace the decision diamond. Preserve symbols required by the selected notation. Include a legend explaining the roles actually used; color must never be the only distinction.

Every flowchart must have an opaque light canvas with faint decorative dots, dark labels and readable lines. The dots carry no meaning. The style checker verifies normal text contrast of at least 4.5:1 and essential outlines/connectors of at least 3:1; decorative dots are exempt. Darker outlines preserve the reference's pastel fills while keeping shapes distinguishable. See [W3C text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) and [color use](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html).

## Render and embed

Follow [self-contained diagram rendering](diagram_rendering.md) for titles, scope subtitles, symbol/label legend entries, export commands and checked delivery. Put the visible title in `accTitle` and scope in `%% Subtitle:`; retain `accDescr` for accessibility. Keep editable `.mmd` source beside its SVG.

Assign semantic roles with `class` statements, such as `class Check decision`. The renderer supplies the palette and matching on-canvas glyphs; use `%% Legend: flow_arrow | Next action` to clarify a line's meaning. Styling stays in the shared configuration. The exported light dotted canvas is independent of the Markdown host's theme.

Use `flowchart_svg` for the selected `context.visuals` entry and capture the SVG/source before checked delivery. Keep the detailed element descriptions below the image as well. If a required export cannot be rendered or checked, retain it as a draft rather than substitute a theme-dependent image.

Use the numbered symbol guide in [Visual Guidance (VG)](../references/visuals.md). Every node needs one semantic class matching its actual shape. Use a circle for a connector, with Yes/No on decision branches. Use `subgraph` for an expanded subprocess and the double-sided predefined-process shape for a subprocess defined elsewhere.
