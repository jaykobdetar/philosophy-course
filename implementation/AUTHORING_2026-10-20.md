# Full-course authoring checkpoint — 20 October 2026

The user authorized finishing every course and its option paths on 20 October. That instruction supersedes the earlier authoring stop at the learner-pilot gate. It does not supply learner evidence, expert validation, reading permissions, or rendered accessibility results. Preserve the accepted curriculum and historical source baselines; record amendments and added time explicitly.

Course workers and the substantive curriculum lead/reviewer are launched with the explicit `gpt-6-astra` model request in fresh contexts. The collaboration interface accepts that request but does not expose independent runtime model attestation. The parent execution context coordinates files, checks and commits; it cannot switch its own model through these tools.

## Shared authoring contract

Each course worker owns only `instruction/course-XX/`. Current curriculum pages, source catalogues, archives, root navigation and shared checks remain coordinator-owned. Preserve useful existing files and the four opening sessions. Read the current course page, shared assessment principles, active tutor instructions, relevant addition briefs and original assets as needed. Do not change sharing permissions, contact people, buy texts, copy unauthorized full texts or touch FE8/UIT.

Deliver complete teaching material for every source module, including every option owned by the course number. A module must contain:

1. A guiding question, prerequisites and measurable outcomes.
2. Exact assigned work/edition/range and an honest access note. Inspect sources where available and distinguish a bibliographic check from reading the assigned passage.
3. Substantive teaching explanations: reconstruct the relevant reasoning, explain key terms, distinguish plausible interpretations and common errors. A list of topics or generic instructions to ask a tutor is insufficient.
4. A time allocation inside the source module hours, with reading, practice, feedback, independent work and revision. Account for previously credited opening sessions and later delayed checks.
5. Concrete original exercises, including an explained example during practice, specified outputs and criteria. Provide enough content to attempt the exercise without asking an AI to invent it.
6. An independent changed-case task with permitted assistance/exposure rules, neutral learner criteria and a separate answer/diagnostic section in examiner guidance.
7. Remediation, delayed retrieval and an exact next step.

Create an overall course README, outcome map, course assessment with fresh and delayed forms, separate tutor/examiner guidance, and source-audit record. Essay and research modules need actual decision procedures, templates and bounded tasks, not invented factual conclusions. Courses with paid or unavailable assigned sources can be fully authored while the affected reading tasks remain access-dependent; never imply an unsighted text was verified. Include audiobook-friendly options with written/text-accessible equivalents and citation checks.

Map every essential row in `current/assessment.md` to a named practice artifact and independent fresh task. Use the course-specific grid timings: the generic introduction does not override Course 1's 150-minute written sample or Course 2's 140-minute grid. Provide concrete alternate fresh/delayed prompts with task-specific examiner anchors. The final course delayed sample follows the shared roughly four-to-six-week or two-later-module interval, charged to the prior course; shorter module retrieval does not replace that final occasion. Across the course set, include annotated developing/competent/strong work and draft-to-revision pairs for methods, interpretation, comparison and research.

Course 12 owns PC-28's non-12A language bridge as well as PC-29. Its Frege/Russell foundation reuses the full 20-hour C12A first module; completion is credited once if the learner later takes C12A. A separately budgeted finite Grice packet applies on each route. Course 6 owns the eight-hour Sartre encounter; Course 12C may credit four hours of its 22-hour Module 5 for the same reading and reconstruction when the Course 6 evidence is retained, leaving eighteen hours of new comparative work. These are explicit planning allocations, subject to actual time logs and source compatibility.

Source notes must record the source actually inspected, date, relevant section, supported claim, access/edition limitation and whether quotations/locators were checked. Use official publishers, authors, libraries or primary texts when possible. Link to copyrighted readings; do not reproduce substantial source passages. Original teaching explanations and invented exercise cases are allowed. Label invented examples.

Implement the course's relevant PC-25–33 amendments as finite packets with named readings, tasks, examiner criteria and transparent additional/replaced hours. Keep the historical baseline unchanged. Track overlap credit (especially Sartre/12C and language/12A); do not silently charge twice. If an exact required source truly cannot be established, author the surrounding material and name the precise blocked reading/criterion.

## Machine-readable handoff

Write `authoring.json` in the owned course directory with this structure (paths are repository-relative):

```json
{
  "course_number": 1,
  "authored_on": "2026-10-20",
  "tracks": [{
    "id": "C01",
    "title": "Course title",
    "curriculum_page": "current/courses/01.md",
    "baseline_hours": 120,
    "readme": "instruction/course-01/README.md",
    "outcomes": "instruction/course-01/outcomes.md",
    "assessment": "instruction/course-01/assessment.md",
    "examiner": "instruction/course-01/examiner-notes.md",
    "source_audit": "instruction/course-01/source-audit.md",
    "modules": [{"id": "C01-M01", "path": "instruction/course-01/modules/01.md", "hours": 10}]
  }],
  "additions": [],
  "limitations": []
}
```

Use actual source module hours. Each addition record needs `id`, `pc_task`, `path`, `hours`, `replaces_hours`, `net_hours`, `applies_to`, and `credit_rule`. Explain the budget in prose too. Course 11 owns tracks C11A/B; Course 12 owns C12A/B/C/D; Course 13 owns C13A/B/C and must include the common eight-module 160-hour sequence. Shared files may be referenced from multiple tracks without billing them twice. Course 14 owns its eight milestones.

The final worker report must list files, completed coverage, sources inspected, precise unresolved dependencies and verification performed. Do not commit or push from worker contexts; the coordinator integrates reviewed checkpoints. Do not mark a course piloted or externally validated.
