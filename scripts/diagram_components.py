"""Bind visible numbered components to parser inventory and exact explanation rows."""
import hashlib
import html
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import xml.etree.ElementTree as ET

SVG = 'http://www.w3.org/2000/svg'
REFERENCE = re.compile(r'^\[?(\d+(?:\.\d+)*)\.\s+\S')


def normalize(value):
    return ' '.join(html.unescape(value).split())


def manifest_errors(manifest, style=None):
    if not isinstance(manifest,dict) or not isinstance(manifest.get('elements'),list):
        return ['Diagram component inventory must contain an elements array.']
    errors, numbers, ids = [], set(), set()
    rows = manifest.get('elements', [])
    if not rows:
        return ['A diagram needs an inventory of its actual meaningful components.']
    for row in rows:
        if not isinstance(row,dict) or not isinstance(row.get('id'),str) or not isinstance(row.get('label'),str) or not isinstance(row.get('kind'),str):
            errors.append('Malformed diagram component.');continue
        label = normalize(row.get('label', ''))
        match = REFERENCE.match(label)
        if not match:
            errors.append('Missing visible numeric reference: '+label)
        elif match[1] in numbers:
            errors.append('Duplicate visible reference: '+match[1])
        else:
            numbers.add(match[1])
        if row['id'] in ids:
            errors.append('Duplicate parser component: '+row['id'])
        ids.add(row['id'])
        if manifest.get('family')=='flowchart' and style:
            roles = set(row.get('classes', [])) & style['roles'].keys()
            if len(roles)!=1:
                errors.append('Assign exactly one semantic role to '+label)
            else:
                role = style['roles'][next(iter(roles))]
                allowed = role.get('mermaid_shapes', [])
                if allowed and row.get('shape') not in allowed:
                    errors.append('Shape disagrees with its semantic role: '+label)
    return errors


def analyze_source(source, style=None, module_root=None):
    node = shutil.which('node')
    root = module_root or os.environ.get('TECHNICAL_WRITER_MERMAID_MODULE_ROOT')
    if not node or not root:
        raise ValueError('Numbered diagram inventory needs Node and TECHNICAL_WRITER_MERMAID_MODULE_ROOT; no diagram was rendered.')
    result = subprocess.run([node, str(Path(__file__).with_name('diagram_inventory.mjs')), str(Path(root).resolve())], input=source, text=True, capture_output=True, timeout=30)
    data = json.loads(result.stdout)
    if result.returncode or data.get('error'):
        raise ValueError('Diagram inventory failed: '+str(data.get('error', result.stderr)))
    errors = manifest_errors(data, style)
    if errors:
        raise ValueError(' '.join(errors))
    return data


def embed_manifest(root, manifest):
    node = ET.SubElement(root, '{'+SVG+'}metadata', {'id':'technical-writer-components'})
    node.text = json.dumps(manifest, sort_keys=True, ensure_ascii=False, separators=(',',':'))
    root.set('data-components-sha256', hashlib.sha256(node.text.encode()).hexdigest())


def read_manifest(root):
    node = root.find(".//{"+SVG+"}metadata[@id='technical-writer-components']")
    if node is None or not node.text or hashlib.sha256(node.text.encode()).hexdigest()!=root.get('data-components-sha256'):
        raise ValueError('Missing or changed diagram component inventory.')
    value=json.loads(node.text)
    if not isinstance(value,dict):
        raise ValueError('Diagram component inventory must be an object.')
    return value


def hidden(element, parents):
    current = element
    while current is not None:
        value = current.get('style','').replace(' ','').lower()
        if any(token in value for token in ('display:none','visibility:hidden')) or re.search(r'(?:^|;)opacity:0(?:;|$)',value) or current.get('display')=='none' or current.get('visibility')=='hidden' or current.get('opacity')=='0':
            return True
        current = parents.get(current)
    return False


def visible_labels(root, kind):
    body = root.find(".//{"+SVG+"}g[@id='technical-writer-content']")
    if body is None:
        return set()
    parents = {child:parent for parent in body.iter() for child in parent}
    classes = {'actor':{'actor'},'participant':{'actor'},'message':{'messageText'},'fragment':{'loopText','sectionTitle'},'note':{'noteText','statediagram-note'},'transition':{'edgeLabel'}}.get(kind)
    values = set()
    for element in body.iter():
        if hidden(element, parents):
            continue
        if classes:
            current, matched = element, False
            while current is not None:
                if set(current.get('class','').split()) & classes:
                    matched=True;break
                current=parents.get(current)
            if not matched:
                continue
        if element.tag.rsplit('}',1)[-1] in {'text','tspan','foreignObject'}:
            value = normalize(' '.join(element.itertext()))
            if value:
                values.add(value)
    # Mermaid 11 renders wrapped sequence lines as adjacent text elements, and
    # else guards as sectionTitle. Join only adjacent visible lines of one label;
    # a new numbered label or a non-label element ends the run.
    if classes:
        for parent in body.iter():
            run = []
            for element in [*list(parent), None]:
                text = normalize(' '.join(element.itertext())) if element is not None else ''
                matches = element is not None and element.tag.rsplit('}',1)[-1] in {'text','tspan'} and bool(set(element.get('class','').split()) & classes) and not hidden(element,parents)
                if run and (not matches or REFERENCE.match(text)):
                    values.add(normalize(' '.join(run)));run=[]
                if matches:
                    run.append(text)
    return values


def svg_errors(root, manifest, style):
    errors = manifest_errors(manifest, style)
    for row in manifest.get('elements', []):
        if normalize(row['label']) not in visible_labels(root, row['kind']):
            errors.append('Component reference and label are not visible in the diagram body: '+row['label'])
    return errors


def cell_text(value):
    value=re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', value.strip())
    return normalize(value.replace('\\|','|').strip('`*'))


def explanation_errors(segment, manifest):
    table = re.search(r'(?m)^\s*\|[^\n]+\|\s*\n\s*\|(?:\s*:?-+:?\s*\|)+\s*\n((?:\s*\|[^\n]+\|\s*\n?)+)', segment)
    if not table:
        return ['Missing a component explanation table after the diagram overview.']
    rows=[]
    for line in table[1].strip().splitlines():
        cells = re.split(r'(?<!\\)\|', line.strip())[1:-1]
        if len(cells)<2 or not cells[1].strip():
            return ['Every component needs its own nonempty explanation.']
        rows.append(cell_text(cells[0]))
    expected = [normalize(row['label']) for row in manifest['elements']]
    if len(rows)!=len(set(rows)) or set(rows)!=set(expected) or len(rows)!=len(expected):
        return ['Explanation rows must match every complete visible reference and label exactly once; missing='+repr(sorted(set(expected)-set(rows)))+'; extra='+repr(sorted(set(rows)-set(expected)))]
    return []
