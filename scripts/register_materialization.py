#!/usr/bin/env python3
from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]; P=ROOT/'raw_data/index.yaml'
def add(items,record,key='path'):
    for i,x in enumerate(items):
        if x.get(key)==record.get(key): items[i]=record; return
    items.append(record)
d=yaml.safe_load(P.read_text(encoding='utf-8')); d['index_version']=max(int(d.get('index_version',0)),4); d['updated_at']='2026-09-09'
c=list(d.get('collections') or []); add(c,{'path':'collections/source_consumption_adapters.yaml','scope':'source-specific-materialization-and-consumption','version':1}); d['collections']=c
a=list(d.get('audits') or []); add(a,{'path':'audits/materialization_validation_2026-09-09.yaml','status':'current'}); d['audits']=a
docs=list(d.get('documentation') or []); add(docs,{'repo_path':'docs/260909-collection/10-materialization-and-consumption.md','scope':'source adapters, registry and materialization'},'repo_path'); add(docs,{'repo_path':'docs/llm-wiki/14-source-specific-consumption.md','scope':'LLM Wiki source-specific consumption'},'repo_path'); d['documentation']=docs
d['generated_artifacts']=[{'repo_path':'source_registry/registry.yaml','role':'source identity, adapter and materialization registry'},{'repo_path':'materialized_sources/index.yaml','role':'materialized source manifest index'}]
rules=list(d.get('consumer_rules') or [])
for r in ['Select a source-specific adapter before consumption; a canonical URL alone is not a consumable artifact.','A GitHub repository must be frozen at a commit and semanticized into a repo-wiki capsule before LLM Wiki use.','Direct TeX is preferred for arXiv; PDF is a fallback that must retain page selectors.','Deterministic repository capsules are review candidates, not verified runtime descriptions.']:
    if r not in rules: rules.append(r)
d['consumer_rules']=rules
P.write_text(yaml.safe_dump(d,sort_keys=False,allow_unicode=True,width=110),encoding='utf-8')
print('registered materialization artifacts')
