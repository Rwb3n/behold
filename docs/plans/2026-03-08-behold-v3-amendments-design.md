# Behold v3 Amendments Design

**Date:** 2026-03-08
**Status:** Approved
**Scope:** Five amendments to SPEC.md + starter kit, driven by convergent patterns across three workspaces (infrastructure-ops, dev-lab, callsheet).

## Context

The Sovereign workspace (infrastructure-ops origin) adopted Behold formally. During the migration, several patterns surfaced that Behold's spec doesn't capture but that all three origin workspaces converged on independently. These amendments push those patterns upstream.

### Evidence Base

| Pattern | Infrastructure-ops | Dev-lab (VM 104) | Callsheet |
|---|---|---|---|
| Unified work queue | retro → backlog → done | sprint → backlog → done | retro → open-actions → done |
| External inbox | Pinocchio escalations | autonomous layer inbox | N/A (no autonomous agents yet) |
| Standalone retro | per-session | per-sprint | per-work-item, per-slice, per-arc |
| Shelf-level tracking | epics.md | sprint docs | chapters/arcs/slices |
| Parked vs active backlog | parked.md vs backlog.md | implicit | implicit (backlog epics vs active) |

---

## Amendment 1: Backlog as Unified Work Queue

### What changes

**SPEC.md Section 4 (State Architecture):**
- Add `backlog.md` to the `state/flow/` directory layout
- Define: unified queue of open work items, fed by retros, sessions, ad-hoc decisions, memory observations, inbox triage
- Distinct from checkpoint (view of what's active now) and from logs (historical record)

**SPEC.md Section 7 (Feedback and Self-Amendment):**
- Update Action Register Lifecycle: backlog subsumes the action register as the default pattern
- New lifecycle: `observation → action → backlog (open) → active (checkpoint) → done`
- Note: workspaces that prefer a separate `open-actions.md` register may still use one. The lifecycle pattern is prescribed; the file structure is recommended. Backlog is the simpler default.
- Remove `open-actions.md` as the primary recommendation; keep as alternative

**SPEC.md Section 5 (Ceremony Catalogue):**
- Session Open: add "scan backlog for open items" step
- Session Close: actions from retro write to backlog

**Starter kit:**
- Add `state/flow/backlog.md` template:

```markdown
# Backlog

*Unified queue of open work items. Fed by retros, sessions, memories, inbox triage.*

## Open

| # | Item | Source | Priority | Status |
|---|------|--------|----------|--------|

## Done

*Completed items. Audit trail, not active work.*
```

---

## Amendment 2: Inbox Redefined

### What changes

**SPEC.md Section 4 (State Architecture):**
- Add explicit definition of inbox: an *external input channel* for items arriving from outside the current session
- Examples: autonomous agent escalations, inter-agent messages, background process outputs, operator notes left between sessions
- Inbox is NOT a triage staging area for internally-generated work (that goes directly to backlog)
- Session-open scans inbox; items get triaged to backlog or dismissed

**SPEC.md Section 9 (Autonomous Layer):**
- Tighten the inbox reference: autonomous layer escalates to `inbox/`, interactive agent triages from `inbox/` to `backlog` during session-open

**Starter kit:**
- Add `state/flow/inbox/.gitkeep` (directory already exists in starter, just ensure it's present)

---

## Amendment 3: Retro as Standalone Skill

### What changes

**SPEC.md Section 5 (Ceremony Catalogue):**
- Session Close step 2 changes from inline retro to "invoke retro skill"
- Add retro to the skill catalogue as a recommended skill (not a required ceremony — it's invoked by session-close and ad-hoc, not on its own cadence)

**SPEC.md Section 6 (Skills and Tools):**
- Add retro as an example of a workflow-type skill that can be invoked at multiple scopes (session, feature, milestone, ad-hoc)

**Starter kit:**
- Add `skills/retro/SKILL.md` with three-layer structure:

```yaml
name: retro
type: workflow
trigger: end of session (invoked by session-close), or ad-hoc
depends: none
provenance: inline keep/stop/start retros produce shallow feedback; the 3-layer structure (reflection, classification, action register) produces actionable items with explicit lifecycle
```

Three layers:
1. **Reflection** — keep/stop/start + "what surprised you" + "what went well" + "could have gone better" + skill amendment detection ("if a start/stop describes a repeatable ceremony failure, name the skill that should change")
2. **Classification** — every item from reflection classified into exactly one bucket: bug (broken, fix it), feature (working, protect it), feature request (missing, build it), refactor (functional but poorly structured), upgrade (functional but capped)
3. **Action Register** — one row per actionable item from classification. Columns: #, Item, Priority (now/next/later), Status (open/done), Owner, Definition of Done. Pre-satisfaction check: before writing each action, check if the Definition of Done is already met. Actions with status `open` are appended to `state/flow/backlog.md`.

Output written to `state/flow/log/` alongside session logs.

**Update `skills/session-close/SKILL.md`:**
- Replace inline retro steps (current steps 2-5) with: "Invoke retro skill. If session was trivial, note 'lightweight session — retro skipped.'"

---

## Amendment 4: Shelf-Level Tracking Pattern

### What changes

**SPEC.md Section 4 (State Architecture), under "The Checkpoint":**
- Add paragraph: "When a workspace matures and checkpoint's Active/Next/Later cannot hold enough work detail, create shelf-level tracking documents. Checkpoint points to them with references. The tracking taxonomy is workspace-specific — epics, sprints, arcs, chapters, or any structure that fits the domain. Behold does not prescribe the vocabulary; it prescribes the tier separation. Detailed tracking is shelf-frequency (changes weekly), not flow-frequency (changes every session)."

**Starter kit:**
- No change. This is a documented pattern for mature workspaces, not something the starter scaffolds. P4 (Earn Complexity).

---

## Amendment 5: Parked Pattern

### What changes

**SPEC.md Section 4 (State Architecture):**
- Add a "Common Patterns" subsection after State Hygiene Rules
- Include parked pattern: "Workspaces with significant idea volume may distinguish between the active work queue (`state/flow/backlog.md` — items that will be worked on) and a parking lot (`state/shelf/parked.md` — ideas deliberately deferred, someday/maybe items). The distinction maps to tier frequency: the backlog changes every session (flow), the parking lot changes monthly at most (shelf)."

**Starter kit:**
- No change. Optional pattern, earned when volume justifies it.

---

## Summary of File Changes

### SPEC.md edits:

| Section | Change |
|---|---|
| 4. State Architecture — directory layout | Add `backlog.md` to flow |
| 4. State Architecture — after checkpoint | Add shelf-level tracking paragraph |
| 4. State Architecture — new "Common Patterns" subsection | Inbox definition, parked pattern |
| 5. Ceremony Catalogue — Session Open | Add backlog scan step |
| 5. Ceremony Catalogue — Session Close | Replace inline retro with skill invocation |
| 6. Skills and Tools | Mention retro as workflow-type example |
| 7. Feedback — Action Register Lifecycle | Backlog as default, open-actions.md as alternative |
| 9. Autonomous Layer | Tighten inbox reference |

### Starter kit additions:

| File | Action |
|---|---|
| `starter/state/flow/backlog.md` | New — template |
| `starter/skills/retro/SKILL.md` | New — 3-layer retro skill |
| `starter/skills/session-close/SKILL.md` | Update — invoke retro instead of inline |
| `starter/skills/session-open/SKILL.md` | Update — add backlog scan step |
| `starter/state/flow/inbox/.gitkeep` | Ensure exists |

### Examples:
- No example changes in this amendment. Examples can be updated in a follow-up if needed.

---

## Impact Assessment

- Non-breaking: no existing Behold adopter is forced to change. Backlog is additive. Retro skill is new. Inbox definition is a clarification, not a breaking change.
- The `open-actions.md` pattern from v2 is preserved as an alternative, not removed.
- Starter kit gains 2 new files (backlog template, retro skill) and 2 updated files (session-open, session-close).
