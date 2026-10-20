# Final integration verification — 2026-10-20

All eleven commands below exited successfully against the completed working tree. The final authoring check ran after the course-specific checks, confirming that the exact accepted inventories still matched. Full outputs are retained in [check results](final-check-results.json).

| Command | Result |
| --- | --- |
| `python3 scripts/check_course.py` | Pass |
| `python3 instruction/course-01/verify.py` | Pass |
| `python3 instruction/course-02/checks/verify.py` | Pass |
| `python3 instruction/course-07/verify.py` | Pass |
| `python3 instruction/course-08/check.py` | Pass |
| `python3 instruction/course-09/verify.py` | Pass |
| `python3 instruction/course-10/check.py` | Pass |
| `python3 instruction/course-11/checks/verify.py` | Pass |
| `python3 instruction/course-13/check_authoring.py` | Pass |
| `python3 instruction/course-14/validate.py` | Pass |
| `python3 scripts/check_authoring.py --reviewed` | Pass |

## Verified scope

- Fourteen course manifests, twenty tracks, 147 distinct baseline module packets and sixteen addition/credit records.
- Independent accepted review records for all fourteen courses, including exact course file lists and SHA-256 digests.
- All seven directly compatible routes; default 1,970 planned hours plus six optional probability hours; conditional Sartre credit and shared foundation counted once.
- Preserved source DOCX/conversion baseline and 214 collection checksums; source module sequences, prerequisites and capstone allocations.
- Local Markdown/HTML links and anchors, source catalogues, generated teaching/source/workload/navigation views and private-path containment rules.
- Course 2 bounded semantic/countermodel checks and Course 10’s 21 exact probability calculations. These do not establish general first-order validity, proof-line correctness or philosophical quality by themselves.

## Local teaching package

`dist/teaching-only.zip` contains 396 allowlisted files. All fourteen manifests are present; every packaged byte matches its current source file; CRC/inventory checks pass. The listed excluded roots and Python caches are absent. The ignored ZIP stays local and is not a new public release.

SHA-256: `14cc7c0761f434bc469796ab41030ad585a2e6e05129d029a078eee349059e44`

Links to deliberately omitted archive/review evidence require the private repository checkout. Packaging is a containment check, not redistribution permission.

## Separate evidence and limits

Independent course and coordinating content reviews are recorded in [progress](PROGRESS_2026-10-20.md) and [review inventories](../data/authoring-reviews.json). Source audits identify actual inspected passages and remaining access/edition dependencies; see [source status](../instruction/source-status.md). No real learner pilot, human specialist certification, empirical timing study, item-level rights clearance or rendered accessibility test was performed. The prior local-navigator browser denial remained in force; no workaround was attempted. FE8 and UIT remain paused.

The final delivery verifies the pushed commit and private GitHub visibility separately. This record describes repository content checks and does not manufacture remote evidence before the push.
