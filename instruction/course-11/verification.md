# Course 11 verification — 20 October 2026

Run from the repository root:

```bash
python instruction/course-11/checks/verify.py
```

The checker is read-only and uses only Python's standard library. It checks the contract's two track records, eight modules per track, baseline module sequences, existence of referenced files, local Markdown link targets, all 24 final fresh/alternate/delayed form IDs across learner/examiner/outcome files, and the detailed minute ledger. The final assessment allocation includes the delayed sample once. It does not fetch external URLs or render local files.

## Recorded result

- C11A module hours: **10 + 22 + 20 + 16 + 24 + 18 + 22 + 8 = 140**.
- C11B module hours: **14 + 20 + 24 + 20 + 16 + 14 + 24 + 8 = 140**.
- Passing run: **72 local Markdown links and 24 final-form IDs checked**, with no missing targets or form mappings.
- Sixteen module minute allocations reconcile in [timing.json](checks/timing.json).
- Each final assessment: 45m audit + 90m fresh + 20m dialogue + 60m feedback + 90m repair + 60m retest reserve + 25m delayed + 90m final revision/audit = **480m / 8h**.
- Course11 PC-25–33 additional/replaced hours: **0/0**. PC-32 preserves both existing tracks; new encounters are assigned elsewhere.
- Initial checker found a missing verification page and no literal source-dependent status in the assessment rules. Both were corrected before the passing run.

Manual content review checked that every teaching module includes a guiding question, prerequisites, outcomes, a finite reading boundary, substantive explanation, original worked practice, a distinct independent task or the linked final forms, criteria, feedback/repair, retrieval and next step. Shared examiner guidance supplies task-specific anchors for all fourteen module independent tasks, six primary fresh tasks, six alternate fresh tasks and twelve delayed choices. Module8 on each track uses the linked final tasks rather than inventing a seventeenth/eighteenth module.

All course text is newly authored under `instruction/course-11/`; current curriculum, archives, other courses and shared navigation were not changed. No commit or push was performed in this worker context. No browser local-file render, FE8 or UIT action occurred.

## Freshness repair after independent review

Four reviewed cases were replaced without changing their IDs, source ranges, response times or module allocations. The evidence map and separate examiner anchors were updated. The repairs were compared against all module worked examples, practice outputs, independent tasks, response examples, final primary/alternate/delayed forms, dialogue examples and retest-design suggestions. This was a manual inference-level comparison; the structural script does not certify semantic freshness.

| Repaired ID | Repetition removed | Consequential new task |
| --- | --- | --- |
| B8-F2 | Caring newcomer/resident refusing an exclusionary practice, already coached in B4 | Two fully recognized communities impose incompatible legitimate duties. Test the moves from communal formation to unconditional authority and from authority conflict to rejection of communal formation. Recognition and good faith are held fixed. |
| A8-D2 | Spontaneous helping followed by trained reliability, already tested in A6-I | An origin/transmission regress challenges the emergence of the first good teachers. Assess the premise of that regress and the inference that initial moral resources eliminate teaching. This differs from A8-F2/X2’s shaping/intervention analogies and A8-DX2’s recovery in a new environment. |
| B5-I | Historical exclusion through registry/evidentiary access, close to B5 worked practice | A false official textbook legitimates a forced land transfer despite accessible records. Test whether epistemic correction alone achieves material restitution, identify its causal role and a defeater. This differs from the scholarship dependency and Fanon representation cases. |
| B8-DX3 | Inclusive announcement retaining an inherited eligibility list, already worked in B5 | Selective police enforcement prevents one racialized group leaving employers. Test the inference from identical signatures to voluntary cooperation and design a comparison of actual enforcement. This differs from miseducation, admission lists and single-rule repeal. |

The examiner’s retest suggestions were also clarified to avoid recycling already practiced refusal/list/evidence-rule variants. One punctuation error in A6’s source-comparison instruction was corrected; its reading range is unchanged. After these repairs, the verifier again passed both 140-hour tracks, all sixteen minute allocations, 72 local links and 24 final-form IDs. No new source-inspection or empirical-validation claim follows from this repair. Independent recheck remains pending.

## Limits

Structural success does not establish accurate interpretation of unsighted primary editions, actual learner completion time, learning effectiveness, source access rights for every jurisdiction or accessibility. The [source audit](source-audit.md) records inspected passages, bibliographic-only evidence and exact remaining dependencies. Commercial primary reading tasks and related assessment judgments remain source-dependent. Learner pilot, independent subject-expert review, tutor calibration and rendered accessibility testing remain pending. Runtime model attestation is unavailable.
