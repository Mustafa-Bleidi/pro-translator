# Indonesian — `--id`

| Field | Value |
|---|---|
| Tag | `--id` |
| Aliases | `--indonesian`, `--bahasa`, `--bahasa-indonesia`, `--ind` |
| Variants | Standard Indonesian (bahasa baku); Malay (`ms`) is a different target |
| BCP 47 | `id-ID` |
| Script / direction | Latin / LTR |
| Tesseract OCR pack | `ind` |
| Fonts | Any Latin font |
| Typical length vs English | +10–25 % |

## 1. Default variant and register
- Bahasa Indonesia baku per **EYD V** (Ejaan yang Disempurnakan, 2022) and **KBBI** spellings.
- Address: **Anda** (capital A) in formal/UI/business; `kamu` in casual brand voice;
  `Bapak/Ibu` in letters and formal address.
- Avoid Jakarta colloquial (gue, nggak, banget) unless the brand voice asks for it.

## 2. Typography and punctuation
- Quotes “ ”. Headings: title case is common in Indonesian titles (except particles and
  conjunctions: di, ke, dari, dan, yang, untuk) — follow EYD for titles; sentence case for UI.
- Prefix `di-` (passive) is attached (`dikirim`), preposition `di` is separate (`di rumah`) —
  the most common spelling error.
- Same for `ke-`: `ketua` (affix) vs `ke kantor` (preposition).
- Reduplication with hyphen: `buku-buku`, `kupu-kupu`.
- Foreign terms not yet absorbed: italic in published text.

## 3. Numbers, dates, currency
- Decimal comma, thousands point: `1.250,75`.
- Dates: `13 Oktober 2026`, `13/10/2026`; months capitalized (Januari, Februari … Desember).
- Currency: `Rp1.250.000` (no space per EYD) or `Rp 1.250.000` (common) — consistent.
- Percent: `25%`.

## 4. Grammar and style rules
- No tense inflection: use time words (sudah, sedang, akan) only when needed.
- No plural inflection: don't reduplicate when a number or quantifier exists
  (`tiga buku`, not `tiga buku-buku`; `banyak pengguna`, not `banyak pengguna-pengguna`).
- Passive `di-` is natural in Indonesian, more than in English — but avoid chains.
- `yang` relative clauses: keep them short; don't stack.
- **Do not use `di mana` / `dimana` as a relative pronoun** for English "where/which"
  (`sistem di mana data disimpan` ✗ → `sistem tempat data disimpan` / `sistem yang menyimpan data`).
- `daripada` only for comparison (`lebih besar daripada`), not "than/of" calques.
- Instructions: `Klik`, `Pilih`, `Masukkan` (imperative) or `Silakan …` for polite UI.

## 5. Terminology conventions
- Use established Indonesian terms (Pusat Bahasa / KBBI, Microsoft Indonesian terminology):
  unduh (download), unggah (upload), surel/email, kata sandi, pengaturan, perangkat lunak
  (software, though "software" is common), basis data, peladen/server (server common).
- Absorbed spellings: sistem, aktivitas, analisis, kualitas, teknologi, efektif, praktik.
- Acronyms: Indonesian ones where established (PBB for UN, KTT for summit), else Latin.

## 6. Traps
- `di`/`ke` spacing (see §2).
- "Play a role" → `berperan` (verb) beats `memainkan peran` (calque).
- "Based on" → `berdasarkan`; "in order to" → `untuk/agar/supaya` (agar/supaya for purpose with subject).
- "Make sure" → `pastikan`.
- Don't overuse `adalah`/`merupakan` as copula; Indonesian often omits it.
- `Anda` capitalized; `anda` ✗.

## 7. Native style — humanizer notes
Remove tells: `Di era modern ini` / `Di era digital saat ini`, `Penting untuk dicatat bahwa`,
`Perlu diketahui bahwa`, `Selain itu,` / `Lebih lanjut,` / `Di samping itu,` at every paragraph,
`memainkan peran penting`, `Kesimpulannya,` closing sections, `dimana` relatives,
`merupakan` everywhere, stacked triads.
Native connectors: `jadi`, `namun`, `tetapi`, `karena itu`, `sehingga`, `bahkan`, `yaitu`,
`padahal`, `meskipun`. Prefer verbs with affixes over noun phrases
(`menganalisis` vs `melakukan analisis`).

## 8. As a source language
- No tense/plural marking — infer from context; target languages need explicit choices.
- `di-` passive often maps to active in English.
- Reduplication can mean plurality, variety or intensity — read in context.

## 9. Final checklist
- [ ] EYD V spelling; `di`/`ke` attached vs separate correctly.
- [ ] No `dimana` relatives; no redundant plurals.
- [ ] Anda capitalized; register consistent.
- [ ] Number/currency format consistent (if `--localize`).
