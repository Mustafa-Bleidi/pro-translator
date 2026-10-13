#!/usr/bin/env python3
"""
qa_check.py - automated source/target comparison for translations (stdlib only).

Checks: numbers (digit systems normalized), URLs, e-mails, inline code, code blocks,
placeholders ({x}, {{x}}, %s, ${x}), markup tags, segment tags (<gN>, <cN>, <xN/>),
Markdown structure, subtitle timecodes, JSON key structure, empty or untranslated text,
length ratio, target typography, and (with --humanize) AI/MT "tell" phrases.

Usage
  python3 qa_check.py SOURCE TARGET --target ar [--localize] [--humanize] [--json]
  python3 qa_check.py --segments source.segments.json translations.json --target ar

Exit code: 2 = CRITICAL issues, 1 = MAJOR issues, 0 = only MINOR / none.
Numbers flagged as CRITICAL must be verified by a human/agent; legitimate changes
(e.g. 12,000 → 1.2万 with --localize) can be dismissed with a note in the report.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter

# --------------------------------------------------------------------------- language data
# ratio = expected (min, max) target/source character ratio when the source is English
LANG_INFO = {
    "ar": {"script": r"[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]", "latin": False, "ratio": (0.8, 1.4)},
    "en": {"script": r"[A-Za-z]", "latin": True, "ratio": (0.7, 1.3)},
    "zh": {"script": r"[\u4E00-\u9FFF\u3400-\u4DBF]", "latin": False, "ratio": (0.25, 0.8)},
    "es": {"script": r"[A-Za-zÁÉÍÓÚÑÜáéíóúñü]", "latin": True, "ratio": (0.95, 1.45)},
    "hi": {"script": r"[\u0900-\u097F]", "latin": False, "ratio": (0.9, 1.5)},
    "fr": {"script": r"[A-Za-zÀ-ÿŒœ]", "latin": True, "ratio": (0.95, 1.45)},
    "pt": {"script": r"[A-Za-zÀ-ÿ]", "latin": True, "ratio": (0.95, 1.45)},
    "ru": {"script": r"[\u0400-\u04FF]", "latin": False, "ratio": (0.9, 1.45)},
    "bn": {"script": r"[\u0980-\u09FF]", "latin": False, "ratio": (0.85, 1.45)},
    "ur": {"script": r"[\u0600-\u06FF\u0750-\u077F\uFB50-\uFDFF\uFE70-\uFEFF]", "latin": False, "ratio": (0.85, 1.45)},
    "id": {"script": r"[A-Za-z]", "latin": True, "ratio": (0.95, 1.45)},
    "de": {"script": r"[A-Za-zÄÖÜäöüß]", "latin": True, "ratio": (0.95, 1.5)},
    "ja": {"script": r"[\u3040-\u30FF\u4E00-\u9FFF]", "latin": False, "ratio": (0.3, 1.0)},
    "tr": {"script": r"[A-Za-zÇĞİÖŞÜçğıöşü]", "latin": True, "ratio": (0.85, 1.35)},
    "ko": {"script": r"[\uAC00-\uD7AF\u1100-\u11FF]", "latin": False, "ratio": (0.35, 1.0)},
}

# AI / MT tell phrases checked with --humanize (lower-cased substring match)
TELLS = {
    "en": ["delve", "tapestry", "testament to", "pivotal", "seamless", "leverage", "in today's",
           "it is important to note", "it's worth noting", "let's dive", "in conclusion", "game-changer",
           "ever-evolving", "furthermore,", "moreover,", "navigate the", "realm", "embark"],
    "ar": ["في عالمنا اليوم", "تجدر الإشارة", "من الجدير بالذكر", "علاوة على ذلك", "بالإضافة إلى ذلك",
           "يلعب دورًا محوريًا", "يلعب دورا محوريا", "حجر الزاوية", "نقلة نوعية", "في الختام", "مما لا شك فيه", "يتم "],
    "zh": ["在当今", "值得注意的是", "总而言之", "综上所述", "扮演着重要的角色", "赋能", "助力", "进行"],
    "es": ["en el mundo actual", "cabe destacar", "es importante señalar", "juega un papel", "sin lugar a dudas",
           "en conclusión", "además,", "asimismo,"],
    "hi": ["आज के इस आधुनिक युग", "यह ध्यान देने योग्य है", "महत्वपूर्ण भूमिका निभा", "निष्कर्ष के तौर पर", "इसके अलावा"],
    "fr": ["dans le monde d’aujourd’hui", "dans le monde d'aujourd'hui", "il est important de noter",
           "il convient de souligner", "jouer un rôle crucial", "joue un rôle crucial", "en conclusion", "en outre,", "de plus,"],
    "pt": ["no mundo atual", "vale ressaltar", "é importante destacar", "desempenha um papel crucial",
           "em conclusão", "além disso,", "vou estar"],
    "ru": ["в современном мире", "важно отметить", "стоит подчеркнуть", "играет ключевую роль",
           "в заключение", "кроме того,", "более того,", "данный"],
    "bn": ["বর্তমান আধুনিক যুগে", "উল্লেখ্য যে", "গুরুত্বপূর্ণ ভূমিকা পালন", "পরিশেষে", "এছাড়াও"],
    "ur": ["آج کے جدید دور", "قابل ذکر ہے", "قابلِ ذکر ہے", "اہم کردار ادا", "مزید برآں", "خلاصہ کلام"],
    "id": ["di era modern ini", "di era digital", "penting untuk dicatat", "memainkan peran penting",
           "kesimpulannya", "selain itu,", " dimana "],
    "de": ["in der heutigen", "es ist wichtig zu beachten", "spielt eine entscheidende rolle", "nahtlos",
           "zusammenfassend lässt sich", "darüber hinaus,", "ganzheitlich"],
    "ja": ["することが重要です", "結論として", "まとめると", "と言えるでしょう", "において"],
    "tr": ["günümüz dünyasında", "önemle belirtmek", "önemli bir rol oynamaktadır", "sonuç olarak",
           "bunun yanı sıra", "buna ek olarak", "bu bağlamda"],
    "ko": ["하는 것이 중요합니다", "결론적으로", "요약하자면", "에 있어서", "되어지", "보여지", "당신"],
}

DIGIT_MAP = {}
for zero in (0x0660, 0x06F0, 0x0966, 0x09E6, 0xFF10):
    for i in range(10):
        DIGIT_MAP[chr(zero + i)] = str(i)
DIGIT_TRANS = str.maketrans(DIGIT_MAP)

SEG_TAG = re.compile(r"</?([gc])(\d+)>|<x(\d+)/>")
NUM = re.compile(r"\d{1,3}(?:[ \u00A0\u202F\u2009]\d{3})+(?:[.,\u066B]\d+)?(?!\d)"
                 r"|\d+(?:[.,\u066B\u066C\u00A0\u202F\u2009'\u2019]\d+)*")
URL = re.compile(r"(?:https?://|ftp://|www\.)[^\s<>\"'\uFF09)\]»\u201D\u060C]+", re.I)
EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")
FENCE = re.compile(r"```.*?```|~~~.*?~~~", re.S)
INLINE_CODE = re.compile(r"`[^`\n]+`")
PLACEHOLDER = re.compile(r"\{\{[^{}]+\}\}|\$\{[^{}]+\}|\{[A-Za-z0-9_.,: #-]*\}|%(?:\d+\$)?[-+ 0#]*\d*(?:\.\d+)?[sdifuxXeEgGc@]")
MARKUP = re.compile(r"</?[A-Za-z][A-Za-z0-9:-]*\b[^<>]*?/?>")
TIMECODE = re.compile(r"\d{1,2}:\d{2}:\d{2}[,.]\d{3}\s*-->\s*\d{1,2}:\d{2}:\d{2}[,.]\d{3}")
LATIN_WORD = re.compile(r"[A-Za-zÀ-ÿ]{2,}")
LETTER = re.compile(r"[^\W\d_]", re.U)


class Report:
    def __init__(self):
        self.items = []

    def add(self, sev, where, msg):
        self.items.append({"severity": sev, "where": where, "message": msg})

    def counts(self):
        c = Counter(i["severity"] for i in self.items)
        return {k: c.get(k, 0) for k in ("CRITICAL", "MAJOR", "MINOR")}


# --------------------------------------------------------------------------- helpers
def strip_seg_tags(s):
    return SEG_TAG.sub("", s)


def protected(s):
    """Remove spans that must be identical (checked separately) before prose checks."""
    s = FENCE.sub(" ", s)
    s = INLINE_CODE.sub(" ", s)
    s = URL.sub(" ", s)
    s = EMAIL.sub(" ", s)
    s = PLACEHOLDER.sub(" ", s)
    s = MARKUP.sub(" ", s)
    return s


def numbers(s):
    s = protected(strip_seg_tags(s)).translate(DIGIT_TRANS)
    out = []
    for m in NUM.finditer(s):
        out.append(re.sub(r"\D", "", m.group()))
    return Counter(out)


def diff_counter(a: Counter, b: Counter):
    missing = a - b
    extra = b - a
    return list(missing.elements()), list(extra.elements())


def compare_exact(rep, where, label, src_items, tgt_items, sev):
    missing, extra = diff_counter(Counter(src_items), Counter(tgt_items))
    if missing:
        rep.add(sev, where, f"{label} missing/changed in target: {missing[:6]}")
    if extra:
        rep.add(sev, where, f"{label} not in source: {extra[:6]}")


def latin_ratio(s):
    s = protected(strip_seg_tags(s))
    letters = LETTER.findall(s)
    if not letters:
        return 0.0, 0
    latin = [ch for ch in letters if re.match(r"[A-Za-zÀ-ÿ]", ch)]
    return len(latin) / len(letters), len(LATIN_WORD.findall(s))


def check_unit(rep, where, src, tgt, lang, args, check_numbers=True):
    if src.strip() and not tgt.strip():
        rep.add("CRITICAL", where, "empty translation for non-empty source")
        return
    if check_numbers:
        missing, extra = diff_counter(numbers(src), numbers(tgt))
        if missing:
            rep.add("CRITICAL", where, f"number(s) missing or changed: {missing[:8]} — verify")
        if extra:
            rep.add("CRITICAL", where, f"number(s) not in source: {extra[:8]} — verify")
    compare_exact(rep, where, "URL", URL.findall(src), URL.findall(tgt), "CRITICAL")
    compare_exact(rep, where, "e-mail", EMAIL.findall(src), EMAIL.findall(tgt), "CRITICAL")
    compare_exact(rep, where, "inline code", INLINE_CODE.findall(src), INLINE_CODE.findall(tgt), "CRITICAL")
    compare_exact(rep, where, "code block", FENCE.findall(src), FENCE.findall(tgt), "CRITICAL")
    compare_exact(rep, where, "placeholder", PLACEHOLDER.findall(strip_seg_tags(src)),
                  PLACEHOLDER.findall(strip_seg_tags(tgt)), "CRITICAL")
    src_tags = [m.group() for m in MARKUP.finditer(src) if not SEG_TAG.fullmatch(m.group())]
    tgt_tags = [m.group() for m in MARKUP.finditer(tgt) if not SEG_TAG.fullmatch(m.group())]
    compare_exact(rep, where, "markup tag", src_tags, tgt_tags, "MAJOR")

    info = LANG_INFO.get(lang)
    if info:
        ratio, latin_words = latin_ratio(tgt)
        s_plain = protected(strip_seg_tags(src)).strip()
        t_plain = protected(strip_seg_tags(tgt)).strip()
        if not info["latin"] and ratio > 0.6 and latin_words >= 3:
            rep.add("MAJOR", where, f"looks untranslated (Latin letters {ratio:.0%}): {t_plain[:70]!r}")
        if info["latin"] and s_plain and s_plain == t_plain and len(s_plain.split()) >= 3 \
                and args.source_lang != lang:
            rep.add("MAJOR", where, f"identical to source (untranslated?): {t_plain[:70]!r}")
        typography(rep, where, tgt, lang, args)


def typography(rep, where, tgt, lang, args):
    t = protected(strip_seg_tags(tgt))
    if lang in ("ar", "ur"):
        if re.search(r"[\u0600-\u06FF]\s*,\s*[\u0600-\u06FF]", t):
            rep.add("MINOR", where, "Latin comma ',' between Arabic-script words — use '،'")
        if re.search(r"[\u0600-\u06FF]\s*\?", t):
            rep.add("MINOR", where, "Latin '?' after Arabic-script text — use '؟'")
    if lang == "ur":
        if re.search(r"[\u0600-\u06FF]\.(\s|$)", t):
            rep.add("MINOR", where, "Urdu sentence ends with '.' — use '۔'")
        if re.search(r"[\u064A\u0643\u0647]", t):
            rep.add("MAJOR", where, "Arabic letter forms (ي ك ه) in Urdu — use ی ک ہ/ھ")
    if lang in ("hi", "bn"):
        if re.search(r"[\u0900-\u09FF]\.(\s|$)", t):
            rep.add("MINOR", where, "sentence ends with '.' — use danda '।'")
    if lang in ("zh", "ja"):
        if re.search(r"[\u3040-\u30FF\u4E00-\u9FFF][,.;:?!][\u3040-\u30FF\u4E00-\u9FFF]", t):
            rep.add("MINOR", where, "half-width punctuation between CJK characters — use full-width")
    if lang == "es":
        if "?" in t and "¿" not in t:
            rep.add("MINOR", where, "question without opening '¿'")
    if lang == "fr" and not (args.variant or "").endswith("ca"):
        if re.search(r"\w[;:!?](\s|$)", t):
            rep.add("MINOR", where, "missing (non-breaking) space before ; : ! ?")
    if lang in ("de", "ru", "fr") and re.search(r'"[^"]+"', t):
        rep.add("MINOR", where, 'straight quotes "…" — use the language’s quotation marks')
    if args.humanize:
        low = t.lower()
        hits = [p for p in TELLS.get(lang, []) if p in low]
        if hits:
            rep.add("MINOR", where, f"humanizer tells present: {hits[:6]}")


def markdown_structure(rep, src, tgt):
    def stats(s):
        s2 = FENCE.sub("", s)
        lines = s2.splitlines()
        st = Counter()
        for ln in lines:
            m = re.match(r"^(#{1,6})\s", ln)
            if m:
                st[f"h{len(m.group(1))}"] += 1
            if re.match(r"^\s*([-*+]|\d+[.)])\s+", ln):
                st["list items"] += 1
            if re.match(r"^\s*\|.*\|\s*$", ln):
                st["table rows"] += 1
            if re.match(r"^\s*>", ln):
                st["blockquote lines"] += 1
        st["images"] = len(re.findall(r"!\[[^\]]*\]\([^)]+\)", s2))
        st["links"] = len(re.findall(r"(?<!!)\[[^\]]*\]\([^)]+\)", s2))
        st["code blocks"] = len(FENCE.findall(s))
        return st
    a, b = stats(src), stats(tgt)
    for k in sorted(set(a) | set(b)):
        if a.get(k, 0) != b.get(k, 0):
            sev = "CRITICAL" if k in ("images", "code blocks") else "MAJOR"
            rep.add(sev, "structure", f"{k}: source {a.get(k, 0)} vs target {b.get(k, 0)}")
    img_s = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", src)
    img_t = re.findall(r"!\[[^\]]*\]\(([^)]+)\)", tgt)
    compare_exact(rep, "structure", "image path", img_s, img_t, "CRITICAL")


def json_keys(obj, prefix=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from json_keys(v, f"{prefix}/{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from json_keys(v, f"{prefix}[{i}]")
    else:
        yield prefix


def length_check(rep, src, tgt, lang, args):
    info = LANG_INFO.get(lang)
    if not info or args.source_lang not in (None, "en"):
        return
    s = len(protected(strip_seg_tags(src)).strip())
    t = len(protected(strip_seg_tags(tgt)).strip())
    if s < 200:
        return
    r = t / s
    lo, hi = info["ratio"]
    if r < lo * 0.75 or r > hi * 1.25:
        rep.add("MAJOR", "length", f"target/source length ratio {r:.2f} far outside expected {lo}–{hi} for {lang} — check for omissions or additions")
    elif r < lo or r > hi:
        rep.add("MINOR", "length", f"target/source length ratio {r:.2f} outside typical {lo}–{hi} for {lang}")


# --------------------------------------------------------------------------- modes
def run_files(args, rep):
    src = open(args.source, encoding="utf-8-sig").read()
    tgt = open(args.target_file, encoding="utf-8-sig").read()
    lang = args.lang
    ext = args.source.rsplit(".", 1)[-1].lower()

    if ext in ("json", "arb"):
        try:
            ks, kt = set(json_keys(json.loads(src))), set(json_keys(json.loads(tgt)))
            if ks != kt:
                rep.add("CRITICAL", "json", f"key structure differs: missing {sorted(ks - kt)[:5]}, extra {sorted(kt - ks)[:5]}")
        except json.JSONDecodeError as e:
            rep.add("CRITICAL", "json", f"invalid JSON: {e}")
    if ext in ("srt", "vtt"):
        compare_exact(rep, "subtitles", "timecode", TIMECODE.findall(src), TIMECODE.findall(tgt), "CRITICAL")
    if ext in ("md", "markdown", "mdx"):
        markdown_structure(rep, src, tgt)

    # align by blank-line paragraphs when counts match, else compare globally
    ps = [p for p in re.split(r"\n\s*\n", src) if p.strip()]
    pt = [p for p in re.split(r"\n\s*\n", tgt) if p.strip()]
    if len(ps) == len(pt):
        for i, (a, b) in enumerate(zip(ps, pt), 1):
            check_unit(rep, f"para {i}", a, b, lang, args)
    else:
        rep.add("MAJOR", "structure", f"paragraph count differs: source {len(ps)} vs target {len(pt)} (checks run globally)")
        check_unit(rep, "document", src, tgt, lang, args)
    length_check(rep, src, tgt, lang, args)


def load_segments(path):
    data = json.load(open(path, encoding="utf-8"))
    if isinstance(data, dict) and "segments" in data:
        return {s["id"]: s["text"] for s in data["segments"]}
    if isinstance(data, list):
        return {s["id"]: s["text"] for s in data}
    return data


def run_segments(args, rep):
    src = load_segments(args.segments[0])
    tgt = load_segments(args.segments[1])
    lang = args.lang
    for sid in src:
        if sid not in tgt:
            rep.add("MAJOR", sid, "segment not translated (missing id)")
    for sid in tgt:
        if sid not in src:
            rep.add("MINOR", sid, "unknown segment id (not in source)")
    for sid, s in src.items():
        if sid not in tgt:
            continue
        t = tgt[sid]
        tags_s = Counter(m.group() for m in SEG_TAG.finditer(s) if not m.group().startswith("</"))
        tags_t = Counter(m.group() for m in SEG_TAG.finditer(t) if not m.group().startswith("</"))
        for tag, n in tags_s.items():
            if tags_t.get(tag, 0) < n:
                sev = "CRITICAL" if tag.startswith("<x") else ("MAJOR" if tag.startswith("<c") else "MINOR")
                rep.add(sev, sid, f"tag {tag} missing")
        for tag in tags_t:
            if tag not in tags_s:
                rep.add("MAJOR", sid, f"tag {tag} not in source")
        opens = len(re.findall(r"<[gc]\d+>", t))
        closes = len(re.findall(r"</[gc]\d+>", t))
        if opens != closes:
            rep.add("MAJOR", sid, "unbalanced <g>/<c> tags")
        check_unit(rep, sid, s, t, lang, args)
    length_check(rep, "\n".join(src.values()), "\n".join(tgt.get(k, "") for k in src), lang, args)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("source", nargs="?")
    ap.add_argument("target_file", nargs="?")
    ap.add_argument("--segments", nargs=2, metavar=("SOURCE_JSON", "TRANSLATION_JSON"))
    ap.add_argument("--target", dest="target_tag", required=True, help="target tag, e.g. ar, pt-br, zh-tw")
    ap.add_argument("--source-lang", default=None, help="source language tag (default: assume en for length ratio)")
    ap.add_argument("--localize", action="store_true", help="number formats were localized (values still checked)")
    ap.add_argument("--humanize", action="store_true", help="also scan for AI/MT tell phrases")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    args = ap.parse_args(argv)
    tag = args.target_tag.lower().lstrip("-")
    args.lang = tag.split("-")[0]
    args.variant = tag
    if args.source_lang:
        args.source_lang = args.source_lang.lower().split("-")[0]

    rep = Report()
    if args.segments:
        run_segments(args, rep)
    elif args.source and args.target_file:
        run_files(args, rep)
    else:
        ap.error("give SOURCE TARGET files or --segments SOURCE_JSON TRANSLATION_JSON")

    counts = rep.counts()
    if args.json:
        print(json.dumps({"counts": counts, "issues": rep.items}, ensure_ascii=False, indent=1))
    else:
        order = {"CRITICAL": 0, "MAJOR": 1, "MINOR": 2}
        for it in sorted(rep.items, key=lambda i: order[i["severity"]]):
            print(f"[{it['severity']}] {it['where']}: {it['message']}")
        print(f"\nSummary: {counts['CRITICAL']} critical · {counts['MAJOR']} major · {counts['MINOR']} minor")
    return 2 if counts["CRITICAL"] else (1 if counts["MAJOR"] else 0)


if __name__ == "__main__":
    sys.exit(main())
