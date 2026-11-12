# 2026-11-14 — Publishing package

**Pillar:** AI in Engineering (Architecture)
**Headline:** MCP no longer remembers your session. That's the point.
**Audience:** Architects, platform engineers, AI builders and engineering leaders running or evaluating MCP servers

## Caption

MCP no longer remembers your session. That's the point.

The Model Context Protocol is how AI clients discover and call tools. Until now, every connection began with an initialize handshake and lived inside a session. The 2026-07-28 spec revision removes both.

What changed:
1. No handshake and no session header. Protocol version and capabilities travel with each request.
2. Servers expose a new server/discover call.
3. Long-running tasks move out of the core into an official extension.
4. Stricter auth: clients must validate the issuer, and dynamic client registration is deprecated.

Why architects should care: without sticky sessions, a plain load balancer can spread tool calls across instances, and you can scale, restart or redeploy servers without breaking a client mid-conversation. MCP servers start to look like ordinary HTTP services.

The trade-off: state moved, and risk moved with it. Akamai's researchers point to guessable state or task IDs, tokens and PII leaking into headers and logs, long-running tasks used to burn compute, and XSS paths through UI extensions.

Before you upgrade: inventory every MCP server and its owner, make state IDs random and scoped to the caller, scrub headers in proxies and logs, and cap task duration and cost.

Are you running MCP servers in production yet, or still experimenting?

Follow @techtaleswithabhi for delivery, architecture and AI, without the hype.

#modelcontextprotocol #mcp #aiagents #softwarearchitecture #systemdesign #platformengineering #apisecurity #aiengineering

## Alt text (per slide)

1. Dark slide headline: MCP no longer remembers your session. That's the point. Subtitle: what the stateless Model Context Protocol changes for teams running agents in production.
2. Spec revision 2026-07-28: MCP lets AI clients discover and call tools; connections used to start with a handshake inside a session; the new revision removes both.
3. Before-and-after diagram: before, a client initializes, gets a session id and every call is tied to server A only. Now, each request carries version and capabilities, and any of instances A, B or C can answer. Simplified.
4. Four changes: no handshake or session header; new server/discover call; long-running tasks moved to an official extension; stricter auth with issuer validation and dynamic client registration deprecated.
5. Stateless is easier to run: no sticky sessions, plain load balancing, restart without breaking clients; MCP servers look like ordinary HTTP services.
6. State moved, risk moved with it (Akamai): guessable state or task IDs; tokens or PII leaking into headers and logs; long-running tasks used to burn compute; UI extensions opening XSS paths.
7. Before you upgrade: inventory MCP servers and owners; make state IDs random and caller-scoped; scrub headers in proxies and logs; cap task duration and cost.
8. Question: Are you running MCP servers in production yet, or still in experiments? Plus save and follow prompts.

## Sources

- MCP specification 2026-07-28, Key Changes (changes since 2025-11-25: stateless protocol, removal of initialize handshake and Mcp-Session-Id, server/discover, tasks moved to io.modelcontextprotocol/tasks extension, RFC 9207 issuer validation, Dynamic Client Registration deprecated in favour of Client ID Metadata Documents): https://modelcontextprotocol.io/specification/2026-07-28/changelog
- SecurityWeek, "New Enterprise-Ready MCP Specification Brings New Security Challenges" (26 Jun 2026): https://www.securityweek.com/new-enterprise-ready-mcp-specification-brings-new-security-challenges/
- Akamai security research on the new MCP specification: https://www.akamai.com/blog/security-research/new-mcp-specification-security-teams-must-prepare
- Slide 5 (operational benefits) and slide 7 (checklist) are our analysis. No statistics are used.
