"""Mandatory guide routing and review guards. These are authored controls."""
import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import validate_document as delivery
import writing_style_contract as style
import render_diagram as diagram
from test_diagram_support import SEQUENCE_ELEMENTS, raw_svg, manifest, AUDIT

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'evals'))
import evaluation


def style_control(contract):
    """Positive fixture, not an AI or human writing-quality observation."""
    return {'guide_sha256': contract['guide_sha256'], 'output_sha256': contract['targets'][0]['sha256'], 'targets_sha256': contract['targets_sha256'], 'reviewed_targets': [row['id'] for row in contract['targets']], 'passed': True, 'rationale': 'Authored unit control covering all listed text targets; no model-quality claim.'}


class WritingStyleTests(unittest.TestCase):
    def test_renderer_does_not_accept_unreviewed_text_or_render_without_guide(self):
        source = '%% Subtitle: The page confirms the saved category.\nsequenceDiagram\naccTitle: Category save results\naccDescr: The user saves a category and sees the result.\nactor U as 1. Administrator\nparticipant P as 2. Websites page\nU->>P: 3. Save category\nP-->>U: 4. Saved\n'
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            path = root / 'source.mmd'
            path.write_text(source)
            def render_control(argv, **kwargs):
                Path(argv[argv.index('-o') + 1]).write_text(raw_svg(SEQUENCE_ELEMENTS))
                return SimpleNamespace(returncode=0)
            with patch.object(diagram.shutil, 'which', return_value='/authored-render-control'), patch.object(diagram.subprocess, 'run', render_control), patch.object(diagram.components, 'analyze_source', return_value=manifest('sequence', SEQUENCE_ELEMENTS)), patch.object(diagram, 'inspect_svg', return_value=AUDIT):
                result = diagram.render(path, root / 'diagram.svg')
            self.assertTrue(result['passed'])
            self.assertFalse(result['accepted'])
            self.assertEqual(result['style_review_status'], 'pending')
            self.assertEqual(result['writing_style']['guide'], style.REFERENCE)
            with patch.object(style, 'load_guide', return_value=''), patch.object(diagram.subprocess, 'run') as render:
                with self.assertRaises(ValueError):
                    diagram.render(path, root / 'missing-guide.svg')
                render.assert_not_called()

    def test_short_labels_questions_and_other_text_have_the_same_required_guide(self):
        guide = style.load_guide(ROOT)
        for value in ('# Change the category', 'Is the signed-in user an administrator?', 'Yes', 'The selected category remains available after a failed save.'):
            contract = style.packet(value, guide)
            self.assertEqual(contract['guide'], style.REFERENCE)
            self.assertTrue(style.check_review(contract, style_control(contract)))
        with self.assertRaises(ValueError):
            style.packet('A title', '')

    def test_missing_stale_partial_or_duplicate_style_reviews_are_rejected(self):
        contract = style.packet('# Review\n\n```mermaid\nflowchart LR\n A["Choose category"] --> B["Save"]\n```\n', style.load_guide(ROOT))
        for change in ({}, {'guide_sha256': 'wrong'}, {'output_sha256': 'wrong'}, {'targets_sha256': 'wrong'}, {'reviewed_targets': ['output']}, {'reviewed_targets': ['output', 'output']}, {'rationale': ''}):
            review = style_control(contract)
            review = {} if not change else {**review, **change}
            with self.subTest(change=change), self.assertRaises(ValueError):
                style.check_review(contract, review)

    def test_a_reported_style_failure_remains_a_failure(self):
        contract = style.packet('Compressed admin save signal.', style.load_guide(ROOT))
        review = style_control(contract)
        review.update(passed=False, rationale='The label is compressed and does not explain the action.')
        self.assertFalse(style.check_review(contract, review))

    def test_captured_svg_text_is_a_required_review_target(self):
        svg = '<svg xmlns="http://www.w3.org/2000/svg"><title>Choose a category</title><desc>Save or cancel an edit.</desc><text>1. Choose category</text><style>ignored CSS</style></svg>'
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            sources = [{'id': 'diagram', 'path': str(root / 'diagram.svg'), 'text': svg}]
            contract = style.packet('# Edit\n\n![Category selection](diagram.svg)\n', style.load_guide(ROOT), sources, root / 'guide.md')
            target = contract['targets'][1]
            self.assertEqual(target['id'], 'diagram:diagram.svg')
            self.assertIn('1. Choose category', target['text'])
            self.assertNotIn('ignored CSS', target['text'])
            changed_sources = [{**sources[0], 'text': svg.replace('Choose category', 'Save category')}]
            changed = style.packet('# Edit\n\n![Category selection](diagram.svg)\n', style.load_guide(ROOT), changed_sources, root / 'guide.md')
            with self.assertRaisesRegex(ValueError, 'stale'):
                style.check_review(changed, style_control(contract))
            review = style_control(contract)
            review['reviewed_targets'] = ['output']
            with self.assertRaisesRegex(ValueError, 'every text target'):
                style.check_review(contract, review)
            with self.assertRaisesRegex(ValueError, 'Capture every linked SVG'):
                style.packet('![Diagram](diagram.svg)', style.load_guide(ROOT), [], root / 'guide.md')

    def test_delivery_rejects_missing_or_failed_style_review_even_with_good_scores(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            request = {'kind': 'readme', 'operation': 'edit', 'scope': 'title', 'sources': [{'id': 'brief', 'text': 'Use Release rules as the title.'}], 'destination': 'result.md'}
            (root / 'request.json').write_text(json.dumps(request))
            delivery.prepare(root / 'request.json', root / 'session')
            (root / 'draft.md').write_text('# Release rules\n')
            packet = delivery.packet(root / 'session', root / 'draft.md')
            data = {'objective_sha256': packet['objective_sha256'], 'output_sha256': packet['output_sha256'], 'reviewer': {'kind': 'current_host_self_review', 'identity': 'fixture', 'model': None, 'method': 'Authored control.'}, 'scores': [3] * 7, 'critical_failures': [], 'reasons': ['Authored control.'], 'requirements': []}
            path = root / 'review.json'
            path.write_text(json.dumps(data))
            with self.assertRaisesRegex(ValueError, 'writing-style'):
                delivery.review(root / 'session', path)
            data['style_review'] = style_control(packet['writing_style'])
            data['style_review'].update(passed=False, rationale='Deliberate failed style control.')
            path.write_text(json.dumps(data))
            self.assertFalse(delivery.review(root / 'session', path)['accepted'])
            self.assertFalse((root / 'result.md').exists())

    def test_every_kind_operation_and_scope_captures_the_shared_guide(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for kind in delivery.load_contracts()['documents']:
                for operation in ('create', 'edit', 'review', 'rewrite'):
                    for scope in ('complete', 'excerpt', 'title'):
                        identifier = '-'.join((kind, operation, scope))
                        request = {'kind': kind, 'operation': operation, 'scope': scope, 'sources': [{'id': 'brief', 'text': 'Authored source fixture; no live user choices.'}], 'destination': identifier + '.md', 'context': {'discovery': {'status': 'ready', 'source_ids': ['brief'], 'decisions': []}}}
                        path = root / 'request.json'
                        path.write_text(json.dumps(request))
                        delivery.prepare(path, root / identifier)
                        state = delivery.state_for(root / identifier)
                        with self.subTest(kind=kind, operation=operation, scope=scope):
                            self.assertTrue(state['frozen']['guidance'][style.REFERENCE])

    def test_custom_eval_case_cannot_omit_style_from_generation_or_grading(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'source.md').write_text('Change only the title to Release rules.')
            case = {'id': 'style-case', 'kind': 'readme', 'operation': 'edit', 'artifact_scope': 'title', 'fixture': 'source.md', 'request': 'Change the title.', 'references': []}
            evaluation.prepare(ROOT, [case], root / 'session', 2, 600, case_root=root)
            packet = evaluation.packet(root / 'session', case['id'], 'generate')
            self.assertIn(style.REFERENCE, packet['writing_style']['guide'])
            response = {'case_id': case['id'], 'phase': 'generate', 'packet_sha256': packet['packet_sha256'], 'data': {'content': '# Release rules', 'references_read': []}}
            result = evaluation.submit(root / 'session', response)
            self.assertFalse(result['accepted'])
            self.assertEqual(result['task_success_percent'], 0)
            with self.assertRaisesRegex(ValueError, 'not awaiting'):
                evaluation.packet(root / 'session', case['id'], 'grade')
            evaluation.prepare(ROOT, [case], root / 'positive', 2, 600, case_root=root)
            generated = evaluation.packet(root / 'positive', case['id'], 'generate')
            response['packet_sha256'] = generated['packet_sha256']
            response['data']['references_read'] = [style.REFERENCE]
            evaluation.submit(root / 'positive', response)
            graded = evaluation.packet(root / 'positive', case['id'], 'grade')
            self.assertEqual(graded['guides'][style.REFERENCE], style.load_guide(ROOT))
            self.assertEqual(graded['writing_style']['guide_sha256'], generated['writing_style']['guide_sha256'])

    def test_style_behavior_cases_cover_non_document_text_and_rendered_delivery(self):
        cases = json.loads((ROOT / 'evals/style_cases.json').read_text())
        rubric = json.loads((ROOT / 'evals/rubrics/style_behavior.json').read_text())
        self.assertEqual({row['id'] for row in cases}, {'style-audit-and-question', 'style-diagram-and-delivery', 'writer-message-convention-gate'})
        self.assertEqual(set(rubric['cases']), {row['id'] for row in cases})
        for case in cases:
            self.assertIn(style.REFERENCE, case['resources'])
            self.assertEqual(case['kind'], 'behavior')
            self.assertTrue(case['request']['source'])


class SvgTextBoundaryTests(unittest.TestCase):
    def test_html_line_break_preserves_document_name_words(self):
        text = '<svg xmlns="http://www.w3.org/2000/svg"><foreignObject><div><p>No separate Low Level<br/>Design (LLD) needed</p></div></foreignObject></svg>'
        rendered = style.svg_text(text)
        self.assertIn('Low Level Design (LLD)', rendered)
        self.assertEqual(style.document_name_findings(rendered), [])

    def test_actual_wrapped_workflow_svg_preserves_document_names(self):
        source = (ROOT / 'examples/diagrams/documentation_workflow.svg').read_text()
        text = style.svg_text(source)
        self.assertIn('No separate Low Level Design (LLD) needed', text)
        self.assertEqual(style.document_name_findings(text), [])

    def test_inline_formatting_preserves_opaque_literal_without_inserted_spaces(self):
        text = '<svg><foreignObject><p>008<span>7</span></p><p>Next</p></foreignObject></svg>'
        self.assertEqual(style.svg_text(text), '0087 Next')
