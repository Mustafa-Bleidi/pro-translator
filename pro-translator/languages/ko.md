# Korean — `--ko`

| Field | Value |
|---|---|
| Tag | `--ko` |
| Aliases | `--korean`, `--한국어`, `--kor`, `--كوري` |
| Variants | Standard Korean (South Korea, 표준어) |
| BCP 47 | `ko-KR` |
| Script / direction | Hangul (Hanja only if source/genre requires) / LTR |
| Tesseract OCR pack | `kor`, `kor_vert` |
| Fonts | Noto Sans CJK KR / Noto Serif CJK KR, Pretendard, Malgun Gothic, Apple SD Gothic Neo |
| Typical length vs English | −10 to +10 % characters |

## 1. Default variant and register
- Choose the speech level once:
  - **합쇼체 (-습니다/-ㅂ니다)**: formal documents, manuals, announcements, business, legal.
  - **해요체 (-아요/-어요)**: UI messages, marketing, friendly customer content.
  - **해라체/한다체 (-다)**: academic papers, reports, news, specifications.
- Honorifics (-시-, 께서, 드리다) toward the reader/customer where appropriate; don't over-honor
  in technical docs.

## 2. Typography and punctuation
- Word spacing (띄어쓰기) per 한글 맞춤법: particles attach to the word (`파일을`), dependent nouns
  are spaced (`할 수 있다`, `하는 것`), units spaced after numerals in words (`두 개`) but attached
  after digits is accepted (`2개`).
- Punctuation: Western `. , ? !`; quotes “ ” / ‘ ’; titles in 「」 or 《》 or “ ” per publication style.
- Headings: no period. Lists: noun endings (`-기`, `-음`) or 합니다 endings consistently.

## 3. Numbers, dates, currency
- Dates: `2026년 10월 13일`, `2026. 10. 13.` (official style with spaces and final period).
- Large numbers: 만 (10⁴), 억 (10⁸) in prose with `--localize` (`1억 2,000만 원`); tables keep digits.
- Currency: `1,250원`, `₩1,250`, `1,250달러`.
- Time: `오후 3시 30분` or `15:30`.

## 4. Grammar and style rules
- SOV; particles 은/는 (topic) vs 이/가 (subject) chosen deliberately; 을/를 object.
- **Particles after English words/numbers follow pronunciation**: `Python을` (pa-i-sseon, ends in
  consonant → 을), `API를` (ends in vowel sound → 를), `3을`/`3개를`.
- Drop pronouns (당신, 그, 그것) — `당신` is especially unnatural for "you".
- Avoid double passives (`되어지다`, `보여지다` ✗ → `되다`, `보이다`).
- Avoid Japanese/English calques: `~에 있어서`, `~에 대해서` overuse, `~를 통해` everywhere,
  `~하는 것이 가능하다` (→ `~할 수 있다`), `가지다` calques ("have a meeting" → `회의를 하다`).
- Instructions: `클릭합니다` (manual descriptive) or `클릭하세요` (request) — consistent.

## 5. Terminology conventions
- Tech: established loanwords in Hangul (데이터베이스, 클라우드, 서버, 애플리케이션/앱) and
  native/Sino-Korean terms where standard (설정, 저장, 삭제, 검색, 인공지능, 머신러닝/기계 학습).
- Loanword spelling per 외래어 표기법 (Standard Korean Language Dictionary): 콘텐츠, 메시지, 소프트웨어.
- First technical occurrence: Korean term + English in parentheses — `기계 학습(Machine Learning)`
  (Korean style typically has no space before the parenthesis).

## 6. Traps
- "You" → never `당신` in UI/manuals; omit or use `사용자`, `고객님`.
- "Please" → `-세요` / `-십시오` is enough; avoid `제발`.
- "Play a role" → `역할을 하다` (natural) — not `역할을 수행하다` everywhere.
- Plural `-들` only when needed (Korean doesn't mark plural routinely).

## 7. Native style — humanizer notes
Remove tells: `~하는 것이 중요합니다` in every paragraph, `또한,` / `더불어,` / `뿐만 아니라`
opening every sentence, `결론적으로,` / `요약하자면,` closing sections, `~에 있어서`, `~를 통해`,
`되어지다`, `당신`, mixed 합니다/해요 endings, stacked Sino-Korean nouns
(`효율성 향상 실현 방안 모색` → verbs).
Native connectors: `그래서`, `하지만`, `그런데`, `따라서`, `즉`, `게다가`, `반면`, `물론`.
Vary endings within the chosen level (-습니다/-ㅂ니다/-ㄹ 수 있습니다/-지 않습니다).

## 8. As a source language
- Subjects omitted — recover from context.
- Speech level conveys relationship, not content — map to target register.
- 만/억 → convert exactly (1억 = 100 million).
- Sino-Korean compounds can be dense — unpack.

## 9. Final checklist
- [ ] One speech level throughout; honorifics appropriate.
- [ ] 띄어쓰기 correct; particles after English/numbers follow pronunciation.
- [ ] No `당신`, no double passives, no calqued `~에 있어서`.
- [ ] Numbers unchanged (watch 만/억).
