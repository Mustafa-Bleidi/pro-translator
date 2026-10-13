<div align="center">

# 🌍 Pro Translator — a Claude Skill

**Professional document translation across 15 world languages: simple tags, format preservation, consistent terminology, a mandatory second review and a natural-writing humanizer.**

![Languages](https://img.shields.io/badge/languages-15-blue)
![Formats](https://img.shields.io/badge/formats-PDF%20%7C%20DOCX%20%7C%20PPTX%20%7C%20XLSX%20%7C%20MD%20%7C%20HTML%20%7C%20SRT-green)
![Python](https://img.shields.io/badge/python-3.9%2B-yellow)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

[العربية](README.ar.md) · English

</div>

---

## What it does

Write a tag such as `--ar`, `--es` or `--ja` together with a file or text. Claude then translates it like a professional agency would:

- **Meaning first.** The skill does not translate word for word. The output reads as if it had been written in the target language.
- **Formatting survives.** DOCX, PPTX and XLSX are edited at the XML level, so styles, tables, images, headers, footers and footnotes stay intact. RTL is set up automatically for Arabic and Urdu.
- **Nothing breaks.** Numbers, code, URLs, placeholders, formulas and citations are protected and checked by scripts.
- **One term, one translation** across the whole document. User glossaries are supported.
- **Mandatory second review**, errors classified as CRITICAL, MAJOR or MINOR, and a verification report.
- **`--humanize`** rewrites the output so it reads like natural native writing, without changing the meaning.
- **Images that contain text are never touched.**

## Supported languages

The 15 languages below cover most of the world's speakers.

| Tag | Language | Native | Variants |
|---|---|---|---|
| `--ar` | Arabic (MSA) | العربية | — |
| `--en` | English | English | `--en-us` · `--en-gb` |
| `--zh` | Chinese | 中文 | `--zh-cn` · `--zh-tw` · `--zh-hk` |
| `--es` | Spanish | Español | `--es-419` · `--es-es` · `--es-mx` |
| `--hi` | Hindi | हिन्दी | — |
| `--fr` | French | Français | `--fr-fr` · `--fr-ca` |
| `--pt` | Portuguese | Português | `--pt-br` · `--pt-pt` |
| `--ru` | Russian | Русский | — |
| `--bn` | Bengali | বাংলা | `--bn-bd` · `--bn-in` |
| `--ur` | Urdu | اردو | `--ur-pk` · `--ur-in` |
| `--id` | Indonesian | Bahasa Indonesia | — |
| `--de` | German | Deutsch | `--de-de` · `--de-ch` · `--de-at` |
| `--ja` | Japanese | 日本語 | — |
| `--tr` | Turkish | Türkçe | — |
| `--ko` | Korean | 한국어 | — |

Aliases also work: `--arabic`, `--عربي`, `--español`, `--中文` and so on. Translation works from **any** of these languages into any other. The source language is detected automatically, or you can force it with `--from=xx`.

## Modifier tags

| Tag | Effect |
|---|---|
| `--humanize` | Natural native-sounding rewrite (`=light`, standard, `=deep`). Can be used alone, without translating |
| `--from=xx` | Force the source language |
| `--formal` / `--casual` | Override the register |
| `--domain=legal\|medical\|tech\|academic\|business\|marketing\|literary\|ui` | Force the domain |
| `--localize` | Adapt number, date and quote formats to the locale (values never change) |
| `--glossary=FILE.csv` | Enforce your terminology |
| `--bilingual` | Source and translation side by side |
| `--review` | Review an existing translation instead of translating |
| `--quick` / `--report` | Short pipeline / force the full verification report |

## Examples

```text
/pro-translator --ar report.pdf
/pro-translator --es --fr --de manual.docx            → three separate files
/pro-translator --ja --formal --domain=tech api-guide.md
/pro-translator --en --humanize   (paste Arabic text)
/pro-translator --humanize=deep   (paste English text, no translation)
/pro-translator --ar --glossary=terms.csv --report contract.docx
/pro-translator --review --from=en --tr original.docx translated.docx
```

You can also just ask: *"translate this into Korean --ko --humanize"*.

## Installation

**Claude Code**

```bash
git clone https://github.com/Mustafa-Bleidi/pro-translator.git
cp -r pro-translator/pro-translator ~/.claude/skills/         # personal skill
# or, for one project only:
cp -r pro-translator/pro-translator .claude/skills/
```

**Claude apps (web / desktop)**: zip the inner `pro-translator/` folder (the zip contains `pro-translator/SKILL.md`) and upload it as a custom skill. A ready-made `pro-translator.zip` is attached to each GitHub release.

Optional Python tools used by the helper scripts: `pip install lxml python-docx python-pptx openpyxl`. The QA scripts need only the standard library.

## Repository layout

```
pro-translator/                     ← the skill (this folder is what gets installed)
├── SKILL.md                        ← entry point: tags, routing, non-negotiable rules
├── references/
│   ├── workflow.md                 ← 8-phase pipeline (preflight → report)
│   ├── preservation-rules.md       ← what must never change
│   ├── formats.md                  ← PDF/DOCX/PPTX/XLSX/HTML/MD/SRT/JSON/PO handling, RTL & fonts
│   ├── terminology.md              ← glossary building, consistency, domain notes
│   ├── quality-review.md           ← second pass, error classes, scoring
│   └── humanizer.md                ← --humanize method, meaning lock, tells, techniques
├── languages/                      ← one profile per language (loaded only when needed)
│   ├── ar.md en.md zh.md es.md hi.md fr.md pt.md ru.md
│   ├── bn.md ur.md id.md de.md ja.md tr.md ko.md
│   └── _TEMPLATE.md                ← copy to add a language
├── scripts/
│   ├── preflight.py                ← which tools / OCR packs / fonts exist (installs nothing)
│   ├── office_segments.py          ← lossless DOCX/PPTX/XLSX extract ↔ apply (+ RTL, language tags)
│   ├── qa_check.py                 ← numbers, URLs, code, placeholders, tags, structure, residue …
│   └── glossary_check.py           ← terminology consistency
└── templates/
    ├── report-template.md
    ├── glossary-template.csv
    └── style-sheet-template.md
tests/                              ← unit tests + fixtures (run in CI)
examples/                           ← usage walkthroughs
```

**Why so many files?** Claude loads only what a task needs: `SKILL.md`, the workflow, and the profile of the target language. A Japanese job never loads the Urdu rules. This keeps the context focused and the instructions precise.

## How it works

```
Preflight → Analysis → Extraction → Terminology & style sheet → Translation
   → (Humanize) → Reconstruction → Automated QA → Second review → Report
```

Office files go through a segment round-trip:

```bash
python3 scripts/office_segments.py extract report.docx -o report.segments.json
#   … Claude translates each segment and keeps the inline tags <g1>…</g1>, <c1>…</c1>, <x1/> …
python3 scripts/qa_check.py --segments report.segments.json report.tr.json --target ar
python3 scripts/office_segments.py apply report.docx report.tr.json -o report_AR.docx --lang ar
```

`--lang ar` sets paragraph and run direction, mirrors tables, and copies bold, italic and size into the complex-script slots, which Word needs for Arabic, Urdu, Hindi and Bengali. It also tags the language for spell-check. Images are copied byte-for-byte.

## About `--humanize`

The humanizer removes the patterns that make text feel machine-written: calqued word order, stacked connectors ("Furthermore… Moreover…"), inflated vocabulary, uniform rhythm, formulaic openers and closers. It rewrites with native information flow, rhythm and collocations. Each language profile lists the typical tells for that language.

It works under a strict **meaning lock**: no new facts, no lost caveats, terminology unchanged. It also refuses quality-damaging tricks such as deliberate typos, invisible characters or look-alike letters. The goal is genuinely good writing. AI detectors are unreliable and can flag human text too, so the skill makes no promises about any detector's score.

## Run the tests

```bash
python3 -m unittest discover -s tests -v
```

## Contributing

New languages, better language rules and more format handlers are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md). To add a language, copy `languages/_TEMPLATE.md`, fill in every section, and register the tag in `SKILL.md`, `qa_check.py` and `preflight.py`.

## License

[MIT](LICENSE)
