#!/usr/bin/env python3
"""Carry named later-course reading assignments into a source-bound catalogue."""

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEEDS = ROOT / "data/later-reading-seeds.tsv"
OUT = ROOT / "data/later-reading-catalogue.json"
EXPECTED = {
    "C03": 10, "C04": 11, "C05": 7, "C06": 9, "C07": 11,
    "C08": 8, "C09": 7, "C10": 8, "C11A": 7, "C11B": 8,
    "C12A": 9, "C12B": 6, "C12C": 7, "C12D": 7,
    "C13A": 5, "C13B": 5, "C13C": 5,
}


def stable_id(prefix, *parts):
    value = "|".join(parts).encode()
    return prefix + hashlib.sha256(value).hexdigest()[:12].upper()


def build():
    rows = []
    works = {}
    editions = {}
    for line in SEEDS.read_text().splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split("|")
        if len(parts) != 6:
            raise ValueError(f"wrong seed field count: {line[:80]}")
        course, creator, work, locator, edition, anchor = parts
        if not all(parts) or course not in EXPECTED:
            raise ValueError(f"invalid seed: {line[:80]}")
        page = f"current/courses/{course[1:].lower()}.md"
        source = (ROOT / page).read_text()
        if anchor not in source:
            raise ValueError(f"source anchor absent: {course} {work}: {anchor}")
        work_id = stable_id("W-", creator, work)
        edition_id = stable_id("E-", creator, work, edition)
        work_record = {"id": work_id, "creator": creator, "title": work}
        edition_record = {"id": edition_id, "work_id": work_id, "description_as_specified": edition,
                          "source_match": "unchecked"}
        if work_id in works and works[work_id] != work_record:
            raise ValueError(f"work ID collision: {work_id}")
        if edition_id in editions and editions[edition_id] != edition_record:
            raise ValueError(f"edition ID collision: {edition_id}")
        works[work_id] = work_record
        editions[edition_id] = edition_record
        rows.append({
            "id": f"{course}-R{sum(r['course_id'] == course for r in rows) + 1:02d}",
            "course_id": course, "work_id": work_id,
            "edition_id": edition_id,
            "assigned_locator": locator, "source_page": page,
            "source_line": source[:source.index(anchor)].count("\n") + 1,
            "source_page_sha256": hashlib.sha256(source.encode()).hexdigest(),
            "source_anchor": anchor, "asset_id": None,
            "access": "unchecked", "rights": "unchecked",
            "readiness": "source-metadata-only",
        })
    counts = Counter(r["course_id"] for r in rows)
    if dict(counts) != EXPECTED:
        raise ValueError(f"reading count mismatch: {counts}")
    ids = [r["id"] for r in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate reading assignment ID")
    return {
        "schema_version": 1,
        "purpose": "Existing named reading assignments in Courses 3–13, not source-verified or released; Course 14 assigns project-specific sources rather than a fixed reading list",
        "advertised_counts": EXPECTED,
        "works": list(works.values()),
        "editions": list(editions.values()),
        "records": rows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    content = json.dumps(build(), ensure_ascii=False, indent=2) + "\n"
    if args.check:
        if not OUT.exists() or OUT.read_text() != content:
            raise SystemExit("Stale later reading catalogue")
    else:
        OUT.write_text(content)
        print(f"{len(build()['records'])} later reading assignments -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
