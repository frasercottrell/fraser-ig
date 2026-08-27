---
name: talking-head-captions
description: >-
  Write the Instagram caption for one of Fraser Cottrell's TALKING-HEAD videos (Fraser speaking
  straight to camera) from its transcript. Use this whenever Fraser pastes a talking-head transcript
  or auto-caption and asks for a caption, "write me a caption", "caption for this talking head",
  "do this one", or drops a filmed reel's words and wants the post copy. ALWAYS use this skill for
  talking-head captions instead of winging it — the register is specific and easy to get generic.
  This is for TALKING HEADS ONLY. Do NOT use it for trial-reel captions, carousels, static-ad copy,
  UGC ad scripts, newsletters, or LinkedIn posts — those have their own formats and standards.
---

# Talking-Head Captions

Write the caption that pairs with a filmed **talking-head** video (Fraser to camera, main-feed
convert/nurture asset). The caption is Fraser talking to people who already chose to listen, so it
sounds like him, not like a brand teaching. It **extends** the video — adds the depth the spoken
version skipped — it never just transcribes it.

## First, ground in the repo (these are the source of truth for his voice)

Read these before drafting — they carry Fraser's actual register and the rules this skill compresses:
- `references/fraser-voice.md` (in this skill) — **how to sound like Fraser and not AI. Read this every
  time.** Ground-truth voice samples from his real transcripts, his signature moves, the judgment-level
  AI tells the linter can't catch, and the read-aloud test.
- `context/talking-head-caption-style.md` — the full style guide (3 modes + rules). **Primary.**
- `context/tone-of-voice.md` — how Fraser sounds (master voice reference).
- `context/ai-writing-tells.md` — the full inventory of written AI tells to avoid.
- `context/sources/talking-head-caption-examples.md` — real captions that work (study the mechanics).
- `context/pillars.md` — which of the 4 pillars this video serves (shapes the angle).
- `references/examples.md` (in this skill) — a before/after showing templated vs. in-voice.

If the repo isn't present (running elsewhere), `references/fraser-voice.md` plus the rules below are
enough to work from.

## Inputs

1. **The transcript** (required) — the video's spoken words, usually pasted as timestamped lines.
2. **The lead magnet / CTA** — what the video promises ("comment X and I'll send you Y"). If the
   transcript ends on a CTA, mirror it. If it's ambiguous or missing, **ask** what the freebie is
   rather than defaulting to HOOKS — the freebie must match the video (see CTA rules).

## Workflow

1. **Read the transcript and name two things:** the pillar (Why Ads Work / Inside the Ad World /
   Case Study / Founder) and the *one idea* the video lands. The caption serves that one idea.
2. **Pick the caption mode** (below) that fits the video.
3. **Find the extension** — what depth did the spoken version skip? A mechanism, a "why", a bigger
   lesson, a mistake to avoid. That's what the caption adds. If the caption only restates the video,
   it's failing.
4. **Draft it** in the mode, following the rules.
5. **Two-pass voice check (both required — this is the point of the skill):**
   - **Mechanical:** `python3 scripts/voice-lint.py <draft>` (or pipe via `-`). Fix real flags by
     rewriting in Fraser's register, not thesaurus-swapping. Aim for 0 flags.
   - **Judgment (sound like Fraser):** run the read-aloud test in `references/fraser-voice.md`. The
     linter passes plenty of captions that still sound like a brand. This pass is what makes it *him*.
   A clean linter alone is not done. Both passes have to be clean.
6. **Deliver** the caption. If Fraser also wants a TOS (text-on-screen) hook, offer one specific +
   contrarian line (name a brand / a hard claim), but the caption is the job unless he asks for more.

## The 3 caption modes — pick by video type

- **Micro** — a line or two of value/opinion + one CTA. Not everything needs a listicle. Use for a
  single sharp point, a quick tool tip, a one-idea hot take.
- **Story / opinion** — a few short punchy paragraphs, one belief, personality forward. Use for
  founder takes and contrarian opinions ("here's what I actually think").
- **Value listicle** — numbered teach, 3–5 points, each with the WHY, plus a closing frame that names
  the bigger lesson. Use for frameworks, breakdowns, teardowns, "3 things / 5 tools". This is the
  workhorse for Fraser's educational talking heads — keep it, but loosen it (see rules).

## Rules (all modes)

- **Open with a result, confession, credential, or number — not a formula.** Rotate the opener.
  "I've made over 10,000 ads." / "I hate to admit this…" / "We scaled this brand 70%." The
  "Save this before X 👇" driver is fine *occasionally*, not by default. Overusing one opener is the
  single biggest tell that a batch of captions was templated.
- **Weave a credential right after the hook** — one casual line that earns the listen ("after 10,000+
  ads", "six years running an agency"). Proof said like a mate, not a CV. A credential can open the
  caption ONLY if it's immediately undercut ("I've made 10,000 ads. Most of them flopped."). The
  self-deprecation is what makes it Fraser and not a LinkedIn flex — a bare brag is off-voice.
- **Personality over polish.** Contractions, asides, the odd CAPS word for emphasis, dry humour. Mild
  swearing is on-brand if it's natural to the point (don't force it; check tone-of-voice.md). It
  should read like Fraser talking, not a brand explaining.
- **Extend the video, don't transcribe it.** Add the mechanism / the why / the bigger lesson.
- **Emoji are native** — as occasional bullet markers and warmth, especially on the CTA line
  (👇 ⭐ 🌟). Tasteful, not a rash.
- **Close on engagement, and vary how.** Rotate: (a) keyword CTA for the freebie, (b) a question
  ("Which one are you missing? 👇") that pulls comments, (c) both — question then keyword. Comments
  drive reach, so a question is often stronger than a bare CTA.
- **Align the freebie to the video.** STATIC video → the static swipe file. Yapper video → the script
  framework. Don't slap HOOKS on everything. If the promised deliverable doesn't exist yet, say so.
- **Still em-dash-free**, and lint every draft. Personality is the opposite of AI-slop, not a licence
  for it — the mechanical tells (em-dashes, "not just X but Y", balanced triads, participle tails)
  still have to be zero.

## Output format

Deliver the caption ready to paste (first line, body, CTA lines). Keep any commentary short and after
the caption — e.g. flag the CTA choice, or note if the promised freebie needs building. Don't wrap the
caption in extra headers Fraser would have to delete.

## Anti-pattern (what to avoid)

Every caption opening "Save this before X 👇", then a tidy 5-point list of one-sentence points, closing
"Follow @frasercottrell … Comment HOOKS". Technically fine, reads like a machine filled a template. The
fix isn't dropping listicles — it's varying the opener, adding a credential, injecting personality, and
rotating the CTA. See `references/examples.md` for the same caption done both ways.
