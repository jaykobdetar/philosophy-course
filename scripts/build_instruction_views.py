#!/usr/bin/env python3
"""Generate the teaching index from course manifests and review records."""

import argparse
import json
from pathlib import Path

from check_authoring import inspect

ROOT = Path(__file__).resolve().parents[1]


def outputs(partial=False):
    errors, tracks, additions = inspect(partial)
    if errors:
        raise ValueError("\n".join(errors))
    review_path = ROOT / "data/authoring-reviews.json"
    reviews = json.loads(review_path.read_text()) if review_path.exists() else {"course_reviews": []}
    review_by_course = {r["course_number"]: r for r in reviews["course_reviews"]}
    course_limits = []
    for number in sorted({int(t["id"][1:3]) for t in tracks}):
        manifest = json.loads((ROOT / f"instruction/course-{number:02d}/authoring.json").read_text())
        course_limits.append({"course_number": number, "limitations": manifest.get("limitations", [])})
    index = {
        "schema_version": 1,
        "authoring_date": "2026-10-20",
        "scope": "Teaching packets and source-access dependencies; no learner-pilot or expert-validation claim",
        "tracks": tracks,
        "additions": additions,
        "course_reviews": reviews["course_reviews"],
        "course_limitations": course_limits,
    }
    lines = [
        "# Philosophy teaching materials", "",
        "Use the course entry below for its reading assignments, explanations, exercises, independent assessments, and feedback. The [current curriculum](../current/README.md) preserves the accepted course scope. Source availability and exact-edition verification are stated in each course's source audit.", "",
        "The full authoring instruction of 20 October supersedes the earlier stop at the opening pilot. These materials have not been piloted with a real learner or certified by a human specialist. Source-dependent tasks require the stated reading; an explanation does not replace an unavailable primary text.", "",
        "| Track | Teaching entry | Modules | Source baseline hours | Review / access |",
        "| --- | --- | ---: | ---: | --- |",
    ]
    for t in tracks:
        number = int(t["id"][1:3])
        review = review_by_course.get(number)
        label = "AI content review recorded" if review and review.get("result") == "accepted after fixes" else "Content review pending"
        readme = "../" + t["readme"]
        audit = "../" + t["source_audit"]
        lines.append(f"| {t['id']} | [{t['title']}]({readme}) | {len(t['modules'])} | {t['baseline_hours']} | {label}; [source audit]({audit}) |")
    lines += [
        "", "## Study and feedback", "",
        "Use [tutor instructions](tutor.md) during practice and the course's separate examiner guidance only after saving an independent attempt. Record [assistance and evidence](learner-record.md), and use the [audio handoff](audio-handoff.md) when listening helps. Each course includes changed-case and delayed checks; public forms are not secure examinations.", "",
        "## Added encounters and shared credit", "",
        "The hours above are source baselines. Added packets and overlap credits are recorded separately; use [structured teaching records](../data/authoring-index.json) and the [workload ledger](../data/workload.json). Reuse an already demonstrated artifact only where the stated credit rule permits it.", "",
    ]
    for a in additions:
        lines.append(f"- [{a['id']}](../{a['path']}): {a['net_hours']} net planned hours; {a['credit_rule']}")
    lines += ["", "A source or edition mismatch blocks only the affected reading-dependent task. Preserve the question and access note, continue any independent ready work, and obtain the specified source through an authorized route before claiming that task complete.", ""]
    return {
        ROOT / "data/authoring-index.json": json.dumps(index, ensure_ascii=False, indent=2) + "\n",
        ROOT / "instruction/README.md": "\n".join(lines),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--partial", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for path, content in outputs(args.partial).items():
        if args.check:
            if not path.exists() or path.read_text() != content:
                raise SystemExit(f"stale instruction view: {path.relative_to(ROOT)}")
        else:
            path.write_text(content)
            print(path.relative_to(ROOT))


if __name__ == "__main__":
    main()
