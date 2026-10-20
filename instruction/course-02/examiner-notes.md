# Course 2 tutor and examiner guidance — keep closed during attempts

Use [active tutor rules](../tutor.md) and [shared assessment principles](../../current/assessment.md). In practice, begin from the attempt, diagnose one or two consequential errors, demonstrate a different example and fade assistance. During independent work, provide no task-specific hints, solutions, checker results or scores. Record exposure before choosing a form. If an answer is inadvertently revealed, classify the task as practice and use the alternate. These public files cannot enforce secrecy; the learner/examiner must preserve a credible exposure record.

[Practice feedback](practice-solutions.md) covers every assigned conceptual, translation and interpretation task; [proof solutions](proof-solutions.md) gives all 20 TFL and 16 FOL practice derivations. Official textbook feedback is mapped in the practice file. A semantic test of a proof's goal is not verification of the learner's lines. Inspect citations, scope and name restrictions directly. Reject an unsupported tutor verdict; require the relevant rule, row or interpretation.

## Judgment and readiness

For each outcome record: criterion; actual line, phrase or model; source/rule; whether independent; and the next repair. Competent symbolization preserves scope and stated key, not simply grammatical well-formedness. Competent semantics supplies a decisive and fully evaluated witness or an exhaustive/general argument. Competent proof has correct rule instances and no hidden dependence. Competent modeling explains what premise truth and interpretation still require. Strong work transfers across these representations and justifies an ambiguity. Missing evidence is unresolved; repeated scope/witness/discharge errors require repair regardless of other success. An independently noticed transcription slip is recorded differently from a conceptual misconception.

The paper and coached revision cannot replace fresh evidence. Use the four-row [outcome map](outcomes.md), with 30+30+60+20 = 140 minutes for a full form. The explanation exchange and delayed hour are also inside Module 8. Calibrate any deployed tutor using the shared calibration set; neither this authoring run nor automated semantic checks supply a learner pilot or expert endorsement.

## Module independent checks and alternate prompts

**M1-I.** Valid by contraposition of the universal restriction: an archive box would be labeled, contradicting the stated lack of label. Soundness also requires the two premises actually true and the words consistently applied. All labeled and some unlabeled are incompatible. The prewritten jar alternate is also valid; some tagged and none tagged are incompatible. Reject an “invalid because we have not inspected the box” response: that confuses form and truth.

**M2-I.** Expected `S→P`, `¬R→P` (or `P∨R`), `¬(P∧S)`, and `P∨(R∧S)` versus `(P∨R)∧S`. The back-translation says if a permit is issued and review completed, the site opens. Alternate prompt: use F funding approved, E equipment arrives, O office opens. Translate “O only if F,” “E unless O, inclusively,” “neither F nor E,” and two readings of “F and E or O”; back-translate `F→(E∨O)`. Answers: `O→F`, `¬O→E`, `¬F∧¬E`, `(F∧E)∨O` / `F∧(E∨O)`, and if funding is approved then equipment arrives or the office opens. Do not give this paragraph to the learner; supply only the prompt.

**M3-I.** First invalid at P=F,Q=T,R=F (the conditional premise is true, Q true, P false). The two negated-conjunction candidates differ at P=T,Q=F: `¬(P∧Q)` true, `¬P∧¬Q` false. The three-member set is unsatisfiable. Alternate prompt: assess `P↔Q, Q∨R ∴ P`; compare `¬(P∨Q)` with `¬P∨¬Q`; assess `{P→Q,P,¬Q}`. Answers: first invalid at P=Q=F,R=T; pair differs at P=T,Q=F; set unsatisfiable. Require main-operator values, not merely assigned letter values.

**M4-I.** First proof:

```text
1   P → Q                   PR
2 | P ∧ R                   AS
3 | P                       ∧E 2
4 | R                       ∧E 2
5 | Q                       →E 1,3
6 | Q ∧ R                   ∧I 5,4
7   (P ∧ R) → (Q ∧ R)       →I 2–6
```

Second: `1 ¬(P∨Q) PR; 2 | P AS; 3 | P∨Q ∨I 2; 4 | ⊥ ¬E 3,1; 5 ¬P ¬I 2–4`. A closed subproof's interior depends on a discharged assumption; only an applicable range-citing rule can export the result. Alternate prompt: prove `P→Q ⊢ (R∧P)→(R∧Q)` and `¬(P∧Q),P ⊢ ¬Q`. First uses extract R/P, →E, conjoin R/Q, discharge. Second: assume Q, derive P∧Q by ∧I, derive ⊥ with the negated premise, discharge Q by ¬I. These are structurally comparable but the assessor must still check every line of the learner's actual proof.

**M5-I.** Answers: `∀x(R(x)→∃y(P(y)∧H(x,y)))`; `∃y(P(y)∧∀x(R(x)→H(x,y)))`; `∃x((R(x)∧H(x,a))∧∀y((R(y)∧H(y,a))→y=x))`. Uniqueness concerns reviewers who help Ari, not all reviewers. Distinguishing model: four people 0,1 reviewers and 2,3 poets, H={(0,2),(1,3)}. First true, second false. Alternate prompt: domain people, D doctor, M musician, V visits, a Al; translate “no doctor visits every musician,” “each musician is visited by some doctor,” and “at most one doctor visits Al.” Answers: `∀x(D(x)→¬∀y(M(y)→V(x,y)))`; `∀y(M(y)→∃x(D(x)∧V(x,y)))`; `∀x∀y(((D(x)∧V(x,a))∧(D(y)∧V(y,a)))→x=y)`. Ask whether the last formula guarantees a visitor; it does not. Ask for a two-doctor/two-musician diagram making the first two true: doctors 0,1, musicians 2,3, V={(0,2),(1,3)} works. Neither doctor visits every musician, but both musicians have a visitor.

**M6-I.** Countermodel: domain {0,1}, R={(0,0),(0,1)}. Object 0 relates to all, but object 1 does not; the conclusion fails. The second argument is valid: the existential supplies an F-object, and the universal makes that object G. A found countermodel conclusively refutes validity, while no countermodel of size ≤3 only establishes a bounded negative search result. Alternate prompt: refute `∀y∃x R(x,y) ∴ ∃x∀y R(x,y)` and assess `∀x F(x) ∴ ∃x F(x)`. Identity relation on {0,1} refutes the first; the second is valid because the domain is nonempty. Explain the domain convention explicitly.

**M7-I.** First derivation:

```text
1   ∀x(F(x) → G(x))          PR
2   ∃x(F(x) ∧ H(x))          PR
3 | F(c) ∧ H(c)              AS (fresh c)
4 | F(c)                     ∧E 3
5 | H(c)                     ∧E 3
6 | F(c) → G(c)              ∀E 1
7 | G(c)                     →E 6,4
8 | G(c) ∧ H(c)              ∧I 7,5
9 | ∃x(G(x) ∧ H(x))          ∃I 8
10  ∃x(G(x) ∧ H(x))          ∃E 2,3–9
```

Second: `a=b PR; R(a,c) PR; R(b,c) =E 1,2`. While F(c)∧H(c) is open, c is not arbitrary, so ∀I on G(c) is forbidden. Alternate prompt: prove `∀x(F(x)→G(x)), ∀x¬G(x) ⊢ ∀x¬F(x)`, plus `a=b,R(c,a) ⊢ R(c,b)`, and explain the ∀I name restriction. For the first: instantiate both universal premises at fresh c; assume F(c); derive G(c) by →E and ⊥ using ¬G(c); discharge F(c) to get ¬F(c); then generalize to ∀x¬F(x). c must be absent from all open assumptions at the final step. Identity changes the second position only. A learner who generalized merely because the letter was “new” needs explicit active-assumption repair.

## Delayed module retrieval answers

- **M1-D:** a lit lamp 0 and unlit lamp 1 refute the inference to all lit. Two contradictions are both false in every case, hence equivalent, but neither can participate in an all-true case.
- **M2-D:** `B→(G∨K)`. At G=T,K=F, `¬(G∨K)` is false and `¬G∨¬K` true.
- **M3-D:** assuming R false, P∨R forces P true; P↔Q then forces Q true, contradicting ¬Q. Thus valid. ⊨ is an assertion about all valuations, whereas → is a connective evaluated within each valuation.
- **M4-D:** `1 P→Q PR; 2 | ¬Q AS; 3 | | P AS; 4 | | Q →E 1,3; 5 | | ⊥ ¬E 4,2; 6 | ¬P ¬I 3–5; 7 ¬Q→¬P →I 2–6`.
- **M5-D:** `∀x∀y(((S(x)∧A(x,a))∧(S(y)∧A(y,a)))→x=y)`. With no students, antecedents are false, so the universal is true. `¬∀xS(x)` requires at least one nonstudent; `∀x¬S(x)` requires everyone be a nonstudent.
- **M6-D:** domain {0,1}, F={0},G=∅. Object 1 satisfies F→G vacuously, so the premise is true; ∃F true and ∃G false make the conclusion false.
- **M7-D:** `1 ∀x(F(x)→G(x)) PR; 2 ¬∃xG(x) PR; 3 | ∃xF(x) AS; 4 | | F(c) AS; 5 | | F(c)→G(c) ∀E 1; 6 | | G(c) →E 5,4; 7 | | ∃xG(x) ∃I 6; 8 | | ⊥ ¬E 7,2; 9 | ⊥ ∃E 3,4–8; 10 ¬∃xF(x) ¬I 3–9`. c occurs in neither outer assumptions nor exported ⊥.

## M8 paper and explanation exchange

Initial formalization: `∀x(A(x)→P(x)), ∃x(W(x)∧¬A(x)) ∴ ∃x(W(x)∧¬P(x))`. It is invalid. A one-object model with W=P={0}, A=∅ makes both premises true and conclusion false. Respecting autonomy was offered as sufficient for permission; failing it was not offered as sufficient for impermissibility. A repair is `∀x(P(x)→A(x))`, making autonomy necessary as well. Alternatively add `∀x(¬A(x)→¬P(x))`, an equivalent repair in classical logic. Require the learner to identify its substantive strength rather than treating the new premise as free.

The one-place abstraction erases who has autonomy, how it is respected, and the difference between respecting no person and failing an overall autonomy condition. A defensible paper identifies this rather than asserting a false synonymy. Do not impose a preferred ethical verdict. Assess reconstruction, explicit choices, correct countermodel, separately defended repair and source/assistance honesty. For a substituted real passage, check its exact source before judging attribution.

In the exchange, ask: “Which conclusion feature suggested your final rule?” and “Where did the witness cease to appear, and why?” Then remove one premise or reverse one conditional in a proof the learner submitted and ask whether the existing reasoning survives. Use a different challenge from the written task, wait for the response, and record its content. Do not infer mastery from confident delivery.

## Full Form A key

**A1:** (1) `C→(T∧V)`; (2) `∀x(H(x)→∃y(A(y)∧R(x,y)))`; (3) some single artist is recommended by every historian; the shared artist may serve every historian, unlike potentially different witnesses in (2); (4) `∃x(H(x)∧∀y(A(y)→R(x,y)))` versus `∀y(A(y)→∃x(H(x)∧R(x,y)))`. The committee context favors the latter, but does not guarantee that the recommended artists or historians actually exist/behave as claimed. Empty artist extensions also distinguish existence commitments: the second reading need not assert a historian exists.

**A2:** (1) valid. To make Q false while P∨Q true, P must be true; P→R then requires R true, contradicting ¬R. All possible countervaluations are excluded. (2) domain {0,1}, F={0},G={1}: the universal disjunction is true at each object, while both universal disjuncts in the conclusion are false. Check each domain object explicitly.

**A3:**

```text
A3.1
1 | P → (Q → R)                       AS
2 | | P ∧ Q                           AS
3 | | P                               ∧E 2
4 | | Q                               ∧E 2
5 | | Q → R                           →E 1,3
6 | | R                               →E 5,4
7 | (P ∧ Q) → R                       →I 2–6
8   (P → (Q → R)) → ((P ∧ Q) → R)     →I 1–7

A3.2
1   ∀x(F(x) → G(x))          PR
2   ∀x(G(x) → H(x))          PR
3 | F(c)                     AS
4 | F(c) → G(c)              ∀E 1
5 | G(c)                     →E 4,3
6 | G(c) → H(c)              ∀E 2
7 | H(c)                     →E 6,5
8   F(c) → H(c)              →I 3–7
9   ∀x(F(x) → H(x))          ∀I 8
```

At line 9 c no longer occurs in an open assumption and never occurred in a premise. A3.3 violates the condition that the exported conclusion contain no witness name; domain {0,1}, a=0,F={1} gives a countermodel. The existence premise cannot identify a as its witness.

**A4:** “Only accountable decisions are legitimate” is `∀x(L(x)→A(x))`, together with A(a). L(a) does not follow: domain {0}, A={0},L=∅. Adding `∀x(A(x)→L(x))` suffices but is a new substantive sufficiency principle. Check actual applicability and truth separately. A valid repair does not settle the meaning or adequacy of accountability as a criterion.

## Full Form B key

**B1:** (1) `¬¬E→P`, equivalently `E→P`, or `P∨¬E`: if evidence is supplied, the proposal passes; the material reading leaves passage without evidence open. (2) `∃x(M(x)∧∀y(S(y)→T(x,y)))`; (3) every student has some mentor who teaches them, possibly different mentors. Two mentors 0,1 and students 2,3, T={(0,2),(1,3)} make (3) true and (2) false. (4) `∃x((M(x)∧∀y(M(y)→y=x))∧¬T(x,a))` versus `¬∃x((M(x)∧∀y(M(y)→y=x))∧T(x,a))`. With no mentors the first is false and the second true. Critically, a reader must not make uniqueness conditional only on teaching Ari.

**B2:** (1) invalid, P=F,Q=F,R=T; both conditionals and R are true, P false. (2) domain {0,1}, F=G={0}: premises true, ∀G false at 1. ∃G does follow, using the F-witness and the universal implication.

**B3:**

```text
B3.1
1   P ∨ Q                              PR
2 | P → R                              AS
3 | | Q → R                            AS
4 | | | P                              AS
5 | | | R                              →E 2,4

6 | | | Q                              AS
7 | | | R                              →E 3,6
8 | | R                                ∨E 1,4–5,6–7
9 | (Q → R) → R                        →I 3–8
10  (P → R) → ((Q → R) → R)            →I 2–9

B3.2
1   ∃x∀y R(x,y)           PR
2 | ∀y R(c,y)             AS (fresh c)
3 | R(c,d)                ∀E 2
4 | ∃x R(x,d)             ∃I 3
5 | ∀y∃x R(x,y)           ∀I 4
6   ∀y∃x R(x,y)           ∃E 1,2–5
```

d occurs in no premise or open assumption at line 5, so ∀I is allowed inside the witness subproof. c occurs in its own witness assumption but no prior assumption or exported conclusion, so ∃E is allowed. B3.3 fails because its proposed witness name a already occurs in the existential premise. Domain {0,1}, a=0, R={(1,0)} makes `∃x R(x,a)` true but `∃x R(x,x)` false. The absence of a from the conclusion satisfies only one of the three ∃E restrictions; it does not license reusing a name embedded in the premise.

**B4:** `∀x(T(x)→A(x)), ¬T(a) ∴ ¬A(a)` is invalid: one object with T=∅,A={0} refutes it. Adding `∀x(A(x)→T(x))` suffices; it makes transparency necessary for accountability, a separate philosophical assertion. A countermodel establishes failure of formal entailment without asserting any real procedure has these features.

## Delayed D and alternate D′

**D1:** `∃x((R(x)∧¬C(x))∧∀y((R(y)∧¬C(y))→y=x))`. The back-translation says not every reviewed book is catalogued, hence at least one reviewed book is not catalogued; it does not require uniqueness. **D2:** domain {0}, F=∅,G={0}; universal premise true, conditional conclusion false.

**D3:**

```text
1   ∀x(F(x) → G(x))       PR
2   ∃x¬G(x)               PR
3 | ¬G(c)                 AS (fresh c)
4 | F(c) → G(c)           ∀E 1
5 | ¬F(c)                 MT 4,3
6 | ∃x¬F(x)               ∃I 5
7   ∃x¬F(x)               ∃E 2,3–6
```

**D4:** a genuinely rule-correct proof establishes derivability and, using soundness, entailment; a complete TFL table settles the finite truth-functional question; a bounded FOL failure to find a countermodel does not establish general validity. None proves that the chosen key/premises faithfully capture the English case.

**D′ prompts (supply without this answer paragraph):** (1) Domain books; translate “At most one reviewed book is uncatalogued”; explain how it differs from exactly one. (2) Refute `∀x(F(x)→G(x)) ∴ (∀xG(x)→∀xF(x))`. (3) Prove `∀x(F(x)→G(x)), ∃x(F(x)∧H(x)) ⊢ ∃x G(x)` and explain the witness restriction. (4) Explain why a countermodel to an abstract relation-based argument may not refute the original English argument if the relation's transitivity was omitted.

D′ answers: (1) `∀x∀y(((R(x)∧¬C(x))∧(R(y)∧¬C(y)))→x=y)`, allowing none. (2) one object, F=∅,G={0}. (3) assume F(c)∧H(c), extract F(c), instantiate F(c)→G(c), derive G(c), introduce ∃G and discharge the fresh witness. (4) the interpretation may violate the intended relation; add the relevant semantic constraint as a premise and retest, while checking that the English really warrants it. Do not count this as proof that all omitted background assumptions are harmless.
