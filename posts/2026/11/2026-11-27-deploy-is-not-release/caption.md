# 2026-11-27 — Publishing package

**Pillar:** Technology & Architecture
**Headline:** Deploying code and releasing a feature are two different decisions.
**Audience:** Engineering managers, architects, TPMs, senior engineers and founders who own how changes reach production

## Caption

Deploy is a technical event. Release is a business decision.

In many teams, the moment code reaches production is the moment every user sees it. So launches wait for a quiet window, big changes pile up in one risky deploy, and when something breaks the only way back is another deploy, under pressure, with customers watching.

Separate the two. Deploy means the new code is running in production. Release means users can actually reach it. A feature flag is the runtime switch between them, changed by configuration rather than a new build. That lets you ship the code dark, turn it on for your own team, then 5% of users, then 50%, then everyone. At any step, the kill switch turns it off in seconds with no redeploy.

Flags carry their own risk. On 1 August 2012, Knight Capital deployed new trading code that reused a flag once used by functionality it had stopped using in 2003, code that was never deleted. One of eight servers missed the update. For 45 minutes that server sent unintended orders, and the firm lost more than $460 million (SEC order and press release, October 2013).

So treat every flag as debt with a due date: give it one owner and an expiry date when it is created, never reuse a flag name, make removal part of done, and test the kill switch in staging before you trust it in production. Engineering decides when code ships. Product and the business decide when users see it.

How many flags in your codebase have no owner, and when did your team last delete one?

Follow @techtaleswithabhi for delivery, architecture and AI, without the hype.

#softwarearchitecture #featureflags #devops #continuousdelivery #releasemanagement #engineeringleadership #techdebt #sre

## Alt text (per slide)

1. Dark slide headline: Deploy is a technical event. Release is a business decision. Subtitle: when one button does both, every launch is a gamble and every rollback is an emergency.
2. The coupled launch: merge, deploy, and hope. In many teams, the moment code reaches production is the moment every user sees it. So launches wait for a quiet window and big changes pile up in one risky deploy. When something breaks, the only way back is another deploy, under pressure, with customers watching.
3. Separate the two: ship the code dark, turn it on later. Deploy: the new code is running in production. Release: users can actually reach it. Feature flag: a runtime switch between the two, changed by configuration, not by a new build.
4. Diagram titled One deploy, a release in steps. A vertical sequence: Deploy, code in production with flag off; Internal, your own team uses it first; Canary 5%, watch errors and latency; Ramp 50%, compare against the old path; Release 100%, everyone has it; Clean up, delete the flag and the old code. A dashed blue line from the canary, ramp and release steps loops back to the top, labelled Kill switch: at any step, flag off in seconds, no redeploy.
5. Real-world example, Knight Capital, 1 August 2012: flags are powerful, old flags are dangerous. The debt: code unused since 2003 was never deleted. The reuse: a new feature reused the old code's flag. The deploy: one of eight servers missed the update. The cost: 45 minutes of unintended orders and a loss of more than 460 million dollars. Source: SEC order and press release, October 2013.
6. Treat every flag as debt with a due date. 01 One owner, one expiry date, set when the flag is created. 02 Never reuse a flag name; a new behaviour gets a new flag. 03 Removal is part of done; the ticket closes when the flag and old path are gone. 04 Test the kill switch in staging before you trust it in production.
7. What to remember. Two decisions: engineering decides when code ships; product and the business decide when users see it. Smaller risk: release to 5% before 100%; rollback becomes a switch, not a redeploy. Real cost: every flag is a branch in production; delete it as soon as it has done its job.
8. Question: How many flags in your codebase have no owner? And when did your team last delete one? Plus save and follow prompts.

## Sources

- SEC press release 2013-222, "SEC Charges Knight Capital With Violations of Market Access Rule" (16 October 2013): 1 August 2012 incident, first 45 minutes after market open, loss of more than $460 million, $12 million penalty. https://www.sec.gov/newsroom/press-releases/2013-222
- SEC order, Release No. 34-70694: functionality unused since 2003 and never deleted, repurposed flag, new code not copied to one of eight servers. https://www.sec.gov/litigation/admin/2013/34-70694.pdf (excerpts as quoted at https://www.jrvarma.in/blog/Y2013/Knight-Capital.html)
- The deploy/release separation, staged rollout percentages and flag hygiene rules are evergreen engineering practice; the 5% and 50% steps are illustrative, not prescribed values.
