#!/usr/bin/env python3
"""Build the v0 meta knowledge-base demo from local materialized capsules."""
from __future__ import annotations

import hashlib
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable

import yaml

from rights_propagation import (
    CLAIM_TRANSFORMATION,
    CLAIM_USE,
    DECLARED,
    EVIDENCE_TRANSFORMATION,
    EVIDENCE_USE,
    UNAVAILABLE,
    make_rights_ref,
    page_rights_payload,
    rights_markdown,
    rights_snapshot,
)

EXPERIMENT_ROOT = Path(__file__).resolve().parents[1]
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_materialization_completeness import pdf_primary_excerpt_range, validate_pdf_supplement
from validate_publication_rights import validate_pdf_supplement_rights
CONFIG_PATH = EXPERIMENT_ROOT / "config.yaml"
MATERIALIZED_INDEX = ROOT / "materialized_sources" / "index.yaml"
KNOWLEDGE_SCHEMA = ROOT / "raw_data" / "schemas" / "knowledge_model.schema.yaml"
WIKI_PAGE_SCHEMA = ROOT / "raw_data" / "schemas" / "wiki_page.schema.yaml"

GENERATED_DIRS = [
    "00_inputs",
    "01_ontology",
    "02_entities",
    "03_evidence",
    "04_claims",
    "05_wiki",
    "06_evaluation",
    "07_review",
    "08_release",
]

DOMAIN_RULES = [
    ("recursive-self-improvement", ("recursive", "godel", "self-improv", "self-modif", "rsi", "intelligence explosion")),
    ("open-ended-evolution", ("open-ended", "evolution", "quality diversity", "map-elites", "poet", "novelty", "population")),
    ("automated-research", ("research agent", "ai scientist", "scientific discovery", "autonomous research", "paperbench", "laboratory", "storm")),
    ("knowledge-memory", ("memory", "retrieval", "rag", "knowledge graph", "graphiti", "hipporag", "zep", "lightrag")),
    ("knowledge-editing", ("knowledge editing", "model editing", "continual learning", "lifelong", "catastrophic forgetting", "memit", "rome")),
    ("ontology-semantic-architecture", ("ontology", "semantic", "schema", "shacl", "owl", "linkml", "mapping", "provenance", "wikidata")),
    ("llm-wiki", ("llm wiki", "wiki", "wikigen", "mediawiki", "wikibase", "factuality", "citation")),
    ("governance-evaluation", ("governance", "evaluation", "benchmark", "verification", "policy", "rollback", "audit", "truth maintenance")),
]


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def dump_yaml(value: Any) -> str:
    return yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=110)


def write_yaml(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump_yaml(value), encoding="utf-8")


def write_jsonl(path: Path, rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def safe_slug(value: str) -> str:
    value = value.lower().replace("/", "--").replace(":", "-")
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-._")
    return value or "item"


def short_hash(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()[:16]


def reset_generated() -> None:
    for name in GENERATED_DIRS:
        shutil.rmtree(EXPERIMENT_ROOT / name, ignore_errors=True)
        (EXPERIMENT_ROOT / name).mkdir(parents=True, exist_ok=True)


def metadata_for(item: dict[str, Any]) -> dict[str, Any]:
    manifest = load_yaml(ROOT / str(item["manifest"]))
    metadata_path = manifest.get("metadata_path") if isinstance(manifest, dict) else None
    if isinstance(metadata_path, str) and (ROOT / metadata_path).exists():
        metadata = load_yaml(ROOT / metadata_path)
        if isinstance(metadata, dict):
            return metadata
    return {}


def domain_bucket(item: dict[str, Any], metadata: dict[str, Any]) -> str:
    terms: list[str] = [str(item.get("title") or ""), str(item.get("canonical_id") or "")]
    classification = metadata.get("classification") if isinstance(metadata.get("classification"), dict) else {}
    domains = classification.get("domains") if isinstance(classification.get("domains"), list) else []
    tags = metadata.get("tags")
    if isinstance(tags, list):
        terms.extend(str(tag) for tag in tags)
    elif isinstance(tags, str):
        terms.append(tags)
    terms.extend(str(domain) for domain in domains)
    text = " ".join(terms).lower()
    scores: list[tuple[int, str]] = []
    for name, keywords in DOMAIN_RULES:
        # Acronyms are words, not arbitrary substrings: RSI is not "version",
        # OWL is not "knowledge", and RAG is not "paragraph".
        score = sum(
            1 for keyword in keywords
            if re.search(r"\b" + re.escape(keyword) +
                         ("" if keyword in {"self-improv", "self-modif"} else r"\b"), text)
        )
        if score:
            scores.append((score, name))
    if not scores:
        return "cross-cutting"
    scores.sort(reverse=True)
    return scores[0][1]


def source_priority(item: dict[str, Any], metadata: dict[str, Any]) -> tuple[int, int, str]:
    collection = metadata.get("collection") if isinstance(metadata.get("collection"), dict) else {}
    priority = str(collection.get("priority") or metadata.get("priority") or "P2")
    priority_rank = {"P0": 0, "P1": 1, "P2": 2, "watch": 3}.get(priority, 4)
    tier_rank = {"full_text": 0, "semantic_capsule": 1, "excerpt_capsule": 2}.get(str(item.get("content_tier")), 9)
    return priority_rank, tier_rank, str(item.get("title") or "")


def select_sources(items: list[dict[str, Any]], config: dict[str, Any]) -> list[dict[str, Any]]:
    allowed = set(config.get("content_tiers_allowed") or [])
    candidates = [item for item in items if item.get("content_tier") in allowed
                  and item.get("content_tier") != "metadata_capsule"
                  and item.get("status") != "metadata_only"]
    metadata_cache = {str(item["uid"]): metadata_for(item) for item in candidates}
    preferred = [str(value).lower() for value in config.get("preferred_sources") or []]
    selected: list[dict[str, Any]] = []
    selected_uids: set[str] = set()

    for preference in preferred:
        for item in candidates:
            if str(item.get("uid", "")).lower() == preference or str(item.get("canonical_id", "")).lower() == preference:
                uid = str(item["uid"])
                if uid not in selected_uids:
                    selected.append(item)
                    selected_uids.add(uid)
                break

    buckets: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in candidates:
        if str(item["uid"]) in selected_uids:
            continue
        metadata = metadata_cache[str(item["uid"])]
        buckets[domain_bucket(item, metadata)].append(item)
    for bucket in buckets.values():
        bucket.sort(key=lambda item: source_priority(item, metadata_cache[str(item["uid"])]))

    maximum = int(config.get("max_selected_sources", 36))
    while len(selected) < maximum and any(buckets.values()):
        for bucket_name in sorted(buckets):
            bucket = buckets[bucket_name]
            if not bucket or len(selected) >= maximum:
                continue
            item = bucket.pop(0)
            selected.append(item)
            selected_uids.add(str(item["uid"]))

    minimum = int(config.get("minimum_selected_sources", 12))
    if len(selected) < minimum:
        raise RuntimeError(f"only {len(selected)} usable sources were available; minimum is {minimum}")
    return selected


def admitted_pdf_supplement(item: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any] | None:
    """Select the optional PDF only after its own audit, local integrity and body check."""
    supplement = manifest.get("pdf_supplement")
    if not isinstance(supplement, dict) or supplement.get("body_quality_verified") is not True:
        return None
    manifest_path = ROOT / str(item["manifest"])
    try:
        audit = load_yaml(ROOT / "raw_data/audits/materialization_rights_review.yaml")
        review = next((row for row in audit["items"] if row.get("uid") == item.get("uid")), None)
        errors, blocked = validate_pdf_supplement_rights(manifest, manifest_path, ROOT, review)
        if errors or blocked:
            return None
        local_files = manifest.get("local_files") or []
        declared = {row["path"] for row in local_files}
        hashes = {row["path"]: row["sha256"] for row in local_files}
        for name in ("document.pdf", "document.txt", "selectors.jsonl", "NOTICE.md"):
            path = manifest_path.parent / "pdf-supplement" / name
            row = next((entry for entry in local_files if entry["path"] == path.relative_to(ROOT).as_posix()), None)
            if row is None or row.get("bytes") != path.stat().st_size or row["sha256"] != hashlib.sha256(path.read_bytes()).hexdigest():
                return None
        validate_pdf_supplement(manifest, manifest_path.parent, declared, hashes, errors, repository_root=ROOT)
        return supplement if not errors else None
    except (KeyError, TypeError, AttributeError, ValueError, OSError, yaml.YAMLError):
        return None


def choose_local_selectors(item: dict[str, Any], manifest: dict[str, Any]) -> Path:
    capsule_root = (ROOT / str(item["manifest"])).parent
    if admitted_pdf_supplement(item, manifest):
        return capsule_root / "pdf-supplement/selectors.jsonl"
    return capsule_root / "selectors.jsonl"


def choose_local_document(item: dict[str, Any], manifest: dict[str, Any]) -> Path | None:
    capsule_root = (ROOT / str(item["manifest"])).parent
    if admitted_pdf_supplement(item, manifest):
        return capsule_root / "pdf-supplement/document.txt"
    candidates = [
        capsule_root / "normalized" / "document.txt",
        capsule_root / "document.md",
        capsule_root / "document.txt",
        capsule_root / "wiki" / "overview.md",
    ]
    materialization = manifest.get("materialization") if isinstance(manifest.get("materialization"), dict) else {}
    document = materialization.get("document")
    if isinstance(document, str):
        candidates.insert(0, capsule_root / document)
    evidence_list = capsule_root / "evidence" / "files.jsonl"
    if evidence_list.exists():
        repository_documents = []
        for line in evidence_list.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            local_path = row.get("local_path")
            if isinstance(local_path, str):
                path = ROOT / local_path
                if path.name.lower().startswith("readme"):
                    repository_documents.append(path)
        # Cite the pinned maintainer file, not our synthetic capsule header.
        candidates = sorted(repository_documents, key=lambda p: (len(p.parts), str(p))) + candidates
    for candidate in candidates:
        if candidate.exists() and candidate.is_file() and candidate.stat().st_size > 0:
            return candidate
    return None


def meaningful_excerpt(text: str, title: str) -> tuple[str, int, int]:
    """Return a contiguous source span and its exact original line interval.

    Offsets are retained before whitespace normalization. No TeX/HTML cleanup
    or noncontiguous sentence joining is allowed to masquerade as a quotation.
    """
    abstract = re.search(
        r"(?im)^\s*(?:#{1,6}\s*)?abstract\s*\n", text
    )
    offset = abstract.end() if abstract else 0
    region = text[offset:]
    for block in re.finditer(r"\S[^\n]*(?:\n(?!\s*\n)[^\n]*)*", region):
        raw = block.group()
        candidate = " ".join(raw.split())
        if raw.lstrip().startswith(("---", "#", "- ", ">", "<", "```", "!", "[", "\\")):
            continue
        if len(re.findall(r"[A-Za-z]{3,}", candidate)) < 12 or len(candidate) < 80:
            continue
        if not re.search(r"[.!?。！？](?:\s|$)", candidate):
            continue
        tokens = list(re.finditer(r"\S+", raw))
        # Keep a prefix of at most two sentences, capped at 700 characters.
        ends = list(re.finditer(r"(?<=[.!?。！？])\s+", candidate))
        length = ends[min(1, len(ends) - 1)].start() if ends else len(candidate)
        excerpt = candidate[:min(length, 700)].rstrip()
        consumed = 0
        last = tokens[0]
        for token in tokens:
            last = token
            consumed += len(token.group())
            if consumed >= len(excerpt):
                break
            consumed += 1
        origin = offset + block.start()
        start = text.count("\n", 0, origin + tokens[0].start()) + 1
        end = text.count("\n", 0, origin + last.end()) + 1
        return excerpt, start, end
    # Absence of quotable prose is not evidence for a source assertion.
    return "", 1, 1


def source_excerpt(
    text: str, title: str, pdf_supplement: dict[str, Any] | None = None,
) -> tuple[str, int, int]:
    """Preserve the old quotation logic, with a parent-paper boundary for new PDFs."""
    if pdf_supplement is None:
        return meaningful_excerpt(text, title)
    start, end = pdf_primary_excerpt_range(pdf_supplement, text)
    excerpt, local_start, local_end = meaningful_excerpt("\n".join(text.splitlines()[start - 1:end]), title)
    return excerpt, start - 1 + local_start, start - 1 + local_end


def inclusion_reason(metadata: dict[str, Any]) -> str:
    return inclusion_reason_field(metadata)[1]


def inclusion_reason_field(metadata: dict[str, Any]) -> tuple[str, str]:
    collection = metadata.get("collection") if isinstance(metadata.get("collection"), dict) else {}
    for field, value in (
        ("collection.inclusion_reason", collection.get("inclusion_reason")),
        ("why_collected", metadata.get("why_collected")),
        ("knowledge_evolution_link", metadata.get("knowledge_evolution_link")),
        ("summary", metadata.get("summary")),
    ):
        if isinstance(value, str) and value.strip():
            return field, re.sub(r"\s+", " ", value).strip()
    raise ValueError("source metadata has no collection assessment field")


def knowledge_object(
    *,
    uid: str,
    kind: str,
    label: str,
    source_refs: list[str],
    recorded_at: str,
    properties: dict[str, Any],
    assertion_kind: str = "not-applicable",
    evidence_refs: list[str] | None = None,
    status: str = "candidate",
    promotion_state: str = "candidate",
    method: str,
    source_version: str | None = None,
    source_hash: str | None = None,
) -> dict[str, Any]:
    return {
        "uid": uid,
        "kind": kind,
        "identity": {
            "stable_id": uid,
            "labels": [label],
            "aliases": [],
            "external_ids": {},
            "identity_criteria": None,
            "merge_lineage": [],
            "split_lineage": [],
        },
        "semantics": {
            "ontology_refs": ["experiment:meta-kb-v0"],
            "type_refs": [kind],
            "world_assumption": "open",
            "asserted_or_inferred": "asserted" if kind in {"Claim", "Evidence", "Source"} else "not-applicable",
            "property_assertions": properties,
            "constraint_refs": [],
        },
        "epistemic": {
            "assertion_kind": assertion_kind,
            "confidence": None,
            "uncertainty_type": None,
            "evidence_refs": evidence_refs or [],
            "contradiction_refs": [],
            "derivation_method": method,
            "calibration_record": None,
        },
        "temporal": {
            "valid_from": None,
            "valid_to": None,
            "observed_at": None,
            "recorded_at": recorded_at,
            "superseded_at": None,
            "temporal_reference_system": "UTC",
            "precision": "second",
        },
        "provenance": {
            "source_refs": source_refs,
            "agent_refs": ["agent:deterministic-v0-builder"],
            "activity_ref": "activity:v0-meta-kb-build-260910",
            "method": method,
            "source_version": source_version,
            "source_hash": source_hash,
            "generated_by_model": None,
            "recorded_at": recorded_at,
        },
        "governance": {
            "owner": "experiment:v0_meta_kb_initialization_demo_260910",
            "policy_refs": ["policy:proposal-review-merge"],
            "permissions": ["read", "review"],
            "review_status": "proposed",
            "promotion_state": promotion_state,
            "reviewer_refs": [],
        },
        "versioning": {
            "version": "0.1",
            "predecessor_ref": None,
            "change_set_ref": "changeset:v0-meta-kb-initialization-260910",
            "semantic_diff_ref": None,
            "compatibility_class": "backward-compatible",
            "migration_ref": None,
            "impact_assessment_ref": None,
            "rollback_ref": "rollback:v0-meta-kb-initialization-260910",
        },
        "status": status,
    }


def wiki_frontmatter(
    *,
    uid: str,
    title: str,
    slug: str,
    page_type: str,
    summary: str,
    claim_refs: list[str],
    source_refs: list[str],
    generated_at: str,
    build_id: str,
    rendered_claim_refs: list[str] | None = None,
    rights_refs: list[dict[str, Any]] | None = None,
    rights_unavailable_source_refs: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "uid": uid,
        "title": title,
        "slug": slug,
        "page_type": page_type,
        "status": "review",
        "summary": summary[:500],
        "aliases": [],
        "ontology_refs": ["experiment:meta-kb-v0"],
        "claim_refs": claim_refs,
        "rendered_claim_refs": rendered_claim_refs or [],
        "source_refs": source_refs,
        "rights_refs": rights_refs or [],
        "rights_unavailable_source_refs": rights_unavailable_source_refs or [],
        "page_refs": [],
        "outgoing_links": [],
        "sections": [],
        "temporal": {
            "created_at": generated_at,
            "updated_at": generated_at,
            "valid_from": None,
            "valid_to": None,
            "as_of": generated_at,
        },
        "provenance": {
            "build_id": build_id,
            "generated_by_agent": "agent:deterministic-v0-builder",
            "generated_by_model": None,
            "prompt_or_skill_version": "deterministic-v0.1",
            "compiled_from_revisions": source_refs,
            "created_at": generated_at,
            "updated_at": generated_at,
            "manual_edits_preserved": False,
        },
        "review": {
            "state": "needs_human",
            "reviewers": [],
            "decision_ref": None,
            "checked_claim_refs": [],
            "unresolved_issues": ["Scientific and semantic review required before publication."],
        },
        "freshness": {
            "status": "fresh",
            "checked_at": generated_at,
            "max_age_days": 30,
            "source_dependencies": source_refs,
            "staleness_reasons": [],
        },
        "consumption": {
            "audiences": ["human", "agent"],
            "summary_tiers": {"one_line": summary[:220], "short": summary[:500], "full": None},
            "estimated_tokens": None,
            "machine_entry_points": ["../../04_claims/claims.jsonl", "../../03_evidence/evidence.jsonl"],
        },
    }


def write_wiki_page(path: Path, frontmatter: dict[str, Any], body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("---\n" + dump_yaml(frontmatter) + "---\n\n" + body.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    config = load_yaml(CONFIG_PATH)
    index = load_yaml(MATERIALIZED_INDEX)
    if not isinstance(config, dict) or not isinstance(index, dict):
        raise SystemExit("configuration or materialized source index is invalid")
    items = index.get("items")
    if not isinstance(items, list):
        raise SystemExit("materialized source index has no items")

    selected = select_sources(items, config)
    generated_at = str(index.get("generated_at") or "")
    if not generated_at:
        raise SystemExit("materialized source index has no pinned generated_at")
    # The existing build identity is derived from inputs, not wall-clock time.
    input_paths = {CONFIG_PATH, MATERIALIZED_INDEX, Path(__file__),
                   Path(__file__).with_name("validate_demo.py"),
                   Path(__file__).with_name("evidence_validation.py"),
                   Path(__file__).with_name("rights_propagation.py"),
                   KNOWLEDGE_SCHEMA, WIKI_PAGE_SCHEMA}
    for item in selected:
        manifest_path = ROOT / str(item["manifest"])
        source_manifest = load_yaml(manifest_path)
        input_paths.update({manifest_path, ROOT / source_manifest["metadata_path"]})
        document = choose_local_document(item, source_manifest)
        if document:
            input_paths.add(document)
        if source_manifest.get("pdf_supplement"):
            input_paths.add(ROOT / "raw_data/audits/materialization_rights_review.yaml")
            input_paths.add(choose_local_selectors(item, source_manifest))
    digest = hashlib.sha256()
    for path in sorted(input_paths):
        digest.update(path.relative_to(ROOT).as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    build_id = f"build:v0-meta-kb-260910:{digest.hexdigest()[:16]}"
    reset_generated()

    metadata_cache: dict[str, dict[str, Any]] = {}
    selected_rows: list[dict[str, Any]] = []
    evidence_objects: list[dict[str, Any]] = []
    claim_objects: list[dict[str, Any]] = []
    source_entities: list[dict[str, Any]] = []
    claims_by_domain: dict[str, list[dict[str, Any]]] = defaultdict(list)
    source_page_records: list[dict[str, Any]] = []

    for item in selected:
        uid = str(item["uid"])
        metadata = metadata_for(item)
        metadata_cache[uid] = metadata
        manifest_path = ROOT / str(item["manifest"])
        manifest = load_yaml(manifest_path)
        if not isinstance(manifest, dict):
            continue
        local_document = choose_local_document(item, manifest)
        use_pdf = local_document == manifest_path.parent / "pdf-supplement/document.txt"
        representation = manifest["pdf_supplement"] if use_pdf else manifest
        consumed_item = {**item, "revision": representation.get("revision")} if use_pdf else item
        if use_pdf:
            consumed_item["source_representation"] = "pdf_supplement"
        declared_rights = rights_snapshot(representation.get("rights"))
        source_for_rights = {
            **consumed_item,
            "rights": declared_rights,
            "rights_status": DECLARED if declared_rights else UNAVAILABLE,
        }
        domain = domain_bucket(item, metadata)
        limited_evidence = item.get("status") == "partial" or item.get("content_tier") == "excerpt_capsule"
        evidence_role = ("bounded-excerpt" if limited_evidence else
                         "static-repository-evidence" if item.get("source_type") == "github" else "source-text")
        excerpt = ""
        start_line = 1
        end_line = 1
        local_path: str | None = None
        if local_document is not None:
            text = local_document.read_text(encoding="utf-8", errors="replace")
            excerpt, start_line, end_line = source_excerpt(
                text, str(item.get("title") or uid), representation if use_pdf else None,
            )
            local_path = local_document.relative_to(ROOT).as_posix()

        source_hash = None
        local_files = manifest.get("local_files") if isinstance(manifest.get("local_files"), list) else []
        if local_path:
            for local_file in local_files:
                if isinstance(local_file, dict) and local_file.get("path") == local_path:
                    source_hash = local_file.get("sha256")
                    break
        if source_hash is None and local_path:
            source_hash = hashlib.sha256((ROOT / local_path).read_bytes()).hexdigest()

        source_entity_uid = f"source:{short_hash(uid)}"
        source_entities.append(
            knowledge_object(
                uid=source_entity_uid,
                kind="Source",
                label=str(item.get("title") or uid),
                source_refs=[uid],
                recorded_at=generated_at,
                properties={
                    "source_uid": uid,
                    "canonical_id": item.get("canonical_id"),
                    "source_type": item.get("source_type"),
                    "content_tier": item.get("content_tier"),
                    "manifest": item.get("manifest"),
                    "domain": domain,
                    "rights_status": source_for_rights["rights_status"],
                    **({"rights": declared_rights} if declared_rights else {}),
                },
                method="materialized-source-registration",
                source_version=str(consumed_item.get("revision") or "unknown"),
                source_hash=source_hash,
                status="active",
                promotion_state="candidate",
            )
        )

        claim_refs: list[str] = []
        rendered_claim_refs: list[str] = []
        if excerpt and local_path:
            evidence_uid = f"evidence:{short_hash(uid + ':source-excerpt')}"
            claim_uid = f"claim:{short_hash(uid + ':source-assertion')}"
            selector = f"local://{local_path}#L{start_line}-L{end_line}"
            evidence_rights_ref = make_rights_ref(
                source_for_rights,
                usage=EVIDENCE_USE,
                transformation=EVIDENCE_TRANSFORMATION,
            )
            evidence_rights = (
                {"rights_refs": [evidence_rights_ref]}
                if evidence_rights_ref
                else {"rights_unavailable_source_refs": [uid]}
            )
            evidence_objects.append(
                knowledge_object(
                    uid=evidence_uid,
                    kind="Evidence",
                    label=f"Evidence excerpt for {item.get('title')}",
                    source_refs=[uid],
                    recorded_at=generated_at,
                    properties={
                        "local_path": local_path,
                        "selector": selector,
                        "excerpt": excerpt,
                        "excerpt_sha256": hashlib.sha256(excerpt.encode("utf-8")).hexdigest(),
                        "content_tier": item.get("content_tier"),
                        "evidence_role": evidence_role,
                        **evidence_rights,
                    },
                    assertion_kind="observation",
                    method="deterministic-local-excerpt",
                    source_version=str(consumed_item.get("revision") or "unknown"),
                    source_hash=source_hash,
                    status="active",
                    promotion_state="candidate",
                )
            )
            claim = knowledge_object(
                uid=claim_uid,
                kind="Claim",
                label=f"Source assertion from {item.get('title')}",
                source_refs=[uid],
                recorded_at=generated_at,
                properties={
                    "text": excerpt,
                    "claim_scope": "source-reported assertion",
                    "domain": domain,
                    "subject_ref": source_entity_uid,
                    "limitations": (["Only the locally retained excerpt is evidence; omitted source content was not reviewed."] if limited_evidence else []) + (representation.get("limitations", []) if use_pdf else []),
                    **(
                        {
                            "rights_refs": [
                                make_rights_ref(
                                    source_for_rights,
                                    usage=CLAIM_USE,
                                    transformation=CLAIM_TRANSFORMATION,
                                )
                            ]
                        }
                        if declared_rights
                        else {"rights_unavailable_source_refs": [uid]}
                    ),
                },
                assertion_kind="assertion",
                evidence_refs=[evidence_uid],
                method="source-assertion-extraction-without-model",
                source_version=str(consumed_item.get("revision") or "unknown"),
                source_hash=source_hash,
            )
            claim_objects.append(claim)
            claims_by_domain[domain].append(claim)
            claim_refs.append(claim_uid)
            rendered_claim_refs.append(claim_uid)

        assessment_field, assessment_text = inclusion_reason_field(metadata)
        assessment_evidence_uid = f"evidence:{short_hash(uid + ':collection-metadata')}"
        assessment_claim_uid = f"claim:{short_hash(uid + ':collection-assessment')}"
        assessment_selector = f"local://{manifest.get('metadata_path')}#{assessment_field}"
        evidence_objects.append(
            knowledge_object(
                uid=assessment_evidence_uid,
                kind="Evidence",
                label=f"Collection metadata for {item.get('title')}",
                source_refs=[uid],
                recorded_at=generated_at,
                properties={
                    "local_path": manifest.get("metadata_path"),
                    "selector": assessment_selector,
                    "excerpt": assessment_text,
                    "excerpt_sha256": hashlib.sha256(assessment_text.encode("utf-8")).hexdigest(),
                    "content_tier": "metadata_capsule",
                },
                assertion_kind="observation",
                method="collection-metadata-read",
                source_version=None,
                source_hash=None,
                status="active",
                promotion_state="candidate",
            )
        )
        assessment_claim = knowledge_object(
            uid=assessment_claim_uid,
            kind="Claim",
            label=f"Collection assessment for {item.get('title')}",
            source_refs=[uid],
            recorded_at=generated_at,
            properties={
                "text": assessment_text,
                "claim_scope": "collector assessment, not source-authored scientific fact",
                "domain": domain,
                "subject_ref": source_entity_uid,
            },
            assertion_kind="assertion",
            evidence_refs=[assessment_evidence_uid],
            method="collection-assessment-extraction",
            source_version=None,
            source_hash=None,
        )
        claim_objects.append(assessment_claim)
        claims_by_domain[domain].append(assessment_claim)
        claim_refs.append(assessment_claim_uid)

        selected_row = {
            **consumed_item,
            "domain": domain,
            "metadata_path": manifest.get("metadata_path"),
            "local_document": local_path,
            "claim_refs": claim_refs,
            "rights_status": source_for_rights["rights_status"],
            **({"rights": declared_rights} if declared_rights else {}),
        }
        selected_rows.append(selected_row)
        source_page_records.append(
            {
                "item": item,
                "domain": domain,
                "claim_refs": claim_refs,
                "rendered_claim_refs": rendered_claim_refs,
                "excerpt": excerpt,
                "assessment": assessment_text,
                "local_path": local_path,
            }
        )

    domain_entities: list[dict[str, Any]] = []
    for domain in sorted(claims_by_domain):
        domain_entities.append(
            knowledge_object(
                uid=f"domain:{domain}",
                kind="Concept",
                label=domain.replace("-", " ").title(),
                source_refs=sorted({ref for claim in claims_by_domain[domain] for ref in claim["provenance"]["source_refs"]}),
                recorded_at=generated_at,
                properties={"domain_key": domain, "claim_count": len(claims_by_domain[domain])},
                method="experiment-domain-bucketing",
                status="active",
                promotion_state="candidate",
            )
        )

    write_yaml(
        EXPERIMENT_ROOT / "00_inputs" / "materialization_snapshot.yaml",
        {
            "build_id": build_id,
            "generated_at": generated_at,
            "materialized_index": MATERIALIZED_INDEX.relative_to(ROOT).as_posix(),
            "corpus_summary": index.get("summary"),
            "collection_item_count": len(items),
            "selected_item_count": len(selected_rows),
        },
    )
    write_yaml(EXPERIMENT_ROOT / "00_inputs" / "selected_sources.yaml", {"sources": selected_rows})

    ontology = {
        "ontology_id": "experiment:meta-kb-v0",
        "version": "0.1.0",
        "world_assumption": "open",
        "entity_types": ["Source", "Paper", "Repository", "Standard", "Method", "System", "Domain", "WikiPage"],
        "epistemic_types": ["Claim", "Observation", "Evidence", "Inference", "Prediction", "Contradiction"],
        "relations": [
            {"name": "reports", "domain": "Source", "range": "Claim"},
            {"name": "supported_by", "domain": "Claim", "range": "Evidence"},
            {"name": "organized_under", "domain": "Source", "range": "Domain"},
            {"name": "compiled_into", "domain": "Claim", "range": "WikiPage"},
            {"name": "contradicts", "domain": "Claim", "range": "Claim"},
            {"name": "supersedes", "domain": "Claim", "range": "Claim"},
            {"name": "implements", "domain": "Repository", "range": "Method"},
        ],
        "assertion_kinds": ["observation", "assertion", "inference", "prediction", "decision", "action"],
        "admission_states": ["draft", "candidate", "trusted", "contested", "superseded", "retracted", "quarantined"],
        "constraints": [
            "every candidate claim has at least one evidence reference",
            "every evidence selector resolves to a local file",
            "wiki pages are derived views rather than truth records",
            "repository documentation claims remain maintainer assertions until runtime-tested",
            "collection assessments remain distinct from source-authored claims",
        ],
    }
    write_yaml(EXPERIMENT_ROOT / "01_ontology" / "meta_kb_ontology.yaml", ontology)
    write_yaml(
        EXPERIMENT_ROOT / "01_ontology" / "schema_bindings.yaml",
        {
            "knowledge_object_schema": KNOWLEDGE_SCHEMA.relative_to(ROOT).as_posix(),
            "wiki_page_schema": WIKI_PAGE_SCHEMA.relative_to(ROOT).as_posix(),
            "source_registry": "source_registry/registry.yaml",
            "materialized_index": "materialized_sources/index.yaml",
        },
    )

    write_jsonl(EXPERIMENT_ROOT / "02_entities" / "sources.jsonl", source_entities)
    write_jsonl(EXPERIMENT_ROOT / "02_entities" / "domains.jsonl", domain_entities)
    write_jsonl(EXPERIMENT_ROOT / "03_evidence" / "evidence.jsonl", evidence_objects)
    write_jsonl(EXPERIMENT_ROOT / "04_claims" / "claims.jsonl", claim_objects)
    write_jsonl(EXPERIMENT_ROOT / "04_claims" / "contradictions.jsonl", [])

    wiki_root = EXPERIMENT_ROOT / "05_wiki"
    claims_by_uid = {str(claim["uid"]): claim for claim in claim_objects}
    selected_by_uid = {str(source["uid"]): source for source in selected_rows}
    source_pages: list[str] = []
    for record in source_page_records:
        item = record["item"]
        slug = safe_slug(str(item["uid"]))
        source_pages.append(f"sources/{slug}.md")
        body_lines = [
            f"# {item.get('title')}",
            "",
            f"- Source UID: `{item.get('uid')}`",
            f"- Canonical ID: `{item.get('canonical_id')}`",
            f"- Source type: `{item.get('source_type')}`",
            f"- Content tier: `{item.get('content_tier')}`",
            f"- Domain bucket: `{record['domain']}`",
            f"- Local document: `{record['local_path']}`",
            "",
            "## Source-reported assertion",
            "",
            *(
                [f"- Claim ID: `{record['rendered_claim_refs'][0]}`", ""]
                if record["rendered_claim_refs"]
                else []
            ),
            record["excerpt"] or "No local full-text assertion was extracted.",
            "",
            "## Collection assessment",
            "",
            record["assessment"],
            "",
            "## Governance state",
            "",
            "Both statements remain candidates. The source assertion is not treated as independently verified, and the collection assessment is not treated as source-authored evidence.",
        ]
        page_rights, unavailable_rights = page_rights_payload(
            record["rendered_claim_refs"], claims_by_uid
        )
        rights_body = rights_markdown(
            current_repo_path=(
                EXPERIMENT_ROOT.relative_to(ROOT) / "05_wiki" / "sources" / f"{slug}.md"
            ).as_posix(),
            rights_refs=page_rights,
            unavailable_source_refs=unavailable_rights,
            sources_by_uid=selected_by_uid,
        )
        if rights_body:
            body_lines.extend(["", rights_body])
        frontmatter = wiki_frontmatter(
            uid=f"wiki-page:source-{short_hash(str(item['uid']))}",
            title=str(item.get("title") or item["uid"]),
            slug=f"sources/{slug}",
            page_type="source",
            summary=f"Candidate source page for {item.get('title')}",
            claim_refs=list(record["claim_refs"]),
            source_refs=[str(item["uid"])],
            generated_at=generated_at,
            build_id=build_id,
            rendered_claim_refs=list(record["rendered_claim_refs"]),
            rights_refs=page_rights,
            rights_unavailable_source_refs=unavailable_rights,
        )
        write_wiki_page(wiki_root / "sources" / f"{slug}.md", frontmatter, "\n".join(body_lines))

    map_pages: list[str] = []
    for domain, claims in sorted(claims_by_domain.items()):
        page_path = f"maps/{domain}.md"
        map_pages.append(page_path)
        source_refs = sorted({ref for claim in claims for ref in claim["provenance"]["source_refs"]})
        body = [f"# {domain.replace('-', ' ').title()}", "", "This map is compiled from candidate source assertions and collection assessments.", ""]
        for claim in claims:
            text = str(claim["semantics"]["property_assertions"].get("text") or "")
            scope = str(claim["semantics"]["property_assertions"].get("claim_scope") or "")
            body.extend([f"## `{claim['uid']}`", "", f"**Scope:** {scope}", "", text, ""])
        rendered_claim_refs = [str(claim["uid"]) for claim in claims]
        page_rights, unavailable_rights = page_rights_payload(rendered_claim_refs, claims_by_uid)
        rights_body = rights_markdown(
            current_repo_path=(
                EXPERIMENT_ROOT.relative_to(ROOT) / "05_wiki" / page_path
            ).as_posix(),
            rights_refs=page_rights,
            unavailable_source_refs=unavailable_rights,
            sources_by_uid=selected_by_uid,
        )
        if rights_body:
            body.extend([rights_body, ""])
        write_wiki_page(
            wiki_root / page_path,
            wiki_frontmatter(
                uid=f"wiki-page:map-{domain}",
                title=domain.replace("-", " ").title(),
                slug=f"maps/{domain}",
                page_type="map",
                summary=f"Candidate map of {domain.replace('-', ' ')} sources and claims.",
                claim_refs=[claim["uid"] for claim in claims],
                source_refs=source_refs,
                generated_at=generated_at,
                build_id=build_id,
                rendered_claim_refs=rendered_claim_refs,
                rights_refs=page_rights,
                rights_unavailable_source_refs=unavailable_rights,
            ),
            "\n".join(body),
        )

    all_claim_refs = [claim["uid"] for claim in claim_objects]
    all_source_refs = [str(item["uid"]) for item in selected]
    concepts = [
        (
            "concepts/source-specific-consumption.md",
            "Source-specific consumption",
            "Different source families require different materialization and evidence selectors before knowledge extraction.",
            "A repository is consumed through a commit-pinned semantic capsule, an arXiv paper through a TeX capsule, and rights-uncertain web material through a bounded excerpt capsule. These paths should not be collapsed into one anonymous chunking operation.",
        ),
        (
            "concepts/knowledge-evolution-loop.md",
            "Knowledge evolution loop",
            "The demo separates variation, evidence evaluation, admission, retention, supersession, and rollback.",
            "Knowledge evolution is represented as source change → candidate evidence → candidate claim → semantic comparison → review → admission → monitored consumption. The current demo stops at candidate review.",
        ),
        (
            "concepts/epistemic-separation.md",
            "Epistemic separation",
            "Source assertions, collector assessments, generated synthesis, and verified observations remain different object types or scopes.",
            "This prevents a wiki paragraph, a repository README statement, and a replicated result from being flattened into the same undifferentiated fact.",
        ),
    ]
    concept_pages: list[str] = []
    for path, title, summary, body in concepts:
        concept_pages.append(path)
        write_wiki_page(
            wiki_root / path,
            wiki_frontmatter(
                uid=f"wiki-page:{safe_slug(title)}",
                title=title,
                slug=path[:-3],
                page_type="concept",
                summary=summary,
                claim_refs=all_claim_refs[: min(12, len(all_claim_refs))],
                source_refs=all_source_refs[: min(12, len(all_source_refs))],
                generated_at=generated_at,
                build_id=build_id,
            ),
            f"# {title}\n\n{body}",
        )

    comparison_path = "comparisons/paper-vs-repository-consumption.md"
    write_wiki_page(
        wiki_root / comparison_path,
        wiki_frontmatter(
            uid="wiki-page:paper-vs-repository-consumption",
            title="Paper versus repository consumption",
            slug="comparisons/paper-vs-repository-consumption",
            page_type="comparison",
            summary="A comparison of TeX-first paper materialization and commit-pinned repository semanticization.",
            claim_refs=all_claim_refs[: min(16, len(all_claim_refs))],
            source_refs=all_source_refs,
            generated_at=generated_at,
            build_id=build_id,
        ),
        """# Paper versus repository consumption

| Source family | Frozen unit | Local evidence | What remains unproven |
|---|---|---|---|
| arXiv paper | source archive hash | TeX files, flattened document, line selectors | correctness and independent replication |
| GitHub repository | commit SHA | selected docs/config/code evidence and repo map | runtime behavior, benchmark claims, production reliability |
| Web/industry source | response hash | full text only when reusable; otherwise bounded excerpt | inaccessible or omitted text and source correctness |

The source adapter is part of epistemic provenance, not an interchangeable parser detail.
""",
    )

    materialization_audit_path = ROOT / "raw_data" / "audits" / "materialization_completeness_2026-09-10.yaml"
    materialization_audit = load_yaml(materialization_audit_path) if materialization_audit_path.exists() else {}
    gap_path = "gaps/materialization-and-trust-gaps.md"
    metadata_only_count = materialization_audit.get("metadata_only_count", 0) if isinstance(materialization_audit, dict) else 0
    partial_count = materialization_audit.get("partial_count", 0) if isinstance(materialization_audit, dict) else 0
    write_wiki_page(
        wiki_root / gap_path,
        wiki_frontmatter(
            uid="wiki-page:materialization-and-trust-gaps",
            title="Materialization and trust gaps",
            slug="gaps/materialization-and-trust-gaps",
            page_type="gap",
            summary="Known full-text, semantic, and trust gaps in the v0 corpus.",
            claim_refs=all_claim_refs[: min(10, len(all_claim_refs))],
            source_refs=all_source_refs[: min(10, len(all_source_refs))],
            generated_at=generated_at,
            build_id=build_id,
        ),
        f"""# Materialization and trust gaps

- Metadata-only local capsules: **{metadata_only_count}**
- Partial materializations: **{partial_count}**
- Trusted scientific claims in this demo: **0**
- Runtime-tested GitHub implementations: **0**
- Independently replicated paper claims: **0**

A local file is necessary for reproducible consumption but is not sufficient for epistemic promotion.
""",
    )

    index_body = [
        "# v0 Meta KB",
        "",
        "## Domain maps",
        "",
        *[f"- `{path}`" for path in map_pages],
        "",
        "## Concepts",
        "",
        *[f"- `{path}`" for path in concept_pages],
        "",
        "## Comparison and gaps",
        "",
        f"- `{comparison_path}`",
        f"- `{gap_path}`",
        "",
        "## Source pages",
        "",
        *[f"- `{path}`" for path in source_pages],
    ]
    write_wiki_page(
        wiki_root / "index.md",
        wiki_frontmatter(
            uid="wiki-page:v0-meta-kb-index",
            title="v0 Meta KB Index",
            slug="index",
            page_type="map",
            summary="Entry point for the candidate v0 meta knowledge base.",
            claim_refs=all_claim_refs,
            source_refs=all_source_refs,
            generated_at=generated_at,
            build_id=build_id,
        ),
        "\n".join(index_body),
    )

    tier_counts = Counter(str(item.get("content_tier")) for item in selected)
    domain_counts = Counter(row["domain"] for row in selected_rows)
    evaluation = {
        "evaluation_id": f"evaluation:{short_hash(build_id)}",
        "build_id": build_id,
        "generated_at": generated_at,
        "checks": {
            "local_source_selection": "pass",
            "evidence_created_for_every_claim": "pending-validator",
            "claim_schema": "pending-validator",
            "wiki_page_schema": "pending-validator",
            "local_evidence_resolution": "pending-validator",
            "scientific_truth": "not-evaluated",
            "repository_runtime_behavior": "not-evaluated",
        },
        "counts": {
            "collection_sources": len(items),
            "selected_sources": len(selected_rows),
            "source_entities": len(source_entities),
            "domain_entities": len(domain_entities),
            "evidence_objects": len(evidence_objects),
            "claim_objects": len(claim_objects),
            "wiki_pages": len(list(wiki_root.rglob("*.md"))),
            "trusted_claims": 0,
        },
        "selected_content_tiers": dict(tier_counts),
        "selected_domains": dict(domain_counts),
        "interpretation": "This report measures structural pipeline completion, not scientific correctness.",
    }
    write_yaml(EXPERIMENT_ROOT / "06_evaluation" / "report.yaml", evaluation)
    (EXPERIMENT_ROOT / "06_evaluation" / "coverage.md").write_text(
        "# Demo coverage\n\n"
        + "\n".join(f"- {domain}: {count} selected sources" for domain, count in sorted(domain_counts.items()))
        + "\n\n"
        + "\n".join(f"- {tier}: {count}" for tier, count in sorted(tier_counts.items()))
        + "\n",
        encoding="utf-8",
    )

    review_items = [
        {
            "claim_ref": claim["uid"],
            "review_type": "source-assertion" if claim["semantics"]["property_assertions"].get("claim_scope") == "source-reported assertion" else "collection-assessment",
            "state": "not_started",
            "required_checks": ["evidence-entailment", "scope", "identity", "source-quality", "contradiction-search"],
        }
        for claim in claim_objects
    ]
    write_yaml(
        EXPERIMENT_ROOT / "07_review" / "queue.yaml",
        {
            "build_id": build_id,
            "items": review_items,
            "policy": "No claim becomes trusted without an explicit admission decision.",
        },
    )

    write_yaml(
        EXPERIMENT_ROOT / "08_release" / "manifest.yaml",
        {
            "experiment_id": config.get("experiment_id"),
            "build_id": build_id,
            "generated_at": generated_at,
            "release_state": "candidate",
            "source_snapshot": "00_inputs/selected_sources.yaml",
            "ontology": "01_ontology/meta_kb_ontology.yaml",
            "entities": ["02_entities/sources.jsonl", "02_entities/domains.jsonl"],
            "evidence": "03_evidence/evidence.jsonl",
            "claims": "04_claims/claims.jsonl",
            "wiki": "05_wiki/index.md",
            "evaluation": "06_evaluation/report.yaml",
            "review_queue": "07_review/queue.yaml",
            "trusted_claims": 0,
            "rollback": "Delete generated directories 00_inputs through 08_release and rebuild from pinned local capsules.",
        },
    )

    print(
        f"demo_built selected_sources={len(selected_rows)} claims={len(claim_objects)} "
        f"evidence={len(evidence_objects)} wiki_pages={len(list(wiki_root.rglob('*.md')))}"
    )
    from validate_demo import main as validate_demo
    return validate_demo(write_reports=True)


if __name__ == "__main__":
    raise SystemExit(main())
