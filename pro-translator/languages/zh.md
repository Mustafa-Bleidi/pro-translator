# Chinese — `--zh`

| Field | Value |
|---|---|
| Tag | `--zh` |
| Aliases | `--chinese`, `--中文`, `--汉语`, `--zho`, `--chi`, `--mandarin` |
| Variants | `--zh-cn` (default: Simplified, Mainland), `--zh-tw` (Traditional, Taiwan); `--zh-hk` on request (Traditional, Hong Kong vocabulary) |
| BCP 47 | `zh-CN` (`zh-Hans`), `zh-TW` (`zh-Hant`) |
| Script / direction | Han characters / LTR (vertical only if the source layout is vertical) |
| Tesseract OCR pack | `chi_sim`, `chi_tra` (+ `_vert`) |
| Fonts | Noto Sans CJK SC / TC, Source Han Sans/Serif, Microsoft YaHei, PingFang |
| Typical length vs English | −30 to −50 % characters (count in characters, not words) |

## 1. Default variant and register
- Simplified Chinese (Mainland) unless `--zh-tw` / audience says Taiwan/Hong Kong.
- Traditional is **not** a character conversion: vocabulary differs (see §5).
- Formal documents: 书面语, concise, no colloquial particles (啊、吧、呢). Address: 您 in
  customer-facing text, 你 in casual/UI for younger audiences if the brand voice wants it.

## 2. Typography and punctuation
- Full-width punctuation in Chinese text: `，。、；：？！“”‘’（）《》【】……——`.
- `、` (enumeration comma) between list items in a sentence; `，` between clauses.
- Book/title marks `《》` for titles of books, laws, articles, films.
- Quotes: Simplified `“ ”` / `‘ ’`; Traditional (TW/HK) uses `「 」` / `『 』`.
- No spaces between Chinese characters. Between Chinese and Latin words/numbers: a half-width
  space is common in tech writing (使用 Python 3 编写) — pick one rule and keep it.
- Ellipsis `……` (6 dots, two characters), dash `——`.
- Numbers, Latin letters and code stay half-width.

## 3. Numbers, dates, currency
- Arabic numerals for data, dates, measurements: `2026年10月13日`.
- Large numbers: Chinese often uses 万 (10⁴) and 亿 (10⁸) — `1.2亿` = 120,000,000.
  Use only with `--localize` or in prose where natural; tables keep source digits.
- Percent `25%`; currency `¥`/`元` (CNY), `NT$` (TWD), `US$`/`美元`.
- Time: `下午3点` or `15:00` (keep source style in tables).

## 4. Grammar and style rules
- Topic–comment structure: put the topic/background first, then the point.
- Avoid overusing `的` (no more than ~2 in a noun phrase; restructure).
- Avoid overusing passive `被`; Chinese uses notional passives (问题已解决) or active forms.
- Avoid unnecessary pronouns (他/它/我们) and articles; drop them when clear.
- Long English relative clauses → split into short clauses or pre-modifiers kept short.
- Measure words (量词) correct: 一台电脑、一份报告、一项研究、一位专家.
- Avoid literal tense markers; use 了/过/将/正在 only where needed.

## 5. Terminology conventions
- Use established Chinese terms (全国科学技术名词审定委员会, official product localization).
  Tech terms Mainland vs Taiwan:
  software 软件 / 軟體 · network 网络 / 網路 · information 信息 / 資訊 · program 程序 / 程式 ·
  video 视频 / 影片 · database 数据库 / 資料庫 · server 服务器 / 伺服器 · default 默认 / 預設 ·
  file 文件 / 檔案 · memory 内存 / 記憶體 · quality 质量 / 品質 · project 项目 / 專案.
- Latin acronyms are common in tech (API、AI、CPU); keep them.
- Foreign names: established Chinese names (微软, 谷歌, 苹果 in Mainland; brands may keep Latin);
  person names transliterated per Xinhua conventions + original in parentheses on first use.

## 6. Traps
- "Play an important role" → 发挥重要作用 (not 扮演重要角色 everywhere).
- "Make sure" → 确保; "ensure" → 确保/保证; "enable" → 启用 (feature) vs 使…能够 (allow).
- "Support" (software) → 支持 (CN) / 支援 (TW).
- "Issue" → 问题 (bug) vs 发布 (publish) vs 期 (magazine issue).
- English plural → Chinese has none; don't add 们 to non-human nouns.
- Avoid 进行 + verb chains (进行分析 → 分析).

## 7. Native style — humanizer notes
Remove tells: `在当今社会/在当今时代`、`值得注意的是`、`总而言之/综上所述` closing every section,
`不仅……而且……` in every paragraph, `扮演着重要的角色`, `赋能`、`助力`、`抓手`、`闭环` buzzwords,
`进行` + verb, stacked `的`, `首先……其次……最后` everywhere.
Native moves: four-character expressions (成语/四字格) sparingly and correctly in formal prose;
short parallel clauses; omit subjects; use `则`、`而`、`即`、`故`、`因此`、`不过`、`另外` by meaning.

## 8. As a source language
- No tense/plural marking: infer from context and English requires explicit choices.
- Subject often omitted; recover it from context.
- 成语 → translate meaning, not imagery.
- Chinese numbers 万/亿 → convert carefully (1.2亿 = 120 million) and double-check.

## 9. Final checklist
- [ ] Correct variant (Simplified/Traditional) and vocabulary (CN vs TW).
- [ ] Full-width punctuation; correct quote style for variant; 《》 for titles.
- [ ] Consistent spacing rule between CJK and Latin.
- [ ] No 的/被/进行 overuse; measure words correct.
- [ ] Numbers unchanged (watch 万/亿 conversions).
