# Course 2 practice feedback — open only after attempting

These are original answer notes. For rule-cited derivations see [proof solutions](proof-solutions.md). Independent checks and assessment answers are separate in [examiner notes](examiner-notes.md). Equivalent formulas are acceptable if their faithfulness is explained; a matching output alone does not show understanding.

## M1 and textbook map

Mandatory textbook feedback routes, all in the pinned local selected-solutions PDF: chapter 1 exercises 1–4 (printed p. 1); chapter 2 A1–A3 and B1/B5 (pp. 2–3); chapter 3 A1/A4, E2 and G4 (pp. 4–6). Chapter/item labels were compared with the local textbook on 20 October 2026. No other numbered textbook item is mandatory. Preserve the useful [opening packet](first-logic-packet.md); this guide completes its surrounding module.

Chapter 3 A1 is contingent: an actual historical truth need not hold in every conceivable case. A4 is necessary under the intended meaning because Caesar's being a crosser supplies someone who crossed. E2 is jointly impossible: four or more giraffes, all Martians, cannot coexist with at most two Martians. G4 is impossible: an argument with a necessary truth as conclusion has no false-conclusion case. These paraphrases explain the relevant reasoning without replacing the source prompts.

O1a is valid: a sealed object cannot be open if the universal premise holds. Soundness remains conditional on actual premise truth. O1b is invalid with a round blue nonred token; adding “every round token is red” makes it valid. The added premise may be false, so the repair does not establish soundness. O1c's claims cannot both hold but are not equivalent: a state with two on makes the first true and the second false. O1d: adding a premise narrows the cases satisfying all premises; it cannot introduce a new countercase to an already valid argument. It may remove all countercases from an invalid one.

## M2 bank

| ID | Answer |
| --- | --- |
| T01 | `L ∧ D` |
| T02 | `¬L` |
| T03 | `D ∨ A` |
| T04 | `¬(L ∧ D)` |
| T05 | `¬L ∧ ¬A` (also `¬(L∨A)`) |
| T06 | `L → D` |
| T07 | `L → D` |
| T08 | `D → L` |
| T09 | `L ↔ A` |
| T10 | `¬A → D` (also `D∨A`) |
| T11 | `(L∨D) ∧ ¬(L∧D)` |
| T12 | `(L∧D) → A` |
| T13 | `L → (D→A)` |
| T14 | `L ∧ ¬A` |
| T15 | `L → (D∧A)` |
| T16 | `(L∨D) → A` |
| T17 | `A → ¬L` |
| T18 | `¬D → ¬A` |
| T19 | `L ↔ ¬D` |
| T20 | `(L∧D)∨A` versus `L∧(D∨A)`; L=F, D=F, A=T distinguishes. |
| T21 | It is false that if the lamp is lit the alarm is armed: materially, the lamp is lit and the alarm is not armed. Main ¬. |
| T22 | The lamp is lit iff the door is locked, and the alarm is not armed. Main ∧. |
| T23 | If the lamp is lit, both the door is locked and the alarm is armed. Main →. |
| T24 | If either the lamp is lit or the door is locked, the alarm is not armed. Main →. |

For T01–20 the outer operator is the main operator: do not identify an interior negation as the main operator of T18. T12 and T13 differ in syntax but are equivalent in classical TFL. The faded example is `D → (L∨A)`. “Only if” points from the sufficient claim to its necessary condition. A reversed answer is diagnosed by the case it forbids, not by word position alone.

## M3 bank

S01 tautology; S02 contradiction; S03 contingent (T,F makes it false; F,F makes it true); S04 tautology. S05 equivalent by De Morgan truth conditions. S06 not equivalent, e.g. P=T,Q=F gives F versus T. S07 equivalent: both are false exactly when P=Q=T and R=F. S08 equivalent: both require matching P,Q.

S09 satisfiable at P=F,Q=T. S10 unsatisfiable: P and `P→Q` force Q, conflicting with `¬Q`. S11 satisfiable at P=Q=R=F. S12 unsatisfiable: P and the biconditional force Q. S13 valid: `¬Q` and the conditional rule out P. S14 invalid at P=F,Q=T: both premises true, conclusion `¬Q` false. S15 valid: if R were false, both conditionals would force P=Q=F, contradicting the disjunction. S16 valid: ¬Q and ¬R make the consequent false, so its conditional requires ¬P. These are semantic arguments; the checker enumerates the relevant rows independently.

Faded answer: Q=F, P=F, satisfiable. S10 concerns a set with no shared satisfying valuation; S02 concerns one formula false on every valuation. The distinctions align but the objects being classified differ.

## M5 bank

The domain and key are as stated in M5. Parentheses around predicate arguments are retained. `≠` abbreviates negated identity.

| ID | Answer |
| --- | --- |
| F01 | `S(a)` |
| F02 | `A(a,b)` |
| F03 | `∀x(S(x)→M(x))` |
| F04 | `∃x(S(x)∧M(x))` |
| F05 | `∀x(S(x)→¬M(x))` |
| F06 | `¬∀x(S(x)→M(x))`, equivalently `∃x(S(x)∧¬M(x))` |
| F07 | `∀x(M(x)→S(x))` |
| F08 | `∀x A(x,a)` |
| F09 | `∃x A(a,x)` |
| F10 | `∀x∃y A(x,y)` |
| F11 | `∃y∀x A(x,y)` |
| F12 | `∃x∀y A(x,y)` |
| F13 | `∀y∃x A(x,y)` |
| F14 | `∀x A(x,x)` |
| F15 | `∀x¬A(x,x)` |
| F16 | `∀x(S(x)→∀y(M(y)→A(x,y)))` |
| F17 | `∃x(S(x)∧∀y(M(y)→¬A(x,y)))` |
| F18 | `¬a=b` |
| F19 | `∀x(¬x=a → A(a,x))` |
| F20 | `∃x∃y((S(x)∧S(y))∧¬x=y)` |
| F21 | `∃x∃y(((S(x)∧S(y))∧¬x=y)∧∀z(S(z)→(z=x∨z=y)))` |
| F22 | `∃x((L(x)∧∀y(L(y)→y=x))∧M(x))` |
| F23 | `∀x(S(x)→∃y(M(y)∧A(x,y)))`; shared witness: `∃y(M(y)∧∀x(S(x)→A(x,y)))`. |
| F24 | Some student admires only Ada (if anyone). It does not assert any admiration; a student with no outgoing arrows satisfies the matrix. |

F21's two witnesses must differ, and every student must equal one of them. Without the last universal, “exactly” becomes “at least.” F22's negation is true if there is no leader or more than one leader, as well as if the unique leader is not a musician. The unique-nonmusician reading asserts a unique leader and is false in the first two cases. For F10–11, adding arrows from both Ada and Bo to Ada makes both formulas true. Faded answer uses ∧ for the existential restriction, → for the universal restriction. An existential quantifier can scope a conjunction; it cannot be dropped because a real-world example feels obvious.

## M6 bank

Unless otherwise stated, constructions use domain `{0,1}`, a=0, b=1; all unlisted predicate instances/tuples are false. Extra names can denote 0 when irrelevant.

- I01: T,T,F,F in the order asked. I02: both true; x=1 witnesses `G∧¬F`. I03: first true (0→1,1→0); second false (no common target).
- I04: F={0}, G={0}; all three claims true, with 1 refuting the universal G. Empty extension and empty domain are different; the domain remains nonempty.
- I05: F={0}, G={1}. Each existential has a witness, but no common witness; conclusion false. Reusing the first witness for the second premise would be unjustified.
- I06: F=∅, G={0}. Premise universally true by false F antecedents; the converse fails at 0.
- I07: R={(0,0),(1,1)}; each object has itself as successor, but neither object is a successor of both. The worked cross-arrow model is also correct. Explain different versus common witnesses.
- I08: domain `{0,1,2}`, a=0,b=1,c=2, R={(0,1),(1,2)}. Add transitivity `∀x∀y∀z((R(x,y)∧R(y,z))→R(x,z))` to block it. Do not assume that property for an arbitrary relation.
- I09: equality model domain `{0}`, a=b=0, F={0}. Inequality model domain `{0,1}`, a=0,b=1,F={0,1}. Having the same listed property does not force identity.
- I10: identity relation is reflexive, symmetric, transitive and antisymmetric. The two cross-arrows are symmetric but not reflexive, not transitive (0→1→0 lacks 0→0), and not antisymmetric (0 and 1 differ).
- I11: for any domain member d, the premise gives both F(d) and G(d); hence F holds of every member. This covers arbitrary interpretations, unlike merely listing small models.
- I12: domain `{0}`, F=G=∅. All F→G instances are true but ∃F is false. The domain cannot be empty; the F-extension can.

Faded task uses F={1}; the existential is true and F(a) false. Require explicit evaluation rather than accepting a promising-looking picture.
