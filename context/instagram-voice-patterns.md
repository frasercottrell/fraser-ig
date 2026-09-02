# Instagram Voice Patterns — Fraser Cottrell

The reference for writing Instagram scripts that sound **exactly like Fraser** (and, where it fits, a
little funnier). Use this alongside `tone-of-voice.md` (master voice) and the talking-head caption skill
at `.claude/skills/talking-head-captions/` — this doc is the *spoken video* companion to those.

## How this was built (and how to grow it)

Built from **verbatim transcripts of Fraser's real IG talking heads** (7 videos as of first draft:
ugly-ads, Grüns teardown, AI research tools, kill-your-darlings, yapper, foot-device, static formats).
These are ground truth — his actual spoken words, not scraped auto-captions. **The more transcripts we
add, the sharper this gets** — paste any new video's transcript and it gets folded in. It is NOT a
complete scrape of the profile (that can't be automated from here), so treat the patterns as strong and
real but still growing.

---

## One-line voice

A sharp, slightly cheeky practitioner talking to one busy DTC founder like a mate who actually makes the
ads. Confident about the work, self-deprecating about himself. Teaches the real method, for free, fast.

## Tone & sentiment

- **Confident but humble.** Big claims backed by real numbers, then undercut with honesty: "I've tested
  over 10,000 ads" but "I don't know the science behind it." He never sounds like a guru.
- **Challenger energy.** He tells you you're doing it wrong, directly: "your ads aren't converting the
  same way this one is", "you're already behind". Never nasty, always followed by the fix.
- **Generous.** Gives the actual playbook, the free sheet, the tool names. No withholding.
- **Dry and a bit self-aware.** The humour lives in asides, not jokes (see Humour).

## Cadence & rhythm

- **Spoken, loose grammar.** He lets lines tail off the way real speech does: "then just letting the
  product do the work", "the rest just like falls into place". Don't tidy every sentence into a neat clause.
- **Sequencing as structure.** He walks you through in order: "The first thing to notice… The next thing
  is… And then she reveals…". It feels like watching over his shoulder.
- **Recipe cadence.** "All you need is X… and then all you need is Y." Makes things feel easy and doable.
- **Short claim → quick context → short claim.** Mixes lengths. Fragments for punch.
- **Softening qualifiers** everywhere: "essentially", "basically", "kind of", "perhaps", "I'd say". They
  make him sound like a person thinking out loud, not reading a script. (Keep some; don't let them turn
  into hedging that dulls a claim.)

## How he STARTS videos (never a greeting — open on tension)

He never says hi. The first line is always a hook. His real openers, by type:

- **Confession:** "I hate to admit this, but the most successful ad growth hack I've used included feet pics."
- **Big number, self-undercut:** "I've tested over 10,000 ads, and I'd say 90% of them were ugly ads." /
  "I've tested thousands of static ads, but only three keep on converting."
- **Competitor threat / FOMO:** "Your competitors are running yapping ads, and if you don't know what
  they are, you're already behind."
- **Contrarian brand claim:** "This is why this ad from Grüns is their top performer, yet it breaks every
  single marketing rule."
- **Blunt diagnosis:** "Brands are wasting money on ads because they're doing these three things by hand."
- **Mid-thought pickup:** "Because your personal opinion is clouded by so many different factors…" (drops
  you into an argument already in motion).

> Rule: open on a claim, number, confession, or threat, and get "you/your" in fast.

## How he ENDS videos (soft CTA + a self-aware tag)

- **Soft follow:** "If you like tips like this, hit the follow button." / "if you want more tips like
  this, make sure you drop a follow."
- **Follow with a self-deprecating tag:** "…hit the follow button, because I make these videos all the
  time. Or at least I'm trying to." (The throwaway self-jab is very him.)
- **Comment keyword for a resource:** "Comment FEET down below and I'll send it over to you." Always tied
  to a real deliverable (a sheet, a framework, a breakdown).

> He rarely hard-sells. The close is either "follow for more" or "comment X for the thing".

## Structures he leans on

- **Teardown walk-through:** claim it breaks the rules → "first thing… next thing… then…" → the lesson.
- **Diagnosis → fix:** "you're wasting money because X" → "here's what to do instead."
- **Recipe:** "all you need is A, then B, then C" → "have all three and you're sorted."
- **Analogy from his past:** the filmmaking "kill your darlings" bit — he borrows a rule from one world
  and maps it onto ads. Distinctive and worth doing more of.

## Words & phrases he says OFTEN (his tics — sprinkle, don't stack)

- "essentially" · "basically" · "kind of" ("kind of disgusting")
- "the mad thing about this is…" / "the thing people don't realise is…"
- "if you can believe it" · "literally" ("literally copy and paste")
- "I'd say…" · "I argue…" · "in brief"
- "all you need is…" · "you might want to think again"
- "just like" as a filler ("the rest just like falls into place")
- "for example" · "over the past couple of years"
- "guaranteed to succeed" / "we can guarantee results"
- His nouns: hook · creative · UGC · static · B-roll · ad library · ad account · spend · convert · scale ·
  self-target · low-fi · subline · offer

## Words & things he NEVER says (keep these OUT)

- Corporate verbs: leverage, unlock, elevate, supercharge, synergy, game-changer.
- Hype openers: "I'm excited to share", "thrilled to", "in today's landscape."
- Forced enthusiasm / exclamation-mark marketing.
- Greetings ("Hey guys", "What's up") — he opens cold on the hook.
- Over-explaining basic marketing terms — he assumes an operator audience.
- **Em-dashes** in anything written (captions) — loudest AI tell. (Doesn't apply to speech, but the
  written caption must be em-dash-free; run `scripts/voice-lint.py`.)

## Niche / generational / slang terms he uses (this is a lot of his flavour)

- **"yap / yapping"** — Gen-Z content slang for casual talking-to-camera. He uses it knowingly.
- **"the mad thing"**, **"waffle"** ("let the creator just waffle") — British, casual.
- **"low-fi"**, **"TikTok shop"**, **"UGC"**, **"B-roll"**, **"ad library"**, **"GLP1"**, **"self-target"**,
  **"ask me anything box"** — the native vocabulary of a 2020s performance-creative operator.
- **"growth hack"** — used slightly tongue-in-cheek.
- British register throughout: "realise", "loads of time", "kind of", understated delivery.

> Using this vocabulary correctly is a big part of sounding like him. It signals he lives in the work.

## Humour — how it actually works

His comedy is **dry, British, deadpan, and self-aware**. He doesn't tell jokes. The funny comes from:

1. **Self-deprecation / status-lowering:** "I hate to admit this", "I know it sounds horrible, right?",
   "or at least I'm trying to."
2. **Gross-out honesty:** "it's kind of disgusting", "feet pics", "dry feet being shaved". He names the
   grim thing plainly and lets it be funny on its own.
3. **Understatement after a bold claim:** "the rest just like falls into place" (after "we scaled them 70%").
4. **Wry acknowledgement of absurdity:** "the mad thing is…", "if you can believe it, people are still
   doing X manually."

## How to make him a LITTLE funnier (the brief)

Escalate what's already there — don't bolt on gags that aren't his:

- **Push the gross/absurd honesty one notch further.** He gets funnier the more bluntly he names the
  cringe thing (the feet, the ugly ads, the sad person eating breakfast in old UGC). Lean in.
- **More mid-sentence self-jabs** in the "or at least I'm trying to" style — a throwaay aside that
  punctures his own authority right after a big claim.
- **Deadpan understatement** as the button on a stat: make the huge result sound almost boring.
- **A dry parenthetical throwaway** ("…because apparently that's a thing now") to flag the madness of the
  industry without breaking character.
- **Call out the awkwardness out loud** — the thing everyone's thinking but won't say. His honesty *is*
  the joke; sharpen it, don't clown it.

Rule: if a line feels like a comedian wrote it, cut it. If it feels like Fraser noticing something absurd
and saying it flatly, keep it. Funnier = more honest and more deadpan, not more jokes.

## Quick reference for scriptwriters

- Open cold on a claim/number/confession/threat. Never greet.
- Get "you/your" in within the first two lines.
- Walk it through in sequence, recipe-style, with softeners ("essentially", "basically").
- Back everything with a real number or a named tool/format.
- Undercut every flex with honesty. That's the whole charm.
- Use the native slang (yap, low-fi, UGC, ad library) correctly.
- Close soft: "follow for more" or "comment X for the thing", ideally with a self-aware tag.
- For captions, run `voice-lint.py` and do the read-aloud test in the caption skill.
