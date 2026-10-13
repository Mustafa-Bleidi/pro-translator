# Contributing

Thanks for helping improve Pro Translator.

## Adding a language

1. Copy `pro-translator/languages/_TEMPLATE.md` to `pro-translator/languages/<code>.md` (ISO 639-1 code).
2. Fill **every** section: default variant and register, typography, numbers and dates,
   grammar rules, terminology conventions, traps, native-style (humanizer) notes, notes on the
   language as a source, and the final checklist. Use real examples in the native script.
3. Register the tag:
   - `pro-translator/SKILL.md` → table in §1.1
   - `pro-translator/scripts/qa_check.py` → `LANG_INFO` (script regex, Latin or not,
     expected length ratio) and `TELLS`
   - `pro-translator/scripts/preflight.py` → `TESS`, `FC_LANG`
   - `pro-translator/scripts/office_segments.py` → `LANG_DEFAULTS` (and `RTL` / `COMPLEX` if relevant)
   - `README.md` and `README.ar.md` tables
4. Ideally, ask a native speaker who translates professionally to review the profile.

## Improving rules

Rules must be specific and testable. "Use natural language" does not help;
"Avoid `يتم + مصدر`; use a direct verb" does. Include an example for each rule.

## Scripts

- Keep `qa_check.py`, `glossary_check.py` and `preflight.py` **standard-library only**.
- `office_segments.py` may depend on `lxml` only.
- Add a test in `tests/test_scripts.py` for every behaviour change, then run
  `python3 -m unittest discover -s tests -v`.

## Principles that must not be weakened

Never modify originals. Never touch images that contain text. Never change numbers. Keep the
mandatory second review. Keep the humanizer's meaning lock and its ban on deceptive tricks
(deliberate errors, invisible characters, homoglyphs).
