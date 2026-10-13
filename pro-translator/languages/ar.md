# Arabic (Modern Standard Arabic) — `--ar`

| Field | Value |
|---|---|
| Tag | `--ar` |
| Aliases | `--arabic`, `--عربي`, `--العربية`, `--ara` |
| Variants | MSA (فصحى معاصرة) only; dialects only on explicit request |
| BCP 47 | `ar` (metadata: `ar-SA` or the user's country if known) |
| Script / direction | Arabic / **RTL** |
| Tesseract OCR pack | `ara` |
| Fonts | Noto Naskh Arabic, Amiri, Noto Sans Arabic, Dubai, Tajawal (UI) |
| Typical length vs English | +10–25 % characters (fewer words, longer words) |

## 1. Default variant and register
- Modern Standard Arabic, professional and clear — not classical, not dialect.
- Address the reader impersonally or with plural/neutral forms in documents
  (يُرجى، يمكنك/يمكنكم). For UI, use the singular masculine imperative by convention
  (اضغط، اختر) unless the user's style guide says otherwise, or neutral forms (الضغط على…).
- `--casual` = light, friendly MSA (still no dialect). Dialect (Egyptian, Gulf, Levantine,
  Maghrebi) only if the user names it.

## 2. Typography and punctuation
- Arabic punctuation: comma `،`, semicolon `؛`, question mark `؟`. Full stop `.`, colon `:`,
  exclamation `!` are shared.
- No space before punctuation; one space after. Quotes: «…» or "…" — choose one and keep it.
- Keep Latin terms, numbers, code and URLs as LTR runs inside RTL text; never reverse them.
- Parentheses mirror automatically in RTL; type them logically `(…)`.
- Tatweel/kashida (ـ) is not used for justification in professional text.
- Diacritics (tashkeel): none in normal text; add a single mark only where a word is genuinely
  ambiguous in context (عِلْم / عَلَم, يُعدّ / يَعُدّ) or when the source is for learners.
- Lists in RTL: bullets and numbers on the right; numbering stays 1, 2, 3 (or أ، ب، ج if the source uses a, b, c).

## 3. Numbers, dates, currency
- Default digits: Western Arabic `0123456789` (standard in most technical, business and digital
  content, and the source format). With `--localize` for audiences that prefer them (e.g. Egypt,
  Gulf print media) Eastern Arabic `٠١٢٣٤٥٦٧٨٩` may be used — consistently, never mixed.
- Decimal separator: keep source `.`; with `--localize` + Eastern digits use `٫` and thousands `٬`.
- Percent: `25%` or `25 بالمئة` in prose; keep the source style in tables.
- Dates: `13 أكتوبر 2026` (Egypt/Gulf month names) or `13 تشرين الأول 2026` (Levant/Iraq) —
  pick by audience; default to the Egypt/Gulf names (يناير، فبراير…) with Western digits.
- Currencies: keep codes/symbols (USD, $, €); amounts unchanged: `1,250 دولارًا`.
- Number–noun agreement (العدد والمعدود) must be correct when numbers are written as words
  (ثلاثة كتب، ثلاث سيارات). Prefer digits in technical text to avoid errors.

## 4. Grammar and style rules
- Prefer the active voice with a real subject. Avoid overusing the passive construction
  `يتم + مصدر` (يتم تنفيذ العملية) — use a direct verb (تُنفَّذ العملية / ينفّذ النظام العملية).
- Avoid `من قِبَل` to introduce the agent of a passive (calque of "by"); rewrite actively.
- Avoid `قام بـ + مصدر` (قام بتحليل) → use the verb (حلّل).
- Avoid chains of إضافة that become unreadable; split with `الخاصة بـ` sparingly — rather
  restructure.
- Verb–subject agreement: verb before a plural subject is singular (حضر الطلابُ); gender agreement
  with non-human plurals is feminine singular (الملفات محفوظة).
- Correct hamza (إ/أ/ؤ/ئ/ء), ta marbuta vs ha (ة/ه), alif maqsura vs ya (ى/ي) — never interchange.
- Tanween on accusative where needed in standard writing: `شكرًا`، `دولارًا`.
- Use `و` naturally to link clauses but avoid 6+ chained `و` clauses; split sentences.
- Headings: no full stop at the end; no title case concept.

## 5. Terminology conventions
- Use established Arabic terms (Arab academies, ITU/UN terminology, Microsoft/Apple Arabic
  localization) when they exist: البرمجيات، الخوارزمية، قاعدة البيانات، الحوسبة السحابية.
- First technical occurrence: Arabic term + English in parentheses — `التعلم الآلي (Machine Learning)`.
- Acronyms: keep Latin acronyms in technical text (API، CPU، AI) or write the Arabic expansion
  with the acronym in parentheses on first use.
- Transliterate names by sound, using established forms: جون، مايكروسوفت، كاليفورنيا.

## 6. Traps
- "Actually" ≠ في الواقع always — often فعلًا / بل. "Eventually" = في نهاية المطاف/لاحقًا (not بشكل احتمالي).
- "Control" in IT/UX = تحكّم, in audit = رقابة/ضوابط. "Policy" = سياسة; "policy (insurance)" = وثيقة تأمين.
- "Library" (software) = مكتبة برمجية. "Platform" = منصة. "Feature" = ميزة (not خاصية in UI).
- "Role" → "plays a role" calque `يلعب دورًا` is acceptable but overused; prefer `يؤدي دورًا` / `يُسهم في`.
- "Based on" → `استنادًا إلى / بناءً على`, avoid `بناءً على ذلك` at every sentence start.
- "Make sure" → `تأكّد من` (not اصنع متأكدًا). "Take into account" → `مراعاة`.
- Don't translate "you" in instructions with a pronoun every time — Arabic verbs already carry it.

## 7. Native style — humanizer notes
Remove these tells (MT/AI Arabic):
- Formulaic openers: `في عالمنا اليوم`، `في ظل التطورات المتسارعة`، `مما لا شك فيه`.
- Filler signposts: `تجدر الإشارة إلى أن`، `من الجدير بالذكر أن`، `ومن المهم أن نلاحظ أن` — keep at
  most one per document, or delete and state the point.
- Stacked connectors: `علاوة على ذلك`، `بالإضافة إلى ذلك`، `فضلًا عن ذلك` at every paragraph start.
- Clichés: `يلعب دورًا محوريًا`، `حجر الزاوية`، `نقلة نوعية`، `في الختام` closing every section.
- Excess `يتم`/`قام بـ`/`من قبل`, and overuse of `حيث` as a generic connector (`حيث أن`).
Native connectors to vary by meaning: `إذ`، `بل`، `غير أنّ`، `لذا`، `ومن ثَمّ`، `أمّا… فـ`، `كما`،
`لكنّ`، `بينما`، `حتى`، `ف` (fa- for consequence), and often no connector at all.
Native rhythm: verbal sentences (فعلية) for narrative/action, nominal (اسمية) for definitions and
states; mix them. Use `أمّا … فـ` for contrast, `إنّ` for emphasis sparingly.

## 8. As a source language
- Long sentences linked by `و`: split into several English/target sentences.
- Pro-drop: recover the implied subject from verb morphology.
- Formulaic religious/courtesy phrases (بسم الله، إن شاء الله، تحية طيبة وبعد) — translate by
  function in the target (greeting/closing) or keep with a note, per register.
- Dual (المثنى) must become explicit "two/both".
- Arabic digits (٠-٩) map to the same values; keep values.

## 9. Final checklist
- [ ] RTL direction set in the output; Latin/numbers display correctly.
- [ ] Arabic punctuation ، ؛ ؟ used; no space before punctuation.
- [ ] Hamza, ة/ه, ى/ي correct; agreement (gender/number) correct.
- [ ] No `يتم`/`قام بـ`/`من قبل` overuse; natural verb-first sentences.
- [ ] Terms consistent; English in parentheses on first technical occurrence.
- [ ] Digits system consistent (one system throughout).
