#!/usr/bin/env python3
"""Static Course 14 authoring checks; no network, rendering, or learner assessment."""
from pathlib import Path
import hashlib
import json
import re
import sys
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
EXPECTED = [16, 26, 20, 40, 16, 32, 12, 18]
errors = []
checks = 0

def check(condition, message):
    global checks
    checks += 1
    if not condition:
        errors.append(message)

manifest = json.loads((HERE / "authoring.json").read_text())
check(manifest["course_number"] == 14, "Wrong course number")
check(manifest["authored_on"] == "2026-10-20", "Wrong authoring date")
check(len(manifest["tracks"]) == 1, "Expected one capstone track")
track = manifest["tracks"][0]
check(track["id"] == "C14", "Wrong track ID")
check(track["baseline_hours"] == 180, "Baseline must be 180")
check(manifest["additions"] == [], "Unexpected extra capstone billing")
check([m["hours"] for m in track["modules"]] == EXPECTED, "Milestone hour sequence differs")
check(sum(m["hours"] for m in track["modules"]) == 180, "Module sum differs from 180")
for key in ("curriculum_page", "readme", "outcomes", "assessment", "examiner", "source_audit"):
    check((ROOT / track[key]).is_file(), f"Missing manifest path: {key}")
for i, module in enumerate(track["modules"], 1):
    check(module["id"] == f"C14-M{i:02d}", f"Wrong module ID at {i}")
    path = ROOT / module["path"]
    check(path.is_file(), f"Missing module: {path}")
    text = path.read_text()
    budget = re.search(r"\| Reading \| Practice \| Feedback \| Independent work \| Revision \| Total \|\n[^\n]+\n\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|", text)
    check(budget is not None, f"Missing budget table: {path.name}")
    if budget:
        values = [int(v) for v in budget.groups()]
        check(sum(values[:5]) == values[5] == EXPECTED[i - 1], f"Budget mismatch: {path.name}")
    for token in ("Guiding question", "Prerequisite", "Outcomes", "Assigned reading", "Budget"):
        check(token.lower() in text.lower(), f"Missing {token}: {path.name}")
source = (ROOT / track["curriculum_page"]).read_text()
source_hours = [int(h) for h in re.findall(r"\*\*\d+\. [^\n]*?, (\d+) hours\.\*\*", source)]
check(source_hours == EXPECTED, f"Authority hours differ: {source_hours}")
for name in ("README.md", "outcomes.md", "assessment.md", "examiner-notes.md", "tutor-notes.md", "source-audit.md", "templates.md", "source-selection.md", "worked-examples.md", "authoring.json", "source-fingerprints.json", "verification.md"):
    check((HERE / name).is_file(), f"Missing deliverable: {name}")
link_count = 0
for path in HERE.rglob("*.md"):
    for target in re.findall(r"\[[^\]]*\]\(([^)]+)\)", path.read_text()):
        if re.match(r"(?:https?://|mailto:|#)", target):
            continue
        target = unquote(target.split("#", 1)[0]).strip("<>")
        if target:
            link_count += 1
            check((path.parent / target).exists(), f"Broken local link in {path.relative_to(HERE)}: {target}")
fingerprints = json.loads((HERE / "source-fingerprints.json").read_text())
for path, expected in fingerprints["sha256"].items():
    actual = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
    check(actual == expected, f"Authority input changed; review required: {path}")
# Regression guards for the two reviewed exposure repairs. These are not a
# semantic proof of freshness; see verification.md for the full-corpus review.
assessment = (HERE / "assessment.md").read_text()
examiner = (HERE / "examiner-notes.md").read_text()
check("In an invented garden, account H" in assessment, "Missing replacement T7 evidence case")
check("Three invented schools endorse one and the same rule" in assessment, "Missing replacement D8 method B case")
check("A community archive publishes two agreeing catalogue descriptions" not in assessment, "Retired coached T7 default restored")
check("An invented institution's origin story" not in assessment, "Retired coached D8 default restored")
check("holds rain absent and runs the sprinkler" in examiner, "Missing T7 discriminating-observation anchor")
check("tracking the criterion across a chain of comparisons" in examiner, "Missing D8 comparison-criterion anchor")
check("two catalogues share one damaged origin" not in examiner, "Stale T7 anchor")
check("D8B distinguishes a rule's origin" not in examiner, "Stale D8 method anchor")
if errors:
    print("FAIL")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)
print(f"PASS: {checks} structural checks; {link_count} local Markdown links; 8 milestones; 180 hours.")
print("No learner, rights, external-review, or rendered-accessibility validation is implied.")
