All of these skills are baked into our AI creative strategy tool, Parker! Use code "PARKERBRAIN" at checkout to get a free month and test it out!

Link here: https://heyparker.ai/

# Anti-AI-Slop Script Writing Skill

A drop-in skill for **Claude Code and Codex** that writes ad scripts sounding **spoken, not written** — and the craft docs and independent review agents that make it work. It's built to beat the thing every AI script does by default: clean, smooth, em-dash-cadenced copy that reads fine on the page and dies the second someone says it out loud.

This is a standalone slice of the Parker marketing-intelligence brain, extracted so anyone can copy it into their own setup and use it.

## What it actually does

The skill enforces one belief: **AI cannot write a good script cold.** Left to invent from scratch, it produces plausible, tell-ridden ad copy. So the default flow is **reference-driven adaptation** — find a proven ad, keep its structural skeleton, and rewrite every word in the brand's own voice. Net-new from scratch is the rare fallback, and even then it's held to the same voice doctrine.

The AI-tells doctrine — no em-dash cadence, no smooth triplets, no "it's not just X, it's Y," no rhetorical self-questions, no throat-clearing openers, no abstractions where a real named thing belongs, and the mess *kept in* (the placed "so," "honestly," the false start, the repeated word) — lives in [`creative-strategy-context/spoken-script-voice.md`](creative-strategy-context/spoken-script-voice.md) and [`creative-strategy-context/ai-writing-tells.md`](creative-strategy-context/ai-writing-tells.md). Those two docs are the heart of the whole thing.

## The review gates — why this isn't just a prompt

The important part: **the skill doesn't grade its own paper.** Before any script reaches you, it automatically spawns two *independent* reviewer agents — running in their own context, having not written the draft — and both have to pass. This is the difference between a skill that *says* "avoid AI tells" and one that actually catches them.

- **Grounding gate** (`skill/reviewers/context-grounding-review.md`) — an independent strategist that re-reads the method docs, runs `scripts/grounding-check.py`, and verifies the script was built from real context: no fabricated facts, numbers and specs trace to a source, the methods were applied not just cited. Returns `grounded` or `bounced`.
- **Voice gate** (`skill/reviewers/creative-voice-review.md`) — an independent reader that runs the mechanical linter `scripts/voice-lint.py` against the AI-tells doctrine, then judges every flag by ear (catching what regex can't) and rewrites in the brand's register. Returns `ships` or `flagged`.

Both run every time, on their own, before you see anything — never offered as a "want me to review it?" The script comes back with both verdicts attached. If either bounces, the skill regenerates and re-runs rather than annotating around it.

In Claude Code it's not even on the honor system: a bundled **Stop hook** (`.claude/hooks/gate-check.py`) checks every finished turn. If a script-shaped deliverable is going out without its two review verdicts, the hook blocks the turn and sends the model back to run the gates. The skill instructs; the hook enforces. Codex runs the same two gates as independent subagents, but it can't load project-local hooks, so there the contract is instruction-level — see [Codex](#codex) below.

The linters are plain Python (standard library only — nothing to install). You can run them yourself: `python3 scripts/voice-lint.py yourscript.md`.

## What's in here

The method, the process files, and the two gate definitions are **harness-neutral** and live in `skill/`. The `.claude/` and `.codex/` folders hold only thin files that point at them, plus whatever is genuinely specific to that harness.

```
skill/                         The craft, shared by both harnesses:
  scriptwriting/
    method.md                  the method — flow, output contract, gates, hard rules
    strategy.md                picking the path for a given request
    processes/                 ~25 process files (adapt-a-reference, script-from-review,
                               write-vsl, and more) — start at processes/INDEX.md
  reviewers/
    context-grounding-review.md    the grounding gate — built from the right context, nothing faked
    creative-voice-review.md       the voice gate — the independent AI-slop reviewer

.claude/                       Claude Code:
  skills/scriptwriting/SKILL.md   thin — triggers + how Claude spawns the gates
  agents/*.md                     thin — point at skill/reviewers/
  hooks/
    craft-context.py           injects the doc catalog every turn, so the craft docs load themselves
    pull-log.py                logs MCP data pulls so the grounding gate can verify them
    gate-check.py              blocks any script from shipping without both review verdicts
  settings.json                wires all three hooks in

.codex/                        Codex:
  skills/scriptwriting/SKILL.md   thin — triggers + how Codex spawns the gates

AGENTS.md                      Codex's standing instructions: the craft-catalog rule and the
                               gate contract, written down because Codex won't run the hooks

scripts/
  voice-lint.py                mechanical AI-tells linter (the voice gate runs this)
  grounding-check.py           deterministic grounding checker (the grounding gate runs this)

creative-strategy-context/     The knowledge docs the skill and the gates read:
  spoken-script-voice.md         ← the anti-AI-slop core: human-voice doctrine + AI-tells audit
  ai-writing-tells.md            ← the written-slop sign families the voice gate lints against
  scriptwriting.md               the scriptwriting craft, cold-audience principles
  adapting-scripts.md            the 1:1 reference-adaptation method (the default flow)
  visual-vocabulary-method.md    per-beat visual direction, in-play/adjacent/out-of-play
  hooks.md                       the hook format taxonomy with examples
  hook-psychology.md             the why-layer beneath hooks
  emotional-delivery-and-timing.md   the emotional landing state + buying-phase model
  customer-review-mining-method.md   pulling real customer language for the script
  organic-social-analysis.md     reading organic feeds as a strategist
  creative-strategy-fundamentals.md  the senior-strategist priors behind the idea gate
  expertise-routing.md           the router — which docs to load for a given script task

system/parker-tools.md         What the Parker MCP can pull (reference ads, reviews, etc.)
```

## Installing it

Copy this repo's `skill/`, `creative-strategy-context/`, `scripts/`, `system/`, and `AGENTS.md` into the root of the project where your ad work lives — plus `.claude/` if you use Claude Code, `.codex/` if you use Codex, or both. Then just ask:

> *write me a script for a 30-second cold-traffic ad*

The skill triggers on natural phrases — "write me a script," "adapt this ad," "VSL script," "rewrite this for our brand," and more.

Keep the folder layout intact. Everything resolves by relative path from the repo root: the thin skill files point at `skill/`, the reviewers run the linters out of `scripts/`, and the craft docs are found under `creative-strategy-context/`.

### Claude Code

Nothing to install. Drop the folders in and it's live. On every turn the bundled hook puts the craft catalog in front of the model so it loads the right docs instead of writing from memory, and the two review agents run automatically before the script comes back — with the Stop hook blocking anything that tries to skip them.

### Codex

Also nothing to install — Codex picks up `.codex/skills/scriptwriting/` from the project and reads `AGENTS.md` automatically. Verified against Codex CLI 0.145.

Two real differences worth knowing:

**The gates still run, but nothing enforces them.** Codex does not load project-local hooks — they only come from your own Codex home or an installed plugin, and either way they sit behind a one-time "these hooks need review" approval. So the Stop hook that blocks a receiptless script in Claude Code does not fire here. The skill and `AGENTS.md` both state the gate contract in hard terms, and the reviewers still run as independent subagents through Codex's `spawn_agent`, but on Codex the discipline is instruction-level. If a script ever comes back without its **Grounding Review** and **Voice Review** blocks, it skipped the gates — send it back.

**If you want the mechanical enforcement anyway,** the hooks in `.claude/hooks/` are plain Python and Codex implements the same hook contract (same event names, same `decision: block` semantics). `gate-check.py` already reads Codex's `last_assistant_message` field as well as Claude's transcript. Wiring them up means adding a `[hooks]` block to your `~/.codex/config.toml` pointing at absolute paths, then approving the hooks once when Codex prompts. That is a per-machine setup step, not something the repo can do for you — which is exactly why the contract is written into `AGENTS.md` instead.

## The Parker MCP dependency

The skill is designed to run on real evidence, not vibes — proven reference ads, actual customer language from reviews and comments, the account's current format performance. It pulls all of that through the **Parker MCP**, which connects a brand's ad account, organic socials, reviews, surveys, and the competitor ad library. [`system/parker-tools.md`](system/parker-tools.md) is the full inventory of what it can reach.

**You can still use the skill without Parker MCP** — hand it a reference ad and some real customer quotes yourself, and the voice doctrine, the adaptation method, and both review gates all still run. But the more real data it can reach, the less it runs on guesses. If a data path isn't connected, the skill is built to say so plainly rather than invent numbers.

## A couple of honest notes

- **The skill routes to sibling skills that aren't in this bundle** — hooks, headlines, iterations, AI-ad-generation, and a `self-improvement-intake` that logs a one-line trace when the grounding gate bounces. Those references degrade gracefully; the review gates and the hook *doctrine* (`hooks.md`, `hook-psychology.md`) are all here, so scripts still ship reviewed and get their openers right. This repo is the scriptwriting slice on purpose.
- **Scriptwriting is actively being trained.** Treat the output as a strong starting point a human should read out loud and refine, not a finished product. Adapt the docs to your brand rather than assuming they're locked.
- Some skill files reference a brand's own vault docs (a `sub-context-docs/visual-vocabulary.md`, a brand voice profile, a `strategy/` folder). Those are files you build up over time for your brand; when they don't exist yet, the skill works without them.

## License

See [LICENSE.md](LICENSE.md). PolyForm Noncommercial 1.0.0 — free to use and adapt for noncommercial purposes.
