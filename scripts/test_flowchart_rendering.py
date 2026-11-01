"""Check shared palette, canvas and source-bound SVG delivery; rendering is checked separately."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest
import xml.etree.ElementTree as ET
from unittest.mock import patch

import render_flowchart as flow
import validate_document as delivery
from test_document_contracts import sample
from test_diagram_support import control_export, FLOW_ELEMENTS


class FlowchartRenderingTests(unittest.TestCase):
    def setUp(self):
        self.source = '%% Subtitle: Validate the proposed category before saving.\nflowchart LR\naccTitle: A category check\naccDescr: Check a category before saving.\nA["1. Choose category"] --> B{"2. Valid?"}\nclass A process\nclass B decision\n'
        self.style = flow.load_style()
        # Authored XML control for canvas mechanics, not proof of Mermaid rendering.
        self.svg = control_export(self.source, 'flowchart', FLOW_ELEMENTS)

    def test_declared_text_and_essential_lines_have_sufficient_contrast(self):
        for role in self.style["roles"].values():
            self.assertGreaterEqual(flow.contrast(self.style["text"], role["fill"]), 4.5)
            self.assertGreaterEqual(flow.contrast(self.style["stroke"], role["fill"]), 3)
        self.assertGreaterEqual(flow.contrast(self.style["stroke"], self.style["canvas"]["background"]), 3)

    def test_low_contrast_configuration_is_rejected(self):
        style = deepcopy(self.style)
        style["text"] = style["roles"]["process"]["fill"]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "style.json"
            path.write_text(json.dumps(style))
            with patch.object(flow, "STYLE", path), self.assertRaisesRegex(ValueError, "text contrast"):
                flow.load_style()

    def test_light_canvas_and_decorative_dots_are_actual_svg_elements(self):
        self.assertEqual(flow.check_svg(self.svg, self.source), [])
        self.assertIn('id="technical-writer-canvas"', self.svg)
        self.assertIn('color-scheme:light', self.svg)
        self.assertTrue(flow.check_svg(self.svg.replace('id="technical-writer-canvas"', 'id="removed"'), self.source))
        self.assertTrue(flow.check_svg(self.svg.replace('fill="#F7F7F7"', 'fill="transparent"'), self.source))

    def test_changed_source_or_style_cannot_reuse_an_old_export(self):
        self.assertIn("stale", " ".join(flow.check_svg(self.svg, self.source + "\nC[Later change]\n")))
        changed = self.svg.replace('data-style-sha256="', 'data-style-sha256="changed-')
        self.assertIn("stale", " ".join(flow.check_svg(changed, self.source)))

    def test_partial_canvas_or_oversized_dots_are_rejected(self):
        root = ET.fromstring(self.svg)
        root.find(".//{" + flow.SVG + "}rect[@id='technical-writer-canvas']").set("width", "40")
        self.assertTrue(flow.check_svg(ET.tostring(root, encoding="unicode"), self.source))
        self.assertTrue(flow.check_svg(self.svg.replace('r="1"', 'r="12"'), self.source))

    def test_incomplete_sources_and_inline_style_overrides_are_rejected(self):
        self.assertTrue(flow.source_errors("sequenceDiagram\nA->>B: Request\n", self.style))
        for suffix in ("\nstyle A fill:black\n", "\nclass A invented\n", '\n%%{init: {"theme":"dark"}}%%\n'):
            with self.assertRaises(ValueError):
                flow.style_source(self.source + suffix, self.style)

    def test_real_example_exports_match_their_sources_and_style(self):
        for source in (flow.ROOT / "examples/diagrams").glob("*.mmd"):
            with self.subTest(source=source.name):
                self.assertEqual(flow.check_svg(source.with_suffix(".svg").read_text(), source.read_text()), [])

    def test_checked_delivery_freezes_both_source_and_export(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            source, svg = root / "flow.mmd", root / "flow.svg"
            source.write_text(self.source)
            svg.write_text(self.svg)
            request = {"kind": "hld", "sources": [{"id": "brief", "text": "Category validation precedes saving."}, {"id": "diagram-source", "path": "flow.mmd"}, {"id": "diagram", "path": "flow.svg"}], "destination": "hld.md", "context": {"discovery": {"status": "ready", "source_ids": ["brief"], "decisions": []}, "visuals": [{"heading": "Category flow", "notation": "flowchart_svg", "reason": "Explain category validation."}]}}
            path = root / "request.json"
            path.write_text(json.dumps(request))
            delivery.prepare(path, root / "session")
            draft = root / "draft.md"
            draft.write_text(sample("hld") + "\n### Category flow\n\n![Category validation](flow.svg)\n\nValidation precedes saving.\n\n| Element | Meaning |\n| --- | --- |\n| 1. Choose category | Provide the proposed value. |\n| 2. Valid? | Determine whether saving may proceed. |\n\n**Mermaid source**\n\n```text\n" + self.source + "```\n")
            self.assertTrue(delivery.check(root / "session", draft)["passed"])
            source.write_text(self.source + "\nC[New step]\n")
            with self.assertRaisesRegex(ValueError, "source changed"):
                delivery.check(root / "session", draft)

    def test_a_link_to_unfrozen_assets_cannot_claim_checked_delivery(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            request = {"kind": "visual", "sources": [{"id": "brief", "text": "Explain category validation."}], "destination": "view.md", "context": {"visuals": [{"heading": "Category flow", "notation": "flowchart_svg", "reason": "Explain validation."}]}}
            (root / "request.json").write_text(json.dumps(request))
            delivery.prepare(root / "request.json", root / "session")
            draft = root / "draft.md"
            draft.write_text("### Category flow\n\n![Category validation](flow.svg)\n")
            # Mandatory Writing Style capture fails before a reviewable packet can
            # be made. The missing asset must never become accepted delivery.
            with self.assertRaisesRegex(ValueError, "Capture every linked SVG"):
                delivery.check(root / "session", draft)
            self.assertFalse((root / "view.md").exists())

    def test_inline_flowcharts_cannot_bypass_the_controlled_canvas(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            request = {"kind": "visual", "sources": [{"id": "brief", "text": "Explain category validation."}], "destination": "view.md"}
            (root / "request.json").write_text(json.dumps(request))
            delivery.prepare(root / "request.json", root / "session")
            draft = root / "draft.md"
            draft.write_text("### Category flow\n\n```mermaid\n" + self.source + "```\n\nCheck the category before saving.\n\n- Choose category: propose a value.\n- Valid: validate the value.\n")
            with patch.object(delivery, "check_syntax", return_value={"status": "passed", "version": "authored control"}):
                report = delivery.check(root / "session", draft)
            self.assertFalse(report["passed"])
            self.assertTrue(any("light dotted canvas" in item for item in report["findings"]))
