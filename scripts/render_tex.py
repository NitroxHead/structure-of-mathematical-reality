#!/usr/bin/env python3
"""
Render per-chapter markdown into LaTeX using shared/smr-style.sty.

Source lives in chapters/chNN-slug/*.md and is the only thing you edit.
Output goes to build/chNN-slug/*.tex and is disposable: this file is the
only producer of .tex in the repository, so never hand-edit the result.
Edit the chapter markdown (or curriculum.md), then run:  make

Each chapter builds: reading.tex, lecture.tex, notes.tex,
exercises.tex, assignment.tex, quiz.tex
"""

import json
import os
import re
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
BUILD_DIR = os.path.join(BASE_DIR, "build")

DOCS = ["reading", "lecture", "notes", "exercises", "assignment", "quiz"]
OPTIONAL_DOCS = ["slides", "solutions"]  # rendered only if the .md exists
DOC_TITLES = {
    "reading": "Parallel Reading",
    "lecture": "Lecture",
    "notes": "Note Template",
    "exercises": "Exercises",
    "assignment": "Assignment",
    "quiz": "Quiz",
    "slides": "Slides",
    "solutions": "Solutions and Hints",
}

# ── inline conversion ─────────────────────────────────────────────────────────

SUPERSCRIPT = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5",
               "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁻": "-", "ⁿ": "n",
               "ʳ": "r", "ᵗ": "t"}
SUBSCRIPT = {"₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4", "₅": "5",
             "₆": "6", "₇": "7", "₈": "8", "₉": "9", "ₙ": "n", "ᵢ": "i"}
BLACKBOARD = {"ℕ": r"\N", "ℤ": r"\Z", "ℚ": r"\Q", "ℝ": r"\R", "ℂ": r"\C"}
SIMPLE = {
    "—": "---", "–": "--",
    "→": r"$\to$", "↓": r"$\downarrow$", "↦": r"$\mapsto$",
    "↔": r"$\leftrightarrow$", "·": r"$\cdot$", "×": r"$\times$",
    "÷": r"$\div$", "−": "--", "≈": r"$\approx$", "≠": r"$\neq$",
    "°": r"$^\circ$", "′": r"$'$", "∘": r"$\circ$", "π": r"$\pi$",
    "δ": r"$\delta$", "Σ": r"$\Sigma$", "√": r"$\surd$",
    "≤": r"$\leq$", "≥": r"$\geq$", "∈": r"$\in$", "∞": r"$\infty$",
}
ALLOWED_PASSTHROUGH = set("öäüéèàçëïñóúíáÉ")  # inputenc-utf8 handles these

SUP_RUN = re.compile("[" + "".join(SUPERSCRIPT) + "]+")
SUB_RUN = re.compile("[" + "".join(SUBSCRIPT) + "]+")
BB_WITH_RUN = re.compile("([" + "".join(BLACKBOARD) + "])([" + "".join(SUPERSCRIPT) + "".join(SUBSCRIPT) + "]*)")

LATEX_SPECIALS = {
    "\\": r"\textbackslash{}", "{": r"\{", "}": r"\}", "$": r"\$",
    "&": r"\&", "%": r"\%", "#": r"\#", "^": r"\^{}", "~": r"\~{}",
    "_": r"\_",
}


def unicode_to_latex(s):
    """Replace the (fixed, audited) unicode inventory with LaTeX. Loud on strays."""
    s = s.replace("√2", r"$\sqrt{2}$")

    def bb(m):
        base = BLACKBOARD[m.group(1)]
        run = m.group(2)
        if not run:
            return f"${base}$"
        if run[0] in SUPERSCRIPT:
            return f"${base}^{{{''.join(SUPERSCRIPT[c] for c in run)}}}$"
        return f"${base}_{{{''.join(SUBSCRIPT[c] for c in run)}}}$"

    s = BB_WITH_RUN.sub(bb, s)
    s = SUP_RUN.sub(lambda m: "$^{" + "".join(SUPERSCRIPT[c] for c in m.group(0)) + "}$", s)
    s = SUB_RUN.sub(lambda m: "$_{" + "".join(SUBSCRIPT[c] for c in m.group(0)) + "}$", s)
    for k, v in SIMPLE.items():
        s = s.replace(k, v)

    stray = [c for c in s if ord(c) > 127 and c not in ALLOWED_PASSTHROUGH]
    if stray:
        raise ValueError(f"unmapped non-ASCII characters {sorted(set(stray))!r} in: {s[:120]!r}")
    return s


BLANK_TOKEN = "\x00BLANK\x00"


def inline(s):
    """Full inline pipeline: md-unescape, protect blanks, escape, unicode, md inline."""
    # markdown backslash-escapes used in the corpus (e.g. x\* in ch10)
    s = re.sub(r"\\([*_\[\]()])", r"\1", s)
    # protect fill-in blanks before underscore escaping
    s = re.sub(r"_{3,}", BLANK_TOKEN, s)
    # escape LaTeX specials (backslash handled by the dict; iterate chars)
    s = "".join(LATEX_SPECIALS.get(c, c) for c in s)
    s = unicode_to_latex(s)
    # markdown inline emphasis / code
    s = re.sub(r"\*\*(.+?)\*\*", r"\\textbf{\1}", s, flags=re.DOTALL)
    s = re.sub(r"(?<![*\w])\*([^*\n]+?)\*(?![*\w])", r"\\emph{\1}", s)
    s = re.sub(r"`([^`]+)`", r"\\texttt{\1}", s)
    # straight double quotes -> TeX quotes
    s = re.sub(r'"([^"]*)"', r"``\1''", s)
    s = s.replace(BLANK_TOKEN, r"\underline{\hspace{2.5cm}}")
    return s


# ── house style gate ──────────────────────────────────────────────────────────
# Course prose uses no em or en dashes. Where a sentence wants one, it takes a
# comma, colon, semicolon, or parentheses instead, or it gets split. Hyphens in
# compound words and numeric ranges are fine and are not checked here.

BANNED_CHARS = {"—": "em dash", "–": "en dash"}


def check_style(text, name):
    """Scan the document BODY. The generated header block is exempt: it is
    boilerplate, not prose the reader sees as text."""
    body = strip_generated_header(text)
    offset = text.count("\n") - body.count("\n")
    problems = []
    for i, l in enumerate(body.split("\n")):
        for ch, label in BANNED_CHARS.items():
            if ch in l:
                problems.append(f"{name}:{i + 1 + offset}: {label} ('{ch}') is not used in this project")
                break
    return problems


# ── block parsing ─────────────────────────────────────────────────────────────

def strip_generated_header(text):
    """Drop HTML comments (AUTHORED markers) and the '# Chapter N ... ---'
    header block that split_curriculum.py adds."""
    text = re.sub(r"<!--.*?-->\n?", "", text, flags=re.DOTALL).lstrip("\n")
    m = re.match(r"(?:#.*\n)+\n---\n\n", text)
    return text[m.end():] if m else text


def parse_blocks(text):
    """Parse markdown into a list of (kind, payload) blocks."""
    lines = text.split("\n")
    blocks, i, n = [], 0, len(lines)
    while i < n:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if line.startswith("```"):
            j = i + 1
            while j < n and not lines[j].startswith("```"):
                j += 1
            blocks.append(("code", lines[i + 1:j]))
            i = j + 1
        elif re.match(r"^#{1,4}\s", line):
            level = len(line) - len(line.lstrip("#"))
            blocks.append(("heading", (level, line.lstrip("#").strip())))
            i += 1
        elif re.match(r"^---+\s*$", line):
            blocks.append(("rule", None))
            i += 1
        elif line.lstrip().startswith(">"):
            quote = []
            while i < n and (lines[i].lstrip().startswith(">") or
                             (lines[i].strip() == "" and i + 1 < n and lines[i + 1].lstrip().startswith(">"))):
                quote.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            blocks.append(("quote", parse_blocks("\n".join(quote))))
        elif line.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|?\s*$", lines[i + 1]):
            rows = []
            while i < n and lines[i].startswith("|"):
                if not re.match(r"^\|[\s:|-]+\|?\s*$", lines[i]):
                    rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
                i += 1
            blocks.append(("table", rows))
        elif re.match(r"^[-*]\s+", line):
            items, cur = [], None
            while i < n:
                if re.match(r"^[-*]\s+", lines[i]):
                    if cur is not None:
                        items.append(cur)
                    cur = [re.sub(r"^[-*]\s+", "", lines[i])]
                elif lines[i].startswith(("  ", "\t")) and lines[i].strip():
                    cur.append(lines[i].strip())
                elif not lines[i].strip():
                    # blank line: list continues only if next line is another bullet/indent
                    if i + 1 < n and (re.match(r"^[-*]\s+", lines[i + 1]) or lines[i + 1].startswith("  ")):
                        i += 1
                        continue
                    break
                else:
                    break
                i += 1
            if cur is not None:
                items.append(cur)
            blocks.append(("ul", [" ".join(it) for it in items]))
        elif re.match(r"^\d+\.\s+", line):
            # ordered list; items may span paragraphs until the next top-level "N. "
            items, cur = [], None
            while i < n:
                m = re.match(r"^(\d+)\.\s+(.*)$", lines[i])
                if m and not lines[i].startswith(" "):
                    if cur is not None:
                        items.append("\n".join(cur))
                    cur = [m.group(2)]
                elif cur is not None and (lines[i].strip() == "" or True):
                    # stop if a new non-list block obviously starts (heading/fence/rule)
                    if re.match(r"^(#{1,4}\s|```|---+\s*$)", lines[i]):
                        break
                    cur.append(lines[i])
                i += 1
            if cur is not None:
                items.append("\n".join(cur))
            blocks.append(("ol", items))
        else:
            para = []
            while i < n and lines[i].strip() and not re.match(r"^(#{1,4}\s|```|---+\s*$|\||[-*]\s|\d+\.\s|\s*>)", lines[i]):
                para.append(lines[i].strip())
                i += 1
            blocks.append(("p", " ".join(para)))
    return blocks


# ── block rendering ───────────────────────────────────────────────────────────

def render_blocks(blocks, subhead_style=True):
    out = []
    for kind, payload in blocks:
        if kind == "p":
            m = re.match(r"^\*\*(.+?)\*\*$", payload)
            if subhead_style and m and len(m.group(1)) < 90:
                title = m.group(1).rstrip(":")
                out.append(r"\subsection*{" + inline(title) + "}")
            else:
                out.append(inline(payload) + "\n")
        elif kind == "heading":
            level, txt = payload
            cmd = {1: r"\section*", 2: r"\section*", 3: r"\subsection*"}.get(level, r"\subsubsection*")
            out.append(cmd + "{" + inline(txt) + "}")
        elif kind == "rule":
            out.append(r"\medskip\noindent\textcolor{smrGray}{\hrulefill}\medskip")
        elif kind == "ul":
            out.append(r"\begin{itemize}[itemsep=2pt]")
            for it in payload:
                out.append(r"    \item " + inline(it))
            out.append(r"\end{itemize}" + "\n")
        elif kind == "ol":
            out.append(r"\begin{enumerate}[leftmargin=*, itemsep=6pt]")
            for it in payload:
                body = render_blocks(parse_blocks(it), subhead_style=False).strip()
                if body.startswith("["):
                    body = "{}" + body
                out.append(r"    \item " + body)
            out.append(r"\end{enumerate}" + "\n")
        elif kind == "quote":
            out.append(r"\begin{keyconcept}[title={Aside}]")
            out.append(render_blocks(payload, subhead_style=False))
            out.append(r"\end{keyconcept}" + "\n")
        elif kind == "table":
            ncol = max(len(r) for r in payload)
            colspec = "l" + "X" * (ncol - 1)
            out.append(r"\begin{tabularx}{\linewidth}{" + colspec + "}")
            out.append(r"\toprule")
            head, *rest = payload
            out.append(" & ".join(inline(c) for c in head) + r" \\")
            out.append(r"\midrule")
            for row in rest:
                row = row + [""] * (ncol - len(row))
                out.append(" & ".join(inline(c) for c in row) + r" \\")
            out.append(r"\bottomrule")
            out.append(r"\end{tabularx}" + "\n")
        elif kind == "code":
            out.append(render_template_lines(payload))
    return "\n".join(out)


def writing_rules(count=2, lead="0.8cm"):
    # Leading \par closes any open paragraph (e.g. the question text) so the
    # full-width rules start in vertical mode; without it the first
    # \rule{\linewidth} is appended to the last line of text and overflows the
    # right margin. Each rule ends with \par to stack them as separate lines.
    parts = [r"\par", rf"\vspace{{{lead}}}"]
    for k in range(count):
        parts.append(r"\noindent\rule{\linewidth}{0.4pt}\par")
        if k < count - 1:
            parts.append(r"\vspace{0.55cm}")
    return "\n".join(parts)


def render_template_lines(lines):
    """Render a fenced note-template block: numbered items -> section + fillbox."""
    # drop the "CHAPTER N NOTES: ..." banner line if present
    lines = [ln for ln in lines]
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and re.match(r"^CHAPTER\s+\d+\s+NOTES", lines[0].strip()):
        lines.pop(0)

    items, cur = [], None
    for ln in lines:
        m = re.match(r"^(\d+)\.\s+(.*)$", ln)
        if m:
            if cur is not None:
                items.append(cur)
            cur = {"num": m.group(1), "head": m.group(2), "body": []}
        elif cur is not None:
            cur["body"].append(ln)
    if cur is not None:
        items.append(cur)

    if not items:  # fallback: not a numbered template
        body = "\n".join(r"\texttt{" + inline(ln) + r"}\par" if ln.strip() else r"\vspace{0.4em}"
                         for ln in lines)
        return r"\begin{fillbox}" + "\n" + body + "\n" + r"\end{fillbox}"

    out = []
    for it in items:
        out.append(r"\section*{" + it["num"] + r".\quad " + inline(it["head"].rstrip(":")) + "}")
        out.append(r"\begin{fillbox}")
        body_lines = [b.rstrip() for b in it["body"]]
        while body_lines and not body_lines[-1].strip():
            body_lines.pop()
        # merge multi-line [hints] into single runs (also keeps a bare '['
        # from being eaten as a tcolorbox/item optional argument)
        merged, hint = [], None
        for b in body_lines:
            s = b.strip()
            if hint is not None:
                hint.append(s)
                if s.endswith("]"):
                    merged.append(("hint", " ".join(hint)))
                    hint = None
            elif s.startswith("[") and not s.endswith("]"):
                hint = [s]
            elif s.startswith("[") and s.endswith("]"):
                merged.append(("hint", s))
            elif not s:
                merged.append(("gap", ""))
            else:
                merged.append(("text", s))
        if hint is not None:
            merged.append(("hint", " ".join(hint) + "]"))
        for kind2, s in merged:
            if kind2 == "gap":
                out.append(r"\vspace{0.5em}")
            elif kind2 == "hint":
                out.append(r"{\itshape\color{smrGray} " + inline(s.strip("[]")) + r"}\par\smallskip")
            else:
                out.append(inline(s) + r"\par\smallskip")
        out.append(writing_rules(2, lead="0.9cm"))
        out.append(r"\end{fillbox}")
        out.append(r"\vspace{0.6cm}")
        out.append("")
    return "\n".join(out)


# ── beamer (slides.md) rendering ──────────────────────────────────────────────
# Slide decks use a restricted block set: no tcolorbox environments (article-
# only in smr-style.sty) and no enumitem options (not loaded under beamer).

def render_blocks_beamer(blocks):
    out = []
    for kind, payload in blocks:
        if kind == "p":
            m = re.match(r"^\*\*(.+?)\*\*$", payload)
            if m and len(m.group(1)) < 90:
                out.append(r"\medskip\structure{" + inline(m.group(1)) + r"}\par\smallskip")
            else:
                out.append(inline(payload) + r"\par\medskip")
        elif kind == "heading":
            out.append(r"\medskip\structure{" + inline(payload[1]) + r"}\par\smallskip")
        elif kind == "rule":
            out.append(r"\bigskip")
        elif kind == "ul":
            out.append(r"\begin{itemize}")
            for it in payload:
                out.append(r"    \item " + inline(it))
            out.append(r"\end{itemize}")
        elif kind == "ol":
            out.append(r"\begin{enumerate}")
            for it in payload:
                out.append(r"    \item " + inline(" ".join(it.split("\n"))))
            out.append(r"\end{enumerate}")
        elif kind == "quote":
            out.append(r"\begin{block}{}")
            out.append(render_blocks_beamer(payload))
            out.append(r"\end{block}")
        elif kind == "table":
            ncol = max(len(r) for r in payload)
            out.append(r"{\small\begin{tabular}{" + "l" * ncol + "}")
            out.append(r"\toprule")
            head, *rest = payload
            out.append(" & ".join(inline(c) for c in head) + r" \\")
            out.append(r"\midrule")
            for row in rest:
                row = row + [""] * (ncol - len(row))
                out.append(" & ".join(inline(c) for c in row) + r" \\")
            out.append(r"\bottomrule")
            out.append(r"\end{tabular}}")
        elif kind == "code":
            for ln in payload:
                out.append(r"\texttt{" + inline(ln) + r"}\par" if ln.strip() else r"\smallskip")
    return "\n".join(out)


def render_slides_doc(text, meta):
    """slides.md -> beamer. Every '## Title' line starts a new frame."""
    body = strip_generated_header(text)
    frames, current, preamble_lines = [], None, []
    for line in body.split("\n"):
        m = re.match(r"^##\s+(.*)$", line)
        if m:
            if current is not None:
                frames.append(current)
            current = {"title": m.group(1).strip(), "lines": []}
        elif current is not None:
            current["lines"].append(line)
        elif line.strip():
            preamble_lines.append(line)
    if current is not None:
        frames.append(current)
    if not frames:
        raise ValueError("slides.md contains no '## Frame Title' frames")
    if preamble_lines:
        raise ValueError(f"slides.md has content outside any frame: {preamble_lines[0]!r}")

    parts = [
        f"% AUTO-GENERATED by render_tex.py from {meta['folder']}/slides.md. DO NOT EDIT.\n"
        "% Edit slides.md, then run: make\n"
        r"\documentclass[11pt]{beamer}" + "\n"
        r"\usepackage{smr-style}" + "\n\n"
        rf"\smrchapter{{{meta['chapter']}}}" + "\n"
        rf"\smrchaptertitle{{{inline(meta['title'])}}}" + "\n"
        rf"\smrphase{{{meta['phase']}}}" + "\n\n"
        rf"\title{{{inline(meta['title'])}}}" + "\n"
        rf"\subtitle{{Chapter {meta['chapter']} --- Phase {meta['phase']}: {inline(meta['phase_title'])}}}" + "\n\n"
        r"\begin{document}" + "\n"
        r"\begin{frame}\titlepage\end{frame}" + "\n"
    ]
    for fr in frames:
        parts.append(r"\begin{frame}{" + inline(fr["title"]) + "}")
        parts.append(render_blocks_beamer(parse_blocks("\n".join(fr["lines"]))))
        parts.append(r"\end{frame}" + "\n")
    parts.append(r"\end{document}" + "\n")
    return "\n".join(parts)


# ── document assembly ─────────────────────────────────────────────────────────

PREAMBLE = r"""% AUTO-GENERATED by render_tex.py from {src}. DO NOT EDIT.
% Edit curriculum.md, then run: make
\documentclass[11pt]{{article}}
\usepackage{{smr-style}}

\smrchapter{{{num}}}
\smrchaptertitle{{{title}}}
\smrphase{{{phase}}}
\smrdoctype{{{doctype}}}

\begin{{document}}
\smrtitlepage

"""

QUIZ_PROLOGUE = r"""\begin{openquestion}[title={Before you begin}]
    \textbf{This quiz tests application, not memorisation. Answer in your
    own words.}

    \medskip
    Do not quote the lecture back at yourself. If you find yourself writing
    a phrase you remember reading, stop and rephrase it from your own
    understanding. A short, precise answer in your own language is worth
    more than a long transcription.
\end{openquestion}

\vspace{0.8cm}

"""

QUIZ_EPILOGUE = r"""
\vspace{1.2cm}
\begin{keyconcept}[title={After the quiz}]
    For each answer, ask yourself: \emph{``Did I explain the \textbf{why},
    or did I just state the \textbf{what}?''} If you stated a fact without
    explanation, go back and add the reasoning.

    \medskip
    \textbf{Date:} \rule{4cm}{0.4pt} \qquad
    \textbf{Questions where I want to go deeper:} \rule{5cm}{0.4pt}
\end{keyconcept}
"""

NOTES_PROLOGUE = r"""\begin{keyconcept}[title={How to use this template}]
    Complete these notes \textbf{after} the reading and the lecture.
    The goal is not to copy phrases from the text --- it is to reconstruct
    the ideas in your own language. Leave every item blank on first pass;
    fill it in from memory, then check.
\end{keyconcept}

\vspace{0.8cm}

"""


def render_qa_doc(blocks, rules_per_item):
    """Exercises/quiz: top-level ordered list gets per-item answer space."""
    out = []
    for kind, payload in blocks:
        if kind == "ol":
            out.append(r"\begin{enumerate}[leftmargin=*, label=\textbf{\arabic*.}, itemsep=1.2cm]")
            for it in payload:
                body = render_blocks(parse_blocks(it), subhead_style=False).strip()
                if body.startswith("["):
                    body = "{}" + body
                out.append(r"    \item " + body)
                out.append(writing_rules(rules_per_item, lead="1.0cm"))
                out.append(r"    \vspace{0.4cm}")
            out.append(r"\end{enumerate}")
        else:
            out.append(render_blocks([(kind, payload)], subhead_style=False))
    return "\n".join(out)


def render_doc(doc, text, meta):
    if doc == "slides":
        return render_slides_doc(text, meta)
    body_md = strip_generated_header(text)
    blocks = parse_blocks(body_md)

    parts = [PREAMBLE.format(
        src=f"{meta['folder']}/{doc}.md",
        num=meta["chapter"],
        title=inline(meta["title"]),
        phase=meta["phase"],
        doctype=DOC_TITLES[doc],
    )]

    if doc == "notes":
        parts.append(NOTES_PROLOGUE)
        parts.append(render_blocks(blocks))
    elif doc == "quiz":
        parts.append(QUIZ_PROLOGUE)
        parts.append(render_qa_doc(blocks, rules_per_item=4))
        parts.append(QUIZ_EPILOGUE)
    elif doc == "exercises":
        parts.append(render_qa_doc(blocks, rules_per_item=3))
    else:
        parts.append(render_blocks(blocks))

    parts.append("\n\\end{document}\n")
    return "\n".join(parts)


def main():
    folders = sorted(d for d in os.listdir(CHAPTERS_DIR)
                     if re.match(r"ch\d{2}-", d) and os.path.isdir(os.path.join(CHAPTERS_DIR, d)))
    failures = []
    for folder in folders:
        meta = json.load(open(os.path.join(CHAPTERS_DIR, folder, "metadata.json"), encoding="utf-8"))
        os.makedirs(os.path.join(BUILD_DIR, folder), exist_ok=True)
        optional_present = [d for d in OPTIONAL_DOCS
                            if os.path.exists(os.path.join(CHAPTERS_DIR, folder, f"{d}.md"))]
        for doc in DOCS + optional_present:
            src = os.path.join(CHAPTERS_DIR, folder, f"{doc}.md")
            if not os.path.exists(src):
                failures.append((folder, doc, "missing source md"))
                continue
            try:
                text = open(src, encoding="utf-8").read()
                style = check_style(text, f"{folder}/{doc}.md")
                if style:
                    raise ValueError("; ".join(style[:5]))
                tex = render_doc(doc, text, meta)
            except Exception as e:
                failures.append((folder, doc, str(e)))
                continue
            with open(os.path.join(BUILD_DIR, folder, f"{doc}.tex"), "w", encoding="utf-8") as f:
                f.write(tex)
        extra = f" (+ {', '.join(optional_present)})" if optional_present else ""
        print(f"  {folder}: {len(DOCS) + len(optional_present)} tex files{extra}")

    if failures:
        print("\nFAILURES:")
        for f in failures:
            print("  ", f)
        sys.exit(1)
    print(f"\nRendered {len(folders)} chapters x {len(DOCS)} documents.")


if __name__ == "__main__":
    main()
