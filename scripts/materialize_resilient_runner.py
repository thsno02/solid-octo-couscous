#!/usr/bin/env python3
"""Run the materializer with bounded network retries.

The core materializer remains deterministic. This runner changes only the
network failure budget so one unavailable source cannot consume the whole job.
"""
from __future__ import annotations
import importlib.util
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "scripts" / "materialize_pipeline.py"
SPEC = importlib.util.spec_from_file_location("materialize_pipeline", TARGET)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot load {TARGET}")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


def bounded_curl(url: str):
    request = urllib.request.Request(
        url,
        headers={"User-Agent": module.UA, "Accept": "*/*"},
    )
    last_error = None
    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=25) as response:
                return response.read(), response.geturl(), dict(response.headers)
        except Exception as exc:  # preserve concrete exception in the manifest
            last_error = exc
            if attempt == 0:
                time.sleep(2)
    raise RuntimeError(f"{url}: {last_error}")


module.curl = bounded_curl
raise SystemExit(module.main())
