---
name: session-close
type: ceremony
trigger: ending a work session
cadence: every session
depends: none
references: P1 (Continuity Over Capability), P3 (Entropy Is the Default), P6 (Feedback Over Prescription)
---

# Session Close

Reflect on the session, update state for continuity, and ensure clean handoff.

## Steps

1. **Review what was accomplished**
   - Check version control history for commits since session start.
   - Review today's log for work recorded during the session.
   - Summarise: what got done, what didn't, what changed.

2. **Retro with operator**
   Present three prompts for collaborative reflection:
   - **Keep doing:** What worked well this session?
   - **Stop doing:** What wasted time or caused friction?
   - **Start doing:** What was missing or would help next time?

   This is collaborative — present observations, then discuss with operator.

3. **Classify session items**
   Tag each piece of work from the session:
   - **bug** — something broke, was fixed or needs fixing
   - **build** — new capability or feature
   - **protect** — working feature that needs tests or documentation
   - **refactor** — restructured, no behavior change
   - **chore** — maintenance, cleanup, dependency updates

4. **Extract prioritised actions**
   - **Now** — carry into checkpoint as active
   - **Next** — queue for upcoming sessions
   - **Later** — backlog, revisit eventually
   - **Bring forward:** re-read previous checkpoint actions. Unfinished items get re-evaluated — re-prioritise, keep, or drop. Nothing silently disappears.

5. **Update checkpoint**
   - Write `state/flow/checkpoint.md` with current Active, Next, and Later.
   - Update "Last updated" date.
   - Carry forward unfinished items explicitly.

6. **Update goals if needed**
   - If standing goals changed or weekly goals shifted, update `state/flow/goals.md`.

7. **Capture lessons**
   - If something was learned that has lasting value, write it to `docs/decisions/`.
   - Lessons that repeat across sessions are candidates for ceremony or principle amendments.

8. **Append to today's log**
   - Add session end entry with:
     - What was accomplished
     - Retro findings (keep/stop/start)
     - Classified items
     - Actions extracted
     - Any decisions made

9. **Commit state**
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

Lessons: [any captured]
```

## Notes

- The retro is not optional. Even a 30-second retro ("nothing to change") forces the reflection habit.
- Apply retro changes immediately where possible — update a skill, adjust a ceremony, note a pattern. Don't defer what can be done now.
- The checkpoint is the save point. Write it as if the next session starts with a different agent that has never seen this workspace before.
