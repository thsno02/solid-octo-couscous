#!/usr/bin/env python3
"""Migrate source metadata and materialize arXiv/GitHub sources.

GitHub repositories are frozen at a commit and converted into a semantic capsule;
the repository itself is never vendored. Generated wiki pages are candidates.
"""
from __future__ import annotations
import argparse, gzip, hashlib, io, json, re, shutil, subprocess, tarfile, tempfile, time
import urllib.parse, urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
import yaml

ROOT=Path(__file__).resolve().parents[1]; RAW=ROOT/'raw_data'; OUT=ROOT/'materialized_sources'; REG=ROOT/'source_registry'
UA='solid-octo-couscous-materializer/1.0 (+https://github.com/thsno02/solid-octo-couscous)'
TEXT={'.tex','.ltx','.bib','.bbl','.sty','.cls','.bst','.def','.txt','.md','.rst','.json','.yaml','.yml','.toml','.ini','.cfg','.py','.sh','.r','.js','.ts','.go','.rs','.html','.xml'}
DIRTYPE={'arxiv':'arxiv','biorxiv':'biorxiv','journal':'journal','paper':'paper','standard':'standard','methodology':'methodology','industry':'industry_doc','blog':'blog','githubs':'github','dataset':'dataset','benchmark':'benchmark','incident':'incident','x':'x'}

def load(p): return yaml.safe_load(p.read_text(encoding='utf-8'))
def dump(x): return yaml.safe_dump(x,sort_keys=False,allow_unicode=True,width=110)
def write(p,x): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(dump(x),encoding='utf-8')
def sha(b): return hashlib.sha256(b).hexdigest()
def key(s):
    t='ZZSLASHZZ'; s=str(s).replace('/',t); s=re.sub(r'[^A-Za-z0-9._-]+','-',s); s=re.sub(r'-+','-',s).strip('-._'); return s.replace(t,'--') or 'item'
def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def stype(p,d): return str(d.get('source_type') or d.get('source') or DIRTYPE.get(p.relative_to(RAW).parts[0],p.relative_to(RAW).parts[0])).lower().replace('-','_')
def cid(t,d):
    v=d.get('canonical_id') or ({'arxiv':d.get('arxiv_id'),'biorxiv':d.get('doi'),'github':d.get('repo')}.get(t)) or d.get('doi') or d.get('id')
    return re.sub(r'v\d+$','',str(v)) if v and t=='arxiv' else (str(v) if v else None)
def curl(url):
    req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'*/*'}); err=None
    for n in range(4):
        try:
            with urllib.request.urlopen(req,timeout=90) as r: return r.read(),r.geturl(),dict(r.headers)
        except Exception as e: err=e; time.sleep(2**n)
    raise RuntimeError(f'{url}: {err}')
def run(cmd,cwd=None,timeout=600,bytes_out=False):
    r=subprocess.run(cmd,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=timeout,check=False)
    if r.returncode: raise RuntimeError(r.stderr.decode(errors='replace')[-3000:])
    return r.stdout if bytes_out else r.stdout.decode(errors='replace')

def ensure_schema():
    p=RAW/'schemas/item.schema.yaml'; d=load(p); e=d['properties']['source_type']['enum']
    if 'biorxiv' not in e: e.insert(1,'biorxiv'); write(p,d)

def migrate(date):
    changed=0
    for p in sorted(RAW.rglob('metadata.yaml')):
        d=load(p)
        if not isinstance(d,dict): continue
        t=stype(p,d); c=cid(t,d); title=str(d.get('title') or d.get('repo') or p.parent.name)
        url=d.get('canonical_url') or d.get('url') or (f'https://arxiv.org/abs/{c}' if t=='arxiv' and c else f'https://github.com/{c}' if t=='github' and c else f'https://doi.org/{c}' if c and (d.get('doi') or t=='biorxiv') else None)
        if not url: url='https://github.com/thsno02/solid-octo-couscous/blob/main/'+urllib.parse.quote(p.relative_to(ROOT).as_posix(),safe='/')
        before=dump(d)
        d.setdefault('uid',f'{t}:{c or key(title)}'); d.setdefault('source_type',t)
        if c: d.setdefault('canonical_id',c)
        d.setdefault('title',title); d.setdefault('canonical_url',str(url))
        a=d.get('authors') or d.get('maintainer') or []
        if isinstance(a,str): a=[a]
        d.setdefault('authors_or_maintainers',a)
        d.setdefault('publisher_or_owner',d.get('journal') or d.get('publisher') or d.get('maintainer'))
        if 'dates' not in d:
            first=d.get('submitted') or d.get('published') or d.get('year')
            d['dates']={'first_published':str(first) if first is not None else None,'last_updated':None,'retrieved_at':str(d.get('snapshot_date') or date)}
        if not isinstance(d.get('verification'),dict): d['verification']={'state':'pending','checked_at':date,'method':'structural-migration-only','evidence_url':str(url),'notes':'Canonical facts were not reverified by this migration.'}
        d.setdefault('versioning',{'source_version':None,'snapshot_commit':None,'release_or_tag':None,'content_sha256':None,'previous_versions':[]})
        d.setdefault('rights',{'license_spdx':d.get('license'),'license_verified_at':None,'access':'unknown','notes':'Requires canonical rights verification.'})
        tags=d.get('tags') or d.get('category') or ['unclassified']; tags=[tags] if isinstance(tags,str) else [str(x) for x in tags]
        d.setdefault('classification',{'domains':tags[:8] or ['unclassified'],'evolution_objects':['implementation' if t=='github' else 'source-record'],'loop_roles':['retention'],'research_lifecycle':[]})
        d.setdefault('linkage',{'papers':[],'repositories':[],'datasets':[],'benchmarks':[],'standards':[],'methodologies':[],'predecessors':[],'successors':[]})
        d.setdefault('evidence',{'level':'unknown','replication_status':'not_checked','primary_source':t in {'arxiv','biorxiv','journal','standard','github'},'known_contradictions':[]})
        d.setdefault('governance',{'provenance_preserved':'partial','reversible':'unknown','evaluator_independence':'unknown','risks':['legacy-metadata-not-fully-reverified'],'promotion_requirements':['canonical-source-validation']})
        rel=str(d.get('relevance') or 'adjacent').lower(); rel=rel if rel in {'foundational','direct','adjacent','governance','infrastructure'} else 'adjacent'
        d.setdefault('collection',{'priority':'P0' if rel in {'foundational','direct','governance'} else 'P1','relevance':rel,'inclusion_reason':str(d.get('why_collected') or d.get('knowledge_evolution_link') or 'Legacy record retained during schema migration.'),'exclusions_or_limits':['legacy-classification-may-be-coarse'],'collector':'materialization-migration-2026-09-09','query_or_seed':None})
        if dump(d)!=before: write(p,d); changed+=1
    print('migrated',changed)

def metapaths():
    m={}
    for p in RAW.rglob('metadata.yaml'):
        d=load(p)
        if isinstance(d,dict):
            t=stype(p,d); c=cid(t,d)
            if c: m[(t,c.lower())]=p.relative_to(ROOT).as_posix()
    return m

def unpack(payload):
    try:
        with tarfile.open(fileobj=io.BytesIO(payload),mode='r:*') as a:
            return [(x.name,a.extractfile(x).read()) for x in a.getmembers() if x.isfile() and x.size<10_000_000][:3000],'tar'
    except tarfile.TarError: pass
    try: data=gzip.decompress(payload)
    except OSError: return [('main.tex',payload)],'single'
    try:
        with tarfile.open(fileobj=io.BytesIO(data),mode='r:*') as a: return [(x.name,a.extractfile(x).read()) for x in a.getmembers() if x.isfile() and x.size<10_000_000][:3000],'gzip-tar'
    except tarfile.TarError: return [('main.tex',data)],'gzip-single'

def arxiv(a,mp,ts):
    aid=str(a['id']); root=OUT/'arxiv'/key(aid); shutil.rmtree(root,ignore_errors=True); (root/'source').mkdir(parents=True)
    payload=url=headers=None; errs=[]
    for u in [f'https://export.arxiv.org/e-print/{urllib.parse.quote(aid,safe="/")}',f'https://arxiv.org/e-print/{urllib.parse.quote(aid,safe="/")}']:
        try: payload,url,headers=curl(u); break
        except Exception as e: errs.append(str(e))
    if payload is None:
        d={'manifest_version':1,'source_type':'arxiv','canonical_id':aid,'status':'failed','generated_at':ts,'metadata_path':mp.get(('arxiv',aid.lower())),'errors':errs}; write(root/'manifest.yaml',d); return d
    files=[]; selectors=[]; main=None; total=0; omitted=[]; bundle,kind=unpack(payload)
    for name,raw in bundle:
        pp=PurePosixPath(name.replace('\\','/'))
        if pp.is_absolute() or '..' in pp.parts: omitted.append({'path':name,'reason':'unsafe'}); continue
        parts=[x for x in pp.parts if x not in {'','.'}]; pp=PurePosixPath(*parts) if parts else None
        if not pp or pp.suffix.lower() not in TEXT or len(raw)>5_000_000 or total+len(raw)>20_000_000: omitted.append({'path':name,'reason':'filtered'}); continue
        text=raw.decode('utf-8',errors='replace'); q=root/'source'/pp.as_posix(); q.parent.mkdir(parents=True,exist_ok=True); q.write_text(text,encoding='utf-8'); total+=len(raw)
        lines=text.splitlines(); files.append({'path':pp.as_posix(),'sha256':sha(q.read_bytes()),'line_count':len(lines),'size':q.stat().st_size})
        selectors.append({'selector':f'arxiv://{aid}@latest/{pp.as_posix()}#L1-L{len(lines)}','file':pp.as_posix(),'start_line':1,'end_line':len(lines),'kind':'file'})
        for i,line in enumerate(lines,1):
            mm=re.search(r'\\(section|subsection|subsubsection)\*?\{([^{}]+)\}',line)
            if mm: selectors.append({'selector':f'arxiv://{aid}@latest/{pp.as_posix()}#L{i}','file':pp.as_posix(),'start_line':i,'end_line':i,'kind':mm.group(1),'heading':mm.group(2)})
        if pp.suffix.lower() in {'.tex','.ltx'} and '\\documentclass' in text and (main is None or pp.name.lower()=='main.tex'): main=pp.as_posix()
    for name,data in [('files.jsonl',files),('selectors.jsonl',selectors)]:
        with (root/name).open('w',encoding='utf-8') as f:
            for x in data: f.write(json.dumps(x,ensure_ascii=False,sort_keys=True)+'\n')
    if main: (root/'normalized').mkdir(); shutil.copyfile(root/'source'/main,root/'normalized/main.tex')
    (root/'SOURCE_MAP.md').write_text(f'# arXiv source map: {aid}\n\n- Main TeX: `{main}`\n- Files: {len(files)}\n- Archive SHA-256: `{sha(payload)}`\n',encoding='utf-8')
    d={'manifest_version':1,'source_type':'arxiv','canonical_id':aid,'status':'materialized' if main else 'partial','generated_at':ts,'metadata_path':mp.get(('arxiv',aid.lower())),'download':{'resolved_url':url,'archive_sha256':sha(payload),'archive_bytes':len(payload),'container_kind':kind,'archive_retained':False},'materialization':{'root':root.relative_to(ROOT).as_posix(),'main_tex':main,'stored_text_files':len(files),'stored_text_bytes':total,'selector_count':len(selectors),'omitted_members':len(omitted),'text_only':True},'omitted':omitted[:200],'warnings':errs}; write(root/'manifest.yaml',d); return d

def front(repo,commit,title,slug,page_type,summary,ts):
    x={'uid':f'wiki-page:repo-{key(repo.lower())}-{slug}-{commit[:12]}','title':title,'slug':f'repos/{key(repo.lower())}/{slug}','page_type':page_type,'status':'review','summary':summary[:500],'aliases':[],'ontology_refs':['github-repository'],'claim_refs':[],'source_refs':[f'github:{repo}@{commit}'],'page_refs':[],'outgoing_links':[],'sections':[],'temporal':{'created_at':ts,'updated_at':ts,'valid_from':None,'valid_to':None,'as_of':ts},'provenance':{'build_id':f'repo-capsule:{key(repo)}:{commit[:12]}','generated_by_agent':'scripts/materialize_pipeline.py','generated_by_model':None,'prompt_or_skill_version':'deterministic-repo-capsule-v1','compiled_from_revisions':[f'github:{repo}@{commit}'],'created_at':ts,'updated_at':ts,'manual_edits_preserved':True},'review':{'state':'automated_checks_only','reviewers':[],'decision_ref':None,'checked_claim_refs':[],'unresolved_issues':['Requires semantic review.']},'freshness':{'status':'fresh','checked_at':ts,'max_age_days':30,'source_dependencies':[f'github:{repo}@{commit}'],'staleness_reasons':[]},'consumption':{'audiences':['human','agent'],'summary_tiers':{'one_line':summary[:300],'short':summary[:500],'full':None},'estimated_tokens':None,'machine_entry_points':['../manifest.yaml','../evidence/files.jsonl','../evidence/excerpts.jsonl']}}
    return '---\n'+dump(x)+'---\n\n'
def repo(r,mp,ts):
    name=str(r['repo']); root=OUT/'github'/key(name); shutil.rmtree(root,ignore_errors=True); (root/'evidence/excerpts').mkdir(parents=True); (root/'wiki').mkdir(parents=True)
    with tempfile.TemporaryDirectory() as td:
        rd=Path(td)/'r'
        try:
            run(['git','clone','--filter=blob:none','--no-checkout','--depth','1',f'https://github.com/{name}.git',str(rd)]); commit=run(['git','rev-parse','HEAD'],rd).strip(); tree=run(['git','ls-tree','-r','-l','HEAD'],rd)
        except Exception as e:
            d={'manifest_version':1,'source_type':'github','canonical_id':name,'status':'failed','generated_at':ts,'metadata_path':mp.get(('github',name.lower())),'errors':[str(e)]}; write(root/'manifest.yaml',d); return d
        rec=[]
        for line in tree.splitlines():
            m=re.match(r'^(\d+)\s+(\w+)\s+([0-9a-f]{40})\s+(-|\d+)\t(.+)$',line)
            if m: rec.append({'mode':m.group(1),'type':m.group(2),'blob_sha':m.group(3),'size':None if m.group(4)=='-' else int(m.group(4)),'path':m.group(5)})
        with (root/'evidence/files.jsonl').open('w') as f:
            for x in rec: f.write(json.dumps(x,sort_keys=True)+'\n')
        cand=[]
        for x in rec:
            p=x['path']; n=PurePosixPath(p).name.lower(); ext=PurePosixPath(p).suffix.lower(); depth=len(PurePosixPath(p).parts)
            pri=0 if n.startswith('readme') and depth==1 else 1 if n in {'agents.md','claude.md','architecture.md','design.md','contributing.md','security.md'} else 2 if p.lower().startswith('docs/') and ext in {'.md','.rst','.txt'} else 3 if n in {'pyproject.toml','package.json','go.mod','cargo.toml','requirements.txt','dockerfile','makefile'} else 9
            if pri<9 and x['size'] is not None and x['size']<300000: cand.append((pri,depth,p,x))
        cand=sorted(cand)[:int(r.get('max_evidence_files',80))]; texts={}; excerpts=[]
        for _,_,p,x in cand:
            raw=run(['git','show',f'{commit}:{p}'],rd,bytes_out=True); text=raw.decode('utf-8',errors='replace'); texts[p]=text; lines=text.splitlines()[:int(r.get('max_excerpt_lines',500))]
            local=root/'evidence/excerpts'/(key(p)+'-'+x['blob_sha'][:8]+'.txt'); local.write_text('\n'.join(lines)+'\n',encoding='utf-8')
            excerpts.append({'path':p,'blob_sha':x['blob_sha'],'selector':f'repo://{name}@{commit}/{p}#L1-L{len(lines)}','local_path':local.relative_to(ROOT).as_posix(),'truncated':len(lines)<len(text.splitlines()),'content_sha256':sha(local.read_bytes())})
        with (root/'evidence/excerpts.jsonl').open('w') as f:
            for x in excerpts: f.write(json.dumps(x,sort_keys=True)+'\n')
        readme=next((p for p in texts if PurePosixPath(p).name.lower().startswith('readme')),''); rt=texts.get(readme,''); lines=rt.splitlines(); desc=next((re.sub(r'\s+',' ',x.strip()) for x in lines if x.strip() and not x.lstrip().startswith(('#','<','!','[','|','---'))),'Repository semantic capsule.')
        tops=Counter(PurePosixPath(x['path']).parts[0] for x in rec); langs=Counter(PurePosixPath(x['path']).suffix.lower() for x in rec if PurePosixPath(x['path']).suffix)
        ov=front(name,commit,f'{name} — repository overview','overview','system',desc,ts)+f'# {name}\n\n{desc}\n\n- Frozen commit: `{commit}`\n- Files: {len(rec)}\n- Evidence excerpts: {len(excerpts)}\n\n## README outline\n'
        for i,l in enumerate(lines,1):
            if re.match(r'^#{1,6}\s+',l): ov+=f'- {l.lstrip("# ")} — `repo://{name}@{commit}/{readme}#L{i}`\n'
        (root/'wiki/overview.md').write_text(ov,encoding='utf-8')
        ar=front(name,commit,f'{name} — architecture','architecture','system',f'Structural view of {name}.',ts)+'# Architecture\n\n## Top-level paths\n\n'+'\n'.join(f'- `{k}`: {v} files' for k,v in tops.most_common(40))+'\n\n## Extension profile\n\n'+'\n'.join(f'- `{k or "none"}`: {v}' for k,v in langs.most_common(30))+'\n\nDirectory structure is not proof of runtime behavior.\n'; (root/'wiki/architecture.md').write_text(ar,encoding='utf-8')
        ops=front(name,commit,f'{name} — interfaces and operations','interfaces-and-operations','method',f'Candidate operating surface of {name}.',ts)+'# Interfaces and operations\n\n'; code=False
        for i,l in enumerate(lines,1):
            if l.strip().startswith('```'): code=not code; continue
            if code and l.strip() and len(l.strip())<220: ops+=f'- `{l.strip()}` — `repo://{name}@{commit}/{readme}#L{i}`\n'
        (root/'wiki/interfaces-and-operations.md').write_text(ops+'\nCommands are syntactically extracted and unverified.\n',encoding='utf-8')
        idx=front(name,commit,f'{name} — semantic capsule index','index','map',f'Navigation for {name}.',ts)+'# Semantic capsule\n\n- [Overview](overview.md)\n- [Architecture](architecture.md)\n- [Interfaces and operations](interfaces-and-operations.md)\n\n## Evidence\n\n- `../evidence/files.jsonl`\n- `../evidence/excerpts.jsonl`\n'; (root/'wiki/index.md').write_text(idx,encoding='utf-8')
        d={'manifest_version':1,'source_type':'github','canonical_id':name,'status':'materialized','generated_at':ts,'metadata_path':mp.get(('github',name.lower())),'source_revision':{'repository':name,'commit':commit,'clone_url':f'https://github.com/{name}.git'},'materialization':{'root':root.relative_to(ROOT).as_posix(),'file_records':len(rec),'selected_evidence_files':len(excerpts),'repo_contents_vendored':False},'semanticization':{'backend':'deterministic-repo-capsule-v1','state':'candidate','llm_used':False,'wiki_pages':['wiki/index.md','wiki/overview.md','wiki/architecture.md','wiki/interfaces-and-operations.md'],'limitations':['Selected excerpts only','No runtime execution','Requires semantic review']}}; write(root/'manifest.yaml',d); return d

def registry(ts):
    entries=[]
    for p in sorted(RAW.rglob('metadata.yaml')):
        d=load(p)
        if not isinstance(d,dict): continue
        t=stype(p,d); c=cid(t,d); uid=str(d.get('uid')); k=key(c or uid); mr=OUT/t/k/'manifest.yaml'; state='not_materialized'
        if mr.exists(): state=str(load(mr).get('status','partial'))
        adapter='arxiv_latex' if t=='arxiv' else 'github_repo_wiki' if t=='github' else 'web_article' if t in {'blog','x'} else 'structured_reference' if t in {'standard','ontology','methodology','industry_doc'} else 'scholarly_document'
        entries.append({'uid':uid,'source_type':t,'canonical_id':c,'title':d.get('title'),'canonical_url':d.get('canonical_url'),'metadata_path':p.relative_to(ROOT).as_posix(),'verification_state':(d.get('verification') or {}).get('state','pending'),'priority':(d.get('collection') or {}).get('priority','watch'),'adapter':{'name':adapter,'semanticization_required':t=='github'},'materialization':{'state':state,'root':(OUT/t/k).relative_to(ROOT).as_posix(),'manifest':mr.relative_to(ROOT).as_posix() if mr.exists() else None}})
    REG.mkdir(exist_ok=True); write(REG/'registry.yaml',{'registry_version':1,'generated_at':ts,'repository':'thsno02/solid-octo-couscous','entry_count':len(entries),'entries':entries})
    with (REG/'registry.jsonl').open('w') as f:
        for x in entries: f.write(json.dumps(x,ensure_ascii=False,sort_keys=True)+'\n')
    (REG/'README.md').write_text('# Source registry\n\nGenerated adapter and materialization index. GitHub repositories require `github_repo_wiki`; a repository URL is not a consumable document.\n',encoding='utf-8')

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--config',default='pipeline/materialization.yaml'); a=ap.parse_args(); cfg=load(ROOT/a.config); ts=str(cfg.get('generated_at') or now()); ensure_schema(); migrate('2026-09-09'); mp=metapaths(); results=[]
    for x in cfg.get('arxiv',{}).get('items',[]): print('arxiv',x['id'],flush=True); results.append(arxiv(x,mp,ts)); time.sleep(cfg.get('arxiv',{}).get('delay_seconds',2))
    for x in cfg.get('github',{}).get('items',[]): print('github',x['repo'],flush=True); results.append(repo(x,mp,ts))
    OUT.mkdir(exist_ok=True); write(OUT/'index.yaml',{'materialization_index_version':1,'generated_at':ts,'summary':dict(Counter(str(x.get('status')) for x in results)),'items':[{'source_type':x.get('source_type'),'canonical_id':x.get('canonical_id'),'status':x.get('status'),'manifest':f"materialized_sources/{x.get('source_type')}/{key(x.get('canonical_id'))}/manifest.yaml"} for x in results]}); (OUT/'README.md').write_text('# Materialized sources\n\nSource-specific frozen artifacts. arXiv stores TeX and selectors; GitHub stores commit-pinned semantic capsules, not repository contents.\n',encoding='utf-8'); registry(ts); usable=sum(x.get('status') in {'materialized','partial'} for x in results); print('materialized',usable,'of',len(results)); return 0 if usable>=int(cfg.get('minimum_usable_items',1)) else 1
if __name__=='__main__': raise SystemExit(main())
