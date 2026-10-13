# Workflow — the full document pipeline

Follow the phases in order. Do not skip a phase; a phase can be short when the document is simple.

```
0 Preflight → 1 Analysis → 2 Extraction → 3 Terminology & style sheet → 4 Translation
→ 5 Reconstruction → 6 Automated validation → 7 Second review → 8 Report
                                        (+ 4b Humanize when --humanize)
```

---

## Phase 0 — Preflight (tools)

1. Identify the input file(s) and their formats.
2. Run `python3 scripts/preflight.py --target <tag> [--source <tag>]`. It reports which CLIs,
   Python modules, OCR language packs and fonts exist. Do not assume any tool exists.
3. Prefer tools already installed. Do not install anything already present or not needed.
4. If something required is missing, tell the user: the tool name, why it is needed, what it
   will be used for, and ask before installing (unless the user already authorized installs).
5. Never send document content to paid or third-party services.

## Phase 1 — Analysis (know the document before touching it)

Record, internally:

| Item | Why it matters |
|---|---|
| File type, pages/slides/sheets, sections | Choose the format route (`formats.md`) |
| Approximate word count | Decide batching |
| Source language (detect; respect `--from`) | Load the source profile if not English |
| Domain and audience (respect `--domain`) | Register, terminology, tone |
| Tables, lists, footnotes/endnotes, headers/footers, captions, references | Structure to preserve |
| Images — and which contain text | They stay untouched (`preservation-rules.md` §3) |
| Code, formulas, placeholders, tags | Do-not-translate inventory |
| PDF type: text / scanned / mixed | Whether OCR is required |
| Fonts and direction needed by the target | RTL? CJK? Indic shaping? |

For PDFs decide: **A. text-based**, **B. scanned/image**, **C. mixed**. OCR only the body text
of B/C pages, with the source language pack (`tesseract --list-langs`).

## Phase 2 — Extraction

Extract content into an internal representation that keeps structure:
section → heading level → paragraph → list item → table cell → caption → footnote → reference,
plus page/slide/sheet location, and image positions (marked, left untouched).

- DOCX/PPTX/XLSX: use `scripts/office_segments.py extract` (keeps inline formatting as tags).
- Other formats: see `formats.md`.
- Number every segment. The segment count is the contract: the output must have the same count.

## Phase 3 — Terminology and style sheet

Before translating a single paragraph:

1. Build the term map (source → target) as described in `terminology.md`. Load `--glossary` first; it wins.
2. Write a short **style sheet** (keep it in working notes, see `templates/style-sheet-template.md`):
   - target variant and register (from the language profile, `--formal`/`--casual`)
   - how names, products and acronyms are handled
   - number/date policy (source format, or localized with `--localize`)
   - quotation marks, list punctuation, heading capitalization for the target
   - first-occurrence policy for keeping the source term in parentheses
3. For long documents, save the term map and style sheet to files in the working directory, so
   later batches stay consistent even when earlier text has left the context.

## Phase 4 — Translation

- Translate everything, in order. Do not skip sections, repeated boilerplate, footnotes, table
  cells, alt text, chart labels that are text (not images), headers/footers or captions.
- Work in **batches of coherent units** (a section, ~800–1500 words, or ~60–120 segments). Before
  each batch re-read the term map and style sheet. After each batch, add any new terms.
- Translate **meaning in context**, then shape it into the target's natural syntax using the
  language profile. Read the whole paragraph before translating its first sentence.
- Keep inline tags/placeholders exactly (`<g1>…</g1>`, `<x3/>`, `{name}`, `%s`), moving them
  only as far as target word order requires.
- Ambiguity: decide from context. If it remains ambiguous, choose the reading best supported by
  the document, translate faithfully, and log it for the report. Never invent.
- Several targets: translate each from the source. Share only the analysis, never the output.

### Phase 4b — Humanize (only with `--humanize`)

After the translation is complete and terminology is final, run `humanizer.md` on the target
text, segment by segment, inside the meaning lock. Re-run Phase 6 afterwards — humanizing must not
break numbers, tags or terms.

## Phase 5 — Reconstruction

Rebuild the output in the closest practical format (`formats.md`):
- same structure and segment order, same tables (rows × columns), same lists and numbering
- images reinserted byte-identical, same position and size
- target direction (RTL for `ar`, `ur`), target fonts that cover the script, language metadata
- output name `name_<TAG>.ext`; the original file is never written to

## Phase 6 — Automated validation

Run, and fix what they find:

```bash
python3 scripts/qa_check.py SOURCE TARGET --target <tag>            # text-like files
python3 scripts/qa_check.py --segments src.json tr.json --target <tag>   # office segments
python3 scripts/glossary_check.py GLOSSARY.csv SOURCE TARGET        # when a glossary exists
```

Then check manually what scripts cannot see: missing/duplicated paragraphs, heading levels,
table logic, image positions, broken references, untranslated text that should be translated
(text inside images is excluded — it must stay as is).

## Phase 7 — Mandatory second review

Do not declare success after the first pass. Run `quality-review.md` in full: a separate,
deliberate re-read of the target against the source, with error classification and fixes.
For high-stakes documents (legal, medical, financial, contracts, safety) and when subagents are
available, the second review is done by an independent agent that did not produce the translation.

## Phase 8 — Report and delivery

Write the report with `templates/report-template.md`. Deliver the output file(s) plus the
report. Be precise about what was verified and how; state limitations plainly.

---

## Batch / multi-file jobs

- Keep the input directory tree; write outputs to a sibling folder (e.g. `out_AR/…`).
- One shared term map across all files of the same project.
- Process smallest-first to stabilize terminology, then the rest.
- Report per file plus a summary table.

## When to stop and ask

- The file cannot be read or extracted reliably (corrupted, encrypted, unreadable scan).
- The user's tags contradict each other (`--formal --casual`).
- The requested output format cannot be produced with available tools and an install is needed.
- A decision is irreversible (overwriting something) — never do it without consent.
