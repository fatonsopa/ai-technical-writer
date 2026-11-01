"""Recursive source/export/consumer checks, independent of rendering controls."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import check_diagram_collection as collection
from test_diagram_components import SOURCE
from test_diagram_support import control_export,FLOW_ELEMENTS,table

class DiagramCollectionTests(unittest.TestCase):
    def fixture(self):
        temp=tempfile.TemporaryDirectory();self.addCleanup(temp.cleanup);r=Path(temp.name);(r/'examples/nested').mkdir(parents=True)
        (r/'examples/nested/view.mmd').write_text(SOURCE);(r/'examples/nested/view.svg').write_text(control_export(SOURCE,'flowchart',FLOW_ELEMENTS))
        text='# Category check\n\n![Category check](view.svg)\n\nThe page validates the selected category.\n\n'+table(FLOW_ELEMENTS)+'\n```text\n'+SOURCE+'```\n';(r/'examples/nested/explanation.md').write_text(text);return r,text

    def test_nested_assets_and_consumers_are_checked(self):
        r,text=self.fixture();result=collection.check(r);self.assertTrue(result['passed'],result);self.assertEqual(result['diagrams'],1);self.assertEqual(len(result['consumers']),1)

    def test_wrong_table_missing_source_or_orphan_asset_fails(self):
        for kind in ('table','source','orphan'):
            with self.subTest(kind=kind):
                r,text=self.fixture();p=r/'examples/nested/explanation.md'
                if kind=='table':p.write_text(text.replace('2. Valid? |','2. Wrong |'))
                if kind=='source':p.write_text(text.replace('```text','```other'))
                if kind=='orphan':p.unlink()
                self.assertFalse(collection.check(r)['passed'])
