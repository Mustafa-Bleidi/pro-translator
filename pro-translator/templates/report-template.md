# Translation Verification Report

| Field | Value |
|---|---|
| Source file | `{source}` |
| Output file(s) | `{output}` |
| Source → target | {source_lang} → {target_lang} ({variant}) |
| Source / output format | {src_format} → {out_format} |
| Domain / register | {domain} / {register} |
| Tags applied | {tags} |
| Pages / slides / sheets processed | {pages} |
| Approx. words / segments | {words} words · {segments} segments |
| Tables processed | {tables} (rows × columns verified: yes/no) |
| Images kept untouched | {images} total · {images_with_text} contain source-language text |
| OCR used | Yes / No (pages: …, engine: …, language pack: …) |
| Glossary / terms | {terms} terms ({user_terms} from user glossary) |
| Humanize | none / light / standard / deep |

## Automated checks
| Check | Result |
|---|---|
| qa_check.py | {critical} critical · {major} major · {minor} minor (after fixes) |
| glossary_check.py | {glossary_result} |
| Segment/tag integrity | {tags_result} |

## Second review
| Class | Found | Fixed | Remaining |
|---|---|---|---|
| CRITICAL | | | |
| MAJOR | | | |
| MINOR | | | |

## Quality ratings (with evidence)
| Dimension | Rating | Evidence |
|---|---|---|
| Fidelity | ★★★★☆ | |
| Hard-content accuracy | | |
| Terminology consistency | | |
| Naturalness | | |
| Structure | | |
| Formatting | | |

## Formatting & visual verification
- Pages inspected: {pages_checked} (first / middle / last / tables / images / RTL)
- Status: {formatting_status}
- If no visual inspection was possible: state it here.

## Notes, decisions and limitations
- Ambiguities resolved: …
- Proposed (non-established) terms: …
- Content that could not be reliably extracted/translated: …
- Known limitations of the output format: …

**Final status:** {Verified with fixes / Verified with limitations / Not verified — reason}
