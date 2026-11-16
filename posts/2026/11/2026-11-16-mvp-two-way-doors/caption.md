# 2026-11-16 — Publishing package

**Pillar:** Product & Startups
**Headline:** Your MVP doesn't need perfect architecture. It needs decisions you can undo.
**Audience:** Founders, CTOs, architects, engineering managers and TPMs shaping early-stage products

## Caption

Your MVP doesn't need perfect architecture. It needs decisions you can undo.

Early teams usually go wrong in one of two ways. Some debate everything: three weeks choosing a CI tool, a queue and a framework before a single user has signed up. Others debate nothing: the data model and the public API are decided in a hurry, and then customers build on top of them.

In Amazon's 2015 shareholder letter, Jeff Bezos separated decisions into two types. One-way doors are hard or impossible to reverse, so you slow down and think them through. Two-way doors can be walked back if you are wrong, so you decide fast with a small group.

Same sprint, two decisions (illustrative):
A background job library. Nothing outside the codebase sees it, and swapping it later is a few days of work. Pick one this afternoon.
A webhook payload format. The day a customer integrates, it becomes their code too. Version it from day one and review it properly.

Three questions before you decide:
1. Who builds on it? If customers, partners or stored data depend on it, treat it as one-way.
2. What would undoing cost? Estimate it in weeks, not feelings.
3. Can we add a seam? An interface or adapter can turn a one-way door into a two-way one.

Speed in an MVP comes from deciding reversible things quickly, not from deciding everything quickly. Spend your design time where customers and data will lock you in, and write down which doors you treated as one-way, and why.

Which early decision turned out to be a one-way door for you?

Follow @techtaleswithabhi for delivery, architecture and AI, without the hype.

#mvp #softwarearchitecture #startups #productdevelopment #systemdesign #cto #engineeringleadership #decisionmaking #saas

## Alt text (per slide)

1. Dark slide headline: Your MVP doesn't need perfect architecture. It needs decisions you can undo. Subtitle: how to tell which early choices deserve a week of thought and which deserve an hour.
2. Teams treat every decision the same: some debate everything, spending weeks on a CI tool, queue or framework before any users; some debate nothing, rushing the data model and public API that customers then build on.
3. One-way doors and two-way doors: in Amazon's 2015 shareholder letter, Jeff Bezos separated decisions into two types. One-way doors are hard or impossible to reverse, so slow down. Two-way doors can be walked back, so decide fast with a small group.
4. Diagram sorting decisions by cost to undo, increasing downward: two-way, decide in hours (CI/CD tool, UI component library, internal service names); costly, add a seam (auth provider, cloud-specific services); one-way, decide in days (core data model, public API and webhooks). Illustrative placement.
5. Illustrative example, same sprint, two decisions: a background job library nobody outside the codebase sees, pick one this afternoon; a webhook payload format that becomes customers' code once they integrate, version it from day one and review it properly.
6. Three questions before you decide: who builds on it; what would undoing cost, estimated in weeks; can we add a seam such as an interface or adapter to make it reversible.
7. Remember this: MVP speed comes from deciding reversible things quickly, not everything quickly; spend design time where customers and data lock you in; write down which doors you treated as one-way and why.
8. Question: Which early decision turned out to be a one-way door? The one you wish you had spent another week on. Plus save and follow prompts.

## Sources

- One-way / two-way door (Type 1 / Type 2) decisions: Jeff Bezos, Amazon 2015 Letter to Shareholders (published April 2016) — https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm. Paraphrased, not quoted. The primary page could not be fetched during this run; the attribution was cross-checked against secondary coverage, e.g. https://www.gurufocus.com/news/681732 and https://medium.com/@dannywen/on-decision-making-3e045c09b173.
- Otherwise evergreen product and architecture practice; no statistics are used.
- Slide 4 placement of decisions is illustrative and context-dependent.
- Slide 5 example is illustrative, not a real project.
