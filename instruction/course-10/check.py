#!/usr/bin/env python3
"""Course 10 offline integrity checks; optional external URL transport checks only."""
from pathlib import Path
from fractions import Fraction as Q
import argparse, hashlib, json, re

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
parser = argparse.ArgumentParser()
parser.add_argument('--external', action='store_true', help='Check source URL transport; does not render or establish passage access')
args = parser.parse_args()
manifest = json.loads((HERE / 'authoring.json').read_text())
track = manifest['tracks'][0]
assert manifest['course_number'] == 10 and track['id'] == 'C10'
expected = [14, 14, 14, 18, 16, 14, 22, 8]
assert [m['hours'] for m in track['modules']] == expected
assert sum(expected) == track['baseline_hours'] == 120
curriculum = (ROOT / track['curriculum_page']).read_text()
source_hours = [int(n) for n in re.findall(r'\*\*\d+\. [^\n]*?, (\d+) hours\.', curriculum)]
assert source_hours == expected, ('curriculum module hours changed', source_hours)
for module in track['modules']:
    assert sum(module['allocation_minutes'].values()) == module['hours'] * 60, module['id']
    assert (ROOT / module['path']).is_file(), module['path']
for key in ['curriculum_page', 'readme', 'outcomes', 'assessment', 'examiner', 'source_audit']:
    assert (ROOT / track[key]).is_file(), key
addition = manifest['additions'][0]
assert addition['pc_task'] == 'PC-31' and addition['optional'] is True
assert addition['applies_to'] == ['C10']
assert addition['hours'] == addition['net_hours'] == 6 and addition['replaces_hours'] == 0
assert sum(addition['allocation_minutes'].values()) == 360
assert (ROOT / addition['path']).is_file()
assert sum(track['assessment_minutes'].values()) == 480
assert track['assessment_minutes']['fresh_written'] == 4 * 25 == 100
assert track['assessment_minutes']['final_delayed'] == 30
assert track['delayed_charge_course'] == 'C10'
assert track['delayed_interval'] == 'roughly four to six weeks or after two later modules'
assert 120 + addition['net_hours'] == 126

links = 0
urls = set()
for p in HERE.rglob('*.md'):
    content = p.read_text()
    for target in re.findall(r'\]\(([^)]+)\)', content):
        target = target.strip('<>')
        if target.startswith(('https://','http://')):
            urls.add(target)
            continue
        if target.startswith('#'):
            continue
        local = target.split('#')[0]
        assert (p.parent / local).resolve().exists(), f'{p.name}: missing {target}'
        links += 1
for row in track['essential_rows']:
    assert row['practice'] and row['fresh'] and row['alternate'] and row['delayed']
    text = (HERE / 'assessment.md').read_text()
    assert f"**{row['fresh']} " in text and f"**{row['alternate']} " in text
assert len(track['essential_rows']) == 4

# Numerical and population-total checks for original cases.
checks = {
    'M01_P1_fault_given_flash': (Q(90, 90+90), Q(1,2)),
    'I1_fault_given_flash_returns': (Q(72,72+2), Q(36,37)),
    'W1_fault_given_alarm': (Q(90,90+990), Q(1,12)),
    'W1_fault_given_no_alarm': (Q(10,10+8910), Q(1,892)),
    'W1_high_base_rate': (Q(900,900+900), Q(1,2)),
    'W2_independent_retest': (Q(81,81+99), Q(9,20)),
    'PB_P_flag_given_fault': (Q(38,40), Q(19,20)),
    'PB_P_fault_given_flag': (Q(38,38+98), Q(19,68)),
    'PB_P_fault_given_no_flag': (Q(2,2+1862), Q(1,932)),
    'PB_F_total_faulty': (Q(72)/Q(9,10), Q(80)),
    'PB_F_base_rate': (Q(80,1000), Q(2,25)),
    'PB_F_fault_given_flag': (Q(72,120), Q(3,5)),
    'PB_F_fault_given_no_flag': (Q(8,880), Q(1,110)),
    'PB_F_min_base_without_detector_condition': (Q(72,1000), Q(9,125)),
    'PB_F_max_base_without_detector_condition': (Q(72+880,1000), Q(119,125)),
    'PB_A_before': (Q(160,240), Q(2,3)),
    'PB_A_after': (Q(120,120+60), Q(2,3)),
    'PB_A_second_given_fault': (Q(120,160), Q(3,4)),
    'PB_A_second_given_sound': (Q(60,80), Q(3,4)),
    'PB_D_fault_given_flag': (Q(30,30+90), Q(1,4)),
    'PB_D_fault_given_selection': (Q(15,15+45), Q(1,4)),
}
for label, (got, expected_value) in checks.items():
    assert got == expected_value, (label, got, expected_value)
for cells, total in [([90,10,990,8910],10000),([38,2,98,1862],2000),([72,8,48,872],1000),([120,40,60,20],240)]:
    assert sum(cells) == total
assert Q(40)*Q(95,100)==38 and Q(1960)*Q(5,100)==98
assert Q(90)*Q(9,10)==81 and Q(990)*Q(1,10)==99
bridge_text=(HERE/'probability-bridge.md').read_text()
key_text=(HERE/'examiner-notes.md').read_text()
for fraction in ['1/12','1/892','19/68','1/932']:
    assert fraction in key_text
assert '81/180' in bridge_text and '45%' in bridge_text
assert 'exactly 120 flag' in bridge_text.lower() and '72 are faulty and 48 are sound' in bridge_text
assert '90% of all faulty devices' in bridge_text
for fraction in ['2/25','3/5','1/110','9/125','119/125']:
    assert fraction in key_text
# The old selected-population PB-F has been replaced, not retained as another required item.
assert 'repair depot receives 1,000 returned devices' not in bridge_text.lower()
hume=ROOT/'collection/philosophy-study-collection/texts/gutenberg/pg9662-an-enquiry-concerning-human-understanding.txt'
print(json.dumps({
    'status':'PASS offline structural/arithmetic checks',
    'module_count':len(track['modules']), 'baseline_hours':120,
    'optional_bridge_hours':6, 'with_bridge_hours':126,
    'fresh_written_minutes':100,'final_delayed_minutes_charged_once_to_C10':30,
    'essential_rows':4,'local_markdown_links_checked':links,
    'rational_calculations_checked':len(checks),
    'hume_comparison_sha256':hashlib.sha256(hume.read_bytes()).hexdigest(),
    'external_links_in_markdown':len(urls),
    'external_check_run':args.external,
    'not_established':['learner competence','passage verification for inaccessible sources','rights clearance','human expert review','rendered accessibility']
}, indent=2))
if args.external:
    import urllib.request, urllib.error
    for url in sorted(urls):
        try:
            req=urllib.request.Request(url,headers={'User-Agent':'Course10-source-link-check/1.0'},method='HEAD')
            with urllib.request.urlopen(req,timeout=15) as response:
                print(json.dumps({'url':url,'status':response.status,'final_url':response.url,'scope':'transport only'}))
        except Exception as exc:
            print(json.dumps({'url':url,'status':'unavailable-or-error','detail':str(exc),'scope':'transport only; not proof of permanent absence'}))
