---
name: session-resume
type: ceremony
trigger: context loss mid-session (compression, restart, new conversation within the same work session)
cadence: as needed
depends: none
references: P1 (Continuity Over Capability)
provenance: required ceremony -- context loss mid-session is inevitable; warm restart prevents redundant work
---

# Session Resume

Re-orient after context loss mid-session. This is a warm restart, not a cold start.

## When This Applies

Use this when the agent loses context during an active session — due to context window compression, conversation restart, or switching to a new conversation while continuing the same work. The operator has not left. The session is still in progress.

## Key Distinction

| | Session Open | Session Resume |
|---|---|---|
| Context | Cold start, no prior knowledge | Warm restart, session was in progress |
| Bedrock | Read in full | Skip (hasn't changed in minutes) |
| Plan | Propose fresh | Don't re-propose (operator has one) |
| Load | Full state | Flow only |
| Tone | Briefing | Confirmation |

## Steps

1. **Read flow state**
   - Read `state/flow/checkpoint.md`
   - Read today's log: `state/flow/log/YYYY-MM-DD.md`
   - Do NOT re-read bedrock files.

2. **Scan recent changes**
   - Check version control history for recent commits.
   - Check file modification times for recently changed files.
   - Reconstruct what was happening immediately before context was lost.

3. **Confirm position with operator**
   - Summarise what you see: "It looks like we were working on X. Last change was Y."
   - Ask for confirmation or correction.
   - Do NOT re-propose a session plan or re-brief from scratch.

4. **Continue**
   - Once position is confirmed, resume work from where it was interrupted.

## Output

```
Resumed — [time]

I see we were working on: [reconstructed context]
Last change: [most recent commit or file modification]
Checkpoint says: [active items from checkpoint]

Continuing from where we left off. [Confirm or correct?]
```

## Notes

- Speed matters here. The operator is waiting to continue, not waiting for a full briefing.
- If the checkpoint is stale (not updated since the session began), reconstruct from version control and log entries instead.
- If you cannot reconstruct what was happening, say so plainly and ask the operator for a brief summary rather than guessing.
