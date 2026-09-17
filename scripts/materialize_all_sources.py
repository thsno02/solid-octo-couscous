#!/usr/bin/env python3
"""Materialize every collected source into a local, source-specific capsule.

The goal is not to pretend that every URL can legally or technically be mirrored in
full.  The invariant is stronger and more honest:

* every metadata record receives a local capsule and manifest;
* open scholarly sources are materialized as full text when available;
* GitHub repositories are frozen at a commit and converted into semantic capsules,
  not vendored wholesale;
* web and proprietary sources are stored as full text only when the metadata says
  redistribution is open, otherwise as bounded evidence excerpts;
* every generated file is hashed and every selector resolves to a local file.

The script is deterministic for a frozen upstream revision except for retrieval
metadata such as timestamps.  Git history is the immutable version store; this
script does not duplicate all payloads into a second snapshot tree.
"""
from __future__ import annotations

import argparse
import base64
import concurrent.futures
import dataclasses
import gzip
import hashlib
import html
import io
import json
import os
import posixpath
import re
import shutil
import stat
import subprocess
import tarfile
import threading
import time
import urllib.parse
import zlib
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

import requests
import yaml

ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / "raw_data"
MATERIALIZED_ROOT = ROOT / "materialized_sources"
CORPUS_ROOT = MATERIALIZED_ROOT / "corpus"
REGISTRY_ROOT = ROOT / "source_registry"
AUDIT_ROOT = RAW_ROOT / "audits"

USER_AGENT = (
    "solid-octo-couscous-materializer/2.0 "
    "(+https://github.com/thsno02/solid-octo-couscous)"
)

DIRECTORY_SOURCE_TYPES = {
    "arxiv": "arxiv",
    "biorxiv": "biorxiv",
    "journal": "journal",
    "paper": "paper",
    "standard": "standard",
    "methodology": "methodology",
    "industry": "industry",
    "blog": "blog",
    "githubs": "github",
    "dataset": "dataset",
    "benchmark": "benchmark",
    "incident": "incident",
    "x": "x",
}

TYPE_ALIASES = {
    "book_chapter": "paper",
    "book-chapter": "paper",
    "conference": "paper",
    "preprint": "paper",
    "industry_doc": "industry",
    "industry-doc": "industry",
    "ontology": "standard",
    "github_repo": "github",
    "github-repository": "github",
}

ARXIV_TEXT_EXTENSIONS = {
    ".tex",
    ".ltx",
    ".bib",
    ".bbl",
    ".sty",
    ".cls",
    ".bst",
    ".def",
    ".txt",
    ".md",
    ".rst",
    ".json",
    ".yaml",
    ".yml",
    ".csv",
}

GITHUB_TEXT_EXTENSIONS = {
    ".md",
    ".mdx",
    ".rst",
    ".txt",
    ".adoc",
    ".json",
    ".yaml",
    ".yml",
    ".toml",
    ".ini",
    ".cfg",
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".go",
    ".rs",
    ".java",
    ".kt",
    ".scala",
    ".rb",
    ".sh",
    ".sql",
    ".proto",
    ".graphql",
    ".gql",
    ".xml",
}

PROMINENT_GITHUB_FILENAMES = {
    "readme.md",
    "readme.rst",
    "readme.txt",
    "agents.md",
    "claude.md",
    "architecture.md",
    "design.md",
    "overview.md",
    "concepts.md",
    "security.md",
    "contributing.md",
    "citation.cff",
    "license",
    "license.md",
    "license.txt",
    "pyproject.toml",
    "package.json",
    "go.mod",
    "cargo.toml",
    "requirements.txt",
    "makefile",
    "dockerfile",
}

GITHUB_DOC_KEYWORDS = {
    "architecture",
    "design",
    "overview",
    "concept",
    "ontology",
    "schema",
    "memory",
    "knowledge",
    "evaluation",
    "benchmark",
    "workflow",
    "agent",
    "api",
    "interface",
    "security",
    "governance",
    "provenance",
    "retrieval",
    "compile",
    "ingest",
    "index",
}

_thread_local = threading.local()
_arxiv_semaphore = threading.Semaphore(3)
_github_semaphore = threading.Semaphore(6)
_generic_semaphore = threading.Semaphore(6)


@dataclasses.dataclass(frozen=True)
class SourceRecord:
    uid: str
    source_type: str
    canonical_id: str | None
    title: str
    canonical_url: str | None
    metadata_path: Path
    metadata: dict[str, Any]
    priority: str
    rights_access: str

    @property
    def relative_metadata_path(self) -> str:
        return self.metadata_path.relative_to(ROOT).as_posix()

    @property
    def capsule_key(self) -> str:
        base = safe_key(self.uid)
        suffix = hashlib.sha1(self.relative_metadata_path.encode("utf-8")).hexdigest()[:8]
        return f"{base}--{suffix}"

    @property
    def capsule_root(self) -> Path:
        return CORPUS_ROOT / self.capsule_key


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def safe_key(value: str) -> str:
    value = value.strip().replace("/", "--").replace(":", "-")
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-._")
    return value or "source"


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


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_source_type(path: Path, metadata: dict[str, Any]) -> str:
    relative = path.relative_to(RAW_ROOT)
    directory = relative.parts[0] if relative.parts else "unknown"
    if directory in DIRECTORY_SOURCE_TYPES:
        return DIRECTORY_SOURCE_TYPES[directory]
    raw = str(metadata.get("source_type") or metadata.get("source") or directory).strip().lower()
    raw = raw.replace(" ", "_")
    return TYPE_ALIASES.get(raw, raw)


def canonical_id_for(source_type: str, metadata: dict[str, Any]) -> str | None:
    candidates = [
        metadata.get("canonical_id"),
        metadata.get("arxiv_id") if source_type == "arxiv" else None,
        metadata.get("repo") if source_type == "github" else None,
        metadata.get("doi"),
        metadata.get("id"),
    ]
    for candidate in candidates:
        if candidate is None:
            continue
        value = str(candidate).strip()
        if not value:
            continue
        if source_type == "arxiv":
            value = re.sub(r"v\d+$", "", value)
        return value
    return None


def canonical_url_for(source_type: str, canonical_id: str | None, metadata: dict[str, Any]) -> str | None:
    for field in (
        "canonical_url",
        "url",
        "official_url",
        "source_url",
        "paper_url",
        "landing_page",
    ):
        value = metadata.get(field)
        if isinstance(value, str) and value.strip():
            return value.strip()
    if canonical_id and source_type == "arxiv":
        return f"https://arxiv.org/abs/{canonical_id}"
    if canonical_id and source_type == "github":
        return f"https://github.com/{canonical_id}"
    if canonical_id and metadata.get("doi"):
        return f"https://doi.org/{canonical_id}"
    return None


def discover_records() -> list[SourceRecord]:
    records: list[SourceRecord] = []
    seen_uids: Counter[str] = Counter()
    for path in sorted(RAW_ROOT.rglob("metadata.yaml")):
        metadata = load_yaml(path)
        if not isinstance(metadata, dict):
            continue
        source_type = normalize_source_type(path, metadata)
        canonical_id = canonical_id_for(source_type, metadata)
        title = str(metadata.get("title") or metadata.get("repo") or path.parent.name).strip()
        base_uid = str(metadata.get("uid") or f"{source_type}:{canonical_id or safe_key(title)}").strip()
        seen_uids[base_uid] += 1
        uid = base_uid if seen_uids[base_uid] == 1 else f"{base_uid}#{seen_uids[base_uid]}"
        canonical_url = canonical_url_for(source_type, canonical_id, metadata)
        collection = metadata.get("collection") if isinstance(metadata.get("collection"), dict) else {}
        priority = str(collection.get("priority") or metadata.get("priority") or "P1")
        rights = metadata.get("rights") if isinstance(metadata.get("rights"), dict) else {}
        rights_access = str(rights.get("access") or "unknown")
        records.append(
            SourceRecord(
                uid=uid,
                source_type=source_type,
                canonical_id=canonical_id,
                title=title,
                canonical_url=canonical_url,
                metadata_path=path,
                metadata=metadata,
                priority=priority,
                rights_access=rights_access,
            )
        )
    return records


def session() -> requests.Session:
    current = getattr(_thread_local, "session", None)
    if current is None:
        current = requests.Session()
        current.headers.update({"User-Agent": USER_AGENT, "Accept": "*/*"})
        _thread_local.session = current
    return current


def fetch_bytes(url: str, *, timeout: int, max_bytes: int, attempts: int = 3) -> tuple[bytes, str, dict[str, str]]:
    last_error: Exception | None = None
    for attempt in range(attempts):
        response: requests.Response | None = None
        try:
            request_headers: dict[str, str] = {}
            host = urllib.parse.urlparse(url).netloc.lower()
            token = os.getenv("GITHUB_TOKEN")
            if token and host == "api.github.com":
                request_headers.update({
                    "Authorization": f"Bearer {token}",
                    "X-GitHub-Api-Version": "2022-11-28",
                })
            response = session().get(
                url,
                timeout=timeout,
                stream=True,
                allow_redirects=True,
                headers=request_headers,
            )
            response.raise_for_status()
            chunks: list[bytes] = []
            total = 0
            for chunk in response.iter_content(chunk_size=128 * 1024):
                if not chunk:
                    continue
                total += len(chunk)
                if total > max_bytes:
                    raise RuntimeError(f"response exceeded {max_bytes} bytes")
                chunks.append(chunk)
            headers = {str(key).lower(): str(value) for key, value in response.headers.items()}
            resolved_url = str(response.url)
            response.close()
            return b"".join(chunks), resolved_url, headers
        except Exception as exc:  # requests raises several useful subclasses.
            if response is not None:
                response.close()
            last_error = exc
            if attempt + 1 < attempts:
                time.sleep(min(8, 2**attempt))
    raise RuntimeError(f"fetch failed for {url}: {last_error}")


def local_file_inventory(root: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.name == "manifest.yaml":
            continue
        rows.append(
            {
                "path": path.relative_to(ROOT).as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    return rows


def candidate_urls(record: SourceRecord) -> list[str]:
    fields = (
        "source_archive_url",
        "open_copy_url",
        "pdf_url",
        "full_text_url",
        "download_url",
        "source_url",
        "canonical_url",
        "url",
    )
    urls: list[str] = []
    for field in fields:
        value = record.metadata.get(field)
        if isinstance(value, str) and value.startswith(("http://", "https://")):
            urls.append(value)
    if record.canonical_url:
        urls.append(record.canonical_url)
    deduped: list[str] = []
    seen: set[str] = set()
    for url in urls:
        if url not in seen:
            seen.add(url)
            deduped.append(url)
    return deduped


def text_is_open(record: SourceRecord, config: dict[str, Any], resolved_url: str | None = None) -> bool:
    if record.rights_access in {"open", "source_available"}:
        return True
    if record.metadata.get("rights") and isinstance(record.metadata["rights"], dict):
        if record.metadata["rights"].get("license_spdx"):
            return True
    allowed_types = set(config.get("full_text_source_types", []))
    if record.source_type in allowed_types:
        return True
    if resolved_url:
        host = urllib.parse.urlparse(resolved_url).netloc.lower()
        if any(host == domain or host.endswith("." + domain) for domain in config.get("open_full_text_domains", [])):
            return True
    return False


def write_capsule_readme(record: SourceRecord, root: Path, manifest: dict[str, Any]) -> None:
    lines = [
        f"# {record.title}",
        "",
        f"- UID: `{record.uid}`",
        f"- Source type: `{record.source_type}`",
        f"- Canonical ID: `{record.canonical_id}`",
        f"- Canonical URL: {record.canonical_url or 'unresolved'}",
        f"- Materialization status: `{manifest.get('status')}`",
        f"- Content tier: `{manifest.get('content_tier')}`",
        "",
        "This directory is a local evidence capsule. It is not, by itself, a trusted knowledge assertion.",
    ]
    if manifest.get("rights", {}).get("redistribution_package"):
        lines.extend(["", "Redistribution notice and attribution: [NOTICE.md](NOTICE.md)."])
    materialization = manifest.get("materialization") or {}
    if materialization.get("tex_reading_view", {}).get("enabled") is True:
        view = materialization["tex_reading_view"]
        lines.extend(["", "Local retained representations:", f"- [Chosen consumer: collector-derived TeX reading view]({view['document']})"])
        for name in view.get("legacy_documents", []):
            lines.append(f"- [Historical normalized representation (unchanged): {Path(name).name}]({name})")
        lines.append("The reading view is derived, not a raw-source quotation. Math/code/table expressions and local macro/citation support are retained without TeX execution; limitations remain explicit in the manifest.")
    if materialization.get("retained_markdown_source"):
        lines.extend(["", "Local retained representations:"])
        for label, field in (("Consumer Markdown", "document"), ("Original Markdown", "retained_markdown_source"), ("Original HTML", "retained_html_source")):
            if materialization.get(field):
                lines.append(f"- [{label}]({materialization[field]})")
    elif materialization.get("retained_text_sources"):
        lines.extend(["", "Local retained representations:", f"- [Consumer Markdown (collector assembly)]({materialization['document']})"])
        source_names = {item["source"] for item in materialization["retained_text_sources"]}
        for item in materialization["retained_text_sources"]:
            lines.append(f"- [Original {item['format'].upper()}: {Path(item['source']).name}]({item['source']})")
        for item in manifest.get("retrievals", []):
            name = item.get("local_path", "")
            if isinstance(name, str) and name.endswith(".html") and name not in source_names:
                lines.append(f"- [Retained HTML evidence: {Path(name).name}]({name})")
    (root / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


class RedistributionPackageError(ValueError):
    """A declared publication condition failed; never downgrade it to metadata-only."""


class ArxivPreflightError(RuntimeError):
    """An arXiv rebuild cannot safely replace the retained capsule."""


class RetainedMarkdownPreflightError(RuntimeError):
    """A fixed Markdown snapshot cannot safely be replayed; keep its originals."""


def redistribution_notice_href(root: Path, document: Path) -> str:
    """Return the safe relative link from a materialized document to its notice."""
    resolved_root = root.resolve()
    resolved_document = document.resolve()
    resolved_document.relative_to(resolved_root)
    return Path(
        os.path.relpath(resolved_root / "NOTICE.md", start=resolved_document.parent)
    ).as_posix()


def redistribution_footer(package: dict[str, Any], notice_href: str = "NOTICE.md") -> str:
    """Append attribution without shifting existing source selectors."""
    return (
        "\n\n<!-- materialization-redistribution-notice -->\n"
        "## Redistribution notice\n\n"
        f"{package['attribution']}\n\n"
        f"Changes: {package['modifications']}\n\n"
        f"Scope: {package['scope']}\n\n"
        f"Full license and original rights links: [NOTICE.md]({notice_href}).\n"
    )


def apply_redistribution_package(record: SourceRecord, root: Path, manifest: dict[str, Any]) -> None:
    """Restore reviewed license packaging on every materialization, not just once."""
    rights = record.metadata.get("rights") or {}
    package = rights.get("redistribution_package")
    if not package:
        return
    if package.get("source_revision") != manifest.get("revision"):
        if manifest.get("content_tier") == "full_text":
            raise ValueError("declared redistribution package does not cover the retrieved revision")
        return
    for field in ("source_revision", "source_version_url", "notice_path", "attribution", "modifications", "scope"):
        if not isinstance(package.get(field), str) or not package[field].strip():
            raise ValueError(f"redistribution package is missing {field}")
    notice_path = (ROOT / package["notice_path"]).resolve()
    notice_path.relative_to(ROOT.resolve())
    notice = notice_path.read_text(encoding="utf-8")
    if not notice.strip():
        raise ValueError("redistribution notice is empty")
    document_name = manifest.get("materialization", {}).get("document")
    if not document_name:
        raise ValueError("redistribution package needs an explicit materialized document")
    document = (root / document_name).resolve()
    document.relative_to(root.resolve())
    notice_href = redistribution_notice_href(root, document)
    text = document.read_bytes().decode("utf-8") if "retained_text_sources" in manifest.get("materialization", {}) else document.read_text(encoding="utf-8")
    previous = manifest.get("rights", {}).get("redistribution_package")
    marker_count = text.count("<!-- materialization-redistribution-notice -->")
    if marker_count:
        if marker_count != 1 or not previous:
            raise ValueError("unexpected or duplicate redistribution footer")
        previous_footer = redistribution_footer(previous, notice_href)
        if not text.endswith(previous_footer):
            raise ValueError("previous redistribution footer is not intact at end of document")
        text = text[:-len(previous_footer)]
    text += redistribution_footer(package, notice_href)
    document.write_text(text, encoding="utf-8")
    (root / "NOTICE.md").write_text(notice, encoding="utf-8")
    manifest["materialization"]["stored_characters"] = len(text)
    manifest["rights"].update({
        "declared_access": rights.get("access"),
        "full_text_redistribution_assumed": False,
        "license_spdx": rights.get("license_spdx"),
        "license_url": rights.get("license_url"),
        "license_verified_at": rights.get("license_verified_at"),
        "redistribution_package": dict(package),
    })


def base_manifest(record: SourceRecord, adapter: str, generated_at: str) -> dict[str, Any]:
    return {
        "manifest_version": 2,
        "uid": record.uid,
        "source_type": record.source_type,
        "canonical_id": record.canonical_id,
        "title": record.title,
        "canonical_url": record.canonical_url,
        "metadata_path": record.relative_metadata_path,
        "generated_at": generated_at,
        "adapter": adapter,
        "status": "metadata_only",
        "content_tier": "metadata_capsule",
        "revision": None,
        "rights": {
            "declared_access": record.rights_access,
            "full_text_redistribution_assumed": False,
        },
        "retrievals": [],
        "selectors": [],
        "local_files": [],
        "warnings": [],
        "errors": [],
    }


def prepare_capsule(record: SourceRecord) -> Path:
    root = record.capsule_root
    shutil.rmtree(root, ignore_errors=True)
    root.mkdir(parents=True, exist_ok=True)
    write_yaml(root / "source-metadata.yaml", record.metadata)
    return root


def finalize_capsule(record: SourceRecord, root: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    try:
        apply_redistribution_package(record, root, manifest)
    except (KeyError, TypeError, AttributeError, ValueError, OSError) as exc:
        raise RedistributionPackageError(f"{record.uid}: {exc}") from exc
    write_capsule_readme(record, root, manifest)
    manifest["local_files"] = local_file_inventory(root)
    manifest["local_bytes"] = sum(item["bytes"] for item in manifest["local_files"])
    write_yaml(root / "manifest.yaml", manifest)
    return manifest


def unpack_arxiv(payload: bytes) -> tuple[list[tuple[str, bytes]], str]:
    try:
        with tarfile.open(fileobj=io.BytesIO(payload), mode="r:*") as archive:
            members = []
            for member in archive.getmembers():
                if not member.isfile() or member.size > 8_000_000:
                    continue
                handle = archive.extractfile(member)
                if handle is not None:
                    members.append((member.name, handle.read()))
            return members, "tar"
    except tarfile.TarError:
        pass
    try:
        uncompressed = gzip.decompress(payload)
    except OSError:
        return [("main.tex", payload)], "single"
    try:
        with tarfile.open(fileobj=io.BytesIO(uncompressed), mode="r:*") as archive:
            members = []
            for member in archive.getmembers():
                if not member.isfile() or member.size > 8_000_000:
                    continue
                handle = archive.extractfile(member)
                if handle is not None:
                    members.append((member.name, handle.read()))
            return members, "gzip-tar"
    except tarfile.TarError:
        return [("main.tex", uncompressed)], "gzip-single"


def arxiv_pdf_payload(payload: bytes) -> tuple[bytes | None, str | None]:
    """Return the actual PDF bytes and transport container when magic confirms it."""

    if payload.startswith(b"%PDF-"):
        return payload, "pdf"
    if not payload.startswith(b"\x1f\x8b"):
        return None, None
    try:
        uncompressed = gzip.decompress(payload)
    except OSError:
        return None, None
    if uncompressed.startswith(b"%PDF-"):
        return uncompressed, "gzip-pdf"
    return None, None


def looks_like_single_tex(payload: bytes) -> bool:
    """Recognize a single TeX source without treating arbitrary 200 bodies as TeX."""

    if b"\x00" in payload[:8192]:
        return False
    sample = payload[:1_000_000].decode("utf-8", errors="ignore")
    return bool(
        re.search(
            r"\\(?:documentclass\b|documentstyle\b|begin\s*\{document\}|input\b|include\b|"
            r"title\b|author\b|section\b|def\b|newcommand\b|usepackage\b|bye\b)",
            sample,
        )
    )


def is_obvious_error_document(payload: bytes) -> bool:
    prefix = payload.lstrip()
    if prefix.startswith(b"\xef\xbb\xbf"):
        prefix = prefix[3:].lstrip()
    prefix = prefix[:512].lower()
    return prefix.startswith((b"<!doctype html", b"<html", b"<!--", b"<?xml", b"{", b"["))


def classify_arxiv_payload(payload: bytes) -> str | None:
    """Classify only supported arXiv e-print representations by their bytes."""

    _, pdf_container = arxiv_pdf_payload(payload)
    if pdf_container is not None:
        return pdf_container
    if is_obvious_error_document(payload):
        return None
    try:
        with tarfile.open(fileobj=io.BytesIO(payload), mode="r:*") as archive:
            if any(member.isfile() for member in archive.getmembers()):
                return "tar"
    except tarfile.TarError:
        pass
    if payload.startswith(b"\x1f\x8b"):
        try:
            uncompressed = gzip.decompress(payload)
        except OSError:
            return None
        if is_obvious_error_document(uncompressed):
            return None
        return "gzip-single" if looks_like_single_tex(uncompressed) else None
    return "single" if looks_like_single_tex(payload) else None


def arxiv_eprint_id(record: SourceRecord) -> str:
    """Bind an arXiv retrieval to ``versioning.source_version`` when declared."""

    if not record.canonical_id:
        raise ValueError("missing arXiv identifier")
    versioning = record.metadata.get("versioning")
    source_version = versioning.get("source_version") if isinstance(versioning, dict) else None
    if source_version in (None, ""):
        return record.canonical_id
    if not isinstance(source_version, str) or not re.fullmatch(r"v[1-9]\d*", source_version.strip()):
        raise ValueError("arXiv versioning.source_version must be vN")
    return f"{record.canonical_id}{source_version.strip()}"


def tex_comment_start(line: str) -> int | None:
    """A percent sign is escaped only after an odd run of backslashes."""
    for index, character in enumerate(line):
        if character != "%":
            continue
        previous = index - 1
        while previous >= 0 and line[previous] == "\\":
            previous -= 1
        if (index - previous - 1) % 2 == 0:
            return index
    return None


def tex_without_comments(text: str) -> str:
    lines: list[str] = []
    for line in text.splitlines(keepends=True):
        start = tex_comment_start(line)
        if start is not None:
            ending = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else "\r" if line.endswith("\r") else ""
            line = line[:start] + ending
        lines.append(line)
    return "".join(lines)


def tex_root_candidates(
    files: dict[str, str], *, exclusions: list[dict[str, str]] | None = None,
) -> list[str]:
    """Find document roots by structure, including TeX saved with a .txt suffix."""
    candidates: list[str] = []
    for path, text in sorted(files.items()):
        suffix = PurePosixPath(path).suffix.lower()
        if suffix not in {".tex", ".ltx", ".txt"}:
            continue
        body = tex_without_comments(text)
        begin = re.search(r"\\begin\s*\{document\}", body)
        if begin is None or re.search(r"\\end\s*\{document\}", body[begin.end():]) is None:
            continue
        # An ordinary .txt containing a TeX fragment is not a source document.
        if suffix == ".txt" and re.search(
            r"\\(?:documentclass|documentstyle)\b", body[:begin.start()]
        ) is None:
            continue
        document_class = re.search(
            r"\\documentclass\s*(?:\[[^\]]*\]\s*)?\{\s*([^{}]+?)\s*\}", body[:begin.start()]
        )
        reason: str | None = None
        evidence = ""
        if document_class is not None and document_class.group(1).strip().lower() == "standalone":
            reason, evidence = "standalone_document", document_class.group(0)
        title_match = re.search(r"\\title\s*(?:\[[^\]]*\]\s*)?\{([^{}]*)\}", body)
        if reason is None and title_match is not None:
            title = re.sub(r"\\[A-Za-z@]+|\\\\", " ", title_match.group(1))
            title = " ".join(title.replace("\\", " ").split())
            if re.search(
                r"^(?:formatting instructions\b.*\b(?:submissions|proceedings)|"
                r"author guidelines\b.*\bproceedings|a new style for\b.*\bpapers)\s*$",
                title, re.IGNORECASE,
            ):
                reason, evidence = "formatting_template_document", title
        parts = PurePosixPath(path).parts
        historical_directory = any(re.fullmatch(r"revision[-_]history", part, re.IGNORECASE) for part in parts[:-1])
        historical_copy = (
            any(part.lower() == "history" for part in parts[:-1])
            and re.search(r"\bpre-final-revision\b", PurePosixPath(path).stem.replace("_", "-"), re.IGNORECASE)
        )
        if reason is None and (historical_directory or historical_copy):
            reason, evidence = "explicit_historical_document", path
        if reason is not None:
            if exclusions is not None:
                exclusions.append({"kind": reason, "path": path, "evidence": evidence})
            continue
        candidates.append(path)
    return candidates


def choose_main_tex(files: dict[str, str]) -> str | None:
    candidates = tex_root_candidates(files)
    # Multiple real documents require a boundary decision, not a size tie-break.
    return candidates[0] if len(candidates) == 1 else None


def resolve_tex_include(
    current_path: str, target: str, files: dict[str, str], *, directory: str | None = None,
) -> str | None:
    """Resolve retained literal paths, without root fallback for an explicit import directory."""
    target = target.strip().strip("{}\"")
    if not target:
        return None
    current_dir = PurePosixPath(directory) if directory is not None else PurePosixPath(current_path).parent
    candidates = [current_dir / target]
    if directory is None:
        candidates.append(PurePosixPath(target))
    expanded: list[PurePosixPath] = []
    for candidate in candidates:
        expanded.append(candidate)
        if not candidate.suffix:
            expanded.append(candidate.with_suffix(".tex"))
    for candidate in expanded:
        normalized = posixpath.normpath(candidate.as_posix())
        if normalized.startswith(("/", "../")) or normalized in {".", ".."}:
            continue
        if normalized in files:
            return normalized
    return None


def flatten_tex(
    main_path: str,
    files: dict[str, str],
    *,
    max_depth: int = 20,
    diagnostics: list[dict[str, str]] | None = None,
    include_graph: list[dict[str, str]] | None = None,
    reading_view: bool = False,
) -> str:
    """Expand literal braced calls, not macros, conditionals, or a full TeX engine.

    ``import`` directories are relative to the selected root's compile directory;
    ``subimport`` appends to the enclosing import directory. A nested ``import``
    resets that directory. Within an import, ``input``/``include`` search only the
    active import directory: unsupported ancestor/system-path searches stay missing
    rather than silently selecting a same-named root file. Only retained paths resolve.
    """
    include_pattern = re.compile(
        r"\\(?:(input|include)\s*\{([^{}]+)\}|(import|subimport)\s*\{([^{}]*)\}\s*\{([^{}]+)\})"
    )
    root_directory = PurePosixPath(main_path).parent.as_posix()

    def visit(path: str, stack: tuple[str, ...], import_directory: str | None) -> str:
        if path in stack:
            if diagnostics is not None:
                diagnostics.append({"kind": "cycle", "path": path})
            return f"\n% [cycle omitted: {path}]\n"
        if len(stack) >= max_depth:
            if diagnostics is not None:
                diagnostics.append({"kind": "depth_limit", "path": path})
            return f"\n% [include depth exceeded: {path}]\n"
        text = files.get(path, "")
        if reading_view:
            literals = tex_reading_regions(text)
            for url in re.finditer(r"\\url\s*\{", text):
                prefix = text[text.rfind("\n", 0, url.start()) + 1:url.start()]
                if tex_comment_start(prefix) is not None or any(first <= url.start() < last for first, last in literals):
                    continue
                group = tex_group(text, url.end() - 1)
                if group and any(tex_comment_start(line) is not None for line in group[0].splitlines()):
                    raise ValueError("literal percent in TeX url is outside the reading profile; retained inputs unchanged")
        searchable = tex_reading_mask(text, definitions=True) if reading_view else text
        supported_starts = {match.start() for match in include_pattern.finditer(searchable)}
        for match in re.finditer(r"\\(?:input|include|import|subimport)\b", searchable):
            line_prefix = text[text.rfind("\n", 0, match.start()) + 1:match.start()]
            if match.start() not in supported_starts and tex_comment_start(line_prefix) is None:
                if diagnostics is not None:
                    line_end = text.find("\n", match.start())
                    diagnostics.append({
                        "kind": "unsupported_include_syntax", "path": path,
                        "target": text[match.start():line_end if line_end >= 0 else len(text)],
                    })

        def replace(match: re.Match[str]) -> str:
            if reading_view and searchable[match.start():match.end()] != match.group(0):
                return match.group(0)
            line_prefix = text[text.rfind("\n", 0, match.start()) + 1:match.start()]
            if tex_comment_start(line_prefix) is not None:
                return match.group(0)
            command = match.group(1) or match.group(3)
            target = match.group(2) if match.group(1) else match.group(5)
            next_import_directory = import_directory
            directory = import_directory
            if match.group(3):
                base_directory = root_directory if command == "import" else import_directory or root_directory
                directory = posixpath.normpath(posixpath.join(base_directory, match.group(4).strip()))
                next_import_directory = directory
            if "\\" in target or (match.group(3) and "\\" in match.group(4)):
                if diagnostics is not None:
                    diagnostics.append({"kind": "unsupported_include_syntax", "path": path, "target": match.group(0)})
                return match.group(0)
            resolved = resolve_tex_include(path, target, files, directory=directory)
            if resolved is None:
                if diagnostics is not None:
                    diagnostics.append({
                        "kind": "missing_include", "path": path, "target": target,
                        **({"directory": directory} if directory is not None else {}),
                    })
                return match.group(0)
            if include_graph is not None:
                include_graph.append({"from": path, "to": resolved})
            return (
                f"\n% --- begin included file: {resolved} ---\n"
                + visit(resolved, stack + (path,), next_import_directory)
                + f"\n% --- end included file: {resolved} ---\n"
            )

        return include_pattern.sub(replace, text)

    return visit(main_path, tuple(), None)


def tex_to_plain(
    text: str, *, diagnostics: list[dict[str, str]] | None = None, path: str = "document.tex",
) -> str:
    # Preserve section labels and arguments while removing the most disruptive TeX syntax.
    text = tex_without_comments(text)
    begin = re.search(r"\\begin\s*\{document\}", text)
    if begin is not None:
        if diagnostics is not None and re.search(r"\\abstract\b|\\begin\s*\{abstract\}", text[:begin.start()]):
            diagnostics.append({"kind": "preamble_semantic_abstract_omitted", "path": path})
        text = text[begin.end():]
        end = re.search(r"\\end\s*\{document\}", text)
        if end is not None:
            text = text[:end.start()]
    text = re.sub(r"\\(?:sub)*section\*?\{([^{}]+)\}", r"\n\n## \1\n", text)
    text = re.sub(r"\\paragraph\*?\{([^{}]+)\}", r"\n\n### \1\n", text)
    text = re.sub(r"\\begin\{abstract\}", "\n\n## Abstract\n", text)
    text = re.sub(r"\\end\{abstract\}", "\n", text)
    text = re.sub(r"\\label\{[^{}]*\}", "", text)
    text = re.sub(r"\\(?:cite|citep|citet|ref|eqref|label|url|href)\*?(?:\[[^\]]*\])?\{([^{}]*)\}", r" \1 ", text)
    text = re.sub(r"\\(?:textbf|textit|emph|mathrm|mathbf|mathit|operatorname)\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\(?:begin|end)\s*\{[^{}]+\}(?:\[[^\]]*\])?", "\n", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", text)
    text = text.replace("{", " ").replace("}", " ")
    text = re.sub(r"\$+", " ", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


TEX_READING_PROFILE = "conservative-v1"
TEX_READING_TRANSFORMATION = "Conservative TeX reading view: literal includes, proven static prose macros; original math/code/table expressions retained; not a raw-source quotation"
TEX_LITERAL_ENVIRONMENTS = {"verbatim", "verbatim*", "Verbatim", "lstlisting", "minted"}
TEX_PROSE_ENVIRONMENTS = {"abstract", "enumerate", "itemize", "description", "document"}


def tex_group(text: str, start: int) -> tuple[str, int] | None:
    """Read one balanced literal group, without evaluating its contents."""
    while start < len(text) and text[start].isspace():
        start += 1
    if start >= len(text) or text[start] != "{":
        return None
    depth, index = 1, start + 1
    while index < len(text):
        if text[index] == "\\":
            index += 2
            continue
        if text[index] == "{":
            depth += 1
        elif text[index] == "}":
            depth -= 1
            if depth == 0:
                return text[start + 1:index], index + 1
        index += 1
    return None


def tex_reading_regions(text: str, *, structured: bool = False) -> list[tuple[int, int]]:
    """Protect literal examples first; optional non-prose environments/math stay raw."""
    regions: list[tuple[int, int]] = []
    token = re.compile(r"%|\\verb\*?(?![A-Za-z@])|\\begin\s*\{([^{}]+)\}|\$\$?|\\[\[(]")
    index = 0
    while match := token.search(text, index):
        first, last = match.span()
        index = last
        prefix = text[text.rfind("\n", 0, first) + 1:first]
        if match.group() == "%":
            if tex_comment_start(prefix + "%") is not None:
                ending = text.find("\n", last)
                index = ending + 1 if ending >= 0 else len(text)
            continue
        # Escaped dollars and command-like examples preceded by an odd slash run.
        previous = first - 1
        while previous >= 0 and text[previous] == "\\":
            previous -= 1
        if (first - previous - 1) % 2:
            continue
        environment = match.group(1)
        if match.group().startswith("\\verb"):
            if last >= len(text) or text[last].isspace():
                raise ValueError("unsupported or unterminated inline verbatim")
            ending = text.find(text[last], last + 1)
            if ending < 0:
                raise ValueError("unterminated inline verbatim")
            last = ending + 1
        elif environment:
            if environment not in TEX_LITERAL_ENVIRONMENTS and (not structured or environment in TEX_PROSE_ENVIRONMENTS):
                continue
            edge = re.compile(r"\\(begin|end)\s*\{" + re.escape(environment) + r"\}")
            depth = 1
            edge_text = text if environment in TEX_LITERAL_ENVIRONMENTS else tex_reading_mask(text)
            for closing in edge.finditer(edge_text, last):
                depth += 1 if closing.group(1) == "begin" else -1
                if depth == 0:
                    last = closing.end()
                    break
            else:
                raise ValueError(f"unterminated retained environment: {environment}")
        elif structured:
            closing = {"\\[": "\\]", "\\(": "\\)"}.get(match.group(), match.group())
            ending = re.compile(r"(?<!\\)" + re.escape(closing)).search(text, last)
            if ending is None:
                raise ValueError("unterminated retained math expression")
            last = ending.end()
        else:
            continue
        regions.append((first, last))
        index = last
    if structured:
        # Use the same-length mask for locations; comments must not shift offsets.
        searchable = tex_reading_mask(text)
        stack: list[int] = []
        for match in re.finditer(r"\\(?:if[A-Za-z@]*|fi)\b", searchable):
            if match.group() == "\\fi":
                if not stack:
                    raise ValueError("unmatched conditional closing expression")
                first = stack.pop()
                if not stack:
                    regions.append((first, match.end()))
            else:
                stack.append(match.start())
        if stack:
            raise ValueError("unterminated conditional expression")
        for declaration in tex_reading_definitions(searchable):
            regions.append((declaration["start"], declaration["end"]))
        merged: list[tuple[int, int]] = []
        for first, last in sorted(regions):
            if merged and first < merged[-1][1]:
                merged[-1] = (merged[-1][0], max(last, merged[-1][1]))
            else:
                merged.append((first, last))
        return merged
    return regions


def tex_reading_definitions(text: str) -> list[dict[str, Any]]:
    """Recognize a finite declaration shape, not arbitrary TeX definitions."""
    result: list[dict[str, Any]] = []
    pattern = re.compile(r"\\(newcommand|renewcommand|providecommand|DeclareRobustCommand)\*?\s*(?:\{\s*(\\[A-Za-z@]+)\s*\}|(\\[A-Za-z@]+))|\\(def|gdef|edef|xdef|let)\s*(\\[A-Za-z@]+)")
    index = 0
    while match := pattern.search(text, index):
        command, name = match.group(1) or match.group(4), match.group(2) or match.group(3) or match.group(5)
        last, count = match.end(), 0
        option = re.match(r"\s*\[([0-9]+)\]", text[last:])
        if option:
            count, last = int(option.group(1)), last + option.end()
        if command in {"def", "gdef", "edef", "xdef"}:
            arguments = re.match(r"((?:#[1-9])*)\s*", text[last:])
            count, last = len(arguments.group(1)) // 2, last + arguments.end()
        group = tex_group(text, last)
        if group is not None:
            body, last = group
        else:
            ending = text.find("\n", last)
            body, last = None, ending if ending >= 0 else len(text)
        result.append({"start": match.start(), "end": last, "name": name[1:], "command": command, "count": count, "body": body, "raw": text[match.start():last]})
        index = max(last, match.end())
    return result


def tex_reading_mask(text: str, *, definitions: bool = False) -> str:
    """Same-length lexical mask: examples/comments/conditional branches are not body."""
    regions = tex_reading_regions(text)
    masked = list(text)
    def hide(first: int, last: int) -> None:
        masked[first:last] = ["\n" if char == "\n" else " " for char in text[first:last]]
    for first, last in regions:
        hide(first, last)
    searchable = "".join(masked)
    for match in re.finditer(r"(?m)^.*$", searchable):
        comment = tex_comment_start(match.group())
        if comment is not None:
            hide(match.start() + comment, match.end())
    if definitions:
        searchable = "".join(masked)
        for declaration in tex_reading_definitions(searchable):
            hide(declaration["start"], declaration["end"])
        searchable = "".join(masked)
        stack: list[int] = []
        for match in re.finditer(r"\\(?:if[A-Za-z@]*|fi)\b", searchable):
            if match.group() == "\\fi":
                if stack:
                    first = stack.pop()
                    if not stack:
                        hide(first, match.end())
            else:
                stack.append(match.start())
        if stack:
            raise ValueError("unterminated conditional expression")
    return "".join(masked)


def tex_reading_body(text: str) -> tuple[int, int]:
    searchable = tex_reading_mask(text, definitions=True)
    begins = list(re.finditer(r"\\begin\s*\{document\}", searchable))
    ends = list(re.finditer(r"\\end\s*\{document\}", searchable))
    if len(begins) != 1 or len(ends) != 1 or ends[0].start() < begins[0].end():
        raise ValueError("reading view needs one explicit, unambiguous document boundary")
    return begins[0].end(), ends[0].start()


def tex_reading_macros(text: str, diagnostics: list[dict[str, str]]) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    # Read definitions with literals/comments masked, but include conditional defs in
    # the count: they cannot accidentally make a same-named static macro admissible.
    searchable = tex_reading_mask(text)
    declarations = tex_reading_definitions(searchable)
    counts = Counter(item["name"] for item in declarations)
    macros: dict[str, dict[str, Any]] = {}
    has_conditions = bool(re.search(r"\\if[A-Za-z@]*\b", searchable))
    begin = re.search(r"\\begin\s*\{document\}", tex_reading_mask(text, definitions=True))
    preamble_end = begin.start() if begin else 0
    has_explicit_groups = bool(re.search(r"\\(?:begingroup|bgroup|catcode|csname|expandafter)\b", searchable[:preamble_end]))
    for item in declarations:
        original = text[item["start"]:item["end"]]
        prefix = re.sub(r"\\.", "", searchable[:item["start"]])
        top_level = prefix.count("{") == prefix.count("}")
        safe_shape = (original == item["raw"] and item["body"] is not None and item["command"] == "newcommand"
                      and item["start"] < preamble_end and top_level and counts[item["name"]] == 1
                      and not has_conditions and not has_explicit_groups)
        item["raw"] = original
        if safe_shape and (item["count"] == 0 or item["count"] == 1 and not item["body"].strip()):
            macros[item["name"]] = item
        else:
            macros[item["name"]] = {**item, "count": -1}
            diagnostics.append({"kind": "unexpanded_macro_definition", "macro": item["name"]})
    return macros, declarations


def tex_reading_inline(text: str, macros: dict[str, dict[str, Any]], *, stack: tuple[str, ...] = ()) -> tuple[str, bool]:
    """Only static prose, nested formatting, explicit ref keys; no numbered guesses."""
    parts: list[str] = []
    safe, index = True, 0
    wrappers = {"emph", "textbf", "textit", "texttt", "textsc", "textrm", "textnormal", "underline"}
    references = {"ref", "eqref", "autoref", "cref", "Cref", "cite", "citep", "citet", "citealp", "citeauthor", "citeyear"}
    while index < len(text):
        if text[index] != "\\":
            if text[index] in "${}#^_&":
                safe = False
            parts.append(" " if text[index] == "~" else text[index])
            index += 1
            continue
        match = re.match(r"\\([A-Za-z@]+)\*?|\\(.)", text[index:], re.DOTALL)
        if match is None:
            return text, False
        name, symbol = match.groups()
        last = index + match.end()
        if name is not None and match.group().endswith("*"):
            return text, False
        if symbol is not None:
            if symbol in "%&_#${}":
                parts.append(symbol)
            elif symbol == " ":
                parts.append(" ")
            else:
                parts.append(match.group())
                safe = False
        elif name in macros:
            if name in stack or len(stack) >= 20:
                return text, False
            macro = macros[name]
            if macro["count"] not in {0, 1}:
                return text, False
            if macro["count"] == 1:
                group = tex_group(text, last)
                if group is None:
                    return text, False
                last = group[1]
            else:
                value, admissible = tex_reading_inline(macro["body"], macros, stack=stack + (name,))
                if not admissible:
                    return text, False
                parts.append(value)
                # Empty delimiter groups after zero-argument commands are layout.
                group = tex_group(text, last)
                if group is not None and not group[0]:
                    last = group[1]
        elif name in wrappers | references | {"label", "url", "href"}:
            option = re.match(r"\s*(?:\[[^\]\n]*\]\s*)*", text[last:])
            if "[" in option.group():
                return text, False  # Optional notes may qualify the assertion.
            last += option.end()
            group = tex_group(text, last)
            if group is None:
                return text, False
            value, last = group
            if name in wrappers:
                value, admissible = tex_reading_inline(value, macros, stack=stack)
                safe = safe and admissible
                parts.append(value)
            elif name == "href":
                return text, False  # Do not silently discard a link target.
            elif name != "label":
                if name in references and ("\n" in value or "\r" in value or not re.fullmatch(r"[A-Za-z0-9_.:/+\-]+(?:[ \t]*,[ \t]*[A-Za-z0-9_.:/+\-]+)*", value.strip())):
                    return text, False
                if name == "url" and not re.fullmatch(r"[A-Za-z][A-Za-z0-9+.\-]*:[^\s\\{}<>]+", value):
                    return text, False
                parts.append(f"[{('cite' if name.startswith('cite') else 'ref')}: {value}]" if name in references else value)
        elif name == "S":
            parts.append("§")
        else:
            parts.append(match.group())
            safe = False
        index = last
    return "".join(parts), safe


def tex_reading_fence(text: str, language: str = "latex") -> str:
    fence = "`" * max(3, max((len(run) + 1 for run in re.findall(r"`+", text)), default=3))
    ending = "" if text.endswith("\n") else "\n"
    return f"\n\n{fence}{language}\n{text}{ending}{fence}\n\n"


def derive_tex_reading(main_path: str, files: dict[str, str], citation_support: list[str]) -> tuple[str, dict[str, Any]]:
    """Conservative opt-in view; all uncertain expressions remain local raw TeX."""
    diagnostics: list[dict[str, str]] = []
    graph: list[dict[str, str]] = []
    source_begin, source_end = tex_reading_body(files[main_path])
    flattened = flatten_tex(main_path, files, reading_view=True, diagnostics=diagnostics, include_graph=graph)
    if diagnostics:
        raise ValueError("reading include preflight failed: " + json.dumps(diagnostics, ensure_ascii=False))
    begin, end = tex_reading_body(flattened)
    macros, declarations = tex_reading_macros(flattened, diagnostics)
    if {"begin", "end"}.intersection(macros):
        raise ValueError("redefined document/environment control is outside the reading profile")
    if re.search(r"\\abstract\b|\\begin\s*\{abstract\}", tex_reading_mask(flattened[:begin], definitions=True)):
        diagnostics.append({"kind": "preamble_semantic_abstract_omitted", "path": main_path})
    body = flattened[begin:end]
    regions = tex_reading_regions(body, structured=True)
    # Comments outside retained expressions only. Inline verbatim/code percent and
    # structural math/table comments remain byte-faithful within their fences.
    cleaned: list[str] = []
    position = 0
    for start, stop in regions:
        cleaned.extend([tex_without_comments(body[position:start]), body[start:stop]])
        position = stop
    cleaned.append(tex_without_comments(body[position:]))
    body = "".join(cleaned)
    regions = dict(tex_reading_regions(body, structured=True))
    parts = ["# Conservative TeX reading view\n\n> Collector-derived reading representation, not a raw-source quotation. Static prose transformations are limited; LaTeX math, algorithms, tables and uncertain expressions are retained without execution. Reference keys are not inferred citation numbers.\n"]
    paragraph: list[str] = []
    index = 0
    def flush() -> None:
        if not paragraph:
            return
        original = "".join(paragraph).strip()
        paragraph.clear()
        if not original:
            return
        value, admissible = tex_reading_inline(original, macros)
        if admissible:
            if value.strip():
                parts.append("\n\n" + value.strip() + "\n")
        else:
            parts.append(tex_reading_fence(original))
            diagnostics.append({"kind": "retained_tex_fallback", "expression": original[:160]})
    while index < len(body):
        # Proven no-op consumes its entire group before nested old abstracts or
        # structured expressions are considered active content.
        command = re.match(r"\\([A-Za-z@]+)\*?", body[index:])
        if command and not command.group().endswith("*") and command.group(1) in macros and macros[command.group(1)]["count"] == 1:
            group = tex_group(body, index + command.end())
            if group is None:
                raise ValueError("proven no-op invocation has no balanced argument")
            index = group[1]
            continue
        if index in regions:
            stop = regions[index]
            retained = body[index:stop]
            environment_name = re.match(r"\\begin\s*\{([^{}]+)\}", retained)
            math_environment = environment_name and environment_name.group(1) in {"equation", "equation*", "align", "align*", "gather", "gather*", "displaymath", "math"}
            if retained.startswith(("$", "\\[", "\\(")) or math_environment:
                # Keep all qualifiers in the same original paragraph. Splitting at
                # inline math can turn a conditional source statement into a claim
                # with its assumptions removed.
                paragraph.append(retained)
                index = stop
                continue
            flush()
            parts.append(tex_reading_fence(retained))
            known = TEX_LITERAL_ENVIRONMENTS | {"equation", "equation*", "align", "align*", "gather", "gather*", "displaymath", "math", "table", "table*", "tabular", "tabular*", "longtable", "algorithm", "algorithmic", "figure", "figure*", "tikzpicture", "proof", "theorem", "proposition"}
            if retained.startswith("\\if") or environment_name and environment_name.group(1) not in known:
                diagnostics.append({"kind": "retained_uncertain_expression", "expression": retained[:160]})
            index = stop
            continue
        heading = re.match(r"\\((?:sub){0,2}section|paragraph)\*?\s*", body[index:])
        if heading and heading.group(1) not in macros:
            group = tex_group(body, index + heading.end())
            if group is None:
                raise ValueError("unsupported or unbalanced section title")
            flush()
            value, admissible = tex_reading_inline(group[0], macros)
            if admissible:
                parts.append("\n\n" + "#" * (2 if heading.group(1) == "section" else 3 if heading.group(1) == "subsection" else 4) + " " + value + "\n")
            else:
                expression = body[index:group[1]]
                parts.append(tex_reading_fence(expression))
                diagnostics.append({"kind": "retained_unsafe_heading", "expression": expression[:160]})
            index = group[1]
            continue
        environment = re.match(r"\\(begin|end)\s*\{(abstract|enumerate|itemize|description)\}", body[index:])
        if environment:
            flush()
            if environment.group(2) == "abstract" and environment.group(1) == "begin":
                parts.append("\n\n## Abstract\n")
            index += environment.end()
            continue
        layout = re.match(r"\\(?:maketitle|appendix|bibliographystyle\s*\{[^{}]*\}|bibliography\s*\{[^{}]*\}|label\s*\{[^{}]*\})(?![A-Za-z@])", body[index:])
        if layout and (command is None or command.group(1) not in macros):
            index += layout.end()
            continue
        item = re.match(r"\\item\b", body[index:])
        if item and "item" not in macros:
            flush()
            paragraph.append("- ")
            index += item.end()
            continue
        if command:
            last = index + command.end()
            option = re.match(r"\s*(?:\[[^\]\n]*\]\s*)*", body[last:])
            last += option.end()
            group = tex_group(body, last)
            if group:
                last = group[1]
                while following := tex_group(body, last):
                    last = following[1]
                expression = body[index:last]
                # Atomic argument consumption: nested environments, headings and
                # blank lines in an unproven macro never leak into active prose.
                # Keep surrounding prose too, since optional notes may qualify it.
                paragraph.append(expression)
                index = last
                continue
        if body[index] == "\\" and index + 1 < len(body) and not re.match(r"[A-Za-z@]", body[index + 1]):
            paragraph.append(body[index:index + 2])
            index += 2
            continue
        if body[index] == "{":
            group = tex_group(body, index)
            if group is None:
                raise ValueError("unbalanced literal body group")
            paragraph.append(body[index:group[1]])
            index = group[1]
            continue
        if body.startswith("\n\n", index):
            flush()
            index += 2
            continue
        paragraph.append(body[index])
        index += 1
    flush()
    if declarations:
        parts.append("\n\n## Local macro definitions (not executed)\n" + tex_reading_fence("\n".join(item["raw"] for item in declarations)))
    for name in citation_support:
        if name not in files or PurePosixPath(name).suffix.lower() not in {".bib", ".bbl"}:
            raise ValueError("citation support must be a retained local .bib/.bbl file")
        parts.append(f"\n\n## Citation support: {name}\n\n> Collector-provided local citation support, not the author's typeset References; may include uncited entries. No cited works were fetched.\n" + tex_reading_fence(files[name], "bibtex" if name.endswith(".bib") else "latex"))
    return "".join(parts).strip() + "\n", {
        "body_start_line": files[main_path].count("\n", 0, source_begin) + 1,
        "body_end_line": files[main_path].count("\n", 0, source_end) + 1,
        "include_graph": graph, "diagnostics": diagnostics,
    }


def tex_reading_selectors(document: Path, text: str, source_paths: list[str], files: dict[str, str]) -> list[dict[str, Any]]:
    local_path = document.relative_to(ROOT).as_posix()
    lines = text.splitlines()
    provenance = {"derived_from": source_paths[0], "source_paths": source_paths, "transformation": TEX_READING_TRANSFORMATION, "reading_profile": TEX_READING_PROFILE}
    headings = extract_markdown_headings(text, local_path, structured=True)
    rows = [{"selector": f"derived://{local_path}#L1-L{len(lines)}", "local_path": local_path,
             "kind": "file", "start_line": 1, "end_line": len(lines), "text_preview": lines[0], **provenance}]
    # Locate nested titles in original files with the same balanced-group parser.
    original_headings: dict[str, list[tuple[str, int]]] = defaultdict(list)
    for source_path, original in files.items():
        if Path(source_path).suffix.lower() not in {".tex", ".ltx", ".txt"}:
            continue
        macros, _ = tex_reading_macros(original, [])
        searchable = tex_reading_mask(original, definitions=True)
        for match in re.finditer(r"\\(?:section|subsection|subsubsection|paragraph)\*?\s*", searchable):
            group = tex_group(original, match.end())
            if group:
                heading, admissible = tex_reading_inline(group[0], macros)
                original_headings[heading if admissible else group[0]].append((source_path, original.count("\n", 0, match.start()) + 1))
    for number, heading in enumerate(headings):
        if heading["level"] == 1:
            continue
        start = heading["line"]
        end = headings[number + 1]["line"] - 1 if number + 1 < len(headings) else len(lines)
        row = {"selector": f"derived://{local_path}#L{start}-L{end}", "local_path": local_path,
               "kind": "section", "heading": heading["heading"], "start_line": start, "end_line": end,
               "text_preview": lines[start - 1], **provenance}
        locations = original_headings.get(heading["heading"], [])
        if len(locations) == 1:
            row["source_heading_path"], row["source_heading_line"] = locations[0]
        rows.append(row)
    return rows


def replay_arxiv_tex_reading(
    record: SourceRecord, manifest: dict[str, Any] | None = None, generated_at: str | None = None,
) -> dict[str, Any]:
    """Opt-in offline replay. Preflight everything before writing only owned derivatives."""
    root = record.capsule_root
    try:
        manifest = load_yaml(root / "manifest.yaml") if manifest is None else manifest
        materialization = manifest["materialization"]
        view = materialization["tex_reading_view"]
        if view.get("enabled") is not True or view.get("profile") != TEX_READING_PROFILE:
            raise ValueError("reading replay needs explicit enabled conservative-v1 opt-in")
        if manifest.get("adapter") != "arxiv_latex_v2" or manifest.get("uid") != record.uid or manifest.get("canonical_id") != record.canonical_id:
            raise ValueError("reading replay identity/adapter differs from retained capsule")
        source_metadata = load_yaml(root / "source-metadata.yaml")
        version = (record.metadata.get("versioning") or {}).get("source_version")
        if not isinstance(version, str) or not re.fullmatch(r"v[1-9]\d*", version) or (source_metadata.get("versioning") or {}).get("source_version") != version:
            raise ValueError("reading replay needs the retained selected arXiv version")
        source_rows = [json.loads(line) for line in (root / "files.jsonl").read_text(encoding="utf-8").splitlines() if line.strip()]
        inventory = {item["path"]: item for item in manifest["local_files"]}
        stored: dict[str, str] = {}
        def check_file(path: Path) -> str:
            path.resolve().relative_to(root.resolve())
            relative = path.relative_to(ROOT).as_posix()
            item = inventory.get(relative)
            if not item or item.get("bytes") != path.stat().st_size or item.get("sha256") != sha256_file(path):
                raise ValueError(f"retained reading input differs from inventory: {relative}")
            return relative
        check_file(root / "files.jsonl")
        for item in source_rows:
            path = (ROOT / item["path"]).resolve()
            path.relative_to((root / "source").resolve())
            check_file(path)
            if item.get("bytes") != path.stat().st_size or item.get("sha256") != sha256_file(path):
                raise ValueError("retained source differs from files.jsonl")
            name = path.relative_to(root / "source").as_posix()
            stored[name] = path.read_bytes().decode("utf-8")
        declared = sanitize_relative_path(view["source_root"])
        if declared is None or declared.parts[0] != "source":
            raise ValueError("reading root must be a retained source path")
        main_path = PurePosixPath(*declared.parts[1:]).as_posix()
        candidates = tex_root_candidates({
            name: tex_reading_mask(text, definitions=True)
            for name, text in stored.items()
            if PurePosixPath(name).suffix.lower() in {".tex", ".ltx", ".txt"}
        })
        if candidates != [main_path]:
            raise ValueError("declared reading root is absent or ambiguous in retained originals")
        if view.get("document") != "normalized/reading.md":
            raise ValueError("reading view writes only normalized/reading.md")
        legacy = view.get("legacy_documents", ["normalized/document.tex", "normalized/document.txt"])
        if legacy != ["normalized/document.tex", "normalized/document.txt"]:
            raise ValueError("reading view must retain both legacy normalized documents")
        for name in legacy:
            check_file(root / name)
        selector_file = root / "selectors.jsonl"
        check_file(selector_file)
        original_lines = selector_file.read_bytes().splitlines(keepends=True)
        if original_lines and not original_lines[-1].endswith(b"\n"):
            raise ValueError("retained selector prefix needs its existing newline boundary")
        selector_rows = [json.loads(line) for line in original_lines]
        legacy_count = view.get("legacy_selector_count", len(selector_rows))
        if not isinstance(legacy_count, int) or isinstance(legacy_count, bool) or not 0 <= legacy_count <= len(selector_rows):
            raise ValueError("invalid legacy selector count")
        document = root / view["document"]
        if document.is_symlink():
            raise ValueError("reading derivative cannot alias a retained original")
        document_relative = document.relative_to(ROOT).as_posix()
        if any(row.get("local_path") != document_relative or row.get("reading_profile") != TEX_READING_PROFILE for row in selector_rows[legacy_count:]):
            raise ValueError("reading replay cannot replace unrelated appended selectors")
        if any(row.get("local_path") == document_relative for row in selector_rows[:legacy_count]):
            raise ValueError("reading selectors cannot be part of the legacy prefix")
        support = view.get("citation_support", [])
        if not isinstance(support, list) or len(set(support)) != len(support):
            raise ValueError("citation support must be a finite unique retained path list")
        support_names: list[str] = []
        for name in support:
            safe_path = sanitize_relative_path(name)
            if safe_path is None or safe_path.parts[0] != "source":
                raise ValueError("citation support must stay in retained source")
            support_names.append(PurePosixPath(*safe_path.parts[1:]).as_posix())
        text, assessment = derive_tex_reading(main_path, stored, support_names)
        paths = [main_path, *[item["to"] for item in assessment["include_graph"]], *support_names]
        paths = list(dict.fromkeys(paths))
        source_paths = [(root / "source" / name).relative_to(ROOT).as_posix() for name in paths]
        selectors = tex_reading_selectors(document, text, source_paths, {source_paths[paths.index(name)]: stored[name] for name in paths})
        package = (record.metadata.get("rights") or {}).get("redistribution_package")
        if package:
            if package.get("source_revision") != manifest.get("revision"):
                raise ValueError("redistribution package does not cover retained revision")
            for field in ("source_revision", "source_version_url", "notice_path", "attribution", "modifications", "scope"):
                if not isinstance(package.get(field), str) or not package[field].strip():
                    raise ValueError(f"redistribution package is missing {field}")
            notice = (ROOT / package["notice_path"]).resolve()
            notice.relative_to(ROOT.resolve())
            if not notice.read_text(encoding="utf-8").strip():
                raise ValueError("redistribution notice is empty")
        # All checks/derivation are complete: no prepare, fetch, original write or
        # legacy normalization. The finalizer touches only the chosen new consumer.
        document.parent.mkdir(parents=True, exist_ok=True)
        document.write_text(text, encoding="utf-8")
        suffix = b"".join((json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n").encode("utf-8") for row in selectors)
        selector_file.write_bytes(b"".join(original_lines[:legacy_count]) + suffix)
        materialization.update({"document": view["document"], "normalized_document": view["document"], "stored_characters": len(text), "selector_count": legacy_count + len(selectors)})
        view.update({"legacy_documents": legacy, "legacy_selector_count": legacy_count, "source_paths": source_paths, **assessment})
        if generated_at is not None:
            manifest["generated_at"] = generated_at
        return finalize_capsule(record, root, manifest)
    except (KeyError, TypeError, AttributeError, ValueError, OSError, UnicodeError, yaml.YAMLError) as exc:
        raise ArxivPreflightError(f"{record.uid}: {exc}; retained originals and legacy representations preserved") from exc


def write_arxiv_tex_derivatives(
    record: SourceRecord,
    root: Path,
    stored: dict[str, str],
    *,
    revision: str,
) -> dict[str, Any]:
    """Reuse retained source text; write only normalized files and selectors."""
    source_root = root / "source"
    root_exclusions: list[dict[str, str]] = []
    candidates = tex_root_candidates(stored, exclusions=root_exclusions)
    main_tex = candidates[0] if len(candidates) == 1 else None
    diagnostics: list[dict[str, str]] = []
    normalization_diagnostics: list[dict[str, str]] = []
    include_graph: list[dict[str, str]] = []
    normalized: dict[str, str] = {}
    if main_tex:
        flattened = flatten_tex(main_tex, stored, diagnostics=diagnostics, include_graph=include_graph)
        normalized = {
            "normalized/document.tex": flattened,
            "normalized/document.txt": tex_to_plain(flattened, diagnostics=normalization_diagnostics, path=main_tex),
        }
        for path, text in normalized.items():
            destination = root / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_text(text, encoding="utf-8")

    selectors: list[dict[str, Any]] = []
    revision_selector = revision.split(":", 1)[-1][:16]
    for path, text in sorted(stored.items()):
        lines = text.splitlines()
        selector_base = f"arxiv://{record.canonical_id}@sha256-{revision_selector}/{path}"
        selectors.append({
            "selector": f"{selector_base}#L1-L{max(1, len(lines))}",
            "local_path": (source_root / path).relative_to(ROOT).as_posix(),
            "kind": "file", "start_line": 1, "end_line": max(1, len(lines)),
        })
        for line_number, line in enumerate(lines, 1):
            match = re.search(r"\\(section|subsection|subsubsection|paragraph)\*?\{([^{}]+)\}", line)
            if match:
                selectors.append({
                    "selector": f"{selector_base}#L{line_number}",
                    "local_path": (source_root / path).relative_to(ROOT).as_posix(),
                    "kind": match.group(1), "heading": match.group(2).strip(),
                    "start_line": line_number, "end_line": line_number,
                })
    for path, text in sorted(normalized.items()):
        lines = text.splitlines()
        selector_base = f"arxiv://{record.canonical_id}@sha256-{revision_selector}/{path}"
        provenance = {"derived_from": f"source/{main_tex}", "transformation": "TeX include expansion"}
        if path.endswith(".txt"):
            provenance["transformation"] += " and lossy plain-text normalization; preamble excluded"
        selectors.append({
            "selector": f"{selector_base}#L1-L{max(1, len(lines))}",
            "local_path": (root / path).relative_to(ROOT).as_posix(),
            "kind": "file", "start_line": 1, "end_line": max(1, len(lines)),
            **({"text_preview": next(line for line in lines if line.strip())} if text.strip() else {}),
            **provenance,
        })
        if path.endswith(".txt"):
            headings = [(number, re.match(r"^(#{2,3})\s+(.+)$", line)) for number, line in enumerate(lines, 1)]
            headings = [(number, match) for number, match in headings if match is not None]
            for index, (start, match) in enumerate(headings):
                end = headings[index + 1][0] - 1 if index + 1 < len(headings) else len(lines)
                selectors.append({
                    "selector": f"{selector_base}#L{start}-L{end}",
                    "local_path": (root / path).relative_to(ROOT).as_posix(),
                    "kind": "section", "heading": match.group(2),
                    "start_line": start, "end_line": end,
                    "text_preview": next((line for line in lines[start:end] if line.strip()), lines[start - 1])[:700],
                    **provenance,
                })
    write_jsonl(root / "selectors.jsonl", selectors)
    return {
        "main_tex": main_tex, "tex_root_candidates": candidates, "tex_root_exclusions": root_exclusions,
        "document": "normalized/document.txt" if main_tex else None,
        "normalized_document": "normalized/document.txt" if main_tex else None,
        "normalized_tex": "normalized/document.tex" if main_tex else None,
        "tex_include_graph": include_graph, "tex_include_errors": diagnostics,
        "tex_normalization_diagnostics": normalization_diagnostics,
        "selector_count": len(selectors),
    }


def materialize_arxiv(record: SourceRecord, config: dict[str, Any], generated_at: str) -> dict[str, Any]:
    root = record.capsule_root
    if (root / "manifest.yaml").is_file():
        retained = load_yaml(root / "manifest.yaml")
        retained_materialization = retained.get("materialization") if isinstance(retained, dict) else None
        if isinstance(retained_materialization, dict) and isinstance(retained_materialization.get("tex_reading_view"), dict) and retained_materialization["tex_reading_view"].get("enabled") is True:
            return replay_arxiv_tex_reading(record, retained)
    manifest = base_manifest(record, "arxiv_latex_v2", generated_at)
    arxiv_id = record.canonical_id
    if not arxiv_id:
        if root.exists():
            raise ArxivPreflightError(f"{record.uid}: missing arXiv identifier; retained capsule unchanged")
        root = prepare_capsule(record)
        manifest["errors"].append("missing arXiv identifier")
        return finalize_capsule(record, root, manifest)

    try:
        requested_arxiv_id = arxiv_eprint_id(record)
    except ValueError as exc:
        if root.exists():
            raise ArxivPreflightError(f"{record.uid}: {exc}; retained capsule unchanged") from exc
        root = prepare_capsule(record)
        manifest["errors"].append(str(exc))
        return finalize_capsule(record, root, manifest)
    quoted_id = urllib.parse.quote(requested_arxiv_id, safe="/")
    urls = [
        f"https://export.arxiv.org/e-print/{quoted_id}",
        f"https://arxiv.org/e-print/{quoted_id}",
    ]
    payload: bytes | None = None
    payload_kind: str | None = None
    resolved_url: str | None = None
    headers: dict[str, str] = {}
    for url in urls:
        try:
            candidate_payload, candidate_url, candidate_headers = fetch_bytes(
                url,
                timeout=int(config.get("http_timeout_seconds", 45)),
                max_bytes=int(config.get("arxiv_max_archive_bytes", 60_000_000)),
            )
            candidate_kind = classify_arxiv_payload(candidate_payload)
            content_type = (candidate_headers.get("content-type") or "").lower()
            if candidate_kind is None or (
                "application/pdf" in content_type and candidate_kind not in {"pdf", "gzip-pdf"}
            ):
                manifest["warnings"].append(
                    f"rejected unsupported arXiv e-print payload from {candidate_url or url} "
                    f"(content-type {content_type or 'unreported'})"
                )
                continue
            payload = candidate_payload
            payload_kind = candidate_kind
            resolved_url = candidate_url
            headers = candidate_headers
            break
        except Exception as exc:
            manifest["warnings"].append(str(exc))
    if payload is None:
        if root.exists():
            raise ArxivPreflightError(f"{record.uid}: arXiv source archive could not be acquired; retained capsule unchanged")
        root = prepare_capsule(record)
        manifest["errors"].append("arXiv source archive could not be acquired")
        # Preserve a bounded local copy of the abstract page when the source archive fails.
        manifest["adapter"] = "generic_web_or_document_v2"
        return materialize_generic(
            record,
            config,
            generated_at,
            existing_root=root,
            existing_manifest=manifest,
            force_excerpt_reason=(
                "arXiv source archive was unavailable; the landing or abstract page is fallback evidence, not full text."
            ),
        )

    archive_hash = sha256_bytes(payload)
    manifest["revision"] = f"sha256:{archive_hash}"
    manifest["retrievals"].append(
        {
            "requested_urls": urls,
            "resolved_url": resolved_url,
            "content_type": headers.get("content-type"),
            "bytes": len(payload),
            "sha256": archive_hash,
        }
    )
    pdf_payload, pdf_container = arxiv_pdf_payload(payload)
    if pdf_payload is not None and pdf_container is not None:
        root = prepare_capsule(record)
        manifest["adapter"] = "arxiv_pdf_v1"
        manifest["archive_container"] = pdf_container
        manifest["media_type"] = "application/pdf"
        manifest["retrievals"][-1]["detected_media_type"] = "application/pdf"

        source_root = root / "source"
        source_root.mkdir(parents=True, exist_ok=True)
        source_pdf = source_root / "document.pdf"
        source_pdf.write_bytes(pdf_payload)
        source_pdf_hash = sha256_bytes(pdf_payload)
        document_text = ""
        selectors: list[dict[str, Any]] = []
        page_count: int | None = None
        extraction_failed_pages: list[int] = []
        pages_without_text: list[int] = []
        try:
            document_text, extracted_selectors, page_count = extract_pdf_text(pdf_payload)
            for selector in extracted_selectors:
                page = selector.get("page")
                preview = selector.get("text_preview")
                if isinstance(preview, str) and preview.startswith("[page extraction failed:"):
                    if isinstance(page, int):
                        extraction_failed_pages.append(page)
                    continue
                if not isinstance(preview, str) or not preview.strip():
                    if isinstance(page, int):
                        pages_without_text.append(page)
                    continue
                selector["selector"] = selector["selector"].replace(
                    "sha256-PENDING", f"sha256-{source_pdf_hash[:16]}"
                )
                selectors.append(selector)
        except Exception as exc:
            manifest["errors"].append(f"PDF parsing failed: {exc}")

        substantive_text = has_substantive_document_text(document_text) if document_text else False
        document_name: str | None = None
        if document_text:
            document_name = "document.txt"
            document_path = root / document_name
            document_path.write_text(document_text, encoding="utf-8")
            if selectors:
                local_path = document_path.relative_to(ROOT).as_posix()
                for selector in selectors:
                    selector["local_path"] = local_path
                write_jsonl(root / "selectors.jsonl", selectors)
                manifest["selectors"] = ["selectors.jsonl"]

        limitations: list[str] = []
        if pages_without_text:
            limitations.append(
                "PDF pages without extractable text: "
                + ", ".join(str(page) for page in pages_without_text)
                + "; the original PDF is preserved and no OCR was performed."
            )
        if extraction_failed_pages:
            limitations.append(
                "PDF text extraction failed on pages: "
                + ", ".join(str(page) for page in extraction_failed_pages)
                + "; the original PDF is preserved."
            )

        if substantive_text and selectors and not extraction_failed_pages:
            manifest["content_tier"] = "full_text"
            manifest["status"] = "partial" if pages_without_text else "materialized"
        elif selectors:
            manifest["content_tier"] = "excerpt_capsule"
            manifest["status"] = "partial"
        else:
            manifest["content_tier"] = "metadata_capsule"
            manifest["status"] = "partial"
            if page_count == 0:
                manifest["warnings"].append("PDF contained no pages; retained only as acquisition evidence.")
            elif not manifest["errors"]:
                manifest["warnings"].append(
                    "PDF contained no substantive extractable text; the original PDF was retained without OCR."
                )
        manifest["warnings"].extend(limitations)
        if limitations:
            manifest["limitations"] = limitations
        manifest["rights"] = {
            "declared_access": record.rights_access,
            "full_text_redistribution_assumed": True,
            "basis": "arXiv e-print PDF",
        }
        manifest["materialization"] = {
            "document": document_name,
            "normalized_document": document_name,
            "source_pdf": "source/document.pdf",
            "source_pdf_sha256": source_pdf_hash,
            "stored_characters": len(document_text),
            "selector_count": len(selectors),
            "pdf_page_count": page_count,
            "pdf_text_page_count": len(selectors),
            "pdf_pages_without_extractable_text": pages_without_text,
            "pdf_page_extraction_failures": extraction_failed_pages,
            "substantive_text": substantive_text,
        }
        return finalize_capsule(record, root, manifest)

    bundle, container_kind = unpack_arxiv(payload)
    if payload_kind not in {"tar", "single", "gzip-single"}:
        raise RuntimeError(f"unsupported classified arXiv payload: {payload_kind}")
    manifest["archive_container"] = container_kind

    stored: dict[str, str] = {}
    omitted: list[dict[str, str]] = []
    total_bytes = 0
    max_total = int(config.get("arxiv_max_stored_text_bytes", 30_000_000))
    max_files = int(config.get("arxiv_max_files", 2500))
    max_file = int(config.get("arxiv_max_single_file_bytes", 6_000_000))
    for original_name, raw in bundle:
        if len(stored) >= max_files:
            omitted.append({"path": original_name, "reason": "file-count-budget"})
            continue
        pure = PurePosixPath(original_name.replace("\\", "/"))
        if pure.is_absolute() or ".." in pure.parts:
            omitted.append({"path": original_name, "reason": "unsafe-path"})
            continue
        parts = [part for part in pure.parts if part not in {"", "."}]
        if not parts:
            continue
        pure = PurePosixPath(*parts)
        if pure.suffix.lower() not in ARXIV_TEXT_EXTENSIONS:
            omitted.append({"path": original_name, "reason": "non-text-document-member"})
            continue
        if len(raw) > max_file or total_bytes + len(raw) > max_total:
            omitted.append({"path": original_name, "reason": "size-budget"})
            continue
        text = raw.decode("utf-8", errors="replace")
        stored[pure.as_posix()] = text
        total_bytes += len(text.encode("utf-8"))

    candidates = tex_root_candidates(stored)
    if (root / "normalized").is_dir() and len(candidates) != 1:
        raise ArxivPreflightError(
            f"{record.uid}: new payload has no unique TeX root ({candidates!r}); retained capsule unchanged"
        )
    root = prepare_capsule(record)
    source_root = root / "source"
    source_root.mkdir(parents=True, exist_ok=True)
    for path, text in stored.items():
        destination = source_root / path
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text, encoding="utf-8")

    derivatives = write_arxiv_tex_derivatives(record, root, stored, revision=manifest["revision"])
    main_tex = derivatives["main_tex"]
    write_jsonl(
        root / "files.jsonl",
        (
            {
                "path": (source_root / path).relative_to(ROOT).as_posix(),
                "bytes": (source_root / path).stat().st_size,
                "sha256": sha256_file(source_root / path),
                "lines": len(text.splitlines()),
            }
            for path, text in sorted(stored.items())
        ),
    )

    manifest.update(
        {
            "status": "materialized" if stored else "partial",
            "content_tier": "full_text" if stored else "metadata_capsule",
            "rights": {
                "declared_access": record.rights_access,
                "full_text_redistribution_assumed": True,
                "basis": "arXiv source archive",
            },
            "materialization": {
                "stored_text_files": len(stored),
                "stored_text_bytes": total_bytes,
                **derivatives,
                "omitted_member_count": len(omitted),
            },
            "selectors": ["selectors.jsonl"],
            "omitted": omitted[:250],
        }
    )
    if not main_tex and stored:
        manifest["status"] = "partial"
        manifest["warnings"].append("TeX files were stored but a root document was not identified")
        if len(derivatives["tex_root_candidates"]) > 1:
            manifest["warnings"].append("Multiple TeX document roots require an explicit target boundary decision.")
    if derivatives["tex_include_errors"]:
        manifest["status"] = "partial"
        manifest["warnings"].append("TeX include expansion is incomplete; see materialization.tex_include_errors.")
    if derivatives["tex_normalization_diagnostics"]:
        manifest["status"] = "partial"
        limitation = (
            "Plain-text normalization excludes semantic abstracts declared in the preamble; "
            "retained source and normalized TeX remain authoritative. This is not a full TeX parser."
        )
        manifest["warnings"].append(limitation)
        manifest.setdefault("limitations", []).append(limitation)
    return finalize_capsule(record, root, manifest)


def github_api_json(url: str, timeout: int = 35, max_bytes: int = 50_000_000) -> dict[str, Any]:
    payload, _, _ = fetch_bytes(url, timeout=timeout, max_bytes=max_bytes)
    data = json.loads(payload.decode("utf-8"))
    if not isinstance(data, dict):
        raise RuntimeError(f"expected object from GitHub API: {url}")
    return data


def github_file_rank(path: str) -> tuple[int, int, str]:
    pure = PurePosixPath(path)
    lower = path.lower()
    name = pure.name.lower()
    depth = len(pure.parts)
    if name.startswith("readme") and depth == 1:
        rank = 0
    elif name in PROMINENT_GITHUB_FILENAMES and depth <= 3:
        rank = 1
    elif lower.startswith("docs/") and any(keyword in lower for keyword in GITHUB_DOC_KEYWORDS):
        rank = 2
    elif lower.startswith("docs/"):
        rank = 3
    elif name in PROMINENT_GITHUB_FILENAMES:
        rank = 4
    elif any(keyword in lower for keyword in GITHUB_DOC_KEYWORDS) and pure.suffix.lower() in GITHUB_TEXT_EXTENSIONS:
        rank = 5
    else:
        rank = 10
    return rank, depth, path


def sanitize_relative_path(path: str) -> PurePosixPath | None:
    pure = PurePosixPath(path.replace("\\", "/"))
    if pure.is_absolute() or ".." in pure.parts:
        return None
    parts = [part for part in pure.parts if part not in {"", "."}]
    return PurePosixPath(*parts) if parts else None


def decode_github_blob(blob: dict[str, Any]) -> bytes:
    content = blob.get("content")
    encoding = blob.get("encoding")
    if not isinstance(content, str):
        raise RuntimeError("GitHub blob has no content")
    if encoding == "base64":
        return base64.b64decode(content.replace("\n", ""))
    return content.encode("utf-8")


def extract_markdown_headings(
    text: str, path: str, *, structured: bool = False,
) -> list[dict[str, Any]]:
    """Keep legacy ATX output; opt in to Setext, fences and Pandoc simple tables."""
    headings: list[dict[str, Any]] = []
    fence = ""
    simple_table = False
    previous: tuple[int, str] | None = None
    lines = text.splitlines()
    for line_number, line in enumerate(lines, 1):
        if structured:
            if fence:
                if re.fullmatch(rf" {{0,3}}{re.escape(fence[0])}{{{len(fence)},}}[ \t]*", line):
                    fence = ""
                previous = None
                continue
            opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
            if opening and not (opening.group(1)[0] == "`" and "`" in opening.group(2)):
                fence = opening.group(1)
                previous = None
                continue
            if simple_table:
                if re.fullmatch(r" {0,3}-{3,}[ \t]*", line):
                    simple_table = False
                previous = None
                continue
            if (
                re.fullmatch(r" {0,3}-{3,}[ \t]*", line) and line_number + 1 < len(lines)
                and re.fullmatch(r" {0,3}-+(?:[ \t]+-+)+[ \t]*", lines[line_number + 1])
            ):
                simple_table = True
                previous = None
                continue
        match = re.match(
            r"^ {0,3}(#{1,6})[ \t]+(.+?)[ \t]*$" if structured else r"^(#{1,6})\s+(.+?)\s*$",
            line,
        )
        if match:
            heading = match.group(2).strip()
            if structured:
                heading = re.sub(r"[ \t]+#+[ \t]*$", "", heading)
            headings.append(
                {
                    "path": path,
                    "line": line_number,
                    "level": len(match.group(1)),
                    "heading": heading,
                }
            )
            previous = None
        elif structured:
            underline = re.fullmatch(r" {0,3}(=+|-+)[ \t]*", line)
            if underline and previous:
                headings.append({
                    "path": path, "line": previous[0],
                    "level": 1 if underline.group(1)[0] == "=" else 2,
                    "heading": previous[1],
                })
                previous = None
            else:
                previous = (line_number, line.strip()) if re.match(r"^ {0,3}\S", line) else None
    return headings


def derive_retained_markdown(
    source: Path, document: Path, asset_rewrites: dict[str, str],
) -> list[dict[str, Any]]:
    """Copy retained UTF-8 Markdown, rewriting only explicitly mapped img src paths.

    Line endings and all other text are preserved. Paths belong to this repository;
    returned section ranges partition the document, including its leading preamble.
    """
    if source.resolve() == document.resolve():
        raise ValueError("derived Markdown cannot overwrite its retained original")
    if not isinstance(asset_rewrites, dict) or any(
        not isinstance(old, str) or not old or not isinstance(new, str) or not new
        or "\n" in old or "\r" in old or "\n" in new or "\r" in new
        for old, new in asset_rewrites.items()
    ):
        raise ValueError("asset_rewrites must map nonempty single-line paths")
    local_path = document.resolve().relative_to(ROOT.resolve()).as_posix()
    source_path = source.resolve().relative_to(ROOT.resolve()).as_posix()
    text = source.read_bytes().decode("utf-8")
    text = re.sub(
        r"(<img\b[^>]*?\s+src\s*=\s*)([\"'])(.*?)\2",
        lambda match: match.group(1) + match.group(2)
        + asset_rewrites.get(match.group(3), match.group(3)) + match.group(2),
        text, flags=re.IGNORECASE,
    )
    lines = text.splitlines()
    headings = extract_markdown_headings(text, local_path, structured=True)
    starts = [(1, headings[0] if headings else None)] + [
        (heading["line"], heading) for heading in headings[1:]
    ]
    selectors: list[dict[str, Any]] = []
    if text.strip():
        for index, (start, heading) in enumerate(starts):
            end = starts[index + 1][0] - 1 if index + 1 < len(starts) else len(lines)
            selectors.append({
                "selector": f"derived://{local_path}#L{start}-L{end}",
                "local_path": local_path, "kind": "section" if heading else "file",
                "start_line": start, "end_line": end,
                "text_preview": next(line for line in lines[start - 1:end] if line.strip())[:700],
                "derived_from": source_path,
                **({"heading": heading["heading"], "level": heading["level"]} if heading else {}),
            })
    document.parent.mkdir(parents=True, exist_ok=True)
    document.write_bytes(text.encode("utf-8"))
    return selectors


def rewrite_markdown_hrefs(text: str, rewrites: dict[str, str]) -> str:
    """Rewrite finite inline hrefs, never fenced, indented or inline code."""
    def rewrite_prose(prose: str) -> str:
        def hrefs(value: str) -> str:
            return re.sub(
                r"(\]\([ \t]*)([^)\s]+)",
                lambda match: match.group(1) + rewrites.get(match.group(2), match.group(2)),
                value,
            )
        parts: list[str] = []
        start = 0
        for code in re.finditer(r"(?<!`)(`+)(?!`)[\s\S]*?(?<!`)\1(?!`)", prose):
            parts.extend((hrefs(prose[start:code.start()]), code.group(0)))
            start = code.end()
        return "".join(parts) + hrefs(prose[start:])

    parts: list[str] = []
    prose: list[str] = []
    fence = ""
    for line in text.splitlines(keepends=True):
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line.rstrip("\r\n"))
        if fence or opening or re.match(r"^(?: {4}|\t)", line):
            parts.append(rewrite_prose("".join(prose)))
            prose = []
            parts.append(line)
            if fence:
                if re.fullmatch(rf" {{0,3}}{re.escape(fence[0])}{{{len(fence)},}}[ \t]*", line.rstrip("\r\n")):
                    fence = ""
            elif opening and not (opening.group(1)[0] == "`" and "`" in opening.group(2)):
                fence = opening.group(1)
        else:
            prose.append(line)
    return "".join(parts) + rewrite_prose("".join(prose))


def retained_html_reference(
    source: Path, reference: str, document: Path,
    html_sources: dict[Path, tuple[Any, str, set[str]]], rewrites: dict[str, str],
    source_url: str = "", *, asset: bool = False,
) -> str:
    """Resolve only explicit routes and already retained local originals."""
    if asset and not reference:
        raise ValueError("retained HTML image has no src")
    parsed = urllib.parse.urlsplit(reference)
    if not asset and not parsed.path and not parsed.scheme and not parsed.netloc:
        _, stem, ids = html_sources[source]
        if parsed.fragment in ids:
            return f"#{stem}-{parsed.fragment}"
    if reference in rewrites:
        return rewrites[reference]
    if parsed.scheme or parsed.netloc:
        return reference
    path = (source.parent / urllib.parse.unquote(parsed.path)).resolve() if parsed.path else source
    if not asset and path not in html_sources and not path.suffix:
        path = path.with_suffix(".html")
    if not asset and path in html_sources:
        _, stem, ids = html_sources[path]
        if not parsed.fragment:
            return f"#{stem}-L1"
        if parsed.fragment in ids:
            return f"#{stem}-{parsed.fragment}"
    try:
        path.relative_to(document.parent.parent.resolve())
        local = path.is_file()
    except ValueError:
        local = False
    if asset and not local:
        raise ValueError(f"retained HTML image is missing: {reference}")
    if local:
        href = Path(os.path.relpath(path, start=document.parent)).as_posix()
        return href + (f"#{parsed.fragment}" if parsed.fragment else "")
    return urllib.parse.urljoin(source_url, reference) if source_url else reference


def retained_text_selector_file(manifest: dict[str, Any], root: Path, *, require_exists: bool = False) -> Path:
    """Route an explicit retained-text pair; keep unopted legacy defaults."""
    materialization = manifest.get("materialization")
    sidecar_declared = isinstance(manifest.get("selectors"), list) and "normalized/selectors.jsonl" in manifest["selectors"]
    if not isinstance(materialization, dict):
        if sidecar_declared:
            raise ValueError("retained selector sidecar has no materialization mapping")
        return root / "selectors.jsonl"
    binding = materialization.get("retained_text_binding")
    if binding is None:
        if "retained_text_binding" in materialization or "retained_text_selectors" in materialization or sidecar_declared:
            raise ValueError("retained selector sidecar requires an explicit binding")
        return root / "selectors.jsonl"
    if not isinstance(binding, str) or binding not in {"dated_html_response", "git_snapshot", "wiki_page_revision_set"}:
        raise ValueError("unknown retained text binding")
    sources = materialization.get("retained_text_sources")
    if (
        materialization.get("document") != "normalized/document.md"
        or materialization.get("normalized_document") != "normalized/document.md"
        or materialization.get("retained_text_selectors") != "normalized/selectors.jsonl"
        or manifest.get("selectors") != ["selectors.jsonl", "normalized/selectors.jsonl"] and not (binding == "git_snapshot" and manifest.get("selectors") == ["normalized/selectors.jsonl"])
        or not isinstance(sources, list) or not sources or any(not isinstance(item, dict) for item in sources)
    ):
        raise ValueError("retained text needs its fixed document and selector pair")
    if binding == "dated_html_response" and (len(sources) != 1 or sources[0].get("source") != "source/specification.html" or sources[0].get("format") != "html"):
        raise ValueError("dated HTML needs its fixed original, document and selector pair")
    if binding == "dated_html_response" and "content_selector" in sources[0] and (not isinstance(sources[0]["content_selector"], str) or not sources[0]["content_selector"].strip()):
        raise ValueError("dated HTML content_selector must be a nonempty CSS string")
    source_names = []
    for item in sources:
        name = item.get("source")
        formats = {"md", "yaml"} if binding == "git_snapshot" else {"html"}
        if not isinstance(name, str) or Path(name).is_absolute() or not Path(name).parts or Path(name).parts[0] != "source" or ".." in Path(name).parts or not isinstance(item.get("format"), str) or item["format"] not in formats:
            raise ValueError("retained text needs explicit capsule-local native sources")
        source_names.append(name)
    if len(source_names) != len(set(source_names)):
        raise ValueError("retained text sources must be unique")
    if binding == "wiki_page_revision_set" and any(item.get("content_selector") != "#mw-content-text .mw-parser-output" or Path(item["source"]).suffix != ".html" for item in sources):
        raise ValueError("wiki pages need their explicit static HTML content container")
    for name in (*source_names, "normalized/document.md", "normalized/selectors.jsonl"):
        path = root / name
        path.resolve().relative_to(root.resolve())
        if path.is_symlink():
            raise ValueError("retained text paths cannot alias retained files")
    if require_exists and any(not (root / name).is_file() or not (root / name).stat().st_size for name in ("normalized/document.md", "normalized/selectors.jsonl")):
        raise ValueError("explicit retained text document or selector sidecar is missing")
    return root / "normalized/selectors.jsonl"


def retained_html_body(
    original: str, *, dated_html_response: bool = False, wiki_page_revision_set: bool = False,
    content_selector: str | None = None, exclude_selectors: Any = None,
) -> Any:
    """Exclude only declared, observed UI from a derived DOM, never the original."""
    from bs4 import BeautifulSoup
    from soupsieve import SelectorSyntaxError
    soup = BeautifulSoup(original, "html.parser")
    if not dated_html_response and not wiki_page_revision_set:
        return soup.body or soup
    if len(soup.find_all("body")) != 1:
        raise ValueError("retained HTML must have one static body")
    body = soup.body
    if wiki_page_revision_set:
        if content_selector != "#mw-content-text .mw-parser-output":
            raise ValueError("wiki HTML needs its declared content container")
        containers = body.select(content_selector)
        if len(containers) != 1 or not containers[0].get_text(" ", strip=True):
            raise ValueError("wiki HTML needs one nonempty static content container")
        body = containers[0]
    elif content_selector is not None:
        if not isinstance(content_selector, str) or not content_selector.strip():
            raise ValueError("dated HTML content_selector must be a nonempty CSS string")
        try:
            containers = body.select(content_selector)
        except (SelectorSyntaxError, NotImplementedError) as exc:
            raise ValueError("dated HTML content_selector is invalid CSS") from exc
        if len(containers) != 1 or containers[0].name != "article" or not containers[0].get_text(" ", strip=True):
            raise ValueError("dated HTML needs one nonempty selected article")
        body = containers[0]
    excluded = [] if exclude_selectors is None else exclude_selectors
    allowed = {
        ".mw-pt-languages", ".mw-editsection", "td.mbox-image img", ".nmbox",
        ".template-pd-help-page img", ".ext-discussiontools-init-replylink-buttons",
        ".sistersitebox .side-box-image img", ".side-box-imageright img",
        "#mwDQ", "#mwAjc", "#mwAjk", "#mwEA", "#mwAgw", "#mwAg4", "#mwAhE",
        "#mwDg", "#mwATI", "#mwATQ", "#mwAUg",
    } if wiki_page_revision_set else {"nav#toc", "p#back-to-top", ".dfn-panel", ".head img", ".head a.orcid svg", "a.headerlink"}
    if not isinstance(excluded, list) or any(not isinstance(value, str) or value not in allowed for value in excluded) or len(excluded) != len(set(excluded)):
        raise ValueError("retained HTML exclusions must be an explicit list of supported UI selectors")
    for selector in excluded:
        nodes = body.select(selector)
        if not nodes:
            raise ValueError(f"declared HTML exclusion is absent: {selector}")
        for node in nodes:
            node.decompose()
    if dated_html_response and content_selector is not None and not body.get_text(" ", strip=True):
        raise ValueError("dated HTML selected article is empty after its declared UI exclusions")
    return body


def preflight_dated_html_assets(manifest: dict[str, Any], root: Path, *, repository_root: Path) -> dict[str, Any]:
    return preflight_retained_html_assets(manifest, root, manifest["materialization"]["retained_text_sources"][0], repository_root=repository_root)


def preflight_retained_html_assets(
    manifest: dict[str, Any], root: Path, item: dict[str, Any], *, repository_root: Path,
    wiki_page_revision_set: bool = False,
) -> dict[str, Any]:
    """Bind finite HTML routes to the existing original inventory and retrievals."""
    materialization = manifest["materialization"]
    retained_text_selector_file(manifest, root)
    if "exclude_selectors" in item and not isinstance(item["exclude_selectors"], list):
        raise ValueError("dated HTML exclude_selectors must be a list")
    source = (root / item["source"]).resolve()
    retrieval = next(row for row in manifest["retrievals"] if row.get("local_path") == item["source"])
    source_url = retrieval["requested_url"]
    entity = source.read_bytes()
    transport_fields = ("content_encoding", "transport_local_path", "transport_bytes", "transport_sha256")
    if not wiki_page_revision_set and any(field in retrieval for field in transport_fields):
        if any(field not in retrieval for field in transport_fields) or retrieval["content_encoding"] != "gzip" or retrieval["transport_local_path"] != "source/specification.html.gz":
            raise ValueError("dated HTML transport needs its complete explicit gzip binding")
        wire = root / retrieval["transport_local_path"]
        wire.resolve().relative_to(root.resolve())
        if not wire.is_file() or wire.is_symlink():
            raise ValueError("dated HTML gzip wire original is missing or aliased")
        wire_bytes = wire.read_bytes()
        wire_hash = sha256_file(wire)
        inventory = [row for row in manifest["local_files"] if row.get("path") == wire.resolve().relative_to(repository_root.resolve()).as_posix()]
        if (
            len(inventory) != 1 or inventory[0].get("sha256") != wire_hash or inventory[0].get("bytes") != len(wire_bytes)
            or retrieval["transport_sha256"] != wire_hash or retrieval["transport_bytes"] != len(wire_bytes)
        ):
            raise ValueError("dated HTML gzip wire differs from its inventory or transport binding")
        try:
            decoded = gzip.decompress(wire_bytes)
        except (OSError, EOFError, zlib.error) as exc:
            raise ValueError("dated HTML gzip wire cannot be decoded") from exc
        if decoded != entity:
            raise ValueError("dated HTML entity differs from its decoded gzip wire")
    body = retained_html_body(entity.decode("utf-8"), dated_html_response=not wiki_page_revision_set, wiki_page_revision_set=wiki_page_revision_set, content_selector=item.get("content_selector"), exclude_selectors=item.get("exclude_selectors"))
    unretained = item.get("unretained_assets", [])
    if wiki_page_revision_set and unretained:
        raise ValueError("wiki revision-set figures must have explicit retained local routes")
    if not isinstance(unretained, list) or any(
        not isinstance(reference, str) or not reference or any(char.isspace() for char in reference)
        or urllib.parse.urlsplit(reference).scheme or urllib.parse.urlsplit(reference).netloc
        or not urllib.parse.urlsplit(reference).path or urllib.parse.urlsplit(reference).query or urllib.parse.urlsplit(reference).fragment
        for reference in unretained
    ) or len(unretained) != len(set(unretained)):
        raise ValueError("unretained HTML assets must be explicit unique relative src values")
    if unretained and manifest.get("status") != "partial":
        raise ValueError("unretained original figures require an honest partial status")
    rewrites = materialization.get("link_rewrites", {})
    if not isinstance(rewrites, dict) or any(
        not isinstance(old, str) or not old or not isinstance(new, str) or not new
        or any(char in old + new for char in "\r\n")
        or urllib.parse.urlsplit(new).scheme or urllib.parse.urlsplit(new).netloc
        for old, new in rewrites.items()
    ):
        raise ValueError("dated HTML needs finite local href routes")
    if any(reference in rewrites for reference in unretained):
        raise ValueError("unretained HTML assets cannot also have retained local routes")
    alternatives = item.get("image_text_alternatives", {}) if wiki_page_revision_set else {}
    if not isinstance(alternatives, dict) or any(
        not isinstance(reference, str) or not isinstance(label, str) or not label.strip() or any(char in label for char in "\r\n")
        or urllib.parse.urlsplit(reference).netloc != "thumb.wikimedia.org"
        or urllib.parse.urlsplit(reference).scheme not in {"", "https"}
        or Path(urllib.parse.urlsplit(reference).path).name not in {"20px-Yes_check.svg.png", "20px-X_mark.svg.png"}
        for reference, label in alternatives.items()
    ) or any(reference in rewrites for reference in alternatives):
        raise ValueError("wiki image-text alternatives need finite semantic-marker src/alt pairs, not local image routes")

    def check_original(path: Path, expected_url: str | None = None) -> None:
        path.relative_to((root / "source").resolve())
        if not path.is_file() or path.is_symlink():
            raise ValueError("dated HTML route or asset original is missing")
        actual = sha256_file(path)
        inventory = [row for row in manifest["local_files"] if row.get("path") == path.relative_to(repository_root).as_posix()]
        records = [row for row in manifest["retrievals"] if row.get("local_path") == path.relative_to(root.resolve()).as_posix()]
        if (
            len(inventory) != 1 or inventory[0].get("sha256") != actual or inventory[0].get("bytes") != path.stat().st_size
            or len(records) != 1 or records[0].get("sha256") != actual or records[0].get("bytes") != path.stat().st_size
            or expected_url is not None and (records[0].get("requested_url") != expected_url or records[0].get("resolved_url") != expected_url or records[0].get("http_status") != 200)
        ):
            raise ValueError("dated HTML route or asset differs from inventory or retrieval")

    document = root / materialization["document"]
    for target in rewrites.values():
        parsed = urllib.parse.urlsplit(target)
        if parsed.path:
            check_original((document.parent / urllib.parse.unquote(parsed.path)).resolve())
    observed_assets: set[str] = set()
    for node in body.find_all(["img", "object"]):
        if node.find_parent(["pre", "code", "script", "style", "template"]):
            continue
        reference = node.get("data" if node.name == "object" else "src", "")
        parsed = urllib.parse.urlsplit(reference)
        if not reference or not parsed.path:
            raise ValueError("dated HTML asset has no original path")
        observed_assets.add(reference)
        if reference in alternatives:
            if node.name != "img" or node.get("alt") != alternatives[reference]:
                raise ValueError("wiki image-text alternative differs from the actual source alt")
            continue
        if reference in unretained:
            continue
        if reference in rewrites:
            route = urllib.parse.urlsplit(rewrites[reference])
            if not route.path:
                raise ValueError("dated HTML asset route must target an original file")
            asset = (document.parent / urllib.parse.unquote(route.path)).resolve()
        elif parsed.scheme or parsed.netloc:
            raise ValueError("dated HTML external asset needs an explicit retained route")
        else:
            asset = (source.parent / urllib.parse.unquote(parsed.path)).resolve()
        check_original(asset, urllib.parse.urljoin(source_url, reference))
    if set(unretained) - observed_assets:
        raise ValueError("declared unretained HTML asset is absent from the derived DOM")
    if set(alternatives) - observed_assets:
        raise ValueError("declared wiki image-text alternative is absent from the derived DOM")
    return {"source_url": source_url, "dated_html_response": not wiki_page_revision_set, "wiki_page_revision_set": wiki_page_revision_set, "content_selector": item.get("content_selector"), "exclude_selectors": item.get("exclude_selectors", []), "unretained_assets": unretained, "image_text_alternatives": alternatives}


def preflight_wiki_html_sources(
    manifest: dict[str, Any], root: Path, canonical: dict[str, Any], capsule: dict[str, Any],
    *, repository_root: Path, actual_hashes: dict[str, str],
) -> dict[Path, dict[str, Any]]:
    """Bind each declared wiki page revision to its saved, non-executed HTML response."""
    from bs4 import BeautifulSoup
    root, repository_root = root.resolve(), repository_root.resolve()
    retained_text_selector_file(manifest, root)
    sources = manifest["materialization"]["retained_text_sources"]
    package = manifest["rights"]["redistribution_package"]
    bindings = package.get("source_bindings")
    if not isinstance(bindings, list) or not bindings or len(bindings) != len(sources) or any(not isinstance(row, dict) for row in bindings):
        raise ValueError("wiki package needs an ordered binding for every retained page")
    version = manifest["source_version"]
    if not isinstance(version, str) or not version.startswith("Wikimedia page snapshot at "):
        raise ValueError("wiki pages need an explicit common revision cutoff")
    cutoff = datetime.strptime(version.removeprefix("Wikimedia page snapshot at "), "%Y-%m-%dT%H:%M:%SZ")
    identities = [row.get("identity_url") for row in bindings]
    if len(identities) != len(set(identities)) or any(metadata.get("source_urls") != identities or metadata["versioning"].get("snapshot_commit") is not None for metadata in (canonical, capsule)):
        raise ValueError("wiki page bindings differ from the canonical identity vector or fabricate a Git commit")
    if package["source_version_url"] != bindings[0].get("source_version_url") or manifest["revision"] != bindings[0].get("source_revision"):
        raise ValueError("wiki root revision and approved URL must describe the first retained page")
    for item, binding in zip(sources, bindings):
        if binding.get("source") != item["source"] or any(not isinstance(binding.get(field), str) or not binding[field].strip() for field in ("identity_url", "source_version_url", "page_title", "revision_timestamp", "source_revision")) or any(type(binding.get(field)) is not int or binding[field] <= 0 for field in ("page_id", "revision_id")):
            raise ValueError("wiki page binding is incomplete or out of source order")
        title = binding["page_title"]
        identity = urllib.parse.urlsplit(binding["identity_url"])
        if (
            identity.scheme != "https" or identity.netloc not in {"www.mediawiki.org", "www.wikidata.org", "en.wikipedia.org"}
            or identity.query or identity.fragment or not identity.path.startswith("/wiki/")
            or urllib.parse.unquote(identity.path.removeprefix("/wiki/")).replace("_", " ") != title.replace("_", " ")
            or any(char in title for char in "\r\n")
        ):
            raise ValueError("wiki page title differs from its literal official identity URL")
        approved = f"https://{identity.netloc}/w/index.php?title={urllib.parse.quote(title.replace(' ', '_'), safe='')}&oldid={binding['revision_id']}"
        if binding["source_version_url"] != approved or datetime.strptime(binding["revision_timestamp"], "%Y-%m-%dT%H:%M:%SZ") > cutoff:
            raise ValueError("wiki fixed permalink or revision timestamp differs from its declared cutoff")
        path = root / item["source"]
        if not path.is_file() or path.is_symlink():
            raise ValueError("wiki page original is missing")
        source_hash = sha256_file(path)
        source_path = path.relative_to(repository_root).as_posix()
        inventory = [row for row in manifest["local_files"] if row.get("path") == source_path]
        retrievals = [row for row in manifest["retrievals"] if row.get("local_path") == item["source"]]
        if binding["source_revision"] != f"sha256:{source_hash}" or actual_hashes.get(source_path) != source_hash or len(inventory) != 1 or inventory[0].get("sha256") != source_hash or inventory[0].get("bytes") != path.stat().st_size:
            raise ValueError("wiki page original differs from its binding or inventory")
        if len(retrievals) != 1 or any(retrievals[0].get(field) != expected for field, expected in (("requested_url", approved), ("resolved_url", approved), ("sha256", source_hash), ("bytes", path.stat().st_size), ("http_status", 200))) or not isinstance(retrievals[0].get("content_type"), str) or retrievals[0]["content_type"].split(";", 1)[0].strip() != "text/html" or not isinstance(retrievals[0].get("retrieved_at"), str) or not retrievals[0]["retrieved_at"].strip():
            raise ValueError("wiki page retrieval does not describe its approved fixed response")
        soup = BeautifulSoup(path.read_bytes().decode("utf-8"), "html.parser")
        configuration = "\n".join(script.get_text() for script in soup.find_all("script"))
        for field, expected in (("wgRevisionId", binding["revision_id"]), ("wgArticleId", binding["page_id"]), ("wgPageName", title.replace(" ", "_"))):
            values = re.findall(r'"' + field + r'"\s*:\s*("(?:\\.|[^"\\])*"|[0-9]+)(?=\s*[,}])', configuration)
            if len(values) != 1 or json.loads(values[0]) != expected:
                raise ValueError(f"wiki actual HTML {field} differs from its page binding")
    options = {(root / item["source"]).resolve(): preflight_retained_html_assets(manifest, root, item, repository_root=repository_root, wiki_page_revision_set=True) for item in sources}
    for item, binding in zip(sources, bindings):
        options[(root / item["source"]).resolve()]["page_title"] = binding["page_title"]
    return options


def retained_html_sections(
    source: Path, document: Path, html_sources: dict[Path, tuple[Any, str, set[str]]],
    rewrites: dict[str, str], source_url: str, *, dated_html_response: bool = False,
    unretained_assets: list[str] | None = None, wiki_page_revision_set: bool = False,
    image_text_alternatives: dict[str, str] | None = None,
) -> list[dict[str, Any]]:
    """Render structural atoms, then visit every remaining body text node once."""
    from bs4 import Comment, NavigableString
    body, stem, _ = html_sources[source]
    sections: list[dict[str, Any]] = []
    parts: list[str] = []
    source_start = body.sourceline or 1
    heading: dict[str, Any] = {}
    def anchor(node: Any) -> str:
        return f'\n<a id="{html.escape(stem + "-" + str(node["id"]), quote=True)}"></a>\n' if node.get("id") else ""

    def code_block(node: Any) -> str:
        value = "".join("\n" if getattr(child, "name", None) == "br" else str(child) if isinstance(child, NavigableString) and not isinstance(child, Comment) else "" for child in node.descendants) if dated_html_response else node.get_text("", strip=False)
        fence = "`" * max(3, max((len(run) + 1 for run in re.findall(r"`+", value)), default=3))
        return f"\n\n{fence}\n" + value + ("" if value.endswith("\n") else "\n") + fence + "\n\n"

    def inline(node: Any) -> str:
        if isinstance(node, Comment):
            return ""
        if isinstance(node, NavigableString):
            return re.sub(r"[ \t\r\n]+", " ", str(node))
        prefix = anchor(node)
        if node.name in {"script", "style", "template"}:
            return ""
        if node.name == "pre":
            return prefix + code_block(node)
        if node.name == "code":
            value = node.get_text("", strip=False)
            fence = "`" * max(1, max((len(run) + 1 for run in re.findall(r"`+", value)), default=1))
            return prefix + fence + value + fence
        if node.name == "img":
            label = " ".join(str(node.get("alt", "")).split()) if dated_html_response else node.get("alt", "")
            if wiki_page_revision_set and node.get("src") in (image_text_alternatives or {}):
                return prefix + f"[Collector-rendered source image alt: {image_text_alternatives[node['src']]}]({urllib.parse.urljoin(source_url, node['src'])})"
            if dated_html_response and node.get("src") in (unretained_assets or []):
                return prefix + f"[Original figure not retained locally: {label}]({urllib.parse.urljoin(source_url, node['src'])})"
            src = retained_html_reference(source, node.get("src", ""), document, html_sources, rewrites, source_url, asset=True)
            return prefix + f"![{label}]({src})"
        if dated_html_response and node.name == "object":
            unretained = node.get("data") in (unretained_assets or [])
            src = urllib.parse.urljoin(source_url, node["data"]) if unretained else retained_html_reference(source, node.get("data", ""), document, html_sources, rewrites, source_url, asset=True)
            label = node.get("aria-label") or Path(urllib.parse.urlsplit(node.get("data", "")).path).name
            label = " ".join(str(label).split())
            descriptions = " ".join(
                f"[aria-describedby: {name}]({retained_html_reference(source, '#' + name, document, html_sources, rewrites, source_url)})"
                for name in str(node.get("aria-describedby", "")).split()
            )
            fallback = "".join(inline(child) for child in node.children)
            representation = f"[Original figure not retained locally: {label}]({src})" if unretained else f"![{label}]({src})"
            return prefix + "\n\n" + representation + "\n\n" + descriptions + "\n\n" + fallback
        value = "".join(inline(child) for child in node.children)
        if wiki_page_revision_set and node.name in {"sub", "sup"}:
            value = f"<{node.name}>" + value + f"</{node.name}>"
        elif wiki_page_revision_set and node.name in {"dl", "dt", "dd"}:
            value = f"\n\n<{node.name}>\n" + value + f"\n</{node.name}>\n\n"
        elif node.name == "a" and node.get("href"):
            href = retained_html_reference(source, node["href"], document, html_sources, rewrites, source_url)
            if dated_html_response and node.find("object"):
                value += f"\n[Enclosing object link]({href})\n"
            else:
                value = f"[{value.strip()}]({href})"
        elif node.name == "br":
            value = "\n"
        return prefix + value

    def finish(end: int) -> bool:
        value = "".join(parts).strip()
        if any(line.strip() and not line.startswith("<a ") for line in value.splitlines()):
            sections.append({"text": value + "\n", "source_start_line": source_start, "source_end_line": max(source_start, end), **heading})
            return True
        return False

    def walk(node: Any) -> None:
        nonlocal source_start, heading, parts
        if isinstance(node, (Comment, NavigableString)):
            parts.append(inline(node))
            return
        if node.name in {"script", "style", "template"}:
            return
        if wiki_page_revision_set and "hatnote" in node.get("class", []):
            # Keep the original navigation/clarification, but not as automatic source prose.
            rendered = inline(node)
            pattern = r'<a id="[^"]+"></a>'
            locators = "\n".join(re.findall(pattern, rendered))
            value = re.sub(pattern, "", rendered).strip()
            parts.append("\n\n" + locators + "\n\n> Collector source role: hatnote (original text and links follow).\n" + "\n".join(
                "> " + line for line in value.splitlines()
            ) + "\n\n")
            return
        if re.fullmatch(r"h[1-6]", node.name or ""):
            line = node.sourceline
            if not isinstance(line, int):
                raise ValueError("retained HTML heading has no native source line")
            recorded = finish(line - 1)
            prefix = "".join(parts) if not recorded else ""
            if recorded:
                source_start = line
            heading = {"heading": node.get_text(" ", strip=True), "level": int(node.name[1]), "heading_line": line}
            title = "".join(inline(child) for child in node.children).strip()
            heading_anchors = ""
            if wiki_page_revision_set:
                # Empty source spans are locators, not the ATX heading's visible title.
                pattern = r'<a id="[^"]+"></a>'
                heading_anchors = "\n".join(re.findall(pattern, title)) + "\n"
                title = " ".join(re.sub(pattern, "", title).split())
            parts = [prefix, anchor(node), heading_anchors, "#" * heading["level"] + " " + title + "\n"]
            return
        if node.name == "pre":
            parts.append(anchor(node) + code_block(node))
            return
        if node.name == "table":
            rows: list[tuple[Any, list[str]]] = []
            block_rows: set[int] = set()
            def table_content(child: Any) -> None:
                if isinstance(child, Comment):
                    return
                if isinstance(child, NavigableString):
                    if child.strip():
                        rows.append((child, [inline(child).strip()]))
                    return
                if child.name in {"script", "style", "template"}:
                    return
                if child.name in {"th", "td", "pre", "code", "a", "img", "br"} or dated_html_response and child.name == "object":
                    row = child.find_parent("tr") or child
                    if not rows or rows[-1][0] is not row:
                        rows.append((row, []))
                    value = inline(child).strip()
                    block_cell = dated_html_response and (child.name == "pre" or child.find("pre") is not None)
                    if block_cell:
                        block_rows.add(id(row))
                    if dated_html_response and child.name in {"th", "td"}:
                        spans = "".join(f" [{attribute}={child[attribute]}]" for attribute in ("rowspan", "colspan") if child.has_attr(attribute))
                        value = "> Collector cell span:" + spans + "\n\n" + value if block_cell and spans else value + spans
                    rows[-1][1].append(value)
                    return  # Includes nested cell text exactly once, including orphan td.
                if child.get("id"):
                    rows.append((child, [anchor(child)]))
                for descendant in child.children:
                    table_content(descendant)
            for child in node.children:
                table_content(child)
            rendered_rows: list[str] = []
            for row, cells in rows:
                if not any(cells):
                    continue
                if id(row) in block_rows:
                    rendered_rows.append("\n> Collector table row: cell blocks remain in original order.\n\n" + "\n\n".join(
                        f"> Collector cell {index} of {len(cells)}:" + (" (empty)" if not cell else "") + "\n\n" + cell
                        for index, cell in enumerate(cells, 1)
                    ) + "\n")
                else:
                    rendered_rows.append("- " + " | ".join(cells))
            parts.append(anchor(node) + "\n\n" + "\n".join(rendered_rows) + "\n\n")
            return
        if node.name in {"a", "img", "code", "br"} or dated_html_response and node.name == "object" or wiki_page_revision_set and node.name in {"sub", "sup", "dl", "dt", "dd"}:
            parts.append(inline(node))
            return
        block = node.name in {"p", "div", "section", "article", "figure", "figcaption", "ul", "ol", "li", "blockquote"} or "concept-item" in node.get("class", []) or dated_html_response and node.name in {"dl", "dt", "dd"}
        parts.append(anchor(node) + ("\n\n" if block else ""))
        if node.name == "li":
            depth = max(0, len(node.find_parents(["ul", "ol"])) - 1)
            marker = f"{len(node.find_previous_siblings('li')) + 1}. " if node.parent.name == "ol" else "- "
            parts.append(("    " if wiki_page_revision_set else "  ") * depth + marker)
        for child in node.children:
            walk(child)
        if block:
            parts.append("\n\n")
    walk(body)
    finish(len(source.read_bytes().decode("utf-8").splitlines()))
    return sections


def retained_markdown_frontmatter_end(text: str) -> int:
    """Locate only a closed leading YAML block, without interpreting its values."""
    lines = text.splitlines()
    if not lines or lines[0].rstrip(" \t") != "---":
        return 0
    for line_number, line in enumerate(lines[1:256], 2):
        if line.rstrip(" \t") in {"---", "..."}:
            return line_number
    raise ValueError("leading YAML frontmatter must close within 256 lines")


def preflight_docfx_includes(
    sources: list[tuple[Path, str]], root: Path, source_options: dict[Path, dict[str, Any]],
) -> tuple[Path | None, dict[int, Path]]:
    """Check only explicitly declared, one-level native Markdown includes."""
    declared = [source.resolve() for source, _ in sources if "docfx_includes" in source_options.get(source.resolve(), {})]
    if not declared:
        return None, {}
    main = sources[0][0].resolve()
    if declared != [main] or any(format_name != "md" for _, format_name in sources):
        raise ValueError("DocFX includes require one declared first Markdown root")
    options = source_options[main]
    routes = options["docfx_includes"]
    if options.get("git_snapshot") is not True or not isinstance(routes, dict) or not routes:
        raise ValueError("DocFX includes require a nonempty explicit Git Markdown mapping")
    originals = {source.resolve() for source, _ in sources}
    targets: dict[str, Path] = {}
    for reference, name in routes.items():
        if not isinstance(reference, str) or not reference or any(char in reference for char in "\r\n") or not isinstance(name, str) or sanitize_relative_path(name) is None or Path(name).parts[0] != "source":
            raise ValueError("DocFX include routes must identify local native originals")
        parsed = urllib.parse.urlsplit(reference)
        target = (root / name).resolve()
        if parsed.scheme or parsed.netloc or parsed.query or parsed.fragment or target not in originals or target == main or (main.parent / reference).resolve() != target:
            raise ValueError("DocFX include route differs from its declared relative original")
        targets[reference] = target
    origins = set()
    for source, _ in sources:
        source = source.resolve()
        item = source_options.get(source, {})
        match = re.fullmatch(r"(https://raw\.githubusercontent\.com/[^/]+/[^/]+/([0-9a-f]{40})/)([^?#]+)", str(item.get("source_url", "")))
        if item.get("git_snapshot") is not True or not match or match.group(2) != item.get("snapshot_commit") or match.group(3) != source.relative_to(root).as_posix().removeprefix("source/"):
            raise ValueError("DocFX references need each original's actual fixed Git source URL")
        origins.add(match.group(1))
    if len(origins) != 1:
        raise ValueError("DocFX originals must belong to one fixed public Git snapshot")
    calls: dict[int, Path] = {}
    used_references: set[str] = set()
    for source, _ in sources:
        source = source.resolve()
        text = source.read_bytes().decode("utf-8")
        fence, comment = "", False
        frontmatter_end = retained_markdown_frontmatter_end(text)
        for line_number, line in enumerate(text.splitlines(), 1):
            if line_number <= frontmatter_end:
                continue
            opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
            if fence:
                if re.fullmatch(rf" {{0,3}}{re.escape(fence[0])}{{{len(fence)},}}[ \t]*", line):
                    fence = ""
                continue
            if opening and not (opening.group(1)[0] == "`" and "`" in opening.group(2)):
                fence = opening.group(1)
                continue
            if comment or line.lstrip().startswith("<!--"):
                comment = "-->" not in line
                continue
            if re.match(r"^(?: {4}|\t)", line):
                continue
            prose = re.sub(r"(`+).*?\1", "", line)
            if not re.search(r"\[!INCLUDE\b", prose, re.IGNORECASE):
                continue
            include = re.fullmatch(r" {0,3}\[!INCLUDE \[[^\]]*\]\(([^()\s]+)\)\][ \t]*", line, re.IGNORECASE)
            if source != main or not include or include.group(1) not in targets:
                raise ValueError("undeclared or nested DocFX include")
            calls[line_number] = targets[include.group(1)]
            used_references.add(include.group(1))
    if used_references != set(routes) or set(targets.values()) != originals - {main}:
        raise ValueError("DocFX include declarations must cover exactly their used originals")
    return main, calls


def derive_retained_text_sources(
    sources: list[tuple[Path, str]], document: Path, link_rewrites: dict[str, str],
    *, source_options: dict[Path, dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """Assemble declared MD/YAML/HTML, with real single-source line ranges."""
    has_html = any(format_name == "html" for _, format_name in sources)
    if not sources or not isinstance(link_rewrites, dict) or any(
        not isinstance(old, str) or not old or not isinstance(new, str) or not new
        or "\n" in old or "\r" in old or "\n" in new or "\r" in new
        or not has_html and (urllib.parse.urlsplit(old).scheme or urllib.parse.urlsplit(old).netloc)
        or urllib.parse.urlsplit(new).scheme or urllib.parse.urlsplit(new).netloc
        for old, new in link_rewrites.items()
    ):
        raise ValueError("retained text sources need a finite, single-line local href mapping")
    local_path = document.resolve().relative_to(ROOT.resolve()).as_posix()
    prepared: list[tuple[str, str, str, str, list[dict[str, Any]], int]] = []
    stems: set[str] = set()
    known_anchors: set[str] = set()
    html_sources: dict[Path, tuple[Any, str, set[str]]] = {}
    for source, format_name in sources:
        if format_name not in {"md", "yaml", "html"} or source.resolve() == document.resolve():
            raise ValueError("retained text format must be md/yaml/html and cannot overwrite its original")
        source_path = source.resolve().relative_to(ROOT.resolve()).as_posix()
        stem = re.sub(r"[^A-Za-z0-9_-]", "-", source.stem)
        if stem in stems:
            raise ValueError("retained text source names must have distinct anchor stems")
        stems.add(stem)
        original = source.read_bytes().decode("utf-8")
        if not original.strip():
            raise ValueError("retained text source is empty")
        options = (source_options or {}).get(source.resolve(), {})
        frontmatter_end = retained_markdown_frontmatter_end(original) if format_name == "md" and options.get("git_snapshot") is True else 0
        original_lines = original.splitlines(keepends=True)
        metadata = "".join(original_lines[:frontmatter_end])
        body = "".join(original_lines[frontmatter_end:])
        text = metadata + rewrite_markdown_hrefs(body, link_rewrites) if format_name == "md" else original
        heading_text = "\n" * frontmatter_end + body if frontmatter_end else original
        headings = extract_markdown_headings(heading_text, source_path, structured=True) if format_name == "md" else []
        known_anchors.update(f"{stem}-L{line}" for line in {1, *(heading["line"] for heading in headings)})
        if format_name == "md":
            known_anchors.update(re.findall(r'<a\b[^>]*\bid=["\']([^"\']+)["\']', heading_text))
        elif format_name == "html":
            options = (source_options or {}).get(source.resolve(), {})
            body = retained_html_body(original, dated_html_response=options.get("dated_html_response") is True, wiki_page_revision_set=options.get("wiki_page_revision_set") is True, content_selector=options.get("content_selector"), exclude_selectors=options.get("exclude_selectors"))
            ids = {str(node["id"]) for node in body.find_all(id=True) if node.name not in {"script", "style", "template"} and not node.find_parent(["pre", "code", "script", "style", "template"])}
            if body.get("id"):
                ids.add(str(body["id"]))
            html_sources[source.resolve()] = (body, stem, ids)
            known_anchors.update(f"{stem}-{name}" for name in ids)
            known_anchors.update(f"{stem}-L{node.sourceline}" for node in body.find_all(re.compile(r"^h[1-6]$")) if not node.find_parent(["pre", "code"]))
        prepared.append((source_path, stem, format_name, text, headings, frontmatter_end))
    if any(target.startswith("#") and target[1:] not in known_anchors for target in link_rewrites.values()):
        raise ValueError("retained href rewrite does not target a real source anchor")

    docfx_root, docfx_calls = preflight_docfx_includes(sources, document.parent.parent.resolve(), source_options or {})
    if docfx_root and link_rewrites:
        raise ValueError("DocFX assembly uses fixed native references, not legacy href rewrites")
    parts: list[str] = []
    selectors: list[dict[str, Any]] = []
    next_line = 1
    def emit(value: str) -> None:
        nonlocal next_line
        if not value.endswith("\n"):
            value += "\n"
        parts.append(value)
        next_line += len(value.splitlines())

    dated_html = any(options.get("dated_html_response") is True for options in (source_options or {}).values())
    wiki_html = any(options.get("wiki_page_revision_set") is True for options in (source_options or {}).values())
    git_sidecar = any(options.get("git_snapshot") is True for options in (source_options or {}).values())
    emit(("# Retained documentation text (collector assembly)\n\n" if docfx_root else "# Retained wiki page revision set (collector assembly)\n\n" if wiki_html else "# Retained specification text (collector assembly)\n\n") + ("> " if dated_html or git_sidecar or wiki_html else "") + "This consumer Markdown assembles the explicitly retained originals in declared order. Source labels, line anchors and local href rewrites are collector additions; " + ("only explicitly declared one-level DocFX include bodies are expanded in place, with fixed source reference URLs; include frontmatter is not body text.\n" if docfx_root else "HTML is represented as structural text with ordered table cells and preserved code, without running source scripts.\n" if has_html else "YAML below is an unmodified native document displayed in a code fence; an explicitly declared example is not a schema.\n" if git_sidecar else "YAML below is an unmodified native schema displayed in a code fence.\n"))
    if docfx_root:
        native = {ROOT.resolve() / item[0]: item for item in prepared}
        main_path, main_stem, _, main_text, main_headings, _ = native[docfx_root]

        def emit_native_span(source: Path, first: int, last: int, included_at: dict[str, Any] | None = None) -> None:
            source_path, stem, _, text, headings, frontmatter_end = native[source]
            lines = text.splitlines(keepends=True)
            body = "".join(lines[first - 1:last])
            if not body.strip():
                emit(body)
                return
            source_url = (source_options or {})[source]["source_url"]
            references = {match.group(1): urllib.parse.urljoin(source_url, match.group(1)) for match in re.finditer(r"\]\([ \t]*([^\s)]+)", body) if not match.group(1).startswith("#") and not urllib.parse.urlsplit(match.group(1)).scheme and not urllib.parse.urlsplit(match.group(1)).netloc}
            if any(reference.startswith("/") for reference in references):
                raise ValueError("DocFX root-relative references need an explicitly reviewed document base")
            rendered = rewrite_markdown_hrefs(body, references)
            prefix = f"{stem}-at-{main_stem}-L{included_at['line']}" if included_at else stem
            emit(f'\n<a id="{prefix}-L{first}"></a>\n\n')
            if first == 1 and frontmatter_end:
                emit(f"> Collector metadata display: original leading YAML frontmatter, source lines 1–{frontmatter_end}; not an upstream body heading.\n\n")
                rendered = tex_reading_fence("".join(lines[:frontmatter_end]), "yaml") + rewrite_markdown_hrefs("".join(lines[frontmatter_end:last]), references)
            start = next_line
            emit(rendered)
            heading = next((item for item in headings if item["line"] == first), None)
            selectors.append({
                "selector": f"derived://{local_path}#L{start}-L{next_line - 1}", "local_path": local_path,
                "kind": "section" if heading else "file", "start_line": start, "end_line": next_line - 1,
                "text_preview": next(line.rstrip("\r\n") for line in rendered.splitlines(keepends=True) if line.strip())[:700],
                "derived_from": source_path, "source_format": "md", "source_start_line": first, "source_end_line": last,
                "transformation": "native Markdown with collector anchors and fixed source reference URLs" + ("; explicitly declared DocFX include body expanded in place" if included_at else "; leading YAML displayed as literal collector metadata" if first == 1 and frontmatter_end else ""),
                **({"included_at": included_at} if included_at else {}),
                **({"heading": heading["heading"], "level": heading["level"]} if heading else {}),
            })

        main_lines = main_text.splitlines()
        href = Path(os.path.relpath(docfx_root, start=document.parent.resolve())).as_posix()
        emit(f"\nOriginal MD: [{docfx_root.name}]({href}#L1-L{len(main_lines)}).\n")
        starts = sorted({1, *(heading["line"] for heading in main_headings), *docfx_calls, *(line + 1 for line in docfx_calls if line < len(main_lines))})
        for index, first in enumerate(starts):
            last = starts[index + 1] - 1 if index + 1 < len(starts) else len(main_lines)
            if first not in docfx_calls:
                emit_native_span(docfx_root, first, last)
                continue
            target = docfx_calls[first]
            source_path, _, _, text, headings, frontmatter_end = native[target]
            target_href = Path(os.path.relpath(target, start=document.parent.resolve())).as_posix()
            emit(f"\n> Collector include: [{target.name}]({target_href}#L{frontmatter_end + 1}-L{len(text.splitlines())}), called at [{docfx_root.name} line {first}]({href}#L{first}-L{first}); original Markdown retained unchanged.\n")
            body_starts = sorted({frontmatter_end + 1, *(heading["line"] for heading in headings)})
            for body_index, body_first in enumerate(body_starts):
                body_last = body_starts[body_index + 1] - 1 if body_index + 1 < len(body_starts) else len(text.splitlines())
                emit_native_span(target, body_first, body_last, {"source": main_path, "line": first})
        document.parent.mkdir(parents=True, exist_ok=True)
        document.write_bytes("".join(parts).encode("utf-8"))
        return selectors
    if dated_html or wiki_html:
        emit("\n> Collector representation: declared cell spans are annotations, not an expanded table grid; code br line breaks and NBSP are retained, and image-label whitespace is normalized without dropping label words.\n")
    if wiki_html:
        emit("\n> Collector snapshot limitation: oldid identifies each page revision, not all transcluded templates or skin dependencies. The saved rendered HTML responses are the offline originals; source scripts are not executed.\n")
        if any(options.get("image_text_alternatives") for options in (source_options or {}).values()):
            emit("\n> Collector image-alt representation: explicitly declared semantic-marker images are represented by their exact source alt and original links, not OCR or model-supplied text; those marker image bytes are not retained locally. Original Y/N fallback and surrounding examples remain source text.\n")
    for source_path, stem, format_name, text, headings, frontmatter_end in prepared:
        options = (source_options or {}).get(ROOT.resolve() / source_path, {})
        lines = text.splitlines(keepends=True)
        href = Path(os.path.relpath(ROOT.resolve() / source_path, start=document.parent.resolve())).as_posix()
        emit(f"\nOriginal {format_name.upper()}: [{Path(source_path).name}]({href}#L1-L{len(lines)}).\n")
        if format_name == "html":
            source = ROOT.resolve() / source_path
            options = (source_options or {}).get(source, {})
            if options.get("wiki_page_revision_set") is True:
                emit(f"\n> Collector page identity: {options['page_title']}; [fixed page revision]({options['source_url']}).\n")
            article_selector = options.get("content_selector") if options.get("dated_html_response") is True else None
            if article_selector is not None:
                emit("\n> Collector content boundary: only the article selected by " + json.dumps(article_selector, ensure_ascii=False) + " is represented below. Original-line ranges are enclosing provenance bounds; the final range may extend to HTML entity EOF and does not imply that every line was converted.\n")
            if options.get("dated_html_response") is True and options.get("unretained_assets"):
                emit("\n> Collector asset gap: these original figures are linked to the publisher response but their image bytes are not retained locally: " + ", ".join(f"[{reference}]({urllib.parse.urljoin(options['source_url'], reference)})" for reference in options["unretained_assets"]) + ".\n")
            emit(f'\n<a id="{stem}-L1"></a>\n')
            static_html = options.get("dated_html_response") is True or options.get("wiki_page_revision_set") is True
            for section in retained_html_sections(source, document.resolve(), html_sources, link_rewrites, options.get("source_url", ""), dated_html_response=static_html, unretained_assets=options.get("unretained_assets"), wiki_page_revision_set=options.get("wiki_page_revision_set") is True, image_text_alternatives=options.get("image_text_alternatives")):
                if section.get("heading_line"):
                    emit(f'\n<a id="{stem}-L{section["heading_line"]}"></a>\n')
                start_line = next_line
                emit(section["text"])
                preview = next(line for line in section["text"].splitlines() if line.strip() and not line.startswith("<a "))[:700]
                selectors.append({
                    "selector": f"derived://{local_path}#L{start_line}-L{next_line - 1}", "local_path": local_path,
                    "kind": "section" if section.get("heading") else "file", "start_line": start_line, "end_line": next_line - 1,
                    "text_preview": preview, "derived_from": source_path, "source_format": "html",
                    **({"transformation": "static HTML structural text with declared UI exclusions and local href routes" + ("; declared article filtering with content_selector=" + json.dumps(article_selector, ensure_ascii=False) + "; enclosing original-line provenance bounds, not full-response coverage" if article_selector is not None else "") + ("; declared original figure links without retained image bytes" if options.get("unretained_assets") else "") + ("; declared semantic-marker images represented by exact source alt, not OCR" if options.get("image_text_alternatives") else "")} if static_html else {}),
                    **({"source_heading_line": section["heading_line"]} if section.get("heading_line") else {}),
                    **{key: value for key, value in section.items() if key in {"source_start_line", "source_end_line", "heading", "level"}},
                })
            if "config_range" in options:
                bounds = options["config_range"]
                start, end = bounds["start_line"], bounds["end_line"]
                if any(not isinstance(value, int) or isinstance(value, bool) for value in (start, end)) or not 1 <= start <= end <= len(lines):
                    raise ValueError("retained HTML config_range must identify real original lines")
                preview = next((line.rstrip("\r\n") for line in lines[start - 1:end] if line.strip()), "")[:700]
                if not preview:
                    raise ValueError("retained HTML config_range contains no source text")
                emit(f"\nReSpec configuration provenance (not executed): [original HTML lines {start}–{end}]({href}#L{start}-L{end}).\n")
                selectors.append({
                    "selector": f"source://{source_path}#L{start}-L{end}", "local_path": source_path, "kind": "configuration",
                    "start_line": start, "end_line": end, "text_preview": preview, "derived_from": source_path,
                    "source_format": "html", "source_start_line": start, "source_end_line": end,
                })
            continue
        if format_name == "yaml":
            label = "example" if options.get("git_snapshot") is True and options.get("role") == "example" else "schema"
            emit(f'\n<a id="{stem}-L1"></a>\n\n## Native YAML {label} (collector display, not upstream Markdown)\n\n```yaml\n')
        starts = [(1, headings[0] if headings else None)] + [(heading["line"], heading) for heading in headings[1:]]
        if frontmatter_end:
            starts = [(1, None)] + [(heading["line"], heading) for heading in headings]
        anchors = {1, *(heading["line"] for heading in headings)} if format_name == "md" else set()
        for index, (source_start, heading) in enumerate(starts):
            source_end = starts[index + 1][0] - 1 if index + 1 < len(starts) else len(lines)
            start_line = next_line
            if frontmatter_end and source_start == 1:
                emit(f'\n<a id="{stem}-L1"></a>\n\n> Collector metadata display: original leading YAML frontmatter, source lines 1–{frontmatter_end}; not an upstream body heading.\n')
                start_line = next_line
                emit(tex_reading_fence("".join(lines[:frontmatter_end]), "yaml"))
                for line in lines[frontmatter_end:source_end]:
                    emit(line)
            else:
                for line_number in range(source_start, source_end + 1):
                    if line_number in anchors:
                        emit(f'\n<a id="{stem}-L{line_number}"></a>\n\n')
                        if line_number == source_start:
                            start_line = next_line
                    emit(lines[line_number - 1])
            selectors.append({
                "selector": f"derived://{local_path}#L{start_line}-L{next_line - 1}",
                "local_path": local_path, "kind": "section" if heading else "file",
                "start_line": start_line, "end_line": next_line - 1,
                "text_preview": next(line.rstrip("\r\n") for line in lines[source_start - 1:source_end] if line.strip())[:700],
                "derived_from": source_path, "source_format": format_name,
                "source_start_line": source_start, "source_end_line": source_end,
                **({"transformation": "native Markdown with collector line anchors and declared local href rewrites" + ("; leading YAML frontmatter displayed as literal collector metadata" if frontmatter_end and source_start == 1 else "") if format_name == "md" else "native YAML displayed unchanged in a fenced collector assembly",
                    **({"source_role": "example"} if options.get("role") == "example" else {})} if options.get("git_snapshot") is True else {}),
                **({"heading": heading["heading"], "level": heading["level"]} if heading else {}),
            })
        if format_name == "yaml":
            emit("```\n")
    document.parent.mkdir(parents=True, exist_ok=True)
    document.write_bytes("".join(parts).encode("utf-8"))
    return selectors


def github_git_inventory(
    repository: str,
    config: dict[str, Any],
) -> tuple[dict[str, Any], str, str, str, None, dict[str, Any], None]:
    """Freeze a public repository and expose bounded raw-file candidates.

    ``git ls-remote`` provides the immutable default-branch commit without using the
    rate-limited REST API. Evidence is then fetched from commit-pinned raw URLs for a
    small set of conventional high-value paths. This intentionally does not claim to
    be a complete repository tree inventory.
    """
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
        raise RuntimeError(f"unsafe owner/repository identifier: {repository}")

    env = os.environ.copy()
    env.update({"GIT_TERMINAL_PROMPT": "0", "GIT_LFS_SKIP_SMUDGE": "1"})
    result = subprocess.run(
        ["git", "ls-remote", "--symref", f"https://github.com/{repository}.git", "HEAD"],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        timeout=60,
        check=False,
    )
    if result.returncode != 0:
        diagnostic = (result.stderr or result.stdout).strip().splitlines()
        raise RuntimeError(diagnostic[-1] if diagnostic else f"git ls-remote exited {result.returncode}")
    default_branch = "HEAD"
    commit_sha = ""
    for line in result.stdout.splitlines():
        if line.startswith("ref: ") and line.endswith("\tHEAD"):
            default_branch = line.split("\t", 1)[0].removeprefix("ref: refs/heads/")
        elif line.endswith("\tHEAD"):
            commit_sha = line.split("\t", 1)[0]
    if not re.fullmatch(r"[0-9a-f]{40}", commit_sha):
        raise RuntimeError("git ls-remote did not return an immutable HEAD commit")

    candidate_paths = [
        "README.md", "README.rst", "README.txt", "README",
        "CONTRIBUTING.md", "SECURITY.md", "AGENTS.md", "CLAUDE.md",
        "pyproject.toml", "package.json", "Cargo.toml", "go.mod", "pom.xml",
        "Makefile", "Dockerfile", "docs/README.md", "docs/index.md",
        "docs/architecture.md", "docs/design.md", "docs/api.md",
        "documentation/README.md",
    ]
    entries = [
        {
            "path": path,
            "type": "blob",
            "sha": None,
            "size": 1,
            "url": None,
            "_raw_url": f"https://raw.githubusercontent.com/{repository}/{commit_sha}/{urllib.parse.quote(path)}",
        }
        for path in candidate_paths
    ]
    repo_info = {
        "full_name": repository,
        "default_branch": default_branch,
        "html_url": f"https://github.com/{repository}",
        "description": None,
        "language": None,
        "topics": [],
        "license": None,
    }
    return repo_info, repository, default_branch, commit_sha, None, {"tree": entries, "truncated": True, "fallback": "commit_pinned_raw_paths"}, None


def materialize_github(record: SourceRecord, config: dict[str, Any], generated_at: str) -> dict[str, Any]:
    root = prepare_capsule(record)
    manifest = base_manifest(record, "github_repo_semantic_capsule_v2", generated_at)
    repository = record.canonical_id
    if not repository or "/" not in repository:
        manifest["errors"].append("missing canonical owner/repository")
        return finalize_capsule(record, root, manifest)

    api_root = f"https://api.github.com/repos/{repository}"
    git_clone_root: Path | None = None
    try:
        repo_info = github_api_json(api_root)
        canonical_repo = str(repo_info.get("full_name") or repository)
        default_branch = str(repo_info.get("default_branch") or "HEAD")
        commit_info = github_api_json(f"https://api.github.com/repos/{canonical_repo}/commits/{urllib.parse.quote(default_branch, safe='')}")
        commit_sha = str(commit_info.get("sha"))
        commit_tree = commit_info.get("commit", {}).get("tree", {})
        tree_sha = str(commit_tree.get("sha") or "")
        if not tree_sha:
            raise RuntimeError("default branch commit has no tree SHA")
        try:
            tree_info = github_api_json(
                f"https://api.github.com/repos/{canonical_repo}/git/trees/{tree_sha}?recursive=1",
                max_bytes=int(config.get("github_max_tree_response_bytes", 50_000_000)),
            )
        except Exception as tree_error:
            # Large repositories can exceed the recursive-tree response budget. Fall back to
            # bounded root/docs listings instead of degrading immediately to metadata-only.
            manifest["warnings"].append(f"recursive tree fallback: {tree_error}")
            fallback_entries: list[dict[str, Any]] = []
            listing_urls = [
                f"https://api.github.com/repos/{canonical_repo}/contents?ref={commit_sha}",
                f"https://api.github.com/repos/{canonical_repo}/contents/docs?ref={commit_sha}",
                f"https://api.github.com/repos/{canonical_repo}/contents/doc?ref={commit_sha}",
            ]
            for listing_url in listing_urls:
                try:
                    payload, _, _ = fetch_bytes(listing_url, timeout=35, max_bytes=8_000_000)
                    listing = json.loads(payload.decode("utf-8"))
                    if isinstance(listing, list):
                        for listed in listing:
                            if not isinstance(listed, dict) or listed.get("type") != "file":
                                continue
                            fallback_entries.append(
                                {
                                    "path": listed.get("path"),
                                    "type": "blob",
                                    "sha": listed.get("sha"),
                                    "size": listed.get("size"),
                                    "url": listed.get("git_url"),
                                }
                            )
                except Exception as listing_error:
                    manifest["warnings"].append(f"listing fallback failed: {listing_error}")
            tree_info = {"tree": fallback_entries, "truncated": True, "fallback": True}
    except Exception as api_error:
        try:
            repo_info, canonical_repo, default_branch, commit_sha, tree_sha, tree_info, git_clone_root = github_git_inventory(repository, config)
            manifest["warnings"].append(f"GitHub API unavailable; used Git transport fallback: {api_error}")
        except Exception as git_error:
            manifest["errors"].append(f"GitHub API: {api_error}")
            manifest["errors"].append(f"Git fallback: {git_error}")
            manifest["status"] = "metadata_only"
            return finalize_capsule(record, root, manifest)

    entries = tree_info.get("tree") if isinstance(tree_info.get("tree"), list) else []
    blobs = [entry for entry in entries if isinstance(entry, dict) and entry.get("type") == "blob"]
    extension_counts: Counter[str] = Counter()
    top_level_counts: Counter[str] = Counter()
    for entry in blobs:
        path = str(entry.get("path") or "")
        pure = PurePosixPath(path)
        extension_counts[pure.suffix.lower() or "<none>"] += 1
        top_level_counts[pure.parts[0] if pure.parts else "<root>"] += 1

    max_files = int(config.get("github_max_evidence_files", 35))
    max_file_bytes = int(config.get("github_max_single_file_bytes", 250_000))
    max_total_bytes = int(config.get("github_max_total_evidence_bytes", 3_000_000))
    ranked = sorted(blobs, key=lambda entry: github_file_rank(str(entry.get("path") or "")))
    selected: list[dict[str, Any]] = []
    total_selected_size = 0
    seen_paths: set[str] = set()
    for entry in ranked:
        path = str(entry.get("path") or "")
        if path in seen_paths:
            continue
        seen_paths.add(path)
        rank = github_file_rank(path)[0]
        size = int(entry.get("size") or 0)
        suffix = PurePosixPath(path).suffix.lower()
        if rank >= 10 or (suffix and suffix not in GITHUB_TEXT_EXTENSIONS) or size <= 0 or size > max_file_bytes:
            continue
        if len(selected) >= max_files or total_selected_size + size > max_total_bytes:
            continue
        selected.append(entry)
        total_selected_size += size

    evidence_root = root / "evidence" / "files"
    evidence_rows: list[dict[str, Any]] = []
    selector_rows: list[dict[str, Any]] = []
    headings: list[dict[str, Any]] = []
    document_parts: list[str] = []
    for entry in selected:
        path = str(entry.get("path") or "")
        safe_path = sanitize_relative_path(path)
        if safe_path is None:
            continue
        try:
            if entry.get("_raw_url"):
                raw, _, _ = fetch_bytes(
                    str(entry["_raw_url"]),
                    timeout=20,
                    max_bytes=max_file_bytes,
                    attempts=1,
                )
            elif git_clone_root is not None:
                raw = (git_clone_root / safe_path.as_posix()).read_bytes()
            else:
                blob = github_api_json(str(entry.get("url")))
                raw = decode_github_blob(blob)
            if b"\x00" in raw[:4096]:
                continue
            text = raw.decode("utf-8", errors="replace")
        except Exception as exc:
            manifest["warnings"].append(f"{path}: {exc}")
            continue
        destination = evidence_root / safe_path.as_posix()
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text, encoding="utf-8")
        lines = text.splitlines()
        local_path = destination.relative_to(ROOT).as_posix()
        selector_base = f"github://{canonical_repo}@{commit_sha}/{path}"
        selector_rows.append(
            {
                "selector": f"{selector_base}#L1-L{max(1, len(lines))}",
                "local_path": local_path,
                "kind": "file",
                "start_line": 1,
                "end_line": max(1, len(lines)),
            }
        )
        for heading in extract_markdown_headings(text, path):
            headings.append(heading)
            selector_rows.append(
                {
                    "selector": f"{selector_base}#L{heading['line']}",
                    "local_path": local_path,
                    "kind": "heading",
                    "heading": heading["heading"],
                    "start_line": heading["line"],
                    "end_line": heading["line"],
                }
            )
        evidence_rows.append(
            {
                "repository_path": path,
                "local_path": local_path,
                "blob_sha": entry.get("sha"),
                "bytes": destination.stat().st_size,
                "sha256": sha256_file(destination),
                "lines": len(lines),
            }
        )
        excerpt_lines = lines[: min(len(lines), int(config.get("github_document_excerpt_lines", 220)))]
        document_parts.append(f"\n\n## `{path}`\n\n" + "\n".join(excerpt_lines))

    write_jsonl(root / "evidence" / "files.jsonl", evidence_rows)
    write_jsonl(root / "selectors.jsonl", selector_rows)
    repository_map = {
        "repository": canonical_repo,
        "requested_repository": repository,
        "default_branch": default_branch,
        "commit": commit_sha,
        "tree_sha": tree_sha,
        "tree_truncated": bool(tree_info.get("truncated")),
        "repository_description": repo_info.get("description"),
        "primary_language": repo_info.get("language"),
        "topics": repo_info.get("topics") or [],
        "license": (repo_info.get("license") or {}).get("spdx_id") if isinstance(repo_info.get("license"), dict) else None,
        "repository_file_count_seen": len(blobs),
        "selected_evidence_files": len(evidence_rows),
        "top_level_counts": dict(top_level_counts.most_common(30)),
        "extension_counts": dict(extension_counts.most_common(30)),
        "prominent_headings": headings[:250],
    }
    write_yaml(root / "repository-map.yaml", repository_map)

    description = str(repo_info.get("description") or record.title or "No repository description supplied.")
    document_header = (
        f"# Repository semantic capsule: {canonical_repo}\n\n"
        f"- Commit: `{commit_sha}`\n"
        f"- Default branch: `{default_branch}`\n"
        f"- Description: {description}\n"
        f"- Selected evidence files: {len(evidence_rows)} of {len(blobs)} files observed\n"
        "- Interpretation: maintainer documentation and static repository evidence; runtime behavior is not proven.\n"
    )
    (root / "document.md").write_text(document_header + "".join(document_parts) + "\n", encoding="utf-8")

    wiki_root = root / "wiki"
    wiki_root.mkdir(parents=True, exist_ok=True)
    (wiki_root / "index.md").write_text(
        f"# {canonical_repo}\n\n"
        "- [Overview](overview.md)\n"
        "- [Architecture evidence](architecture.md)\n"
        "- [Interfaces and operations](interfaces-and-operations.md)\n",
        encoding="utf-8",
    )
    heading_lines = [f"- `{item['path']}:{item['line']}` — {item['heading']}" for item in headings[:120]]
    (wiki_root / "overview.md").write_text(
        f"# Overview: {canonical_repo}\n\n{description}\n\n"
        f"Frozen at `{commit_sha}`. This is a candidate semantic view, not a verified runtime assessment.\n",
        encoding="utf-8",
    )
    (wiki_root / "architecture.md").write_text(
        f"# Architecture evidence: {canonical_repo}\n\n"
        + ("\n".join(heading_lines) if heading_lines else "No architecture headings were extracted.")
        + "\n",
        encoding="utf-8",
    )
    interface_files = [row["repository_path"] for row in evidence_rows if any(token in row["repository_path"].lower() for token in ("api", "cli", "config", "schema", "workflow", "interface"))]
    (wiki_root / "interfaces-and-operations.md").write_text(
        f"# Interfaces and operations: {canonical_repo}\n\n"
        + "\n".join(f"- `{path}`" for path in interface_files[:100])
        + "\n",
        encoding="utf-8",
    )

    manifest.update(
        {
            "status": "materialized" if evidence_rows else "partial",
            "content_tier": "semantic_capsule" if evidence_rows else "metadata_capsule",
            "canonical_id": canonical_repo,
            "canonical_url": str(repo_info.get("html_url") or record.canonical_url),
            "revision": commit_sha,
            "rights": {
                "declared_access": record.rights_access,
                "full_text_redistribution_assumed": False,
                "repository_license": repository_map["license"],
                "basis": "bounded commit-pinned evidence selection; repository not vendored",
            },
            "retrievals": [
                {
                    "resolved_url": str(repo_info.get("html_url") or record.canonical_url),
                    "commit": commit_sha,
                    "tree_sha": tree_sha,
                    "tree_truncated": bool(tree_info.get("truncated")),
                }
            ],
            "materialization": {
                "repository_file_count_seen": len(blobs),
                "selected_evidence_files": len(evidence_rows),
                "selected_evidence_bytes": sum(row["bytes"] for row in evidence_rows),
                "selector_count": len(selector_rows),
                "repo_wiki_pages": 4,
            },
            "selectors": ["selectors.jsonl"],
            "limitations": [
                "The full repository is not copied.",
                "Static evidence does not prove tests, benchmarks, security, or production behavior.",
                "Generated repo wiki pages remain candidate views.",
            ],
        }
    )
    result = finalize_capsule(record, root, manifest)
    if git_clone_root is not None:
        shutil.rmtree(git_clone_root.parent, ignore_errors=True)
    return result


def html_to_sections(payload: bytes, resolved_url: str) -> tuple[str, list[dict[str, Any]], str | None]:
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(payload, "html.parser")
    for tag in soup(["script", "style", "noscript", "svg", "canvas", "form", "nav", "footer"]):
        tag.decompose()
    title = soup.title.get_text(" ", strip=True) if soup.title else None
    main = soup.find("main") or soup.find("article") or soup.body or soup
    blocks: list[dict[str, Any]] = []
    text_parts: list[str] = []
    index = 0
    for node in main.find_all(["h1", "h2", "h3", "h4", "p", "li", "pre"]):
        text = node.get_text(" ", strip=True)
        if not text or len(text) < 2:
            continue
        index += 1
        kind = "heading" if node.name and node.name.startswith("h") else ("code" if node.name == "pre" else "paragraph")
        blocks.append(
            {
                "selector": f"web://{sha256_bytes(resolved_url.encode())[:16]}#B{index}",
                "kind": kind,
                "ordinal": index,
                "text_preview": text[:240],
            }
        )
        if kind == "heading":
            level = int(node.name[1]) if node.name and len(node.name) > 1 and node.name[1].isdigit() else 2
            text_parts.append("\n" + "#" * min(6, max(1, level)) + " " + text + "\n")
        else:
            text_parts.append(text + "\n")
    return "\n".join(text_parts).strip() + "\n", blocks, title


def extract_pdf_text(
    payload: bytes, max_pages: int | None = None, *, extraction_mode: str = "layout",
) -> tuple[str, list[dict[str, Any]], int]:
    from pypdf import PdfReader

    if extraction_mode not in {"layout", "plain"}:
        raise ValueError("unsupported PDF text extraction mode")
    reader = PdfReader(io.BytesIO(payload))
    page_count = len(reader.pages)
    limit = page_count if max_pages is None else min(page_count, max_pages)
    text_parts: list[str] = []
    selectors: list[dict[str, Any]] = []
    for page_index in range(limit):
        try:
            text = reader.pages[page_index].extract_text(
                extraction_mode=extraction_mode,
                **({"layout_mode_strip_rotated": False} if extraction_mode == "layout" else {}),
            ) or ""
        except Exception as exc:
            text = f"[page extraction failed: {exc}]"
        text_parts.append(f"\n\n## Page {page_index + 1}\n\n{text.strip()}\n")
        selectors.append(
            {
                "selector": f"pdf://sha256-PENDING#page={page_index + 1}",
                "kind": "page",
                "page": page_index + 1,
                "text_preview": text.strip()[:240],
            }
        )
    return "".join(text_parts).strip() + "\n", selectors, page_count


def arxiv_pdf_version_url(canonical_id: Any, source_version: Any) -> str:
    """Require an existing arXiv identity and an explicit, positive version."""
    if not isinstance(canonical_id, str) or not re.fullmatch(r"\d{4}\.\d{4,5}", canonical_id):
        raise ValueError("PDF supplement requires an unversioned arXiv canonical ID")
    if not isinstance(source_version, str) or not re.fullmatch(r"v[1-9]\d*", source_version):
        raise ValueError("PDF supplement requires a fixed vN source version")
    return f"https://arxiv.org/pdf/{canonical_id}{source_version}"


def normalize_publisher_doi(value: Any) -> str | None:
    """Compare reviewed DOI identifiers without treating them as source identities."""
    if not isinstance(value, str):
        return None
    normalized = value.strip().lower()
    for prefix in ("doi:", "https://doi.org/"):
        if normalized.startswith(prefix):
            normalized = normalized.removeprefix(prefix)
            break
    return normalized.strip() or None


def pdf_supplement_version_urls(
    manifest: dict[str, Any], canonical: dict[str, Any], capsule: dict[str, Any], source_version: Any,
) -> tuple[str, str | None]:
    """Bind the existing arXiv representation or an explicitly reviewed publisher work."""
    arxiv = manifest.get("source_type") == "arxiv" and manifest.get("adapter") == "arxiv_latex_v2"
    journal = manifest.get("source_type") == "journal" and manifest.get("adapter") == "generic_web_or_document_v2"
    if not arxiv and not journal:
        raise ValueError("PDF supplement requires an existing arXiv TeX or declared journal capsule")
    versions = []
    for metadata in (canonical, capsule):
        versioning = metadata.get("versioning")
        if versioning is not None and not isinstance(versioning, dict):
            raise ValueError("PDF supplement versioning must be a mapping or null")
        versions.append(versioning or {})
    publisher_declared = any("publisher_pdf" in versioning for versioning in versions)
    if arxiv and not publisher_declared:
        url = arxiv_pdf_version_url(manifest.get("canonical_id"), source_version)
        if any(versioning.get("source_version") != source_version for versioning in versions):
            raise ValueError("PDF supplement version differs from the retained source version")
        return url, None
    for metadata in (canonical, capsule):
        if any(metadata.get(field) != manifest.get(field) for field in ("uid", "source_type", "canonical_id", "canonical_url")):
            raise ValueError("publisher PDF canonical identity differs from the retained work")
    declaration = versions[0].get("publisher_pdf")
    if not isinstance(declaration, dict) or declaration != versions[1].get("publisher_pdf"):
        raise ValueError("canonical and capsule publisher PDF declarations differ")
    doi = declaration.get("doi")
    canonical_id = manifest.get("canonical_id")
    if arxiv:
        correspondence = declaration.get("correspondence")
        if (
            not isinstance(canonical_id, str) or not re.fullmatch(r"\d{4}\.\d{4,5}", canonical_id)
            or not isinstance(correspondence, dict) or correspondence.get("reviewed") is not True
            or versions[1]["publisher_pdf"]["correspondence"].get("reviewed") is not True
            or correspondence.get("originating_arxiv_id") != canonical_id
            or normalize_publisher_doi(doi) is None
            or normalize_publisher_doi(correspondence.get("publisher_doi")) != normalize_publisher_doi(doi)
            or not isinstance(correspondence.get("audit_evidence_kind"), str)
            or not correspondence["audit_evidence_kind"].strip()
            or versions[0].get("source_version") != versions[1].get("source_version")
        ):
            raise ValueError("publisher PDF needs an explicitly reviewed originating arXiv/DOI correspondence")
    elif not isinstance(doi, str) or not doi.strip() or not isinstance(canonical_id, str) or doi != canonical_id.removeprefix("doi:"):
        raise ValueError("publisher PDF DOI differs from the retained work")
    if (
        not isinstance(source_version, str) or not source_version.startswith("publisher-vor:")
        or not source_version.removeprefix("publisher-vor:").strip() or "\n" in source_version or "\r" in source_version
        or declaration.get("source_version") != source_version
    ):
        raise ValueError("publisher PDF version differs from its explicit declaration")
    si = declaration.get("supplementary_information")
    if not isinstance(si, dict) or type(si.get("required")) is not bool:
        raise ValueError("publisher PDF must explicitly declare whether SI is required")
    si_url = si.get("source_pdf_url")
    if (si["required"] and not isinstance(si_url, str)) or (not si["required"] and si_url is not None):
        raise ValueError("publisher SI requirement and approved URL disagree")
    main_url = declaration.get("source_pdf_url")
    for url in (main_url, si_url) if si["required"] else (main_url,):
        if not isinstance(url, str):
            raise ValueError("publisher PDF requires an explicitly approved URL")
        parsed = urllib.parse.urlsplit(url)
        if (
            parsed.scheme != "https" or not parsed.netloc or not parsed.path or parsed.query or parsed.fragment
            or parsed.username is not None or parsed.password is not None
        ):
            raise ValueError("publisher PDF approved URL must be an explicit HTTPS resource")
    return main_url, si_url


def pdf_supplement_retrieval_url_matches(
    retrieval: dict[str, Any], approved_url: str, *, publisher: bool = False,
) -> bool:
    """Keep real redirect provenance; only Nature's observed cookie query is equivalent."""
    if retrieval.get("requested_urls") != [approved_url]:
        return False
    resolved = retrieval.get("resolved_url")
    if resolved == approved_url:
        return True
    if not publisher or not isinstance(resolved, str):
        return False
    requested, effective = urllib.parse.urlsplit(approved_url), urllib.parse.urlsplit(resolved)
    if (
        requested.scheme != "https" or requested.netloc != "www.nature.com" or requested.query
        or (effective.scheme, effective.netloc, effective.path, effective.fragment)
        != (requested.scheme, requested.netloc, requested.path, "")
    ):
        return False
    query = urllib.parse.parse_qsl(effective.query, keep_blank_values=True)
    values = dict(query)
    return (
        len(query) == 2 and set(values) == {"error", "code"} and values["error"] == "cookies_not_supported"
        and re.fullmatch(r"[0-9a-fA-F]{8}(?:-[0-9a-fA-F]{4}){3}-[0-9a-fA-F]{12}", values["code"]) is not None
    )


def pdf_supplement_content_type_supported(content_type: Any) -> bool:
    """Accept PDF transport MIME labels without rewriting retrieval provenance."""
    return isinstance(content_type, str) and content_type.split(";", 1)[0].strip().lower() in {
        "application/pdf", "application/octet-stream", "binary/octet-stream",
    }


def _derive_pdf_supplement_part(
    root: Path, directory: str, source_version: str, version_url: str,
    retrieval: dict[str, Any], rights: dict[str, Any], *, publisher: bool,
    body_quality_verified: bool, limitations: list[str] | None, primary_excerpt: dict[str, int] | None = None,
) -> tuple[dict[str, Any], str, list[dict[str, Any]]]:
    """Preflight and derive one fixed local PDF entirely in memory."""
    base = root / directory
    base.resolve().relative_to(root.resolve())
    for name in ("document.pdf", "document.txt", "selectors.jsonl", "NOTICE.md"):
        if (base / name).is_symlink():
            raise ValueError("PDF supplement paths must not alias retained files")
    payload = (base / "document.pdf").read_bytes()
    if not payload.startswith(b"%PDF-"):
        raise ValueError("PDF supplement source is not a PDF")
    source_hash = sha256_bytes(payload)
    revision = f"sha256:{source_hash}"
    if (
        not pdf_supplement_retrieval_url_matches(retrieval, version_url, publisher=publisher)
        or retrieval.get("bytes") != len(payload) or retrieval.get("sha256") != source_hash
        or not pdf_supplement_content_type_supported(retrieval.get("content_type"))
        or not isinstance(retrieval.get("retrieved_at"), str) or not retrieval["retrieved_at"].strip()
    ):
        raise ValueError("PDF supplement retrieval does not describe the approved fixed-version PDF")
    package = rights.get("redistribution_package") or {}
    gate = rights.get("publication_gate") or {}
    if not all(isinstance(package.get(field), str) and package[field].strip() for field in (
        "source_revision", "source_version_url", "notice_path", "attribution", "modifications", "scope",
    )) or package.get("source_revision") != revision or package.get("source_version_url") != version_url:
        raise ValueError("PDF supplement needs its own complete, revision-bound redistribution package")
    if publisher and package.get("source_version") != source_version:
        raise ValueError("publisher PDF allowance does not bind its declared source version")
    if gate.get("decision") != "allow" or gate.get("approved_scope") != package.get("scope"):
        raise ValueError("PDF supplement scope has no explicit publication allowance")
    if type(body_quality_verified) is not bool or not isinstance(limitations or [], list) or any(
        not isinstance(value, str) or not value.strip() for value in (limitations or [])
    ):
        raise ValueError("PDF supplement body check and limitations must be explicit")
    document_text, extracted, page_count = extract_pdf_text(payload, extraction_mode="plain")
    selectors, empty_pages, failed_pages = [], [], []
    for original in extracted:
        preview = original.get("text_preview") or ""
        if preview.startswith("[page extraction failed:"):
            failed_pages.append(original["page"])
        elif not preview.strip():
            empty_pages.append(original["page"])
        else:
            selectors.append({
                **original, "selector": f"pdf://sha256-{source_hash[:16]}#page={original['page']}",
                "local_path": (base / "document.txt").relative_to(ROOT).as_posix(),
            })
    if primary_excerpt is not None:
        from validate_materialization_completeness import pdf_primary_excerpt_range
        pdf_primary_excerpt_range({"primary_excerpt": primary_excerpt}, document_text)
    substantive = has_substantive_document_text(document_text)
    if body_quality_verified and (not substantive or failed_pages):
        raise ValueError("PDF supplement body quality cannot hide missing substantive text or extraction failures")
    document_text += redistribution_footer(package)
    part = {
        "source_version": source_version, "revision": revision, "media_type": "application/pdf",
        "retrievals": [dict(retrieval)], "selectors": [f"{directory}/selectors.jsonl"],
        "body_quality_verified": body_quality_verified, "limitations": list(limitations or []),
        **({"primary_excerpt": dict(primary_excerpt)} if primary_excerpt is not None else {}),
        "rights": rights,
        "materialization": {
            "source_pdf": f"{directory}/document.pdf", "source_pdf_sha256": source_hash,
            "document": f"{directory}/document.txt", "normalized_document": f"{directory}/document.txt",
            "stored_characters": len(document_text), "selector_count": len(selectors),
            "pdf_page_count": page_count, "pdf_text_page_count": len(selectors), "pdf_text_extraction_mode": "plain",
            "pdf_pages_without_extractable_text": empty_pages, "pdf_page_extraction_failures": failed_pages,
            "substantive_text": substantive,
        },
    }
    return part, document_text, selectors


def build_pdf_supplement(
    root: Path, source_version: str, retrieval: dict[str, Any], rights: dict[str, Any],
    *, body_quality_verified: bool = False, limitations: list[str] | None = None,
    primary_excerpt: dict[str, int] | None = None,
    supplementary_information: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Derive main and optional required SI PDFs without rebuilding the legacy capsule.

    The caller owns acquisition, the independently reviewed PDF notice, canonical
    metadata/audit updates and the final local-file inventory. No source bytes,
    default document/selectors, manifest or metadata are changed here.
    """
    try:
        manifest = load_yaml(root / "manifest.yaml")
        canonical_path = (ROOT / manifest["metadata_path"]).resolve()
        canonical_path.relative_to(ROOT.resolve())
        canonical = load_yaml(canonical_path)
        capsule = load_yaml(root / "source-metadata.yaml")
        version_url, si_url = pdf_supplement_version_urls(manifest, canonical, capsule, source_version)
        publisher = source_version.startswith("publisher-vor:")
        if (si_url is not None) != (supplementary_information is not None):
            raise ValueError("required publisher SI must be provided exactly once")
        if (root / "pdf-supplement/supplementary-information").exists() and si_url is None:
            raise ValueError("undeclared SI files cannot be retained as an approved representation")
        if publisher:
            for row in manifest.get("local_files", []):
                path = (ROOT / row["path"]).resolve()
                path.relative_to(root.resolve())
                if row.get("bytes") != path.stat().st_size or row.get("sha256") != sha256_file(path):
                    raise ValueError("retained capsule inventory differs before PDF replay")
        main = _derive_pdf_supplement_part(
            root, "pdf-supplement", source_version, version_url, retrieval, rights, publisher=publisher,
            body_quality_verified=body_quality_verified, limitations=limitations, primary_excerpt=primary_excerpt,
        )
        parts = [("pdf-supplement", main)]
        if si_url is not None:
            if not isinstance(supplementary_information, dict) or "supplementary_information" in supplementary_information:
                raise ValueError("only one explicitly declared SI PDF is supported")
            si = _derive_pdf_supplement_part(
                root, "pdf-supplement/supplementary-information", source_version, si_url,
                supplementary_information["retrieval"], supplementary_information["rights"], publisher=True,
                body_quality_verified=supplementary_information.get("body_quality_verified", False),
                limitations=supplementary_information.get("limitations"),
            )
            main[0]["supplementary_information"] = si[0]
            parts.append(("pdf-supplement/supplementary-information", si))
        if publisher:
            from validate_publication_rights import validate_pdf_supplement_rights
            audit = load_yaml(ROOT / "raw_data/audits/materialization_rights_review.yaml")
            review = next((row for row in audit["items"] if isinstance(row, dict) and row.get("uid") == manifest.get("uid")), None)
            errors, blocked = validate_pdf_supplement_rights(
                {**manifest, "pdf_supplement": main[0]}, root / "manifest.yaml", ROOT, review, check_derived=False,
            )
            if errors or blocked:
                raise ValueError("; ".join(errors + blocked))
        # Neither PDF/NOTICE nor any legacy file is written; all parts have passed preflight.
        for directory, (_, text, selectors) in parts:
            (root / directory / "document.txt").write_text(text, encoding="utf-8")
            write_jsonl(root / directory / "selectors.jsonl", selectors)
        return main[0]
    except RedistributionPackageError:
        raise
    except Exception as exc:
        raise RedistributionPackageError(f"PDF supplement preflight/replay failed: {exc}; retained capsule preserved") from exc


def replay_pdf_supplement(record: SourceRecord, manifest: dict[str, Any]) -> dict[str, Any]:
    """Replay declared publisher PDFs before generic acquisition or capsule clearing."""
    try:
        if any(manifest.get(field) != value for field, value in (
            ("uid", record.uid), ("source_type", record.source_type), ("canonical_id", record.canonical_id),
            ("canonical_url", record.canonical_url), ("metadata_path", record.relative_metadata_path),
        )):
            raise ValueError("publisher PDF replay identity differs from the retained capsule")
        from validate_materialization_completeness import validate_pdf_supplement
        inventory = manifest.get("local_files") or []
        errors: list[str] = []
        validate_pdf_supplement(
            manifest, record.capsule_root, {row["path"] for row in inventory},
            {row["path"]: row["sha256"] for row in inventory}, errors, repository_root=ROOT,
        )
        if errors:
            raise ValueError("; ".join(errors))
        old = manifest["pdf_supplement"]
        si = old.get("supplementary_information")
        supplement = build_pdf_supplement(
            record.capsule_root, old["source_version"], old["retrievals"][0], old["rights"],
            body_quality_verified=old["body_quality_verified"], limitations=old["limitations"],
            primary_excerpt=old.get("primary_excerpt"),
            supplementary_information=None if si is None else {
                "retrieval": si["retrievals"][0], "rights": si["rights"],
                "body_quality_verified": si["body_quality_verified"], "limitations": si["limitations"],
            },
        )
        manifest["pdf_supplement"] = supplement
        manifest["local_files"] = local_file_inventory(record.capsule_root)
        manifest["local_bytes"] = sum(row["bytes"] for row in manifest["local_files"])
        write_yaml(record.capsule_root / "manifest.yaml", manifest)
        return manifest
    except RedistributionPackageError:
        raise
    except Exception as exc:
        raise RedistributionPackageError(f"{record.uid}: PDF replay failed: {exc}; retained capsule preserved") from exc


def original_retention_requested(
    manifest: dict[str, Any], root: Path, *, repository_root: Path,
    metadata: dict[str, Any] | None = None, review: dict[str, Any] | None = None,
) -> bool:
    """Use key presence, not truthiness; do not appropriate a legacy paired HTML."""
    if (
        "original_retention" in manifest
        or isinstance(metadata, dict) and any(isinstance(metadata.get(field), dict) and "original_retention" in metadata[field]
                                               for field in ("versioning", "rights"))
        or isinstance(review, dict) and "original_retention" in review
        or (root / "source/NOTICE.md").exists() or (root / "source/NOTICE.md").is_symlink()
    ):
        return True
    metadata_path = manifest.get("metadata_path")
    if metadata is None and isinstance(metadata_path, str) and sanitize_relative_path(metadata_path) is not None:
        path = repository_root / metadata_path
        metadata = load_yaml(path) if path.is_file() else None
    snapshot_path = root / "source-metadata.yaml"
    snapshot = load_yaml(snapshot_path) if snapshot_path.is_file() else None
    return (
        "original_retention" in manifest
        or any(isinstance(item, dict) and isinstance(item.get(field), dict) and "original_retention" in item[field]
               for item in (metadata, snapshot) for field in ("versioning", "rights"))
        or isinstance(review, dict) and "original_retention" in review
        or (root / "source/NOTICE.md").exists() or (root / "source/NOTICE.md").is_symlink()
    )


def preflight_original_retention(
    manifest: dict[str, Any], root: Path, *, repository_root: Path,
    review: dict[str, Any] | None = None, require_allow: bool = True,
) -> dict[str, Any] | None:
    """Validate an independent, unchanged HTML original without writing any file.

    The caller packages the source, finite media, independent NOTICE and inventory
    once. This layer never derives text or replaces the legacy root representation.
    """
    repo_root = repository_root.resolve()
    root = root.absolute()
    root.resolve().relative_to(repo_root)
    if not original_retention_requested(manifest, root, repository_root=repo_root, review=review):
        return None
    metadata_path = manifest.get("metadata_path")
    if not isinstance(metadata_path, str) or sanitize_relative_path(metadata_path) is None:
        raise ValueError("original retention needs its canonical metadata path")
    canonical = load_yaml(repo_root / metadata_path)
    capsule = load_yaml(root / "source-metadata.yaml")
    if not isinstance(canonical, dict) or not isinstance(capsule, dict):
        raise ValueError("original retention metadata must be mappings")

    materialization = manifest.get("materialization")
    paired = isinstance(materialization, dict) and any(field in materialization for field in (
        "retained_markdown_source", "retained_text_sources", "retained_text_binding", "retained_text_selectors",
    ))
    part = manifest.get("original_retention")
    if not isinstance(part, dict) or not part:
        raise ValueError("original retention requires its explicit nonempty manifest declaration")
    if manifest.get("adapter") != "generic_web_or_document_v2" or paired or "pdf_supplement" in manifest:
        raise ValueError("original retention conflicts with a paired/derived representation")
    if "normalized/selectors.jsonl" in (manifest.get("selectors") or []) or (root / "normalized/selectors.jsonl").exists():
        raise ValueError("original retention cannot silently adopt a paired selector sidecar")
    if part.get("source") != "source/specification.html" or part.get("media_type") != "text/html":
        raise ValueError("original retention needs its unchanged source/specification.html")
    version = part.get("source_version")
    if not isinstance(version, str) or not version.strip() or part.get("status") not in {"materialized", "partial"}:
        raise ValueError("original retention version/status must be explicit")
    for field in ("retained_assets", "unretained_assets", "limitations"):
        values = part.get(field)
        if not isinstance(values, list) or any(not isinstance(value, str) or not value.strip() for value in values):
            raise ValueError(f"original retention {field} must be an explicit string list")
    retained, unretained = part["retained_assets"], part["unretained_assets"]
    if len(set(retained + unretained)) != len(retained + unretained):
        raise ValueError("original retention asset declarations overlap or repeat")
    for reference in retained + unretained:
        parsed = urllib.parse.urlsplit(reference)
        if (
            any(char.isspace() for char in reference) or parsed.scheme or parsed.netloc
            or parsed.query or parsed.fragment or not parsed.path or parsed.path != reference
            or Path(reference).is_absolute() or any(piece in {"", ".", ".."} for piece in reference.split("/"))
            or urllib.parse.unquote(reference) != reference or "\\" in reference
        ):
            raise ValueError("original retention media src must be a unique literal relative path")
    if unretained and (part["status"] != "partial" or not part["limitations"]):
        raise ValueError("explicitly unretained media require independent partial status and limitations")

    def regular(path: Path, scope: Path = root) -> Path:
        path.relative_to(repo_root)
        path.resolve().relative_to(scope.resolve())
        for ancestor in (path, *path.parents):
            if ancestor == repo_root:
                break
            if ancestor.is_symlink():
                raise ValueError("original retention files and parents cannot be symlinks")
        if not path.is_file() or not stat.S_ISREG(path.stat().st_mode) or path.stat().st_nlink != 1:
            raise ValueError("original retention requires ordinary, non-aliased files")
        return path

    regular(root / "manifest.yaml")
    regular(repo_root / metadata_path, repo_root)
    regular(root / "source-metadata.yaml")
    if any(manifest.get(field) != canonical.get(field) or capsule.get(field) != canonical.get(field) for field in (
        "uid", "source_type", "canonical_id", "canonical_url", "title",
    )):
        raise ValueError("original retention canonical/capsule identity differs")
    inventory = manifest.get("local_files")
    if not isinstance(inventory, list) or not inventory:
        raise ValueError("original retention needs the complete existing capsule inventory")
    declared_paths, identities, byte_count = set(), set(), 0
    for row in inventory:
        name = row.get("path") if isinstance(row, dict) else None
        if not isinstance(name, str) or sanitize_relative_path(name) is None or name in declared_paths:
            raise ValueError("original retention inventory paths are invalid or repeated")
        path = regular(repo_root / name)
        if path.relative_to(repo_root).as_posix() != name:
            raise ValueError("original retention inventory path aliases another file")
        identity = (path.stat().st_dev, path.stat().st_ino)
        if identity in identities:
            raise ValueError("original retention inventory files alias each other")
        identities.add(identity)
        if type(row.get("bytes")) is not int or row["bytes"] != path.stat().st_size or row.get("sha256") != sha256_file(path):
            raise ValueError("original retention inventory differs from actual bytes")
        declared_paths.add(name)
        byte_count += row["bytes"]
    actual_paths = {path.relative_to(repo_root).as_posix() for path in root.rglob("*")
                    if (path.is_file() or path.is_symlink()) and path != root / "manifest.yaml"}
    if declared_paths != actual_paths or manifest.get("local_bytes") != byte_count:
        raise ValueError("original retention inventory is incomplete or has an incorrect byte total")

    source = regular(root / part["source"])
    source_hash = sha256_file(source)
    if part.get("revision") != f"sha256:{source_hash}":
        raise ValueError("original retention revision differs from its unchanged HTML")
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(source.read_bytes().decode("utf-8"), "html.parser")
    if len(soup.find_all("body")) != 1 or not soup.body.get_text(" ", strip=True):
        raise ValueError("original retention needs one nonempty original HTML body")
    references = {node.get("src" if node.name == "img" else "data") for node in soup.body.find_all(["img", "object"])}
    if any(reference not in references for reference in retained + unretained):
        raise ValueError("original retention media declaration is absent from the actual HTML")
    for reference in unretained:
        if (root / "source" / reference).exists() or (root / "source" / reference).is_symlink():
            raise ValueError("explicitly unretained media must not be published in this capsule")
    allowed_sources = {"source/specification.html", "source/NOTICE.md", *(f"source/{src}" for src in retained)}
    actual_sources = {path.relative_to(root).as_posix() for path in (root / "source").rglob("*") if path.is_file() or path.is_symlink()}
    if allowed_sources != actual_sources:
        raise ValueError("original retention source inventory exceeds or misses its finite declared scope")

    rights = part.get("rights")
    if review is None:
        audit = load_yaml(repo_root / "raw_data/audits/materialization_rights_review.yaml")
        reviews = [row for row in audit["items"] if isinstance(row, dict) and row.get("uid") == manifest.get("uid")]
        if len(reviews) != 1:
            raise ValueError("original retention needs exactly one audited review")
        review = reviews[0]
    if not isinstance(review, dict) or review.get("uid") != manifest.get("uid") or review.get("manifest_path") != (root / "manifest.yaml").relative_to(repo_root).as_posix():
        raise ValueError("original retention audit points to another identity or manifest")
    if not isinstance(rights, dict) or not (
        rights == canonical.get("rights", {}).get("original_retention")
        == capsule.get("rights", {}).get("original_retention") == review.get("original_retention")
    ):
        raise ValueError("original retention canonical, capsule, manifest and audited rights differ")
    if any(not isinstance(rights.get(field), str) or not rights[field].strip() for field in ("license_spdx", "license_url", "license_verified_at")):
        raise ValueError("original retention lacks its independently reviewed license")
    package = rights.get("redistribution_package")
    if not isinstance(package, dict) or any(not isinstance(package.get(field), str) or not package[field].strip() for field in (
        "source_revision", "source_version", "source_version_url", "notice_path", "attribution", "modifications", "scope",
    )):
        raise ValueError("original retention redistribution package is incomplete")
    approved_url = package["source_version_url"]
    parsed = urllib.parse.urlsplit(approved_url)
    if parsed.scheme != "https" or not parsed.netloc or parsed.query or parsed.fragment or parsed.username:
        raise ValueError("original retention needs its literal approved fixed HTTPS URL")
    declaration = {"source_version": version, "source_version_url": approved_url}
    if any(metadata.get("versioning", {}).get("original_retention") != declaration for metadata in (canonical, capsule)):
        raise ValueError("original retention version declaration differs from the selected original")
    if package["source_revision"] != part["revision"] or package["source_version"] != version:
        raise ValueError("original retention rights do not bind this original revision/version")
    gate = rights.get("publication_gate")
    if not isinstance(gate, dict) or gate.get("approved_scope") != package["scope"] or not isinstance(gate.get("reason"), str) or not gate["reason"].strip():
        raise ValueError("original retention allowance must explicitly cover its own scope")
    if require_allow and gate.get("decision") != "allow":
        raise ValueError("original retention requires an independent audited allow decision")
    notice_path = package["notice_path"]
    if sanitize_relative_path(notice_path) is None:
        raise ValueError("original retention NOTICE asset is outside the repository")
    expected_notice = regular(repo_root / notice_path, repo_root).read_bytes()
    if not expected_notice.strip() or regular(root / "source/NOTICE.md").read_bytes() != expected_notice:
        raise ValueError("original retention NOTICE differs from its reviewed complete carrier")
    retrievals = part.get("retrievals")
    originals = [("source/specification.html", approved_url, "text/html"),
                 *((f"source/{src}", urllib.parse.urljoin(approved_url, src), None) for src in retained)]
    if not isinstance(retrievals, list) or len(retrievals) != len(originals) or any(not isinstance(row, dict) for row in retrievals):
        raise ValueError("original retention retrievals must match its retained originals exactly")
    for name, url, media_type in originals:
        records = [row for row in retrievals if row.get("local_path") == name]
        path = regular(root / name)
        if len(records) != 1:
            raise ValueError("original retention needs one retrieval for every retained original")
        row = records[0]
        content_type = row.get("content_type")
        if (
            row.get("requested_url") != url or row.get("resolved_url") != url or row.get("http_status") != 200
            or row.get("sha256") != sha256_file(path) or type(row.get("bytes")) is not int or row["bytes"] != path.stat().st_size
            or not isinstance(row.get("completion_observed_at"), str) or not row["completion_observed_at"].strip()
            or not isinstance(content_type, str) or not content_type.strip()
            or media_type is not None and content_type.split(";", 1)[0].strip().lower() != media_type
            or row.get("content_encoding") is not None
            or any(field in row for field in ("transport_local_path", "transport_bytes", "transport_sha256"))
        ):
            raise ValueError("original retention retrieval differs from its fixed URL, actual bytes or recorded response")
    return part


def replay_original_retention(record: SourceRecord, manifest: dict[str, Any]) -> dict[str, Any]:
    """A normal replay is pure preflight: no acquisition, derivation or finalization."""
    try:
        if any(manifest.get(field) != value for field, value in (
            ("uid", record.uid), ("source_type", record.source_type), ("canonical_id", record.canonical_id),
            ("canonical_url", record.canonical_url), ("title", record.title),
            ("metadata_path", record.relative_metadata_path),
        )):
            raise ValueError("original retention caller identity differs from the existing capsule")
        if preflight_original_retention(manifest, record.capsule_root, repository_root=ROOT) is None:
            raise ValueError("original retention declaration is missing")
        return manifest
    except Exception as exc:
        raise RedistributionPackageError(f"{record.uid}: original retention preflight failed: {exc}; retained capsule preserved") from exc


def filter_selectors_for_document(
    selectors: Iterable[dict[str, Any]],
    document_text: str,
) -> tuple[list[dict[str, Any]], int]:
    """Keep only selectors whose cited evidence remains in ``document_text``.

    Generic adapters create selectors from the downloaded representation before the
    local character budget is applied.  A selector for a removed HTML block or PDF
    page is not locally resolvable merely because its ``local_path`` still exists.
    Preview evidence must occur in the stored text, and line selectors are clamped to
    the actual stored file.
    """

    stored_lines = document_text.splitlines()
    line_count = max(1, len(stored_lines))
    stored_pages = {
        int(match.group(1))
        for match in re.finditer(r"(?m)^## Page (\d+)\s*$", document_text)
    }
    retained: list[dict[str, Any]] = []
    omitted = 0

    for original in selectors:
        selector = dict(original)
        start_line = selector.get("start_line")
        end_line = selector.get("end_line")
        if start_line is not None or end_line is not None:
            if (
                not isinstance(start_line, int)
                or isinstance(start_line, bool)
                or not isinstance(end_line, int)
                or isinstance(end_line, bool)
                or start_line < 1
                or end_line < start_line
                or start_line > line_count
            ):
                omitted += 1
                continue
            clamped_end = min(end_line, line_count)
            selector["end_line"] = clamped_end
            selector_id = selector.get("selector")
            if isinstance(selector_id, str) and clamped_end != end_line:
                selector["selector"] = re.sub(r"(#L\d+-L)\d+$", rf"\g<1>{clamped_end}", selector_id)

        page = selector.get("page")
        if page is not None and (
            not isinstance(page, int)
            or isinstance(page, bool)
            or page < 1
            or page not in stored_pages
        ):
            omitted += 1
            continue

        preview = selector.get("text_preview")
        if preview is not None:
            if not isinstance(preview, str) or not preview or preview not in document_text:
                omitted += 1
                continue

        retained.append(selector)

    return retained, omitted


def has_substantive_document_text(document_text: str) -> bool:
    """Reject navigation/title shells that contain no non-heading evidence."""

    non_heading = re.sub(r"(?m)^\s{0,3}#{1,6}\s+.*$", "", document_text)
    tokens = re.findall(r"[\w\u0080-\uffff]+", non_heading)
    return len(non_heading.strip()) >= 20 and len(tokens) >= 3


def replay_retained_text_sources(
    record: SourceRecord, manifest: dict[str, Any], generated_at: str,
    *, check_derived: bool = True,
) -> dict[str, Any]:
    """Preflight all declared originals before writing a collector assembly."""
    root = record.capsule_root
    materialization = manifest["materialization"]
    dated_html = materialization.get("retained_text_binding") == "dated_html_response"
    wiki_html = materialization.get("retained_text_binding") == "wiki_page_revision_set"
    git_sidecar = materialization.get("retained_text_binding") == "git_snapshot"
    paired_sidecar = dated_html or git_sidecar or wiki_html
    selector_path = retained_text_selector_file(manifest, root, require_exists=paired_sidecar and check_derived)
    if paired_sidecar and (
        not isinstance(record.metadata.get("versioning"), dict)
        or record.metadata["versioning"].get("source_version") != manifest.get("source_version")
        or record.metadata.get("rights", {}).get("redistribution_package") != manifest.get("rights", {}).get("redistribution_package")
        or (dated_html or wiki_html) and record.metadata.get("full_text_url") != manifest.get("rights", {}).get("redistribution_package", {}).get("source_version_url")
    ):
        raise ValueError("retained text replay metadata differs from its reviewed current package")
    if "retained_markdown_source" in materialization:
        raise ValueError("retained single Markdown and ordered text declarations are mutually exclusive")
    document_name = sanitize_relative_path(materialization["document"])
    if document_name is None or document_name.parts[0] != "normalized":
        raise ValueError("retained document must be a capsule-local normalized path")
    document = (root / document_name).resolve()
    document.relative_to(root.resolve())
    sources = materialization["retained_text_sources"]
    if not isinstance(sources, list) or not sources:
        raise ValueError("retained_text_sources must be a nonempty explicit list")
    paths: list[tuple[Path, str]] = []
    for item in sources:
        source_name = sanitize_relative_path(item["source"])
        if source_name is None or source_name.parts[0] != "source":
            raise ValueError("retained text source must be a capsule-local source path")
        source = (root / source_name).resolve()
        source.relative_to(root.resolve())
        paths.append((source, item["format"]))
    from validate_materialization_completeness import validate_retained_markdown_binding
    errors: list[str] = []
    validate_retained_markdown_binding(
        manifest, root, {source.relative_to(ROOT.resolve()).as_posix(): sha256_file(source) for source, _ in paths},
        errors, repository_root=ROOT,
        check_derived=check_derived,
    )
    commit = record.metadata.get("versioning", {}).get("snapshot_commit")
    if not dated_html and not wiki_html and manifest.get("revision") != f"git:{commit}":
        errors.append("retained snapshot commit differs from canonical metadata")
    if errors:
        raise ValueError("; ".join(errors))
    package = (record.metadata.get("rights") or {}).get("redistribution_package")
    if package and package.get("source_revision") != manifest.get("revision"):
        raise ValueError("redistribution package does not cover the retained snapshot revision")
    rewrites = materialization.get("link_rewrites", {})
    if not isinstance(rewrites, dict):
        raise ValueError("retained link_rewrites must be an explicit href mapping")
    def check_original(path: Path, *, require_commit: bool = False) -> None:
        path.relative_to(root.resolve())
        if not path.is_file():
            raise ValueError("retained href rewrite target or image is not a local original")
        actual_hash = sha256_file(path)
        inventory = [item for item in manifest.get("local_files", []) if item.get("path") == path.relative_to(ROOT.resolve()).as_posix()]
        retrievals = [item for item in manifest.get("retrievals", []) if item.get("local_path") == path.relative_to(root.resolve()).as_posix()]
        if len(inventory) != 1 or inventory[0].get("sha256") != actual_hash or inventory[0].get("bytes") != path.stat().st_size or len(retrievals) != 1 or retrievals[0].get("sha256") != actual_hash or retrievals[0].get("bytes") != path.stat().st_size or require_commit and retrievals[0].get("commit") != commit:
            raise ValueError("retained href rewrite original differs from inventory or retrieval")

    for target in rewrites.values():
        if not isinstance(target, str):
            raise ValueError("retained link_rewrites must map local hrefs")
        parsed = urllib.parse.urlsplit(target)
        if parsed.path:
            path = (document.parent / urllib.parse.unquote(parsed.path)).resolve()
            check_original(path, require_commit=git_sidecar)
            if parsed.fragment.startswith("L"):
                match = re.fullmatch(r"L([1-9]\d*)-L([1-9]\d*)", parsed.fragment)
                if not match or not int(match.group(1)) <= int(match.group(2)) <= len(path.read_bytes().decode("utf-8").splitlines()):
                    raise ValueError("retained href rewrite source line range is invalid")
    options: dict[Path, dict[str, Any]] = {}
    if git_sidecar:
        options = {source: {"git_snapshot": True, **({"role": item["role"]} if "role" in item else {})} for item, (source, _) in zip(sources, paths)}
        if any("docfx_includes" in item for item in sources):
            for item, (source, _) in zip(sources, paths):
                retrieval = next(row for row in manifest["retrievals"] if row.get("local_path") == item["source"])
                options[source].update({"snapshot_commit": commit, "source_url": retrieval.get("resolved_url") or retrieval.get("requested_url") or ""})
                if "docfx_includes" in item:
                    options[source]["docfx_includes"] = item["docfx_includes"]
    if dated_html:
        options[paths[0][0]] = preflight_dated_html_assets(manifest, root, repository_root=ROOT.resolve())
    if wiki_html:
        options = preflight_wiki_html_sources(manifest, root, record.metadata, load_yaml(root / "source-metadata.yaml"), repository_root=ROOT.resolve(), actual_hashes={source.relative_to(ROOT.resolve()).as_posix(): sha256_file(source) for source, _ in paths})
    for item, (source, format_name) in zip(sources, paths):
        if format_name != "html" or dated_html or wiki_html:
            continue
        from bs4 import BeautifulSoup
        retrieval = next(row for row in manifest["retrievals"] if row.get("local_path") == item["source"])
        options.setdefault(source, {}).update({"source_url": retrieval.get("document_url") or retrieval.get("resolved_url") or retrieval.get("requested_url") or ""})
        if "config_range" in item:
            options[source]["config_range"] = item["config_range"]
        soup = BeautifulSoup(source.read_bytes(), "html.parser")
        for image in (soup.body or soup).find_all("img"):
            src = image.get("src", "")
            parsed = urllib.parse.urlsplit(src)
            if parsed.scheme or parsed.netloc:
                if src in rewrites:
                    check_original((document.parent / urllib.parse.unquote(urllib.parse.urlsplit(rewrites[src]).path)).resolve(), require_commit=True)
                continue  # External images stay external unless explicitly routed above.
            if not parsed.path:
                raise ValueError("retained HTML image has no local src path")
            asset = (source.parent / urllib.parse.unquote(parsed.path)).resolve()
            check_original(asset, require_commit=True)
            if src in rewrites and (document.parent / urllib.parse.unquote(urllib.parse.urlsplit(rewrites[src]).path)).resolve() != asset:
                raise ValueError("retained HTML src rewrite does not resolve to the same original")
    if paired_sidecar and "selectors.jsonl" in manifest["selectors"]:
        legacy_count = sum(bool(line.strip()) for line in (root / "selectors.jsonl").read_bytes().decode("utf-8").splitlines())
    else:
        legacy_count = 0
    selectors = derive_retained_text_sources(paths, document, rewrites, source_options=options)
    write_jsonl(selector_path, selectors)
    manifest.update({"generated_at": generated_at, "selectors": manifest["selectors"] if paired_sidecar else ["selectors.jsonl"]})
    materialization.update({
        "normalized_document": materialization["document"],
        "stored_characters": len(document.read_bytes().decode("utf-8")), "selector_count": legacy_count + len(selectors),
    })
    return finalize_capsule(record, root, manifest)


def replay_retained_markdown(
    record: SourceRecord, manifest: dict[str, Any], generated_at: str,
) -> dict[str, Any]:
    """Replay an explicitly fixed snapshot without fetching or clearing originals."""
    root = record.capsule_root
    try:
        identity = {
            "uid": record.uid, "source_type": record.source_type,
            "canonical_id": record.canonical_id, "canonical_url": record.canonical_url,
            "title": record.title, "metadata_path": record.relative_metadata_path,
        }
        if any(manifest.get(field) != value for field, value in identity.items()):
            raise ValueError("retained snapshot canonical identity differs from metadata")
        source_metadata = load_yaml(root / "source-metadata.yaml")
        version = (record.metadata.get("versioning") or {}).get("source_version")
        if (
            not isinstance(source_metadata, dict) or not isinstance(version, str) or not version.strip()
            or manifest.get("source_version") != version
            or (source_metadata.get("versioning") or {}).get("source_version") != version
            or any(source_metadata.get(field) != record.metadata.get(field) for field in (
                "uid", "title", "url", "canonical_url", "canonical_id",
            ))
        ):
            raise ValueError("retained snapshot source metadata or selected version differs")
        materialization = manifest["materialization"]
        if not isinstance(materialization, dict):
            raise TypeError("retained materialization must be a mapping")
        if "retained_text_binding" in materialization and "retained_text_sources" not in materialization:
            raise ValueError("retained text binding has no original declaration")
        if "retained_text_sources" in materialization:
            return replay_retained_text_sources(record, manifest, generated_at)
        paths: dict[str, Path] = {}
        for field, prefix in (("retained_markdown_source", "source"), ("document", "normalized")):
            relative_path = sanitize_relative_path(materialization[field])
            if relative_path is None or relative_path.parts[0] != prefix:
                raise ValueError(f"retained {field} must be a capsule-local {prefix} path")
            paths[field] = (root / relative_path).resolve()
            paths[field].relative_to(root.resolve())
        source, document = paths["retained_markdown_source"], paths["document"]
        from validate_materialization_completeness import validate_retained_markdown_binding
        binding_errors: list[str] = []
        validate_retained_markdown_binding(
            manifest, root, {source.relative_to(ROOT.resolve()).as_posix(): sha256_file(source)},
            binding_errors, repository_root=ROOT,
        )
        if binding_errors:
            raise ValueError("; ".join(binding_errors))
        rewrites = materialization.get("asset_rewrites", {})
        if not isinstance(rewrites, dict):
            raise ValueError("retained asset_rewrites must be an explicit path mapping")
        for old, new in rewrites.items():
            if not isinstance(old, str) or not isinstance(new, str):
                raise ValueError("retained asset_rewrites must map local paths")
            asset = (source.parent / old).resolve()
            asset.relative_to(root.resolve())
            if not asset.is_file() or asset != (document.parent / new).resolve():
                raise ValueError("retained asset rewrite must resolve to the same local original")
        package = (record.metadata.get("rights") or {}).get("redistribution_package")
        if package and package.get("source_revision") != manifest.get("revision"):
            raise ValueError("redistribution package does not cover the retained snapshot revision")
        selectors = derive_retained_markdown(source, document, rewrites)
        write_jsonl(root / "selectors.jsonl", selectors)
        manifest["generated_at"] = generated_at
        manifest["selectors"] = ["selectors.jsonl"]
        materialization.update({
            "normalized_document": materialization["document"],
            "stored_characters": len(document.read_bytes().decode("utf-8")),
            "selector_count": len(selectors),
        })
        return finalize_capsule(record, root, manifest)
    except (KeyError, TypeError, AttributeError, ValueError, OSError, yaml.YAMLError) as exc:
        raise RetainedMarkdownPreflightError(f"{record.uid}: {exc}; retained originals preserved") from exc


def materialize_generic(
    record: SourceRecord,
    config: dict[str, Any],
    generated_at: str,
    *,
    existing_root: Path | None = None,
    existing_manifest: dict[str, Any] | None = None,
    force_excerpt_reason: str | None = None,
) -> dict[str, Any]:
    metadata = record.metadata
    versioning = metadata.get("versioning") if isinstance(metadata, dict) else None
    publisher_declared = record.source_type == "journal" and isinstance(versioning, dict) and "publisher_pdf" in versioning
    retained = existing_manifest
    try:
        if existing_root is None and (record.capsule_root / "manifest.yaml").is_file():
            retained = load_yaml(record.capsule_root / "manifest.yaml")
        try:
            original_requested = original_retention_requested(
                retained if isinstance(retained, dict) else {}, record.capsule_root,
                repository_root=ROOT, metadata=record.metadata,
            )
        except Exception as exc:
            raise RedistributionPackageError(f"{record.uid}: original retention declaration inspection failed: {exc}; retained capsule preserved") from exc
        if original_requested:
            if existing_root is not None or not isinstance(retained, dict):
                raise RedistributionPackageError(f"{record.uid}: original retention needs its existing manifest; retained capsule preserved")
            return replay_original_retention(record, retained)
        if record.source_type == "journal" and (
            not isinstance(metadata, dict) or (versioning is not None and not isinstance(versioning, dict))
        ):
            raise TypeError("journal versioning must be a mapping or null")
        if existing_root is None:
            if isinstance(retained, dict) and "pdf_supplement" in retained:
                return replay_pdf_supplement(record, retained)
            if (record.capsule_root / "pdf-supplement").exists() or publisher_declared:
                raise ValueError("retained PDF supplement is undeclared")
    except Exception as exc:
        if isinstance(exc, RedistributionPackageError):
            raise
        try:
            original_requested = original_retention_requested(
                retained if isinstance(retained, dict) else {}, record.capsule_root,
                repository_root=ROOT, metadata=record.metadata,
            )
        except Exception as inspection_exc:
            raise RedistributionPackageError(f"{record.uid}: original retention declaration inspection failed: {inspection_exc}; retained capsule preserved") from exc
        if original_requested:
            raise RedistributionPackageError(f"{record.uid}: original retention manifest/preflight failed: {exc}; retained capsule preserved") from exc
        if (
            (record.capsule_root / "pdf-supplement").exists() or publisher_declared
            or (isinstance(retained, dict) and "pdf_supplement" in retained)
        ):
            raise RedistributionPackageError(f"{record.uid}: PDF replay preflight failed: {exc}; retained capsule preserved") from exc
        if (record.capsule_root / "source/specification.html").exists() or (record.capsule_root / "normalized/selectors.jsonl").exists():
            raise RetainedMarkdownPreflightError(f"{record.uid}: retained HTML preflight failed: {exc}; retained originals preserved") from exc
        raise
    if existing_root is None:
        retained_materialization = retained.get("materialization") if isinstance(retained, dict) else None
        sidecar_declared = isinstance(retained, dict) and isinstance(retained.get("selectors"), list) and "normalized/selectors.jsonl" in retained["selectors"]
        if sidecar_declared or isinstance(retained_materialization, dict) and any(field in retained_materialization for field in ("retained_markdown_source", "retained_text_sources", "retained_text_binding", "retained_text_selectors")):
            return replay_retained_markdown(record, retained, generated_at)
        if (record.capsule_root / "source/specification.html").exists() or (record.capsule_root / "normalized/selectors.jsonl").exists():
            raise RetainedMarkdownPreflightError(f"{record.uid}: retained HTML original has no replay declaration; retained originals preserved")
    if publisher_declared:
        raise RedistributionPackageError(f"{record.uid}: declared publisher PDF has no offline replay manifest; retained capsule preserved")
    root = existing_root or prepare_capsule(record)
    manifest = existing_manifest or base_manifest(record, "generic_web_or_document_v2", generated_at)
    if existing_root is None:
        # prepare_capsule already wrote this; retained for clarity.
        pass
    urls = candidate_urls(record)
    if not urls:
        manifest["errors"].append("no retrievable URL in metadata")
        return finalize_capsule(record, root, manifest)

    payload: bytes | None = None
    resolved_url: str | None = None
    headers: dict[str, str] = {}
    requested_url: str | None = None
    for url in urls[: int(config.get("generic_max_candidate_urls", 4))]:
        try:
            payload, resolved_url, headers = fetch_bytes(
                url,
                timeout=int(config.get("http_timeout_seconds", 45)),
                max_bytes=int(config.get("generic_max_download_bytes", 30_000_000)),
            )
            requested_url = url
            break
        except Exception as exc:
            manifest["warnings"].append(str(exc))
    if payload is None or resolved_url is None:
        manifest["errors"].append("all candidate URLs failed")
        return finalize_capsule(record, root, manifest)

    content_hash = sha256_bytes(payload)
    content_type = headers.get("content-type", "").lower()
    full_text_allowed = text_is_open(record, config, resolved_url)
    manifest["revision"] = f"sha256:{content_hash}"
    manifest["retrievals"].append(
        {
            "requested_url": requested_url,
            "resolved_url": resolved_url,
            "content_type": content_type,
            "bytes": len(payload),
            "sha256": content_hash,
        }
    )
    manifest["rights"]["full_text_redistribution_assumed"] = full_text_allowed

    selectors: list[dict[str, Any]] = []
    document_text = ""
    document_name = "document.md"
    page_count: int | None = None
    is_pdf = payload.startswith(b"%PDF") or "application/pdf" in content_type or resolved_url.lower().split("?", 1)[0].endswith(".pdf")
    try:
        if is_pdf:
            max_pages = None if full_text_allowed else int(config.get("restricted_pdf_excerpt_pages", 3))
            document_text, selectors, page_count = extract_pdf_text(payload, max_pages=max_pages)
            pdf_hash_prefix = content_hash[:16]
            for selector in selectors:
                selector["selector"] = selector["selector"].replace("sha256-PENDING", f"sha256-{pdf_hash_prefix}")
            document_name = "document.txt"
        elif "html" in content_type or payload.lstrip().startswith((b"<!DOCTYPE html", b"<html", b"<HTML")):
            document_text, selectors, detected_title = html_to_sections(payload, resolved_url)
            if detected_title:
                manifest["detected_title"] = detected_title
        else:
            document_text = payload.decode("utf-8", errors="replace")
            lines = document_text.splitlines()
            selectors = [
                {
                    "selector": f"text://sha256-{content_hash[:16]}#L1-L{max(1, len(lines))}",
                    "kind": "file",
                    "start_line": 1,
                    "end_line": max(1, len(lines)),
                    "text_preview": document_text[:240],
                }
            ]
            document_name = "document.txt"
    except Exception as exc:
        manifest["errors"].append(f"content parsing failed: {exc}")
        return finalize_capsule(record, root, manifest)

    content_was_truncated = False
    if not full_text_allowed or force_excerpt_reason:
        max_chars = int(config.get("restricted_excerpt_chars", 8_000))
        if len(document_text) > max_chars:
            content_was_truncated = True
            document_text = document_text[:max_chars].rstrip() + "\n"
        if force_excerpt_reason:
            manifest["warnings"].append(force_excerpt_reason)
        else:
            manifest["warnings"].append(
                "Full-text redistribution was not established; stored content is a bounded evidence excerpt."
            )
    else:
        max_chars = int(config.get("open_full_text_max_chars", 1_500_000))
        if len(document_text) > max_chars:
            content_was_truncated = True
            document_text = document_text[:max_chars].rstrip() + "\n"
            manifest["warnings"].append("Open text exceeded the configured local character budget and was truncated.")

    selectors, omitted_selector_count = filter_selectors_for_document(selectors, document_text)
    if omitted_selector_count:
        manifest["warnings"].append(
            f"Omitted {omitted_selector_count} selectors whose evidence was outside the stored document boundary."
        )

    if document_text.strip():
        (root / document_name).write_text(document_text, encoding="utf-8")
        substantive_text = has_substantive_document_text(document_text)
        if substantive_text and selectors:
            local_path = (root / document_name).relative_to(ROOT).as_posix()
            for selector in selectors:
                selector["local_path"] = local_path
            write_jsonl(root / "selectors.jsonl", selectors)
            complete_full_text = (
                full_text_allowed and not content_was_truncated and not force_excerpt_reason
            )
            manifest["status"] = "materialized" if complete_full_text else "partial"
            manifest["content_tier"] = "full_text" if complete_full_text else "excerpt_capsule"
            manifest["selectors"] = ["selectors.jsonl"]
        else:
            selectors = []
            if not substantive_text:
                manifest["warnings"].append(
                    "Retrieved document contained no substantive non-heading text; retained only as acquisition evidence."
                )
            else:
                manifest["warnings"].append(
                    "Retrieved document had no selector that resolved inside the stored boundary; retained only as acquisition evidence."
                )
        manifest["materialization"] = {
            "document": document_name,
            "stored_characters": len(document_text),
            "selector_count": len(selectors),
            "pdf_page_count": page_count,
            "full_text_allowed": full_text_allowed,
            "content_was_truncated": content_was_truncated,
            "substantive_text": substantive_text,
            "omitted_selector_count": omitted_selector_count,
            "forced_excerpt_reason": force_excerpt_reason,
        }
    return finalize_capsule(record, root, manifest)


def adapter_name(source_type: str) -> str:
    if source_type == "arxiv":
        return "arxiv_latex_v2"
    if source_type == "github":
        return "github_repo_semantic_capsule_v2"
    return "generic_web_or_document_v2"


def evidence_role_for(status: Any, content_tier: Any) -> str:
    if status in {"metadata_only", "failed"} or content_tier == "metadata_capsule":
        return "catalog-only"
    if status == "partial" or content_tier == "excerpt_capsule":
        return "bounded-excerpt"
    if content_tier == "semantic_capsule":
        return "static-repository-evidence"
    return "source-text"


def materialize_one(record: SourceRecord, config: dict[str, Any], generated_at: str) -> dict[str, Any]:
    try:
        if record.source_type == "arxiv":
            with _arxiv_semaphore:
                time.sleep(0.25)
                return materialize_arxiv(record, config, generated_at)
        if record.source_type == "github":
            with _github_semaphore:
                return materialize_github(record, config, generated_at)
        with _generic_semaphore:
            return materialize_generic(record, config, generated_at)
    except (RedistributionPackageError, ArxivPreflightError, RetainedMarkdownPreflightError):
        raise
    except Exception as exc:
        root = record.capsule_root
        if record.source_type == "arxiv" and root.exists():
            raise
        if not root.exists():
            root = prepare_capsule(record)
        manifest = base_manifest(record, adapter_name(record.source_type), generated_at)
        manifest["status"] = "metadata_only"
        manifest["errors"].append(f"unhandled adapter failure: {type(exc).__name__}: {exc}")
        return finalize_capsule(record, root, manifest)


def rebuild_registry(records: list[SourceRecord], manifests: dict[str, dict[str, Any]], generated_at: str) -> None:
    entries: list[dict[str, Any]] = []
    for record in records:
        manifest = manifests[record.uid]
        manifest_path = record.capsule_root / "manifest.yaml"
        entries.append(
            {
                "uid": record.uid,
                "source_type": record.source_type,
                "canonical_id": record.canonical_id,
                "title": record.title,
                "canonical_url": record.canonical_url,
                "metadata_path": record.relative_metadata_path,
                "verification_state": (
                    record.metadata.get("verification", {}).get("state")
                    if isinstance(record.metadata.get("verification"), dict)
                    else "pending"
                ),
                "priority": record.priority,
                "adapter": {
                    "name": manifest.get("adapter"),
                    "semanticization_required": record.source_type == "github",
                },
                "materialization": {
                    "state": manifest.get("status"),
                    "content_tier": manifest.get("content_tier"),
                    "evidence_role": evidence_role_for(
                        manifest.get("status"), manifest.get("content_tier")
                    ),
                    "revision": manifest.get("revision"),
                    "root": record.capsule_root.relative_to(ROOT).as_posix(),
                    "manifest": manifest_path.relative_to(ROOT).as_posix(),
                    "local_bytes": manifest.get("local_bytes", 0),
                },
            }
        )
    entries.sort(key=lambda item: (str(item["source_type"]), str(item["uid"])))
    REGISTRY_ROOT.mkdir(parents=True, exist_ok=True)
    write_yaml(
        REGISTRY_ROOT / "registry.yaml",
        {
            "registry_version": 2,
            "generated_at": generated_at,
            "repository": "thsno02/solid-octo-couscous",
            "entry_count": len(entries),
            "entries": entries,
        },
    )
    write_jsonl(REGISTRY_ROOT / "registry.jsonl", entries)
    (REGISTRY_ROOT / "README.md").write_text(
        "# 来源注册表（Source Registry）\n\n"
        "每条已收集的 metadata record 都在 `materialized_sources/corpus/` 下对应一个本地胶囊。"
        "注册表明确区分全文（full text）、repository 语义胶囊（semantic capsule）、"
        "有边界的摘录（bounded excerpt）和仅 metadata 的胶囊。\n",
        encoding="utf-8",
    )


def write_indexes_and_audit(records: list[SourceRecord], manifests: dict[str, dict[str, Any]], generated_at: str) -> None:
    items: list[dict[str, Any]] = []
    by_type: dict[str, Counter[str]] = defaultdict(Counter)
    statuses: Counter[str] = Counter()
    tiers: Counter[str] = Counter()
    metadata_only: list[dict[str, Any]] = []
    partial: list[dict[str, Any]] = []
    total_bytes = 0
    total_hashes = 0
    for record in records:
        manifest = manifests[record.uid]
        status = str(manifest.get("status") or "unknown")
        tier = str(manifest.get("content_tier") or "unknown")
        statuses[status] += 1
        tiers[tier] += 1
        by_type[record.source_type][tier] += 1
        total_bytes += int(manifest.get("local_bytes") or 0)
        total_hashes += len(manifest.get("local_files") or [])
        item = {
            "uid": record.uid,
            "source_type": record.source_type,
            "canonical_id": record.canonical_id,
            "title": record.title,
            "status": status,
            "content_tier": tier,
            "manifest": (record.capsule_root / "manifest.yaml").relative_to(ROOT).as_posix(),
            "revision": manifest.get("revision"),
            "local_bytes": manifest.get("local_bytes", 0),
        }
        items.append(item)
        if tier == "metadata_capsule":
            metadata_only.append(item)
        elif status == "partial":
            partial.append(item)
    items.sort(key=lambda item: (str(item["source_type"]), str(item["uid"])))
    full_or_semantic = tiers["full_text"] + tiers["semantic_capsule"]
    locally_usable = full_or_semantic + tiers["excerpt_capsule"]
    total = len(records)
    index = {
        "materialization_index_version": 2,
        "generated_at": generated_at,
        "corpus_root": "materialized_sources/corpus",
        "summary": {
            "records": total,
            "statuses": dict(statuses),
            "content_tiers": dict(tiers),
            "all_records_have_local_capsules": len(items) == total,
            "full_or_semantic_count": full_or_semantic,
            "locally_usable_count": locally_usable,
            "local_bytes": total_bytes,
            "hashed_files": total_hashes,
        },
        "items": items,
    }
    write_yaml(MATERIALIZED_ROOT / "index.yaml", index)
    (MATERIALIZED_ROOT / "README.md").write_text(
        "# 物化来源语料（Materialized Source Corpus）\n\n"
        "`corpus/` 为每条 metadata record 保存一个本地胶囊（local capsule）。"
        "内容层级（content tier）包括：\n\n"
        "- `full_text`：技术上已取得本地全文；该层级本身不证明具备公开再分发许可；\n"
        "- `semantic_capsule`：GitHub repository 已固定到具体 commit，并根据选定证据生成语义胶囊；\n"
        "- `excerpt_capsule`：未确认再分发权利时，只保存有边界的本地摘录；\n"
        "- `metadata_capsule`：仅允许元数据消费；也可能保留抓取失败的标题等诊断性文件，不能作为正文证据。\n\n"
        "本地胶囊不自动等于可信知识（trusted knowledge）。\n\n"
        "公开存储另受[版权与许可审计](../docs/materialization-rights-audit.md)约束。"
        "`full_text_redistribution_assumed` 是历史获取器的假设，不是许可凭据；"
        "Git LFS 或公开 release artifact 也不消除再分发义务。摘录有长度边界也不自动代表具备公开再分发权。\n\n"
        "离线修复和定位器抽检结果见 `raw_data/audits/`。注册表的 `evidence_role` 将仅目录导航（catalog-only）、"
        "有限摘录（bounded-excerpt）、仓库静态证据（static-repository-evidence）与原文（source-text）分开。\n",
        encoding="utf-8",
    )
    audit = {
        "audit_id": "materialization-completeness-2026-09-10",
        "generated_at": generated_at,
        "repository": "thsno02/solid-octo-couscous",
        "collection_records": total,
        "local_capsules": len(items),
        "all_records_local": len(items) == total,
        "status_counts": dict(statuses),
        "content_tier_counts": dict(tiers),
        "by_source_type": {key: dict(value) for key, value in sorted(by_type.items())},
        "full_or_semantic_coverage": round(full_or_semantic / total, 4) if total else 0,
        "locally_usable_coverage": round(locally_usable / total, 4) if total else 0,
        "metadata_only_count": len(metadata_only),
        "partial_count": len(partial),
        "metadata_only_items": metadata_only,
        "partial_items": partial,
        "local_bytes": total_bytes,
        "hashed_files": total_hashes,
        "interpretation": (
            "Every record having a local capsule does not mean every copyrighted or inaccessible source is mirrored in full. "
            "The content tier records the actual consumability boundary."
        ),
        "acceptance": {
            "all_metadata_records_have_local_manifest": len(items) == total,
            "no_unclassified_missing_capsule": len(items) == total,
            "full_content_gaps_are_explicit": True,
        },
    }
    AUDIT_ROOT.mkdir(parents=True, exist_ok=True)
    write_yaml(AUDIT_ROOT / "materialization_completeness_2026-09-10.yaml", audit)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="pipeline/materialization_all_260910.yaml")
    parser.add_argument("--workers", type=int, default=None)
    parser.add_argument(
        "--only-source-type",
        choices=sorted(set(DIRECTORY_SOURCE_TYPES.values())),
        help="Rebuild one source family and reuse existing capsules for all other records.",
    )
    args = parser.parse_args()

    config = load_yaml(ROOT / args.config)
    if not isinstance(config, dict):
        raise SystemExit("materialization config must be a YAML object")
    generated_at = str(config.get("generated_at") or utc_now())
    records = discover_records()
    if not records:
        raise SystemExit("no metadata records found")

    selected_records = (
        [record for record in records if record.source_type == args.only_source_type]
        if args.only_source_type
        else records
    )
    if not selected_records:
        raise SystemExit(f"no metadata records found for source type {args.only_source_type}")

    CORPUS_ROOT.mkdir(parents=True, exist_ok=True)
    workers = int(args.workers or config.get("workers", 12))
    manifests: dict[str, dict[str, Any]] = {}
    if args.only_source_type:
        for record in records:
            if record in selected_records:
                continue
            manifest_path = record.capsule_root / "manifest.yaml"
            if not manifest_path.exists():
                raise SystemExit(
                    f"cannot run an incremental rebuild; existing capsule is missing for {record.uid}"
                )
            manifest = load_yaml(manifest_path)
            if not isinstance(manifest, dict):
                raise SystemExit(f"existing manifest is invalid for {record.uid}")
            manifests[record.uid] = manifest
    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, workers)) as pool:
        future_map = {
            pool.submit(materialize_one, record, config, generated_at): record
            for record in selected_records
        }
        for future in concurrent.futures.as_completed(future_map):
            record = future_map[future]
            try:
                manifest = future.result()
            except (RedistributionPackageError, ArxivPreflightError, RetainedMarkdownPreflightError):
                raise
            except Exception as exc:
                if record.source_type == "arxiv" and record.capsule_root.exists():
                    raise
                root = prepare_capsule(record)
                manifest = base_manifest(record, adapter_name(record.source_type), generated_at)
                manifest["errors"].append(f"executor failure: {type(exc).__name__}: {exc}")
                manifest = finalize_capsule(record, root, manifest)
            manifests[record.uid] = manifest
            print(
                f"materialized uid={record.uid} type={record.source_type} "
                f"status={manifest.get('status')} tier={manifest.get('content_tier')}",
                flush=True,
            )

    rebuild_registry(records, manifests, generated_at)
    write_indexes_and_audit(records, manifests, generated_at)
    total = len(records)
    local = sum((record.capsule_root / "manifest.yaml").exists() for record in records)
    print(f"materialization_complete records={total} local_capsules={local}")
    return 0 if local == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
