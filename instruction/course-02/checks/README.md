# Verification of Course 2 authored materials

Run from the repository root:

```sh
python3 instruction/course-02/checks/verify.py
```

The standard-library script writes [results.json](results.json). It parses the displayed formula language into syntax trees, evaluates them recursively and performs four distinct checks:

1. Exhaustive TFL valuation checks for all 20 proof goals, the semantic bank, selected translation equivalences, module checks and fresh TFL proof/semantic forms. Negative controls include affirming the consequent and incorrect De Morgan equivalences.
2. Direct evaluation of specified FOL countermodels, relation properties, witness-order examples and description cases. Cardinality translations are compared with ordinary set counts on domains of sizes 1–3.
3. Enumeration of interpretations of sizes **1 and 2** for all 16 FOL practice proof goals and registered fresh/delayed goals. This can detect mistakes; a pass is **not a proof of general FOL validity**. Explicit countermodels elsewhere use the sizes stated in their tasks, including 3 and 4.
4. Manifest/module-hour arithmetic, file existence, local Markdown link targets and source-file SHA-256 fingerprints. Link fragments, remote URLs and rendering are not tested.

This is **not** a natural-deduction proof checker. The source-backed authored derivations include every line/rule/range so a tutor or learner can check them directly; authoring reviewed those rules, citations, scope and name conditions. The semantic evaluator checks their goals independently of that prose. It cannot certify a malformed derivation merely because the conclusion is valid, and it does not check the fidelity of English symbolization. No Carnap or third-party calculus has been tested or made a dependency.

The test is a targeted content check, not learner evidence. Source-ready locally available readings, completed authoring, automated semantic checks, tutor calibration, expert review and pilot success are separate statuses. Only the first three are supported here; actual deployed tutor calibration, learner/expert review and visual/accessibility QA remain pending.
