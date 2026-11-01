"""Meaningful controls for numbering, exact rows, visibility and delivery."""
from copy import deepcopy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET
import diagram_components as c
import render_diagram as diagram
import validate_document as delivery
from test_diagram_support import manifest, FLOW_ELEMENTS, table, control_export, NS

SOURCE = '%% Subtitle: Validate the category before saving.\nflowchart LR\naccTitle: Category validation\naccDescr: Choose and validate the category.\nA["1. Choose category"] --> B{"2. Valid?"}\nclass A process\nclass B decision\n'

class DiagramComponentTests(unittest.TestCase):
    def setUp(self):
        self.manifest=manifest('flowchart',deepcopy(FLOW_ELEMENTS));self.style=diagram.load_style()

    def test_unique_visible_references_and_real_hierarchy_are_accepted(self):
        self.assertEqual(c.manifest_errors(self.manifest,self.style),[])
        self.manifest['elements'][1]['label']='1.1. Validate category'
        self.assertEqual(c.manifest_errors(self.manifest,self.style),[])

    def test_internal_ids_cannot_replace_visible_numbers(self):
        for label in ('Choose category','A1 Choose category','1.',''):
            self.manifest['elements'][0]['label']=label
            self.assertTrue(c.manifest_errors(self.manifest,self.style),label)

    def test_duplicate_references_and_parser_ids_fail(self):
        for field,value in [('label','1. Different label'),('id','A')]:
            m=deepcopy(self.manifest);m['elements'][1][field]=value
            self.assertTrue(c.manifest_errors(m,self.style))

    def test_semantic_roles_must_match_the_actual_shape(self):
        for change in ({'classes':[]},{'classes':['process','decision']},{'shape':'circle'}):
            m=deepcopy(self.manifest);m['elements'][0].update(change)
            self.assertTrue(c.manifest_errors(m,self.style))

    def test_legacy_input_output_shape_matches_the_same_data_role(self):
        m=manifest('flowchart',[{'id':'I','kind':'node','label':'1. Input','shape':'lean_right','classes':['data']}])
        self.assertEqual(c.manifest_errors(m,self.style),[])

    def test_exact_bijective_explanation_rows_pass(self):
        self.assertEqual(c.explanation_errors(table(self.manifest['elements']),self.manifest),[])

    def test_missing_grouped_orphan_duplicate_and_paraphrased_rows_fail(self):
        good=table(self.manifest['elements'])
        cases=[good.replace('| 2. Valid? | Authored explanation control for this component. |\n',''),good+'| 3. Orphan | Not in diagram. |\n',good+good.splitlines()[-1]+'\n',good.replace('2. Valid?','2. Is it valid?'),good.replace('1. Choose category','1–2. Choose and validate'),good.replace('2. Valid?','3. Valid?'),good.replace('Authored explanation control for this component.','')]
        for bad in cases:
            with self.subTest(text=bad):self.assertTrue(c.explanation_errors(bad,self.manifest))

    def test_hidden_or_metadata_only_labels_cannot_satisfy_visibility(self):
        svg=control_export(SOURCE,'flowchart',self.manifest['elements']);root=ET.fromstring(svg)
        self.assertEqual(c.svg_errors(root,self.manifest,self.style),[])
        body=root.find('.//'+NS+'g[@id="technical-writer-content"]')
        for node in body.iter():
            if node.text=='1. Choose category':node.set('style','display:none')
        self.assertTrue(c.svg_errors(root,self.manifest,self.style))

    def test_wrapped_sequence_lines_and_else_guards_keep_exact_labels(self):
        root=ET.fromstring('<svg xmlns="http://www.w3.org/2000/svg"><g id="technical-writer-content"><text class="messageText">1. Check access and</text><text class="messageText">input</text><path/><text class="messageText">2. Return result</text><g><text class="sectionTitle">[3. Request accepted]</text></g></g></svg>')
        self.assertIn('1. Check access and input',c.visible_labels(root,'message'))
        self.assertIn('[3. Request accepted]',c.visible_labels(root,'fragment'))
        self.assertNotIn('1. Check access and input 2. Return result',c.visible_labels(root,'message'))

    def test_expanded_subprocess_uses_its_configured_fill_and_outline(self):
        m=manifest('flowchart',[{'id':'N15','kind':'node','label':'15. Expanded subprocess','group':True,'shape':'rect','classes':['subprocess']}])
        raw='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 200"><g class="cluster" id="my-svg-N15"><rect/><text>15. Expanded subprocess</text></g></svg>'
        svg=diagram.add_canvas(raw,SOURCE,self.style,m);root=ET.fromstring(svg)
        paint=root.find('.//'+NS+'g[@id="my-svg-N15"]/'+NS+'rect').get('style')
        self.assertIn(self.style['roles']['subprocess']['fill'],paint)
        self.assertIn(self.style['stroke'],paint)

    def test_source_body_renderer_inventory_and_used_pattern_are_bound(self):
        svg=control_export(SOURCE,'flowchart',self.manifest['elements'])
        for bad in [svg.replace('1. Choose category</text>','1. Changed</text>'),svg.replace('url(#technical-writer-dots)','none'),svg.replace('data-renderer-sha256="','data-renderer-sha256="stale-'),svg.replace('technical-writer-components','changed-components')]:
            with self.subTest():self.assertTrue(diagram.check_svg(bad,SOURCE))

    def test_omitting_visual_selection_does_not_skip_exact_row_validation(self):
        with tempfile.TemporaryDirectory() as folder:
            r=Path(folder);svg=control_export(SOURCE,'flowchart',self.manifest['elements']);(r/'view.mmd').write_text(SOURCE);(r/'view.svg').write_text(svg)
            req={'kind':'visual','sources':[{'id':'source','path':'view.mmd'},{'id':'svg','path':'view.svg'}],'destination':'accepted.md'}
            (r/'request.json').write_text(json.dumps(req));delivery.prepare(r/'request.json',r/'session')
            self.assertIn('workflows/diagram_rendering.md',delivery.state_for(r/'session')['frozen']['guidance'])
            doc='# Category validation\n\n![Category check](view.svg)\n\nThe page validates the category before saving.\n\n'+table(self.manifest['elements'])+'\n```text\n'+SOURCE+'```\n';(r/'draft.md').write_text(doc)
            self.assertTrue(delivery.check(r/'session',r/'draft.md')['passed'])
            (r/'draft.md').write_text(doc.replace('| 2. Valid? |','| 2. Wrong label |'))
            self.assertFalse(delivery.check(r/'session',r/'draft.md')['passed'])

    def test_frozen_model_cases_and_rubrics_cover_both_notations(self):
        root=Path(__file__).resolve().parents[1];cases=json.loads((root/'evals/diagram_cases.json').read_text());rubric=json.loads((root/'evals/rubrics/diagram_behavior.json').read_text())
        self.assertEqual({x['id'] for x in cases},set(rubric['cases']))
        self.assertEqual(len(cases),2)
        for case in cases:
            self.assertEqual(case['kind'],'behavior');self.assertTrue(case['semantic']);self.assertIn('/technical-writer',case['request']['instruction']);self.assertTrue(case['request']['source'])
