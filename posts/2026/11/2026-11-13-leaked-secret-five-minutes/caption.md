# 2026-11-13 — Publishing package

**Pillar:** AI in Engineering (Security)
**Headline:** From leaked secret to stolen data: five minutes.
**Audience:** Engineering managers, TPMs, platform/DevOps engineers and tech leads who own CI/CD and cloud identities

## Caption

From leaked secret to stolen data: five minutes.

On 5 November, Microsoft Threat Intelligence described attackers using agentic AI tooling to find and abuse exposed credentials. In one observed case, an AI agent went from scanning GitHub for client secrets to exfiltrating data from Azure Key Vault in about five minutes.

No human had to read the code, test the credential or work out what it could reach.

The uncomfortable part: deleting the file does not un-leak the secret. Git keeps history, forks keep copies, and scanners may have read it within minutes. Microsoft's guidance is to treat any credential that was ever public as compromised, even after the file is edited. The fix is rotation, not a cleanup commit.

Change the defaults, not just the habits:
→ Managed identities instead of client secrets
→ Secret scanning and push protection instead of hoping
→ Least-privilege roles per app
→ Short maximum secret lifetimes
→ Rotate everything a leaked secret could reach

And treat it as a delivery concern: push protection in the definition of done, an owner for every service identity, and a rotation you have rehearsed.

How long would it take your team to rotate a leaked production secret?

Follow @techtaleswithabhi for delivery, architecture and AI, without the hype.

#cybersecurity #devsecops #devops #cloudsecurity #azure #secretsmanagement #engineeringmanagement #aiagents #softwareengineering

## Alt text (per slide)

1. Dark slide headline: From leaked secret to stolen data: five minutes. Subtitle: attackers are using AI agents to find and abuse exposed credentials.
2. Microsoft Threat Intelligence, 5 Nov 2026: in one observed case an AI agent went from scanning GitHub for client secrets to exfiltrating data from Azure Key Vault in about five minutes.
3. Five-step chain diagram: scan public repos for secrets; find an app's client secret; sign in as that app; enumerate what it can read; pull data from Key Vault. Simplified, one observed case.
4. Deleting the file does not un-leak the secret. Treat any credential that was ever public as compromised; the fix is rotation.
5. Two-column table, instead of and move to: client secrets to managed identities; hoping to secret scanning and push protection; broad permissions to least privilege; long-lived secrets to short lifetimes; editing the file to rotating everything it could reach.
6. For delivery leads: add push protection to the definition of done, name an owner for every service identity, rehearse a rotation.
7. Takeaways: leak-to-breach is now minutes; a public secret is compromised, rotate it; use managed identities so the secret never exists.
8. Question: How long would it take your team to rotate a leaked production secret? Plus share and follow prompts.

## Sources

- Microsoft Security Blog, "Threat actors use agentic AI tooling to find and abuse exposed secrets" (5 Nov 2026): https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/
- The five-minute figure is a single observed case, as stated by Microsoft. The step-by-step chain on slide 3 is a simplification; the "enumerate" step is our summary of the attack flow.
- Slide 6 is practical delivery advice, not from Microsoft.
