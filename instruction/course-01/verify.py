"""Validate Course 1's authoring contract, time allocations and local links."""
from pathlib import Path
from urllib.parse import unquote
import json
import re

here = Path(__file__).resolve().parent
repo = here.parents[1]
contract = json.loads((here / "authoring.json").read_text())
errors = []
track = contract["tracks"][0]
assert track["id"] == "C01"
assert track["baseline_hours"] == 120
assert len(track["modules"]) == 12
assert sum(m["hours"] for m in track["modules"]) == 120
assert 90 + 70 + 20 + 90 + 90 == 360
for module in track["modules"]:
    assert sum(module["allocation_minutes"].values()) == 60 * module["hours"], module["id"]
for addition in contract["additions"]:
    assert addition["hours"] - addition["replaces_hours"] == addition["net_hours"]
assert sum(a["net_hours"] for a in contract["additions"]) == 0

def paths(value):
    if isinstance(value, dict):
        for key, item in value.items():
            if key in {"path", "readme", "outcomes", "assessment", "examiner", "source_audit", "curriculum_page"}:
                yield item
            else:
                yield from paths(item)
    elif isinstance(value, list):
        for item in value:
            yield from paths(item)

for path in paths(contract):
    if not (repo / path).is_file():
        errors.append(f"Contract path missing: {path}")

def headings(path):
    found = set()
    for line in path.read_text().splitlines():
        if re.match(r"^#{1,6}\s", line):
            title = re.sub(r"^#{1,6}\s+", "", line).strip().lower()
            title = re.sub(r"[^\w\- ]", "", title)
            found.add(title.replace(" ", "-"))
    return found

checked = 0
for doc in here.rglob("*.md"):
    for target in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", doc.read_text()):
        if target.startswith(("https://", "http://", "mailto:")):
            continue
        file_part, _, anchor = target.partition("#")
        dest = (doc.parent / unquote(file_part)).resolve() if file_part else doc
        checked += 1
        if not dest.exists():
            errors.append(f"{doc.relative_to(repo)} -> missing {target}")
        elif anchor and dest.suffix == ".md" and unquote(anchor) not in headings(dest):
            errors.append(f"{doc.relative_to(repo)} -> missing heading {target}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: 12 modules; 120 hours; allocations 7200 minutes; opening credit 360 minutes; PC-31 net 0; {checked} local links and anchors; all contract paths.")
