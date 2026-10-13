# Russian — `--ru`

| Field | Value |
|---|---|
| Tag | `--ru` |
| Aliases | `--russian`, `--русский`, `--rus`, `--روسي` |
| Variants | Standard Russian |
| BCP 47 | `ru-RU` |
| Script / direction | Cyrillic / LTR |
| Tesseract OCR pack | `rus` |
| Fonts | Any font with Cyrillic (Noto Sans, PT Sans, Arial) |
| Typical length vs English | +10–20 % |

## 1. Default variant and register
- Modern literary standard. Business and technical: neutral, precise, not bureaucratic.
- Address: **Вы/вы** in formal text (capital «Вы» only in personal letters to one person),
  **ты** only for casual brand voice on request. UI: vy-forms or impersonal infinitives.

## 2. Typography and punctuation
- Quotes: «ёлочки» primary, „лапки“ for nested.
- Dash: em dash `—` with spaces (`Москва — столица России`); en dash for ranges without spaces
  (`2010–2020`); hyphen for compounds only.
- Headings: sentence case; no period at the end.
- Commas before subordinate clauses (что, который, если, чтобы) are mandatory.
- `ё`: either consistently written or consistently replaced by `е` (except where meaning
  changes: всё/все) — decide in the style sheet.
- Abbreviations: т. е., т. д., г. (year), с. (page) with non-breaking spaces.

## 3. Numbers, dates, currency
- Decimal comma; thousands with (non-breaking) space: `1 250,75`.
- Dates: `13 октября 2026 г.` or `13.10.2026`.
- Percent: `25 %` (GOST) or `25%` (common) — consistent.
- Currency after amount: `1 250 руб.` / `1 250 ₽`, `25 $` or `$25` in business texts.
- Ordinals: `5-й`, `2-го`.

## 4. Grammar and style rules
- Free word order: put new information at the end of the sentence (theme → rheme). Don't copy
  English order mechanically.
- Six cases, gender, aspect (perfective/imperfective) — choose aspect deliberately in
  instructions: «Нажмите» (one-time action, perfective) vs «Нажимайте» (repeated).
- Avoid канцелярит: «осуществлять», «производить», «является», «данный», «в целях»,
  «в рамках» chains, genitive strings («проведение анализа результатов внедрения системы»).
- Avoid overuse of «который»; use participles sparingly but correctly.
- Numerals agreement: 1 файл, 2 файла, 5 файлов, 21 файл.
- Passive: use reflexive or active where natural («Система обновляется»).

## 5. Terminology conventions
- Established Russian IT terms: файл, папка, сервер, база данных, облако, учётная запись,
  пароль, настройки, приложение. Many anglicisms are standard (браузер, интерфейс, дедлайн in casual).
- GOST terms for engineering/standards documentation.
- Acronyms: Russian ones where established (ООН, НАТО, ЕС, ВВП, ДНК, ИИ for AI).
- Transliteration of names: established forms (Джон Смит; Майкрософт for Microsoft in prose,
  Latin for product names).

## 6. Traps
- False friends: accurate (точный, not «аккуратный»), actual (фактический/текущий, «актуальный» = relevant),
  magazine (журнал, «магазин» = shop), sympathetic (сочувствующий, «симпатичный» = cute),
  decade (десятилетие, «декада» = 10 days), data (данные, «дата» = date), control (управление/контроль),
  intelligence (разведка vs интеллект), artist (художник/исполнитель).
- "Play a role" → `играть роль` OK but overused; vary: `влиять на`, `иметь значение`.
- "Important to note" → don't translate as a filler.
- Articles don't exist — don't add «этот/один» to fake them.

## 7. Native style — humanizer notes
Remove tells: `В современном мире`, `Важно отметить, что`, `Стоит подчеркнуть`, `Кроме того,` /
`Более того,` / `Также` opening every paragraph, `играет ключевую роль`, `В заключение`,
`является` in every sentence, `данный` instead of `этот`, genitive chains, stacked triads.
Native moves: verbs over nouns («проверить» vs «осуществить проверку»), connectors by meaning:
`однако`, `впрочем`, `зато`, `поэтому`, `то есть`, `ведь`, `при этом`, `тем не менее`;
end sentences on the new information.

## 8. As a source language
- No articles: decide a/the from context.
- Aspect conveys completion/repetition — reflect it in target tense/adverbs.
- Word order shows focus; rheme at the end may need a cleft or emphasis in English.
- Decimal comma and spaces in numbers.

## 9. Final checklist
- [ ] «» quotes; spaced em dash; mandatory commas.
- [ ] Case and numeral agreement; aspect choice in instructions.
- [ ] No канцелярит; theme–rheme order natural.
- [ ] ё policy consistent.
