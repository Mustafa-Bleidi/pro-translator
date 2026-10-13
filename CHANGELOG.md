# Changelog

## 2.0.0 — 2026-10-13

Complete rewrite of `professional-en-ar-translation` as **Pro Translator**.

### Added
- 15 languages with dedicated profiles and tags: `--ar --en --zh --es --hi --fr --pt --ru --bn --ur --id --de --ja --tr --ko`, plus regional variants and aliases.
- Any-to-any translation with source auto-detection (`--from=xx` to force).
- Modifier tags: `--humanize[=light|deep]`, `--formal`, `--casual`, `--domain=…`, `--localize`, `--glossary=…`, `--bilingual`, `--review`, `--quick`, `--report`.
- Humanizer with a meaning lock, universal and per-language tell lists, and level guide.
- Split into a multi-file layout (references, languages, templates, scripts) with progressive loading.
- `office_segments.py`: lossless DOCX/PPTX/XLSX round-trip with inline-format tags, RTL setup, complex-script formatting and language tagging.
- `qa_check.py`: automated source/target verification.
- `glossary_check.py`: terminology consistency.
- `preflight.py`: tool, OCR pack and font availability report.
- Report, glossary and style-sheet templates; unit tests and CI.

### Kept from 1.x
- All preservation rules (originals, images with text, numbers, code, references), the mandatory second review, error classification and the verification report.

## 1.0.0
- English → Arabic professional document translation skill.
