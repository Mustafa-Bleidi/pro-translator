# Urdu — `--ur`

| Field | Value |
|---|---|
| Tag | `--ur` |
| Aliases | `--urdu`, `--اردو`, `--urd` |
| Variants | Standard Urdu (Pakistan default; India on request `--ur-in`) |
| BCP 47 | `ur-PK`, `ur-IN` |
| Script / direction | Perso-Arabic (Nastaliq preferred) / **RTL** |
| Tesseract OCR pack | `urd` |
| Fonts | Noto Nastaliq Urdu, Jameel Noori Nastaleeq, Noto Naskh Arabic (fallback/technical) |
| Typical length vs English | +15–25 % |

## 1. Default variant and register
- Standard written Urdu as in quality newspapers and official documents.
- Vocabulary: balanced — Persian/Arabic-origin words for formal registers, but avoid archaic
  ornate style; common English loans in Urdu script for tech (کمپیوٹر، سافٹ ویئر، ای میل).
- Address: **آپ** with plural verb forms always in professional text; تم only casual; never تو.

## 2. Typography and punctuation
- Full stop: **۔** (Urdu full stop, U+06D4) — not the Latin period.
- Comma `،`, semicolon `؛`, question mark `؟`. Quotes “ ” or « ».
- RTL direction; Latin terms, numbers and URLs as LTR runs.
- Use Urdu-specific letters correctly: ٹ ڈ ڑ ں ھ ے ی ۂ ۓ — do not substitute Arabic ي/ه/ك
  (use ی U+06CC, ہ U+06C1, ک U+06A9). This matters for search and rendering.
- Do-chashmi he `ھ` only in aspirates (بھی، کھانا); gol he `ہ` elsewhere.
- Bari ye `ے` at word end for ے-sounds (ہے، کے) vs choti ye `ی` (ہی، کی).

## 3. Numbers, dates, currency
- Western digits `0–9` are common in modern print and digital text; Extended Arabic-Indic
  digits `۰۱۲۳۴۵۶۷۸۹` (Urdu forms — not Arabic ٠١٢) with `--localize` if the audience expects them.
  Keep one system.
- Lakh/crore grouping with `--localize` (Pakistan uses lakh/crore and also million/billion in
  business — keep the source unit unless asked).
- Dates: `13 اکتوبر 2026` (months: جنوری، فروری، مارچ، اپریل، مئی، جون، جولائی، اگست، ستمبر، اکتوبر، نومبر، دسمبر).
- Currency: `Rs. 1,250` / `1,250 روپے` (PKR).

## 4. Grammar and style rules
- SOV; postpositions (میں، پر، سے، کو، کے لیے). Verb at the end.
- Gender agreement (verbs, adjectives, postposition کا/کی/کے) — assign gender to loanwords
  by convention (فائل f., کمپیوٹر m., ویب سائٹ f.).
- Ergative `نے` with perfective transitive verbs.
- Izafat (Persian construct) `ِ`: use established ones (وزیرِ اعظم، حقوقِ انسانی); don't create
  long izafat chains.
- Avoid literal passive chains (`کے ذریعے کیا گیا`); use active voice.
- Instructions: polite imperative `کلک کریں`، `منتخب کریں`، `درج کریں`.

## 5. Terminology conventions
- Official Pakistani terminology (National Language Promotion Department / ادارۂ فروغِ قومی زبان)
  for government texts; common loans for tech.
- First technical occurrence: Urdu term + English in parentheses — `مصنوعی ذہانت (Artificial Intelligence)`.

## 6. Traps
- Don't write Urdu with Arabic letter forms (ي ك ه) — wrong Unicode, broken search.
- Formal Urdu draws on Persian/Arabic-origin vocabulary, not Sanskrit-origin Hindi words
  (استعمال، اطلاع، حفاظت — not Hindi प्रयोग, सूचना, सुरक्षा transliterated).
- "Play a role" → `کردار ادا کرنا` — fine but overused; vary: `اہم ہونا`، `حصہ ڈالنا`.
- Don't add pronouns where verb agreement already shows the subject.

## 7. Native style — humanizer notes
Remove tells: `آج کے جدید دور میں`، `یہ بات قابلِ ذکر ہے کہ`، `اس کے علاوہ` / `مزید برآں` at every
sentence start, `اہم کردار ادا کرتا ہے` everywhere, `خلاصہ کلام یہ کہ` closing sections, over-Persianized
ornate vocabulary in plain contexts, mechanical passives.
Native connectors: `لہٰذا`، `لیکن`، `تاہم`، `بلکہ`، `یعنی`، `کیونکہ`، `جبکہ`، `چنانچہ`، `پھر بھی`.

## 8. As a source language
- Honorific plural ≠ plural; gender agreement shows who acts.
- Lakh/crore conversions exact.
- Persian/Arabic vocabulary may be formal — choose target register accordingly.

## 9. Final checklist
- [ ] RTL set; Nastaliq (or Naskh) font renders; Latin/numbers display correctly.
- [ ] ۔ ، ؟ used; Urdu letter forms (ی ک ہ) — not Arabic forms.
- [ ] آپ + plural verbs; gender agreement correct.
- [ ] Digit system consistent; numbers unchanged.
