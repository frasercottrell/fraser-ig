---
name: scriptwriting
description: Write ad scripts that sound spoken, not written, by adapting proven reference ads into the brand's own voice fingerprint. AI cannot write good scripts cold — references are the default input and the brand script-voice profile is the sound. Every script passes the spoken-script-voice AI-tells check and read-aloud test. Net-new from scratch is the rare fallback.
triggers:
  - write me a script
  - write a script for this ad
  - new script ideas
  - script for this brand
  - adapt this script
  - adapt this ad
  - recreate this script
  - VSL script
  - long-form script
  - 30-second script
  - 60-second script
  - story-arc script
  - problem-solution script
  - rewrite this for our brand
---

# Scriptwriting (Claude Code)

**Read `skill/scriptwriting/method.md` now, end to end, before you write anything.**
That file is the method — the flow, the output contract, the two gates, and the
hard rules. It is shared with the Codex build of this skill, so it says nothing
about how *this* harness spawns a subagent. That one detail is below. Everything
else you need is in the method.

The rest of the skill lives alongside it: `skill/scriptwriting/strategy.md` for
picking the path, and `skill/scriptwriting/processes/` for the ~25 process files
(start at `processes/INDEX.md`). Craft docs are in `creative-strategy-context/`,
routed by `creative-strategy-context/expertise-routing.md`.

## How you spawn the two gates here

The method's step 7 tells you to run both reviewers in their own context. In
Claude Code you do that with the Task tool and the two agents shipped in
`.claude/agents/`:

- **Grounding gate** — spawn the `context-grounding-review` agent.
- **Voice gate** — spawn the `creative-voice-review` agent, after grounding passes.

Both agent files are thin and point at the real definitions in
`skill/reviewers/`. Pass each one the draft, the brand root, and the pulls you
made this session, exactly as the method describes. Their returned verdicts go
into the output verbatim — you never write those blocks yourself.

A bundled Stop hook (`.claude/hooks/gate-check.py`) enforces this: a script-shaped
message that ships without both receipts gets blocked and sent back.
