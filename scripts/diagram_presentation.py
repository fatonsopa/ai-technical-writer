"""Visible context and notation legends carried inside exported diagrams."""
import math
import re
import textwrap
import xml.etree.ElementTree as ET

SVG = "http://www.w3.org/2000/svg"
SYMBOLS = {
    "process": "Process", "decision": "Decision", "document": "Document",
    "data": "Data", "terminator": "Start / end", "subprocess": "Subprocess",
    "predefined": "Predefined process", "connector": "Connector", "preparation": "Preparation",
    "display": "Display", "paper": "Paper tape", "delay": "Delay", "manual": "Manual operation",
    "actor": "Person", "datastore": "Database", "flow_arrow": "Flow line",
    "flow_dashed": "Supporting link", "human": "Actor", "participant": "Participant",
    "message": "Message", "response": "Response", "lost": "Response (crossed arrow)",
    "crossed": "Message (crossed arrow)",
    "alternative": "Alternative paths", "loop": "Loop", "optional": "Optional interaction",
    "note": "Note", "order": "Message number", "state": "State", "initial": "Start",
    "final": "End", "transition": "Transition", "entity": "Entity", "relationship": "Relationship",
}
# Names follow Mermaid's notation documentation, not a universal flowchart vocabulary.
# https://mermaid.js.org/syntax/stateDiagram.html
# https://mermaid.js.org/syntax/sequenceDiagram.html
# The crossed arrow's "Lost response" meaning is the examples' explicit local convention.
DIAGRAM_TYPES = {
    "flowchart": ("Flowchart", "User flow", "Architecture diagram"),
    "sequence": ("Sequence diagram",), "state": ("State diagram",),
    "erDiagram": ("Entity relationship diagram",), "classDiagram": ("Class diagram",),
    "C4Context": ("System context diagram",), "C4Container": ("Container diagram",),
    "C4Component": ("Component diagram",), "C4Deployment": ("Deployment diagram",),
    "C4Dynamic": ("Dynamic diagram",), "journey": ("User journey map",),
    "gantt": ("Gantt chart",), "pie": ("Pie chart",), "timeline": ("Timeline",),
}


def source_context(source, style):
    lines = [line.strip() for line in source.splitlines() if line.strip() and not line.lstrip().startswith("%%")]
    declaration = re.match(r"[A-Za-z][\w-]*", lines[0]) if lines else None
    token = declaration[0] if declaration else ""
    family = {"graph": "flowchart", "sequenceDiagram": "sequence", "stateDiagram": "state", "stateDiagram-v2": "state"}.get(token, token)
    title = re.search(r"(?m)^[ \t]*accTitle:[ \t]*(\S[^\n]*)", source)
    subtitle = re.search(r"(?mi)^[ \t]*%%[ \t]*Subtitle:[ \t]*(\S[^\n]*)", source)
    declared_type = re.search(r"(?mi)^[ \t]*%%[ \t]*Diagram:[ \t]*(\S[^\n]*)", source)
    type_label = declared_type[1].strip() if declared_type else DIAGRAM_TYPES.get(family, ("",))[0]
    entries = []
    if family == "flowchart":
        roles = set(re.findall(r"(?m)^\s*class\s+[\w, -]+\s+(\w+)\s*;?\s*$", source))
        entries += [(role, SYMBOLS.get(role, role)) for role in style["roles"] if role in roles]
        if "-->" in source:
            entries.append(("flow_arrow", SYMBOLS["flow_arrow"]))
        if "-." in source:
            entries.append(("flow_dashed", SYMBOLS["flow_dashed"]))
    elif family == "sequence":
        rules = [("human", r"(?m)^\s*actor\s"), ("participant", r"(?m)^\s*participant\s"),
                 ("message", r"(?<!-)->>"), ("response", r"-->>"), ("lost", r"--x"),
                 ("crossed", r"(?<!-)-x"),
                 ("alternative", r"(?m)^\s*alt\s"), ("loop", r"(?m)^\s*loop\s"),
                 ("optional", r"(?m)^\s*opt\s"), ("note", r"(?mi)^\s*note\s"),
                 ("order", r"(?m)^\s*autonumber\b")]
        entries += [(symbol, SYMBOLS[symbol]) for symbol, pattern in rules if re.search(pattern, source)]
    elif family == "state":
        entries.append(("state", SYMBOLS["state"]))
        for symbol, pattern in [("initial", r"\[\*\]\s*-->"), ("final", r"-->\s*\[\*\]"), ("transition", r"-->"), ("note", r"(?mi)^\s*note\s")]:
            if re.search(pattern, source):
                entries.append((symbol, SYMBOLS[symbol]))
    # Explicit entries can refine a generic connection label or explain another notation.
    explicit = re.findall(r"(?mi)^[ \t]*%%[ \t]*Legend:[ \t]*(\w+)[ \t]*\|[ \t]*(\S[^\n]*)", source)
    legend = dict(entries)
    legend.update((symbol, label.strip()) for symbol, label in explicit)
    return {"family": family, "type": type_label, "title": title[1].strip() if title else "", "subtitle": subtitle[1].strip() if subtitle else "", "legend": list(legend.items())}


def context_errors(context):
    errors = []
    if context["type"] not in DIAGRAM_TYPES.get(context["family"], ()):
        errors.append("Use an established diagram type matching the source notation.")
    if not context["title"]:
        errors.append("Diagram needs a visible title from accTitle.")
    if not context["subtitle"]:
        errors.append("Diagram needs a scope subtitle: %% Subtitle: ...")
    if not context["legend"]:
        errors.append("Diagram needs symbol/label legend entries; use semantic classes or %% Legend: symbol | label.")
    for symbol, label in context["legend"]:
        if symbol not in SYMBOLS or not label.strip():
            errors.append("Unknown or empty diagram legend entry: " + symbol)
        allowed = {
            "flowchart": {"process", "decision", "document", "data", "terminator", "subprocess", "predefined", "connector", "preparation", "display", "paper", "delay", "manual", "actor", "datastore", "flow_arrow", "flow_dashed"},
            "sequence": {"human", "participant", "message", "response", "lost", "crossed", "alternative", "loop", "optional", "note", "order"},
            "state": {"state", "initial", "final", "transition", "note"},
        }.get(context["family"])
        if allowed is not None and symbol not in allowed:
            errors.append("Legend symbol does not belong to " + context["family"] + ": " + symbol)
    return errors


def element(parent, tag, attributes=None, text=None):
    node = ET.SubElement(parent, "{" + SVG + "}" + tag, {k: str(v) for k, v in (attributes or {}).items()})
    node.text = text
    return node


def text(parent, value, x, y, size, color, weight="normal"):
    return element(parent, "text", {"x": x, "y": y, "style": f"font-family:Arial,sans-serif;font-size:{size}px;font-weight:{weight};fill:{color};stroke:none"}, value)


def glyph(parent, symbol, x, y, style):
    group = element(parent, "g", {"transform": f"translate({x},{y})", "data-symbol": symbol})
    role = {"participant": "process", "state": "process", "human": "actor", "note": "decision", "entity": "document"}.get(symbol, symbol)
    fill = style["roles"].get(role, {}).get("fill", style["canvas"]["background"])
    line = style["stroke"]
    shape = {"fill": fill, "stroke": line, "stroke-width": 1.5}
    def rectangle(rx=0):
        return element(group, "rect", {"x": 0, "y": 2, "width": 30, "height": 20, "rx": rx, **shape})
    if symbol in {"flow_arrow", "message", "response", "lost", "crossed", "transition", "flow_dashed", "relationship"}:
        dash = "4 3" if symbol in {"response", "lost", "flow_dashed"} else "none"
        element(group, "path", {"d": "M0 12 H29", "fill": "none", "stroke": line, "stroke-width": 1.5, "stroke-dasharray": dash})
        if symbol in {"lost", "crossed"}:
            element(group, "path", {"d": "M24 7 L31 17 M24 17 L31 7", "stroke": line, "stroke-width": 1.5})
        elif symbol == "relationship":
            element(group, "path", {"d": "M24 12 L31 5 M24 12 L31 19", "stroke": line, "fill": "none"})
        else:
            element(group, "path", {"d": "M23 8 L30 12 L23 16 Z", "fill": line, "stroke": line})
    elif symbol == "human":
        element(group, "circle", {"cx": 15, "cy": 4, "r": 3, **shape})
        element(group, "path", {"d": "M15 7 V16 M7 11 H23 M15 16 L8 24 M15 16 L22 24", "fill": "none", "stroke": line, "stroke-width": 1.5})
    elif symbol in {"initial", "final", "connector", "order"}:
        if symbol in {"initial", "final", "order"}:
            shape["fill"] = line
        element(group, "circle", {"cx": 15, "cy": 12, "r": 8, **shape})
        if symbol == "final":
            element(group, "circle", {"cx": 15, "cy": 12, "r": 11, "fill": "none", "stroke": line})
        if symbol == "order":
            text(group, "1", 11, 17, 13, "#FFFFFF", "bold")
    elif symbol in {"alternative", "loop", "optional"}:
        rectangle()
        element(group, "polygon", {"points":"0,2 20,2 20,10 16,14 0,14", "fill":style["roles"]["subprocess"]["fill"], "stroke":line, "stroke-width":1.5})
        text(group, {"alternative":"alt", "loop":"loop", "optional":"opt"}[symbol], 2, 10, 7, style["text"])
    elif symbol == "decision":
        element(group, "polygon", {"points": "15,0 30,12 15,24 0,12", **shape})
    elif symbol == "data":
        element(group, "polygon", {"points": "6,2 30,2 24,22 0,22", **shape})
    elif symbol == "preparation":
        element(group, "polygon", {"points": "6,2 24,2 30,12 24,22 6,22 0,12", **shape})
    elif symbol == "manual":
        element(group, "polygon", {"points": "0,2 30,2 24,22 6,22", **shape})
    elif symbol in {"document", "paper"}:
        path = "M0 2 H30 V20 C20 14 10 26 0 20 Z" if symbol == "document" else "M0 4 C10 10 20 -2 30 4 V20 C20 14 10 26 0 20 Z"
        element(group, "path", {"d": path, **shape})
    elif symbol == "datastore":
        element(group, "path", {"d": "M0 5 C0 -1 30 -1 30 5 V19 C30 25 0 25 0 19 Z M0 5 C0 11 30 11 30 5", **shape})
    elif symbol == "delay":
        element(group, "path", {"d": "M0 2 H19 A10 10 0 0 1 19 22 H0 Z", **shape})
    elif symbol == "display":
        element(group, "path", {"d": "M6 2 H23 Q35 12 23 22 H6 L0 12 Z", **shape})
    else:
        rectangle(10 if symbol == "terminator" else (4 if symbol in {"state", "actor"} else 0))
        if symbol in {"predefined", "entity"}:
            d = "M5 2 V22 M25 2 V22" if symbol == "predefined" else "M0 9 H30 M0 15 H30"
            element(group, "path", {"d": d, "fill": "none", "stroke": line})
        if symbol in {"alternative", "loop", "optional"}:
            label = {"alternative": "alt", "loop": "loop", "optional": "opt"}[symbol]
            text(group, label, 3, 15, 9, line)
    return group


def frame_svg(root, context, style):
    """Add title, subtitle and a wrapping legend without changing diagram coordinates."""
    view = [float(v) for v in root.attrib["viewBox"].split()]
    if len(view) != 4 or not all(math.isfinite(v) for v in view) or min(view[2:]) <= 0:
        raise ValueError("The rendered SVG needs a usable viewBox.")
    padding, width = 28, max(760, math.ceil(view[2] + 56))
    title_lines = textwrap.wrap(context["title"], width=max(25, int((width - 56) / 14)))
    subtitle_lines = textwrap.wrap(context["subtitle"], width=max(35, int((width - 56) / 8)))
    body_y = 52 + len(title_lines) * 32 + len(subtitle_lines) * 22 + 24
    rows, current, used = [], [], 0
    for symbol, label in context["legend"]:
        item_width = 46 + len(label) * 8 + 24
        if current and used + item_width > width - 56:
            rows.append(current)
            current, used = [], 0
        current.append((symbol, label, used))
        used += item_width
    if current:
        rows.append(current)
    legend_y = body_y + view[3] + 28
    height = math.ceil(legend_y + 30 + len(rows) * 38 + padding)
    contents = ET.Element("{" + SVG + "}g", {"id": "technical-writer-content", "transform": f"translate({(width - view[2]) / 2 - view[0]},{body_y - view[1]})"})
    for child in list(root):
        if child.tag.rsplit("}", 1)[-1] not in {"defs", "style", "title", "desc"}:
            root.remove(child)
            contents.append(child)
    root.append(contents)
    root.set("viewBox", f"0 0 {width} {height}")
    root.set("width", str(width))
    root.set("height", str(height))
    root.set("role", "img")
    root.set("style", re.sub(r"max-width\s*:[^;]+;?", "", root.get("style", "")) + f";max-width:{width}px;color-scheme:light;")
    frame = element(root, "g", {"id": "technical-writer-frame"})
    type_group = element(frame, "g", {"id": "technical-writer-type"})
    text(type_group, context["type"], padding, 42, 14, style["stroke"], "bold")
    title_group = element(frame, "g", {"id": "technical-writer-title", "data-value": context["title"]})
    y = 52 + 24
    for line in title_lines:
        text(title_group, line, padding, y, 24, style["text"], "bold")
        y += 32
    subtitle_group = element(frame, "g", {"id": "technical-writer-subtitle", "data-value": context["subtitle"]})
    for line in subtitle_lines:
        text(subtitle_group, line, padding, y, 15, style["text"])
        y += 22
    legend = element(frame, "g", {"id": "technical-writer-legend"})
    text(legend, "Legend", padding, legend_y, 16, style["text"], "bold")
    for row_index, row in enumerate(rows):
        for symbol, label, offset in row:
            entry = element(legend, "g", {"data-symbol": symbol, "data-label": label})
            entry_y = legend_y + 14 + row_index * 38
            glyph(entry, symbol, padding + offset, entry_y, style)
            text(entry, label, padding + offset + 42, entry_y + 17, 14, style["text"])
    return root


def frame_errors(root, context):
    errors = []
    for identifier, expected in [("type", context["type"]), ("title", context["title"]), ("subtitle", context["subtitle"])]:
        group = root.find(".//{" + SVG + "}g[@id='technical-writer-" + identifier + "']")
        actual = " ".join("".join(node.itertext()) for node in group.findall("{" + SVG + "}text")) if group is not None else ""
        if group is None or actual != expected:
            errors.append("Missing or incorrect visible diagram " + identifier + ".")
    legend = root.find(".//{" + SVG + "}g[@id='technical-writer-legend']")
    if legend is None:
        return errors + ["Missing on-canvas symbol legend."]
    heading = legend.find("{" + SVG + "}text")
    if heading is None or heading.text != "Legend":
        errors.append("The diagram symbol explanations must be headed Legend.")
    for symbol, label in context["legend"]:
        entries = [node for node in legend.findall("{" + SVG + "}g") if node.get("data-symbol") == symbol]
        if len(entries) != 1 or entries[0].get("data-label") != label:
            errors.append("Missing diagram legend entry: " + symbol)
            continue
        visible = entries[0].find("{" + SVG + "}text")
        icon = entries[0].find("{" + SVG + "}g")
        if visible is None or visible.text != label or icon is None or not list(icon):
            errors.append("Legend needs both a visible shape and label: " + symbol)
    return errors
