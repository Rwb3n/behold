---
name: session-close
type: ceremony
trigger: ending a work session
cadence: every session
depends: none
references: P1 (Continuity Over Capability), P3 (Entropy Is the Default), P6 (Feedback Over Prescription)
provenance: required ceremony -- session handoff prevents context loss (P1, P3)
---

# Session Close

Reflect on the session, update state for continuity, and ensure clean handoff.

## Steps

1. **Review what was accomplished**
   - Check version control history for commits since session start.
   - Review today's log for work recorded during the session.
   - Summarise: what got done, what didn't, what changed.

2. **Invoke retro skill**
   - Run the retro skill (3-layer: reflection, classification, action register).
   - If the session was trivial, note "lightweight session -- retro skipped."

3. **Triage actions to backlog**
   - Forward actionable items from the retro to `state/flow/backlog.md` with operator review.
   - Each item gets priority (`now` / `next` / `later`) and status (`open`).
   - **Bring forward:** re-read previous checkpoint actions. Unfinished items get re-evaluated -- re-prioritise, keep, or drop. Nothing silently disappears.
   - If the workspace uses `state/flow/open-actions.md` instead, triage there.

4. **Update checkpoint**
   - Write `state/flow/checkpoint.md` with current Active, Next, and Later.
   - Update "Last updated" date.
   - Carry forward unfinished items explicitly.

5. **Update goals if needed**
   - If standing goals changed or weekly goals shifted, update `state/flow/goals.md`.

6. **Capture lessons**
   - If something was learned that has lasting value, write it to `docs/decisions/`.
   - Lessons that repeat across sessions are candidates for ceremony or principle amendments.

7. **Append to today's log**
   - Add session end entry with:
     - What was accomplished
     - Retro findings (keep/stop/start)
     - Classified items
     - Actions extracted
     - Any decisions made

8. **Commit state**
   - Stage and commit all state changes.

## Output

```
Session end — [date] [time]

Done:
- [accomplishments]

Retro:
- Keep: [what worked]
- Stop: [what didn't]
- Start: [what to add]

Items: [classified list]

Actions:
- Now: [active]
- Next: [queued]
- Later: [backlog]
- Brought forward: [re-evaluated from previous checkpoint]
Backlog: [N actions forwarded to backlog]

Lessons: [any captured]
```

## Notes

- The retro is not optional. Even a 30-second retro ("nothing to change") forces the reflection habit.
- Apply retro changes immediately where possible — update a skill, adjust a ceremony, note a pattern. Don't defer what can be done now.
- The checkpoint is the save point. Write it as if the next session starts with a different agent that has never seen this workspace before.
