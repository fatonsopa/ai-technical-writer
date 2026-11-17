'Controlled local deletion cases; no model-performance claim.'
from pathlib import Path
import json
import sys
import tempfile
import unittest
from unittest.mock import patch
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import record_retention as records
class RetentionTests(unittest.TestCase):

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.now = 1000000.0

    def bundle(self, name, **kwargs):
        path = self.root / name
        with patch.object(records.time, 'time', return_value=self.now):
            records.begin(path, 'fixture', **kwargs)
        (path / 'events.jsonl').write_text('observed event\n')
        return path

    def close(self, path, **kwargs):
        with patch.object(records.time, 'time', return_value=self.now):
            return records.finish(path, **kwargs)

    def sweep(self, days, **kwargs):
        return records.cleanup(self.root, 'fixture', now=self.now + days * 86400, **kwargs)

    def test_first_preview_then_expiry_leaves_unmanaged_and_active_files(self):
        old = self.bundle('old')
        self.close(old)
        active = self.bundle('active')
        legacy = self.root / 'legacy'
        legacy.mkdir()
        (legacy / 'events.jsonl').write_text('historical')
        preview = self.sweep(31)
        self.assertEqual(preview['mode'], 'preview')
        self.assertTrue(old.exists())
        self.assertEqual(next((r['action'] for r in preview['records'] if r.get('bundle') == str(old))), 'would_delete')
        applied = self.sweep(31)
        self.assertFalse(old.exists())
        self.assertTrue(active.exists())
        self.assertTrue(legacy.exists())
        self.assertEqual([r['action'] for r in applied['records'] if r.get('bundle') == str(old)], ['deleted'])
        receipt = json.loads((self.root / '.record-retention-fixture.json').read_text())['deletions'][0]
        self.assertEqual(receipt['record_id'], preview['records'][1]['record_id'] if preview['records'][1]['bundle'] == str(old) else preview['records'][0]['record_id'])
        self.assertNotIn('observed event', json.dumps(receipt))

    def test_failed_clock_starts_at_resolution_and_pins_survive(self):
        failed = self.bundle('failed')
        self.close(failed, outcome='failed')
        accepted = self.bundle('accepted')
        self.close(accepted, pin='accepted-version')
        self.sweep(400)
        self.sweep(400)
        self.assertTrue(failed.exists())
        self.assertTrue(accepted.exists())
        with patch.object(records.time, 'time', return_value=self.now + 400 * 86400):
            records.finish(failed, outcome='failed', resolved=True)
        self.sweep(489)
        self.assertTrue(failed.exists())
        self.sweep(491)
        self.assertFalse(failed.exists())
        self.assertTrue(accepted.exists())

    def test_details_expire_separately_but_ancestor_evidence_protects_them(self):
        parent = self.bundle('run')
        child = parent / 'diagnostics'
        with patch.object(records.time, 'time', return_value=self.now):
            records.begin(child, 'fixture', kind='diagnostic')
        (child / 'tool-bodies.json').write_text('{"result":"synthetic"}')
        self.close(child)
        self.close(parent)
        self.sweep(8)
        self.sweep(8)
        self.assertFalse(child.exists())
        self.assertTrue(parent.exists())
        self.sweep(31)
        self.assertFalse(parent.exists())
        parent = self.bundle('pinned-run')
        child = parent / 'diagnostics'
        records.begin(child, 'fixture', kind='diagnostic')
        (child / 'body').write_text('synthetic')
        self.close(child)
        self.close(parent)
        records.pin_reference(child / 'body', 'accepted-proof')
        self.sweep(500)
        self.assertTrue(child.exists())
        self.assertTrue(parent.exists())

    def test_changed_bundle_symlink_and_protected_source_are_never_deleted(self):
        changed = self.bundle('changed')
        self.close(changed)
        (changed / 'events.jsonl').write_text('new information')
        outside = self.root / 'outside'
        outside.mkdir()
        (outside / 'keep').write_text('user content')
        link = self.root / 'alias'
        link.symlink_to(outside, target_is_directory=True)
        with self.assertRaises(ValueError):
            records.begin(link, 'fixture')
        with self.assertRaises(ValueError):
            records.begin(self.root / 'protected', 'fixture', protected=[self.root])
        with self.assertRaises(ValueError):
            records.begin(outside, 'fixture')
        self.sweep(500)
        self.sweep(500)
        self.assertTrue(changed.exists())
        self.assertEqual((outside / 'keep').read_text(), 'user content')

    def test_owned_symlink_only_unlinks_pointer_and_explicit_dry_run_never_deletes(self):
        outside = self.root / 'source'
        outside.mkdir()
        (outside / 'keep').write_text('user')
        bundle = self.bundle('closed')
        (bundle / 'source-link').symlink_to(outside, target_is_directory=True)
        self.close(bundle)
        self.sweep(31, dry_run=True)
        self.sweep(31, dry_run=True)
        self.assertTrue(bundle.exists())
        self.sweep(31)
        self.assertFalse(bundle.exists())
        self.assertEqual((outside / 'keep').read_text(), 'user')

    def test_investigation_is_an_explicit_class_even_without_program_failure(self):
        case = self.bundle('investigation', kind='investigation')
        self.close(case)
        self.sweep(400)
        self.sweep(400)
        self.assertTrue(case.exists())
        with patch.object(records.time, 'time', return_value=self.now + 400 * 86400):
            records.finish(case, resolved=True)
        self.sweep(491)
        self.assertFalse(case.exists())

    def test_resolved_investigation_starts_the_diagnostic_seven_day_clock(self):
        parent = self.bundle('case', kind='investigation')
        child = parent / 'diagnostics'
        records.begin(child, 'fixture', kind='diagnostic')
        (child / 'body').write_text('synthetic')
        self.close(child)
        self.close(parent, outcome='failed')
        self.sweep(100)
        self.sweep(100)
        self.assertTrue(child.exists())
        with patch.object(records.time, 'time', return_value=self.now + 100 * 86400):
            records.finish(parent, outcome='failed', resolved=True)
        self.sweep(106)
        self.assertTrue(child.exists())
        self.sweep(108)
        self.assertFalse(child.exists())
        self.assertTrue(parent.exists())


class WriterRecordIntegrationTests(unittest.TestCase):
    def test_actual_prepare_finalize_and_legacy_evidence_preservation(self):
        from test_document_delivery import DocumentDeliveryTests
        import validate_document as writer
        fixture=DocumentDeliveryTests();fixture.setUp();self.addCleanup(fixture.tearDown)
        fixture.prepare()
        marker=fixture.session/records.MARKER
        meta=json.loads(marker.read_text())
        self.assertEqual(meta['owner'],'technical-writer');self.assertIsNone(meta['closed_at'])
        report=fixture.judgment();writer.finalize(fixture.session,fixture.draft,report['review'])
        meta=json.loads(marker.read_text());self.assertIsNotNone(meta['closed_at']);self.assertTrue(meta['pins'])
        records.cleanup(fixture.session.parent,'technical-writer',now=meta['closed_at']+500*86400)
        self.assertTrue(fixture.session.exists());self.assertEqual(fixture.target.read_bytes(),fixture.draft.read_bytes())

    def test_cli_closes_after_its_transient_lock_and_retirement_preserves_output(self):
        import subprocess
        import validate_document as writer
        from test_document_delivery import DocumentDeliveryTests
        fixture=DocumentDeliveryTests();fixture.setUp();self.addCleanup(fixture.tearDown)
        fixture.prepare();review=fixture.judgment()
        result=subprocess.run([sys.executable,str(Path(writer.__file__)),'finalize','--session',str(fixture.session),'--draft',str(fixture.draft),'--review',review['review']],capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)
        meta=json.loads((fixture.session/records.MARKER).read_text())
        self.assertEqual(meta['fingerprint'],records._fingerprint(fixture.session,meta['children']))
        for pin in meta['pins']:records.release(fixture.session,pin,'Authored control retires its own temporary evidence.')
        records.cleanup(fixture.session.parent,'technical-writer',now=meta['closed_at']+31*86400)
        self.assertFalse(fixture.session.exists());self.assertEqual(fixture.target.read_bytes(),fixture.draft.read_bytes())
