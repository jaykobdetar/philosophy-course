# Decisions and corrections

## 2026-10-13 — PC-01 and PC-06 — Current source and baseline

- **Decision:** Preserve the September 30 DOCX and convert its full content to linkable Markdown pages before curricular amendments. The pages in `current/` are the editable source.
- **Course/module:** Whole route; original converted pages retain all 14 courses, choices, 1,890-hour default source baseline, and eight 180-hour capstone milestones.
- **Source:** Original DOCX SHA-256 `27230b5bfd47434c252df8293b305fb1d7cb01a4e97abd5722bad12bb8ba1ee8`; Git baseline `51a35d3`.
- **Task/assessment/budget:** No assignment, gate, or hour change in the conversion. Later adopted proposals use separate records.
- **Validation:** Section inventory and baseline digest recorded in `archive/conversion-map.json`; link and content checks in `scripts/check_course.py`.
- **Limit:** Markdown conversion is a structural preservation check, not a visual reproduction of the original DOCX. Historical source PDFs have separate rights and edition limits.

## 2026-10-13 — PC-02, PC-41 and PC-42 — Authority and private-study boundary

- **Decision:** Treat the fifteen-unit files and original reading packages as recoverable historical/private-study sources. Active entry points and tutor instructions point to the revised course. No whole-collection redistribution license is asserted.
- **Scope:** Private repository only; no visibility change or history rewrite. A future distributable package must use the explicit rights allowlist, not copy the entire collection.
- **Validation:** Existing original bytes and Git history are retained; tracked-file and permission checks are scope-limited to the new distributable route.
- **Limit:** Historical restricted assets are still present in the private Git history. Public publication remains out of scope and would require a separate review and decision.

## 2026-10-13 — PC-31 and PC-37 — Practical reasoning within Course 1

- **Decision:** Add OpenStax 5.5 and a two-hour assumptions, relevance and near-case packet within Course 1 Module 2. Reallocate two hours of its previously unassigned remaining practice time; retain all six reconstructions, four condition tests and the 200-word output.
- **Source:** OpenStax 5.5 and the revised DOCX's eight-hour Module 2, checked on 2026-10-13. Reading ends at the end of section 5.5.
- **Task/assessment/budget:** `C01-M02-PRACTICAL`, roughly 0.5 hour reading, 1 hour practice, 0.5 hour feedback/revision. Two hours replaced within the module; net addition zero to C01's 120-hour baseline. Actual learner time remains unmeasured.
- **Validation:** Named source, task, feedback and workload ledger; pilot pending. The route-wide revised total remains unpublished until other additions and selected bridges are specified.

## 2026-10-13 — PC-11 and PC-13 — Source description corrections

- **Decision:** Correct the Patrick/Sextus classification in the current Course 3 and access pages, and record the Aquinas, Pryor, Bennett, Descartes and Wittgenstein distinctions in `current/readiness/source-corrections.md`.
- **Source:** Local Gutenberg 17556 and 17611 TXT files; local Descartes filenames; revised DOCX Course 1 and Course 4; archived manifest rows CAT-005, 012, 015, 017 and 023. Wittgenstein replacement URL remains unverified.
- **Task/assessment/budget:** No new required reading or hour change. Aquinas objection/reply is inside the already assigned article; Patrick is not substituted for Annas/Barnes.
- **Validation:** Local file headings and relevant article boundaries inspected. Future-source access remains pending before later packet release.
