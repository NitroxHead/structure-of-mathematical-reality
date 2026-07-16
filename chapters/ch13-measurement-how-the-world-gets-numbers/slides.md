<!-- AUTHORED: expanded 2026-07-11 -->
# Chapter 13: Measurement: How the World Gets Numbers
## Phase IV: Information, Compression, and Models
### Slides

---

## The other half of averaging

- Chapter 11 gave the *statistical* half: averaging needs concentration.
- This chapter gives the deeper half: it applies *before any statistics run*.
- It asks how the world acquires numbers, and which operations on them mean anything.

> Statistical failure: your average is unstable. Measurement failure: your average is not even asking a question the world can answer.

## The first homomorphism

> A measurement scale is itself a homomorphism.

- **Empirical relational structure**: objects plus relations you can observe without numbers (this rod is longer; these two balance that one).
- **Numerical relational structure**: the reals with <, +, times.
- A scale maps one to the other and must *preserve the relations*.
- It is the first structure-preserving map in the pipeline, earlier than all of Phase III.

## Extensive vs intensive

- **Extensive**: you can physically concatenate (length, mass, count, volume). Addition is handed to you; you land near a ratio scale.
- **Intensive**: no such combining (temperature, pH, pain). Measured indirectly or by rank; tops out lower on the ladder.
- Scale type is a readout of how much structure the world actually offers.

## Scale types: the ladder

| Scale | Preserves | Admissible transformations |
| --- | --- | --- |
| Nominal | equality | any relabeling |
| Ordinal | order | any monotone map |
| Interval | differences | x to ax + b, a > 0 |
| Ratio | ratios, true zero | x to ax, a > 0 |

- Up the ladder: more structure, smaller transformation group.

## Admissible transformations form a group

- Ratio: positive reals under multiplication (x to ax).
- Interval: the affine group (x to ax + b), containing ratio.
- Ordinal: all monotone increasing functions, containing affine.
- Nominal: all relabelings (permutations), containing everything.
- Each nests in the next; invariants shrink in lockstep (Chapter 7).

## Sorting your own instruments

- **Ratio**: molar concentration, counts (true zero, can concatenate).
- **Interval**: temperature in °C, pH, qPCR Ct (differences yes, ratios no).
- **Ordinal**: Likert score, tumor grade I to IV (order only).
- **Nominal**: species identity (equality only).
- Ct near the detection limit drifts toward ordinal.

## Meaningfulness = invariance

- A statistic is **meaningful** exactly when its truth is invariant under the scale's admissible transformations.
- This is Noether's logic (Chapter 5) in a new domain.
- If a legal relabeling can change your conclusion, the conclusion was about your numbering, not the world.

## Averaging, re-examined

- **Mean**: needs addition, meaningful for interval and ratio only.
- **Median**: needs only order, meaningful for ordinal too.
- **Ratios / fold-change**: need a true zero, ratio scales only.
- "Averaging fails" (measurement sense): whenever data are not at least interval.

## The mean that reverses

- Grades I to IV coded 1,2,3,4: group A mean 2.8 vs B 2.5, "A worse."
- Recode as 1,2,3,10 (a legal monotone relabeling): the means can flip.
- The patients did not change; only an arbitrary numbering did.
- Fix: compare ranks, medians, or the full distribution, which are invariant.

## Log-fold-change vs mean pH

- Raw concentration is ratio; its admissible group is x to ax (multiplicative).
- Take the log: x to ax becomes an *added constant*, so log-concentration is interval.
- A log-fold-change is a difference on that interval scale: solidly meaningful.
- A mean pH is licensed but subtle: it is a geometric mean of concentration, a different question than average acidity.

## Do not weaponize the taxonomy

- Scale type is not stamped on data; it depends on the question and the empirical operations behind the numbers.
- Ordinal data are often *justifiably* treated as interval when spacing is calibrated.
- Ratio-looking counts can behave ordinally near a limit.

> The taxonomy is a lens for asking "which operations are invariant here?", not a rulebook.

## Same move, two verdicts

- Averaging a *calibrated* summed questionnaire across a large group: defensible (spacing is backed, aggregate concentrates).
- Averaging a single four-point grade across a few patients: fatal (spacing unproven, relabeling flips it).
- What decides is evidence for equal spacing plus robustness to relabeling, not the label "ordinal."

## Where this sits on your map

- Your data are assays, scores, proxies: each a homomorphism into numbers.
- Measurement is the first step of numbers to structure to prediction.
- Get it wrong and it is not noise; it is a *category mistake* every downstream model inherits.
- You cannot out-compute a scale that was never faithful.

## Takeaway and the bridge ahead

> A scale is a homomorphism; its admissible-transformation group fixes which statistics are meaningful; meaningful equals invariant. This completes the averaging question: it can fail for lack of concentration (Chapter 11) or for lack of invariance (here).

- Measurement is the *first* structure-preserving map.
- Chapter 14: a model is the *next* one, so applying math is a chain of such maps.
