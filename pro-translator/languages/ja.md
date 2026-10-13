# Japanese — `--ja`

| Field | Value |
|---|---|
| Tag | `--ja` |
| Aliases | `--japanese`, `--日本語`, `--jpn`, `--ياباني` |
| Variants | Standard Japanese |
| BCP 47 | `ja-JP` |
| Script / direction | Kanji + hiragana + katakana / LTR horizontal (vertical 縦書き only if source layout is vertical) |
| Tesseract OCR pack | `jpn`, `jpn_vert` |
| Fonts | Noto Sans CJK JP / Noto Serif CJK JP, Hiragino, Yu Gothic, Meiryo |
| Typical length vs English | −10 to −40 % characters; count characters, not words |

## 1. Default variant and register
- Choose one style and keep it for the whole document:
  - **です・ます調** (polite): UI, manuals, marketing, customer communication, most business docs.
  - **である調 / だ・である** (plain written): academic papers, reports, specifications, legal,
    news-like text.
- Honorifics (敬語): 尊敬語/謙譲語 in customer-facing business correspondence
  (ご確認ください, いただけます). Don't over-honor in technical documentation.
- `--casual` = friendly です・ます without stiff keigo; plain casual speech only on request.

## 2. Typography and punctuation
- Full-width punctuation: `、` (comma), `。` (period), `「」` quotes, `『』` nested/titles,
  `（）` parentheses, `・` (nakaguro) for list items / foreign name breaks (ジョン・スミス), `〜` ranges.
- No spaces between words. Between Japanese and Latin/numbers: many tech style guides use no
  space; some use half-width space — pick one and keep it.
- Latin letters and digits: half-width (`Python 3`, `100`). Katakana: always full-width.
- Long vowel mark ー for loanwords per standard spellings (サーバー, コンピューター per current
  JIS/Microsoft style; older style サーバ) — be consistent.
- Headings: no period.

## 3. Numbers, dates, currency
- Arabic numerals (half-width) for data: `2026年10月13日`, `15時30分` or `15:30`.
- Large numbers: 万 (10⁴), 億 (10⁸) in prose with `--localize` (`1億2,000万円`); tables keep digits.
- Currency: `1,250円`, `¥1,250`, `1,250ドル`/`US$1,250`.
- Era names (令和8年) only if the source uses them or the user asks.

## 4. Grammar and style rules
- SOV; topic marker は vs subject が chosen deliberately; particles correct (に/で/を/へ).
- Drop pronouns (あなた, 彼, それ) — almost always unnatural when copied from English.
- Avoid stacked の (〜の〜の〜の); restructure.
- Avoid unnecessary passive (〜される) and causative calques.
- Long English relative clauses → pre-noun modifiers kept short, or split into two sentences.
- Instructions: `〜をクリックします` (manual, descriptive) or `〜をクリックしてください` (request) — consistent.
- Plurality and articles don't exist; don't add たち/それら mechanically.

## 5. Terminology conventions
- Katakana for established loanwords (データベース, クラウド, アカウント);
  established kanji terms where standard (設定, 保存, 削除, 検索, 機械学習, 人工知能).
- Microsoft/Apple Japanese style guides and JIS terminology for tech.
- First technical occurrence: Japanese term + English in parentheses — `機械学習（Machine Learning）`.
- Product names stay in Latin letters.

## 6. Traps
- Katakana overuse (ソリューションをレバレッジする ✗) — use Japanese words when they exist.
- "Please" in UI isn't always ください; descriptive forms often read better in manuals.
- "You can …" → `〜できます`; avoid `あなたは〜できます`.
- "Important to note" → 注意: / ※ notes, not a sentence of filler.
- English emphasis (bold, exclamation) — Japanese business text uses fewer `！`.

## 7. Native style — humanizer notes
Remove tells: `〜することが重要です` in every paragraph, `さらに、` / `また、` opening every
sentence, `結論として、` / `まとめると、` closing each section, `〜と言えるでしょう` hedging
everywhere, `〜において` overuse, katakana buzzwords, pronouns, mixed です・ます and である.
Native moves: natural sentence endings variety within the chosen style (〜です／〜ます／〜でしょう／
〜ません／体言止め in headings and lists), connectors by meaning: `ただし`, `そのため`, `なお`,
`一方`, `つまり`, `ところが`, `したがって`; omit the obvious subject.

## 8. As a source language
- Subjects and objects omitted — recover from context; ask if crucial and unclear.
- Keigo signals relationship, not content — map to target register.
- 万/億 → convert exactly (1億 = 100 million).
- Vertical text and ruby (furigana) in source: translate base text; drop ruby unless needed.

## 9. Final checklist
- [ ] One style (です・ます or である) throughout.
- [ ] Full-width punctuation, half-width alphanumerics, consistent spacing rule.
- [ ] No unnecessary pronouns; no の chains; katakana consistent with style guide.
- [ ] Numbers unchanged (watch 万/億).
