<!-- AUTHORED: expanded 2026-07-11 -->
# Chapter 2: What Numbers Actually Are
## Phase I: What Mathematics Is
### Slides

---

## Numbers Are Positions, Not Things

> A number is a position in a structure, defined by its relationships, not its substance.

- The number line is a *picture* of one model, not a definition.
- The number 3 = "three steps of successor from the start."
- There is no "3-stuff"; every trio just points at that position.
- This one idea carries the whole chapter.

## Peano: The Interface for ℕ

- Five requirements to *be* the natural numbers:
- A start (0); every element has a unique successor.
- Successor never repeats; 0 is nobody's successor.
- Induction: true at 0 and inherited by successor means true for all.
- It never says what the numbers are *made of*.

## Same Structure, Different Costume

- Tally marks, nested boxes, a hardware counter: all satisfy Peano.
- So all three *are* ℕ; they are *isomorphic*.
- Isomorphism = a perfect, operation-preserving one-to-one translation.
- "Structurally identical" is a precise claim, not a loose analogy.
- Two systems match when an operation-preserving bijection connects them.

## The Chain Is Forced Closure

- Each system fails to *close* under one operation; the next fixes it.
- ℕ → ℤ: close subtraction (3 - 5).
- ℤ → ℚ: close division (3 ÷ 5).
- ℚ → ℝ: fill the holes (limits of huddling sequences).
- ℝ → ℂ: solve every polynomial (x² + 1 = 0).
- ℂ is *algebraically closed*: the process stops here.

## What Each Step Costs

| Step | Buys | Loses |
|---|---|---|
| ℕ → ℤ | subtraction | a floor / least element |
| ℤ → ℚ | division | discreteness (a "next" number) |
| ℚ → ℝ | limits, completeness | countability, nameability |
| ℝ → ℂ | polynomial roots | order (the line) |

> Nothing is free: every gain in closure is paid for in structure.

## Dense But Full of Holes

- ℚ is *dense*: between any two rationals sits another.
- ℚ is *not complete*: huddling sequences point at non-members.
- Newton's method on x² = 2: every iterate rational, limit √2 is not.
- A real number *is* the destination of such a huddling sequence.
- Density = no gaps you can see; completeness = limits land inside.

## The Number Line Is a Partial Portrait

- The reals carry many structures at once:
- field (arithmetic), metric (distance), topology (nearness), order (the line).
- The line shows order and metric; it *hides* algebra and topology.
- Mistaking the projection for the object is the prejudice you sensed.
- ℂ forces the rest into view: no line is possible.

## Complex Multiplication Is Rotation

- Step from ℝ to ℂ: trade the *line* for a *plane*, *order* for *rotation*.
- Multiplying by a complex number = rotate + scale the plane. Literal, not metaphor.
- `cos t + i sin t` is a unit arrow at angle t; multiply to swing by t.
- Euler: `e^(it) = cos t + i sin t`, the machine that turns angles into products.
- This is the phase your Fourier transforms have been tracking all along.

## Why ℂ in Physics, Not Accounting

- ℂ is the native arithmetic of rotation, oscillation, phase.
- Quantum mechanics, circuits, optics, signal processing: all have phase.
- Accounting is one-dimensional ordered magnitude; nothing rotates.
- Presence of ℂ in a theory is a *structural fact* about the phenomenon.
- Where there is phase, reach for ℂ; where only magnitude, ℝ suffices.

## You Cannot Order ℂ

- Any arithmetic-respecting order makes every square non-negative.
- On ℝ that holds: 1 = 1² > 0.
- In ℂ: i² = -1, so a square would be negative. Contradiction.
- So no order compatible with the arithmetic can exist.
- Not a defect: the *price of algebraic closure*, honestly paid.

## Imaginary Is a Misnomer

- ℂ is just the plane ℝ² with a rule for multiplying points.
- i is the point (0, 1); i² = -1 says "two 90° turns face backward."
- Negatives once seemed unreal too ("less than nothing").
- Both are ordinary positions in a well-defined structure.
- "Imaginary" is a historical insult, not a lesser mode of existence.

## Sizes of Infinity: The Pairing Test

- Same size = a bijection: match every element, nothing left over.
- Evens pair with ℕ (n ↔ 2n): whole and part, same size.
- Integers pair with ℕ; even the rationals pair with ℕ.
- Any set listable in one infinite line is *countable*.
- So far, one infinite size for everything.

## Cantor's Diagonal

- Claim: no list can contain all reals in (0, 1).
- Given any list, build a number differing from entry n at digit n.
- It disagrees with every entry somewhere, so the list missed it.
- Works against *any* list: the reals are *uncountable*, a bigger infinity.
- Binary version: flip the nth bit of the nth string.
- Fails on *finite* strings because the built object is infinite.

## Almost Every Real Is Unnameable

- Descriptions (formulas, programs, names) are finite strings: countable.
- Reals are uncountable. Not enough descriptions to go around.
- So *almost every* real has no formula, no name, no algorithm at all.
- Nameable numbers are a countable dust in an uncountable sea.
- The diagonal returns as Gödel (Ch 4) and the halting problem (Ch 15).
- Ch 12: structure = compressibility; the generic real has none.

## Where You Now Stand

- Numbers are forced constructions, not primitives; each closure costs a structure.
- A number is a position; ℕ → ℤ → ℚ → ℝ → ℂ is a narrative, not a taxonomy.
- Infinity comes in sizes; the diagonal bounds proof and computation to come.
> You watched numbers refuse to be one thing. Next, Chapter 3 shows mathematics itself refuses to be one thing, and maps the fields and the borders where the power lives.
