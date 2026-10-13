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
from audit_conversion import audit as audit_conversion
from build_assignment_catalogue import build as build_assignment_catalogue
from course_model import COMMON, OPTIONS, base, requirements_met, route_records

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
    catalogue = read_json("data/assignment-catalogue.json")
    if catalogue != build_assignment_catalogue():
        fail("later assignment catalogue differs from current source pages")
    catalogue_items = unique(catalogue["records"], "later assignment")
    if len(catalogue_items) != 130:
        fail("later assignment catalogue incomplete")
    workload = read_json("data/workload.json")
    if data["curriculum_version"] != workload["curriculum_version"]:
        fail("course and workload versions differ")
    courses = unique(data["courses"], "course")
    works = unique(data["works"], "work")
    editions = unique(data["editions"], "edition")
    assets = unique(data["assets"], "asset")
    assignments = unique(data["assignments"], "assignment")
    backlog = read_json("data/reading-backlog.json")
    later = unique(backlog["records"], "later reading")
    if set(later) & set(assignments):
        fail("later reading ID duplicates a released assignment")
    for item in later.values():
        if item["course_id"] not in courses or not (ROOT / item["source_page"]).is_file():
            fail(f"later reading has no course/source page: {item['id']}")
        if not item.get("range") or not item.get("rights") or not item.get("quality_note") or not item.get("readiness"):
            fail(f"later reading lacks range/rights/quality/readiness: {item['id']}")
        if item.get("local_path") and not (ROOT / item["local_path"]).is_file():
            fail(f"later reading local candidate absent: {item['id']}")
        if not item.get("local_path") and not item.get("access_url"):
            fail(f"later reading has no access candidate: {item['id']}")
    for c in courses.values():
        if not (ROOT / c["page"]).is_file() or c["baseline_hours"] <= 0:
            fail(f"course page or hours invalid: {c['id']}")
        for req in c.get("prerequisites", []) + c.get("recommended_after", []):
            if base(req) not in courses:
                fail(f"unknown prerequisite: {c['id']} -> {req}")
        for group in c.get("prerequisite_groups", []):
            if not group or any(base(req) not in courses for req in group):
                fail(f"unknown or empty prerequisite group: {c['id']} -> {group}")
    expected_required = {
        "C02": ["C01:argument-and-paragraph-modules"],
        "C04": ["C01", "C03"], "C05": ["C01", "C03"],
        "C07": ["C01", "C02:semantics-and-symbolization", "C05"],
        "C09": ["C05", "C06"], "C10": ["C01", "C05:induction"],
        "C12D": ["C06", "C07", "C08"],
    }
    for id_, expected in expected_required.items():
        if courses[id_].get("prerequisites") != expected:
            fail(f"preserved prerequisite mismatch: {id_}")
    if courses["C14"].get("prerequisite_groups") != [["C13A", "C13B", "C13C"]]:
        fail("capstone must accept each selected seminar")
    visiting, visited = set(), set()

    def visit(id_):
        if id_ in visiting:
            fail(f"dependency cycle at {id_}")
            return
        if id_ in visited:
            return
        visiting.add(id_)
        for req in courses[id_].get("prerequisites", []):
            visit(base(req))
        for group in courses[id_].get("prerequisite_groups", []):
            for req in group:
                visit(base(req))
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
    if len(route) != 14 or len(set(route)) != 14 or any(x not in courses for x in route) or route[:10] != COMMON:
        fail("invalid default route")
    else:
        completed = set()
        for id_ in route:
            if not requirements_met(courses[id_], completed):
                fail(f"default route violates prerequisites at {id_}")
            completed.add(id_)
    expected_choices = {
        ("C11A", "C12A", "C13A"), ("C11A", "C12A", "C13B"),
        ("C11A", "C12B", "C13B"), ("C11A", "C12C", "C13B"),
        ("C11A", "C12D", "C13B"), ("C11B", "C12A", "C13A"),
        ("C11B", "C12D", "C13C"),
    }
    direct = route_records(data["courses"])
    if {choice for choice, _ in direct} != expected_choices or len(direct) != len(expected_choices):
        fail("direct option compatibility differs from the preserved curriculum")
    if {(choice, hours) for choice, hours in direct if hours != 1890} != {(('C11A', 'C12B', 'C13B'), 1870)}:
        fail("alternative route baseline hours differ from source")
    source = (ROOT / "archive/revised-curriculum-pandoc-baseline.md").read_text()
    table = dict((f"C{int(n):02d}", int(hours)) for n, hours in re.findall(r"^\|\s*(\d+)\s*\|[^\n]*?\|\s*(\d+)\s*\|", source, flags=re.M))
    for id_ in COMMON:
        if courses[id_]["baseline_hours"] != table.get(id_):
            fail(f"source baseline hour mismatch: {id_}")
    for group, expected in {"C11": 140, "C13": 160}.items():
        if any(courses[id_]["baseline_hours"] != expected for id_ in courses if id_.startswith(group)):
            fail(f"option baseline hour mismatch: {group}")
    for id_, expected in {"C12A": 140, "C12B": 120, "C12C": 140, "C12D": 140, "C14": 180}.items():
        if courses[id_]["baseline_hours"] != expected:
            fail(f"source baseline hour mismatch: {id_}")
    total = sum(courses[x]["baseline_hours"] for x in route)
    if total != workload["baseline"]["default_route"] or sum(courses[x]["baseline_hours"] for x in route[:10]) != workload["baseline"]["common_core_through_C10"]:
        fail("route hours do not match source baselines")
    for addition in workload["adopted_additions"]:
        if addition["net_hours"] != addition["gross_hours"] - addition["replaced_hours"]:
            fail(f"incorrect net hours: {addition['task']}")
        if sum(addition[k] for k in ("reading_hours", "practice_hours", "feedback_and_revision_hours")) != addition["gross_hours"]:
            fail(f"adopted hour components differ from gross: {addition['task']}")
        if addition["course"] not in courses or not addition.get("replacement") and addition["replaced_hours"]:
            fail(f"unlocated adopted replacement: {addition['task']}")
    if len({(a["task"], a["course"], a["description"]) for a in workload["adopted_additions"]}) != len(workload["adopted_additions"]):
        fail("adopted workload entry counted twice")
    proposals = workload["specified_proposals"]
    if {p["task"] for p in proposals} != {f"PC-{n:02d}" for n in range(25, 34)}:
        fail("later addition proposal register is incomplete")
    if any(p.get("seed_hours") is not None and p["seed_hours"] <= 0 for p in proposals):
        fail("proposal seed hours must be positive or explicitly unknown")
    if any("proposal" not in p["status"] for p in proposals):
        fail("later addition falsely marked adopted in proposal register")
    if workload["revised_default_total"] is not None:
        fail("revised total asserted before later route additions are specified")
    cap = (ROOT / "current/courses/14.md").read_text()
    cap_hours = [int(x) for x in re.findall(r"^\*\*[1-8]\. .*?, (\d+) hours\.\*\*", cap, flags=re.M)]
    if cap_hours != [16, 26, 20, 40, 16, 32, 12, 18] or sum(cap_hours) != 180:
        fail(f"capstone eight-milestone regression: {cap_hours}")
    for n in range(1, 5):
        if not (ROOT / f"instruction/course-01/sessions/{n:02d}.md").is_file():
            fail(f"missing opening session {n}")
    c01 = (ROOT / "current/courses/01.md").read_text()
    for n in range(1, 5):
        if f"../../instruction/course-01/sessions/{n:02d}.md" not in c01:
            fail(f"current Course 1 does not delegate Session {n} to its packet")
    if "validity/soundness examples in 5.3" in c01 or "bounded deductive part of **5.4**" not in c01:
        fail("stale Course 1 Session 3 reading summary")


def check_baseline_and_distribution():
    m = read_json("archive/conversion-map.json")
    for path, expected in [(ROOT / "Philosophy curriculum and writing foundations.docx", m["source_docx_sha256"]), (ROOT / "archive/revised-curriculum-pandoc-baseline.md", m["baseline_markdown_sha256"])]:
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            fail(f"baseline digest changed: {path.name}")
    for name in m["pages"]:
        if not (ROOT / "current" / name).is_file():
            fail(f"missing converted page: {name}")
    try:
        audit_conversion()
    except ValueError as exc:
        fail(str(exc))
    collection = ROOT / "collection/philosophy-study-collection"
    manifest = json.loads((collection / "FILE_CHECKSUMS.json").read_text())
    if len(manifest) != 214:
        fail("collection checksum inventory count changed")
    for row in manifest:
        path = collection / row["path"]
        if not path.is_file() or path.stat().st_size != row["bytes"] or hashlib.sha256(path.read_bytes()).hexdigest() != row["sha256"]:
            fail(f"collection checksum mismatch: {row['path']}")
    originals = ROOT / "archive/legacy-html-originals"
    for name in ["START_HERE.html", *(f"PART-{n:02d}.html" for n in range(1, 14))]:
        archived = originals / name
        active = collection / name
        if not archived.is_file() or not active.is_file() or "Historical collection index" not in active.read_text() or "../../current/README.md" not in active.read_text():
            fail(f"missing legacy migration or original: {name}")
        else:
            baseline = subprocess.check_output(["git", "show", f"51a35d3:collection/philosophy-study-collection/{name}"], cwd=ROOT)
            if archived.read_bytes() != baseline:
                fail(f"legacy original differs from Git baseline: {name}")
    if (originals / "FILE_CHECKSUMS.original.json").read_bytes() != subprocess.check_output(["git", "show", "51a35d3:collection/philosophy-study-collection/FILE_CHECKSUMS.json"], cwd=ROOT):
        fail("legacy checksum manifest original differs from Git baseline")
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
