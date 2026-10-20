#!/usr/bin/env python3
"""Read-only structural checks for C08. Run from any working directory."""
import json
import re
from pathlib import Path

base = Path(__file__).resolve().parent
root = base.parent.parent
manifest = json.loads((base / 'authoring.json').read_text())
track = manifest['tracks'][0]
assert manifest['course_number'] == 8
assert track['id'] == 'C08'
expected = [12, 18, 16, 18, 20, 20, 28, 8]
assert [m['hours'] for m in track['modules']] == expected
assert sum(expected) == track['baseline_hours'] == 140
for key in ['curriculum_page', 'readme', 'outcomes', 'assessment', 'examiner', 'source_audit']:
    assert (root / track[key]).is_file(), track[key]
for module in track['modules']:
    p = root / module['path']
    assert p.is_file(), p
    assert sum(module['activity_hours'].values()) == module['hours'], module['id']
    prose = p.read_text()
    assert module['id'] in prose
    assert 'Prerequisite' in prose or 'Prerequisites' in prose
for addition in manifest['additions']:
    assert (root / addition['path']).is_file()
    assert addition['hours'] - addition['replaces_hours'] == addition['net_hours'] == 8
    assert sum(addition['activity_hours'].values()) == addition['hours']
assert 140 + sum(a['net_hours'] for a in manifest['additions']) == 148
assert sum(manifest['assessment_minutes'].values()) == 480
assert manifest['assessment_minutes']['fresh_written'] == 90
assert manifest['assessment_minutes']['final_delayed'] == 30
assessment = (base / 'assessment.md').read_text()
examiner = (base / 'examiner-notes.md').read_text()
for form in ['A', 'B', 'D', 'E']:
    for i in range(1, 4):
        item = f'{form}{i}'
        assert re.search(r'\b'+item+r'\b', assessment), item
        assert re.search(r'\b'+item+r'\b', examiner), item
for i in range(1, 8):
    assert f'F{i}' in examiner
for item in ['H-F', 'H-A']:
    assert item in examiner
outcomes = (base / 'outcomes.md').read_text()
for group in ['Authority and liberty', 'Distribution', 'Gender race and idealization']:
    assert group in outcomes
link_count = 0
for file in base.rglob('*.md'):
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', file.read_text()):
        if target.startswith(('https://', 'http://', '#', 'mailto:')):
            continue
        target = target.split('#', 1)[0]
        assert (file.parent / target).resolve().exists(), (file.relative_to(root), target)
        link_count += 1
print(f'PASS: 8 modules, baseline 140h, PC-32 +8h, total 148h; Module 8 480min.')
print(f'PASS: 3 outcome rows; 12 final/alternate/delayed items with examiner anchors; F1-F7 and H-F/H-A.')
print(f'PASS: {link_count} local Markdown links resolve; manifest paths and activity allocations agree.')
print('LIMITS: no remote-link uptime, semantic accuracy, source rights, exposure, rendering or learner validation certified.')
