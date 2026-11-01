#!/usr/bin/env python3
"""Render a self-contained diagram with visible context, a symbol legend and source binding."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET

from diagram_presentation import context_errors, frame_errors, frame_svg, source_context
import writing_style_contract as writing_style
import diagram_components as components

ROOT = Path(__file__).resolve().parents[1]
STYLE = ROOT / "config/diagram_style.json"
SVG = "http://www.w3.org/2000/svg"
ET.register_namespace("", SVG)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def contrast(first, second):
    def luminance(color):
        if not re.fullmatch(r"#[0-9A-Fa-f]{6}", color):
            raise ValueError("Use six-digit hexadecimal colors.")
        channels = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
        linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in channels]
        return sum(v * weight for v, weight in zip(linear, (0.2126, 0.7152, 0.0722)))
    a, b = sorted((luminance(first), luminance(second)))
    return (b + 0.05) / (a + 0.05)


def load_style():
    style = json.loads(STYLE.read_text())
    for name, role in style["roles"].items():
        if contrast(style["text"], role["fill"]) < style["minimum_text_contrast"]:
            raise ValueError("Insufficient text contrast for " + name)
        if contrast(style["stroke"], role["fill"]) < style["minimum_graphic_contrast"]:
            raise ValueError("Insufficient outline contrast for " + name)
    if contrast(style["stroke"], style["canvas"]["background"]) < style["minimum_graphic_contrast"]:
        raise ValueError("Insufficient connector contrast against canvas.")
    return style


def source_errors(source, style):
    context = source_context(source, style)
    errors = context_errors(context)
    if not context["family"]:
        errors.append("Begin the source with its Mermaid diagram declaration.")
    if re.search(r"(?m)^\s*(?:classDef|style|linkStyle)\b|%%\{", source):
        errors.append("Keep visual styling in the shared configuration; remove inline style overrides.")
    if re.search(r'(?m)^\s*autonumber\b', source):
        errors.append('Use explicit component references; do not add a second automatic message-number sequence.')
    if context["family"] == "state" and re.search(r"(?m)^.*-->.*:[^\n]*;", source):
        errors.append("Semicolons in state transition labels can create unintended states; use a separate line per transition.")
    for label in ("accTitle", "accDescr"):
        if not re.search(r"(?m)^[ \t]*" + label + r":[ \t]*\S", source):
            errors.append("Source needs nonempty " + label + ".")
    for roles in re.findall(r"(?m)^\s*class\s+[\w, -]+\s+(\w+)\s*;?\s*$", source):
        if roles not in style["roles"]:
            errors.append("Unknown semantic style role: " + roles)
    return errors


def style_source(source, style):
    errors = source_errors(source, style)
    if errors:
        raise ValueError(" ".join(errors))
    lines = [source.rstrip(), ""]
    if source_context(source, style)["family"] == "flowchart":
        for name, role in {"default": style["roles"]["process"], **style["roles"]}.items():
            lines.append(f"classDef {name} fill:{role['fill']},color:{style['text']},stroke:{style['stroke']},stroke-width:1.5px;")
    return "\n".join(lines) + "\n"


def renderer_identity():
    names = ('render_diagram.py', 'diagram_presentation.py', 'diagram_components.py', 'diagram_inventory.mjs', 'mermaid_runtime.mjs', 'audit_diagram.mjs')
    return sha(json.dumps({name:sha(Path(__file__).with_name(name).read_bytes()) for name in names},sort_keys=True).encode())


def pipeline_errors(events):
    return [] if isinstance(events,list) and all(isinstance(event,dict) for event in events) and [event.get('phase') for event in events]==['inventory','render','inspect'] and all(event.get('evidence') for event in events) else ['Diagram pipeline needs inventory, render and inspect in that order, with actual evidence.']


def add_canvas(svg, source, style, manifest=None):
    context = source_context(source, style)
    problems = context_errors(context)
    if problems:
        raise ValueError(" ".join(problems))
    manifest = manifest if manifest is not None else components.analyze_source(source, style)
    root = ET.fromstring(svg)
    # Mermaid's group renderer omits the parsed group's semantic class.
    # Apply its configured role directly to the actual group rectangle.
    for row in manifest['elements']:
        if not row.get('group'):
            continue
        role = next(name for name in row['classes'] if name in style['roles'])
        group = next((node for node in root.iter() if 'cluster' in node.get('class','').split() and node.get('id','').endswith('-'+row['id'])), None)
        rectangle = group.find('{'+SVG+'}rect') if group is not None else None
        if rectangle is None:
            raise ValueError('Rendered subprocess group is missing: '+row['id'])
        rectangle.set('style', 'fill:'+style['roles'][role]['fill']+';stroke:'+style['stroke']+';stroke-width:1.5px')
    special = [row for row in manifest['elements'] if row['kind'] in {'initial','final'}]
    for row in special:
        group = next((node for node in root.iter() if node.tag.endswith('}g') and '-state-'+row['id']+'-' in node.get('id','')), None)
        if group is None:
            raise ValueError('Rendered special-state symbol is missing: '+row['id'])
        label = ET.SubElement(group, '{'+SVG+'}text', {'x':'0','y':'-20','text-anchor':'middle','class':'technical-writer-special-reference','style':'fill:'+style['text']+';font-size:14px;font-family:Arial,sans-serif'})
        label.text = row['label']
    if special:
        box = [float(value) for value in root.get('viewBox').split()]
        margin=max(120,max(len(row['label'])*4 for row in special))
        root.set('viewBox',f'{box[0]-margin} {box[1]-32} {box[2]+margin*2} {box[3]+64}')
    root = frame_svg(root, context, style)
    view = [float(v) for v in root.attrib["viewBox"].split()]
    if len(view) != 4 or view[2] <= 0 or view[3] <= 0:
        raise ValueError("The rendered SVG needs a usable viewBox.")
    canvas = style["canvas"]
    defs = ET.Element("{" + SVG + "}defs")
    pattern = ET.SubElement(defs, "{" + SVG + "}pattern", {"id": "technical-writer-dots", "patternUnits": "userSpaceOnUse", "width": str(canvas["spacing"]), "height": str(canvas["spacing"])})
    ET.SubElement(pattern, "{" + SVG + "}rect", {"width": "100%", "height": "100%", "fill": canvas["background"]})
    ET.SubElement(pattern, "{" + SVG + "}circle", {"cx": str(canvas["spacing"] / 2), "cy": str(canvas["spacing"] / 2), "r": str(canvas["radius"]), "fill": canvas["dots"]})
    root.insert(0, defs)
    fill = "url(#technical-writer-dots)"
    rect = ET.Element("{" + SVG + "}rect", {"id": "technical-writer-canvas", "x": str(view[0]), "y": str(view[1]), "width": str(view[2]), "height": str(view[3]), "fill": fill, "aria-hidden": "true"})
    root.insert(1, rect)
    root.set("data-diagram-type", context["family"])
    root.set("data-source-sha256", sha(source.encode()))
    root.set("data-style-sha256", sha(STYLE.read_bytes()))
    root.set("data-presentation-sha256", sha(Path(__file__).with_name("diagram_presentation.py").read_bytes()))
    root.set('data-renderer-sha256',renderer_identity())
    components.embed_manifest(root,manifest)
    root.set("style", root.get("style", "") + ";background-color:" + canvas["background"] + ";color-scheme:light;")
    return ET.tostring(root, encoding="unicode")


def finish_export(svg, audit, events):
    if audit.get('passed') is not True or audit.get('kind')!='browser_observation' or pipeline_errors(events):
        raise ValueError('Actual diagram inspection and complete pipeline evidence are required before export.')
    root=ET.fromstring(svg)
    for name,value in (('design-audit',audit),('render-trace',events)):
        node=ET.SubElement(root,'{'+SVG+'}metadata',{'id':'technical-writer-'+name})
        node.text=json.dumps(value,sort_keys=True,ensure_ascii=False,separators=(',',':'))
    root.set('data-export-sha256',sha(ET.tostring(root,encoding='utf-8')))
    return ET.tostring(root,encoding='unicode')


def check_svg(svg, source, style=None):
    style = style or load_style()
    errors = source_errors(source, style)
    context = source_context(source, style)
    try:
        root = ET.fromstring(svg)
        if root.tag != "{" + SVG + "}svg" or root.get("data-diagram-type") != context["family"]:
            errors.append("Expected a generated SVG matching the source's diagram family.")
        if root.get("data-source-sha256") != sha(source.encode()) or root.get("data-style-sha256") != sha(STYLE.read_bytes()):
            errors.append("SVG source or shared style is stale.")
        if root.get("data-presentation-sha256") != sha(Path(__file__).with_name("diagram_presentation.py").read_bytes()):
            errors.append("SVG presentation is stale; rerender the diagram.")
        if root.get('data-renderer-sha256')!=renderer_identity():
            errors.append('SVG renderer/inventory code is stale; rerender the diagram.')
        sealed = root.attrib.pop('data-export-sha256',None)
        if sealed!=sha(ET.tostring(root,encoding='utf-8')):
            errors.append('SVG body or export evidence changed; rerender the diagram.')
        if sealed:
            root.set('data-export-sha256',sealed)
        manifest=components.read_manifest(root)
        errors.extend(components.svg_errors(root,manifest,style))
        audit=root.find(".//{"+SVG+"}metadata[@id='technical-writer-design-audit']")
        trace=root.find(".//{"+SVG+"}metadata[@id='technical-writer-render-trace']")
        audit_data=json.loads(audit.text) if audit is not None else None
        if not isinstance(audit_data,dict) or audit_data.get('passed') is not True or audit_data.get('kind')!='browser_observation':
            errors.append('Missing successful browser-computed diagram inspection.')
        if trace is None:
            errors.append('Missing render pipeline evidence.')
        else:
            errors.extend(pipeline_errors(json.loads(trace.text)))
        errors.extend(frame_errors(root, context))
        canvas = root.find(".//{" + SVG + "}rect[@id='technical-writer-canvas']")
        pattern = root.find(".//{" + SVG + "}pattern[@id='technical-writer-dots']")
        expected_fill = "url(#technical-writer-dots)"
        if canvas is None or canvas.get("fill") != expected_fill or canvas.get("aria-hidden") != "true":
            errors.append("Missing controlled light canvas.")
        elif [float(canvas.get(key, "nan")) for key in ("x", "y", "width", "height")] != [float(v) for v in root.get("viewBox", "").split()]:
            errors.append("Canvas does not cover the complete SVG viewBox.")
        if pattern is None:
            errors.append("Missing dot pattern.")
        else:
            background = pattern.find("{" + SVG + "}rect")
            dot = pattern.find("{" + SVG + "}circle")
            if background is None or background.get("fill") != style["canvas"]["background"]:
                errors.append("Incorrect opaque canvas background.")
            if dot is None or dot.get("fill") != style["canvas"]["dots"]:
                errors.append("Incorrect decorative dot color.")
            if pattern.get("patternUnits") != "userSpaceOnUse" or any(float(pattern.get(key, "nan")) != style["canvas"]["spacing"] for key in ("width", "height")):
                errors.append("Incorrect dot grid spacing.")
            if dot is not None and float(dot.get("r", "nan")) != style["canvas"]["radius"]:
                errors.append("Incorrect decorative dot size.")
    except (ET.ParseError, KeyError, ValueError, TypeError) as error:
        errors.append("Invalid diagram SVG: " + str(error))
    return errors


def mermaid_config(style):
    fill=style['roles']['process']['fill'];text=style['text'];line=style['stroke'];background=style['canvas']['background']
    variables={name:text for name in ('textColor','primaryTextColor','actorTextColor','signalTextColor','noteTextColor','labelTextColor','loopTextColor','stateLabelColor','transitionLabelColor','titleColor')}
    variables.update({name:line for name in ('primaryBorderColor','lineColor','actorBorder','actorLineColor','signalColor','noteBorderColor','labelBoxBorderColor','transitionColor','compositeBorder','specialStateColor','innerEndBackground','arrowheadColor')})
    variables.update(darkMode=False,background=background,primaryColor=fill,mainBkg=fill,nodeBkg=fill,nodeBorder=line,stateBkg=fill,actorBkg=fill,edgeLabelBackground=background,labelBackgroundColor=background,compositeBackground=background,compositeTitleBackground=fill,labelBoxBkgColor=style['roles']['subprocess']['fill'],noteBkgColor=style['roles']['decision']['fill'],sequenceNumberColor=text,fontFamily='Arial, sans-serif')
    css=f'''#technical-writer-content text, #technical-writer-content tspan {{fill:{text}!important;stroke:none!important;}}
#technical-writer-content foreignObject * {{color:{text}!important;font-family:Arial,sans-serif!important;}}
#technical-writer-content .actor-man circle {{fill:{style['roles']['actor']['fill']}!important;stroke:{line}!important;}}
#technical-writer-content .actor-man line, #technical-writer-content .actor-line, #technical-writer-content .loopLine {{stroke:{line}!important;}}
#technical-writer-content .edgeLabel rect {{opacity:1;fill:{background};}}'''
    return {'theme':'base','securityLevel':'strict','flowchart':{'htmlLabels':False,'curve':'linear'},'state':{'nodeSpacing':100,'rankSpacing':100},'sequence':{'wrap':True,'wrapPadding':16,'actorFontFamily':'Arial, sans-serif','noteFontFamily':'Arial, sans-serif','messageFontFamily':'Arial, sans-serif'},'themeCSS':css,'themeVariables':variables}


def inspect_svg(path, browser=None):
    node=shutil.which('node');module_root=os.environ.get('TECHNICAL_WRITER_MERMAID_MODULE_ROOT')
    if not node or not module_root:
        raise ValueError('Browser inspection needs Node and TECHNICAL_WRITER_MERMAID_MODULE_ROOT.')
    argv=[node,str(Path(__file__).with_name('audit_diagram.mjs')),module_root,str(path),str(STYLE)]
    if browser:
        argv.append(str(browser))
    result=subprocess.run(argv,text=True,capture_output=True,timeout=60,check=False)
    report=json.loads(result.stdout)
    if result.returncode or report.get('passed') is not True:
        raise ValueError('Diagram browser inspection failed: '+'; '.join(report.get('errors',[result.stderr])))
    return report


def render(source_path, output, renderer=None, puppeteer_config=None):
    source_path, output = Path(source_path), Path(output)
    guide = writing_style.guide_packet(writing_style.load_guide(ROOT), include_text=False)
    style, source = load_style(), source_path.read_text()
    executable = shutil.which(renderer or os.environ.get("TECHNICAL_WRITER_MERMAID_CLI", "mmdc"))
    if not executable:
        raise ValueError("Mermaid CLI unavailable; no diagram was rendered.")
    styled=style_source(source,style)
    manifest=components.analyze_source(source,style)
    events=[{'phase':'inventory','evidence':sha(json.dumps(manifest,sort_keys=True).encode())}]
    with tempfile.TemporaryDirectory(prefix="writer-diagram-") as folder:
        folder = Path(folder)
        (folder / "source.mmd").write_text(styled)
        config = mermaid_config(style)
        (folder / "config.json").write_text(json.dumps(config))
        argv = [executable, "-i", str(folder / "source.mmd"), "-o", str(folder / "diagram.svg"), "-c", str(folder / "config.json"), "-b", style["canvas"]["background"]]
        browser = puppeteer_config or os.environ.get("TECHNICAL_WRITER_PUPPETEER_CONFIG")
        if browser:
            argv += ["-p", str(browser)]
        result = subprocess.run(argv, capture_output=True, text=True, timeout=60, check=False)
        if result.returncode:
            raise ValueError("Mermaid rendering failed: " + result.stderr[-2000:])
        raw=(folder/'diagram.svg').read_text()
        events.append({'phase':'render','evidence':sha(raw.encode())})
        svg = add_canvas(raw, source, style, manifest)
        # Frame styles refer to its controlled group, which did not exist during Mermaid layout.
        root=ET.fromstring(svg)
        css=ET.SubElement(root,'{'+SVG+'}style');css.text=config['themeCSS']
        svg=ET.tostring(root,encoding='unicode')
        (folder/'inspected.svg').write_text(svg)
        audit=inspect_svg(folder/'inspected.svg',browser)
        events.append({'phase':'inspect','evidence':sha(json.dumps(audit,sort_keys=True).encode())})
        svg=finish_export(svg,audit,events)
        errors = check_svg(svg, source, style)
        if errors:
            raise ValueError(" ".join(errors))
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(svg + "\n")
    return {"passed": True, "source": str(source_path), "output": str(output), "canvas": style["canvas"], "source_sha256": sha(source.encode()), "style_sha256": sha(STYLE.read_bytes()), 'components':len(manifest['elements']),'design_audit':audit,'process_trace':{'provenance':{'kind':'instrumented_execution','source':'Actual parser, Mermaid rendering and browser inspection in render_diagram.py.'},'events':events}, "writing_style": guide, "style_review_status": "pending", "accepted": False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--check", action="store_true", help="Check an existing SVG without rerendering.")
    parser.add_argument("--renderer")
    parser.add_argument("--puppeteer-config", type=Path)
    args = parser.parse_args()
    try:
        if args.check:
            errors = check_svg(args.out.read_text(), args.source.read_text())
            result = {"passed": not errors, "findings": errors}
        else:
            result = render(args.source, args.out, args.renderer, args.puppeteer_config)
        print(json.dumps(result, indent=2))
        return int(not result["passed"])
    except (OSError, ValueError, subprocess.TimeoutExpired) as error:
        print(json.dumps({"passed": False, "error": str(error)}))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
