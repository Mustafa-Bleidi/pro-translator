# Usage walkthroughs

## 1. Short text in chat (chat mode)

```
--es --formal
Please review the attached invoice and confirm payment by Friday.
```

→ `Le rogamos que revise la factura adjunta y confirme el pago antes del viernes.`

Only the translation is returned. Add `--report` if you want the checks listed.

## 2. Translate and humanize

```
--en --humanize
تجدر الإشارة إلى أن النظام يلعب دورًا محوريًا في تحسين الأداء، علاوة على ذلك فإنه يتم تحديثه بشكل دوري.
```

Literal output (what the humanizer prevents):
> It is worth noting that the system plays a pivotal role in improving performance; furthermore, it is updated periodically.

Humanized:
> The system does much of the work of improving performance, and it is updated regularly.

Same facts. The filler, the cliché and the stacked connector are gone.

## 3. Humanize only (no translation)

```
--humanize=light
في عالمنا اليوم، يتم استخدام الذكاء الاصطناعي من قبل الشركات بشكل كبير، ومن الجدير بالذكر أنه يلعب دورًا محوريًا في اتخاذ القرار.
```

→ `تعتمد الشركات اليوم على الذكاء الاصطناعي اعتمادًا كبيرًا، وصار له أثر واضح في اتخاذ القرار.`

## 4. A Word document into three languages

```
--ar --fr --de  handbook.docx
```

Output: `handbook_AR.docx`, `handbook_FR.docx`, `handbook_DE.docx`. Each is translated from the
English original, with its own verification report. The Arabic file is right-to-left.

## 5. Contract with your own glossary

`terms.csv`
```csv
source,target,target_lang,part_of_speech,context,first_use_note,avoid
Service Provider,مقدّم الخدمة,ar,noun,contract party,,المزوّد|مورد الخدمة
shall,يلتزم,ar,modal,obligation,,ينبغي|يجب أن يحاول
Effective Date,تاريخ السريان,ar,noun,defined term,,تاريخ النفاذ
```

```
--ar --domain=legal --glossary=terms.csv --report  agreement.docx
```

The humanizer is capped at `light` for legal text, and `glossary_check.py` must pass before delivery.

## 6. Review someone else's translation

```
--review --from=en --ja  spec.docx  spec_JA.docx
```

→ An issue table (location · source · current · problem · class · fix), scores and, on request,
a corrected `spec_JA_REVIEWED.docx`. The file you gave is never overwritten.

## 7. Subtitles

```
--pt-br  episode01.srt
```

Timecodes and cue count stay identical. Lines respect about 42 characters per line and 2 lines per cue.
