#!/usr/bin/env python3
"""
preflight.py - report which document tools, Python modules, OCR language packs and fonts
are available, so the translation plan uses what exists and installs nothing silently.

Usage
  python3 preflight.py --target ar [--source en] [--json]

It never installs anything. Missing items are listed with what they would be used for.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
import subprocess
import sys

CLIS = {
    "soffice": "convert DOC/PPT/XLS ↔ modern formats; render DOCX/PPTX to PDF for visual checks",
    "pandoc": "convert Markdown/HTML/DOCX/EPUB",
    "pdftotext": "extract text from text-based PDFs (poppler)",
    "pdfinfo": "PDF page count / metadata (poppler)",
    "pdfimages": "extract embedded PDF images byte-identical (poppler)",
    "pdftoppm": "rasterize PDF pages for visual inspection (poppler)",
    "tesseract": "OCR for scanned PDFs/images",
    "ocrmypdf": "OCR whole PDFs in one step (optional)",
    "qpdf": "repair/decrypt PDFs (optional)",
    "fc-list": "list installed fonts (fontconfig)",
    "chromium": "render HTML → PDF with correct RTL/Indic/CJK shaping (optional)",
}
MODULES = {
    "lxml": "office_segments.py (lossless DOCX/PPTX/XLSX)",
    "docx": "python-docx: inspect/build DOCX",
    "pptx": "python-pptx: inspect/build PPTX",
    "openpyxl": "inspect/build XLSX",
    "fitz": "PyMuPDF: PDF text/images, in-place PDF translation",
    "pdfplumber": "PDF tables",
    "pypdf": "basic PDF operations",
    "PIL": "Pillow: images (read only — images are never modified)",
    "bs4": "BeautifulSoup: HTML",
    "playwright": "Chromium HTML → PDF",
    "yaml": "PyYAML: YAML string files",
    "polib": ".po/.pot files",
}
TESS = {"ar": "ara", "en": "eng", "zh": "chi_sim", "zh-tw": "chi_tra", "es": "spa", "hi": "hin",
        "fr": "fra", "pt": "por", "ru": "rus", "bn": "ben", "ur": "urd", "id": "ind", "de": "deu",
        "ja": "jpn", "tr": "tur", "ko": "kor"}
FC_LANG = {"ar": "ar", "en": "en", "zh": "zh-cn", "zh-tw": "zh-tw", "es": "es", "hi": "hi", "fr": "fr",
           "pt": "pt", "ru": "ru", "bn": "bn", "ur": "ur", "id": "id", "de": "de", "ja": "ja",
           "tr": "tr", "ko": "ko"}
FONT_HINT = {"ar": "fonts-noto-core (Noto Naskh Arabic) or Amiri", "ur": "Noto Nastaliq Urdu",
             "hi": "Noto Sans Devanagari", "bn": "Noto Sans Bengali", "zh": "fonts-noto-cjk",
             "zh-tw": "fonts-noto-cjk", "ja": "fonts-noto-cjk", "ko": "fonts-noto-cjk"}


def norm(tag):
    if not tag:
        return None
    t = tag.lower().lstrip("-")
    return t if t in TESS else t.split("-")[0]


def run(cmd):
    try:
        return subprocess.run(cmd, capture_output=True, text=True, timeout=20).stdout
    except Exception:
        return ""


def find_cli(name):
    if name == "soffice":
        return shutil.which("soffice") or shutil.which("libreoffice")
    if name == "chromium":
        for n in ("chromium", "chromium-browser", "google-chrome", "/opt/pw-browsers/chromium"):
            p = shutil.which(n)
            if p:
                return p
        return None
    return shutil.which(name)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--target", action="append", default=[], help="target tag (repeatable)")
    ap.add_argument("--source", help="source language tag (for OCR pack)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    res = {"python": sys.version.split()[0], "cli": {}, "modules": {}, "ocr": {}, "fonts": {}}
    for name, why in CLIS.items():
        res["cli"][name] = {"path": find_cli(name), "use": why}
    for mod, why in MODULES.items():
        res["modules"][mod] = {"ok": importlib.util.find_spec(mod) is not None, "use": why}

    tess_langs = set()
    if res["cli"]["tesseract"]["path"]:
        tess_langs = {l.strip() for l in run(["tesseract", "--list-langs"]).splitlines()[1:]}
    for tag in filter(None, [norm(args.source)] + [norm(t) for t in args.target]):
        code = TESS.get(tag)
        if code:
            res["ocr"][tag] = {"pack": code, "installed": code in tess_langs}

    if res["cli"]["fc-list"]["path"]:
        for tag in filter(None, [norm(t) for t in args.target]):
            fams = run(["fc-list", f":lang={FC_LANG.get(tag, tag)}", "family"]).splitlines()
            fams = sorted({f.split(",")[0].strip() for f in fams if f.strip()})
            res["fonts"][tag] = {"count": len(fams), "examples": fams[:6], "hint": FONT_HINT.get(tag)}

    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=1))
        return 0

    ok, no = "✓", "✗"
    print(f"Python {res['python']}\n\nCommand-line tools")
    for n, v in res["cli"].items():
        print(f"  {ok if v['path'] else no} {n:<10} {v['path'] or '— missing'}   ({v['use']})")
    print("\nPython modules")
    for n, v in res["modules"].items():
        print(f"  {ok if v['ok'] else no} {n:<11} ({v['use']})")
    if res["ocr"]:
        print("\nOCR language packs (OCR uses the SOURCE language)")
        for tag, v in res["ocr"].items():
            print(f"  {ok if v['installed'] else no} {tag}: tesseract '{v['pack']}'")
    if res["fonts"]:
        print("\nFonts covering the target script (for rendering/visual checks)")
        for tag, v in res["fonts"].items():
            mark = ok if v["count"] else no
            extra = f"e.g. {', '.join(v['examples'])}" if v["count"] else f"none found — consider {v['hint'] or 'a Noto font'}"
            print(f"  {mark} {tag}: {v['count']} families; {extra}")
    print("\nNothing was installed. Ask the user before installing anything that is missing and needed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
