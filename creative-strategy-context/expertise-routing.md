# Expertise routing — which creative-strategy-context docs scriptwriting loads

> This is the scriptwriting-scoped router for the Anti-AI-Slop Script Writing Skill. The reads named here are mandatory before writing, not optional references — the script is written *through* these methods, in their vocabulary. Paths are relative to `creative-strategy-context/`. Where a brand lens overlay exists (`_<brand>-lens.md`), load it after the generic docs — it bends the rules for this brand.

## The doc catalog — what exists, so you can reason over all of it

This is the catalog of every method doc in this bundle and an honest line on what each one *is*. It is deliberately **descriptive, not prescriptive** — it does not tell you when to pull a doc, because those guesses go stale and quietly cap what you'd consider. Relevance is *your* call as the planner: read the catalog, hold the task in mind, and reason like a strategist about which docs would genuinely help — generously, biased toward pulling more.

How to use it:

- **Reason over the whole set, generously.** Don't match a label — look at what each doc actually is and pull everything that would make the script better. A script question is usually several docs at once (a hook question that's really about a persona's emotional state pulls hooks *and* emotional-delivery). There's no quota and no cap; under-retrieval is the failure mode.
- **The catalog is a starting point, not the boundary.** A one-line summary can't capture everything in a doc. When the task is gray or specific, grep the actual doc bodies for the question's concepts and open what surfaces.
- **An opened doc beats an assumption.** If you're unsure whether a doc is relevant, open it and look; the cost of reading one more is small, the cost of a generic answer is not.

Many of these docs end with a required sign-off line ("This is everything I know about X"). That stamp is a proof-of-read: if you used a doc, its sign-off must appear.

**Not a reasoning doc — never pull it for analysis:** `expertise-routing.md` (this catalog). It carries no method.

<!-- DOC-MAP:START -->
| Doc | What it is |
|---|---|
| `adapting-scripts.md` | The method for adapting an existing video or script (such as a breakout organic) into a new ad. |
| `ai-writing-tells.md` | The written AI-slop signs — vocabulary, rhetoric, and formatting tells — and the lint-then-judge review every creative deliverable passes before it ships. |
| `creative-strategy-fundamentals.md` | The senior-strategist priors — confidence before speed, the kill-list discipline, where curiosity tends to land, the trying-too-hard failure modes. |
| `customer-review-mining-method.md` | How to mine customer reviews and comments for creative material — golden nuggets, denominators, theme rates. |
| `emotional-delivery-and-timing.md` | The emotional landing state beneath hooks — valence/intensity and the TEEP buying phase (Trigger, Exploration, Evaluation, Purchase). |
| `hook-psychology.md` | The cognitive science beneath hooks — the mechanisms (notice, qualify, intrigue, reassure, move, transport) that explain why a hook works. The why-layer under the format taxonomy. |
| `hooks.md` | The reference taxonomy of hook formats with real examples — the named formats and what each one is. |
| `organic-social-analysis.md` | How to analyze organic social through a creative-strategy lens. |
| `scriptwriting.md` | The scriptwriting craft for ads — cold-audience acquisition principles and how to build a script. |
| `spoken-script-voice.md` | The doctrine of human-sounding ad scripts and the brand voice-profile method, plus the AI-tells audit run on every draft. |
| `visual-vocabulary-method.md` | The method behind a brand's visual vocabulary — in-play / adjacent / out-of-play shot classification, the script-congruence and format-dependence rules. |

<!-- DOC-MAP:END -->

## Scriptwriting — any task that produces spoken words for an ad

- `spoken-script-voice.md` — the human-voice doctrine and the brand voice-profile method; mandatory before writing any script's words, and the AI-tells audit runs on every draft
- `scriptwriting.md` — the scriptwriting craft: cold-audience acquisition principles and how to build a script
- `adapting-scripts.md` — the 1:1 adaptation method, the default flow (adapt a proven reference into the brand's voice rather than write cold)
- `visual-vocabulary-method.md` — the visual twin of the voice profile; per-beat visual direction sources from the brand's `sub-context-docs/visual-vocabulary.md`, each beat marked in-play, adjacent, or out-of-play, with the script-congruence and format-dependence rules

## The hook layer — the first three seconds

A script contains a hook, and the opener is the creative gate. Load these before writing the first three seconds:

- `hook-psychology.md` — the why-layer; reason from its mechanisms (notice / qualify / intrigue / reassure / move / transport) and diagnose a weak opener by which job it fails, before reaching for format labels
- `hooks.md` — the hook format taxonomy and examples; name the real format and ground the opener in its examples. Any opener that delays voice, motion, or sound needs explicit support from this doctrine by name
- `emotional-delivery-and-timing.md` — the layer beneath hooks: the emotional state the viewer lands in, valence/intensity, and the TEEP phase she's in. Load it when the hook has to match a mood or a decision phase, not just create an emotion

## Sourcing the customer language

Every script pulls language from real reviews, comments, surveys, voice of customer — marketing voice fails:

- `customer-review-mining-method.md` — the mining method: golden nuggets, denominators, theme rates
- `organic-social-analysis.md` — how to read the brand's own and the niche's organic as a strategist, where in-play and adjacent shots and real customer language are seen

## The review gates — the independent AI-slop check

Every script runs through two independent reviewer agents before it ships (their definitions live in `skill/reviewers/`, spawned by whichever harness you are in). The voice gate reads this doctrine:

- `ai-writing-tells.md` — the written-slop sign families and the false-positive discipline; the `creative-voice-review` agent lints against it (`scripts/voice-lint.py`) and judges the flags
- `spoken-script-voice.md` — the spoken twin; the voice gate loads it for anything spoken aloud

## The strategist priors behind the idea gate

Nobody just writes a script — it comes out of a read of what's working. These priors order that read:

- `creative-strategy-fundamentals.md` — confidence before speed, the kill-list discipline, where curiosity lands, the trying-too-hard failure modes

## The test

Before emitting, re-read the script against the loaded docs: does it use their named concepts, taxonomies, and vocabulary where they apply? A script that routes to a method but does not speak its language proves the method was never opened, and the run failed regardless of how finished the draft looks.
