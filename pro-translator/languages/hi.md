# Hindi — `--hi`

| Field | Value |
|---|---|
| Tag | `--hi` |
| Aliases | `--hindi`, `--हिन्दी`, `--हिंदी`, `--hin` |
| Variants | Standard Hindi (मानक हिंदी) |
| BCP 47 | `hi-IN` |
| Script / direction | Devanagari / LTR (complex shaping: conjuncts, matras) |
| Tesseract OCR pack | `hin` |
| Fonts | Noto Sans/Serif Devanagari, Mangal, Nirmala UI, Mukta, Hind |
| Typical length vs English | +15–30 % |

## 1. Default variant and register
- Contemporary standard Hindi as used in quality journalism, government and modern business —
  **not** heavily Sanskritized (शुद्ध) Hindi, and not Hinglish.
- Rule: when an English loan is what educated readers actually use (कंप्यूटर, मोबाइल, ईमेल,
  सॉफ़्टवेयर, इंटरनेट), use it in Devanagari. When a natural Hindi word is in common use
  (सूचना, सुरक्षा, खाता, भुगतान), use the Hindi word.
- Government/legal: follow official terminology (राजभाषा / CSTT glossaries) — more formal vocabulary is expected.
- Address: **आप** with plural verb forms in all formal/professional text; तुम only for
  informal brand voice if asked; never तू.

## 2. Typography and punctuation
- Full stop: पूर्ण विराम **।** (danda). Questions `?`, exclamation `!`, comma `,` as in English.
- No space before `।`/`?`. Quotes “ ” or ‘ ’.
- Nukta for loan sounds where standard: ज़ (z), फ़ (f), ड़/ढ़ (native retroflex flaps) — be
  consistent (सॉफ़्टवेयर, फ़ाइल).
- Chandrabindu vs anusvara: हँसना (ँ) vs संस्था (ं) — modern usage allows ं in many places; be consistent.
- Chandra-o for English "o/aw" sounds: ऑफ़िस, डॉक्टर, कॉल.

## 3. Numbers, dates, currency
- Digits: international numerals `0–9` are standard in modern Hindi (official usage allows
  both). Devanagari digits `०–९` only with `--localize` if the audience expects them.
- Indian grouping (lakh/crore) with `--localize`: `12,34,567`; words: लाख (10⁵), करोड़ (10⁷).
  Never convert between million and lakh without checking arithmetic: 1.5 million = 15 लाख.
- Dates: `13 अक्तूबर 2026` (months: जनवरी, फ़रवरी, मार्च, अप्रैल, मई, जून, जुलाई, अगस्त, सितंबर, अक्तूबर, नवंबर, दिसंबर).
- Currency: `₹1,250` / `1,250 रुपये`.

## 4. Grammar and style rules
- SOV order; postpositions (में, पर, से, को, के लिए). Verb at the end.
- Gender agreement of verbs/adjectives with nouns (assign gender to loanwords by convention:
  कंप्यूटर m., फ़ाइल f., वेबसाइट f., ऐप m.).
- Ergative `ने` in perfective transitive sentences — agreement shifts to the object.
- Honorific plural for respected persons (प्रधानमंत्री ने कहा… वे आए).
- Avoid English-style passive (`द्वारा किया गया`) chains; use active voice or impersonal forms.
- Instructions: `क्लिक करें`, `चुनें`, `दर्ज करें` (polite imperative with आप implied).

## 5. Terminology conventions
- Tech: established loans (डेटाबेस, सर्वर, क्लाउड, एल्गोरिदम) or official Hindi terms in
  government content (संगणक is rare; prefer कंप्यूटर outside strict government text).
- First technical occurrence: Hindi term + English in parentheses — `मशीन लर्निंग (Machine Learning)`
  or `कृत्रिम बुद्धिमत्ता (Artificial Intelligence)`.
- Acronyms: keep Latin (AI, API) or Devanagari spelled form (एआई) — consistent.

## 6. Traps
- "Play a role" → `भूमिका निभाना` is natural but overused; vary with `योगदान देना`, `असर डालना`.
- "Make sure" → `सुनिश्चित करें`. "Update" → `अपडेट करें` (UI) / `अद्यतन` (government).
- Don't translate "you" with आप in every sentence; verb forms imply it.
- English plural nouns → Hindi plural forms must agree (फ़ाइलें, ऐप्स/ऐप).
- Avoid calqued "is being done" (`किया जा रहा है`) for every present-tense English passive.

## 7. Native style — humanizer notes
Remove tells: `आज के इस आधुनिक युग में`, `यह ध्यान देने योग्य है कि`, `इसके अलावा` / `साथ ही`
at every sentence start, `महत्वपूर्ण भूमिका निभाता है` everywhere, `निष्कर्ष के तौर पर` closing
every section, Sanskrit-heavy words where common words exist (प्रयोग vs इस्तेमाल — choose by register),
mechanical `द्वारा` passives.
Native moves: natural compound verbs (कर लेना, हो जाना, दे देना) where register allows;
connectors by meaning: `इसलिए`, `लेकिन`, `फिर भी`, `बल्कि`, `यानी`, `क्योंकि`, `जबकि`, `तो`;
vary sentence length; keep verb-final flow.

## 8. As a source language
- Honorific plural ≠ grammatical plural; translate as singular person.
- Gender of nouns and verb agreement reveal who did what; read carefully.
- Lakh/crore → millions/billions: compute exactly.
- Hinglish code-mixing: translate meaning, keep brand terms.

## 9. Final checklist
- [ ] Danda । for full stops; nukta/chandra usage consistent.
- [ ] आप + plural verb forms; gender agreement correct.
- [ ] Register: modern standard (not over-Sanskritized, not Hinglish) unless domain needs it.
- [ ] Numbers unchanged; lakh/crore only if localized and computed correctly.
- [ ] Devanagari renders correctly (conjuncts) in the output.
