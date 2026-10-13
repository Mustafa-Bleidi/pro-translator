# Formats — how to extract, translate and rebuild each file type

Rule of thumb: **same format in, same format out** (PDF → PDF, DOCX → DOCX) when technically
feasible. If not, produce the closest practical equivalent and explain the limitation.
Always verify a tool exists (`scripts/preflight.py`) before planning around it.

---

## DOCX / PPTX / XLSX — use `scripts/office_segments.py` (preferred)

This route edits the original XML in a copy of the file, so styles, layout, images, charts,
headers/footers, footnotes and numbering survive. Only `lxml` is required.

```bash
# 1. extract translatable segments (inline formatting becomes tags)
python3 scripts/office_segments.py extract report.docx -o report.segments.json

# 2. translate: write report.tr.json  →  {"<segment id>": "<translated text>", ...}
#    keep every <gN>…</gN>, <cN>…</cN>, <xN/> tag (see preservation-rules.md §8)

# 3. check segment-level integrity before building the file
python3 scripts/qa_check.py --segments report.segments.json report.tr.json --target ar

# 4. build the output (never overwrite the input)
python3 scripts/office_segments.py apply report.docx report.tr.json -o report_AR.docx --lang ar
```

What `--lang` does: sets the language tag on runs (spell-check, font fallback, hyphenation),
and for RTL targets (`ar`, `ur`) sets paragraph/run direction (`w:bidi`, `w:rtl`), mirrors
tables (`w:bidiVisual`), and right-aligns PPTX paragraphs. `--rtl-sheets` also flips XLSX sheets
to right-to-left.

Covered parts:
- DOCX: body, tables (incl. nested), headers, footers, footnotes, endnotes, comments, text boxes.
- PPTX: slides (shapes, groups, tables, text boxes), notes, (layouts/masters are left as is).
- XLSX: shared strings and inline strings (cell text). Formulas, numbers, sheet names untouched.

Translating segment files: for large files, translate the JSON in batches (e.g. 100 segments),
writing to the same `*.tr.json`. Keep the term map open. Never change segment ids.

Fonts: if the document's fonts lack the target script (e.g. Calibri for Bengali is OK on
Windows but not everywhere), keep the font settings — Office falls back by language — and
mention it in the report. Only change fonts when the user asks or the render check shows tofu
(□□□) boxes.

**Render check:** convert the output to PDF and look at representative pages:
```bash
soffice --headless --convert-to pdf --outdir out/ report_AR.docx
pdftoppm -png -r 70 -f 1 -l 3 out/report_AR.pdf out/page
```
Look for: direction, alignment, tofu boxes, overflowing text boxes (PPTX — German/Russian/
Spanish expand 15–35 %), broken tables, misplaced images.

Fallback without lxml: python-docx / python-pptx / openpyxl paragraph-level replacement
(loses mixed inline formatting inside a paragraph — report it).

Legacy `.doc/.ppt/.xls`: convert a **copy** with `soffice --headless --convert-to docx` first;
deliver in the modern format unless the user needs the legacy one (convert back at the end).

---

## PDF

Determine the type first (`pdftotext` output empty or garbage → scanned).

**A. Text-based PDF** — choose by priority:
1. If the user has the source DOCX/PPTX, ask for it; translating it gives a far better PDF.
2. Rebuild route (most robust, best typography for RTL/CJK/Indic):
   extract with `pdftotext -layout` / PyMuPDF / pdfplumber (text, headings by font size,
   tables with pdfplumber), extract images byte-identical (`pdfimages -all` or PyMuPDF),
   rebuild as HTML or DOCX with the same structure, then render to PDF
   (Chromium/Playwright `page.pdf()` or `soffice --convert-to pdf`). Chromium shapes Arabic,
   Urdu, Hindi, Bengali correctly; set `<html lang="xx" dir="rtl|ltr">` and Noto fonts.
3. In-place route (keeps exact page geometry, good for forms/brochures with short text):
   PyMuPDF — redact text blocks (keep images: `images=fitz.PDF_REDACT_IMAGE_NONE`) and write
   the translation into the same rectangles with `insert_htmlbox` (handles RTL and shaping,
   auto-shrinks). Check every page visually; long expansions overflow.

**B. Scanned PDF** — OCR body text with the source language pack
(`tesseract page.png out -l eng --psm 3`, or `ocrmypdf` if installed), then rebuild as in A.2.
Embedded figures are cut out as images and reinserted untouched. Report OCR use and pages
where OCR confidence was low.

**C. Mixed** — per page: text route for text pages, OCR route for scanned pages.

Never claim the PDF layout is identical; describe what was preserved and how it was checked.

---

## Markdown / plain text

- Translate prose; keep fenced code, inline code, link URLs, image paths, HTML tags, front-matter
  keys (translate front-matter values only if they are human-readable titles/descriptions).
- Keep heading levels, list markers, table pipes, line breaks inside tables.
- Link text is translated; anchors (`#section-id`) stay, unless they are auto-generated from
  headings — then note that anchors may break.
- Run `qa_check.py source.md target.md --target xx`.

## HTML / XML

- Translate text nodes and the attributes `alt`, `title`, `placeholder`, `aria-label`,
  `content` of `<meta name="description">`.
- Never touch tags, other attributes, `<script>`, `<style>`, `<code>`, `<pre>`, `translate="no"`.
- Set `<html lang="xx">` and, for RTL targets, `dir="rtl"`; check CSS uses logical properties
  or add a minimal `[dir=rtl]` override if layout breaks.
- Parse with a real parser (lxml/BeautifulSoup), never regex replacement on whole files.

## Subtitles (SRT / VTT / ASS)

- Keep cue numbers and timecodes byte-identical; keep cue count.
- Respect reading speed and line limits: Latin/Cyrillic ≈ 42 chars/line, 2 lines;
  CJK ≈ 16–18 chars/line; Arabic/Urdu/Hindi/Bengali ≈ 40–42 chars/line.
- Condense *wording* if needed for readability, never meaning; no cue merges unless asked.
- Keep styling tags (`<i>`, `{\an8}`) and speaker labels.

## Software strings (JSON, YAML, .po/.pot, .strings, .xliff, .arb, .properties, .resx)

- Translate values only; keys, comments, IDs stay.
- Keep placeholders and ICU syntax: `{count, plural, one {# file} other {# files}}` — translate
  the inner text and **supply all plural categories the target language needs**:
  ar: zero/one/two/few/many/other; ru/uk: one/few/many/other; pl similar; fr: one/many/other;
  ja/zh/ko/id/tr(nouns): usually only other; hi/bn/ur/de/es/pt/en: one/other.
- `.po`: fill `msgstr`, keep `msgid`, handle `msgid_plural` with the `Plural-Forms` header.
- UI strings: short, consistent verbs for buttons; respect length limits; note truncation risks.
- Validate the file parses after writing (`python3 -c "import json; json.load(open(f))"`, etc.).

## CSV / TSV

Translate only textual columns the user wants translated (ask if unclear); keep headers used by
code; keep delimiters, quoting and encoding (write UTF-8; add BOM only if the source had one or
Excel users need it for non-Latin scripts).

## EPUB

It is a zip of XHTML: handle each chapter as HTML (above), update `<dc:language>` in the OPF,
keep the spine and TOC structure, translate the NCX/nav labels.

---

## Direction and script essentials

| Target | Direction | Script notes | Suggested fonts (Noto family covers all) |
|---|---|---|---|
| ar | RTL | Contextual shaping; never break ligatures; keep Latin/digits as LTR runs | Noto Naskh Arabic, Amiri, Noto Sans Arabic |
| ur | RTL | Nastaliq preferred for prose; Naskh acceptable for technical text | Noto Nastaliq Urdu, Noto Naskh Arabic |
| hi | LTR | Devanagari conjuncts need a shaping engine (HarfBuzz) | Noto Sans/Serif Devanagari |
| bn | LTR | Bengali conjuncts need shaping | Noto Sans/Serif Bengali |
| zh-cn / zh-tw | LTR (vertical optional) | Full-width punctuation; no word spaces | Noto Sans CJK SC / TC |
| ja | LTR (vertical optional) | Mixed kana/kanji; no word spaces | Noto Sans CJK JP |
| ko | LTR | Hangul with word spacing | Noto Sans CJK KR |
| ru | LTR | Cyrillic | Any modern font (Noto Sans) |
| others | LTR | Latin with diacritics (ş ğ ı İ ç ã õ ñ ß é …) | Any modern font |

Mixed-direction text (RTL with English terms/numbers): the logical order is what you write;
the renderer handles display. Do not insert manual direction marks unless a render check shows
punctuation jumping to the wrong side; then use U+200F (RLM) / U+200E (LRM) sparingly and only
in formats that support them. Never insert invisible characters anywhere else.
