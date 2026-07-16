<!-- AUTHORED: expanded 2026-07-11 -->
# Chapter 15: Algorithmic Complexity and the Search for Generative Equations
## Phase IV: Information, Compression, and Models
### Slides

---

## The Intuition Being Formalized

- Finding the generative equation behind data is a form of compression.
- It is qualitatively different from statistical encoding.
- Your follow-up question (can the search space itself vary?) is a real frontier.
- This chapter installs both, and hands you two impossibility proofs.

## Two Complexities, Two Shelves

> Do not conflate these. It is the most common error here.

- **Kolmogorov / descriptive:** length of the *shortest program*. Size. Uncomputable.
- **Time / computational:** number of *steps* to run. Cost. Computable.
- π's first billion digits: tiny to describe, real work to compute.
- "Complexity" in this chapter always means descriptive.

## What "Program" Means

- Turing (1936): a finite rule table reading and writing a tape.
- Church-Turing thesis: any rote step-by-step procedure fits this.
- Every language, lambda calculus, your laptop: the same class of functions.
- So "program" is structural, not technological, which makes K well-posed.

## Universal Machines And Invariance

- A universal machine simulates any machine from its rule table (your laptop).
- Fix one universal machine U to define shortest-program length.
- Change U, and every length shifts by at most a fixed constant (a translator).
- That constant washes out for large objects: the *invariance theorem*.

## The Halting Problem

- Question: does a given program on a given input halt, or run forever?
- Assume an always-correct decider HALTS. Build saboteur D.
- D asks HALTS about a program run on its own text, then does the opposite.
- Run D on D: whatever HALTS says, D makes it wrong. HALTS cannot exist.

## One Diagonal, Four Results

| Where | Object built to defeat |
|---|---|
| Cantor (Ch 2) | a list of all reals |
| Gödel (Ch 4) | a complete proof system |
| Halting | an infallible decider |
| K (here) | a complexity computer |

- Recipe: assume the decider, build a self-referential defeater, get contradiction.

## Kolmogorov Complexity

> K(x) = min{ |p| : U(p) = x }

- The length of the shortest program that outputs x and halts.
- Structured string ("01" a million times): K is tiny.
- Patternless string: K is about |x| itself (print this exact string).
- Structure is the gap between |x| and K(x). It is machine-independent.

## Randomness = Incompressibility

- A string is *random* when K(x) is close to |x|: no shorter generator.
- A property of the individual object, not of a coin-flipping source.
- Random = maximally complex, because its shortest description is itself.
- Structure lets you say less; randomness forces you to say everything.

## Kolmogorov vs Shannon

- **Shannon entropy:** property of a *source* (a distribution); needs the statistics.
- **Kolmogorov:** property of an *individual object*; needs nothing but the object.
- Related (both count bits) but not the same quantity.
- Shannon is computable. Kolmogorov is not, and that is the price of generality.

## Why K Is Uncomputable

- Assume COMPLEX(x) returns K(x) exactly.
- Build BERRY: print the first string s with COMPLEX(s) > n.
- BERRY's length is about a constant plus log n, so under n for large n.
- But BERRY describes s in under n bits, though s needs over n. Contradiction.
- Berry's paradox made mechanical: same self-reference, fourth appearance.

## Generative Equations Are Short Programs

- Find the rule and you have a short program that regenerates the data.
- Data = output; equation = program; finding it = decompression.
- Logistic `dN/dt = r*N*(1 - N/K)`: two parameters regenerate the whole curve.
- A 40-knot spline is a photograph; the equation is the growth logic.
- Caution (Ch 10): a short rule need not give a long-range prediction (chaos).

## The Search Space Of Equations

- Symbolic regression (Eureqa, PySR) searches a fixed *grammar* of operations.
- You only find equations expressible in the primitives you include.
- Your question: can the grammar itself evolve? (program synthesis, meta-learning).
- Dimensional analysis prunes the grammar honestly, using known units.

## Expressiveness vs Searchability

- Bigger grammar expresses more but is harder to search.
- Expressiveness = descriptive complexity (can it write the equation?).
- Searchability = time complexity (can you find it in time?).
- The collision is your frontier: it is P vs. NP (Ch 5) and open question #4 (Ch 17).
- Powerful move (along the grain) vs brute-force sweep of an exponential space.

## Solomonoff Induction, The Ideal

- Prior on each program p: 2 to the power of minus |p| (shorter = more probable).
- Update on data; the posterior converges on the true generator.
- Bayesian Occam's razor (Ch 14) taken to its logical conclusion.
- Optimal, and uncomputable, so every real method is an approximation.

## The Hierarchy Of Ambition

| Level | Asks for | Captures |
|---|---|---|
| Statistics | a distribution | the source |
| Machine learning | a function | the input-output map |
| Symbolic regression | an equation | the mechanism |
| Solomonoff | a program | the ultimate compression |

- Each rung subsumes the last, is harder, and is more powerful once reached.

## Where You Now Stand

- K is the shortest-program measure; randomness is incompressibility; the ideal is uncomputable.
- Mechanism beats pattern, and your compression intuition sits at the top of the ladder.
> Next: every chapter has leaned on "the right map preserves the structure." Chapter 16, category theory, makes that map itself the object of study.
