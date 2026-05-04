# /behold:init

Scaffold a `.behold/` governance directory in the current project.

## What it creates

```
.behold/
├── principles.md       # Your bedrock — why you do things this way
├── methods.md          # How you work — development process, ceremonies
├── golden-suite.jsonl  # Behavioral assertions (starts empty)
└── session-count       # Session counter (starts at 0)
```

## Instructions

When the user runs `/behold:init`:

1. Check if `.behold/` already exists. If so, report what's there and ask before overwriting.
2. Create the directory structure above.
3. Write `principles.md` with this starter content:

```markdown
# Principles

Write your team's non-negotiable rules here. These are the WHY behind your process.

Examples to consider:
- Evidence before claims (verify outputs, not self-reports)
- Function over art (will this change behavior? if not, skip it)
- Fix root causes, not symptoms
- Small and reviewable (keep changes focused)

Delete these examples and write your own. 3-7 principles is the sweet spot.
```

4. Write `methods.md` with this starter content:

```markdown
# Methods

How you work. Process rules that encode your principles into action.

Examples to consider:
- Brainstorm before building
- TDD when behavior matters
- Verify before claiming done
- Review before merging

Delete these examples and write your own.
```

5. Create empty `golden-suite.jsonl` and `session-count` (containing "0").
6. Report what was created and suggest next steps:
   - "Write your principles — the rules your agent must follow"
   - "After 2-3 sessions, propose golden suite assertions from corrections"
   - "Use /behold:golden to manage assertions over time"
