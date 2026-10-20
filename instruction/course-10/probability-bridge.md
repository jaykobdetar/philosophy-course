# PC-31 — Needs-based probability support for C10

**Optional support, six additional hours; zero replacement hours.** This implements the existing six-hour seed, not a new compulsory outcome. C10 remains 120h; take this packet once for a 126h total. Prerequisites: count, add, multiply and divide small numbers; a calculator, tactile counters or a spoken table is allowed. No algebraic derivation of Bayes' theorem, calculus, statistical significance test or advanced Bayesian epistemology is required.

Use it when M01's P1 reveals repeated denominator reversal, neglect of base rates, or an unsupported independence assumption. A learner who can explain the denominators and limits can proceed without it. The tutor records the decision and unique credit. If this support was previously completed with equivalent evidence, retain the record rather than bill another six hours. Actual time calibration remains pending.

## Bounded educational reading

Barbara Illowsky and Susan Dean, *Introductory Statistics 2e*, OpenStax, published **13 December 2023**, current HTML consulted 20 October 2026. Read [§3.2](https://openstax.org/books/introductory-statistics-2e/pages/3-2-independent-and-mutually-exclusive-events) from the heading **Independent Events** through the sentence before **Example 3.4**, plus **Example 3.8, its problem and solution only**; then [§3.4](https://openstax.org/books/introductory-statistics-2e/pages/3-4-contingency-tables) from its opening through **Example 3.20's solution**, stopping before **Try It 3.20**. Do not read all of chapter 3 or do every textbook exercise. The source illustrates conditioning as restriction of the relevant group and tables for joint categories; the problems below are original. These bounded passages were inspected. Pages are linked, not copied; live licensing/access notices and versions may change. [Audit](source-audit.md).

## Six-hour allocation

Reading and notation orientation 60 minutes; explained examples 60; practice PB-P 75; feedback and revision 45; independent PB-F or PB-A 45; remediation/consolidation 45; delayed support retrieval PB-D and review 30 = **360 minutes**. PB-D occurs at the start of M03 or about a week later and is charged to this bridge, not to the final course delayed sample. Reading, audio and calculation time all belong inside this allocation; additional access time is logged.

## Teaching: choose the group before the fraction

For an invented inspection population, “faulty given alarm” means select the alarming items first, then count how many selected items are faulty. “Alarm given faulty” starts from the faulty items. A common numerator does not make these the same question. Write the conditioning phrase in full before calculating. A fraction is a relationship within a specified group; moving the fraction to a different population needs an assumption about comparability.

The base rate is the proportion faulty before using the alarm result. When faults are rare, even a fairly good detector may produce many false alarms because so many sound items are tested. This does not make the alarm worthless: it can still raise the probability substantially. Distinguish “raises support” from “establishes certainty.” A negative result similarly needs its own denominator and may leave some residual risk.

For repeated evidence, ask whether the second result adds information beyond the first. Two reports copied from the same sensor are not two independent tests. Even two instruments can share a source of error. Independence of tests *conditional on fault status* is an explicit modeling assumption, not something the word “retest” guarantees. We use counts to show the consequence, without requiring a formula derivation.

## Worked original example W1 — base rate

In an invented population of 10,000 units, 100 are faulty and 9,900 sound. The alarm sounds for 90 faulty and 990 sound units. The table is:

| Status | Alarm | No alarm | Total |
|---|---:|---:|---:|
| Faulty | 90 | 10 | 100 |
| Sound | 990 | 8,910 | 9,900 |
| Total | 1,080 | 8,920 | 10,000 |

The alarm rate among faulty units is 90/100 = 90%. The faulty proportion among alarmed units is 90/1,080 = **1/12**, about **8.33%**. Faults were initially 1%, so this is a substantial increase without a majority of alarms indicating faults. The faulty proportion given no alarm is 10/8,920 = **1/892**, about **0.112%**. For a second population with 1,000 faulty and 9,000 sound and the same 90% detection/10% false-alarm rates, there are 900 true and 900 false alarms, so half the alarms indicate faults. The detector rates are unchanged; the population composition matters.

## Worked original example W2 — repeat evidence

Return to W1. If a second test is conditionally independent with the same rates, both alarms occur for 81 faulty and 99 sound units: 90 × 0.9 and 990 × 0.1. The faulty proportion among double alarms is **81/180 = 45%**. If the “second test” merely duplicates the first result, both-alarm counts stay 90 and 990 and the proportion remains **1/12**. Never multiply marginal probabilities just because two displays show alarms. The contrast depends on a different mechanism, not a smaller arithmetic error.

## Practice PB-P — original inspection exercise

A fictional fleet has 2,000 devices, 40 faulty. A test flags 95% of faulty devices and 5% of sound devices. Assume these proportions correspond to exact counts for this exercise.

1. Complete the 2×2 table and all totals.
2. Calculate P(flag given faulty), P(faulty given flag), and P(faulty given no flag). Name the denominator in words each time.
3. Compare the result to the initial 2% fault rate. Explain in 100 words why useful evidence may still be insufficient for certainty.
4. The fleet manager tests only devices that have already malfunctioned. Explain why the fleet table does not directly give the fault probability among those selected devices; name the missing information.
5. A second dashboard copies the first flag. Explain whether the flag should be counted twice as independent evidence.

Spend 75 minutes, then use 45 minutes of feedback/revision. The tutor may ask “which units are in the given group?” or model an unrelated example. Solutions are in [examiner notes](examiner-notes.md); do not consult them before attempting the table.

## Independent PB-F — reconstructing an unknown base rate (45 minutes)

A fictional population contains exactly 1,000 devices. Exactly 120 flag, and a complete audit of those flagged devices establishes that 72 are faulty and 48 are sound. The total number of faulty devices was initially unknown. For this exercise an independently established detector condition is exact: **90% of all faulty devices in this same population flag**. No further status information is initially supplied about unflagged devices.

Reconstruct the entire 2×2 table, including unflagged faulty and sound counts. Calculate the population's fault base rate, P(faulty given flag), and P(faulty given no flag); explain the different denominators. Then withdraw the 90% detector condition while retaining the flagged audit. Explain whether the population base rate is still uniquely determined, and give the smallest and largest possible faulty counts consistent with the remaining information. This is a problem about recovering and losing information within one population, not transferring a table to another population. Source-open, calculator allowed, no tutor/AI or answer key. Criteria: correct inverse count reasoning, conditional groups, and the consequence of removing an identifying premise.

## Independent PB-A — changed mechanism (45 minutes)

Among 240 devices that already flagged in a first test, 160 are faulty and 80 sound. A second instrument flags 120 of the faulty and 60 of the sound devices. Calculate the fault proportion before and after this second flag, and the second-flag rates conditional on fault and on sound status within this selected group. Does the second flag add discrimination here? Explain why a claim of independence based only on the instruments being different is insufficient, and why these counts cannot establish rates for all unselected retail devices. This changes evidential relevance and conditioning, rather than merely renaming PB-F.

## Delayed PB-D (20-minute response + 10-minute review)

In a fictional maintenance sample, 30 of 300 devices are faulty. All 30 faulty devices and 90 sound devices flag. Of the 120 flagged devices, a verifier selects exactly 15 faulty and 45 sound for review by a method that preserves those proportions. Compute P(faulty given flag) and P(faulty given selected review). Explain why a second selection need not improve diagnostic support and whether a zero false-negative count here proves zero future false negatives. No old solution notes; calculator allowed. This retrieval is separate from the course's final delayed check and charged only to the bridge.

## Repair and return to C10

A denominator mistake: sort cards into the conditioning group, say the fraction aloud, and recalculate. A base-rate mistake: compare true/false positives as counts before percentages. An independence mistake: draw a data-flow diagram or describe who copies what. A population mistake: label the table's sampling frame and write the missing transport assumption. Use the 45-minute consolidation block for the weakest one, then revise a paragraph in P1. If additional support is needed, log the exact skill and extra actual time; do not silently turn six planned hours into an unlimited requirement. Return to M02 with a one-sentence explanation of why evidence can be informative without proving a hypothesis.
