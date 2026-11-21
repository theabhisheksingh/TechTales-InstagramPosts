# 2026-11-21 — Publishing package

**Pillar:** Product & Startups
**Headline:** Say yes to the customer. Say no to the fork.
**Audience:** Founders, product managers, TPMs, engineering managers and architects building early-stage B2B SaaS

## Caption

Say yes to the customer. Say no to the fork.

Your largest prospect wants a different approval flow. Sales has a quarter-end deadline. Someone suggests a branch, or an if-statement on their customer ID. It ships. Then the next customer asks for their version, and a year later every release is tested several ways and nobody can say which behaviour is the product.

Customization is a cost: it changes the product for one customer, and you carry that code in every release for as long as they stay. Configuration is a product: a capability any customer can switch on, one code path with many behaviours. The test is simple: would a second customer ever want this switch?

Use the request ladder and climb only as far as the problem needs: 01 already possible (show them how), 02 configuration (a per-customer setting with a safe default), 03 extension point (API, webhook or custom field), 04 roadmap feature (build it once, for everyone), 05 fork (last resort, priced as services). Most requests should stop at 02 or 03.

Illustrative example: "invoices above a set amount need CFO sign-off." Answer A hard-codes it for one customer and ships fast, and every release now carries a customer-only path to test. Answer B builds approval rules per account (threshold plus approver role), takes a little longer, and the next customers set it up themselves.

Before you say yes, ask: what problem sits behind the request? Who else has it (check support tickets and lost deals)? Can it be a setting with a default that changes nothing for everyone else? And if it must be custom, who maintains it, for how long, and who pays?

What's the most expensive "just this once" your product ever shipped?

Follow @techtaleswithabhi for delivery, architecture and AI, without the hype.

#saas #productmanagement #startups #softwarearchitecture #b2bsaas #founders #tpm #engineeringleadership #productstrategy

## Alt text (per slide)

1. Dark slide headline: Say yes to the customer. Say no to the fork. Subtitle: in early SaaS, every custom build feels like revenue; most become a second product you maintain for one customer.
2. The big logo: "We'll sign, if it works our way." The largest prospect wants a different approval flow, sales has a deadline, and someone suggests a branch or an if on their customer ID. It ships, the next customer asks for their version, and a year later nobody can say which behaviour is the product.
3. Customization is a cost, configuration is a product. Customization changes the product for one customer and you carry that code in every release. Configuration is a capability any customer can switch on: one code path, many behaviours. The test: would a second customer ever want this switch?
4. Diagram, the request ladder, five steps: 01 already possible, show them how it works today; 02 configuration, a per-customer setting with a safe default (highlighted); 03 extension point, API, webhook or custom field (highlighted); 04 roadmap feature, build it once for everyone; 05 fork, last resort, priced as services (dashed). Note: most requests should stop at 02 or 03; climb only as far as the problem needs.
5. Illustrative example, one request, two answers: "Invoices above a set amount need CFO sign-off before they go out." Answer A, custom: if customer equals acme, ships fast, and every release carries an Acme-only path to test. Answer B, configuration: approval rules per account, threshold plus approver role, takes a little longer, and the next customers set it up themselves.
6. Before you say yes, ask: 01 what problem sits behind it; 02 who else has it, check support tickets and lost deals; 03 can it be a setting with a default that changes nothing for everyone else; 04 if it must be custom, who maintains it, for how long, and who pays.
7. Three rules: never branch on a customer ID; ask for the problem, not the solution; if it's truly custom, price the maintenance, not just the build.
8. Question: What's the most expensive "just this once" your product ever shipped? A fork, a flag, a hard-coded customer? Plus save and follow prompts.

## Sources

- Content is evergreen practitioner guidance; no statistics, dates or named companies are used.
- The slide 2 scenario and the slide 5 CFO sign-off request ("acme") are illustrative, not from a real customer.
- The request ladder (slide 4) is a framework for this post, not an external standard.
