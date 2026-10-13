# English — `--en`

| Field | Value |
|---|---|
| Tag | `--en` |
| Aliases | `--english`, `--eng`, `--انجليزي`, `--الإنجليزية` |
| Variants | `--en-us` (default), `--en-gb` (also suits AU/NZ/IE/IN with notes) |
| BCP 47 | `en-US`, `en-GB` |
| Script / direction | Latin / LTR |
| Tesseract OCR pack | `eng` |
| Fonts | Any (Noto Sans/Serif, Calibri, Arial, Georgia) |
| Typical length vs source | Usually shorter than Romance/Arabic/German sources |

## 1. Default variant and register
- US English unless the user, audience or source context points to UK (then `--en-gb`).
- Plain-language professional style: clear, direct, active voice, short paragraphs.
- Address: "you" for instructions; imperative for steps ("Click **Save**").

## 2. Typography and punctuation
- US: double quotes “ ” with periods/commas inside; UK: single quotes ‘ ’ commonly, punctuation
  outside unless part of the quote.
- Oxford comma: US default yes (Chicago/AP differ — AP omits); UK default no. Be consistent.
- Em dash — closed in US (word—word), spaced en dash in UK (word – word). Use sparingly.
- Headings: sentence case by default in modern technical/business writing; title case only if
  the user's style guide or the source document's English style uses it.
- Spelling: US (color, organize, center, license n./v.) vs UK (colour, organise, centre, licence n. / license v.).

## 3. Numbers, dates, currency
- Decimal point, comma thousands: `1,250.75`.
- Dates: US `October 13, 2026` / `10/13/2026`; UK `13 October 2026` / `13/10/2026`.
  Prefer spelled-out month to avoid ambiguity when converting with `--localize`.
- Numbers one–nine in words in prose (Chicago/AP), digits for 10+, units, data — unless the
  document's convention is different.
- Currency symbol before amount: `$25`, `€25` (UK: `€25` too).

## 4. Grammar and style rules
- Subject–verb–object order; keep the actor visible (active voice) unless the source is
  deliberately impersonal (scientific methods may stay passive).
- Break long sentences inherited from Arabic, German, Russian, Hindi sources.
- Articles: add a/an/the correctly — the main error source when translating from article-less
  languages (ru, zh, ja, ko, hi, bn, ur, id, tr).
- Tense consistency; English uses present perfect where many languages use simple past.
- Phrasal verbs are natural in informal/neutral text; in formal/legal text prefer Latinate
  verbs moderately.

## 5. Terminology conventions
- Use established English terms of the field; for legal text distinguish "shall" (obligation,
  traditional drafting) vs "must" (plain-language drafting) — follow the document's system.
- Foreign institution names: official English name if it exists; otherwise translate and keep
  the original in parentheses on first use.
- Transliteration of names from Arabic/Russian/Chinese etc.: use the person's or the
  organization's own Latin spelling if known; else standard romanization (Pinyin for Chinese,
  Hepburn for Japanese, Revised Romanization for Korean, BGN/PCGN or common practice for Russian/Arabic).

## 6. Traps (when English is the target)
- False friends: actual/actualmente (current), eventual/éventuellement (possible), sympathique
  (nice), Handy (mobile phone), "magazine" in Arabic contexts (مجلة) vs "store".
- Calques: "realize a project" → carry out; "make a reunion" → hold a meeting; "in the frame of"
  → as part of; "assist to a conference" → attend.
- Honorific formulas from Arabic/Urdu/Hindi/Japanese/Korean: translate by function ("Dear…",
  "Kind regards"), not literally.
- Over-formal register copied from the source; English business prose is less formal than
  Arabic, German, Russian or Japanese.

## 7. Native style — humanizer notes
Remove: "delve, tapestry, testament, pivotal, crucial, seamless, robust, leverage, landscape,
realm, foster, underscore, navigate (figurative), holistic, cutting-edge, game-changer, unlock,
empower, elevate, embark, ever-evolving, in today's fast-paced world, it's worth noting that,
let's dive in, in conclusion, at the end of the day". Remove "not just X — it's Y" reveals,
stacked triads, Moreover/Furthermore/Additionally chains, em-dash overuse, hedge stacking
("may potentially").
Native moves: concrete verbs, contractions in neutral/informal text (it's, don't), sentence
fragments only in informal registers, varied sentence openings, "so / but / and" as sentence
starters are fine in modern prose.

## 8. As a source language
- Ambiguous "you" (singular/plural, formal/informal) — decide once for the target.
- Noun stacks ("user account password reset link") must be unpacked into the target's syntax.
- "Shall/should/must/may" carry legal weight — map consistently.
- Gender-neutral "they" — choose the target's established neutral strategy.
- Title Case headings → convert to target heading convention.
- Phrasal verbs and idioms: translate the meaning, not the particles.

## 9. Final checklist
- [ ] Variant spelling consistent (US or UK).
- [ ] Articles and tenses correct.
- [ ] Heading case and quote style consistent.
- [ ] No calques or source-language formality.
- [ ] Number/date style consistent with the chosen variant.
