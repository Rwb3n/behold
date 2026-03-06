# Principles

Pragmatic building principles for a dev lab.

---

## P1: Look First, Theorize Second

Check what it is before generating abstract ideas. Read before philosophizing.

**Implies:**
- Read the code before suggesting changes
- Check existing tools before building new ones
- Verify assumptions with real output

**Does not mean:**
- Never think ahead
- No architectural planning

---

## P2: Function Over Art

Will this change behavior? If not, it's art.

**Implies:**
- Every change must affect observable behavior
- No cosmetic refactors without functional reason
- Tests prove function, not appearance

**Does not mean:**
- Code can be unreadable
- No cleanup ever

---

## P3: Economy Before Building

Can existing tools do this? Use what exists.

**Implies:**
- Check for existing solutions first
- Prefer composing existing tools over building new ones
- Evaluate build vs. buy honestly

**Does not mean:**
- Never build anything
- Accept bad tools forever

---

## P4: Fix Root Causes, Not Symptoms

No band-aids. If unsure, read more code. If still stuck, ask with short options.

**Implies:**
- Investigate before patching
- Prefer deeper fixes over quick workarounds
- Ask for help with specific options, not open-ended questions

**Does not mean:**
- Never use temporary fixes in emergencies
- Perfection before progress

---

## P5: Bugs Get Tests

When fixing a bug, add a regression test.

**Implies:**
- Every bugfix comes with a test that would have caught it
- Tests run before commits
- Test failures block merges

**Does not mean:**
- 100% coverage required
- Test everything regardless of risk
