#!/usr/bin/env python3
"""Read-only Course 7 contract, timing, local-link and source-identity checks.
Run from any directory. No network, browser, source rendering or learner scoring.
"""
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
errors = []
checks = []

def check(ok, message):
    (checks if ok else errors).append(message)

contract = json.loads((HERE / 'authoring.json').read_text())
track = contract['tracks'][0]
expected = [16, 16, 14, 18, 16, 22, 28, 10]
check(contract['course_number'] == 7 and track['id'] == 'C07', 'Course/track identity')
check([m['hours'] for m in track['modules']] == expected, 'Eight preserved module allocations')
check(sum(expected) == track['baseline_hours'] == 140, 'Baseline is 140 hours')
source = (ROOT / track['curriculum_page']).read_text()
source_hours = [int(x) for x in re.findall(r'\*\*\d+\. [^\n]*?, (\d+) hours\.\*\*', source)]
check(source_hours == expected, 'Module hours match current/courses/07.md')
for key in ['readme', 'outcomes', 'assessment', 'examiner', 'source_audit']:
    check((ROOT / track[key]).is_file(), f'Contract path exists: {key}')
for m in track['modules']:
    f = ROOT / m['path']
    check(f.is_file(), f"Module path {m['id']}")
    text = f.read_text()
    check(sum(m['budget_minutes']) == m['hours'] * 60, f"Minute budget {m['id']}")
    check(f"**{m['hours']} hours" in text, f"Prose total {m['id']}")
    check('Guiding question:' in text and 'Prerequisites:' in text and 'Outcomes:' in text,
          f"Question/prerequisites/outcomes {m['id']}")
    check(bool(re.search(r'## .*?(Reading|Assigned work|Assignment)', text)), f"Reading boundary {m['id']}")
    check(bool(re.search(r'## .*?(Teaching|Explanation)', text)), f"Teaching section {m['id']}")
    check('Independent' in text and ('repair' in text.lower() or 'remediation' in text.lower()),
          f"Independent work and repair {m['id']}")
    check('Next:' in text, f"Next step {m['id']}")
    check(len(text.split()) >= 350, f"Substantive-size sanity check {m['id']} (not pedagogical validation)")
for a in contract['additions']:
    check((ROOT / a['path']).is_file(), f"Addition path {a['id']}")
    check(a['hours'] - a['replaces_hours'] == a['net_hours'], f"Net-hour arithmetic {a['id']}")
    check(sum(a['budget_minutes']) == 60 * a['hours'], f"Minute budget {a['id']}")
    check(bool(a['credit_rule']) and a['applies_to'] == ['C07'], f"Credit/scope {a['id']}")
check(sum(a['net_hours'] for a in contract['additions']) == 32, 'Additions total +32h, replace 0h')
check(track['baseline_hours'] + sum(a['net_hours'] for a in contract['additions']) == contract['planned_amended_hours'] == 172,
      'Amended planned total 172h')
assess = (HERE / 'assessment.md').read_text()
anchors = (HERE / 'examiner-notes.md').read_text()
for form in ['F', 'B', 'D', 'E']:
    for i in range(1, 4):
        label = f'{form}{i}'
        check(bool(re.search(r'\*\*' + label + r'[ —:,]', assess)), f'Concrete assessment {label}')
        check(bool(re.search(r'\*\*' + label + r'[,:]', anchors)), f'Separate anchor {label}')
check(contract['assessment_minutes']['fresh_rows'] == [35,30,25], 'Essential-row timing 35/30/25')
check('4–6 weeks' in assess and '4–6 weeks' in (HERE/'modules/08.md').read_text(), 'Final delayed interval in learner materials')
check('600 = 10h' in (HERE/'modules/08.md').read_text(), 'M8 budget includes delayed time')
links = 0
external = set()
for f in sorted(HERE.rglob('*.md')):
    text = f.read_text()
    for raw in re.findall(r'\[[^\]]*\]\(([^)]+)\)', text):
        target = raw.strip('<>')
        if target.startswith(('https://','http://')):
            external.add(target)
            continue
        if target.startswith('#'):
            continue
        target = unquote(target.split('#')[0])
        links += 1
        check((f.parent/target).resolve().exists(), f'Local link {f.relative_to(HERE)} → {target}')
fingerprints = json.loads((HERE/'source-fingerprints.json').read_text())
for item in fingerprints['sources']:
    f = ROOT/item['path']
    check(f.is_file() and hashlib.sha256(f.read_bytes()).hexdigest() == item['sha256'],
          'Source bytes unchanged: '+f.name)
check(not (HERE/'.source-check').exists(), 'Temporary source-page derivatives removed')
result = {
    'status': 'pass' if not errors else 'fail',
    'checks_passed': len(checks), 'errors': errors,
    'baseline_hours': 140, 'addition_net_hours': 32, 'planned_total_hours': 172,
    'modules': len(track['modules']), 'additions': len(contract['additions']),
    'markdown_files': len(list(HERE.rglob('*.md'))), 'local_links_checked': links,
    'external_links_enumerated_not_retested': len(external),
    'source_fingerprints_checked': len(fingerprints['sources']),
    'limits': ['Structural/link/contract arithmetic only; no learner evidence or pedagogical certification.',
               'External source access outcomes are manually recorded in source-audit.md; no HTTP success inferred.',
               'No browser/rendered accessibility, FE8/UIT, rights, expert or model-identity validation.']
}
print(json.dumps(result, ensure_ascii=False, indent=2))
sys.exit(bool(errors))
