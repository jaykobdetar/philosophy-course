#!/usr/bin/env python3
"""Render the small current-course navigation from data/course.json."""

import argparse
import hashlib
import html
import json
from pathlib import Path
from course_model import route_records

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data/course.json"


def load():
    data = json.loads(DATA.read_text())
    digest = hashlib.sha256(DATA.read_bytes()).hexdigest()[:12]
    return data, digest


def readiness(data, digest):
    editions = {item["id"]: item for item in data["editions"]}
    assets = {item["id"]: item for item in data["assets"]}
    lines = [
        "# Course 1 reading readiness",
        "",
        f"Generated from `data/course.json` ({digest}); run `python3 scripts/build_views.py` after changing readings.",
        "",
        "**Scope:** Opening four sessions and the Course 1 practical-reasoning packet. Later readings in the full course remain unverified here. `ready-online` requires internet access. An unmarked local copy is not a substitute for a marked locator.",
        "",
        "| Assignment | Edition and bounded reading | Route | Rights / quality | Readiness |",
        "| --- | --- | --- | --- | --- |",
    ]
    for a in data["assignments"]:
        if a["course_id"] != "C01":
            continue
        edition = editions[a["edition_id"]]
        asset = assets[a["asset_id"]]
        route = f"[Open online]({asset['url']})" if asset.get("url") else "Local/loan route pending"
        lines.append(
            f"| `{a['id']}` | {edition['description']}; {a['locator']} | {route} | {asset['rights']}; {asset['text_quality']} | {a['readiness']} |"
        )
    lines += [
        "",
        "If a link fails, obtain the same edition and exact passage through a legitimate library or publisher route, or pause that packet. Do not substitute a summary or silently widen the assigned range. Record the edition actually read.",
        "",
    ]
    return "\n".join(lines)


def navigation(data, digest):
    authored_path = ROOT / "data/authoring-index.json"
    authored = json.loads(authored_path.read_text()) if authored_path.exists() else {"tracks": []}
    packets = {t["id"]: t for t in authored["tracks"]}

    def course_link(c):
        page = ROOT / c["page"]
        heading = next(line[2:].strip() for line in page.read_text().splitlines() if line.startswith("# "))
        href = c["page"].removeprefix("current/")
        result = f'<a href="{html.escape(href, quote=True)}">{html.escape(heading)}</a> <span>({c["baseline_hours"]} baseline hours)</span>'
        if c["id"] in packets:
            packet = packets[c["id"]]
            result += f' — <a href="../{html.escape(packet["readme"], quote=True)}">Teaching materials for {c["id"]}</a> · <a href="../{html.escape(packet["source_audit"], quote=True)}">Source access and checks</a>'
        return result

    items = []
    for number in range(1, 15):
        options = [c for c in data["courses"] if c["id"].startswith(f"C{number:02d}")]
        if len(options) == 1:
            items.append(f'<li>{course_link(options[0])}</li>')
        else:
            choices = "".join(f'<li>{course_link(c)}</li>' for c in options)
            items.append(f'<li>Course {number}: select one option<ul>{choices}</ul></li>')
    reading = []
    for a in data["assignments"]:
        if a["session_id"] not in {"C01-S01", "C01-S02", "C01-S03", "C01-S04"}:
            continue
        asset = next(item for item in data["assets"] if item["id"] == a["asset_id"])
        edition = next(item for item in data["editions"] if item["id"] == a["edition_id"])
        work = next(item for item in data["works"] if item["id"] == edition["work_id"])
        reading.append(f'<li><code>{html.escape(a["id"])}</code> — <a href="{html.escape(asset["url"], quote=True)}">{html.escape(work["title"])}: {html.escape(a["locator"])}</a> (online)</li>')
    teaching_note = (
        f'{len(packets)} course and option tracks have authored teaching packets. Check each source audit before source-dependent work. Learner piloting, human expert validation and rendered accessibility checks remain pending.'
        if packets else
        'The opening four sessions are study-ready but not piloted. Later pages preserve the revised curriculum’s specification; full authoring progress is recorded separately.'
    )
    teaching_nav = '<a href="../instruction/README.md">All teaching materials</a> · ' if packets else ''
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Current philosophy course navigator</title>
<style>body{font:1.05rem/1.55 system-ui,sans-serif;max-width:76ch;margin:auto;padding:1.2rem;color:#17212b;background:#fff}a{color:#064e8a}a:focus-visible{outline:3px solid #e36b00;outline-offset:3px}.skip{position:absolute;left:-10000px}.skip:focus{left:1rem;top:1rem;background:white;padding:.5rem}nav,main,footer{display:block}li{margin:.45rem 0}aside{border-left:4px solid #667;padding:.4rem 1rem;background:#f3f5f7}@media print{body{max-width:none}.skip{display:none}a{color:#17212b}}</style>
</head><body><a class="skip" href="#main">Skip to course content</a><header><h1>Current philosophy course</h1><p>Version 2026-10-13-r0. Generated reading data: """ + digest + """.</p></header>
<nav aria-label="Primary"><a href="README.md">Current curriculum guide</a> · """ + teaching_nav + """<a href="../instruction/course-01/README.md">Course 1 teaching guide</a> · <a href="readiness/course-01.md">Opening reading readiness</a> · <a href="route-options.md">Direct route options</a></nav>
<main id="main"><h2>Begin</h2><p>Read OpenStax 2.5 and Plato’s <em>Euthyphro</em> 2a to before 5d, then write a 120-word paraphrase. <a href="../instruction/course-01/sessions/01.md">Open the exact first-session packet</a>.</p>
<aside><p>""" + teaching_note + """ Third-party readings have separate rights and may need online or library access.</p></aside>
<h2>Opening readings</h2><ul>""" + "\n".join(reading) + """</ul>
<h2>Courses and options</h2><ol>""" + "\n".join(items) + """</ol>
</main><footer><p>Source of truth: <a href="README.md">current Markdown pages</a>. Original readings and notices remain in the private archive.</p></footer></body></html>
"""


def route_options(data, digest):
    lines = [
        "# Directly compatible route options", "",
        f"Generated from `data/course.json` ({digest}). These are September 30 **source-baseline** hours, not revised totals or completion claims.",
        "",
        "Courses 1–10 come first. Choose one Course 11 tradition, one Course 12 area and one compatible Course 13 seminar, then Course 14. Every listed route satisfies the currently recorded prerequisites without an extra option. A combination absent from this list may require an additional course or a documented equivalent; it is not silently approved.",
        "", "| Course 11 | Course 12 | Course 13 | Source-baseline focused hours |",
        "| --- | --- | --- | ---: |",
    ]
    for choice, hours in route_records(data["courses"]):
        lines.append("| " + " | ".join(choice) + f" | {hours:,} |")
    lines += [
        "", "The default C11A/C12A/C13A route is 1,890 source-baseline hours. Choosing C12B on the compatible C11A/C13B route yields 1,870. The [authored workload view](../instruction/workload.md) adds finite packets and the non-12A language bridge, separates optional probability support, and applies only earned overlap credits. Any completed work is credited once.",
        "", "See the [prerequisites and source route](program.md), [interim milestones](milestones.md), [all teaching materials](../instruction/README.md), and [original workload ledger](../data/workload.json).", "",
    ]
    return "\n".join(lines)


def later_readings():
    backlog = json.loads((ROOT / "data/reading-backlog.json").read_text())
    lines = [
        "# Later reading acquisition backlog", "",
        "These earlier acquisition candidates supplement the opening reading catalogue. Their original readiness labels are retained; they do not incorporate every later course source audit. Consult the teaching packet's audit for newer passage checks and remaining edition dependencies. Recheck edition, locator, access and rights before the relevant module.",
        "", "| ID | Work and assigned range | Candidate access | Readiness |",
        "| --- | --- | --- | --- |",
    ]
    for r in backlog["records"]:
        access = f"[Open host]({r['access_url']})" if r.get("access_url") else "Local private-study copy; see JSON path"
        lines.append(f"| `{r['id']}` | {r['work']}; {r['range']} | {access} | {r['readiness']} |")
    lines += ["", "See [candidate metadata, rights and quality notes](../../data/reading-backlog.json) and the [source corrections](source-corrections.md).", ""]
    return "\n".join(lines)


def outputs():
    data, digest = load()
    return {
        ROOT / "current/readiness/course-01.md": readiness(data, digest),
        ROOT / "current/navigation.html": navigation(data, digest),
        ROOT / "current/route-options.md": route_options(data, digest),
        ROOT / "current/readiness/later-backlog.md": later_readings(),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if generated views are stale")
    args = parser.parse_args()
    stale = []
    for path, content in outputs().items():
        if args.check:
            if not path.exists() or path.read_text() != content:
                stale.append(str(path.relative_to(ROOT)))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content)
            print(path.relative_to(ROOT))
    if stale:
        raise SystemExit("Stale generated views: " + ", ".join(stale))


if __name__ == "__main__":
    main()
