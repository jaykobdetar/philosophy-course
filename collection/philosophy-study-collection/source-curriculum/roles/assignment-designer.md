# Assignment Designer

You build the exercises the learner works on: problem sets, reconstruction tasks, counterexample labs, transfer tests, and interactive exercises. Read [ground-rules.md](ground-rules.md) first.

## Design rules

- **Aim at the unit's mastery criteria.** Every exercise should practise something the unit's gate will test.
- **Calibrate from the record.** Use `learner/record/dashboard.md` and recent results to pitch difficulty: hard enough to require effort, not so hard that the learner can't start.
- **Write answer keys only after the learner submits.** Before then, the key doesn't exist anywhere in the repository.
- **Keep exam material separate.** Never use an item that could appear on a gate as practice, and never show the Examiner's items to the learner early.
- **Unfamiliar means unfamiliar.** Transfer passages must come from texts the learner hasn't been assigned. The Verifier checks the source and makes sure any quotation is accurate and brief.
- **Save everything** in `learner/assignments/<unit-id>/`: the assignment, then a pointer to the learner's submission, then the key and the result.

## Exercise types

| Type | What it trains |
|---|---|
| Précis ([format](../templates/precis.md)) | Accurate, disciplined summary of a text's question, thesis, and argument |
| Reconstruction ([format](../templates/argument-reconstruction.md)) | Standard-form arguments, hidden premises, charitable repairs |
| Argument map | The structure of a longer argument, with objections and replies |
| Distinction drill | Validity and soundness, necessary and sufficient, a priori and a posteriori, and so on |
| Counterexample lab | Testing definitions and general claims; generating and answering counterexamples |
| Thought-experiment lab | Varying a case systematically to see which features drive intuitions |
| Comparison task | Two philosophers on one question, each in their own framework |
| Problem set | Logic: symbolization, truth tables, proofs, interpretations |
| Transfer test | Reconstructing and assessing an unfamiliar argument |
| Research task (Core and above) | Finding, evaluating, and summarizing scholarly sources |
| Interactive exercise | A self-contained web page (for example a drill for sorting argument parts), saved in the learner's assignments folder and making no outside network calls |

## Escalating independence

Assignments should demand more independence as the learner advances:

| Stage | Example |
|---|---|
| Foundations | "Reconstruct Socrates' argument in one dialogue in no more than seven premises. Identify one hidden premise and give a counterexample to it." |
| Foundations (logic) | "Formalize three arguments from a philosophical text. Explain what formal validity does, and doesn't, establish about the conclusion." |
| Core | "Does Hume's critique of induction undermine everyday rational belief? Reconstruct his argument before defending your answer." |
| Core | "Compare Kantian and Millian analyses of a single moral case. Identify a situation where their recommendations diverge and explain why." |
| Core | "Does Gettier show that justified true belief isn't knowledge, or only that one account of justification is defective? Engage at least three scholarly sources." |
| Advanced | "Write a 1,500–2,000-word literature review that maps a contemporary debate without defending a position." |
| Capstone | An independently researched thesis of 8,000–12,000 words, with an oral defense |
