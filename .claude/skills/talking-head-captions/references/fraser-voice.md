# Sound like Fraser, not AI

The linter (`scripts/voice-lint.py`) catches the *mechanical* tells (em-dashes, negative parallelism,
balanced triads, participle tails). It cannot hear whether a caption sounds like Fraser. That's a
judgment pass, and it's the difference between a correct caption and one Fraser will actually post.

## Ground truth: how Fraser actually talks

These are verbatim from Fraser's own filmed talking heads. This is the target cadence. Read them, then
write so the caption could sit next to them without a seam.

- "I've tested over 10,000 ads, and I'd say 90% of them were ugly ads." … "I don't know the science behind it."
- "I hate to admit this, but the most successful ad growth hack that I've used included feet pics." … "It's kind of disgusting."
- "The mad thing about this that people don't realise is each of these videos is entirely scripted." … "We're not leaving it up to chance and letting the creator just waffle with some bullet points."
- "When I used to work in filmmaking, we had this saying called kill your darlings. I know it sounds horrible, right?"
- "Brands are wasting money on ads because they're doing these three things by hand." … "If you can believe it, people are still looking through Reddit manually."
- "This ad from Grüns is their top performer, yet it breaks every single marketing rule." … "The audience is going to self-target themselves."
- "Literally copy and paste your best review and put it on top of a product image."

## Fraser's signature moves (do these)

- **Confession / self-deprecation openers.** "I hate to admit this…", "I know it sounds horrible, right?"
  He lowers his status before he teaches. It's disarming and it's him.
- **The self-undercut.** A number or credential immediately deflated: "I've made 10,000 ads. Most of
  them flopped." That's why he can open on a credential when the tone doc says don't — the humility
  cancels the brag. A bare flex ("I've made 10,000 ads, so listen up") is NOT him.
- **Casual intensifiers.** "the mad thing is", "kind of disgusting", "if you can believe it",
  "honestly", "literally", "basically". Sprinkled, not stacked.
- **Concrete numbers as proof.** 10,000 ads, 70%, 90%. Always prefer a real number to "a lot".
- **Direct second person.** "your ads", "you're already behind", "go steal it". He talks *at* one person.
- **British and blunt.** "waffle", "yap", "mate" energy, "cleaning up", "printing money". Not American
  hustle-speak.
- **Trailing, spoken endings.** He lets a line tail off the way speech does: "…and just let the product
  do the work." Don't over-tidy every sentence into a neat clause.
- **Rhythm: short, short, longer, short.** Fragments for punch. A rhetorical question to turn the corner.

## AI tells to kill (judgment-level — the linter won't flag these)

- **Listicle throat-clearing:** "Here are 5 tips…", "In this post, I'll break down…". Just start.
- **Over-symmetry:** every list item the same length and shape ("It works because…" x3). Vary them.
  Real speech is lumpy. Perfectly parallel bullets scream template.
- **The "it's not about X, it's about Y" reflex** and "the truth is…" as filler. Fine once if earned,
  a tell when reflexive.
- **Hedging and softeners:** "it's worth noting", "arguably", "in many cases", "that said". Fraser is
  blunt. Cut them.
- **Corporate warmth:** "I'm excited to share", "hope this helps", "let me know your thoughts". Banned
  (see tone-of-voice.md).
- **Uniform sentence length.** If every sentence is 12–15 words, it reads like a machine. Break it up.
- **Explaining the joke / over-clarifying.** He trusts the reader. Say it once, move on.
- **A tidy moral bow** that restates everything. End on one line that lands, not a summary.

## The read-aloud test (do this before delivering)

Read the caption out loud. Ask:
1. Could this sentence come out of Fraser's mouth in one of the transcripts above? If it sounds like it
   needs a podium, rewrite it.
2. Is there a self-undercut or a confession somewhere, or does it read like a brag?
3. Did I vary the sentence lengths, or is it a wall of same-size lines?
4. Is there one real number or concrete detail, not vague claims?
5. Would a busy DTC founder feel talked-to by a mate, or lectured by a brand?

If any answer is off, rewrite that part in his register. Then run `voice-lint.py` for the mechanical pass.
Both passes have to be clean: the linter for the tells it catches, this checklist for the ones it can't.
