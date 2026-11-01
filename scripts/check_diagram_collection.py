#!/usr/bin/env python3
"""Check every diagram pair and Markdown consumer, including nested examples."""
import argparse
import json
from pathlib import Path
import re
import xml.etree.ElementTree as ET

from repository_files import inventory
from render_diagram import check_svg
from visual_contracts import embedded_source_errors
from diagram_components import explanation_errors, read_manifest

IMAGES = re.compile(r'!\[[^\]\n]*\]\((?:<([^>\n]+\.svg)>|([^)\n]+\.svg))\)', re.I)


def check(root):
    root=Path(root).resolve();files=inventory(root);findings=[];assets={};consumers=[]
    for name in files:
        if name.endswith('.mmd') and name.startswith(('examples/','references/','assets/')):
            source=root/name;svg=source.with_suffix('.svg')
            if not svg.is_file():
                findings.append(name+': missing rendered SVG.');continue
            text=source.read_text();raw=svg.read_text()
            findings += [name+': '+error for error in check_svg(raw,text)]
            try:
                assets[svg.resolve()]={'source':text,'manifest':read_manifest(ET.fromstring(raw)),'name':name,'uses':0}
            except (ValueError,ET.ParseError) as error:
                findings.append(name+': '+str(error))
    for name in files:
        if not name.endswith('.md'):
            continue
        path=root/name;text=path.read_text()
        masked=re.sub(r'(?ms)^ {0,3}(`{3,}|~{3,})[^\n]*\n.*?^ {0,3}\1[ \t]*$', lambda m: ' '*len(m[0]), text)
        images=list(IMAGES.finditer(masked))
        for index,image in enumerate(images):
            target=image[1] or image[2]
            if re.match(r'\w+://',target):
                continue
            resolved=(path.parent/target).resolve()
            if not resolved.is_relative_to(root):
                findings.append(name+': diagram path leaves the package: '+target);continue
            if resolved not in assets:
                if resolved.is_file() and 'data-diagram-type=' not in resolved.read_text() and not resolved.with_suffix('.mmd').exists():
                    continue  # Icons/charts are outside this Mermaid collection.
                findings.append(name+': SVG needs an inventoried source/export pair: '+target);continue
            asset=assets[resolved];asset['uses']+=1
            segment=text[image.start():images[index+1].start() if index+1<len(images) else len(text)]
            findings += [name+': '+error for error in explanation_errors(segment,asset['manifest'])]
            findings += [name+': '+error for error in embedded_source_errors(segment,asset['source'])]
            consumers.append({'document':name,'diagram':str(resolved.relative_to(root)),'components':len(asset['manifest']['elements'])})
    for asset in assets.values():
        if not asset['uses']:
            findings.append(asset['name']+': diagram has no Markdown consumer.')
    return {'passed':not findings,'findings':findings,'diagrams':len(assets),'consumers':consumers,'limits':'Checks source/export/design binding and exact component rows. Actual wording, source meaning and browser evidence still need review.'}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--package',type=Path,default=Path(__file__).resolve().parents[1])
    result=check(parser.parse_args().package);print(json.dumps(result,indent=2));raise SystemExit(not result['passed'])
