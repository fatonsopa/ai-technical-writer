"""Title, scope and reader-level regressions; no claims about model accuracy."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import xml.etree.ElementTree as ET

import title_contract as titles
import diagram_presentation as presentation
import render_diagram as diagram
from document_contracts import validate
from test_document_contracts import sample
import test_document_delivery as delivery_controls
from test_diagram_support import control_export
from test_diagram_presentation import SEQUENCE

ROOT = Path(__file__).resolve().parents[1]


class TitleContractTests(unittest.TestCase):
    def test_reported_command_titles_and_generic_titles_are_rejected(self):
        for title in ('Save category for selected website', 'Save a category for selected websites', 'Click the save button', 'Overview', 'Diagram'):
            with self.subTest(title=title):
                self.assertTrue(titles.title_errors(title))

    def test_topic_titles_and_real_noun_uses_are_accepted(self):
        for title in ('Website review workflow', 'Category save results', 'Save behavior', 'Build configuration', 'Review process', 'Category editor states'):
            with self.subTest(title=title):
                self.assertEqual(titles.title_errors(title), [])

    def test_actions_remain_valid_for_task_titles_and_steps(self):
        self.assertEqual(titles.title_errors('Fix category saves for selected websites', task=True), [])
        self.assertTrue(validate('# Fix category saves for selected websites', 'issue_bug', scope='title')['passed'])
        self.assertTrue(validate('# Review omits parked websites without citation aggregates', 'bug_report', scope='title')['passed'])
        self.assertEqual(diagram.source_errors(SEQUENCE, diagram.load_style()), [])
        self.assertIn('3. Save category', SEQUENCE)

    def test_document_title_cannot_pass_just_by_completing_the_sections(self):
        text = sample('prd')
        old = text.splitlines()[0]
        self.assertFalse(validate(text.replace(old, '# Save category for selected website', 1), 'prd')['passed'])
        self.assertTrue(validate(text.replace(old, '# Website review requirements', 1), 'prd')['passed'])

    def test_unrelated_excerpt_does_not_require_rewriting_the_title(self):
        result = validate('# Save a category\n\nAn unchanged source title.', 'prd', 'edit', 'excerpt')
        self.assertTrue(result['passed'], result)

    def test_high_self_review_scores_cannot_publish_a_rejected_title(self):
        fixture = delivery_controls.DocumentDeliveryTests()
        fixture.setUp()
        try:
            fixture.prepare()
            text = fixture.draft.read_text()
            fixture.draft.write_text(text.replace(text.splitlines()[0], '# Save category for selected website', 1))
            result = fixture.judgment()
            self.assertFalse(result['accepted'])
            import validate_document as delivery
            with self.assertRaisesRegex(ValueError, 'passing checks'):
                delivery.finalize(fixture.session, fixture.draft, result['review'])
            self.assertFalse(fixture.target.exists())
        finally:
            fixture.tearDown()

    def test_visible_scope_is_short_but_accessibility_description_can_explain(self):
        self.assertEqual(titles.subtitle_errors('Successful category changes, from submission to confirmation.'), [])
        self.assertTrue(titles.subtitle_errors('This diagram illustrates the comprehensive end to end process ' * 6))
        source = SEQUENCE.replace('accDescr:', 'accDescr: ' + 'The confirmed save returns to the page. ' * 6)
        self.assertEqual(diagram.source_errors(source, diagram.load_style()), [])

    def test_bad_title_stops_before_browser_or_dependency_lookup(self):
        with tempfile.TemporaryDirectory() as folder:
            source = Path(folder) / 'diagram.mmd'
            source.write_text(SEQUENCE.replace('Category save results', 'Save category for selected website'))
            with patch.object(diagram.shutil, 'which', side_effect=AssertionError('Do not launch a renderer for rejected text.')):
                with self.assertRaisesRegex(ValueError, 'topic title'):
                    diagram.render(source, Path(folder) / 'diagram.svg')

    def test_overview_is_default_and_dense_overviews_are_rejected(self):
        context = presentation.source_context(SEQUENCE, diagram.load_style())
        self.assertEqual(context['view'], 'overview')
        self.assertTrue(titles.readability_errors(SEQUENCE, context, {'elements': list(range(9))}))
        self.assertEqual(titles.readability_errors(SEQUENCE, context, {'elements': list(range(4))}), [])

    def test_detail_is_explicit_bounded_and_visible_in_export(self):
        source = SEQUENCE.replace('%% Diagram:', '%% View: detail\n%% Diagram:', 1)
        context = presentation.source_context(source, diagram.load_style())
        self.assertEqual(titles.readability_errors(source, context, {'elements': list(range(9))}), [])
        self.assertTrue(titles.readability_errors(source, context, {'elements': list(range(33))}))
        root = ET.fromstring(control_export(source))
        group = root.find('.//{' + diagram.SVG + "}g[@id='technical-writer-view']")
        self.assertIn('Technical detail', ''.join(group.itertext()))
        self.assertEqual(root.get('data-view-profile'), 'detail')

    def test_sequence_nesting_is_bounded_for_the_selected_reader_level(self):
        source = SEQUENCE + '\nalt Save confirmed\nopt Refresh\nUI->>A: 5. Updated\nend\nend\n'
        self.assertTrue(titles.readability_errors(source, {'family': 'sequence', 'view': 'overview'}))
        self.assertEqual(titles.readability_errors(source, {'family': 'sequence', 'view': 'detail'}), [])

    def test_unknown_profile_and_changed_export_profile_are_rejected(self):
        source = SEQUENCE.replace('%% Diagram:', '%% View: unlimited\n%% Diagram:', 1)
        self.assertTrue(diagram.source_errors(source, diagram.load_style()))
        svg = control_export(SEQUENCE).replace('data-view-profile="overview"', 'data-view-profile="detail"')
        self.assertTrue(diagram.check_svg(svg, SEQUENCE))

    def test_maintained_diagrams_have_topic_titles_and_brief_scopes(self):
        for path in (ROOT / 'examples/diagrams').glob('*.mmd'):
            with self.subTest(path=path.name):
                self.assertEqual(diagram.source_errors(path.read_text(), diagram.load_style()), [])

    def test_embedded_teaching_sources_follow_the_same_title_rule(self):
        import re
        for folder in ('references', 'examples', 'workflows'):
            for path in (ROOT / folder).rglob('*.md'):
                for title in re.findall(r'(?m)^\s*accTitle:\s*(.+)$', path.read_text()):
                    with self.subTest(path=path.name, title=title):
                        self.assertEqual(titles.title_errors(title), [])

    def test_actual_model_case_has_quality_criteria_and_checked_host_coverage(self):
        cases = json.loads((ROOT / 'evals/title_cases.json').read_text())
        rubric = json.loads((ROOT / 'evals/rubrics/title_behavior.json').read_text())
        self.assertEqual(len(cases), 1)
        self.assertTrue(cases[0]['critical'] and cases[0]['semantic'])
        self.assertIn('Save category for selected website', cases[0]['request']['source']['brief.txt'])
        self.assertGreaterEqual(len(rubric['cases'][cases[0]['id']]), 5)
        config = json.loads((ROOT / 'config/host_validation.json').read_text())
        self.assertIn({'path': 'evals/title_cases.json', 'verify_delivery': True}, config['case_files'])
