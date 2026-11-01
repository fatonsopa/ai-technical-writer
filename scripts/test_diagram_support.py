"""Authored XML/inspection controls for unit tests; not real render evidence."""
import json
import xml.etree.ElementTree as ET
import render_diagram as diagram

NS = "{" + diagram.SVG + "}"
AUDIT = {"kind":"browser_observation", "passed":True, "browser":"AUTHORED UNIT CONTROL", "errors":[], "provenance":"Authored data for unit control only; not an actual browser observation."}
SEQUENCE_ELEMENTS = [{"id":str(i), "kind":kind,"label":label} for i,kind,label in [(1,"actor","1. Administrator"),(2,"participant","2. Websites page"),(3,"message","3. Save category"),(4,"message","4. Saved")]]
FLOW_ELEMENTS = [{"id":"A","kind":"node","label":"1. Choose category","shape":"squareRect","classes":["process"]},{"id":"B","kind":"node","label":"2. Valid?","shape":"diamond","classes":["decision"]}]

def manifest(family, elements):
    return {"schema_version":1,"version":"AUTHORED UNIT CONTROL","family":family,"elements":elements,"links":[]}

def raw_svg(elements):
    root=ET.Element(NS+"svg",{"viewBox":"0 0 600 300"})
    body=ET.SubElement(root,NS+"g",{"id":"drawing"})
    classes={"actor":"actor","participant":"actor","message":"messageText","fragment":"loopText","note":"noteText","transition":"edgeLabel"}
    for index,row in enumerate(elements):
        node=ET.SubElement(body,NS+"text",{"x":"20","y":str(25+index*25),"class":classes.get(row["kind"],"nodeLabel")});node.text=row["label"]
    return ET.tostring(root,encoding="unicode")

def control_export(source, family="sequence", elements=None):
    elements=elements or SEQUENCE_ELEMENTS
    svg=diagram.add_canvas(raw_svg(elements),source,diagram.load_style(),manifest(family,elements))
    return diagram.finish_export(svg,AUDIT,[{"phase":phase,"evidence":"AUTHORED UNIT CONTROL"} for phase in ("inventory","render","inspect")])

def table(elements):
    return "| Component | Explanation |\n| --- | --- |\n"+"".join("| "+row["label"]+" | Authored explanation control for this component. |\n" for row in elements)
