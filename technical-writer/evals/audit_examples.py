#!/usr/bin/env python3
import argparse, concurrent.futures, importlib.util, json, tempfile
from pathlib import Path
parser=argparse.ArgumentParser(description='Audit complete authored examples in separate read-only model contexts. This reviews examples; it does not generate documents or execute the source application.')
parser.add_argument('--model',required=True)
parser.add_argument('--out',type=Path,required=True)
parser.add_argument('--document',action='append',help='Example filename, repeatable; defaults to the full collection.')
args=parser.parse_args()
root=Path(__file__).resolve().parents[2];spec=importlib.util.spec_from_file_location('runner',root/'technical-writer/evals/run.py');runner=importlib.util.module_from_spec(spec);spec.loader.exec_module(runner)
examples=root/'technical-writer/examples';out=args.out.resolve();out.mkdir(parents=True,exist_ok=True)
context={'user_scope':'These are teaching examples. User authorized realistic invented details and requested finished documents without labels distinguishing original project details from additions. Do not require such labels or treat stated example statuses/results as claims that the author executed the application. The audit itself must not claim application execution.','requirements':(examples/'spec_driven_development.md').read_text(),'test_specification':(examples/'test_specification.md').read_text(),'evidence_baseline':{'candidate1':'R1, wr-candidate-1, isolated staging, 2026-10-28 09:00-16:00 UTC; T01-T09 pass, T10 fail retained selection, T11-T14 pass, T15 blocked journal failure injection, T16 pass, T17 fail stale counts, T18-T19 not run, T20 pass; 15/2/1/2; 17 executed','candidate2':'R2, wr-candidate-2, isolated staging, 2026-10-29 09:00-15:00 UTC; complete rerun T01-T20 all pass; no deployment or release approval recorded','incident':'Staging partial-write display incident during R1, first500 committed, next500 rejected, last1 unattempted, stale counts until reload. Fixed invalidation in candidate2. No production outage.'},'authority':'The SDD controls intended example behavior. Designs can supply technical details consistent with it; product and governance examples may establish explicit example roles. No fixed-length requirement. Examples must demonstrate the substance of their own document type, not repeat every other document.'}
paths=sorted(examples.glob('*.md'))
if args.document:
 names=set(args.document)
 if names-{p.name for p in paths}:parser.error('Unknown example filename')
 paths=[p for p in paths if p.name in names]
def audit(start):
 batch=paths[start:start+6];target=out/('batch-%02d'%start)
 if (target/'record.json').exists(): raise RuntimeError('Preserve previous results')
 with tempfile.TemporaryDirectory(prefix='worked-example-audit-') as d:
  work=Path(d);packet={'context':context,'writing_style':(root/'technical-writer/references/writing_style.md').read_text(),'documents':[{'id':p.stem,'guide':(root/'technical-writer/references'/p.name).read_text(),'content':p.read_text()} for p in batch]};(work/'packet.json').write_text(json.dumps(packet))
  prompt='Read packet.json. Independently audit each complete authored document against its guide, writing_style, and shared context. These are user-authorized teaching examples, not model-generated evaluation outputs. Return seven 0-3 scores for grounding within example context, meaning/obligations, type completeness, usefulness/depth, natural connected language, scope, and cross-document traceability. A 2 is usable with minor correction; 3 meets the request; 1 needs material correction; 0 unusable. Report concrete supported issues in reasons. Flag material contradictory requirements, arithmetic, misleading transaction or permission behavior, broken document structure, or missing essential information as critical_failures. Do not demand arbitrary length or irrelevant sections. Evaluate drafts honestly without requiring every design to be implemented. Read only local packet.json; do not write or use network. Return each document id once.'
  record=runner.invoke(work,target,prompt,args.model,grading=True)
 if record['status']=='completed' and (len(record['results'])!=len(batch) or {x['id'] for x in record['results']}!={p.stem for p in batch}):record.update(status='infrastructure_error',error='Audit output IDs differ from requested examples')
 for x in record.get('results',[]):x['passed']=len(x['scores'])==7 and min(x['scores'])>=2 and not x['critical_failures']
 record['input_kind']='Author-written worked examples; independent model audit, not independent generation or human review';(target/'record.json').write_text(json.dumps(record,indent=2)+'\n');return target.name,record['status'],[(x['id'],x['passed']) for x in record.get('results',[])]
with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
 for value in pool.map(audit,range(0,len(paths),6)):print(json.dumps(value),flush=True)
