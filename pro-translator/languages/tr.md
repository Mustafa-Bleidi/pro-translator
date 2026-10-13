# Turkish — `--tr`

| Field | Value |
|---|---|
| Tag | `--tr` |
| Aliases | `--turkish`, `--türkçe`, `--turkce`, `--tur`, `--تركي` |
| Variants | Standard Turkish (Türkiye) |
| BCP 47 | `tr-TR` |
| Script / direction | Latin (with ç ğ ı İ ö ş ü) / LTR |
| Tesseract OCR pack | `tur` |
| Fonts | Any Latin font with Turkish glyphs |
| Typical length vs English | 0 to +20 % |

## 1. Default variant and register
- Standard Turkish per **TDK** (Türk Dil Kurumu) spelling guide (Yazım Kılavuzu).
- Address: **siz** (formal, plural verb forms) for business, legal, UI; **sen** in casual brand
  voice on request. Never mix.
- Avoid Ottoman-era/archaic Arabic-Persian vocabulary where modern Turkish words exist, and
  avoid unnecessary English (`toplantı` not "meeting").

## 2. Typography and punctuation
- **Dotted/dotless i**: `I ı` and `İ i` are different letters. Uppercase of `i` is `İ`
  (İSTANBUL), lowercase of `I` is `ı`. Never use English case conversion on Turkish text.
- Suffixes on proper nouns, acronyms and numbers are separated by an apostrophe:
  `Microsoft'un`, `Ankara'da`, `ABD'de`, `2026'da`, `5'inci`. Follow vowel harmony and the
  pronunciation of the word (`Excel'de`, `PDF'yi` pronounced pe-de-fe → `PDF'yi`).
- Do **not** put an apostrophe on common nouns: `şirketin`, not `şirket'in`.
- Quotes “ ” (or « » in some publishing). Sentence case for headings is common in modern UI;
  titles often capitalize each word — follow the document.
- `de/da` conjunction ("also") written separately (`Ben de geldim`); locative suffix attached
  (`evde`). `ki` conjunction separate; `-ki` suffix attached. `mi/mı/mu/mü` question particle separate.

## 3. Numbers, dates, currency
- Decimal comma, thousands point: `1.250,75`.
- Dates: `13 Ekim 2026`, `13.10.2026`; months capitalized when a specific date (13 Ekim) per TDK.
- Percent sign **before** the number: `%25` (Turkish convention) — apply with `--localize`;
  otherwise keep source but note TDK style.
- Currency: `1.250,75 TL` / `₺1.250,75`.
- Ordinals: `5.` or `5'inci`.

## 4. Grammar and style rules
- SOV; agglutinative suffixes in fixed order; vowel harmony (front/back, rounded/unrounded) for
  every suffix — check harmony on loanwords (`saati`, `rolü`, `analizi`).
- No grammatical gender; no articles (use `bir` only when "a/one" matters).
- Avoid long `-mektedir/-maktadır` formal endings in every sentence; use `-ır/-ir/-yor` or `-dır`
  where natural. Overuse sounds bureaucratic/MT.
- Avoid English-style relative clauses with `ki` ("Biliyorum ki…" style) — use participles
  (`-en/-an`, `-dığı`).
- Instructions: `Tıklayın`, `Seçin`, `Girin` (siz-imperative), or noun form in labels (`Kaydet`).

## 5. Terminology conventions
- Established Turkish IT terms (TDK/Microsoft): dosya, klasör, ayarlar, kaydet, indir, yükle,
  sunucu, veri tabanı, bulut, parola/şifre, kullanıcı hesabı, yapay zekâ.
- Acronyms: Turkish ones where established (BM for UN, AB for EU, ABD for USA, GSYH for GDP,
  DNA used), else Latin with apostrophe suffixes.
- Circumflex in established words: `yapay zekâ`, `hâlâ` (still) vs `hala` (aunt).

## 6. Traps
- Case conversion I/İ/ı/i errors (`DİKKAT`, not `DIKKAT`).
- Apostrophe rules (proper nouns only).
- "Play a role" → `rol oynamak` (OK) — overused; vary: `etkili olmak`, `katkı sağlamak`.
- "Make sure" → `emin olun`. "Based on" → `-e dayalı / -e göre`.
- Don't calque English passives with `tarafından` everywhere.

## 7. Native style — humanizer notes
Remove tells: `Günümüz dünyasında`, `Önemle belirtmek gerekir ki`, `Ayrıca,` / `Bunun yanı sıra,`
/ `Buna ek olarak,` at every paragraph, `önemli bir rol oynamaktadır`, `Sonuç olarak,` closing
sections, `-mektedir/-maktadır` in every sentence, `bu bağlamda` overuse, `tarafından` passives.
Native connectors: `ancak`, `fakat`, `bu yüzden`, `bu nedenle`, `yani`, `üstelik`, `oysa`,
`çünkü`, `hatta`. Verb-final flow; mix short sentences with participial ones.

## 8. As a source language
- Agglutinated words = whole phrases: `yapamayacaklarımızdan` ≈ "among those we will not be able to do".
- Evidential `-miş` (reported/inferred) — convey with "reportedly/apparently".
- No gender: `o` = he/she/it — decide from context.
- `%25` → 25%.

## 9. Final checklist
- [ ] I/İ/ı/i correct in all cases (especially UPPERCASE text).
- [ ] Apostrophes on proper nouns/acronyms/numbers only; vowel harmony of suffixes.
- [ ] siz/sen consistent; not every sentence ends in -mektedir.
- [ ] Number/percent/date formats per TDK when localized.
