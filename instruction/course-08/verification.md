# C08 verification — 20 October 2026

Run from the repository root:

```sh
python3 instruction/course-08/check.py
```

The checker is read-only. It checks manifest paths; the eight preserved module allocations (12,18,16,18,20,20,28,8); activity-budget arithmetic; PC-32 8−0=8 net hours; the 480-minute final module; three required outcome row names; all 12 A/B/D/E assessment items and examiner anchors; F1–F7 and H-F/H-A diagnostic coverage; and relative Markdown link target existence. It does not resolve heading anchors or remotely fetch URLs. The expected authored route is 140+8=148 hours. Planning estimates remain subject to learner logs.

A manual content review confirmed that every module contains a guiding question, prerequisites/outcomes, exact reading range, budget, teaching explanation, original explained practice, specified output, independent changed task, repair and next action. Source access caveats are repeated at the affected use points. Module 8 has three 30-minute fresh rows, one 20-minute explanation, a 30-minute final delayed sample after 4–6 weeks/two later modules, and repair/retest time. Short earlier retrieval does not replace the final delayed occasion. The four existing C01 opening sessions were not modified or billed to C08.

No local-file browser or substitute rendered workflow was used. FE8/UIT stayed paused. Markdown link checks do not establish keyboard, screen-reader, audio or reflow usability. No learner pilot, actual-model calibration, expert review, publication permission, or independent model attestation occurred. The source-audit record distinguishes targeted passage inspection from metadata-only assignments.

## Recorded check output

```text
PASS: 8 modules, baseline 140h, PC-32 +8h, total 148h; Module 8 480min.
PASS: 3 outcome rows; 12 final/alternate/delayed items with examiner anchors; F1-F7 and H-F/H-A.
PASS: 32 local Markdown links resolve; manifest paths and activity allocations agree.
LIMITS: no remote-link uptime, semantic accuracy, source rights, exposure, rendering or learner validation certified.
```

## Input fingerprints

SHA-256 records the inspected local bytes, not accuracy, rights or completeness.

| Input | SHA-256 |
| --- | --- |
| `current/courses/08.md` | `a2a76742bf518bbeb52d01063990cdd3fc1f05f5aa6d1b6e23fb7546900a473b` |
| `current/assessment.md` | `9872c96df607fea437d7f445ea3774fba56069ee4012693a5b602c8ef29b2e03` |
| `data/later-reading-catalogue.json` | `8d264aa5a90bf4212a440afb6d62bceb90af9d7cd6248337230c4a3531acf6a8` |
| `implementation/AUTHORING_2026-10-20.md` | `00b12e1b86a8a730cefec11a2d6e1d4432b56f3a9686fa24b4c3bc873db710a4` |
| `implementation/ADDITIONS.md` | `f540f5be75a0544193a5c675ea40f4a3c27154b2412d8cbf564a03614ee8c279` |
| `implementation/UNIFIED_PLAN.md` | `e9cc5ba8ce86faa371f60727b397db6423936455fd80e7cf104a9c9560027725` |
| `collection/philosophy-study-collection/texts/gutenberg/pg34901-on-liberty.txt` | `fad90451253e40190995748ed5d5b60b48b0881cd1a37fa705e471bc628b36ca` |
| `collection/philosophy-study-collection/texts/gutenberg/pg408-the-souls-of-black-folk.txt` | `87f8e832484792b761a510b953d67e3835fa46a9f4231a508bfeb914a98559ca` |

## Independent-review repairs — 20 October 2026

Replaced final A2, A3 and delayed D2 after review identified rehearsed inferential patterns. Updated their separate examiner anchors and retained their IDs, outcome rows, reading extents and minute allocations. Reviewed the replacements against every existing case in Modules 1–8 (worked cases, P1–P8, F1–F7 and essay choices), the H-P/H-F/H-A cases, both example sequences, and all A/B/D/E alternatives. This is an authored distinctness review, not evidence of any particular learner's non-exposure.

| Replaced item | New inferential work | Comparison with the closest existing tasks |
| --- | --- | --- |
| A2 | Test whether a patterned redistributive aim implies coercive maintenance; distinguish a conditional, annual assurance transfer from Rawlsian justification through the original position | P5/examples/B2/E2 compare numerical institutional outcomes, histories or forced maintenance; F5 assesses a private inventor's transfers and a levy. A2 instead asks about jointly authorized conditional transfers and whether expiring participation can secure an ongoing institution. No confiscation surprise or minimum-number ranking is reused. |
| A3 | Interpret reported versus endorsed claims about standards of virtue; assess different appraisal of equally demonstrated reasoning, including equal scores awarded for different reasons | Module 4 worked case/examples/E3 produce or preserve disadvantage through training/access; F4/B3 examine self-relation under an external standard; F6 uses referral access. A3 expressly stipulates equal training and ability, testing the normative appraisal of successful reasoning rather than inferred incapacity, access barriers or a psychological consequence. |
| D2 | Distinguish random assignment of holdings from selection of principles under restricted information; ask what licenses the lottery's domain | The removed delayed case matched examples.md's same-holdings/different-history test. New D2 stipulates just existing holdings and changes the allocation domain to authorized donations. A2 concerns conditional contributions and continuity; B2 concerns pattern maintenance; E2 concerns comparative minima and solidarity. No preceding case tests lottery impartiality against entitlement authority and the original position. |

Corrected F4 and B3 passage boundaries against the local Du Bois text: the paragraph beginning “After the Egyptian and Indian” and ending “torn asunder” includes both double-consciousness and two-ness; the next begins “The history of the American Negro” and ends “in his face.” Examiner notes now reflect the distinction. Verified the revised A3 selection in the linked Gutenberg chapter II: four prose paragraphs beginning “Let us examine this question” and ending “an immortal soul.” Updated the source audit without expanding any claims of edition verification.

Reran `python3 instruction/course-08/check.py`: all reported checks passed (140 baseline hours +8 addition; 480 assessment minutes; three rows; 12 final-form anchors; F1–F7/H-F/H-A; 32 local links). Source-access and empirical-validation limitations remain unchanged. No files outside `instruction/course-08/` were edited in this repair, and no commits, pushes or rendering attempts were performed.
