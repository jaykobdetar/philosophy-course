#!/usr/bin/env python3
"""Check that substantive DOCX-conversion blocks survive in current pages.

The untouched Pandoc conversion is the comparison source. Link destinations and
Markdown decoration are ignored; the three intentional textual amendments are
identified by exact source-block digest and checked against their current pages.
"""

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "archive/revised-curriculum-pandoc-baseline.md"
EXCEPTIONS = {
    "caa70c0622ad47ced2e90585d29e17191173a79c86f8a41c7d428f1e24a973e2": (
        "current/courses/01.md", "Session 1 — first encounter"
    ),
    "8c3f7ea12384ff583581568623217426b351e3f2f1a27fe437a74a9514eb4502": (
        "current/courses/01.md", "Session 2 — reasons"
    ),
    "b1d00afda73e93bb8bdfae2929410f1a89f551294bf29c44b5d4f8c8c0da0e28": (
        "current/courses/01.md", "Session 3 — validity"
    ),
    "f7e22b9d40e63e81cdce5a70cdf779d1efb021be9110f898fdc94eec2c11d1b9": (
        "current/courses/01.md", "Session 4 — example"
    ),
    "b987c2c1b2cd3d896be87f2ed49ddeca54179c8724bac4560d53407a10fd9535": (
        "current/courses/01.md", "sections 2.1–2.6 and 5.1–5.5"
    ),
    "1b0b80ca3db88e013751e0ff2ffba1e926d5c9dde3fe77ba142f548bae31c325": (
        "current/courses/01.md", "two-hour practical-reasoning packet"
    ),
    "bfba0e51b7a63bca7740c9ef49435ce59a6b48e91633f52c8cd4e19a9cd7452a": (
        "current/courses/03.md", "Patrick’s own translation of Book I"
    ),
    "c198276d781267d9870a2f68439e55853edd49cff7eaa4c15da48ee49e49c53a": (
        "current/access.md", "followed by her translation of Book I"
    ),
    "4a28fdce77c87b7b6efab754fa5266ba3ecfd6992a584cc60f764f01daece351": (
        "current/access.md", "later modules still need their own packet and readiness checks"
    ),
}
EXCEPTION_LINES = {
    "caa70c0622ad47ced2e90585d29e17191173a79c86f8a41c7d428f1e24a973e2",
    "8c3f7ea12384ff583581568623217426b351e3f2f1a27fe437a74a9514eb4502",
    "b1d00afda73e93bb8bdfae2929410f1a89f551294bf29c44b5d4f8c8c0da0e28",
    "f7e22b9d40e63e81cdce5a70cdf779d1efb021be9110f898fdc94eec2c11d1b9",
    "d96439aa3c462e82bc6aaf85a388b2b7d036ec2809900c03b83ae260791821bd",
    "1b0b80ca3db88e013751e0ff2ffba1e926d5c9dde3fe77ba142f548bae31c325",
    "bfba0e51b7a63bca7740c9ef49435ce59a6b48e91633f52c8cd4e19a9cd7452a",
    "c198276d781267d9870a2f68439e55853edd49cff7eaa4c15da48ee49e49c53a",
    "4a28fdce77c87b7b6efab754fa5266ba3ecfd6992a584cc60f764f01daece351",
}


def normalize(s):
    s = re.sub(r"\[([^]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[#*>|_`\\]", " ", s)
    return " ".join(s.split()).lower()


def audit():
    source = SOURCE.read_text()
    page_map = json.loads((ROOT / "archive/conversion-map.json").read_text())
    current = "\n".join((ROOT / "current" / name).read_text() for name in page_map["pages"])
    normalized_current = normalize(current)
    blocks = [b for b in re.split(r"\n\s*\n", source) if len(normalize(b)) >= 80]
    seen_exceptions = set()
    missing = []
    for block in blocks:
        if normalize(block) in normalized_current:
            continue
        digest = hashlib.sha256(block.encode()).hexdigest()
        if digest not in EXCEPTIONS:
            missing.append(digest)
            continue
        path, marker = EXCEPTIONS[digest]
        if marker not in (ROOT / path).read_text():
            missing.append(digest + " (replacement marker absent)")
        seen_exceptions.add(digest)
    if seen_exceptions != set(EXCEPTIONS):
        missing.extend("expected amendment absent: " + d for d in set(EXCEPTIONS) - seen_exceptions)
    long_lines = [line for line in source.splitlines() if len(normalize(line)) >= 80]
    seen_lines = set()
    for line in long_lines:
        if normalize(line) in normalized_current:
            continue
        digest = hashlib.sha256(line.encode()).hexdigest()
        if digest not in EXCEPTION_LINES:
            missing.append("source line absent: " + digest)
        seen_lines.add(digest)
    if seen_lines != EXCEPTION_LINES:
        missing.extend("expected amended line absent: " + d for d in EXCEPTION_LINES - seen_lines)
    if missing:
        raise ValueError(f"Conversion preservation failed for {len(missing)} blocks: {missing[:10]}")
    return len(blocks), len(seen_exceptions), len(long_lines), len(seen_lines)


if __name__ == "__main__":
    total, changed, lines, amended_lines = audit()
    print(f"Conversion audit passed: {total - changed}/{total} source blocks and {lines - amended_lines}/{lines} substantive lines exact after Markdown normalization; {changed} named amendments checked.")
