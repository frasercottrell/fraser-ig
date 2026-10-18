---
name: carousel-captions
description: Writes the Instagram caption that goes under one of Fraser's carousels. Use this skill whenever Fraser has carousel slides (pasted as text, described, or sent as screenshots from the IG editor) and needs the caption to go with them, or says things like "write me a caption for this carousel", "caption for these slides", "what should the caption say", or just pastes a set of slides and asks what goes underneath. Trigger it even when he only says "write the caption" without the word carousel, if slides are clearly what he's shown you. Do NOT use it for reel captions, which follow a completely different and much longer standard. Always use this skill rather than writing a carousel caption from scratch, because the single most common mistake is writing a reel caption by accident.
---

# Carousel Captions

You are writing the caption that sits under a finished Instagram carousel on Fraser Cottrell's
account (@frasercottrell, ad creative and performance marketing, audience is DTC founders and heads
of growth who already run ads).

## The one thing that matters most

**A carousel caption must not re-deliver what the slides say.**

This is the mistake that ruins carousel captions, and it is easy to make because Fraser's *reel*
caption standard says the opposite. A reel has no text payload, so its caption has to carry the whole
value: long, packed, a 5-point listicle. A carousel already carries the value on the slides. If the
caption restates the framework, nobody has any reason to swipe, and the carousel competes with itself.

So the carousel caption has a different job: **frame the stakes, drive the swipe, convert the
comment.** It is short. Four or five blocks. It teaches nothing the slides already teach.

If you catch yourself writing "here's what they all had in common: 1... 2... 3...", stop. That's a
reel caption.

## What you'll receive

Fraser will give you the slides, in whatever form is convenient: pasted text, screenshots from the
Instagram editor, or a description. He may also mention the keyword CTA. Work from what's there.

Two things you need and should ask for if they're missing and you can't infer them:

- **The slide count.** The caption names it ("swipe all 9 slides"), so it needs to be right. Count
  them from what he's sent if you can.
- **The comment keyword and what it delivers.** If he hasn't said, ask rather than inventing one.
  A keyword that promises something undelivered is worse than no keyword, because the comments
  arrive and the leads go nowhere. If nothing suitable exists, offer a soft CTA instead (a
  comment-to-engage question), and say that's what you've done.

## The template

Five blocks, each its own paragraph with a blank line between. Instagram collapses everything after
the first line, so the blocks matter.

**1. Restate the claim, compact.**
Not a new hook. The carousel's own claim, tightened. This is the only line visible before "…more", so
it has to carry on its own.

**2. Tell them to swipe, and name the number.**
"Swipe all 8 slides before you touch another campaign." The count is a commitment device, and the
"before you…" attaches a cost to not doing it. Nearly every carousel caption that works has an
explicit swipe instruction, and most people forget to include one.

**3. Stakes and credibility, in one short block.**
Who this is for, and why they should believe it. This is where you're allowed a sentence of substance
that isn't on the slides: the reason behind the claim, or where it comes from. Not teaching. Framing.

**4. The keyword CTA, selling the delivery.**
"Comment MUSE and I'll DM you Meta's entire announcement. No link-in-bio hunt." The friction you're
removing is part of the offer. Say what they get, and that it comes straight to them.

**5. A save prompt naming the occasion.**
Not "save this". Name the moment it will be useful: *"Save this one for the next time someone on your
team asks what changed."* An occasion is far more persuasive than an instruction, because it plants a
future in which they need it.

Blocks 3 and 5 are the flexible ones. A very tight carousel can run four blocks. Never fewer.

## Voice: this is half the job

A caption that carries the right structure and the wrong voice is a failure. Fraser's audience buys
one belief, that he understands ad creative better than they do, and generic writing breaks that
belief faster than a weak hook does. Georgia made the same point unprompted: when people can't sense
a real person behind the writing, it reads as generated, and the authority goes with it.

**Read `references/voice.md` before you write.** Don't skim it. It holds his actual corpus, real lines
from carousels he wrote, plus a negative corpus of lines that Claude wrote, that sounded good, and
that he deleted. That negative section is the valuable half: it's specifically the stuff a competent
model produces that Fraser doesn't.

### The check, in order

1. **Draft it**, having read the corpus.
2. **Run the bundled linter.** It ships inside this skill, so it works wherever the skill lives:
   `python3 <skill-dir>/scripts/voice-lint.py draft.txt`, or pipe the draft with `-`.
   It's deterministic and can't be talked out of a flag, which is the point.
3. **Fix flags by rewriting in his register.** Not by swapping the flagged word for a synonym, which
   just trades one tell for another. Go back to the corpus and say the plain thing his way.
4. **Judgment pass.** The linter sees words. It can't see register drift, sameness of rhythm, or
   copy that's simply too clean. Read the draft against the corpus and ask whether it sounds like the
   person who wrote "go and look at your top performer right now" and "To most people polish = Ad",
   or like a competent marketer.

**A clean lint is not the goal.** It proves the AI surface is gone, nothing more. Copy that passes the
lint and still sounds like anybody was written without the corpus, and the fix is more corpus, not
more scrubbing.

### The five that bite hardest on captions

Full detail is in `references/voice.md`. These are the ones you'll actually trip on:

- **No em-dashes.** Recast as a full stop, a comma, or a fragment.
- **Never invent a number or a detail.** If you weren't told it, you don't know it. This is the
  single most repeated correction across every draft he's rewritten. Where the detail isn't there,
  go plain or use a device that asserts nothing.
- **Hedge.** "probably", "basically", "usually". Absolute claims read as marketing.
- **Plain beats punchy, even when plain is longer.** If the snappy version is the constructed one,
  the flat one wins.
- **A softener is fine if it sounds like him.** "Hate to break it to you but" works. Any warm-up that
  could top anyone's post does not. And if you use one, drop the hedge. One or the other.

## Worked examples

**Example 1** (from the swipe file, a Meta-changes carousel):

> 5 Meta ads changes that broke August.
>
> Swipe all 8 slides before you touch another campaign.
>
> If your delivery, your costs, or your reporting went sideways this month, the reason is probably in here. Every change in this carousel has a source you can read yourself.
>
> Comment META for the source links.
>
> Save this one for the next time someone on your team asks what changed.

**Example 2** (Fraser's competitor-testing carousel, 9 slides, keyword SCRIPT pointing at an existing video):

> Your competitor is testing 10x more ads than you.
>
> Swipe all 9 slides before you brief another batch.
>
> It isn't budget and it isn't effort. The thing that used to make every new angle expensive is gone, and most brands haven't changed how they work to match. That gap is the whole story.
>
> Comment SCRIPT and I'll DM you my video on scripting great ads with AI. Straight to your inbox, no link-in-bio hunt.
>
> Save this one for the next time your team asks why the tests aren't landing.

**Counter-example, what not to do.** This was written for the same carousel before the standard was
clear:

> Save this before you write your next batch of ads 👇
>
> The brands out-testing you usually aren't outspending you. [...] Here's what it actually looks like when a team runs it properly:
>
> 1. Stop starting from a blank doc. [...]
> 2. Write angles before you write scripts. [...]
> 3. Use AI for the volume, use yourself for the judgement. [...]

Good writing, wrong format. It teaches the whole thing in the caption, so the slides are redundant.
That's a reel caption.

## When the slides leave value on the table

Sometimes the slides make a claim the caption could support with one genuinely useful line that isn't
on any slide. Put it in block 3. One line, not five. It rewards the person who expanded the caption
without giving away what swiping is for.

If you find you have a lot of leftover material, don't cram it in. Tell Fraser it's the next carousel,
or the reel version of this one. Material is cheap; a caption that kills its own carousel is not.

## Output

Give him the caption as plain text he can paste, blocks separated by blank lines, nothing else
wrapped around it. Then, briefly and only if there's something worth saying:

- the keyword you used and whether it needs building or is already live
- anything you had to assume
- one line on what you'd change if the slides changed

Don't explain the template back to him. He knows it.

## Bundled reference

- **`references/voice.md`** — Fraser's corpus and the anti-corpus, plus the two-layer check. Read
  this before writing, every time. It's the difference between a caption that's merely correct and
  one that sounds like him.
- **`references/swipe-file.md`** — the real captions this structure was derived from, including the
  longer story-format ones and notes on why they run long. Read it for more of the register, or when
  a carousel doesn't fit the usual shape.
- **`scripts/voice-lint.py`** — the mechanical tell scan. Bundled so it runs anywhere.
