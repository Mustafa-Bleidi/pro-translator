# Bengali (Bangla) — `--bn`

| Field | Value |
|---|---|
| Tag | `--bn` |
| Aliases | `--bengali`, `--bangla`, `--বাংলা`, `--ben` |
| Variants | Standard colloquial (চলিত/প্রমিত) — Bangladesh default; India (West Bengal) on request: `--bn-in` |
| BCP 47 | `bn-BD`, `bn-IN` |
| Script / direction | Bengali–Assamese script / LTR (complex shaping: যুক্তাক্ষর conjuncts) |
| Tesseract OCR pack | `ben` |
| Fonts | Noto Sans/Serif Bengali, Kalpurush, SolaimanLipi, Nirmala UI |
| Typical length vs English | +10–25 % |

## 1. Default variant and register
- **Standard colloquial Bengali (প্রমিত চলিত ভাষা)** — the norm for all modern writing.
  The old literary sadhu bhasha (সাধু ভাষা: করিয়াছিল, তাহাদের) is not used except for
  quoting old texts.
- **Never mix sadhu and cholito forms** in one text (গুরুচণ্ডালী দোষ) — a classic error.
- Spelling: Bangla Academy standard spelling (প্রমিত বানান) for Bangladesh; Paschimbanga Bangla
  Akademi for India — minor differences; be consistent.
- Address: **আপনি** in formal/professional text and UI; তুমি only in casual brand voice; never তুই.

## 2. Typography and punctuation
- Full stop: দাঁড়ি **।**; `?`, `!`, `,`, `;`, `:` as in English.
- No space before `।`. Quotes “ ” or ‘ ’.
- Hasanta (্) and conjuncts must render; check output for broken conjuncts.
- Use ৎ (khanda ta) correctly (উৎসব, হঠাৎ).

## 3. Numbers, dates, currency
- Bengali digits `০১২৩৪৫৬৭৮৯` are standard in Bangladesh for formal/government/print text;
  Western digits are common in tech and in India. Default: keep source digits; `--localize`
  for Bangladesh → Bengali digits consistently.
- Lakh/crore grouping with `--localize`: `১২,৩৪,৫৬৭` — লাখ (10⁵), কোটি (10⁷); compute exactly.
- Dates: `১৩ অক্টোবর ২০২৬` (Gregorian months: জানুয়ারি, ফেব্রুয়ারি, মার্চ, এপ্রিল, মে, জুন,
  জুলাই, আগস্ট, সেপ্টেম্বর, অক্টোবর, নভেম্বর, ডিসেম্বর). Bengali calendar only if the source uses it.
- Currency: `৳১,২৫০` / `১,২৫০ টাকা` (BDT), `₹` for India.

## 4. Grammar and style rules
- SOV order; postpositions and case suffixes (-কে, -র/-এর, -তে/-এ, -থেকে).
- No grammatical gender in verbs — but honorific verb forms (আপনি করেন / তুমি করো / সে করে /
  তিনি করেন) must match the subject's honorific level consistently.
- Classifiers: -টা, -টি, -গুলো, -গুলি, জন (for people): ফাইলটি, তিনজন ব্যবহারকারী.
- Avoid literal English passives (`দ্বারা করা হয়েছে` chains); prefer active.
- Instructions: polite imperative `ক্লিক করুন`, `নির্বাচন করুন`, `লিখুন`.

## 5. Terminology conventions
- Common loans in Bengali script for tech (কম্পিউটার, সফটওয়্যার, ইমেইল, ইন্টারনেট, অ্যাপ);
  Bengali words where established (তথ্য, নিরাপত্তা, পাসওয়ার্ড is loan, হিসাব/অ্যাকাউন্ট both seen).
- First technical occurrence: Bengali term + English in parentheses —
  `কৃত্রিম বুদ্ধিমত্তা (Artificial Intelligence)`.
- Government (Bangladesh): Bangla Academy / official glossaries.

## 6. Traps
- "Play a role" → `ভূমিকা পালন করা` is fine but overused; vary: `অবদান রাখা`, `প্রভাব ফেলা`.
- Don't translate "you" into a pronoun every sentence; verbs carry person.
- Plural: use -গুলো/-গুলি or numerals with classifiers, not both (তিনটি ফাইলগুলো ✗).
- Don't calque English article "the" — use classifiers (-টি/-টা) only when definiteness matters.

## 7. Native style — humanizer notes
Remove tells: `বর্তমান আধুনিক যুগে`, `উল্লেখ্য যে`, `এটি লক্ষণীয় যে`, `এছাড়াও` / `তাছাড়া`
at every sentence start, `গুরুত্বপূর্ণ ভূমিকা পালন করে` everywhere, `পরিশেষে বলা যায়` closing
sections, sadhu–cholito mixing, heavy Sanskrit (তৎসম) words where common words exist.
Native connectors: `তাই`, `কিন্তু`, `তবে`, `বরং`, `অর্থাৎ`, `কারণ`, `যদিও`, `ফলে`, `তবু`.
Vary sentence length; keep verb-final flow.

## 8. As a source language
- Honorific verb forms identify respect level, not number.
- Classifiers mark definiteness — map to a/the.
- Bengali digits and lakh/crore → convert exactly.

## 9. Final checklist
- [ ] Pure cholito (no sadhu forms); standard spelling consistent.
- [ ] দাঁড়ি । for full stops; conjuncts render.
- [ ] আপনি + matching verb forms throughout.
- [ ] Digit system consistent; numbers unchanged.
