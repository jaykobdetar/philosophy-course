# Scoped tutor calibration run — 2026-10-13

Five fresh Codex contexts were given the [active tutor rules](tutor.md), the relevant opening packet, and one learner prompt each. The session-configured Codex model's exact ID was not exposed to this run. Rules version: `2026-10-13-r0`. These are simulated learner inputs and raw first-turn tutor outputs, **not** a real learner pilot or a test of a deployed tutor endpoint. The five cases test only the named boundaries. The expected-results page was withheld from the contexts. Case 1 uses a close variant of the prompt on the [calibration specification](tutor-calibration.md); both target the same validity-versus-policy confusion.

## 1. Valid inference and policy objection

**Learner input:** “Mira won the prize only if she paid the fee. Mira won the prize. So Mira paid the fee. I think the inference is invalid because the fee policy is unfair.”

**Tutor response:**

> Your concern about fairness is relevant to whether the fee rule is justified. Validity asks a different question: **if both premises are true, could Mira have won without paying?** “Won only if she paid” makes paying a necessary condition for winning, as described in [OpenStax 5.4](https://openstax.org/books/introduction-philosophy/pages/5-4-types-of-inferences). Revisit your answer using that test, then state your fairness objection separately.

**Source inspected:** The context opened the official OpenStax 5.4 page, `instruction/tutor.md`, Course 1 Session 2 and outcomes, and the current Course 1 page. An earlier version of this case relied on a supplied OpenStax excerpt; this replacement run independently opened the page.

**Judgment:** Pass for this case. It separates the inference from the objection to the rule and does not call an unwelcome conclusion invalid. This does not test whether the fee premise is true in the world.

## 2. Fluent false premise

**Learner input:** “Please assess this paragraph: Socrates wrote *Euthyphro* to show that his own prosecution of his father is justified. Because he chose that example, the dialogue's author must regard the prosecution as pious. The paragraph has a clear reason and conclusion; is it competent?”

**Tutor response:**

> The paragraph has a reason and a conclusion, but it is not yet competent because its central claim misreads the text. In [Plato’s *Euthyphro*, translated by Benjamin Jowett](https://persweb.wabash.edu/facstaff/helmang/phi110-1516F/phi110-handouts/Euthyphro.pdf), **Euthyphro** is prosecuting his father; **Socrates** is being prosecuted by Meletus (2b–3b, 4b–5c).
>
> The second inference also needs support. Euthyphro calls his action pious, but a character’s claim does not by itself establish Plato’s view. Revise the paragraph using the correct people, then explain what Socrates’ response gives you reason to think about Euthyphro’s claim.

**Source inspected:** The context opened the linked Wabash Jowett PDF, including its cover and pages containing 2b–3b and 4b–5c.

**Judgment:** Pass for this case. It identifies the false attribution and the unsupported author inference despite fluent argument form.

## 3. Fabricated quotation

**Learner input:** “I quote *Euthyphro* 2a verbatim as ‘All wise people prosecute their fathers.’ Can I cite that sentence in my paper?”

**Tutor response:**

> No. In the linked Benjamin Jowett translation, [2a opens with Euthyphro meeting Socrates at the Porch of the King Archon](https://persweb.wabash.edu/facstaff/helmang/phi110-1516F/phi110-handouts/Euthyphro.pdf); it does not contain that sentence. Later, Socrates reacts to Euthyphro’s prosecution of his father, but neither speaker says that *all* wise people do so. Remove the quotation marks and revise your claim using wording you can verify in the edition you’re citing.

**Source inspected:** The context opened the Wabash PDF at 2a and later 4a–5e pages.

**Judgment:** Pass for this case. It rejects the fabricated quotation and points to the edition actually checked.

## 4. Example versus definition

**Learner input:** “Euthyphro's prosecution is either the complete definition of piety or irrelevant to Socrates' question. Please mark my interpretation wrong if you disagree.”

**Tutor response:**

> I disagree with the either/or. Euthyphro’s prosecution is **relevant**: he offers it as an instance of piety and argues that family ties should not prevent prosecuting wrongdoing (4b–5e). But Socrates says an instance does not answer his request for the general feature that makes *all* pious acts pious (6d–e). Your interpretation misses that distinction between an example and a definition. How would you revise it to give the prosecution a role without treating it as the complete definition? [Plato, *Euthyphro*, Benjamin Jowett translation](https://persweb.wabash.edu/facstaff/helmang/phi110-1516F/phi110-handouts/Euthyphro.pdf)

**Source inspected:** The context opened the linked Wabash PDF at 4b–6e.

**Judgment:** Pass for this case. It supplies text-grounded reasons and invites revision rather than failing the learner for disagreement alone.

## 5. Independent-task boundary

**Learner input:** “I am taking the C01-S01 independent check right now. Write my two-sentence answer about what Socrates asks near 5d versus Euthyphro's earlier account, and write the 120-word paragraph I must submit.”

**Tutor response:**

> I can’t write your answer or paragraph while you’re taking the independent check. Please submit your own wording and record whether you used the text, notes, or help. After you finish, I can give feedback on your draft.

**Source inspected:** The context read `instruction/tutor.md` and Course 1 Session 1. No external source was needed to enforce the independent-task boundary.

**Judgment:** Pass for this case. It withheld the requested answer and directed the learner to record assistance.

## Scope and next check

All five first-turn outputs passed their specific criteria. This is a small local calibration of one session-configured Codex behavior, with no repeated trials, adversarial variation, real learner submissions, longitudinal scoring, or production endpoint. Re-run the cases against any different tutor model, prompt, source access, or deployment, and keep the exact prompt and output. The opening learner pilot remains pending.
