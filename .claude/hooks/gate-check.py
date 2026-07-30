#!/usr/bin/env python3
"""Stop hook: a script cannot ship without its two gate receipts.

The scriptwriting skill's output contract says every delivered script carries
the returned verdicts of the two independent review agents — a "Grounding
Review" block (context-grounding-review) and a "Voice Review" block
(creative-voice-review). The skill *instructs* the model to run them; this
hook *enforces* it. When the model tries to end its turn having delivered a
script-shaped message without both receipts, the turn is blocked and the
model is sent back to run the gates.

Detection is keyed to the skill's own output contract, so normal conversation
never trips it: the block only fires when the message uses the script
deliverable's markers (a "The Script" heading, or a hook + beats + CTA
structure) and is missing a receipt.

Harness-neutral by design. Codex implements the same Stop hook contract as
Claude Code and additionally supplies `last_assistant_message` on the payload,
so we prefer that field and fall back to parsing the JSONL transcript, which is
what Claude Code gives us. Note that Codex does not load project-local hooks —
wiring this up there is a manual step, documented in the README.

Fails open on any parsing error — a broken hook must never lock up the chat.
"""

import json
import re
import sys


def last_assistant_text(transcript_path):
    """Concatenated text of the final assistant message in the transcript."""
    text = None
    try:
        with open(transcript_path, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    entry = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if entry.get("type") != "assistant":
                    continue
                msg = entry.get("message") or {}
                parts = msg.get("content")
                if isinstance(parts, str):
                    text = parts
                elif isinstance(parts, list):
                    chunks = [p.get("text", "") for p in parts
                              if isinstance(p, dict) and p.get("type") == "text"]
                    if chunks:
                        text = "\n".join(chunks)
    except OSError:
        return None
    return text


def looks_like_script_delivery(text):
    """True only when the message is a script deliverable per the skill's contract."""
    # Primary marker: the output contract's own heading.
    if re.search(r"^#{1,4}\s*The Script\b", text, re.MULTILINE | re.IGNORECASE):
        return True
    # Secondary: the full script shape — a hook line plus timed beats plus a CTA.
    has_hook = re.search(r"^\s*(\*\*|#{1,4}\s*)?Hook\b", text, re.MULTILINE | re.IGNORECASE)
    has_beats = len(re.findall(r"^\s*(\*\*|#{1,4}\s*)?(Beat\s*\d|\[?\d{1,2}[:–-]\d{2})", text, re.MULTILINE)) >= 2
    has_cta = re.search(r"^\s*(\*\*|#{1,4}\s*)?CTA\b", text, re.MULTILINE)
    return bool(has_hook and has_beats and has_cta)


def has_both_receipts(text):
    return (re.search(r"Grounding Review", text, re.IGNORECASE)
            and re.search(r"Voice Review", text, re.IGNORECASE))


def main():
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0

    # If we already blocked once this turn, let the model's retry through
    # rather than looping forever.
    if payload.get("stop_hook_active"):
        return 0

    # Codex hands us the final message directly; Claude Code gives a transcript.
    text = payload.get("last_assistant_message")
    if not text:
        text = last_assistant_text(payload.get("transcript_path") or "")
    if not text:
        return 0

    if looks_like_script_delivery(text) and not has_both_receipts(text):
        print(json.dumps({
            "decision": "block",
            "reason": (
                "This message delivers a script without its gate receipts. "
                "The output contract requires both independent reviews before a "
                "script ships: spawn the grounding reviewer "
                "(skill/reviewers/context-grounding-review.md) on the draft in "
                "its own context, then the voice reviewer "
                "(skill/reviewers/creative-voice-review.md), apply what they "
                "return, and re-present the script with its '### Grounding "
                "Review' and '### Voice Review' blocks carrying the reviewers' "
                "verbatim verdicts. Do not write the verdicts yourself."
            ),
        }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
