// Load the user's installed parser; never download packages or guess a version.
import {createRequire} from 'node:module';
import {dirname, join, resolve} from 'node:path';
import {pathToFileURL} from 'node:url';
import {readFileSync} from 'node:fs';

export async function runtime(root) {
  if (!root) throw new Error('Configure the directory containing Mermaid and jsdom.');
  const require = createRequire(join(resolve(root), 'package.json'));
  const {JSDOM} = require('jsdom');
  const dom = new JSDOM('<!doctype html><html><body></body></html>');
  globalThis.window = dom.window;
  globalThis.document = dom.window.document;
  const entry = require.resolve('mermaid');
  const version = JSON.parse(readFileSync(join(dirname(entry), '..', 'package.json'), 'utf8')).version;
  const {default: mermaid} = await import(pathToFileURL(entry).href);
  mermaid.initialize({startOnLoad: false, securityLevel: 'strict'});
  return {mermaid, version, require};
}
