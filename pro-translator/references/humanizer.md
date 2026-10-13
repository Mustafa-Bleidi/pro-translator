# Humanizer — `--humanize`

Purpose: make text read like it was written by a skilled native writer of that language, not by
a machine translation engine or a language model. The standard is a professional native editor
who knows the subject.

Usage:
- `--humanize` alone → rewrite the input in its own language.
- `--<lang> --humanize` → translate first (full pipeline), then humanize the target text.
- Levels: `--humanize=light` (fix only clear tells, minimal edits) · `--humanize` (standard) ·
  `--humanize=deep` (free restructuring of sentences and paragraph flow, still meaning-locked).

---

## 1. The meaning lock (non-negotiable)

Humanizing changes **how** something is said, never **what** is said.

- No new facts, numbers, examples, anecdotes, quotes, opinions or claims. No invented personal
  experience ("When I worked at…").
- No removed facts, caveats, conditions or hedges. *"may reduce"* never becomes *"reduces"*.
- Terminology from the term map stays. Defined terms stay identical.
- Names, numbers, code, citations, URLs, placeholders, tags: untouched.
- Structure stays (headings, lists, tables), except `deep` may merge/split sentences and reorder
  sentences **within** a paragraph when the target's information flow requires it.
- No deliberate typos or grammar errors, no invisible/zero-width characters, no look-alike
  letters from other scripts, no random noise. These degrade the document, can corrupt files and
  search, and are a form of deception. Quality writing is the only method used here.
- Honesty about detectors: AI-text detectors are unreliable and also flag human writing. This
  mode makes text genuinely natural; it does not and cannot promise any detector score. If the
  user asks for a guarantee, say so plainly.

## 2. Process

1. **Read for purpose and audience.** Who reads this, in what situation, at what register?
2. **Diagnose.** Scan for the tells in §3 and the language profile's "Native style" section.
   Note the dominant problems (e.g. "uniform sentence length + stacked connectors + calqued
   passives").
3. **Rewrite** paragraph by paragraph using §4, at the requested level.
4. **Read aloud test** (mentally): would a native professional say it this way? Any sentence that
   needs a second read gets rewritten.
5. **Meaning check** against the pre-humanized text (and the source, when translating): every
   claim, number, condition still there, nothing new. Re-run `qa_check.py`.
6. **Optional log** (on request or with `--report`): categories fixed, with 2–3 before/after examples.

## 3. Tells to remove (universal)

### 3.1 Machine-translation tells
- Source-language word order and sentence length carried over unchanged.
- Calques of idioms and collocations ("play a role", "take a decision", "in terms of") rendered
  literally where the target has its own collocation.
- Overuse of passives/nominalizations that mirror English (*the implementation of the
  configuration is performed by…*).
- Pronoun overuse in pro-drop languages (ar, es, pt, ja, ko, zh, tr, hi, bn, ur, id often drop).
- Source punctuation and typography (English quotes in French, spaces in Chinese, Western comma
  in Arabic).
- Source capitalization in headings (Title Case copied into languages that use sentence case).
- Inconsistent address (formal/informal mixed).
- False friends and wrong-sense dictionary picks.

### 3.2 Language-model tells
- **Vocabulary inflation:** "delve, tapestry, testament, pivotal, crucial, seamless, robust,
  leverage, landscape, realm, foster, underscore, navigate, holistic, cutting-edge,
  game-changer, unlock, empower, elevate" (and their equivalents in each language — see the
  profile). Use plain, precise words.
- **Throat-clearing openers:** "In today's fast-paced world…", "It is important to note that…",
  "When it comes to…".
- **Signposting and wrap-ups:** "Let's dive in", "In conclusion", "Overall", "Ultimately" closing
  every section; a summary paragraph that repeats what was just said.
- **Rule of three everywhere:** stacked triads of adjectives or clauses in every paragraph.
- **Reveal structures:** "It's not just X — it's Y", "Here's the thing:", colon reveals, rhetorical
  questions answered immediately.
- **Connector stacking:** every sentence or paragraph starting with Moreover / Furthermore /
  Additionally / However.
- **Uniform rhythm:** every sentence 15–25 words; every paragraph 3–4 sentences; identical
  paragraph shapes.
- **Em-dash and bold overuse;** emoji and headings where prose would do.
- **Hedge stacking / performed sincerity:** "may potentially", "truly", "genuinely", "honestly".
- **Generic abstraction:** claims without the concrete noun/verb the source actually has.

## 4. Techniques

1. **Native information flow.** Rebuild sentences the way the target language orders
   information (topic first in zh/ja/ko; verb-initial is natural in Arabic narrative; German verb
   brackets; Turkish/Japanese/Korean/Hindi verb-final). Don't keep the English skeleton.
2. **Rhythm with purpose.** Mix short and long sentences where the content allows: a short one
   for the key point, longer ones for explanation. Don't vary length randomly.
3. **Precise verbs over nominal chains.** "decide" over "make a decision"; Arabic "نفّذ" over
   "قام بتنفيذ"; Russian "проверить" over "осуществить проверку".
4. **Connectors by meaning, not by habit.** Use a connector only when the logical relation needs
   marking; vary them using the language's own repertoire (profile lists them). Often the best
   connector is none.
5. **Native collocations.** Replace calqued word pairs with the target's natural pairs
   (profile "Traps" section).
6. **Register fit.** Same formality throughout; idioms only if the register allows them; no
   slang in formal text, no bureaucratic jargon in friendly text.
7. **Cut padding, not content.** Remove filler words and redundant framing — never a fact,
   qualifier or condition.
8. **Paragraph shape.** Let paragraph length follow content; one-sentence paragraphs are fine
   when they carry weight.
9. **Concrete over vague** — only using concrete material that is already in the text.
10. **Punctuation like a native:** the target's own conventions, few dashes, few colons.

## 5. Level guide

| Level | Edits | When |
|---|---|---|
| `light` | Fix tells, calques, punctuation, connector stacking; keep sentence boundaries | Legal, medical, regulated text; text already decent |
| standard | Above + restructure sentences for native flow, rhythm, collocations | Most documents, articles, reports, emails |
| `deep` | Above + merge/split sentences, reorder within paragraphs, rebuild paragraph flow | Marketing, blog, speeches, essays; text with heavy AI style |

For legal/contract text, cap at `light` even if the user asks for more, and say so in one line
(legal wording is precise by design; restructuring can change obligations).

## 6. Self-check rubric (score 1–5, aim ≥ 4 everywhere)

- Fidelity — same meaning, nothing added or lost.
- Naturalness — a native professional would write it this way.
- Register — consistent and right for the audience.
- Rhythm — varied, purposeful, no template feel.
- Precision — plain, specific words; no inflated vocabulary.

If fidelity drops below 5, revert that change.
