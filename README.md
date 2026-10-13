# Philosophy course

This private repository holds the current self-directed philosophy curriculum and its preserved source collection. **Start with [Session 1](instruction/course-01/sessions/01.md):** read [OpenStax 2.5](https://openstax.org/books/introduction-philosophy/pages/2-5-reading-philosophy) and Plato's *Euthyphro* [2a up to before 5d](https://persweb.wabash.edu/facstaff/helmang/phi110-1516F/phi110-handouts/Euthyphro.pdf), then write a 120-word paraphrase of Euthyphro's reason for prosecuting his father. The marked reading is online and requires internet access; use the visible Stephanus markers. Save your own untouched attempt and one question for next time.

The [first four session packets](instruction/course-01/README.md) contain readings, outputs, feedback criteria, fresh checks, and next steps. They cover six hours within Course 1 and are **study-ready for that scope, not learner-piloted**. The remaining courses are specified in the [current 14-course curriculum](current/README.md); they are not all authored lesson packets. The [course navigator](current/navigation.html) and [opening reading checklist](current/readiness/course-01.md) are generated from the reading records.

## Which rules apply

The Markdown pages in [current/](current/README.md) are the editable curriculum authority. The September 30 [revised DOCX](Philosophy%20curriculum%20and%20writing%20foundations.docx) and [conversion snapshot](archive/revised-curriculum-pandoc-baseline.md) are preserved baselines. The original fifteen-unit source in [collection/](collection/README.md) is historical and its numerical gates, tutor rules, and public-template instructions are superseded. Use the [active tutor rules](instruction/tutor.md) and [private learner record](instruction/learner-record.md).

The current default route is writing-first, then logic and the core courses, one global-tradition option, one selected area, an advanced seminar, and a capstone. The source baseline estimates 1,890 focused hours for the default route and 1,270 through Course 10; proposed additions and bridges do **not** yet have a verified route-wide total. The program awards no credit or external certification.

The [stopping and continuation milestones](current/milestones.md) describe what each checkpoint actually demonstrates. [Direct route options](current/route-options.md) list prerequisite-compatible combinations and their source-baseline hours. [Optional listening](instruction/audio-handoff.md) has a short text-check handoff; every essential task has a written route.

## Files and rights

- [Source packages](source-packages/) preserve the 14 numbered ZIPs, earlier standalone packs, and separate retrieval-tool source. Bundled workflows are archived, not installed as this repository's CI.
- [Collection](collection/philosophy-study-collection/) holds the extracted private-study reading library. Many third-party readings and audio have no general redistribution permission; the [manifest](philosophy-materials-manifest.txt) and [access gaps](philosophy-access-gaps.txt) describe individual sources and missing material. Keep this repository private. No whole-collection license is asserted.
- [Data](data/course.json) records current reading IDs, editions, assets and bounded opening assignments. [Workload](data/workload.json) records baseline and scoped changes. A future distributable build must use a rights allowlist and exclude restricted readings and private learner work.
- [Unified plan](implementation/UNIFIED_PLAN.md), [implementation status](implementation/STATUS.md), [PC-by-PC register](implementation/TASK_REGISTER.md), [decisions](implementation/DECISIONS.md), and [maintenance procedure](implementation/MAINTENANCE.md) explain scope and limits. Run `python3 scripts/check_course.py` in a clean checkout to check current links, identifiers, hours, and generated views.

Personal work goes in the ignored `learner/` directory. The repository's old source and original packages remain recoverable in Git history; do not publish or share the private reading collection as an anthology.
