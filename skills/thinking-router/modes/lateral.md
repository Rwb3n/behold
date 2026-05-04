# Lateral Thinking

Generate non-obvious hypotheses by connecting domains that don't usually touch. Fight the gravitational pull toward conventional, expected, most-likely-next-token reasoning. The value is in the surprising connection, not the safe one.

## When to use
- Exploring what a dataset *could* reveal beyond the obvious queries
- Generating investigation hypotheses before running queries
- When the conventional analysis feels complete but shallow
- When designing new playbooks (the play itself is the lateral insight)

## The Problem This Solves

LLMs default to the centroid of their training distribution — the most expected response. For data investigation, this produces: filter by status, sort by metric, show results. Competent, predictable, low-value. The high-value insights come from connecting a *human behavioral model* to a *data signal*:

- "Old owners will just stop" + "PSC has DOB" = retirement succession play
- "Aggressive acquirers need deal flow" + "same postcode, same SIC" = matchmaker play
- "Serial fraudsters recycle company structures" + "shared directors across liquidations" = phoenix play

The lateral move is always: **what would a human do in this situation, and what data signal would that leave behind?**

## Guiding questions

1. What human behaviors are invisible in the data but leave visible traces?
   - Aging → DOB in PSC, no new directors appointed
   - Fraud → same directors across multiple failed companies
   - Distress → late filings, overdue accounts, proposal to strike off
   - Ambition → rapid mortgage accumulation, recent incorporation
   - Succession failure → sole owner died, company still "Active"

2. Who benefits from a situation that the data reveals?
   - Don't just find the distressed entity. Find the *counterparty* who profits from the distress.
   - Competitor in same area. Creditor with a charge. Employee who could do an MBO. PE firm rolling up the sector.

3. What would be true if this hypothesis were correct — and can the data confirm it?
   - "Old sole owners let companies drift" → testable: do companies with elderly sole PSCs have more overdue filings?
   - "Serial operators cycle through companies" → testable: do directors of liquidated companies incorporate new ones within 12 months?

4. What's the contrarian view of what the data shows?
   - Everyone sees "Liquidation" as failure. What if it's strategic? (Asset stripping before dissolution)
   - Everyone sees "92 mortgages" as aggressive growth. What if it's distress? (Leveraging to survive)
   - Everyone ignores "Dormant" companies. What if dormancy is a holding pattern before activation?

5. What would a domain expert notice that I wouldn't?
   - An insolvency practitioner sees nominee addresses as a signal
   - A property investor sees SIC 68 + outstanding charges as a proxy for owned property
   - A journalist sees shared directors across multiple failures as a story

## Anti-patterns

- **Don't force it.** If the conventional analysis is genuinely sufficient, don't manufacture lateral connections for novelty.
- **Don't hallucinate domain knowledge.** A lateral hypothesis is a *question to test against data*, not a conclusion. "Old owners might let assets drift" is a hypothesis. "Old owners definitely abandon £2M in property" is fabrication.
- **Don't replace exploration with theory.** Generate the hypothesis, then immediately test it. A beautiful theory that doesn't survive contact with the data is worthless.

## Output structure
- Conventional analysis (what the obvious approach would produce)
- Behavioral hypothesis (what human behavior might the data be hiding)
- Data signal (what trace would that behavior leave)
- Test (how to confirm or refute with available data)
- Counterparty (who benefits if the hypothesis is correct)
