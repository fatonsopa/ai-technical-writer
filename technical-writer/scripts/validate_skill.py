#!/usr/bin/env python3
"""Static package integrity and evaluation coverage; not a semantic writing grader."""
import argparse
import json
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
T=chr(96)

def blocks(text):
    found=[]; opened=None; body=[]
    for line in text.splitlines():
        m=re.match(r'^\s*('+T+r'{3,}|~{3,})(.*)$',line)
        if opened is None:
            if m:opened=(m[1][0],len(m[1]),m[2].strip());body=[]
        elif m and m[1][0]==opened[0] and len(m[1])>=opened[1] and not m[2].strip():
            found.append((opened[2],'\n'.join(body)));opened=None
        else:body.append(line)
    return found,opened is not None

def validate(root=ROOT):
    root=Path(root);errors=[];warnings=[];main=root/'SKILL.md'
    if not main.exists():return {'valid':False,'errors':['Missing SKILL.md'],'warnings':[]}
    text=main.read_text();header=re.match(r'\A---\n(.*?)\n---\n',text,re.S)
    if not header:errors.append('Missing first frontmatter block')
    else:
        if not re.search(r'^name: technical-writer$',header[1],re.M):errors.append('Invalid skill name')
        d=re.search(r'^description:\s*(.+)$',header[1],re.M)
        if not d or not 1<=len(d[1])<=1024:errors.append('Invalid description')
    refs=sorted((root/'references').glob('*.md'));runtime=[main]+refs+sorted((root/'workflows').glob('*.md'));reachable=set()
    for old in ['reference.md','requirements.md','work_item.md','work_items.md','work-item.md','work-items.md','work item.md','test_execution_log.md']:
        if (root/'references'/old).exists():errors.append('Unexpected retired reference: '+old)
    issue=root/'references/issue.md'
    if issue.exists() and issue.read_text().splitlines()[:1]!=['# Issue']:
        errors.append('Canonical issue guide title must be Issue')
    for p in runtime:
        s=p.read_text()
        if blocks(s)[1]:errors.append('Unclosed code fence: '+str(p.relative_to(root)))
        for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',s):
            target=target.split('#')[0]
            if not target or re.match(r'[a-z]+:',target):continue
            q=(p.parent/target).resolve()
            if not q.is_file():errors.append('Broken local link: '+str(p.relative_to(root))+' -> '+target)
            elif q.parent==(root/'references').resolve():reachable.add(q.name)
        for label,target in re.findall(r'\[([^\]]*)\]\(([^)]+)\)',s):
            if Path(target).name=='issue.md' and re.search(r'\bwork[ _-]?items?\b',label,re.I):
                errors.append('Stale issue link label: '+str(p.relative_to(root)))
        for target in re.findall(T+r'((?:references|workflows)/[a-z_\-]+\.md)'+T,s):
            if not (root/target).is_file():errors.append('Broken runtime path: '+target)
        if p in refs and not re.fullmatch(r'[a-z]+(?:_[a-z]+)*\.md',p.name):errors.append('Invalid reference filename: '+p.name)
        if p in refs and p.name not in ['writing_style.md','visuals.md']:
            for marker in ['## Quality check','Completed example']:
                if marker not in s and not (marker=='Completed example' and 'Completed agent example' in s):errors.append('Missing '+marker+': '+p.name)
            if not re.search(r'^## .*emplate',s,re.M) and not (p.name=='agents_and_skills.md' and len([b for tag,b in blocks(s)[0] if tag=='md' and b.startswith('---')])>=6):errors.append('Missing template/composition: '+p.name)
    for p in refs:
        if p.name not in reachable:errors.append('Unreachable reference: '+p.name)
    for name,required in [('policy.md',['Definitions','Principles']),('technical_standard.md',['Definitions','Principles','Rules','Verification'])]:
        p=root/'references'/name
        if not p.exists():errors.append('Missing governance reference: '+name);continue
        docs=[body for tag,body in blocks(p.read_text())[0] if tag in ['md','markdown']]
        if len(docs)<2:errors.append('Missing governance template/example: '+name);continue
        for label,doc in [('template',docs[0]),('example',docs[-1])]:
            for heading in required:
                m=re.search(r'^## '+heading+r'\s*\n(.*?)(?=^## |\Z)',doc,re.M|re.S)
                if not m or not m[1].strip():errors.append('Missing/empty '+heading+' in '+name+' '+label)
    sdd=root/'references/spec_driven_development.md'
    if sdd.exists():
        docs=[s for tag,s in blocks(sdd.read_text())[0] if '# Filtered results' in s]
        for doc in docs:
            if set(re.findall(r'^- (REQ-\d+):',doc,re.M))!=set(re.findall(r'^\| (REQ-\d+) \|',doc,re.M)):errors.append('SDD acceptance mapping mismatch')
    case_list=[]
    try:
        catalog=json.loads((root/'evals/catalog.json').read_text());coverage=json.loads((root/'evals/coverage.json').read_text())
        case_list=[json.loads(line) for p in sorted((root/'evals/cases').glob('*.jsonl')) for line in p.read_text().splitlines() if line.strip()]
        by_id={c['id']:c for c in case_list}
        if len(by_id)!=len(case_list):errors.append('Duplicate case IDs')
        fields={'id','kind','operation','split','references','requirements','fixture','request','permitted_actions','expected_properties','prohibited','grading'}
        for c in case_list:
            if not fields<=c.keys():errors.append('Incomplete case: '+c.get('id','?'));continue
            if not (root/'evals'/c['fixture']).is_file():errors.append('Missing fixture: '+c['id'])
            for ref in c['references']:
                if not (root/ref).is_file():errors.append('Missing eval reference: '+c['id']+' -> '+ref)
        covered=set(catalog['shared_references'])
        for item in catalog['output_kinds']:
            covered.add(item['reference'])
            for op in coverage['required_operations']:
                ids=coverage['output_kinds'].get(item['id'],{}).get(op,[])
                if not ids or any(i not in by_id or by_id[i]['operation']!=op or by_id[i]['kind']!=item['id'] for i in ids):errors.append('Missing operation coverage: '+item['id']+'/'+op)
        for p in refs:
            if 'references/'+p.name not in covered:errors.append('Missing reference eval coverage: '+p.name)
    except (OSError,ValueError,KeyError,TypeError) as error:errors.append('Invalid evaluation manifest: '+str(error))
    sizes={str(p.relative_to(root)):{'bytes':p.stat().st_size,'words':len(p.read_text().split()),'tokens_estimate':round(len(p.read_text())/4)} for p in runtime}
    for name,info in sizes.items():
        budget=11264 if name=='SKILL.md' else (14336 if name.endswith('writing_style.md') else 8192)
        if info['bytes']>budget:warnings.append(name+' exceeds role budget; inspect useful content and selective loading')
    return {'valid':not errors,'errors':errors,'warnings':warnings,'reference_count':len(refs),'case_count':len(case_list),'sizes':sizes,'limits':'Static integrity/coverage only. Semantic quality and host behavior need separate evaluation. Tokens estimated as characters/4.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--root',type=Path,default=ROOT)
    result=validate(parser.parse_args().root);print(json.dumps(result,indent=2));raise SystemExit(not result['valid'])
