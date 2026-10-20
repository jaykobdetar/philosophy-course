#!/usr/bin/env python3
"""Check complete teaching coverage against the preserved curriculum modules."""

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COURSES = json.loads((ROOT / "data/course.json").read_text())["courses"]
MODULE = re.compile(r"^\*\*(\d+)\. (.*?), (\d+) hours\.\*\*", re.M)


def inspect(partial=False):
    errors, tracks, additions = [], [], []
    for number in range(1, 15):
        path = ROOT / f"instruction/course-{number:02d}/authoring.json"
        if not path.exists():
            if not partial:
                errors.append(f"missing course authoring manifest: {number}")
            continue
        try:
            manifest = json.loads(path.read_text())
        except (ValueError, OSError) as exc:
            errors.append(f"invalid manifest {path.relative_to(ROOT)}: {exc}")
            continue
        expected = {c["id"]: c for c in COURSES if c["id"].startswith(f"C{number:02d}")}
        actual = manifest.get("tracks", [])
        if manifest.get("course_number") != number:
            errors.append(f"wrong course number: {path.relative_to(ROOT)}")
        if {t.get("id") for t in actual} != set(expected) or len(actual) != len(expected):
            errors.append(f"missing/duplicate/extra option tracks for Course {number}")
        for track in actual:
            id_ = track.get("id", "?")
            if id_ not in expected:
                continue
            spec = expected[id_]
            source_path = "current/courses/13.md" if number == 13 else spec["page"]
            expected_modules = [(int(n), int(h)) for n, _, h in MODULE.findall((ROOT / source_path).read_text())]
            modules = track.get("modules", [])
            if len(modules) != len(expected_modules):
                errors.append(f"{id_}: {len(modules)} modules, expected {len(expected_modules)}")
            if track.get("baseline_hours") != spec["baseline_hours"]:
                errors.append(f"{id_}: baseline hours differ from curriculum")
            if [m.get("hours") for m in modules] != [hours for _, hours in expected_modules]:
                errors.append(f"{id_}: module hour sequence differs from source")
            module_ids = [m.get("id") for m in modules]
            if len(set(module_ids)) != len(module_ids):
                errors.append(f"{id_}: duplicate module ID")
            module_paths = [m.get("path") for m in modules]
            if len(set(module_paths)) != len(module_paths):
                errors.append(f"{id_}: multiple source modules point to the same packet")
            for (module_number, _), item in zip(expected_modules, modules):
                allowed_ids = {f"{id_}-M{module_number:02d}"}
                if number == 13:
                    allowed_ids.add(f"C13-M{module_number:02d}")
                if item.get("id") not in allowed_ids:
                    errors.append(f"{id_}: module ID/sequence does not match source: {item.get('id')}")
            if track.get("assessment") == track.get("examiner"):
                errors.append(f"{id_}: learner assessment and examiner guidance share a file")
            refs = [(key, track.get(key)) for key in ("curriculum_page", "readme", "outcomes", "assessment", "examiner", "source_audit")]
            refs += [("module", m.get("path")) for m in modules]
            for kind, ref in refs:
                if not isinstance(ref, str):
                    errors.append(f"{id_}: missing {kind} path")
                    continue
                target = (ROOT / ref).resolve()
                if not target.is_relative_to(ROOT) or not target.is_file():
                    errors.append(f"{id_}: missing/unsafe {kind} path {ref}")
                elif not target.read_text().strip():
                    errors.append(f"{id_}: empty {kind} file {ref}")
            tracks.append(track)
        for addition in manifest.get("additions", []):
            required = ("id", "pc_task", "path", "hours", "replaces_hours", "net_hours", "applies_to", "credit_rule")
            if any(key not in addition for key in required):
                errors.append(f"Course {number}: addition lacks handoff fields: {addition.get('id')}")
                continue
            if addition["hours"] - addition["replaces_hours"] != addition["net_hours"]:
                errors.append(f"{addition['id']}: addition budget does not reconcile")
            if not (ROOT / addition["path"]).is_file():
                errors.append(f"{addition['id']}: missing addition packet")
            additions.append(addition)
    ids = [a["id"] for a in additions]
    if len(ids) != len(set(ids)):
        errors.append("addition IDs overlap between course owners")
    return errors, tracks, additions


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--partial", action="store_true", help="check existing course manifests during authoring")
    args = parser.parse_args()
    errors, tracks, additions = inspect(args.partial)
    if errors:
        raise SystemExit("Authoring coverage failed:\n- " + "\n- ".join(errors))
    unique_modules = {m["path"] for t in tracks for m in t["modules"]}
    print(f"Authoring coverage passed: {len(tracks)} tracks, {len(unique_modules)} distinct module packets, {len(additions)} additions. Source and learner validation remain separate.")


if __name__ == "__main__":
    main()
