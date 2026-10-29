#!/usr/bin/env python3
"""Structural checks for a saved pop-explainer answer.

Checks that the four blocks appear in order, that none of the listed terms
appear in the story more than once (the user's own term may appear once), that the invented-number label is used at most once,
and that the closing line points to /答案 or /answer. It doesn't judge
whether the story is clear or correct — that's what expected.md is for.

Usage:
  python3 check_story.py OUTPUT.md --terms "p-value,null hypothesis"

Exit code 0 = all checks passed, 1 = at least one failure.
"""
import argparse
import re
import sys
from pathlib import Path


def report(results):
    ok = True
    for passed, msg in results:
        print(("PASS  " if passed else "FAIL  ") + msg)
        ok &= passed
    return 0 if ok else 1


def check_explainer(text, terms):
    res = []
    order = [text.find(h) for h in ("🎬", "💡", "⚠️", "🤔")]
    res.append((all(i >= 0 for i in order) and order == sorted(order), "🎬 💡 ⚠️ 🤔 present and in order"))
    if order[0] >= 0 and order[1] > order[0]:
        story = text[order[0]:order[1]].lower()
        # The skill lets the user's own term appear once (as a headline or a
        # character's words); more than that means the story is explaining
        # with jargon instead of showing.
        leaked = [t for t in terms if t and story.count(t.lower()) > 1]
        res.append((not leaked, "no listed term used more than once inside the story" + (f" (leaked: {leaked})" if leaked else "")))
        res.append((len(re.findall(r"虚构|made up", story)) <= 1, "invented-number label used at most once in the story"))
    res.append((bool(re.search(r"/答案|/answer", text)), "closing line points to /答案 or /answer"))
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("output")
    ap.add_argument("--terms", default="", help="comma-separated terms to keep out of the story")
    a = ap.parse_args()
    text = Path(a.output).read_text(encoding="utf-8")
    sys.exit(report(check_explainer(text, [t.strip() for t in a.terms.split(",")])))


if __name__ == "__main__":
    main()
