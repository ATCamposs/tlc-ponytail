#!/usr/bin/env python3
"""PostToolUse(Skill): when tlc-spec-lean/driven loads, remind the model to load grill-me."""
import json
import re
import sys

PATTERN = re.compile(r"(^|:)tlc-spec-(lean|driven)$")

MESSAGE = (
    "tlc-spec-* loaded: before deciding anything in the plan, load the tlc-ponytail `grill-me` skill "
    "(unless it is already in context). Every gap - gray area, assumption, ambiguous term, "
    "contradiction with the code - becomes a round of questions with a recommendation; no assumption "
    "passes unasked (hooks/tlc-plan.md)."
)


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except ValueError:
        return 0
    skill = str((data.get("tool_input") or {}).get("skill", "")).strip()
    if PATTERN.search(skill):
        print(json.dumps({"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": MESSAGE}}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
