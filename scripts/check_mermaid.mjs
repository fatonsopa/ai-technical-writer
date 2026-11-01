// Parse with the configured Mermaid installation; no network access or package installation.
import { readFileSync } from 'node:fs';
import { runtime } from './mermaid_runtime.mjs';

try {
  const { mermaid, version } = await runtime(process.argv[2]);
  const blocks = JSON.parse(readFileSync(0, 'utf8'));
  const results = [];
  for (const block of blocks) {
    try {
      await mermaid.parse(block.body);
      results.push({ line: block.line, passed: true });
    } catch (error) {
      results.push({ line: block.line, passed: false, error: String(error) });
    }
  }
  const passed = results.every(row => row.passed);
  process.stdout.write(JSON.stringify({ passed, version, results }));
  process.exitCode = passed ? 0 : 1;
} catch (error) {
  process.stdout.write(JSON.stringify({ passed: false, error: String(error) }));
  process.exitCode = 2;
}
