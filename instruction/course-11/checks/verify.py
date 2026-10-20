#!/usr/bin/env python3
"""Read-only Course 11 structural/link/budget check; run from any directory."""
import json
import re
from fractions import Fraction
from pathlib import Path
from urllib.parse import unquote, urlsplit

OWN = Path(__file__).resolve().parents[1]
ROOT = OWN.parents[1]
errors = []
def need(condition, message):
    if not condition:
        errors.append(message)

manifest = json.loads((OWN / 'authoring.json').read_text())
timing = json.loads((OWN / 'checks/timing.json').read_text())
expected = {'C11A': [10,22,20,16,24,18,22,8], 'C11B': [14,20,24,20,16,14,24,8]}
need(manifest['course_number'] == 11, 'wrong course number')
need({x['id'] for x in manifest['tracks']} == set(expected), 'missing/extra track')
for track in manifest['tracks']:
    tid = track['id']
    need(len(track['modules']) == 8, f'{tid}: expected eight modules')
    need([m['hours'] for m in track['modules']] == expected[tid], f'{tid}: baseline module hours differ')
    need(sum(m['hours'] for m in track['modules']) == track['baseline_hours'] == 140, f'{tid}: total differs')
    for key in ['curriculum_page','readme','outcomes','assessment','examiner','source_audit']:
        need((ROOT / track[key]).is_file(), f'{tid}: missing {key} {track[key]}')
    for module in track['modules']:
        p = ROOT / module['path']
        need(p.is_file(), f'missing module {p}')
        if not p.is_file():
            continue
        text = p.read_text()
        need(module['id'] in text, f'{p.name}: missing module id')
        for token in ['Guiding question', 'Prerequisites', 'independent', 'feedback', 'revision']:
            need(token.lower() in text.lower(), f'{module["id"]}: missing {token}')
        need('worked' in text.lower(), f'{module["id"]}: missing worked practice')
        parts = timing[module['id']]['minutes']
        need(sum(Fraction(v) for v in parts.values()) == module['hours']*60, f'{module["id"]}: time parts do not sum')
        need(timing[module['id']]['total_hours'] == module['hours'], f'{module["id"]}: timing total differs')
        # The prose's stated total is checked separately from the allocation ledger.
        need(f'**{module["hours"]}h**' in text or f'**{module["hours"]} hours' in text, f'{module["id"]}: missing prose total')

links = 0
for p in OWN.rglob('*.md'):
    for target in re.findall(r'\]\(([^)]+)\)', p.read_text()):
        target = target.strip('<>')
        if urlsplit(target).scheme or target.startswith('#'):
            continue
        path = unquote(target.split('#')[0])
        if not path:
            continue
        links += 1
        need((p.parent/path).resolve().exists(), f'broken local link: {p.relative_to(OWN)} -> {target}')

assessment = (OWN/'assessment.md').read_text()
anchors = (OWN/'examiner-notes.md').read_text()
outcomes = (OWN/'outcomes.md').read_text()
for prefix in ['A8','B8']:
    for stem in ['F','X','D','DX']:
        for n in range(1,4):
            task = f'{prefix}-{stem}{n}'
            need(task in assessment, f'missing learner form {task}')
            # Compact F/X paired headings give each alternate a clear shared criterion.
            need(task in anchors or (stem=='X' and f'{prefix}-F{n}/X{n}' in anchors), f'missing examiner anchor {task}')
            need(task in outcomes, f'missing outcome map {task}')
need(not manifest['additions'], 'Course11 has no PC25–33 net addition')
need('source-dependent' in assessment, 'missing access-conditional assessment rule')
need('four to six weeks' in assessment, 'missing delayed interval')
print(f'Tracks: 2; modules: 16; baseline: C11A=140h, C11B=140h; additions: 0h')
print(f'Checked {links} local Markdown links and 24 final-form IDs; all 16 minute allocations reconciled.')
if errors:
    print('\n'.join('FAIL: '+e for e in errors))
    raise SystemExit(1)
print('PASS: structure, referenced files, internal links, task coverage, timing ledger.')
print('Not tested: source accuracy, external URLs, learner timing, rendering, accessibility or empirical learning.')
