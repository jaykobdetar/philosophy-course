# Course 2 independent assessment — learner copy

Use only at Module 8. The examiner selects **one wholly unexposed form**, A or B. Do not preview the other form or [answer guidance](examiner-notes.md). Declare previous exposure, outside help and tools. No task-specific tutor help, solutions, search, proof checker or semantic script during the attempt. A blank work log and a sheet listing rule names (without examples) are allowed. Accommodations may change timing/input format, not the independence requirement. Record adjusted time instead of judging speed. Answer every subpart; submit keys, domains, tables/models, line-cited proofs and explanations. The paper and explanation exchange are separate Module 8 artifacts.

Neutral criteria: translations preserve stated scope and vocabulary; semantic evidence evaluates all premises and the conclusion; proofs cite valid rule instances with legal scope/name restrictions; explanations distinguish the model from substantive premise truth. Each of the four families must succeed independently. No overall score compensates for a missing family.

## Form A — 140 minutes

### A1. Symbolization and scope — 30 minutes

1. Key C: a certificate is issued; T: training is completed; V: a visit occurs. Translate: “A certificate is issued only if training is completed and a visit occurs.”
2. Domain people; `H(x)` historian, `A(x)` artist, `R(x,y)` x recommends y. Translate: “Every historian recommends some artist.”
3. Using the same key, back-translate `∃y(A(y) ∧ ∀x(H(x) → R(x,y)))`. Explain how its witness requirement compares with item 2.
4. “A historian recommends every artist.” Give a single-historian reading and a potentially different-historian-for-each-artist reading. Explain which reading you would select in a context where a committee allocates artists to different historians and why that context is not itself a formal proof of the sentence.

### A2. Semantics — 30 minutes

1. Test `P ∨ Q, P → R, ¬R ∴ Q` with a complete truth table or an exhaustive failed-countervaluation argument. Show each relevant premise value.
2. Give a finite countermodel to `∀x(F(x) ∨ G(x)) ∴ (∀x F(x) ∨ ∀x G(x))`. Specify the domain and extensions and explain every quantifier's value. A picture alone is insufficient.

### A3. Proof and restrictions — 60 minutes

1. Prove `⊢ (P → (Q → R)) → ((P ∧ Q) → R)` using chapter 17 rules, with visible nested subproofs.
2. Prove `∀x(F(x) → G(x)), ∀x(G(x) → H(x)) ⊢ ∀x(F(x) → H(x))`. Explain the choice of name at ∀I and its active-assumption condition.
3. A proposed proof reads `∃x F(x) PR; | F(a) AS; | F(a) R; F(a) ∃E`. Explain the exact problem at the last step and give an interpretation showing why the intended conclusion does not follow. This is independent evidence about a rule restriction, not a request to repair the argument by adding a premise.

### A4. Modeling limits — 20 minutes

Invented argument: “Only accountable decisions are legitimate. Decision a is accountable. Therefore it is legitimate.” Domain decisions; A accountable, L legitimate. Give the stated premise's formula, test the inference, and identify one premise that would suffice to repair it. Explain why the repaired inference's validity would not settle whether a is actually legitimate. In 150–250 words, distinguish a mistaken direction of “only” from a substantive dispute about legitimacy.

## Form B — 140 minutes

### B1. Symbolization and scope — 30 minutes

1. Key P: the proposal passes; E: evidence is supplied; D: discussion occurs. Translate: “The proposal passes unless evidence is not supplied,” using the inclusive material reading, and back-translate your result.
2. Domain people; `M(x)` mentor, `S(x)` student, `T(x,y)` x teaches y. Translate: “Some mentor teaches every student.”
3. Translate `∀y(S(y) → ∃x(M(x) ∧ T(x,y)))` into English and compare it with item 2 using a two-mentor/two-student example.
4. “The mentor does not teach Ari,” with `a` Ari. Give a Russell-style reading that asserts a unique mentor and denies that mentor teaches Ari, and a reading denying that there is a unique mentor who teaches Ari. Explain a case distinguishing the readings.

### B2. Semantics — 30 minutes

1. Test `P → Q, Q → R, R ∴ P` and explain a countervaluation if invalid.
2. Refute `∃x F(x), ∀x(F(x) → G(x)) ∴ ∀x G(x)` with a finite interpretation, evaluating all claims. Explain why the corresponding existential conclusion would behave differently.

### B3. Proof and restrictions — 60 minutes

1. Prove `P ∨ Q ⊢ (P → R) → ((Q → R) → R)` using basic rules and cases.
2. Prove `∃x∀y R(x,y) ⊢ ∀y∃x R(x,y)`. Identify the fresh witness name and the arbitrary name, and explain when each can occur in open assumptions.
3. Audit this attempted proof: `1 ∃x R(x,a) PR; 2 | R(a,a) AS; 3 | ∃x R(x,x) ∃I 2; 4 ∃x R(x,x) ∃E 1,2–3`. Give a countermodel to the claimed inference and identify the violated witness restriction, even though a does not occur in the exported conclusion.

### B4. Modeling limits — 20 minutes

Invented argument: “Every transparent procedure is accountable. Procedure a is not transparent. Therefore it is not accountable.” Domain procedures; T transparent, A accountable. Formalize and assess it. Add one substantive premise sufficient to repair the inference, and distinguish an objection to that premise from an objection to a valid inference rule. Explain in 150–250 words what the model cannot determine by itself.

## Delayed Form D — roughly four to six weeks or two later modules later

Allocate 30 minutes for the attempt and 30 for feedback/logging inside Module 8. No rehearsed warm-up or answers. Use D1–D4 as a short sample, prioritizing the least secure family; if all four cannot be meaningfully attempted, record what remains unsampled and allocate additional time transparently. The delayed sample supplements the full fresh form; it does not replace a missing family.

- **D1:** Domain books; `R(x)` reviewed, `C(x)` catalogued, `a` a named book. Translate “Exactly one reviewed book is not catalogued.” Back-translate `¬∀x(R(x) → C(x))`; distinguish its strength from your first answer.
- **D2:** Give a countermodel to `∀x(F(x) → G(x)) ∴ (∃x G(x) → ∃x F(x))` and explain all values.
- **D3:** Prove `∀x(F(x) → G(x)), ∃x¬G(x) ⊢ ∃x¬F(x)`. Explain the witness restriction and the TFL step used inside the subproof. MT is permitted.
- **D4:** Explain why an accepted formal proof, an exhaustive TFL table, and “no FOL countermodel found up to three objects” support different kinds of conclusions. State what none of them establishes about a poorly chosen English key.

If D is exposed, the examiner supplies the concrete alternate D′ prompts from the answer file without showing the answers. If both full forms or both delayed forms are exposed, no claim of independent readiness is made from them. Select genuinely unseen problems from the pinned textbook with inspected answers, recording exact chapter/item IDs; an assessor must check a replacement form before use. No untested generated problem is counted as an approved fresh form.
