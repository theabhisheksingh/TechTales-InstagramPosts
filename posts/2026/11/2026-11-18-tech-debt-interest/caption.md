# 2026-11-18 — Publishing package

**Pillar:** Technology & Architecture
**Headline:** Not all technical debt is worth paying. Pay the debt that charges interest.
**Audience:** Engineering managers, architects, senior engineers, TPMs and founders who decide what tech debt gets fixed

## Caption

Not all technical debt is worth paying. Pay the debt that charges interest.

Every team keeps a cleanup list: the modules engineers dislike, ranked by how ugly they are. Product sees no customer value and says "next quarter." The list grows, engineers stop raising it, and the real problem hides among the cosmetic ones.

Separate principal from interest. Principal is what it would cost to fix the code properly. Interest is the extra cost you pay every time you touch it: slower changes, more bugs, longer reviews. Ugly code that nobody changes charges almost no interest. That cost of continuing to work on not-quite-right code is what Ward Cunningham's original 1992 debt metaphor was about.

Map each debt on two axes: how painful a change is, and how often the code changes (your git history tells you). Painful and changed all the time: pay down now. Painful but rarely touched: contain it. Easy and changed often: keep it clean. Easy and rarely touched: ignore it.

Illustrative example: a legacy PDF exporter that changes twice a year can wait. A pricing rules engine that changes in most sprints and needs days of manual regression on every change cannot.

To make the case, write it in delivery terms: area, changes last quarter, extra days per change and bugs traced there, the smallest paydown that cuts the interest, and how many sprints until it pays for itself. "It's messy" loses the argument. "It costs us two days on every pricing change" usually wins it. Then pay down in slices, inside the feature work that already touches the area.

Which part of your codebase charges the most interest, and does your backlog know it?

Follow @techtaleswithabhi for delivery, architecture and AI, without the hype.

#technicaldebt #softwarearchitecture #engineeringmanagement #softwareengineering #refactoring #tpm #engineeringleadership #legacycode #softwaredelivery

## Alt text (per slide)

1. Dark slide headline: Not all technical debt is worth paying. Pay the debt that charges interest. Subtitle: how to tell the difference, and how to make the case in the language of delivery.
2. The cleanup list that never gets prioritised: every team keeps a list of modules engineers dislike, ranked by how ugly they are; product says next quarter, the list grows, and the real problem hides among the cosmetic ones.
3. Principal vs. interest. Principal: what it would cost to fix the code properly. Interest: the extra cost paid every time you touch it, such as slower changes, more bugs and longer reviews. Ugly code nobody changes charges almost no interest; Ward Cunningham's 1992 metaphor was about this cost.
4. Two-by-two diagram, Map debt on two axes. Vertical axis: pain per change. Horizontal axis: how often it changes. Painful and rarely touched: contain it. Painful and changed all the time, highlighted: pay down now. Easy and rarely touched: ignore. Easy and changed often: keep it clean. Note: change frequency comes from git history.
5. Illustrative example, three debts, one worth paying. Legacy PDF exporter, ugly and untested but changed twice a year: contain. Old admin screens, dated but simple and rarely touched: ignore. Pricing rules engine, changed in most sprints, each change needs days of manual regression and still ships bugs: pay down now.
6. Make the case in delivery terms, a template: AREA module or service; CHANGES commits or tickets last quarter; INTEREST extra days per change and bugs; FIX smallest paydown that cuts the interest; PAYBACK sprints until it pays for itself. "It's messy" loses the argument; "it costs us two days on every pricing change" usually wins it.
7. Remember this: rank debt by the interest it charges, not by how ugly it looks; interest only accrues where code changes, so let git history tell you where; pay down in slices inside the feature work that already touches the area.
8. Question: Which part of your codebase charges the most interest? And does your backlog know it, in days, not adjectives? Plus save and follow prompts.

## Sources

- Ward Cunningham, "The WyCash Portfolio Management System", OOPSLA '92 experience report (origin of the debt metaphor): https://c2.com/doc/oopsla92.html
- Martin Fowler, "Technical Debt" (principal and interest framing): https://martinfowler.com/bliki/TechnicalDebt.html
- Adam Tornhill, "Software (r)Evolution, Part 1" (hotspots: combining change frequency from version control with code complexity to prioritise): https://adamtornhill.com/articles/software-revolution/part1/index.html
- The two-by-two quadrant is an evergreen prioritisation heuristic built on these ideas; no statistics are used.
- Slide 2 scenario, slide 5 (PDF exporter, admin screens, pricing engine) and the "two days per change" line on slide 6 are illustrative, not data from a real project.
