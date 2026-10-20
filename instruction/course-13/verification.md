# Verification and remaining validation

Run from the repository root:

```bash
python instruction/course-13/check_authoring.py
python -m json.tool instruction/course-13/authoring.json > /dev/null
git diff --check -- instruction/course-13
```

The read-only checker verifies three track records, all required file paths, the shared eight-module hour vector `[10,44,22,16,24,24,10,10]`, 160 hours per selected route, no new addition hours, minimum module structure, relative link targets, and all twelve route transfer prompts/anchors. It does not claim that word count establishes teaching quality. The final worker report records the actual run result.

Manual review checks: every route uses all eight modules; M2 reading allocations each sum to28h within44h; each shared module’s budget sums to its baseline; M7’s30-minute defense is counted once; M7T1 and M8T2 are distinct; M8 reserves30 minutes after roughly4–6weeks or two later modules; outcomes map every Course13 essential row; source audit distinguishes partial-text inspection from metadata and access dependency; no primary full text is redistributed.

These checks cannot establish learner outcomes, expert philosophical review, quotation accuracy in uninspected editions, legal redistribution permission, tutor calibration or rendered visual/accessibility quality. Those remain pending. No browser rendering or workaround was attempted. Model-runtime attestation is unavailable. FE8/UIT remain paused.

## Executed result — 20 October 2026

`check_authoring.py` passed: 3 tracks, shared8-module sequence,160h each,43 local links,12 route transfer forms with examiner anchors. JSON parsing passed. `git diff --check -- instruction/course-13` returned no errors; because newly authored files may be untracked, a direct scan of all Course13 text files also checked trailing whitespace and conflict markers. This is static checking only.

A transient exec-server transport disconnect interrupted one write operation; a subsequent read established that neither target file existed, then the write succeeded. No approval denial or uncertain write remains in this worker scope.
