#!/usr/bin/env python3
"""Validate source registry and materialized arXiv/GitHub artifacts."""
from __future__ import annotations
import hashlib, json, re, sys
from datetime import datetime, timezone
from pathlib import Path
import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT=Path(__file__).resolve().parents[1]; RAW=ROOT/'raw_data'; OUT=ROOT/'materialized_sources'; REG=ROOT/'source_registry'
def load(p): return yaml.safe_load(p.read_text(encoding='utf-8'))
def digest(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def front(p):
    t=p.read_text(encoding='utf-8'); m=re.match(r'^---\n(.*?)\n---\n',t,re.S)
    if not m: raise ValueError('missing or unclosed frontmatter')
    d=yaml.safe_load(m.group(1));
    if not isinstance(d,dict): raise ValueError('frontmatter must be a mapping')
    return d
def main():
    errors=[]; warnings=[]; counts={'registry_entries':0,'manifests':0,'arxiv':0,'github':0,'wiki_pages':0,'hashes':0}
    rp=REG/'registry.yaml'
    if not rp.exists(): errors.append('missing source_registry/registry.yaml')
    else:
        r=load(rp); entries=r.get('entries',[]) if isinstance(r,dict) else []; counts['registry_entries']=len(entries)
        u=[x.get('uid') for x in entries if isinstance(x,dict)]; dup=sorted({x for x in u if u.count(x)>1})
        errors += [f'duplicate registry uid: {x}' for x in dup]
    wp=RAW/'schemas/wiki_page.schema.yaml'; wv=Draft202012Validator(load(wp),format_checker=FormatChecker())
    for mp in sorted(OUT.glob('*/*/manifest.yaml')):
        counts['manifests']+=1; d=load(mp); typ=d.get('source_type'); status=d.get('status'); root=mp.parent
        if status=='failed': warnings.append(f'failed materialization: {mp.relative_to(ROOT)}'); continue
        if typ=='arxiv':
            counts['arxiv']+=1; fp=root/'files.jsonl'; sp=root/'selectors.jsonl'
            if not fp.exists() or not sp.exists(): errors.append(f'missing arxiv index: {root.relative_to(ROOT)}'); continue
            for line in fp.read_text(encoding='utf-8').splitlines():
                if not line: continue
                x=json.loads(line); p=root/'source'/x['path']
                if not p.exists(): errors.append(f'missing file: {p.relative_to(ROOT)}')
                elif digest(p)!=x['sha256']: errors.append(f'hash mismatch: {p.relative_to(ROOT)}')
                else: counts['hashes']+=1
            for line in sp.read_text(encoding='utf-8').splitlines():
                if line:
                    x=json.loads(line)
                    if not (root/'source'/x['file']).exists(): errors.append(f'broken selector: {x.get("selector")}')
        elif typ=='github':
            counts['github']+=1
            for p in [root/'evidence/files.jsonl',root/'evidence/excerpts.jsonl',root/'wiki/index.md']:
                if not p.exists(): errors.append(f'missing repo capsule artifact: {p.relative_to(ROOT)}')
            for p in sorted((root/'wiki').glob('*.md')):
                counts['wiki_pages']+=1
                try: d=front(p)
                except Exception as e: errors.append(f'{p.relative_to(ROOT)}: {e}'); continue
                for e in wv.iter_errors(d): errors.append(f'{p.relative_to(ROOT)} at {"/".join(map(str,e.path))}: {e.message}')
            ep=root/'evidence/excerpts.jsonl'
            if ep.exists():
                for line in ep.read_text(encoding='utf-8').splitlines():
                    if line:
                        x=json.loads(line); q=ROOT/x['local_path']
                        if not q.exists(): errors.append(f'broken excerpt reference: {x["local_path"]}')
        else: errors.append(f'unsupported materialization type: {typ}')
    report={'validation_id':'materialization-validation-2026-09-09','generated_at':datetime.now(timezone.utc).replace(microsecond=0).isoformat(),'status':'passed' if not errors else 'failed','counts':counts,'warnings':warnings,'errors':errors,'interpretation':'Structural integrity only; this does not prove scientific truth or repository runtime behavior.'}
    ap=RAW/'audits/materialization_validation_2026-09-09.yaml'; ap.parent.mkdir(parents=True,exist_ok=True); ap.write_text(yaml.safe_dump(report,sort_keys=False,allow_unicode=True),encoding='utf-8')
    print('materialization_validation',counts,'warnings',len(warnings),'errors',len(errors))
    for x in warnings: print('WARNING',x)
    for x in errors: print('ERROR',x)
    return 1 if errors else 0
if __name__=='__main__': sys.exit(main())
