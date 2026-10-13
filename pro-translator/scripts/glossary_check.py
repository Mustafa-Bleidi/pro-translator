#!/usr/bin/env python3
"""
glossary_check.py - verify that glossary terms were applied consistently (stdlib only).

Glossary CSV columns (header required):
  source,target,target_lang,part_of_speech,context,first_use_note,avoid
  - avoid: variants that must NOT appear in the target, separated by "|"

Usage
  python3 glossary_check.py GLOSSARY.csv SOURCE TARGET [--target ar]
  python3 glossary_check.py GLOSSARY.csv src.segments.json tr.json --target ar   (per segment)

Matching is case-insensitive; Latin-script source terms match whole words; Arabic-script
text is normalized (diacritics, tatweel, alef forms) so prefixed forms (ال، و، ب، ل) match.
Exit code: 1 if any MAJOR issue, else 0.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys

AR_DIACRITICS = re.compile(r"[\u064B-\u0652\u0670\u0640]")


def norm(s: str) -> str:
    s = AR_DIACRITICS.sub("", s)
    s = re.sub("[\u0623\u0625\u0622\u0671]", "\u0627", s)
    return s.casefold()


def pattern(term: str):
    t = re.escape(norm(term))
    if re.match(r"^[\w\s\-.'\u2019]+$", term, re.A):      # ASCII/Latin term -> whole word
        return re.compile(rf"(?<!\w){t}(?!\w)")
    return re.compile(t)


def count(term, text):
    return len(pattern(term).findall(norm(text)))


def load_units(path):
    if path.endswith(".json"):
        data = json.load(open(path, encoding="utf-8"))
        if isinstance(data, dict) and "segments" in data:
            return {s["id"]: re.sub(r"</?[gc]\d+>|<x\d+/>", "", s["text"]) for s in data["segments"]}
        return {k: re.sub(r"</?[gc]\d+>|<x\d+/>", "", v) for k, v in data.items()}
    return {"document": open(path, encoding="utf-8-sig").read()}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("glossary")
    ap.add_argument("source")
    ap.add_argument("target_file")
    ap.add_argument("--target", help="only use rows whose target_lang matches (e.g. ar)")
    args = ap.parse_args(argv)

    rows = list(csv.DictReader(open(args.glossary, encoding="utf-8-sig")))
    if args.target:
        base = args.target.lower().split("-")[0]
        rows = [r for r in rows if not r.get("target_lang") or
                r["target_lang"].lower().split("-")[0] == base]
    src, tgt = load_units(args.source), load_units(args.target_file)

    major = minor = 0
    for r in rows:
        s_term, t_term = (r.get("source") or "").strip(), (r.get("target") or "").strip()
        if not s_term or not t_term:
            continue
        avoid = [a.strip() for a in (r.get("avoid") or "").split("|") if a.strip()]
        # ignore variants that normalize to (part of) the approved term, e.g. only diacritics differ
        avoid = [a for a in avoid if norm(a) not in norm(t_term)]
        n_src = sum(count(s_term, u) for u in src.values())
        n_tgt = sum(count(t_term, u) for u in tgt.values())
        missing_in = [k for k, u in src.items() if count(s_term, u) and not count(t_term, tgt.get(k, ""))]
        bad = {a: sum(count(a, u) for u in tgt.values()) for a in avoid}
        bad = {a: n for a, n in bad.items() if n}
        if n_src and missing_in:
            major += 1
            where = "" if list(src) == ["document"] else f" in {len(missing_in)} unit(s), e.g. {missing_in[:4]}"
            print(f"[MAJOR] '{s_term}' → '{t_term}' not found{where} (source {n_src}×, target {n_tgt}×)")
        elif n_src and n_tgt < n_src:
            minor += 1
            print(f"[MINOR] '{s_term}' → '{t_term}': source {n_src}×, target {n_tgt}× "
                  "(pronouns/inflection may explain — check)")
        if bad:
            major += 1
            print(f"[MAJOR] forbidden variant(s) for '{s_term}' found in target: {bad}")
        if n_src and not missing_in and not bad and n_tgt >= n_src:
            print(f"[OK]    '{s_term}' → '{t_term}' ({n_src}×)")
    print(f"\nSummary: {major} major · {minor} minor · {len(rows)} glossary rows checked")
    return 1 if major else 0


if __name__ == "__main__":
    sys.exit(main())
