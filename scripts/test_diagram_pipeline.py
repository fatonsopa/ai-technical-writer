"""Exercise phase order, failure boundaries and export gating with authored controls."""
import json
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from unittest.mock import patch
import render_diagram as d
from test_diagram_components import SOURCE
from test_diagram_support import manifest,FLOW_ELEMENTS,raw_svg,AUDIT

class DiagramPipelineTests(unittest.TestCase):
    def test_every_required_step_and_adjacent_order_is_enforced(self):
        events=[{'phase':phase,'evidence':'authored'} for phase in ('inventory','render','inspect')]
        self.assertFalse(d.pipeline_errors(events))
        for index in range(3):self.assertTrue(d.pipeline_errors(events[:index]+events[index+1:]))
        for index in range(2):
            wrong=list(events);wrong[index],wrong[index+1]=wrong[index+1],wrong[index];self.assertTrue(d.pipeline_errors(wrong))
        self.assertTrue(d.pipeline_errors([{'phase':p} for p in ('inventory','render','inspect')]))

    def perform(self,failure=None):
        folder=tempfile.TemporaryDirectory();self.addCleanup(folder.cleanup);root=Path(folder.name);source=root/'source.mmd';source.write_text(SOURCE);out=root/'out.svg';events=[]
        def inventory(*args):
            events.append('inventory')
            if failure=='inventory':raise ValueError('invalid inventory')
            return manifest('flowchart',FLOW_ELEMENTS)
        def render(argv,**kwargs):
            events.append('render')
            if failure=='render':return SimpleNamespace(returncode=1,stderr='renderer failed')
            Path(argv[argv.index('-o')+1]).write_text(raw_svg(FLOW_ELEMENTS));return SimpleNamespace(returncode=0)
        def inspect(*args):
            events.append('inspect')
            if failure=='inspect':raise ValueError('inspection failed')
            return AUDIT
        with patch.object(d.shutil,'which',return_value=None if failure=='missing' else '/authored-renderer'),patch.object(d.components,'analyze_source',side_effect=inventory),patch.object(d.subprocess,'run',side_effect=render),patch.object(d,'inspect_svg',side_effect=inspect):
            if failure:
                with self.assertRaises(ValueError):d.render(source,out)
                self.assertFalse(out.exists());return events
            result=d.render(source,out)
            self.assertEqual(d.check_svg(out.read_text(),SOURCE),[]);self.assertFalse(result['accepted']);self.assertEqual(result['style_review_status'],'pending');return events

    def test_actual_call_order_and_pending_writing_review(self):
        self.assertEqual(self.perform(),['inventory','render','inspect'])

    def test_failure_stops_before_later_phases_and_does_not_export(self):
        for failure,expected in [('missing',[]),('inventory',['inventory']),('render',['inventory','render']),('inspect',['inventory','render','inspect'])]:
            with self.subTest(failure=failure):self.assertEqual(self.perform(failure),expected)

    def test_failed_or_absent_browser_inspection_cannot_seal_export(self):
        for audit in ({},{**AUDIT,'passed':False},{**AUDIT,'kind':'authored_control'}):
            with self.assertRaises(ValueError):d.finish_export('<svg/>',audit,[{'phase':p,'evidence':'control'} for p in ('inventory','render','inspect')])
