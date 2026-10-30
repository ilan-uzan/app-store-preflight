#!/usr/bin/env python3
"""Verify that every quote in the reference files appears verbatim in Apple's source texts.

Usage: python3 -I verify_quotes.py <skill_dir> [--verbose]
Checks both "quote:" lines and "> " source-text blocks against every file in source/.
Only whitespace, non-breaking spaces and zero-width characters are normalized.
"""
import glob
import os
import re
import sys

ZW = dict.fromkeys(map(ord, "​‌‍﻿"), None)


def norm(s):
    s = s.translate(ZW).replace(" ", " ")
    s = re.sub(r"\[\[GL [0-9.]+\]\]", " ", s)
    s = re.sub(r"\*\*|`|\[|\]\([^)]*\)", "", s)  # markdown emphasis/links the authors may have kept
    s = s.replace("]", "")
    return re.sub(r"\s+", " ", s).strip()


def main():
    skill = sys.argv[1]
    verbose = "--verbose" in sys.argv
    corpus = " ".join(norm(open(p, encoding="utf-8").read()) for p in glob.glob(os.path.join(skill, "source", "*.md")))
    corpus_lower = corpus.lower()
    total, bad = 0, []
    for path in sorted(glob.glob(os.path.join(skill, "references", "*", "*.md"))):
        rel = os.path.relpath(path, os.path.join(skill, "references"))
        lines = open(path, encoding="utf-8").read().split("\n")
        for n, line in enumerate(lines, 1):
            text = None
            nxt = lines[n] if n < len(lines) else ""
            if re.match(r"^>\s*\|[-:| ]+\|\s*$", nxt):  # table header row: authored, not quoted
                continue
            if re.match(r"^>\s*(-\s+)?(\[?Editor\b|Note \(not Apple text\))", line):  # labeled editor notes
                continue
            m = re.match(r'^\s+- quote:\s*"(.*)"\s*$', line)
            if m:
                text = m.group(1)
            elif line.startswith("> "):
                text = re.sub(r"^>\s*(-\s+)?", "", line.rstrip("\n"))
            if not text:
                continue
            q = norm(text)
            if len(q) < 4 or set(q) <= set("|-: "):
                continue
            if q.startswith("|"):  # table row: check each cell separately
                cells = [norm(c) for cell in q.strip("|").split("|") for c in re.split(r"<br\s*/?>", cell) if len(norm(c)) > 3]
                for c in cells:
                    total += 1
                    if c not in corpus and c.lower() not in corpus_lower:
                        bad.append((rel, n, c))
                continue
            total += 1
            # Quotes may span an ellipsis: every fragment must match.
            q = re.sub(r"^\([^)]{1,80}\)\s*", "", q)  # leading locator such as "(Bundle ID row)"
            frags = [f.strip() for f in re.split(r"\s*(?:\.\.\.|…|; | — |<br\s*/?>| \| )\s*", q) if len(f.strip(' "“”')) > 3]
            frags = [f.strip(' "“”') for f in frags]
            frags = [re.sub(r"^\d+\.\s+", "", f) for f in frags]
            if not all(f in corpus or re.sub(r"^[A-Za-z ]{2,30}:\s*", "", f) in corpus for f in frags):
                bad.append((rel, n, q))
    print(f"{total - len(bad)}/{total} quoted passages found verbatim in source/")
    for rel, n, q in bad[: (None if verbose else 40)]:
        print(f"  NOT FOUND {rel}:{n}: {q[:140]}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
