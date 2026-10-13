# French — `--fr`

| Field | Value |
|---|---|
| Tag | `--fr` |
| Aliases | `--french`, `--français`, `--francais`, `--fra`, `--فرنسي` |
| Variants | `--fr-fr` (default: France), `--fr-ca` (Canada/Québec); BE/CH/Africa on request |
| BCP 47 | `fr-FR`, `fr-CA` |
| Script / direction | Latin / LTR |
| Tesseract OCR pack | `fra` |
| Fonts | Any Latin font |
| Typical length vs English | +15–25 % |

## 1. Default variant and register
- France French by default; `--fr-ca` follows OQLF recommendations (courriel, clavarder,
  magasiner) and Canadian conventions.
- Address: **vous** for professional, legal, UI and most marketing. **tu** only for very casual
  brand voices if the user wants it. Never mix.
- Inclusive writing: do not introduce point médian forms (utilisateur·rice·s) unless the client
  style requires it; prefer neutral rewording (« les personnes inscrites »).

## 2. Typography and punctuation
- France: non-breaking space (U+00A0 or narrow U+202F) **before** `; : ! ?` and `»`, and **after** `«`.
  Canada (OQLF): space only before `:` and inside « » (no space before ; ! ?).
- Quotes: « guillemets » with non-breaking spaces; “ ” for quotes inside quotes.
- Accents on capitals are required (État, À propos, ÉCOLE).
- Headings: sentence case (only first word and proper nouns).
- Ordinals: 1er, 1re, 2e (not 2ème in careful style). Abbreviations: M., Mme, n°.
- Apostrophe ’ (typographic) in published text; elision mandatory (l’utilisateur, qu’il).

## 3. Numbers, dates, currency
- Decimal comma; thousands separated by a (narrow) non-breaking space: `1 250,75`.
- Dates: `13 octobre 2026`, `13/10/2026`; months/days lowercase.
- Time: `15 h 30` (France), `15 h 30` / `15:30` (CA, both seen).
- Percent and units with a non-breaking space: `25 %`, `25 kg`.
- Currency after the amount: `25 €`, `25 $` (CA).

## 4. Grammar and style rules
- Avoid English-style passive overuse; prefer active, `on`, or pronominal (`se vend`).
- Keep agreement of past participles (with avoir when COD precedes).
- Prefer noun phrases where French naturally nominalizes, but avoid heavy chains
  (« la mise en œuvre de la configuration de… »).
- Instructions: infinitive in UI/procedures (« Cliquer sur Enregistrer ») or imperative
  vous form (« Cliquez sur Enregistrer ») — pick one per document.
- Avoid repeating "il y a" and "est-ce que" in formal writing.

## 5. Terminology conventions
- France: FranceTerme / Journal officiel recommendations for official texts; tech usage tolerates
  common anglicisms (logiciel, but « cloud » often « nuage/infonuagique » in Canada).
  Common: courriel (CA) / e-mail or courriel (FR formal), télécharger, mot de passe,
  paramètres, tableau de bord.
- Acronyms in French form when established: ONU, OTAN, UE, ADN, PIB, IA (AI), TVA.
- Microsoft/Apple French localization terms for UI.

## 6. Traps
- False friends: actually (en fait), eventually (finalement), library (bibliothèque),
  sensible (raisonnable), to realize (se rendre compte), to assist (aider), to control (contrôler
  = to check), demand (exigence), formation (training), application (candidature vs application),
  achievement (réussite, not achèvement), resume/CV.
- "Play a role" → `jouer un rôle` is correct but overused; vary: `contribuer à`, `peser sur`.
- "Based on" → `fondé sur / à partir de` (avoid « basé sur » in careful style).
- "In order to" → `pour`, not « afin de » every time.
- Don't keep English Title Case or missing non-breaking spaces.

## 7. Native style — humanizer notes
Remove tells: `Dans le monde d’aujourd’hui`, `Il est important de noter que`, `Il convient de
souligner que`, `En outre,` / `De plus,` / `Par ailleurs,` opening every paragraph,
`jouer un rôle crucial`, `En conclusion,` closing each section, `véritable` / `incontournable`
everywhere, stacked triads.
Native connectors by meaning: `or`, `donc`, `en effet`, `pourtant`, `toutefois`, `ainsi`,
`d’ailleurs`, `quant à`, `certes … mais`. French prose favors balanced, longer sentences than
English; vary length deliberately.

## 8. As a source language
- Long nominal sentences → unpack into verbs for English/Asian targets.
- `on` can mean we/they/one/passive — decide from context.
- vous: formal singular or plural — decide from context.
- Decimal comma and spaces in numbers → do not misread `1 250,5` as two numbers.

## 9. Final checklist
- [ ] Non-breaking spaces per variant; « » quotes; accents on capitals.
- [ ] vous consistent; agreement of participles.
- [ ] Sentence-case headings; lowercase months.
- [ ] No anglicisms where a standard French term is expected (esp. fr-CA).
