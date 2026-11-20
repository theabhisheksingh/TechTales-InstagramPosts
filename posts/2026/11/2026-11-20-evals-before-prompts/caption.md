# 2026-11-20 — Publishing package

**Pillar:** AI in Engineering
**Headline:** You fixed the prompt. What did you break?
**Audience:** Engineering managers, TPMs, tech leads, architects and founders shipping LLM-backed features to production

## Caption

You fixed the prompt. What did you break?

A customer complains. Someone edits the prompt, tries it on the failing case plus a few others, and it reads better. Two weeks later a different customer complains about something that used to work, and nobody can say which change broke it.

An AI feature without an eval set is a codebase without tests. An eval set is a regression suite for behaviour: a fixed set of real inputs, each with a clear definition of a good answer. You run it on every change (prompt, model version, retrieval, settings) and compare against the last accepted baseline, per criterion rather than as one total. Outputs vary from run to run, so you judge the score across the set, not any single answer.

Illustrative example: a support-reply prompt gets a warmer tone in v2. Tone improves from 38/50 to 47/50, but "refund policy stated correctly" drops from 49/50 to 41/50. Friendlier, and wrong about money eight more times. Blocked.

Start this week: take 30–50 cases from real traffic, including the ugly ones. Grade each criterion with the cheapest check that works: code checks (exact match, contains, valid JSON, length), an LLM-scored rubric you have first checked against human labels, and human review to calibrate the others and read failures. Every production bug becomes a new case. And treat a model upgrade like a dependency upgrade: run the suite first.

How does your team decide a prompt change is safe to ship?

Follow @techtaleswithabhi for delivery, architecture and AI, without the hype.

#aiengineering #llmevals #promptengineering #softwaretesting #engineeringmanagement #tpm #techlead #mlops #softwaredelivery

## Alt text (per slide)

1. Dark slide headline: You fixed the prompt. What did you break? Subtitle: an AI feature without an eval set is a codebase without tests; every change is a guess.
2. The vibe check: five examples, looks better, ship it. A customer complains, someone edits the prompt and tries a few cases. Two weeks later a different customer complains about something that used to work, and nobody can say which change broke it.
3. An eval set is a regression suite for behaviour: a fixed set of real inputs, each with a clear definition of a good answer, run on every change (prompt, model version, retrieval, temperature) and compared against the last accepted score. Outputs vary, so judge the score across the set.
4. Diagram, the change gate: Change (prompt, model, retrieval, settings) leads to Run the eval set (same real cases every time), then Compare with baseline (per criterion, not one total), which splits into No regression (ship, new baseline) or Regression (block, read failures). Note: every production bug becomes a new case; the set grows with the product.
5. Illustrative example, a support-reply prompt v1 to v2, goal a warmer tone, run against 50 past tickets. Tone meets rubric: 38/50 to 47/50. Refund policy stated correctly: 49/50 to 41/50. Ticket ID included: 50/50 both. Verdict: blocked, friendlier and wrong about money eight more times. Illustrative numbers.
6. Start this week: begin with 30 to 50 cases from real traffic, including the ugly ones, and grade each criterion with the cheapest check that works. Code: exact match, contains, valid JSON, length. Model: a rubric scored by an LLM, checked against human labels first. Human: slow and costly, used to calibrate the others and review failures.
7. Remember this: write down what good means before you tune anything; score per criterion, a better total can hide a new failure; treat a model upgrade like a dependency upgrade and run the suite first.
8. Question: How does your team decide a prompt change is safe to ship? Test set, review, or a quick look and hope? Plus save and follow prompts.

## Sources

- Anthropic, "Define success criteria and build evaluations" (test cases from real-world distributions, code-based, LLM-based and human grading): https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
- Anthropic Engineering, "Demystifying evals for AI agents": https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- OpenAI, "Evaluation best practices": https://developers.openai.com/api/docs/guides/evaluation-best-practices
- Content is evergreen; no statistics are used. The slide 2 scenario, the slide 5 v1/v2 scores and the 30–50 case starting size on slide 6 are illustrative rules of thumb, not data from a real team.
