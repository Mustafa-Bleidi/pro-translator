# German — `--de`

| Field | Value |
|---|---|
| Tag | `--de` |
| Aliases | `--german`, `--deutsch`, `--deu`, `--ger`, `--الماني` |
| Variants | `--de-de` (default: Germany), `--de-ch` (Switzerland), `--de-at` (Austria) |
| BCP 47 | `de-DE`, `de-CH`, `de-AT` |
| Script / direction | Latin / LTR |
| Tesseract OCR pack | `deu` |
| Fonts | Any Latin font |
| Typical length vs English | +15–35 % (watch UI and slide overflow) |

## 1. Default variant and register
- Standard German per current Duden / official spelling (Reform 2006).
- Address: **Sie** (formal) for business, legal, technical and most UI; **du** for casual brands,
  apps for young audiences, internal communication if the client uses it. Never mix.
- de-CH: no `ß` (always `ss`), some vocabulary differences (Velo, parkieren); de-AT: Jänner, etc.
- Gender-inclusive language: follow the client's style (Doppelnennung "Kundinnen und Kunden",
  neutral forms "Mitarbeitende"); do not introduce asterisk/colon forms (Kund*innen) unless asked.

## 2. Typography and punctuation
- Quotes: „Anführungszeichen unten/oben“; nested ‚…‘. de-CH: «…» guillemets.
- All nouns capitalized; adjectives from proper names lowercase except fixed names.
- Headings: no Title Case beyond noun capitalization.
- Compound nouns written together or with hyphen when containing acronyms/English parts:
  `E-Mail-Adresse`, `Cloud-Speicher`, `IT-Sicherheit` (Durchkopplung).
- Dash: Halbgeviertstrich with spaces ` – ` as a dash.
- Comma before subordinate clauses (dass, weil, wenn, der/die/das relative) is mandatory.

## 3. Numbers, dates, currency
- Decimal comma; thousands point or (thin) space: `1.250,75` / `1 250,75`.
  de-CH uses apostrophe thousands in many contexts: `1'250.75` (decimal point for amounts).
- Dates: `13. Oktober 2026`, `13.10.2026`.
- Percent: `25 %` (DIN 5008, with space).
- Currency: `25 €` / `25 EUR`, `CHF 25.–` (CH).
- Time: `15:30 Uhr`.

## 4. Grammar and style rules
- Verb-second in main clauses; verb-final in subordinate clauses; separable verbs
  ("Klicken Sie auf **Speichern**"). Keep the verb bracket readable — don't stretch it.
- Avoid Nominalstil chains (Durchführung der Umsetzung der Konfiguration) — use verbs.
- Avoid overusing passive "wird … durchgeführt"; prefer active or "man" sparingly.
- Cases and gender (der/die/das) for loanwords per Duden: die E-Mail, das Update, die App, der Server.
- Instructions: Sie-imperative (`Klicken Sie …`) or infinitive in UI labels (`Datei speichern`).

## 5. Terminology conventions
- Tech: German UI terms of Microsoft/Apple/SAP for software (Datei, Ordner, Einstellungen,
  Speichern, Benutzerkonto). Accepted anglicisms (Software, Browser, Cloud, Download) where
  standard; avoid unnecessary Denglisch in formal text (Meeting → Besprechung in formal docs).
- Legal: German legal terms are system-bound (GmbH, AG, Vertrag, Haftung); don't "localize"
  foreign legal concepts into German law concepts — translate descriptively when they differ.
- Acronyms: German ones where established (EU, UNO, BIP, DNA/DNS (DNS in older texts), KI for AI).

## 6. Traps
- False friends: become (werden; "bekommen" = get), eventually (schließlich; "eventuell" =
  possibly), actual (tatsächlich; "aktuell" = current), also (auch; "also" = so/thus),
  gift (Geschenk; "Gift" = poison), sensible (vernünftig; "sensibel" = sensitive),
  chef (Koch; "Chef" = boss), handy (praktisch; "Handy" = mobile phone), map (Karte; "Mappe" = folder).
- "Make sense" → `sinnvoll sein` (not "Sinn machen" in formal style).
- "Play a role" → `eine Rolle spielen` (OK) — not in every paragraph.
- English apostrophe genitive ("Peter's Shop") ✗ → `Peters Shop`.
- Separate English compounds ("Kunden Service") ✗ → `Kundenservice`.

## 7. Native style — humanizer notes
Remove tells: `In der heutigen schnelllebigen Welt`, `Es ist wichtig zu beachten, dass`,
`Darüber hinaus,` / `Zudem,` / `Außerdem,` at every paragraph, `spielt eine entscheidende Rolle`,
`nahtlos`, `ganzheitlich`, `Zusammenfassend lässt sich sagen` closing sections,
Nominalstil, stacked triads, Denglisch in formal text.
Native connectors by meaning: `denn`, `daher`, `deshalb`, `allerdings`, `jedoch`, `zwar … aber`,
`also`, `nämlich`, `dabei`, `stattdessen`. German tolerates longer sentences, but keep the
verb bracket short; put the key information at the end of the clause.

## 8. As a source language
- Long compounds → unpack: `Kundenzufriedenheitsumfrage` = customer satisfaction survey.
- Verb at the end may carry negation/meaning — read the whole clause first.
- Modal particles (ja, doch, mal, eben) carry tone — render tone, not words.
- Sie (formal you) vs sie (she/they) — capitalization matters.

## 9. Final checklist
- [ ] Nouns capitalized; compounds/Durchkopplung correct; ß/ss per variant.
- [ ] „…“ quotes; mandatory commas; DIN number/percent formats if localized.
- [ ] Sie/du consistent; gender of loanwords per Duden.
- [ ] No Nominalstil chains; text fits UI/slide space (check overflow).
