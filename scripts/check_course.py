#!/usr/bin/env python3
"""One local check for the currently released course scope."""

import hashlib
import html.parser
import json
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ERRORS = []


def fail(message):
    ERRORS.append(message)


def read_json(name):
    return json.loads((ROOT / name).read_text())


def unique(items, label):
    ids = [x["id"] for x in items]
    if len(ids) != len(set(ids)):
        fail(f"duplicate {label} ID")
    return {x["id"]: x for x in items}


def slug(s):
    s = re.sub(r"<[^>]+>|[*_`]", "", s).lower()
    s = re.sub(r"[^\w -]", "", s)
    return re.sub(r"\s+", "-", s.strip())


class Links(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.hrefs = []
        self.ids = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "href" in attrs:
            self.hrefs.append(attrs["href"])
        if "id" in attrs:
            self.ids.append(attrs["id"])


def check_links():
    paths = [ROOT / "README.md"]
    for dirname in ("current", "instruction", "implementation", "collection"):
        if dirname == "collection":
            paths.append(ROOT / "collection/README.md")
        else:
            paths.extend(p for p in (ROOT / dirname).rglob("*") if p.suffix in {".md", ".html"})
    for path in paths:
        text = path.read_text()
        if path.suffix == ".html":
            parser = Links()
            parser.feed(text)
            refs = parser.hrefs
        else:
            refs = re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)", text)
        for ref in refs:
            if ref.startswith(("http:", "https:", "mailto:", "data:")):
                continue
            parsed = urlsplit(ref)
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not target.is_relative_to(ROOT) or not target.exists():
                fail(f"broken local link: {path.relative_to(ROOT)} -> {ref}")
                continue
            if not parsed.fragment:
                continue
            if target.suffix == ".md":
                anchors = {slug(h) for h in re.findall(r"^#{1,6}\s+(.+)$", target.read_text(), flags=re.M)}
            elif target.suffix == ".html":
                parser = Links()
                parser.feed(target.read_text())
                anchors = set(parser.ids)
            else:
                continue
            if unquote(parsed.fragment) not in anchors:
                fail(f"broken local anchor: {path.relative_to(ROOT)} -> {ref}")


def check_data():
    data = read_json("data/course.json")
    workload = read_json("data/workload.json")
    if data["curriculum_version"] != workload["curriculum_version"]:
        fail("course and workload versions differ")
    courses = unique(data["courses"], "course")
    works = unique(data["works"], "work")
    editions = unique(data["editions"], "edition")
    assets = unique(data["assets"], "asset")
    assignments = unique(data["assignments"], "assignment")
    for c in courses.values():
        if not (ROOT / c["page"]).is_file() or c["baseline_hours"] <= 0:
            fail(f"course page or hours invalid: {c['id']}")
        for req in c["prerequisites"]:
            base = req.split(":")[0]
            if base not in courses:
                fail(f"unknown prerequisite: {c['id']} -> {req}")
    visiting, visited = set(), set()

    def visit(id_):
        if id_ in visiting:
            fail(f"dependency cycle at {id_}")
            return
        if id_ in visited:
            return
        visiting.add(id_)
        for req in courses[id_]["prerequisites"]:
            visit(req.split(":")[0])
        visiting.remove(id_)
        visited.add(id_)

    for id_ in courses:
        visit(id_)
    for e in editions.values():
        if e["work_id"] not in works:
            fail(f"edition without work: {e['id']}")
    for a in assets.values():
        if a["edition_id"] not in editions:
            fail(f"asset without edition: {a['id']}")
        if a.get("local_path") and not (ROOT / a["local_path"]).is_file():
            fail(f"missing local asset: {a['id']}")
        if not a.get("rights") or not a.get("text_quality"):
            fail(f"asset lacks separate rights/quality: {a['id']}")
    for a in assignments.values():
        if a["course_id"] not in courses or a["edition_id"] not in editions or a["asset_id"] not in assets:
            fail(f"broken assignment reference: {a['id']}")
        if a["asset_id"] in assets and assets[a["asset_id"]]["edition_id"] != a["edition_id"]:
            fail(f"assignment edition/asset mismatch: {a['id']}")
        if not a.get("locator") or re.search(r"\b(?:TBD|selections only|not yet specified)\b", a["locator"], re.I):
            fail(f"unbounded opening assignment: {a['id']}")
    route = data["default_route"]
    if len(route) != 14 or len(set(route)) != 14 or any(x not in courses for x in route):
        fail("invalid default route")
    total = sum(courses[x]["baseline_hours"] for x in route)
    if total != workload["baseline"]["default_route"] or sum(courses[x]["baseline_hours"] for x in route[:10]) != workload["baseline"]["common_core_through_C10"]:
        fail("route hours do not match source baselines")
    for addition in workload["adopted_additions"]:
        if addition["net_hours"] != addition["gross_hours"] - addition["replaced_hours"]:
            fail(f"incorrect net hours: {addition['task']}")
    if workload["revised_default_total"] is not None:
        fail("revised total asserted before later route additions are specified")
    cap = (ROOT / "current/courses/14.md").read_text()
    cap_hours = [int(x) for x in re.findall(r"^\*\*[1-8]\. .*?, (\d+) hours\.\*\*", cap, flags=re.M)]
    if cap_hours != [16, 26, 20, 40, 16, 32, 12, 18] or sum(cap_hours) != 180:
        fail(f"capstone eight-milestone regression: {cap_hours}")
    for n in range(1, 5):
        if not (ROOT / f"instruction/course-01/sessions/{n:02d}.md").is_file():
            fail(f"missing opening session {n}")


def check_baseline_and_distribution():
    m = read_json("archive/conversion-map.json")
    for path, expected in [(ROOT / "Philosophy curriculum and writing foundations.docx", m["source_docx_sha256"]), (ROOT / "archive/revised-curriculum-pandoc-baseline.md", m["baseline_markdown_sha256"])]:
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            fail(f"baseline digest changed: {path.name}")
    for name in m["pages"]:
        if not (ROOT / "current" / name).is_file():
            fail(f"missing converted page: {name}")
    rules = read_json("data/distribution.json")
    forbidden = set(rules["excluded_roots"])
    for name in rules["files"] + rules["directories"]:
        p = ROOT / name
        if name.split("/")[0] in forbidden or not p.exists():
            fail(f"unsafe or missing distribution allowlist entry: {name}")
    tracked = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT).split(b"\0")
    if any(p.startswith((b"learner/", b".private_readings/", b"dist/")) for p in tracked):
        fail("private learner/cache/dist file tracked")
    for p in [ROOT / "README.md", *list((ROOT / "current").rglob("*.md")), *list((ROOT / "instruction").rglob("*.md"))]:
        if re.search(r"https?://(?:www\.)?chatgpt\.com/(?:c|s)/", p.read_text()):
            fail(f"stale private ChatGPT link: {p.relative_to(ROOT)}")


def main():
    check_data()
    check_baseline_and_distribution()
    check_links()
    proc = subprocess.run([sys.executable, str(ROOT / "scripts/build_views.py"), "--check"], capture_output=True, text=True)
    if proc.returncode:
        fail(proc.stderr.strip() or proc.stdout.strip() or "generated views stale")
    if ERRORS:
        print("Course check failed:")
        for error in ERRORS:
            print("-", error)
        raise SystemExit(1)
    print("Course check passed: current IDs, route hours, capstone, baselines, links, private-path rules and generated views.")


if __name__ == "__main__":
    main()
