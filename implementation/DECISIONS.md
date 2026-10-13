# Decisions and corrections

## 2026-10-13 — PC-04, PC-15–24 and PC-44 — Opening authority and assessment calibration

- **Decision:** Make the four Course 1 session packets canonical by replacing duplicated course-page summaries with direct links. Keep form-specific answers in examiner notes and only neutral criteria in the learner assessment.
- **Source:** Revised DOCX conversion and the current Session 1–4 packets; OpenStax 5.4 supplies the Session 3 validity reading. The conversion audit records four additional named summary replacements.
- **Validation:** Local preservation and course checks pass. Five fresh Codex contexts tested bounded tutor cases; exact prompts, outputs, source access and judgments are in the [run record](../instruction/tutor-calibration-run-2026-10-13.md).
- **Limit:** The five cases do not establish production tutor reliability or substitute for a learner pilot. Re-run against any different deployed tutor.

## 2026-10-13 — PC-45 — Opening navigator accessibility check

- **Scope:** Bounded static keyboard, narrow-screen, and print inspection of `current/navigation.html` only.
- **Evidence:** All 33 anchors have `href`; none has a negative tab order. A skip link targets the unique `main` ID, and the document has one `nav` and one `main`. The page declares a viewport, visible focus styling, fluid body width with padding, and print rules; the course checker validates local links.
- **Limit:** Chrome headless could not start in this sandbox, and browser UI policy blocked opening the local `file:` page. No rendered reflow, keyboard traversal, or print-preview result is claimed. Those manual checks remain in PC-45 before a broader accessibility claim.

## 2026-10-13 — PC-07 and PC-44 — Later assignment metadata

- **Decision:** Extract the current later-course module headings, baseline hours, and assignment text into a structured [source assignment catalogue](../data/assignment-catalogue.json). Record the three Course 13 seminar paper prompts as course-level prompts because those pages have no module timetable.
- **Source:** `current/courses/02.md` through `14.md`, excluding aggregate option overview pages and the separately handled Course 1. Every record has a source page and line. The 127 module allocations sum to each page's baseline hours; the three seminar prompts have no invented hours.
- **Validation:** `scripts/build_assignment_catalogue.py --check` and `scripts/check_course.py` compare all 130 records with their source pages and check unique IDs and per-course module hour totals.
- **Limit:** This preserves existing assignment metadata. It does not assert that later reading editions, assets, passage boundaries, permissions, or teaching packets are ready.

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

## 2026-10-13 — PC-03, PC-07, PC-09, PC-37 and PC-44 — Prerequisites and opening inference source

- **Decision:** Reconcile structured course prerequisites with the preserved prose, including Course 2's module-level entry, Course 5 induction before Course 10, and the general Course 11/12 gates for each seminar. Generate the seven directly compatible option routes and check their source-baseline hours. Correct Course 1 Session 3 to OpenStax 5.4 for deductive validity and give a separate soundness explanation grounded in *forall x: Calgary* chapter 2 §2.4.
- **Scope:** Source-baseline route model and opening Session 3; later routes still require source and workload verification before release.
- **Source:** September 30 DOCX and OpenStax 5.4, inspected 2026-10-13; local *forall x: Calgary* Fall 2025 revision `c5cb415`.
- **Task/assessment/budget:** The Session 3 reading changes within its existing 90-minute session. No change to the 1,890-hour source baseline or the PC-31 net-zero allocation. Measured learner time is pending.
- **Validation:** `scripts/check_course.py` checks route compatibility, option hours, bounded opening locators and conversion preservation.

## 2026-10-13 — PC-02, PC-03, PC-42 and PC-43 — Legacy HTML migration

- **Decision:** Add a prominent current-course notice to START_HERE and all thirteen PART HTML entry points; replace the stale private Library download link in START_HERE. Keep full original HTML bytes and original checksum manifest in `archive/legacy-html-originals/`, along with the unchanged source ZIPs in Git history.
- **Scope:** Entry-point migration within the private repository, no public distribution or history rewrite.
- **Validation:** All 214 active collection checksum entries match after the edit; archived START_HERE matches original SHA-256 `982ceebdd367a7c5c7d22085450e174d385e6b0782dc09ebc874371cbc19b2fe`.
