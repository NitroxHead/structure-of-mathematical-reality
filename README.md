# The Structure of Mathematical Reality

A self-study curriculum on what mathematics is, what it does when it works, and why it connects to the physical world at all.

This started from a question I could not answer for myself. Mathematics is not one subject but a family of self-contained systems, each built from its own starting axioms, with its own internal logic and its own blind spots. Call them canvases. Following that idea surfaced a sharper question, and the curriculum is built around it: why do some mathematical tools feel disproportionately powerful, a few moves producing exact and sweeping results, while others grind through brute computation for a comparable payoff?

The working hypothesis is that this is not accidental. Certain operations work with the grain of a problem's underlying symmetry, and properties like linearity are not fixed features of a system but artifacts of the relationship between the system and the framework used to describe it.

These lectures are an attempt to formalize and chase that intuition, moving from the standard toolkits (algebra, calculus, linear algebra, probability, topology) toward the structural question of when and why a given canvas fits a given problem. It is aimed at people who already have some mathematical fluency but want the connective tissue between fields, the "why does this work here and not there" layer, rather than another pass through standard course content.

I built this to study from myself and thought it might be useful to others. Corrections and improvements are welcome.

## How it is organized

Seventeen chapters, each a self-contained unit meant to be worked through in one intensive sitting rather than on a fixed weekly schedule. Every chapter carries six documents:

| Document | What it is |
| --- | --- |
| `reading.md` | What to read alongside the chapter, and how far to get |
| `lecture.md` | The core prose: introduces and develops the ideas |
| `notes.md` | A structured template you fill in yourself |
| `exercises.md` | Short problems that test whether the idea landed |
| `assignment.md` | Produce something that demonstrates real understanding |
| `quiz.md` | Application and explanation, not recall |

Chapters run in parallel with outside reading. The main spine is *The Princeton Companion to Mathematics* (PCM), supplemented by Weyl's *Symmetry*, Carter's *Visual Group Theory*, Axler's *Linear Algebra Done Right*, Strogatz's *Nonlinear Dynamics and Chaos*, MacKay's *Information Theory, Inference and Learning Algorithms*, Lawvere and Schanuel's *Conceptual Mathematics*, and a number of individual papers. Each `reading.md` names the specific sections.

## Contents

**Phase I: What Mathematics Is**

1. Mathematics Is Not About Numbers
2. What Numbers Actually Are
3. The Map of Mathematical Fields

**Phase II: Why Mathematics Works**

4. Formal Systems and the Architecture of Proof
5. Symmetry and Invariance: Why Some Operations Are Powerful
6. The Unreasonable Effectiveness Problem

**Phase III: The Grammar of Structure**

7. Groups: The Language of Symmetry
8. Vector Spaces and the Meaning of "Canvas"
9. Topology: Structure Without Measurement
10. Dynamics and Approximation: The Structure of Change

**Phase IV: Information, Compression, and Models**

11. Probability, Universality, and Levels of Description
12. Information Theory and the Cost of Description
13. Measurement: How the World Gets Numbers
14. What a Model Is and Why It Works
15. Algorithmic Complexity and the Search for Generative Equations

**Phase V: The Connective Tissue**

16. Category Theory: The Mathematics of Mathematics
17. Open Questions and the Shape of the Unknown

## Reading it

If you just want to read, take `chapters/chNN-*/lecture.md` in order. The markdown is the source and is meant to be readable on its own.

For typeset PDFs, either grab them from the [Releases](../../releases) page or build them yourself.

## Building

You need Python 3 and a LaTeX distribution providing `pdflatex` (TeX Live or MacTeX).

```
make          # render markdown to LaTeX and compile every chapter PDF
make render   # markdown to LaTeX only, no PDFs
make book     # stitch the 17 lectures into a single build/book.pdf
make clean    # remove LaTeX aux files
make distclean# remove the whole build/ tree
```

Everything lands in `build/`, which is disposable and not tracked. Nothing in `build/` should ever be edited by hand.

## Repository layout

```
curriculum.md          the blueprint: scope, readings, schedule, seed content
chapters/chNN-slug/    the course itself, six markdown documents per chapter
shared/smr-style.sty   LaTeX style shared by every document
scripts/               the markdown to LaTeX pipeline
build/                 generated output (git-ignored)
```

`curriculum.md` is the single source the chapters were seeded from. `make reseed` re-derives chapter markdown from it, but skips any file carrying an `<!-- AUTHORED -->` marker, since those have been expanded well past the blueprint and are first-class content.

## A note on the material

This is a map, not a textbook. It is built for orientation rather than mastery: enough of the terrain that when you hit a wall in your own work, you can locate yourself, ask a better question, and know which direction to move. It does not sacrifice depth for accessibility, and where a question is genuinely open it says so instead of papering over it.

I am not a mathematician. If you find an error, a distortion, or a place where I have oversimplified something into being wrong, please open an issue.

## License

[Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY-SA 4.0). Share it, adapt it, build on it, including commercially, as long as you credit and license derivative work the same way. See [LICENSE](LICENSE).
