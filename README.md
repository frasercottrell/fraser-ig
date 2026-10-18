# fraser-ig

Working context for writing Fraser Cottrell's Instagram content. This repo is the
shared brain — the more that lives here, the sharper and more on-voice the content gets.

**North star:** make Fraser the go-to voice of authority in ad creative. Every post answers
*"What can I teach my audience today?"* so a stranger lands on the profile and thinks
*"If anyone understands ad creative, it's Fraser."*

## ⚠️ One brain, one branch (read first)

This repo IS the memory — nothing carries between Claude sessions except what's committed here.
So the whole brain must live on **one branch: the repo default** (`claude/instagram-content-context-tp1gwf`).
History fragmented once (call-2 notes landed on a different branch than the talking-head work, and a
later session couldn't see them). To stop it happening again:

- **Always branch new work from the default**, and **merge it back to the default** when done. Don't leave
  learnings stranded on a feature branch.
- **Every consultant/strategy call** → raw source verbatim in `context/sources/`, then ingest the
  *knowledge* into the right context file (ideas → `idea-bank.md`, execution → `instagram-playbook.md`).
- If something you're sure exists isn't on the working branch, search **all** branches
  (`git log --all`, `git branch -a --contains <hash>`) before concluding it's gone.

## Context files

- **[operating-model.md](context/operating-model.md)** — ⭐ how to *think* about all of this: the mechanisms, tensions, and judgment. Reason from here; the rest is reference. When a rule conflicts with this, this wins.
- **[strategy.md](context/strategy.md)** — positioning, the goal, the every-post checklist
- **[tone-of-voice.md](context/tone-of-voice.md)** — how Fraser sounds (master voice reference)
- **[audience.md](context/audience.md)** — who we're talking to + their pain points
- **[business.md](context/business.md)** — offers, funnel, course, newsletters, freebies
- **[pillars.md](context/pillars.md)** — the 4 content pillars + hook formula
- **[instagram-playbook.md](context/instagram-playbook.md)** — execution: bio, trial reels, carousels, cadence, action plan
- **[carousels.md](context/carousels.md)** — ⭐ the complete carousel guide: slide-by-slide anatomy, slide-2 mechanics, CTA rules, caption bar, testing discipline
- **[hooks-swipe.md](context/hooks-swipe.md)** — hook swipe file by category
- **[proven-content.md](context/proven-content.md)** — what's already worked (idea mine)
- **[idea-bank.md](context/idea-bank.md)** — video ideas + topics + hooks (kills the blank-screen problem)
- **[talking-head-caption-style.md](context/talking-head-caption-style.md)** — the register talking-head captions should be written in (3 modes; vary the opener, weave credentials, add personality, rotate the CTA)
- **[instagram-voice-patterns.md](context/instagram-voice-patterns.md)** — how Fraser sounds on camera (openers, enders, cadence, words he says/never says, slang, humour) for writing IG scripts that sound exactly like him. Grows as more real transcripts are added.
- **[results-log.md](context/results-log.md)** — real performance data + what each reel taught us (the flywheel)
- **[instagram-brain.md](context/instagram-brain.md)** — condensed working summary (the one test, format scoreboards, save ladder, carousel cover rule, how to work with Fraser). Good first read.
- **[sources/](context/sources/)** — raw source material kept verbatim for provenance (Georgia's call-2 email, call-3 email + **call-3 transcript**, caption examples, the 2026-10-18 handoff note)

## Hooks

- **[hooks/LEDGER.md](hooks/LEDGER.md)** — every hook handed to Fraser (2026-09-16 → 2026-10-04) with status + result, the MISS 1-8 rejection rules, findings already given (don't restate), and the tested-won / tested-lost / untested angle map. **Check it before writing any new hooks.**
- `hooks/YYYY-MM-DD-*.md` — individual hook batches. **Numbering is separate from `posts/batch-NN-*.md`** (hooks batch 15/16 ≠ posts batch 15/16) — always cite by filename.

## Anti-AI-slop check

Every piece of content should sound like Fraser, not like a machine. Two reference docs + a linter
(pulled from the anti-ai-slop-scriptwriting toolkit, `LICENSE.md` — noncommercial):

- **[context/ai-writing-tells.md](context/ai-writing-tells.md)** — the inventory of *written* AI tells (vocabulary, negative parallelism, balanced triads, participle tails…)
- **[context/spoken-script-voice.md](context/spoken-script-voice.md)** — how human content *sounds* out loud (for talking-head reel scripts)
- **`scripts/voice-lint.py`** — mechanical scan for the tells. Run on any draft:
  ```
  python3 scripts/voice-lint.py path/to/draft.md   # or '-' for stdin
  ```

**Workflow:** draft → run `voice-lint.py` → fix real flags by rewriting in Fraser's register (not thesaurus-swapping) → sanity-check against the tells doc.

## Skills

- **`.claude/skills/talking-head-captions/`** — writes the caption for a talking-head video from its
  transcript, in Fraser's voice (3 modes, vary the opener, weave a credential, rotate the CTA, lint it).
  Invoke with `/talking-head-captions` or just paste a talking-head transcript and ask for a caption.
  **Talking heads only** — not trial reels, carousels, or static-ad copy.
- **[.claude/skills/carousel-captions/](.claude/skills/carousel-captions/)** — writes the caption
  under a finished carousel. Carousel captions are a different job from reel captions (short, frames
  and drives the swipe, never re-delivers the slides), and getting them confused is the easy mistake.
  Includes the swipe file the standard came from.

## To add over time

- `posts/` — drafted and published content
- `context/content-bank.md` — the 50+ idea brain-dump
- Real client results / case-study numbers (fuel for the proof pillar)
