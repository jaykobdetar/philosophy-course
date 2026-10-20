# Course 2 original practice proofs — answer guidance

These are worked derivations in the pinned Calgary calculus. Each line's rule and scope was reviewed during authoring. The local automated checks establish TFL entailments and test finite FOL interpretations; they **do not mechanically verify these derivations**. See [verification limits](checks/README.md). Alternatives are acceptable when every line is legal. Blank lines between sibling subproofs indicate closure; vertical bars show the active assumptions. Do not present these pages during an independent attempt.

## P01–P05

```text
P01
1   P ∧ Q     PR
2   Q         ∧E 1
3   P         ∧E 1
4   Q ∧ P     ∧I 2,3

P02
1   P         PR
2   Q         PR
3   P ∧ Q     ∧I 1,2

P03
1   P → Q     PR
2   P         PR
3   Q         →E 1,2

P04
1   P         PR
2 | Q         AS
3 | P         R 1
4   Q → P     →I 2–3

P05
1 | P         AS
2 | P         R 1
3   P → P     →I 1–2
```

P04's P remains available within the subproof because it is a premise. P05's P is an assumption, discharged at the end: no premise remains.

## P06–P10

```text
P06
1   P → Q       PR
2   Q → R       PR
3 | P           AS
4 | Q           →E 1,3
5 | R           →E 2,4
6   P → R       →I 3–5

P07
1   P ∨ Q       PR
2   P → R       PR
3   Q → R       PR
4 | P           AS
5 | R           →E 2,4

6 | Q           AS
7 | R           →E 3,6
8   R           ∨E 1,4–5,6–7

P08
1   P ↔ Q       PR
2   P           PR
3   Q           ↔E 1,2

P09
1   P → Q       PR
2   Q → P       PR
3 | P           AS
4 | Q           →E 1,3

5 | Q           AS
6 | P           →E 2,5
7   P ↔ Q       ↔I 3–4,5–6

P10
1   P → Q       PR
2   ¬Q          PR
3 | P           AS
4 | Q           →E 1,3
5 | ⊥           ¬E 4,2
6   ¬P          ¬I 3–5
```

P07 cannot stop after its P branch: the Q disjunct might be the true one. P09's two ranges prove the two required directions; citing just the two conditional premises directly as ↔I would not follow the stated basic rule. P10 is an expansion of MT into basic rules.

## P11–P15

```text
P11
1   ¬¬P         PR
2 | ¬P          AS
3 | ⊥           ¬E 1,2
4   P           IP 2–3

P12
1 | P           AS
2 | | Q         AS
3 | | P         R 1
4 | Q → P       →I 2–3
5   P → (Q → P) →I 1–4

P13
1   P           PR
2   ¬P          PR
3   ⊥           ¬E 1,2
4   R           X 3

P14
1   P           PR
2   Q ∨ P       ∨I 1

P15
1   P ∨ Q       PR
2   ¬P          PR
3 | P           AS
4 | ⊥           ¬E 3,2
5 | Q           X 4

6 | Q           AS
7 | Q           R 6
8   Q           ∨E 1,3–5,6–7
```

P11 assumes the negation of the target and closes with IP, not ¬I. P12's inner Q closes before the outer P. P15 explains why DS is safe: the impossible P branch permits Q by explosion, while the Q branch already supplies it.

## P16–P20

```text
P16
1   P → Q           PR
2   Q → R           PR
3   ¬R              PR
4   ¬Q              MT 2,3
5   ¬P              MT 1,4

P17
1   ¬(P ∨ Q)        PR
2   ¬P ∧ ¬Q         DeM 1

P18
1   ¬¬P             PR
2   P               DNE 1
3   P ∨ R           ∨I 2

P19
1   P → R           PR
2   ¬P → R          PR
3 | P               AS
4 | R               →E 1,3

5 | ¬P              AS
6 | R               →E 2,5
7   R               LEM 3–4,5–6

P20
1 | P ∧ Q                 AS
2 | Q                     ∧E 1
3 | P                     ∧E 1
4 | Q ∧ P                 ∧I 2,3
5   (P ∧ Q) → (Q ∧ P)     →I 1–4
```

The P19 use of LEM matches the book's two-subproof rule. P20 is a theorem, unlike P01, whose first line remains an undischarged premise. Their common internal reasoning does not erase that difference.

## Q01–Q04

```text
Q01
1   ∀x(F(x) → G(x))     PR
2   F(a)                PR
3   F(a) → G(a)         ∀E 1
4   G(a)                →E 3,2

Q02
1   F(a)                PR
2   ∃x F(x)             ∃I 1

Q03
1   ∀x F(x)             PR
2   F(c)                ∀E 1
3   ∃x F(x)             ∃I 2

Q04
1   ∀x(F(x) → G(x))     PR
2   ∀x F(x)             PR
3   F(c) → G(c)         ∀E 1
4   F(c)                ∀E 2
5   G(c)                →E 3,4
6   ∀x G(x)             ∀I 5
```

Q03 uses the course's nonempty-domain convention. In Q04 c occurs in neither premise nor any active assumption, so it is arbitrary. Q01 cannot generalize G(a), because F(a) remains a premise.

## Q05–Q08

```text
Q05
1   ∃x F(x)               PR
2   ∀x(F(x) → G(x))       PR
3 | F(c)                  AS
4 | F(c) → G(c)           ∀E 2
5 | G(c)                  →E 4,3
6 | ∃x G(x)               ∃I 5
7   ∃x G(x)               ∃E 1,3–6

Q06
1   ∀x(F(x) ∧ G(x))       PR
2   F(c) ∧ G(c)           ∀E 1
3   F(c)                  ∧E 2
4   ∀x F(x)               ∀I 3

Q07
1   ∀x F(x)               PR
2   ∀x G(x)               PR
3   F(c)                  ∀E 1
4   G(c)                  ∀E 2
5   F(c) ∧ G(c)           ∧I 3,4
6   ∀x(F(x) ∧ G(x))       ∀I 5

Q08
1   ∃x(F(x) ∧ G(x))       PR
2 | F(c) ∧ G(c)           AS
3 | F(c)                  ∧E 2
4 | ∃x F(x)               ∃I 3
5   ∃x F(x)               ∃E 1,2–4
```

For Q05/Q08, c is absent from both the existential premise and the exported conclusion, and from all assumptions open before the witness subproof. For Q06/Q07 the premise list has no c. A witness name in an active assumption is not arbitrary for ∀I.

## Q09–Q12

```text
Q09
1   ∀x¬F(x)               PR
2 | ∃x F(x)               AS
3 | | F(c)                AS
4 | | ¬F(c)               ∀E 1
5 | | ⊥                   ¬E 3,4
6 | ⊥                     ∃E 2,3–5
7   ¬∃x F(x)              ¬I 2–6

Q10
1   ¬∀x F(x)              PR
2   ∃x¬F(x)               CQ 1

Q11
1   a=b                   PR
2   F(a)                  PR
3   F(b)                  =E 1,2

Q12
1   a=b                   PR
2   a=a                   =I
3   b=a                   =E 1,2
```

Q09 c is fresh even relative to the outer existential assumption; ⊥ contains no c and can leave the witness subproof before ¬I closes the outer assumption. Q12 replaces only the first occurrence of a; =E allows selective replacement. =I alone never gives a=b for different names.

## Q13–Q16

```text
Q13
1   a=b                   PR
2   b=c                   PR
3   a=c                   =E 1,2

Q14
1   c=c                   =I
2   ∀x x=x                ∀I 1

Q15
1   ∃x(F(x) ∧ x=a)        PR
2 | F(c) ∧ c=a            AS
3 | F(c)                  ∧E 2
4 | c=a                   ∧E 2
5 | F(a)                  =E 4,3
6   F(a)                  ∃E 1,2–5

Q16
1   ∀x∀y R(x,y)           PR
2   ∀y R(c,y)             ∀E 1
3   R(c,d)                ∀E 2
4   ∀x R(x,d)             ∀I 3
5   ∀y∀x R(x,y)           ∀I 4
```

Q13 uses the allowed reverse direction of =E to replace b by a in line 2. In Q15 choose c different from the a already in the premise; F(a) can be exported because it contains no c. Q16 generalizes c first, then d; both names are absent from the sole premise and all active assumptions.

Bad-proof audits from M7: (i) the generalization name occurs in a premise; domain {0,1}, a=0,F={0} refutes the inference. (ii) ∃E requires a subproof and a name-free exported conclusion; domain {0,1}, a=0,F={1} refutes the proposed inference. (iii) ∀I must replace every occurrence of the arbitrary name in the formula: domain {0,1}, c=0,R={(0,0),(1,1)} makes the premise true and `∀x R(x,c)` false. Renaming a bound variable does not fix partial replacement of c.
