# 2026-11-11 — Publishing package

**Pillar:** Technology & Architecture
**Headline:** In six months, nobody will remember why you made this decision.
**Audience:** Architects, engineering managers, TPMs, tech leads and senior engineers who own long-lived systems

## Caption

In six months, nobody will remember why you made this decision.

A new engineer asks why the system uses a queue instead of a direct call. The person who decided has left. The reasoning lived in a meeting and a Slack thread.

Now the team has two bad options: keep the choice blindly, or change it blindly and rediscover the problem it was solving.

Architecture Decision Records fix this cheaply. Michael Nygard proposed the format in 2011: one short file per significant decision, with a title, a status, the context, the decision, and its consequences. It lives in the repo, next to the code.

The part most teams miss: you never rewrite an old record. When a decision changes, you write a new one and mark the old one "superseded." The history of your thinking stays readable.

Write one when a decision is expensive to reverse or confusing to someone new: database or queue choices, sync vs async, auth and tenancy models, build vs buy. Skip it for naming and lint rules. Review ADRs in pull requests, like code.

Code shows what you built. Only a record explains why.

Which decision in your system does nobody remember the reason for? Would you keep it today?

Follow @techtaleswithabhi for delivery, architecture and AI, without the hype.

#softwarearchitecture #systemdesign #architecturedecisionrecords #engineeringmanagement #techleadership #technicaldebt #softwareengineering #technicalprojectmanager

## Alt text (per slide)

1. Dark slide headline: In six months, nobody will remember why you made this decision. Subtitle: Architecture Decision Records, the cheapest architecture practice that actually works.
2. The problem: a new engineer asks why the system uses a queue instead of a direct call; nobody knows. Two bad options: blindly keep it, or blindly change it.
3. The ADR format by Michael Nygard, 2011: Title, Status, Context, Decision, Consequences, stored as markdown in the repo.
4. Diagram (illustrative): ADR-007 "Use REST between services", status superseded by 014, arrow labelled "load grew, coupling hurt" to ADR-014 "Move order events to a queue", status accepted. The old record stays.
5. Illustrative ADR 014, "Order events via a queue": context, decision to publish an OrderPlaced event, and consequences including eventual consistency, idempotent consumers and a dead-letter queue.
6. When to write an ADR: database, queue or cloud service choice; sync vs async; auth, tenancy or data-retention model; build vs buy. Not for library minor versions, naming or lint rules. Review ADRs in pull requests.
7. Three takeaways: code shows what, records explain why; write consequences honestly; short and kept beats complete and abandoned.
8. Question: Which decision in your system does nobody remember the reason for? Plus save and follow prompts.

## Sources

- Michael Nygard, "Documenting Architecture Decisions" (Cognitect blog, 15 Nov 2011): https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Martin Fowler, "Architecture Decision Record" (bliki): https://www.martinfowler.com/bliki/ArchitectureDecisionRecord.html
- Note: the content is evergreen. ADR-007, ADR-014 and the checkout/queue scenario on slides 2, 4 and 5 are illustrative, not a real system. No statistics are used.
