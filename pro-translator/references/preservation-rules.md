# Preservation rules — what must never change

These rules apply to every language and every format. Violations are CRITICAL errors.

## 1. Never translate (keep byte-identical)

| Category | Examples |
|---|---|
| Code blocks and inline code | ```` ```python … ``` ````, `` `npm install` `` |
| Commands, shell lines | `git clone …`, `pip install -r requirements.txt` |
| File names, paths, extensions | `C:\Users\data.csv`, `/etc/nginx/nginx.conf`, `.docx` |
| URLs, URIs, emails | `https://example.com/a?b=c`, `info@example.com` |
| API names, endpoints, keys | `GET /v2/users/{id}`, `api_key` |
| Variables, functions, classes, config keys | `calculate_score()`, `MAX_RETRIES`, `user.name` |
| Placeholders and format specifiers | `{name}`, `{{count}}`, `%s`, `%1$d`, `$VAR`, `${var}`, `:param`, `<0>…</0>` |
| Markup tags and attributes | `<b>`, `<a href="…">`, `class="…"` (translate only human-readable text and `alt`/`title`) |
| Formulas and equations | `E = mc^2`, `\frac{a}{b}`, `=SUM(A1:A10)` |
| Identifiers | DOI, ISBN, ISSN, patent numbers, part numbers, SKUs, version numbers, hashes |
| Programming languages, software, products | Python, Excel, Kubernetes, iPhone |

Translate the prose **around** these elements, never inside them. Comments inside code stay in
the source language unless the user explicitly asks to translate code comments.

## 2. Names and proper nouns

- **Personal names**: keep in the original form for Latin-script targets. For non-Latin targets
  (ar, ur, zh, ja, ko, ru, hi, bn) use the established transliteration if one exists
  (e.g. well-known public figures), otherwise transliterate by the profile's convention and add
  the original in parentheses on first occurrence: `جون سميث (John Smith)`.
- **Companies, brands, products, software**: keep the official name. Use a local official name
  only if the company itself uses one in that market.
- **Organizations and institutions**: use the official target-language name if one exists
  (UN → الأمم المتحدة / Naciones Unidas / 联合国); otherwise translate descriptively and keep the
  original acronym: `منظمة الصحة العالمية (WHO)`.
- **Places**: use the conventional exonym of the target language (London → لندن, Londres, 伦敦).
- **Titles of works**: use the published translation if one exists; otherwise translate and keep
  the original title in parentheses on first occurrence.

## 3. Images containing text — DO NOT TOUCH

Never modify, redraw, overlay, inpaint, crop, resize, recompress or translate images with text:
screenshots, diagrams/charts exported as images, scanned figures, logos, banners, infographics.

- Keep each image byte-identical, in the same position, at the same size.
- Do not OCR these images to replace their text.
- Translate the caption, figure number text and references to the figure (they are text).
- Do not add translations of the image text into the body unless the user asks.
- Report: number of images kept untouched, and how many contain source-language text.
- Native charts (DOCX/PPTX/XLSX chart objects with text labels stored as text) are **not**
  images; their titles/labels are translatable text. When in doubt, leave untouched and report.

## 4. Numbers, dates, units, money

- Never change a value. `25.6 kg` stays `25.6 kg` unless the user requests unit conversion.
- Never round, never "fix" a number that looks wrong — flag it in the report instead.
- Default: keep the source number format. With `--localize`, adapt *format only*:
  decimal/thousands separators, digit system, date order, currency symbol position — following
  the target profile. A localized date must stay unambiguous (spell out the month if needed).
- Percentages, ranges and signs keep their logic (`10–15 %`, `−3`, `±0.5`).
- Phone numbers, IDs, codes, version numbers, years in references: never localized.
- Keep digits in LTR order inside RTL text (direction handling, not reordering).

## 5. Tables

- Same number of tables, rows and columns; same merged cells; same header rows; same order.
- Translate cell text only. Numbers in cells follow §4.
- Never merge, split, drop, duplicate or reorder rows/columns.
- For RTL targets in formats that support it, the table may be mirrored visually
  (column order displayed right-to-left) — the logical order of data stays the same.

## 6. Structure and hierarchy

Preserve: title → chapter → section → subsection → paragraph; heading levels; numbered sections;
bullet and numbered lists (same items, same nesting); captions; footnotes/endnotes (same markers
and numbering); cross-references ("see Section 3.2" → keep 3.2); tables of contents (regenerate
from translated headings when possible); page/section breaks; headers/footers.

## 7. References and citations

- Keep citation markers and numbering exactly: `[12]`, `(Smith, 2020)`, superscripts.
- Bibliography: keep authors, titles in their original language, journal names, volume, issue,
  pages, years, DOI, URLs. Translate only connective words if the target style needs them
  (e.g. "Retrieved from", "et al." per profile) — or leave the bibliography as is; state choice.
- Legal citations, article numbers and clause numbers are never renumbered.

## 8. Inline markup and segment tags

When text is extracted with tags (`office_segments.py`):
- `<gN>…</gN>` = a formatting run (bold, italic, color, link …). Keep each pair, translate its
  inner text, move it so the formatting lands on the equivalent words.
- `<cN>…</cN>` = a container (hyperlink, field result). Keep it; translate inner text.
- `<xN/>` = an object (image, tab, break, field code, footnote mark). Keep every one, unchanged.
- Never add, drop, renumber or nest tags differently. Text outside tags takes the format of `g1`.

## 9. Things that must be translated (common misses)

Alt text of images, table headers, chart titles stored as text, captions, footnotes, headers and
footers, text boxes, slide notes, form field labels, hyperlink display text (not the URL),
document title metadata (when the format exposes it), bookmarks/TOC entries, spreadsheet sheet
names (only if the user wants and no formula references break — default: keep sheet names).
