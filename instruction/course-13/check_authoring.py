#!/usr/bin/env python3
"""Read-only structural audit. It does not test teaching quality or access rights."""
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
data = json.loads((HERE / 'authoring.json').read_text())
assert data['course_number'] == 13
assert {t['id'] for t in data['tracks']} == {'C13A', 'C13B', 'C13C'}
expected = [10, 44, 22, 16, 24, 24, 10, 10]
for track in data['tracks']:
    assert [m['hours'] for m in track['modules']] == expected, track['id']
    assert sum(m['hours'] for m in track['modules']) == track['baseline_hours'] == 160
    for key in ['curriculum_page', 'readme', 'outcomes', 'assessment', 'examiner', 'source_audit', 'packet']:
        assert (ROOT / track[key]).is_file(), (track['id'], key)
    for mod in track['modules']:
        path = ROOT / mod['path']
        assert path.is_file(), path
        body = path.read_text()
        assert len(body.split()) > 380, (path, 'unexpectedly short module')
        assert 'Prerequisite' in body and 'Outcomes:' in body, path
        assert 'Budget' in body and ('Independent' in body or 'independent' in body), path
assert len({m['path'] for t in data['tracks'] for m in t['modules']}) == 8
assert data['additions'] == []
links = 0
for path in HERE.rglob('*.md'):
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
        if '://' in target or target.startswith('#'):
            continue
        target = target.split('#')[0]
        if target:
            links += 1
            assert (path.parent / target).resolve().exists(), (path, target)
assessment = (HERE / 'assessment.md').read_text()
key = (HERE / 'examiner-notes.md').read_text()
for route in 'ABC':
    for form in ['F1', 'F2', 'D1', 'D2']:
        assert f'{route}-{form}' in assessment, (route, form, 'prompt')
        assert f'{route}-{form}' in key, (route, form, 'anchor')
assert 'four to six weeks or two later modules' in assessment
print(f'PASS: 3 tracks; shared 8-module sequence; each 160h; {links} local links; 12 route transfer forms with examiner anchors.')
print('NOT TESTED: source accuracy/access, permissions, learner outcomes, expert review, rendering/accessibility, runtime model.')
