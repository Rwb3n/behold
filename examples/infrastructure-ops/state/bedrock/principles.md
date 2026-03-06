# Principles

Adapted from Behold defaults with domain-specific additions.

---

## P1: Sovereignty Over Convenience

Own the hardware. Own the data. Accept the operational cost.

**Implies:**
- Self-hosted over SaaS when feasible
- Local storage over cloud storage
- Complexity we control over simplicity we don't

**Does not mean:**
- Reject all external services
- Build everything from scratch

---

## P2: Isolation by Default

Every service is a silo. Blast radius is contained.

**Implies:**
- One service per container or VM
- Explicit network rules between services
- No shared credentials

**Does not mean:**
- No service can talk to another
- Duplicate common infrastructure unnecessarily

---

## P3: Document Before You Forget

Capture knowledge while it's fresh. Future you is a stranger.

**Implies:**
- Session logs written same-day
- Config changes documented immediately
- Troubleshooting steps recorded even if obvious

**Does not mean:**
- Document hypotheticals
- Write essays when bullets suffice

---

## P4: Rebuild From Docs

If the docs can't rebuild it, the docs are incomplete.

**Implies:**
- Setup guides tested against fresh installs
- Rebuild guides assume total loss
- Config files versioned or documented

**Does not mean:**
- Automate everything
- No tribal knowledge ever

---

## P5: Feedback Loops Over Static Plans

The system informs itself. Lessons flow upward.

**Implies:**
- Retrospectives update ways of working
- Repeated friction triggers review
- Assets are living documents

**Does not mean:**
- Constant churn
- No stable foundation
