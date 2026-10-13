# Portuguese — `--pt`

| Field | Value |
|---|---|
| Tag | `--pt` |
| Aliases | `--portuguese`, `--português`, `--portugues`, `--por`, `--برتغالي` |
| Variants | `--pt-br` (default: Brazil), `--pt-pt` (Portugal; also base for Africa/Timor) |
| BCP 47 | `pt-BR`, `pt-PT` |
| Script / direction | Latin / LTR |
| Tesseract OCR pack | `por` |
| Fonts | Any Latin font |
| Typical length vs English | +15–25 % |

## 1. Default variant and register
- Brazilian Portuguese unless the audience is Portugal/PALOP (`--pt-pt`).
- Address: pt-BR `você` (neutral-friendly; `o senhor/a senhora` very formal); pt-PT formal
  impersonal 3rd person or `você` carefully, informal `tu`. Business pt-PT often avoids direct
  address: « Deve clicar em… ».
- Spelling: Acordo Ortográfico de 1990 for both variants (pt-PT: ação, ótimo, direção).

## 2. Typography and punctuation
- Quotes: “ ” in pt-BR; « » or “ ” in pt-PT (consistent).
- Headings: sentence case.
- Months and days lowercase (outubro, segunda-feira).
- Hyphenation per Acordo (autoestima, antissocial, micro-ondas).
- Crase (à) correct usage.

## 3. Numbers, dates, currency
- Decimal comma, thousands point: `1.250,75` (BR); pt-PT also uses space for thousands (`1 250,75`).
- Dates: `13 de outubro de 2026`, `13/10/2026`.
- Currency: `R$ 1.250,75` (BR), `1250,75 €` (PT).
- Percent: `25%`.

## 4. Grammar and style rules
- Clitic placement differs: pt-BR proclisis is natural (« Ele me disse »), pt-PT enclisis is
  standard in affirmative main clauses (« Ele disse-me »). Follow the variant.
- Progressive: pt-BR `estou fazendo`; pt-PT `estou a fazer`.
- Avoid gerundismo in pt-BR business text (« vou estar enviando » ✗ → « vou enviar / envio »).
- Avoid English-style passive overuse; use active or `se` passive (« Vendem-se casas »).
- Omit subject pronouns when the verb is clear (less so in pt-BR colloquial).
- Instructions: imperative (« Clique em Salvar » BR / « Clique em Guardar » PT) or infinitive in labels.

## 5. Terminology conventions
- Vocabulary BR vs PT: file arquivo / ficheiro · save salvar / guardar · screen tela / ecrã ·
  user usuário / utilizador · mouse mouse / rato · cell phone celular / telemóvel ·
  bus ônibus / autocarro · team equipe (or time, informal) / equipa · download baixar / transferir.
- Microsoft/Apple localization terms per variant.
- Acronyms: ONU, OTAN, UE, PIB, IA (AI), DNA (BR) / ADN (PT).

## 6. Traps
- False friends: actually (na verdade), eventually (finalmente), pretend (fingir; "pretender"=intend),
  push (empurrar; "puxar"=pull), exquisite (requintado; "esquisito"=strange), library (biblioteca),
  data (dados; "data"=date), costume (fantasia; "costume"=habit), parents (pais; "parentes"=relatives).
- "Play a role" → `desempenhar um papel` (not "jogar um papel").
- "Based on" → `com base em` (avoid "baseado em" repetition).

## 7. Native style — humanizer notes
Remove tells: `No mundo atual`, `Vale ressaltar que`, `É importante destacar que`, `Além disso,`
/ `Ademais,` / `Outrossim,` at every paragraph, `desempenha um papel crucial`, `Em suma,` /
`Em conclusão,` closing sections, gerundismo, stacked triads.
Native connectors: `então`, `por isso`, `afinal`, `aliás`, `no entanto`, `mesmo assim`,
`ou seja`, `já que`, `enquanto isso`. pt-BR prose is direct and warm; pt-PT more formal.

## 8. As a source language
- Personal infinitive (para eles fazerem) → explicit subject in English.
- BR/PT vocabulary differences (ônibus/autocarro) may signal audience.
- você = you (singular) but conjugates in 3rd person — don't misread as he/she.

## 9. Final checklist
- [ ] Variant consistent: vocabulary, clitics, progressive, spelling.
- [ ] No gerundismo; sentence-case headings; lowercase months.
- [ ] Number and currency formats per variant (if `--localize`).
