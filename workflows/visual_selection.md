# Choose and explain the right visual

Use this guidance from [Visual Guidance (VG)](../references/visuals.md) when deciding which view the document needs. Read [Writing Style (WS)](../references/writing_style.md) for every text surface.

## Select the view and its owner

These are established names; document placement is this skill's convention. Select by the question.

| Reader question | Suitable view | Usual owner and trigger |
| --- | --- | --- |
| Who uses the system, and what is outside it? | C4 system context | High Level Document (HLD): establish or change system boundaries |
| Which applications and stores communicate? | C4 container | High Level Document (HLD): explain major responsibilities and interfaces |
| How is one application organized internally? | C4 component; selective code/class view for deeper detail | Low Level Design (LLD): internals need explanation |
| Where do applications and stores run? | Deployment diagram | High Level Document (HLD): hosting, networks or environment matters |
| What happens between participants, in what order? | Sequence diagram or C4 dynamic diagram | High Level Document (HLD): significant interactions; Low Level Design (LLD): detailed contracts |
| Which action follows a condition, loop or handoff? | Flowchart or UML activity diagram; swimlanes for responsibilities | Spec Driven Development document (SDD): required behavior; High Level Document (HLD)/Low Level Design (LLD): technical workflow |
| How does someone complete a task? | User flow | Spec Driven Development document (SDD): actions, decisions and responses need agreement |
| What appears at each interaction? | Wireflow combining simplified screens and flow; wireframe for static layout | In or linked from Spec Driven Development document (SDD); technical UI design in Low Level Design (LLD) |
| What states and transitions are allowed? | State machine diagram | Spec Driven Development document (SDD): observable lifecycle; Low Level Design (LLD): internal state |
| How are entities related? | Entity Relationship Diagram (ERD) | High Level Document (HLD): significant conceptual model; Low Level Design (LLD): detailed schema |
| Where does data cross ownership or trust boundaries? | Data Flow Diagram (DFD), with trust boundaries for security analysis | High Level Document (HLD) data/security view; link a detailed threat model when needed |
| How does experience span channels and time? | Journey map | Product Requirements Document (PRD)/discovery: broader experience matters |
| How do roles coordinate a business process? | BPMN business process diagram | Business behavior in or linked from Spec Driven Development document (SDD) when formal notation helps |
| What does evidence show or how do values compare? | Screenshot; quantitative chart; comparison table | Relevant document, using actual evidence and data |

C4 levels describe zoom, not phases. A container is an application or data store; Docker is not implied. Context/container views often suffice. Deployment shows infrastructure separately.


## Construct the visual

1. Put a visible title, scope subtitle and symbol legend inside every diagram image. They must survive copying or a screenshot. Identify current/proposed/example status where relevant. Use the document's actors, terms and requirement IDs.
2. Separate structural relationships from scenario execution. Label relationship arrows with meaning and relevant protocol; show event order explicitly in a sequence or numbered dynamic view.
3. Show workflow triggers, conditions, branches, loops, handoffs and outcomes. Use activity notation for concurrency and swimlanes for responsibility.
4. For a sequence, identify participants, messages, meaningful responses and failure alternatives. Show asynchronous behavior, transaction boundaries or uncertain outcomes when material. Split scenarios when one diagram becomes hard to read.
5. For states, label transitions with events and relevant guards. A tab or filter is not automatically a lifecycle state. For an ERD, identify conceptual/logical/physical scope and relevant relationships and cardinality; it does not show execution or data movement.
6. For deployment, identify the environment and map applications onto actual or proposed infrastructure. For a DFD, identify processes, stores, external entities, data flows and relevant trust boundaries. Preserve unknown hosting/security choices.
7. For user flows and wireflows, connect actions to feedback, including relevant cancellation, validation, permission and failure outcomes. A wireframe shows layout; a wireflow adds interaction. Link editable UX artifacts where Markdown cannot represent their layout well.
8. Give charts units, period, source and a suitable scale. Screenshots establish observed appearance; do not fabricate them. Avoid color-only meaning. Add a legend for unfamiliar shapes, icons or line styles.
9. Give every meaningful component a unique visible numeric reference: flowchart nodes; sequence participants, messages, notes and branch guards; and state nodes, transitions and notes. Keep state start/end symbols intact and place their reference beside the symbol. Use hierarchical numbers only for real containment. Below each diagram, give an overview and one table row per component, repeating its complete visible number and label exactly. Explain the condition, action, feedback and next path in enough context to be understood without the author. For Mermaid, embed its source in a `text` code block directly below the table. Provide alternative text and accessible metadata.

Use a host-supported notation. Mermaid flowcharts are not automatically C4, UML or BPMN; follow the claimed notation. Keep views focused.

Flowcharts/user flows follow [Flowchart design](flowcharts.md): palette, shapes, light dotted SVG canvas and editable source.

Follow [diagram rendering](diagram_rendering.md) for visible context, matching symbols and legends, and export checks. Apply [Writing Style (WS)](../references/writing_style.md) to titles, subtitles, node labels and legends as well as prose.

Use step numbers for ordered interactions. Use hierarchical IDs only for genuine parent/child decomposition, consistently across views. Keep names visible; never make readers decode numbers alone or imply execution order with structural IDs. Reuse stable element IDs across views and distinguish them from local sequence numbers. Quantitative charts explain series, axes and encodings, rather than every data point.

