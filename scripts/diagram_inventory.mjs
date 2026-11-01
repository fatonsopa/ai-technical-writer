// Read actual parser objects, including implicit nodes; do not infer coverage from comments.
import {readFileSync} from 'node:fs';
import {runtime} from './mermaid_runtime.mjs';

try {
  const {mermaid, version} = await runtime(process.argv[2]);
  const source = readFileSync(0, 'utf8');
  const diagram = await mermaid.mermaidAPI.getDiagramFromText(source);
  const family = ({'flowchart-v2':'flowchart', flowchart:'flowchart', stateDiagram:'state', 'stateDiagram-v2':'state'})[diagram.type] || diagram.type;
  const db = diagram.db;
  const overrides = new Map();
  for (const match of source.matchAll(/^\s*%%\s*Reference:\s*([^|\n]+)\|\s*([^\n]+)$/gmi)) {
    const id=match[1].trim();
    if (overrides.has(id)) throw new Error('Duplicate special-symbol reference: '+id);
    overrides.set(id, match[2].trim());
  }
  const elements = [], links = [];
  const label = value => {
    if (typeof value !== 'string') throw new Error('Unsupported parser label type; add a verified adapter.');
    return value.replace(/<br\s*\/?\s*>/gi,' ').replace(/\s+/g,' ').trim();
  };
  if (family === 'sequence') {
    for (const [id, actor] of db.getActors()) elements.push({id, kind:actor.type === 'actor'?'actor':'participant', label:label(actor.description)});
    for (const [index, message] of db.getMessages().entries()) {
      if (typeof message.message !== 'string' || !message.message.trim()) continue;
      const kind = message.type === 2 ? 'note' : message.from && message.to ? 'message' : 'fragment';
      const text = label(message.message);
      elements.push({id:'message-'+index, kind, label:kind==='fragment'?'['+text+']':text});
      if (message.from && message.to) links.push({from:message.from,to:message.to,type:message.type,label:text});
    }
  } else if (typeof db.getData === 'function') {
    const data = db.getData();
    const groups = typeof db.getSubGraphs === 'function' ? new Map(db.getSubGraphs().map(group=>[group.id,group])) : new Map();
    if (!Array.isArray(data.nodes) || !Array.isArray(data.edges)) throw new Error('Unsupported parser inventory; add a verified adapter for '+diagram.type);
    for (const node of data.nodes) {
      if (node.shape==='noteGroup' || node.isGroup && !label(node.label || '').trim()) continue;
      const special = node.shape==='stateStart'?'initial':node.shape==='stateEnd'?'final':null;
      const name = special ? overrides.get(node.id) : label(node.label || node.id);
      if (special && !name) throw new Error('Add %% Reference: '+node.id+' | NUMBER. LABEL for the special state symbol.');
      if (special) overrides.delete(node.id);
      elements.push({id:node.id,kind:special || (node.shape==='note'?'note':family==='state'?'state':'node'),label:name,shape:node.shape,group:!!node.isGroup,classes:node.isGroup ? (groups.get(node.id)?.classes || []) : (node.cssClasses || '').split(/\s+/).filter(Boolean)});
    }
    for (const edge of data.edges) {
      const text=label(edge.label || '');
      links.push({from:edge.start,to:edge.end,label:text,type:edge.type || edge.arrowTypeEnd || ''});
      if (family==='state' && text) elements.push({id:edge.id,kind:'transition',label:text});
    }
  } else {
    throw new Error('No verified component adapter for '+diagram.type+' in Mermaid '+version+'. Keep the output a draft or use a suitable exporter.');
  }
  if (overrides.size) throw new Error('References name nonexistent or non-special components: '+[...overrides.keys()].join(', '));
  process.stdout.write(JSON.stringify({schema_version:1,version,family,elements,links}));
} catch (error) {
  process.stdout.write(JSON.stringify({error:String(error)}));
  process.exitCode=2;
}
