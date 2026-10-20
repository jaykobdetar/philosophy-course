#!/usr/bin/env python3
"""Read-only structural checks for the Course 9 authoring handoff."""
import hashlib
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]


def main():
    data = json.loads((HERE / "authoring.json").read_text())
    assert data["course_number"] == 9
    track, = data["tracks"]
    assert track["id"] == "C09"
    source = (ROOT / track["curriculum_page"]).read_text()
    baseline = [int(h) for h in re.findall(r"^\*\*\d+\. .*?, (\d+) hours\.\*\*", source, re.M)]
    assert baseline == [12, 18, 26, 12, 18, 22, 24, 8]
    assert [m["hours"] for m in track["modules"]] == baseline
    assert sum(baseline) == track["baseline_hours"] == 140
    for n, module in enumerate(track["modules"], 1):
        assert module["id"] == f"C09-M{n:02d}"
        body = (ROOT / module["path"]).read_text()
        assert f"C09-M{n:02d}" in body
        assert sum(module["budget_minutes"].values()) == module["hours"] * 60
        for marker in ["Guiding question", "Prerequisites", "Outcomes", "Independent task", "Repair"]:
            assert marker in body, (module["path"], marker)
    for key in ["readme", "outcomes", "assessment", "examiner", "source_audit"]:
        assert (ROOT / track[key]).is_file(), key
    assert track["assessment"] != track["examiner"]
    for addition in data["additions"]:
        for key in ["id", "pc_task", "path", "hours", "replaces_hours", "net_hours", "applies_to", "credit_rule"]:
            assert key in addition
        assert addition["hours"] - addition["replaces_hours"] == addition["net_hours"]
        assert (ROOT / addition["path"]).is_file()
    assert sum(a["net_hours"] for a in data["additions"]) == 0
    checked_links = 0
    markdown = list(HERE.rglob("*.md"))
    for path in markdown:
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            if target.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = target.split("#", 1)[0]
            assert (path.parent / target).resolve().is_file(), (path.relative_to(ROOT), target)
            checked_links += 1
    for path, digest in data["source_sha256"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest, f"Source changed: {path}"
    for form, ids in {
        "fresh-a.md": ["A-K", "A-S", "A-G"],
        "fresh-b.md": ["B-K", "B-S", "B-G"],
        "delayed-a.md": ["DA-K", "DA-S", "DA-G"],
        "delayed-b.md": ["DB-K", "DB-S", "DB-G"],
    }.items():
        body = (HERE / "assessment-forms" / form).read_text()
        for id_ in ids:
            assert id_ in body and id_ in (HERE / "examiner-notes.md").read_text(), id_
    print(f"PASS: C09, 8 modules, 140 baseline hours, 0 net added hours; {checked_links} local Markdown links; {len(markdown)} Markdown files; source hashes unchanged.")
    print("PASS: budget minutes reconcile; fresh and delayed IDs have separate examiner anchors.")
    print("LIMIT: structural checks do not verify philosophical accuracy, source rights, rendering, runtime identity or learner outcomes.")


if __name__ == "__main__":
    main()
