# Course 9 verification record

Run from repository root:

```sh
python instruction/course-09/verify.py
python scripts/check_authoring.py --partial
```

The course-owned verifier checks all eight manifest module IDs and paths against the preserved source hour sequence **12, 18, 26, 12, 18, 22, 24, 8**, all per-module budget minute totals, required teaching/task markers, manifest deliverables, internal relative Markdown link targets, fresh/delayed item IDs with separate examiner anchors, addition arithmetic and hashes of the inspected current course/assessment/catalogue/authoring inputs. It is read-only and does not require network or browser access.

The shared checker may report other course workers' incomplete files while authoring proceeds. Its result is a structural coverage check, never source verification or learner evidence. The coordinator owns shared outputs; this worker changes only `instruction/course-09/` and makes no commits or pushes.

**Executed 2026-10-20:** course verifier passed: 8 modules, 140 baseline hours, 0 net added hours, 56 relative Markdown links, reconciled budget minutes, unchanged input hashes and matching fresh/delayed examiner IDs. The shared `--partial` check passed at this checkpoint. `git diff --check -- instruction/course-09` reported no tracked whitespace errors; the new directory was still untracked, so a separate scan of all 23 authored files was also run and found no trailing whitespace. These are structural results, not the pending validations below.

## Authored scope

- Eight full module packets with original explanations, worked cases, bounded practice, independent changed cases, remedies, retrieval and exact next steps.
- All three essential assessment rows mapped; 35/30/25-minute fresh forms and alternate forms; delayed forms reserved inside M08.
- Four bounded essay choices, source dossier procedure, revision steps and route-specific transfer objections.
- Separate tutor/examiner guidance and constructed developing/competent/strong plus draft-to-revision historical interpretation examples.
- Source audit distinguishing inspected older primary passages, live commentary and unverified assigned editions.
- PC-25 causal/modal connection: 1h replacement in M03, net zero; historical baseline unchanged.

## Assessment freshness repair — 2026-10-20

Independent review identified three cases whose reasoning was rehearsed in the teaching/practice corpus. Replaced A-K's fixed display/backward film with a simultaneous causal activity and temporal-gap objection; replaced A-G's excluded-group origin/refutation case with competing explanations of the same public rhetoric and an unestablished historical premise; replaced DB-G's new-current-reasons case with reflexive application of a universal genealogical defeater and an unsupported scientific exemption. Updated their separate examiner anchors and the outcome/form mapping. B-G and DA-G prompts are unchanged; B-G's examiner cross-reference now describes the revised A-G accurately.

The comparison includes all eight modules, their teaching/worked/practice/independent cases, the causal/modal bridge, historical interpretation examples, tutor guidance and all four final forms, checked against the outcome map, README and assessment procedure. The revised demands differ respectively from M03's presentation-order cases, M06's assumed-origin cases and I06/I07-N's independent-current-justification cases. This is a reasoned corpus comparison, not a machine certification of novelty or a claim about a learner's actual exposure. Exposure must still be checked at administration. Source and access gates remain unchanged.

Hours remain **140**, bridge **1h replaced / net 0**, fresh allocations **35/30/25 minutes**, delayed **25+5 minutes** at the shared interval. **Post-repair checks passed:** `python instruction/course-09/verify.py` (8 modules, 140h, net 0, 56 local links, reconciled budgets and unchanged input hashes); `python scripts/check_authoring.py --partial` (18 tracks, 131 distinct module packets, 15 additions at this checkpoint); scoped `git diff --check`. A scan of every Course 9 file also found no trailing whitespace. No browser/rendering action was performed.

## Pending validation

No rendered/browser accessibility QA, FE8/UIT action, human specialist review, learner pilot, actual timing trial, runtime model attestation or new rights clearance. Exact modern-edition reading/quotation checks and Marx version comparison remain dependencies. The current files are complete authored material, not a claim of completed learning or validated instructional effectiveness.
