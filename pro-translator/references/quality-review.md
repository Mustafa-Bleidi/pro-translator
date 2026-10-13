# Quality review — mandatory second pass, error classes, final verification

The first draft is never the deliverable. This review is a separate, deliberate pass that
compares the target against the source. It is also the whole job when the user writes `--review`.

## 1. How to run the second pass

1. Re-open the **source** and the **target** side by side, segment by segment (or paragraph by
   paragraph). Do not review the target alone — fluent text can still be wrong.
2. Read the target once **as a native reader** of the target language, without the source,
   marking anything that sounds translated (calques, wrong register, unnatural order).
3. Check the hard items with tools (`qa_check.py`, `glossary_check.py`), then by eye.
4. Fix, then re-run the scripts. Repeat until no CRITICAL or MAJOR issues remain.
5. High-stakes content (legal, medical, financial, safety, publication): when subagents exist,
   give an independent reviewer agent the source, the target, the language profile and this
   file, and have it report issues without seeing your reasoning. Fix what it finds.
6. Optional for high stakes: back-translate 3–5 critical passages (definitions, obligations,
   dosages, warnings) mentally into the source language and compare meaning.

## 2. Checklist

**Fidelity**
- [ ] Every sentence of the source is present; nothing added; nothing summarized.
- [ ] Negations, conditions, modality (must/should/may), quantifiers (all/some/none), tense and
      aspect, and hedging preserved exactly.
- [ ] Who-does-what (agent/patient) unchanged — passives did not hide or swap the actor.
- [ ] Technical concepts correct for the domain; no false friends.
- [ ] Ambiguities resolved from context and logged.

**Hard content**
- [ ] All numbers, dates, percentages, units, currencies, formulas identical in value.
- [ ] Names, products, code, URLs, emails, placeholders, tags identical.
- [ ] Citations, footnote markers, cross-references intact.

**Terminology**
- [ ] Glossary/term map applied everywhere; no synonyms for defined terms.
- [ ] First-occurrence parentheses policy applied as decided.

**Target language quality** (use the language profile's checklist)
- [ ] Grammar, agreement, spelling, diacritics, punctuation of the target.
- [ ] Natural word order and information flow; no source-language syntax.
- [ ] Register consistent (formal/informal address chosen once and kept).
- [ ] Typography: quotes, spacing rules, capitalization rules of the target.

**Structure and formatting**
- [ ] Heading levels, lists, tables (rows × columns), captions, notes, references preserved.
- [ ] Images untouched: same count, position, size; none altered.
- [ ] Direction (RTL/LTR), alignment, fonts render without tofu boxes; no overflow.
- [ ] Headers/footers, page breaks, TOC.

## 3. Error classification

| Class | Examples | Action |
|---|---|---|
| **CRITICAL** | Missing/added content; wrong meaning of an obligation, warning, dose, figure; wrong number/formula/date; corrupted or missing table; missing section; image with text altered or removed; code/URL/placeholder broken; file won't open | Must fix before delivery |
| **MAJOR** | Wrong or inconsistent terminology; significant mistranslation of a non-critical sentence; wrong register for the audience; structural problem (heading level, list nesting); broken cross-reference; untranslated paragraph | Must fix before delivery |
| **MINOR** | Punctuation, spacing, typographic conventions; stylistic awkwardness; minor grammar slip that does not change meaning | Fix when practical; count in report |

## 4. Scoring (for the report)

Give each dimension an honest rating (★1–5) with one line of evidence:
Fidelity · Hard-content accuracy · Terminology · Naturalness · Structure · Formatting.
Never rate 5 without having verified it, and never claim "100 % accurate".

## 5. Visual verification

When a render is possible (PDF, DOCX, PPTX, HTML), inspect representative pages: first, middle,
last, every page with tables, complex formatting, images, and RTL/CJK/Indic text. If visual
inspection is not possible, say so explicitly in the report.

## 6. `--review` mode output

1. Summary verdict (usable as is / usable after fixes / needs retranslation).
2. Issue table: location · source · current translation · problem · class · suggested fix.
3. Corrected file (if the user wants fixes applied) — never overwrite their file; write `name_REVIEWED.ext`.
4. Scores as in §4.
