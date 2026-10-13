# Terminology — one concept, one term, everywhere

## 1. Priority of sources (highest wins)

1. The user's glossary (`--glossary=FILE`) and explicit user instructions.
2. Terminology already used in the user's previous translations / reference files they gave.
3. Official terminology: standards bodies, laws/regulations in the target country, official
   product localizations, the organization's own target-language website.
4. Established usage in the target-language professional field.
5. Your own coinage — last resort; mark it in the report as "proposed term".

When web search is available and the term is high-stakes (legal, medical, regulatory, product
UI), verify the established equivalent instead of guessing.

## 2. Building the term map (Phase 3)

1. Scan the whole source first. Collect: recurring nouns/noun phrases, defined terms
   ("the 'Service'", capitalized defined terms in contracts), acronyms, product/feature names,
   units, role names, UI labels, domain jargon.
2. For each, decide the target term, part of speech, gender/number if relevant, and whether
   the source term is shown in parentheses on first occurrence.
3. Record homonyms with context: *"charge"* (billing) vs *"charge"* (electrical) vs *"charge"* (legal).
4. Save as CSV for long jobs (`templates/glossary-template.csv` columns):
   `source,target,target_lang,part_of_speech,context,first_use_note,avoid`

## 3. First-occurrence policy

For technical, scientific, legal, medical and academic text, show the source term in
parentheses at the **first occurrence** in the document (and optionally first occurrence per
chapter in very long documents), then use only the target term:

- `Machine Learning` → `التعلم الآلي (Machine Learning)` → afterwards `التعلم الآلي`
- `Large Language Model (LLM)` → `大型语言模型（Large Language Model，LLM）` → then `大型语言模型` or `LLM`

Skip parentheses for: everyday words, marketing/literary text, UI strings, subtitles.
Acronyms: keep the internationally used acronym (API, GDP, DNA, HTML) unless the target has an
established local one (French: ADN for DNA, PIB for GDP; Spanish: ADN, PIB; Russian: ДНК, ВВП;
Arabic usually keeps the Latin acronym in technical writing; Chinese keeps Latin for tech).

## 4. Consistency rules

- Never alternate synonyms for a defined term to "avoid repetition". In legal/technical text,
  repetition is correct; elegant variation creates ambiguity.
- Keep part-of-speech families consistent: *configure/configuration/configurable* map to one root
  in the target where the language allows it.
- UI elements: use the exact localized label of the software if it exists in that language
  (e.g. Microsoft, Apple, Google terminology portals); otherwise keep the English label in
  quotation marks and translate the instruction around it.
- Capitalization of defined terms follows the target profile (German capitalizes all nouns;
  most others capitalize defined terms only if the source does and the target style allows).
- After the translation, run `scripts/glossary_check.py` and fix every inconsistency.

## 5. Domain notes

| Domain | Priorities |
|---|---|
| Legal / contracts | Defined terms locked; "shall/must/may" mapped to the target's normative modal system consistently; no paraphrasing of obligations; numbering identical; keep party names exact. |
| Medical / pharma | Official INN drug names; anatomical terms per target standard; doses/units untouched; patient-facing text plain and clear; regulatory phrases (EMA/FDA/national) per official templates. |
| Technical / IT | UI labels per official localization; code untouched; imperative instructions; consistent verbs (click/select/enter). |
| Academic | Discipline-standard terms; citations untouched; hedging preserved exactly (may/might/suggests ≠ proves). |
| Financial | Official accounting terms (IFRS/GAAP local versions); numbers untouched; currency codes kept. |
| Marketing | Transcreation allowed for slogans **only if the user wants**; otherwise faithful but idiomatic; brand names and taglines flagged. |
| Literary | Voice, rhythm, register, imagery; names kept; footnotes only if the source has them. |
| UI / software | Length limits, placeholders, plural rules, consistent tone (formal/informal address chosen once). |

## 6. Do-not-translate list (DNT)

Maintain a DNT list per project: brand names, product names, code identifiers, trademarked
terms, names the user says to keep. Check it before each batch.
