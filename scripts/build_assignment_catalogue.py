#!/usr/bin/env python3
"""Preserve later-course module assignments as structured source metadata."""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSES = json.loads((ROOT / "data/course.json").read_text())["courses"]
MODULE = re.compile(r"^\*\*(\d+)\. (.*?), (\d+) hours\.\*\* (.*)$", re.M)


def build():
    records = []
    for course in COURSES:
        id_ = course["id"]
        if id_ == "C01":
            continue
        page = course["page"]
        source = (ROOT / page).read_text()
        matches = list(MODULE.finditer(source))
        if matches:
            if sum(int(m.group(3)) for m in matches) != course["baseline_hours"]:
                raise ValueError(f"module hours do not equal baseline: {id_}")
            if [int(m.group(1)) for m in matches] != list(range(1, len(matches) + 1)):
                raise ValueError(f"nonsequential modules: {id_}")
            for m in matches:
                records.append({
                    "id": f"{id_}-M{int(m.group(1)):02d}",
                    "course_id": id_, "source_page": page, "source_line": source[:m.start()].count("\n") + 1,
                    "kind": "source_module_assignment", "title": m.group(2),
                    "source_baseline_hours": int(m.group(3)), "source_text": m.group(4),
                    "readiness": "curriculum-specification-not-packet",
                })
        elif id_ in {"C13A", "C13B", "C13C"}:
            lines = source.splitlines()
            prompt = next(((n, line) for n, line in enumerate(lines, 1) if line.startswith("Default paper prompt:")), None)
            if prompt is None:
                raise ValueError(f"missing seminar prompt: {id_}")
            records.append({
                "id": f"{id_}-PAPER", "course_id": id_, "source_page": page,
                "source_line": prompt[0], "kind": "source_course_prompt",
                "title": "Default and alternative paper prompts", "source_baseline_hours": None,
                "source_text": prompt[1], "readiness": "curriculum-specification-not-packet",
            })
        else:
            raise ValueError(f"no extractable assignment metadata: {id_}")
    return {
        "schema_version": 1,
        "purpose": "Verbatim assignment metadata from current later-course pages; source-baseline allocations, not released lesson packets or verified reading assets",
        "records": records,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    path = ROOT / "data/assignment-catalogue.json"
    content = json.dumps(build(), ensure_ascii=False, indent=2) + "\n"
    if args.check:
        if not path.exists() or path.read_text() != content:
            raise SystemExit("Stale assignment catalogue")
    else:
        path.write_text(content)
        print(f"{len(build()['records'])} source assignments -> {path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
