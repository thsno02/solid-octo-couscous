#!/usr/bin/env python3
"""Compile atomic claim, source, and domain-map pages."""
from __future__ import annotations

from collections import defaultdict
from typing import Any

from llm_wiki_common import *

def build_atomic_pages(sources: list[dict[str, Any]], claims: list[dict[str, Any]], evidence: list[dict[str, Any]], snapshot: dict[str, Any]) -> dict[str, Any]:
    by_uid = {str(item["uid"]): item for item in claims}; ev = {str(item["uid"]): item for item in evidence}; srow = {str(item["uid"]): item for item in sources}
    titles = {uid: text(row.get("title")) or text(row.get("canonical_id")) or uid for uid, row in srow.items()}
    by_source: dict[str, list[dict[str, Any]]] = defaultdict(list); by_domain: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for claim in claims:
        for ref in srcs(claim): by_source[ref].append(claim)
        by_domain[cdomain(claim)].append(claim)
    claim_paths = {uid: f"claims/{slug(uid)}.md" for uid in by_uid}; claim_page_ids = {uid: f"wiki-page:evidence-{h(uid)}" for uid in by_uid}
    source_paths = {uid: f"sources/{slug(uid)}.md" for uid in srow}; source_page_ids = {uid: f"wiki-page:source-{h(uid)}" for uid in srow}
    domains = sorted(set(by_domain) | {text(item.get("domain")) or "cross-cutting" for item in sources})
    map_paths = {d: f"maps/{d}.md" for d in domains}; map_ids = {d: f"wiki-page:map-{d}" for d in domains}
    pages: list[dict[str, Any]] = []

    for uid, claim in sorted(by_uid.items()):
        refs = srcs(claim); rows = []
        for eid in evrefs(claim):
            p = prop(ev.get(eid, {})); rows.append(f"| `{eid}` | `{p.get('selector')}` | `{p.get('local_path')}` | `{p.get('content_tier')}` |")
        body = f"""# {text(claim.get('identity', {}).get('labels', ['Candidate claim'])[0])}\n\n> **Candidate only.** This page exposes one atomic claim and its evidence bindings.\n\n## Candidate statement\n\n{ctext(claim)}\n\n## Scope\n\n- Claim ID: `{uid}`\n- Scope: `{cscope(claim) or 'unspecified'}`\n- Domain: {link(claim_paths[uid], map_paths[cdomain(claim)], cdomain(claim))}\n- Promotion state: `{claim.get('governance', {}).get('promotion_state')}`\n\n## Evidence bindings\n\n| Evidence | Selector | Local artifact | Tier |\n|---|---|---|---|\n{chr(10).join(rows) if rows else '| none | none | none | none |'}\n\n## Review requirements\n\nCheck entailment, selector precision, source quality, identity, scope, contradiction, and due weight before promotion."""
        p = page(claim_paths[uid], claim_page_ids[uid], f"Claim {uid.split(':', 1)[-1]}", "evidence", ctext(claim)[:220] or f"Evidence expansion for {uid}.", body)
        p["claims"] = [uid]; p["rendered_claims"] = [uid]; p["sources"] = refs; p["sections"] = [{"heading": "Candidate statement", "claim_refs": [uid], "source_refs": refs, "editorial_intent": "Expose the exact candidate statement."}, {"heading": "Evidence bindings", "claim_refs": [uid], "source_refs": refs, "editorial_intent": "Resolve to local selectors."}]
        for ref in refs:
            if ref in source_page_ids: add(p, source_page_ids[ref], "evidenced_by", [uid])
        add(p, map_ids[cdomain(claim)], "part_of", [uid]); pages.append(p)

    for uid, row in sorted(srow.items(), key=lambda item: titles[item[0]].lower()):
        rows = sorted(by_source.get(uid, []), key=lambda item: str(item["uid"])); rep = [x for x in rows if reported(x)]; assess = [x for x in rows if not reported(x)]
        def bullets(items: list[dict[str, Any]]) -> str:
            return "\n".join(f"- {ctext(x)[:420]} 〔{link(source_paths[uid], claim_paths[str(x['uid'])], str(x['uid']))}〕" for x in items) or "- None recorded."
        e_rows = []
        for claim in rows:
            for eid in evrefs(claim):
                pp = prop(ev.get(eid, {})); e_rows.append(f"| `{claim['uid']}` | `{eid}` | `{pp.get('selector')}` | `{pp.get('content_tier')}` |")
        domain = text(row.get("domain")) or (cdomain(rows[0]) if rows else "cross-cutting")
        body = f"""# {titles[uid]}\n\n> Source-oriented candidate page. Source statements and collector interpretation remain separate.\n\n## Source identity\n\n- Source UID: `{uid}`\n- Canonical ID: `{row.get('canonical_id')}`\n- Source type: `{row.get('source_type')}`\n- Content tier: `{row.get('content_tier')}`\n- Revision: `{row.get('revision') or 'unknown'}`\n- Domain: {link(source_paths[uid], map_paths[domain], domain)}\n- Local document: `{row.get('local_document')}`\n\n## Source-reported candidate statements\n\n{bullets(rep)}\n\n## Collection assessments\n\n{bullets(assess)}\n\n## Evidence inventory\n\n| Claim | Evidence | Selector | Tier |\n|---|---|---|---|\n{chr(10).join(e_rows) if e_rows else '| none | none | none | none |'}\n\n## Governance boundary\n\nSource statements remain unverified candidates. Collection assessments explain inclusion but are not source-authored scientific evidence."""
        p = page(source_paths[uid], source_page_ids[uid], titles[uid], "source", f"Source page for {titles[uid]} with claim/evidence expansion.", body)
        p["claims"] = [str(x["uid"]) for x in rows]; p["rendered_claims"] = list(p["claims"]); p["sources"] = [uid]; p["sections"] = [{"heading": "Source-reported candidate statements", "claim_refs": [str(x["uid"]) for x in rep], "source_refs": [uid], "editorial_intent": "Represent source statements."}, {"heading": "Collection assessments", "claim_refs": [str(x["uid"]) for x in assess], "source_refs": [uid], "editorial_intent": "Keep collector interpretation separate."}]
        add(p, map_ids[domain], "part_of", p["claims"])
        for cid in p["claims"]: add(p, claim_page_ids[cid], "evidenced_by", [cid])
        pages.append(p)

    for domain in domains:
        rows = sorted(by_domain.get(domain, []), key=lambda item: str(item["uid"])); refs = unique(ref for item in rows for ref in srcs(item)); rep = [x for x in rows if reported(x)]; assess = [x for x in rows if not reported(x)]
        desc, questions = DOMAINS.get(domain, ("Cross-domain candidate knowledge pending a more specific module.", ["What stable question should organize this material?"]))
        roster = "\n".join(f"| {link(map_paths[domain], source_paths[ref], titles.get(ref, ref))} | `{srow[ref].get('source_type')}` | `{srow[ref].get('content_tier')}` | {len(by_source.get(ref, []))} |" for ref in refs if ref in source_paths)
        body = f"""# {domain.replace('-', ' ').title()}\n\n{desc}\n\n## Routing questions\n\n{chr(10).join('- ' + q for q in questions)}\n\n## Source coverage\n\n| Source | Type | Tier | Claims |\n|---|---|---|---|\n{roster or '| none | none | none | 0 |'}\n\n## Source-reported signals\n\n{signals(rep, map_paths[domain], claim_paths, titles)}\n\n## Collector assessments\n\n{signals(assess, map_paths[domain], claim_paths, titles)}\n\n## Current synthesis boundary\n\nThe map routes candidate evidence; it does not flatten sources into consensus or resolve contradictions automatically."""
        p = page(map_paths[domain], map_ids[domain], domain.replace("-", " ").title(), "map", f"Routing map for {domain.replace('-', ' ')} sources, questions, and claims.", body)
        p["claims"] = [str(x["uid"]) for x in rows]; p["rendered_claims"] = list(p["claims"]); p["sources"] = refs; p["sections"] = [{"heading": "Source coverage", "claim_refs": [], "source_refs": refs, "editorial_intent": "Route by source family."}, {"heading": "Source-reported signals", "claim_refs": [str(x["uid"]) for x in rep], "source_refs": unique(ref for x in rep for ref in srcs(x)), "editorial_intent": "Preserve source-authored scope."}, {"heading": "Collector assessments", "claim_refs": [str(x["uid"]) for x in assess], "source_refs": unique(ref for x in assess for ref in srcs(x)), "editorial_intent": "Preserve collector scope."}]
        for ref in refs:
            if ref in source_page_ids: add(p, source_page_ids[ref], "explains", [str(x["uid"]) for x in by_source.get(ref, [])])
        pages.append(p)
    return {
        "sources": sources, "claims": claims, "evidence": evidence,
        "by_uid": by_uid, "ev": ev, "srow": srow, "titles": titles,
        "by_source": by_source, "by_domain": by_domain,
        "claim_paths": claim_paths, "claim_page_ids": claim_page_ids,
        "source_paths": source_paths, "source_page_ids": source_page_ids,
        "domains": domains, "map_paths": map_paths, "map_ids": map_ids,
        "pages": pages,
    }
