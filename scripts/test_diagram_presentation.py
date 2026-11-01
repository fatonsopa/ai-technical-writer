"""Export-context controls; actual Mermaid rendering is verified on example artifacts."""
import json
from pathlib import Path
import re
import tempfile
import unittest
import xml.etree.ElementTree as ET
from unittest.mock import patch

import diagram_presentation as presentation
import render_diagram as diagram
import validate_document as delivery
from visual_contracts import diagram_blocks, embedded_source_errors, visual_errors
from document_contracts import headings
from test_diagram_support import control_export, SEQUENCE_ELEMENTS, table, raw_svg, manifest

SEQUENCE = '''%% Diagram: Sequence diagram
%% Subtitle: The administrator saves a category through the Websites page.
sequenceDiagram
accTitle: Save a website category
accDescr: The administrator sends a category change and receives confirmation.
actor A as 1. Administrator
participant UI as 2. Websites page
A->>UI: 3. Save category
UI-->>A: 4. Saved
'''
STATE = '''%% Subtitle: The editor keeps the selected value when saving fails.
stateDiagram-v2
accTitle: Category editor behavior
accDescr: Saving returns to editing if the request fails.
[*] --> Editing
Editing --> Saving: Save
Saving --> Editing: Request fails
'''
CONTROL = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 200"><g id="drawing"/></svg>'
NS = "{" + diagram.SVG + "}"


class DiagramPresentationTests(unittest.TestCase):
    def setUp(self):
        self.style = diagram.load_style()
        self.svg = control_export(SEQUENCE)

    def check_changed(self, change):
        root = ET.fromstring(self.svg)
        change(root)
        return diagram.check_svg(ET.tostring(root, encoding="unicode"), SEQUENCE)

    def test_title_subtitle_and_type_must_be_visible_text_not_metadata(self):
        self.assertEqual(diagram.check_svg(self.svg, SEQUENCE), [])
        for field in ("title", "subtitle", "type"):
            def remove(root):
                group = root.find(".//" + NS + "g[@id='technical-writer-" + field + "']")
                for text in group.findall(NS + "text"):
                    group.remove(text)
            with self.subTest(field=field):
                self.assertIn("visible diagram " + field, " ".join(self.check_changed(remove)))

    def test_symbol_explanations_are_headed_legend(self):
        for wrong in ("Key", "References", ""):
            def rename(root):
                root.find(".//" + NS + "g[@id='technical-writer-legend']/" + NS + "text").text = wrong
            with self.subTest(heading=wrong):
                self.assertIn("headed Legend", " ".join(self.check_changed(rename)))

    def test_each_legend_entry_needs_a_shape_and_a_matching_label(self):
        for tag in ("g", "text"):
            def remove(root):
                legend = root.find(".//" + NS + "g[@id='technical-writer-legend']")
                entry = legend.find(NS + "g")
                entry.remove(entry.find(NS + tag))
            with self.subTest(part=tag):
                self.assertIn("visible shape and label", " ".join(self.check_changed(remove)))

    def test_sequence_and_state_legends_keep_their_own_notation(self):
        seq = dict(presentation.source_context(SEQUENCE, self.style)["legend"])
        self.assertEqual(seq, {"human": "Actor", "participant": "Participant", "message": "Message", "response": "Response"})
        state = dict(presentation.source_context(STATE, self.style)["legend"])
        self.assertEqual(state, {"state": "State", "initial": "Start", "transition": "Transition"})
        for source in (SEQUENCE, STATE):
            self.assertTrue(diagram.source_errors(source + "\n%% Legend: decision | Decision\n", self.style))

    def test_sequence_alternative_legend_matches_the_rendered_tab_color(self):
        root=ET.Element(NS+"g");icon=presentation.glyph(root,"alternative",0,0,self.style)
        tab=icon.find(NS+"polygon")
        self.assertEqual(tab.get("fill"),diagram.mermaid_config(self.style)["themeVariables"]["labelBoxBkgColor"])
        self.assertEqual(icon.find(NS+"text").text,"alt")

    def test_visible_type_must_match_the_source_notation(self):
        mismatched = SEQUENCE.replace("%% Diagram: Sequence diagram", "%% Diagram: Flowchart")
        self.assertIn("matching the source notation", " ".join(diagram.source_errors(mismatched, self.style)))

    def test_subtitle_is_required_even_with_accessibility_description(self):
        source = "\n".join(line for line in SEQUENCE.splitlines() if not line.startswith("%% Subtitle:"))
        self.assertIn("scope subtitle", " ".join(diagram.source_errors(source, self.style)))

    def test_explicit_connection_label_retains_its_symbol(self):
        source = '%% Subtitle: The page reads website records.\nflowchart LR\naccTitle: Website reads\naccDescr: The page reads the database.\nA[Page] --> B[(Websites)]\nclass A process\nclass B datastore\n%% Legend: flow_arrow | Relationship\n'
        context = presentation.source_context(source, self.style)
        self.assertIn(("flow_arrow", "Relationship"), context["legend"])
        svg = control_export(source)
        self.assertEqual(diagram.check_svg(svg, source), [])

    def test_crossed_arrows_keep_their_line_style_and_explicit_scenario_meaning(self):
        for arrow, symbol, dash in (("--x", "lost", "4 3"), ("-x", "crossed", "none")):
            source = SEQUENCE + f"UI{arrow}A: No confirmation\n%% Legend: {symbol} | Lost response\n"
            context = presentation.source_context(source, self.style)
            self.assertIn((symbol, "Lost response"), context["legend"])
            other = "crossed" if symbol == "lost" else "lost"
            self.assertNotIn(other, dict(context["legend"]))
            root = ET.fromstring(control_export(source))
            icon = root.find(".//" + NS + "g[@id='technical-writer-legend']/" + NS + "g[@data-symbol='" + symbol + "']/" + NS + "g")
            self.assertEqual(icon.find(NS + "path").get("stroke-dasharray"), dash)

    def test_state_transition_semicolons_cannot_create_unintended_states(self):
        source = STATE.replace("Request fails", "Request fails; keep selection")
        self.assertIn("unintended states", " ".join(diagram.source_errors(source, self.style)))

    def test_sequence_source_does_not_receive_flowchart_class_definitions(self):
        styled = diagram.style_source(SEQUENCE, self.style)
        self.assertNotIn("classDef", styled)
        self.assertIn("sequenceDiagram", styled)

    def test_visible_context_is_part_of_source_version_binding(self):
        changed = self.svg.replace('data-presentation-sha256="', 'data-presentation-sha256="changed-')
        self.assertIn("presentation is stale", " ".join(diagram.check_svg(changed, SEQUENCE)))

    def test_diagram_delivery_freezes_source_export_and_rendering_guidance(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "save.mmd").write_text(SEQUENCE)
            (root / "save.svg").write_text(self.svg)
            request = {"kind": "visual", "sources": [{"id": "brief", "text": "Show the administrator's category save."}, {"id": "source", "path": "save.mmd"}, {"id": "svg", "path": "save.svg"}], "destination": "save.md", "context": {"visuals": [{"heading": "Save a category", "notation": "diagram_svg", "reason": "Show who sends and confirms the change."}]}}
            (root / "request.json").write_text(json.dumps(request))
            delivery.prepare(root / "request.json", root / "session")
            text = '# Save a category\n\n![Category save sequence](save.svg)\n\nThe administrator sends the category through the page.\n\n' + table(SEQUENCE_ELEMENTS) + '\n**Mermaid source**\n\n```text\n' + SEQUENCE + '```\n'
            (root / "draft.md").write_text(text)
            with patch.object(delivery, "check_syntax", side_effect=AssertionError("Literal source is not a second rendered diagram.")):
                result = delivery.check(root / "session", root / "draft.md")
            self.assertTrue(result["passed"], result)
            frozen = delivery.state_for(root / "session")["frozen"]
            self.assertIn("workflows/diagram_rendering.md", frozen["guidance"])
            (root / "draft.md").write_text(text.replace("A->>UI: 3. Save category", "A->>UI: 3. Save a different value"))
            result = delivery.check(root / "session", root / "draft.md")
            self.assertFalse(result["passed"])
            self.assertTrue(any("matching Mermaid source" in error for error in result["findings"]))
            (root / "save.svg").write_text(self.svg + "\n")
            with self.assertRaisesRegex(ValueError, "source changed"):
                delivery.check(root / "session", root / "draft.md")

    def test_source_link_alone_cannot_replace_the_embedded_code(self):
        text = '![Category save](save.svg)\n\n[Editable Mermaid source](save.mmd)\n'
        self.assertTrue(embedded_source_errors(text, SEQUENCE))

    def test_embedded_source_follows_the_image_and_explanation_table(self):
        image = '![Category save](save.svg)\n\n'
        table = '| Participant | Meaning |\n| --- | --- |\n| Administrator | Requests the save. |\n\n'
        code = '**Mermaid source**\n\n```text\n' + SEQUENCE + '```\n'
        self.assertEqual(embedded_source_errors(image + table + code, SEQUENCE), [])
        self.assertEqual(embedded_source_errors(image + table + code, SEQUENCE.replace("\n", "\r\n")), [])
        self.assertTrue(embedded_source_errors(image + code + table, SEQUENCE))
        self.assertTrue(embedded_source_errors(code + image + table, SEQUENCE))
        self.assertTrue(embedded_source_errors(image + table + code + code, SEQUENCE))

    def test_literal_source_cannot_supply_the_diagram_explanations(self):
        text = '# Save a category\n\n![Category save](save.svg)\n\n```text\n' + SEQUENCE + '\n| Participant | Meaning |\n| --- | --- |\n| Administrator | Requests the save. |\n```\n'
        self.assertEqual(diagram_blocks(text)[0], [])
        errors = visual_errors(text, headings(text), [{"heading": "Save a category", "notation": "diagram_svg", "reason": "Explain the request."}])
        self.assertTrue(any("Missing overview" in error for error in errors))
        self.assertTrue(any("Missing element explanations" in error for error in errors))

    def test_example_sources_are_embedded_below_their_explanation_tables(self):
        count = 0
        for path in sorted(diagram.ROOT.rglob("*.md")):
            if ".git" in path.parts or ".venv" in path.parts:
                continue
            text = path.read_text()
            images = list(re.finditer(r'!\[[^\]\n]+\]\(([^)]+\.svg)\)', text))
            for index, match in enumerate(images):
                source = (path.parent / match[1]).with_suffix(".mmd")
                if not source.is_file():
                    continue
                end = images[index + 1].start() if index + 1 < len(images) else len(text)
                with self.subTest(document=path.name, source=source.name):
                    self.assertEqual(embedded_source_errors(text[match.start():end], source.read_text()), [])
                count += 1
        self.assertGreater(count, 0)

    def test_workflow_document_nodes_use_canonical_names_and_acronyms(self):
        catalog = json.loads((diagram.ROOT / "evals/catalog.json").read_text())
        by_acronym = {row["acronym"]: row["full_name"] for row in catalog["output_kinds"]}
        source = (diagram.ROOT / "examples/diagrams/documentation_workflow.mmd").read_text()
        labels = dict(re.findall(r'(\w+)@\{ shape: doc, label: "([^"]+)" \}', source))
        expected = {acro: by_acronym[acro] + " (" + acro + ")" for acro in ("PRD", "SDD", "HLD", "LLD", "DR", "IP", "TP", "TS", "TSR", "TCR")}
        expected["WI"] = "Issue"
        self.assertEqual({key: re.sub(r"^\d+\.\s+", "", value) for key,value in labels.items()}, expected)
