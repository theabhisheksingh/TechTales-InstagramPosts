# 2026-11-25 — Publishing package

**Pillar:** AI in Engineering
**Headline:** Approve the action, not the answer.
**Audience:** TPMs, engineering managers, architects and senior engineers putting AI agents into delivery workflows

## Caption

Approve the action, not the answer.

Reviewing everything an AI agent produces does not scale. Human-in-the-loop usually fails in one of two ways. Approve everything, and by the tenth prompt of the day people click yes without reading. Approve nothing, and an agent with production credentials acts on a vague instruction while nobody watches. Either way, no one is paying attention at the moment it matters.

Sort every tool the agent can call by two questions. Can it be undone? Who does it reach? That gives four zones: run freely (read code, draft a PR), run and notify (update a ticket), snapshot first (reset a dev database), and human approves (deploy to production, email a client, delete shared data). OWASP calls the failure mode Excessive Agency: too much functionality, permission or autonomy.

An illustrative release notes agent: it reads merged PRs and drafts notes freely, sets fix versions with a notification, and asks for approval only before emailing client stakeholders. One approval per release, not forty.

This week: list every tool your agent can call, remove what it doesn't need, place each one in a zone, and enforce the rule in the tool layer. A prompt can be ignored. A missing permission cannot. Match credentials to the zone, show the exact action in every approval (the diff, the recipient, the command), and move tools between zones based on what actually went wrong.

Which action would you never let an agent take without asking?

Follow @techtaleswithabhi for delivery, architecture and AI, without the hype.

#aiagents #engineeringleadership #softwareengineering #devops #aiengineering #tpm #engineeringmanagement #llmsecurity

## Alt text (per slide)

1. Dark slide headline: Approve the action, not the answer. Subtitle: reviewing everything an AI agent produces does not scale; gating the few actions you cannot undo does.
2. Two ways human-in-the-loop fails: too many approvals, or none at all. Approve everything: forty prompts a day, and by the tenth people click yes without reading. Approve nothing: production credentials, a vague instruction, and nobody watching. Same result: no one is paying attention at the moment it matters.
3. Two questions per tool: sort actions by cost of being wrong. Can it be undone? A draft can be deleted, a sent email cannot. Who does it reach? Your branch, or your customers. OWASP lists this as Excessive Agency: too much functionality, permission or autonomy.
4. Two-by-two diagram titled Four zones, four rules. Columns: stays with you, reaches others. Rows: undoable, permanent. Run freely: read code and logs, summarise tickets, draft a pull request. Run and notify: update a ticket, comment on a PR, post to team channel. Snapshot first: rewrite local files, reset a dev database, delete a local branch. Human approves, highlighted in blue: deploy to production, email a client, delete shared data. Note: approval effort goes where mistakes are expensive.
5. Illustrative release notes agent: one approval per release, not forty. Reads merged PRs: free. Drafts notes in a shared doc: free. Sets fix versions in the tracker: notify. Emails client stakeholders: approve. The human reviews the one thing a client will read, and nothing else.
6. Set it up this week. 01 List every tool the agent can call, including the ones nobody uses. 02 Remove what it doesn't need; the safest tool is the one that isn't there. 03 Place each one in a zone and write the rule next to it. 04 Enforce it in the tool layer; a prompt can be ignored, a missing permission cannot.
7. What makes it hold. Credentials: match keys to the zone; read-only work gets read-only access. Approvals: show the exact action, the diff, the recipient, the command, not a summary. Review: move tools between zones based on what actually went wrong, not on fear.
8. Question: Which action would you never let an agent take without asking? And which approvals have you stopped reading? Plus save and follow prompts.

## Sources

- OWASP Top 10 for LLM Applications 2025, LLM06:2025 Excessive Agency (root causes: excessive functionality, permissions and autonomy; mitigations include minimising extensions and permissions and requiring human approval for high-impact actions): https://genai.owasp.org/llmrisk/llm062025-excessive-agency/
- Otherwise evergreen practitioner guidance; no statistics are used. "Forty prompts a day", the four-zone examples and the release notes agent are illustrative.
