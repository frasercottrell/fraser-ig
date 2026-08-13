# fraser-ig

Working context for writing Fraser Cottrell's Instagram content. This repo is the
shared brain — the more that lives here, the sharper and more on-voice the content gets.

**North star:** make Fraser the go-to voice of authority in ad creative. Every post answers
*"What can I teach my audience today?"* so a stranger lands on the profile and thinks
*"If anyone understands ad creative, it's Fraser."*

## Context files

- **[operating-model.md](context/operating-model.md)** — ⭐ how to *think* about all of this: the mechanisms, tensions, and judgment. Reason from here; the rest is reference. When a rule conflicts with this, this wins.
- **[strategy.md](context/strategy.md)** — positioning, the goal, the every-post checklist
- **[tone-of-voice.md](context/tone-of-voice.md)** — how Fraser sounds (master voice reference)
- **[audience.md](context/audience.md)** — who we're talking to + their pain points
- **[business.md](context/business.md)** — offers, funnel, course, newsletters, freebies
- **[pillars.md](context/pillars.md)** — the 4 content pillars + hook formula
- **[instagram-playbook.md](context/instagram-playbook.md)** — execution: bio, trial reels, carousels, cadence, action plan
- **[hooks-swipe.md](context/hooks-swipe.md)** — hook swipe file by category
- **[proven-content.md](context/proven-content.md)** — what's already worked (idea mine)
- **[idea-bank.md](context/idea-bank.md)** — video ideas + topics + hooks (kills the blank-screen problem)
- **[results-log.md](context/results-log.md)** — real performance data + what each reel taught us (the flywheel)
- **[sources/](context/sources/)** — raw source material kept verbatim for provenance (e.g. Georgia's call-2 email)

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

## To add over time

- `posts/` — drafted and published content
- `context/content-bank.md` — the 50+ idea brain-dump
- Real client results / case-study numbers (fuel for the proof pillar)
