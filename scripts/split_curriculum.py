#!/usr/bin/env python3
"""
Split curriculum.md into per-chapter markdown files organized in folders.
Each chapter gets: lecture.md, notes.md, exercises.md, assignment.md, quiz.md, reading.md
"""

import re
import os
import textwrap

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHAPTERS_DIR = os.path.join(BASE_DIR, "chapters")
CURRICULUM = os.path.join(BASE_DIR, "curriculum.md")

# Chapter metadata: number, slug, title, phase
CHAPTERS = [
    (1,  "mathematics-is-not-about-numbers",          "Mathematics Is Not About Numbers",                        "I",   "What Mathematics Is"),
    (2,  "what-numbers-actually-are",                  "What Numbers Actually Are",                               "I",   "What Mathematics Is"),
    (3,  "the-map-of-mathematical-fields",             "The Map of Mathematical Fields",                          "I",   "What Mathematics Is"),
    (4,  "formal-systems-and-the-architecture-of-proof","Formal Systems and the Architecture of Proof",           "II",  "Why Mathematics Works"),
    (5,  "symmetry-and-invariance",                    "Symmetry and Invariance: Why Some Operations Are Powerful","II",  "Why Mathematics Works"),
    (6,  "the-unreasonable-effectiveness-problem",     "The Unreasonable Effectiveness Problem",                  "II",  "Why Mathematics Works"),
    (7,  "groups-the-language-of-symmetry",            "Groups: The Language of Symmetry",                        "III", "The Grammar of Structure"),
    (8,  "vector-spaces-and-the-meaning-of-canvas",    "Vector Spaces and the Meaning of \"Canvas\"",             "III", "The Grammar of Structure"),
    (9,  "topology-structure-without-measurement",     "Topology: Structure Without Measurement",                 "III", "The Grammar of Structure"),
    (10, "dynamics-and-approximation",                 "Dynamics and Approximation: The Structure of Change",     "III", "The Grammar of Structure"),
    (11, "probability-universality-and-levels",        "Probability, Universality, and Levels of Description",    "IV",  "Information, Compression, and Models"),
    (12, "information-theory-and-the-cost-of-description","Information Theory and the Cost of Description",       "IV",  "Information, Compression, and Models"),
    (13, "measurement-how-the-world-gets-numbers",     "Measurement: How the World Gets Numbers",                 "IV",  "Information, Compression, and Models"),
    (14, "what-a-model-is-and-why-it-works",           "What a Model Is and Why It Works",                        "IV",  "Information, Compression, and Models"),
    (15, "algorithmic-complexity-and-generative-equations","Algorithmic Complexity and the Search for Generative Equations","IV","Information, Compression, and Models"),
    (16, "category-theory",                            "Category Theory: The Mathematics of Mathematics",         "V",   "The Connective Tissue"),
    (17, "open-questions-and-the-shape-of-the-unknown","Open Questions and the Shape of the Unknown",             "V",   "The Connective Tissue"),
]


def read_curriculum():
    with open(CURRICULUM, "r", encoding="utf-8") as f:
        return f.read()


def extract_chapter_blocks(text):
    """Split the full text into per-chapter raw blocks."""
    # Each chapter starts with ### Chapter N:
    pattern = r'### Chapter (\d+): '
    splits = list(re.finditer(pattern, text))

    blocks = {}
    for i, match in enumerate(splits):
        ch_num = int(match.group(1))
        start = match.start()
        end = splits[i + 1].start() if i + 1 < len(splits) else len(text)
        blocks[ch_num] = text[start:end].strip()

    return blocks


def extract_section(block, section_name):
    """Extract a named section from a chapter block.

    Sections are delimited by **Section Name** on its own line (after ---).
    """
    if section_name == "reading":
        # Reading is the first part: from chapter header to first ---\n\n**Lecture**
        # Extract Parallel Reading paragraphs
        reading_match = re.search(
            r'\*\*Parallel Reading\*\*:(.+?)(?=\n---\n)',
            block, re.DOTALL
        )
        if not reading_match:
            # Try without the --- delimiter
            reading_match = re.search(
                r'\*\*Parallel Reading\*\*:(.+?)(?=\n\n\*\*Lecture\*\*)',
                block, re.DOTALL
            )
        if reading_match:
            reading_text = reading_match.group(0).strip()
            # Also grab any "Also read:" lines
            also_pattern = r'Also read.*?(?=\n---|\n\n\*\*Lecture\*\*)'
            also_matches = re.findall(also_pattern, block, re.DOTALL)
            if also_matches:
                for a in also_matches:
                    if a.strip() not in reading_text:
                        reading_text += "\n\n" + a.strip()
            return reading_text
        return ""

    if section_name == "lecture":
        # From **Lecture** to the next ---\n\n**Note Template**
        match = re.search(
            r'\*\*Lecture\*\*\n\n(.+?)(?=\n---\n\n\*\*Note Template\*\*)',
            block, re.DOTALL
        )
        return match.group(1).strip() if match else ""

    if section_name == "notes":
        # From **Note Template** to ---\n\n**Exercises**
        match = re.search(
            r'\*\*Note Template\*\*\n\n(.+?)(?=\n---\n\n\*\*Exercises\*\*)',
            block, re.DOTALL
        )
        return match.group(1).strip() if match else ""

    if section_name == "exercises":
        # From **Exercises** to ---\n\n**Assignment**
        match = re.search(
            r'\*\*Exercises\*\*\n\n(.+?)(?=\n---\n\n\*\*Assignment)',
            block, re.DOTALL
        )
        return match.group(1).strip() if match else ""

    if section_name == "assignment":
        # From **Assignment** to ---\n\n**Quiz**
        # Handle both "**Assignment**" and "**Assignment (Final)**"
        match = re.search(
            r'\*\*Assignment(?:\s*\(Final\))?\*\*\n\n(.+?)(?=\n---\n\n\*\*Quiz)',
            block, re.DOTALL
        )
        return match.group(1).strip() if match else ""

    if section_name == "quiz":
        # From **Quiz** to end of block (or next ---)
        match = re.search(
            r'\*\*Quiz(?:\s*\(Final\))?\*\*\n\n(.+?)(?=\n---\n---|$)',
            block, re.DOTALL
        )
        return match.group(1).strip() if match else ""

    return ""


def is_authored(path):
    """True if the file opts out of reseeding via an AUTHORED marker.

    Authored files (expanded lectures, slide decks, solutions) are first-class
    content owned by the chapter folder, not derived from curriculum.md.
    They carry '<!-- AUTHORED ... -->' near the top and are never overwritten.
    """
    if not os.path.exists(path):
        return False
    with open(path, "r", encoding="utf-8") as f:
        return "<!-- AUTHORED" in f.read(400)


def write_chapter_files(ch_num, slug, title, phase, phase_title, block):
    """Write all markdown files for a single chapter."""
    folder_name = f"ch{ch_num:02d}-{slug}"
    folder_path = os.path.join(CHAPTERS_DIR, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    sections = {
        "reading":    extract_section(block, "reading"),
        "lecture":    extract_section(block, "lecture"),
        "notes":      extract_section(block, "notes"),
        "exercises":  extract_section(block, "exercises"),
        "assignment": extract_section(block, "assignment"),
        "quiz":       extract_section(block, "quiz"),
    }

    # Metadata header for each file
    def header(doc_type):
        return (
            f"# Chapter {ch_num}: {title}\n"
            f"## Phase {phase}: {phase_title}\n"
            f"### {doc_type}\n\n"
            f"---\n\n"
        )

    skipped = []
    doc_map = [
        ("reading.md", "Parallel Reading", "reading"),
        ("lecture.md", "Lecture", "lecture"),
        ("notes.md", "Note Template", "notes"),
        ("exercises.md", "Exercises", "exercises"),
        ("assignment.md", "Assignment", "assignment"),
        ("quiz.md", "Quiz", "quiz"),
    ]
    for fname, doc_title, key in doc_map:
        path = os.path.join(folder_path, fname)
        if is_authored(path):
            skipped.append(fname)
            continue
        with open(path, "w", encoding="utf-8") as f:
            f.write(header(doc_title))
            f.write(sections[key] + "\n")
    if skipped:
        print(f"  ch{ch_num:02d}: preserved AUTHORED files: {', '.join(skipped)}")

    # Write metadata.json for agents to consume
    import json
    meta = {
        "chapter": ch_num,
        "slug": slug,
        "title": title,
        "phase": phase,
        "phase_title": phase_title,
        "folder": folder_name,
        "files": ["reading.md", "lecture.md", "notes.md", "exercises.md", "assignment.md", "quiz.md"]
    }
    with open(os.path.join(folder_path, "metadata.json"), "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    return folder_name, sections


def main():
    text = read_curriculum()
    blocks = extract_chapter_blocks(text)

    print(f"Found {len(blocks)} chapter blocks\n")

    results = []
    for ch_num, slug, title, phase, phase_title in CHAPTERS:
        if ch_num not in blocks:
            print(f"  WARNING: Chapter {ch_num} not found in curriculum.md")
            continue

        folder, sections = write_chapter_files(ch_num, slug, title, phase, phase_title, blocks[ch_num])

        # Validation: check each section is non-empty
        empty = [k for k, v in sections.items() if not v.strip()]
        status = "OK" if not empty else f"MISSING: {', '.join(empty)}"

        section_lengths = {k: len(v) for k, v in sections.items()}
        print(f"  ch{ch_num:02d} [{status}]")
        for k, v in section_lengths.items():
            print(f"    {k:12s}: {v:5d} chars")

        results.append((ch_num, folder, empty))

    print(f"\n{'='*60}")
    print(f"Summary: {len(results)} chapters processed")

    failures = [(n, f, e) for n, f, e in results if e]
    if failures:
        print(f"\nChapters with missing sections:")
        for n, f, e in failures:
            print(f"  Chapter {n} ({f}): missing {', '.join(e)}")
    else:
        print("All sections extracted successfully.")

    # Print folder structure
    print(f"\nFolder structure created:")
    for ch_num, slug, title, phase, phase_title in CHAPTERS:
        folder = f"ch{ch_num:02d}-{slug}"
        if os.path.isdir(os.path.join(CHAPTERS_DIR, folder)):
            files = sorted(os.listdir(os.path.join(CHAPTERS_DIR, folder)))
            print(f"  {folder}/")
            for fi in files:
                size = os.path.getsize(os.path.join(CHAPTERS_DIR, folder, fi))
                print(f"    {fi:20s} {size:6d} bytes")


if __name__ == "__main__":
    main()
