# Spanish — `--es`

| Field | Value |
|---|---|
| Tag | `--es` |
| Aliases | `--spanish`, `--español`, `--espanol`, `--spa`, `--اسباني` |
| Variants | `--es-419` (default: neutral Latin American), `--es-es` (Spain), `--es-mx` (Mexico) |
| BCP 47 | `es-419`, `es-ES`, `es-MX` |
| Script / direction | Latin / LTR |
| Tesseract OCR pack | `spa` |
| Fonts | Any Latin font |
| Typical length vs English | +15–25 % |

## 1. Default variant and register
- Neutral Latin American Spanish for global audiences (avoid strong regionalisms);
  `--es-es` for Spain (vosotros, ordenador, móvil).
- Address: **usted** in formal/business/legal; **tú** in UI, marketing and casual content
  (common in modern tech brands). Choose once; never mix.
- `--es-es` informal plural: vosotros; Latin America: ustedes for all plural.

## 2. Typography and punctuation
- Opening marks: `¿…?`, `¡…!` — always.
- Quotes: RAE recommends « » then “ ” then ‘ ’; in Latin American digital text “ ” is common.
  Pick one, keep it.
- Sentence case for titles and headings (only the first word and proper nouns capitalized).
- Lowercase: days, months, languages, nationalities (lunes, octubre, español).
- Em dash for incisos —así— without spaces inside.
- Abbreviation `etc.` preceded by a comma; ordinals `1.º`, `2.ª`.

## 3. Numbers, dates, currency
- Spain: decimal comma, thousands point or thin space (`1.250,75` / `1 250,75`).
  Mexico and much of Central America: decimal point (`1,250.75`). Default = source format;
  `--localize` applies the variant's convention.
- Dates: `13 de octubre de 2026`, `13/10/2026`.
- Percent: `25 %` (RAE, with space) or `25%` (common) — consistent.
- Currency: `25 €` (Spain), `$25` / `25 USD` (Americas).

## 4. Grammar and style rules
- Avoid the passive `ser + participio` calqued from English; prefer `se` passive or active voice
  (`Se actualizó el sistema` / `El equipo actualizó el sistema`).
- Avoid gerund misuse (gerundio de posterioridad: "Llegó, abriendo la puerta" ✗) and gerund as
  adjective ("caja conteniendo libros" ✗ → "caja que contiene libros").
- Drop subject pronouns unless needed for emphasis or clarity.
- Possessives: "Levanta tu mano" → "Levanta la mano" (body parts, own items use article).
- Concordancia of gender and number; agreement in compound subjects.
- Avoid excessive "el mismo/la misma" as a pronoun ("el mismo fue enviado" ✗).
- Use "deber + infinitivo" (obligation) vs "deber de + infinitivo" (probability) correctly.

## 5. Terminology conventions
- Prefer established Spanish terms where professional usage accepts them (correo electrónico,
  contraseña, descargar, nube); keep accepted anglicisms (software, hardware, marketing, email in LatAm).
- Spain vs LatAm: computer ordenador / computadora · mobile móvil / celular · car coche / carro-auto
  · file archivo/fichero (Spain: fichero also) · to save guardar.
- Acronyms: Spanish ones where established (ONU, OTAN, ADN, PIB, UE); plural acronyms invariable (las ONG).

## 6. Traps
- False friends: actually (en realidad, no "actualmente"), eventually (finalmente), library
  (biblioteca), embarrassed (avergonzado, no "embarazada"), realize (darse cuenta), assist
  (ayudar; "asistir" = attend), application (solicitud vs aplicación/app), support (soporte técnico ok; "apoyar" for support a cause), sensible (sensato), introduce (presentar).
- "Play a role" → `desempeñar un papel` (not "jugar un rol").
- "In terms of" → `en cuanto a / en materia de`; "based on" → `basado en` (avoid "en base a" in formal text).
- English title case and excess capitals → sentence case.

## 7. Native style — humanizer notes
Remove tells: `En el mundo actual`, `Cabe destacar que`, `Es importante señalar que`,
`Además,` / `Asimismo,` / `Por otro lado,` opening every paragraph, `juega un papel crucial`,
`sin lugar a dudas`, `En conclusión,` closing every section, stacked triads of adjectives,
overuse of "mismo", passive ser+participio.
Native connectors by meaning: `pues`, `así que`, `por eso`, `sin embargo`, `aun así`,
`en cambio`, `de hecho`, `o sea`, `es decir`, `ya que`, `dado que`. Spanish tolerates longer
sentences than English, linked with commas and relative clauses — vary, don't chop everything.

## 8. As a source language
- Long sentences with many subordinate clauses → split for English and many Asian targets.
- Subject pronoun omitted; recover from verb.
- Usted vs tú signals register; map to target's formality system.
- `se` constructions can be passive, impersonal or reflexive — read carefully.

## 9. Final checklist
- [ ] Variant consistent (vocabulary, vosotros/ustedes, number format).
- [ ] ¿ ¡ present; sentence-case headings; lowercase months/days.
- [ ] No calqued passives, gerund misuse, "el mismo".
- [ ] tú/usted consistent.
