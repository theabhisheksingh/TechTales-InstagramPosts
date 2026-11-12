# 2026-11-12 — Publishing package

**Pillar:** Technology & Architecture (Resilience)
**Headline:** The backup power was fine. It just never got the signal to start.
**Audience:** Architects, SREs, platform and engineering leaders who own availability and disaster-recovery plans

## Caption

The backup power was fine. It just never got the signal to start.

On 20 October, Google Cloud's europe-west2-b zone in London went dark. A cable fault cut the main utility feed. The second feed was already offline for maintenance. The generators should have started, but the control logic read a sensor wired upstream of the open breaker and concluded that power was healthy. The UPS batteries ran out after about five minutes, and the zone lost power. Most services took around six hours to recover.

Every component worked. The combination had never been exercised: one feed already down, the other failing.

Then a second-order effect: workloads failed over to the other two London zones at once, and that surge, plus cross-zone control-plane dependencies, spread the impact further.

What to take into your own systems:
1. Test failover in degraded states, not only on a clean day.
2. Check what your detector actually sees. "Healthy" can be measured from the wrong place.
3. Size the surviving zones for peak load, not average.
4. Make sure your recovery path does not depend on the thing that failed.

Redundancy you have not exercised is an assumption.

When did you last test failover while something else was already broken?

Follow @techtaleswithabhi for delivery, architecture and AI, without the hype.

#softwarearchitecture #sitereliabilityengineering #sre #cloudcomputing #googlecloud #disasterrecovery #resilience #devops #incidentmanagement

## Alt text (per slide)

1. Dark slide headline: The backup power was fine. It just never got the signal to start. Subtitle: what Google Cloud's London outage teaches about failover you have never really tested.
2. Timeline for 20 Oct 2026, europe-west2-b, London, in UK time: 07:00 a cable fault cuts the main utility feed; the second feed is already offline for maintenance; generators do not start; after about 5 minutes UPS batteries run out; about 6 hours until most services recover.
3. Failure-chain diagram: utility feed A fails; control logic reads a sensor upstream of the open breaker and sees power as healthy; generators never auto-start; UPS drains and the zone goes dark. Simplified from Google's incident report.
4. Every part worked; the combination had never been tried. A failover not tested in that state is a hypothesis, not a plan.
5. Losing one zone stressed the other two: simultaneous failover demand and cross-zone control-plane dependencies widened the impact. Questions: can surviving zones absorb the full load, and does anything needed for recovery live only in the failed zone?
6. Four practices: test in degraded states; check what the detector sees; size for N minus 1 at peak load; map recovery dependencies.
7. Takeaways: unexercised redundancy is an assumption; the riskiest moment is during maintenance; plan for the failover load, not just the failure.
8. Question: When did you last test failover while something else was already broken? Plus save and follow prompts.

## Sources

- Google Cloud incident report, europe-west2 (incident began 2026-10-19 23:00 US/Pacific = 20 Oct 07:00 UK; main impact 6h 8m; root cause: utility cable fault on feed A, feed B open for maintenance, PLC undervoltage sensing wired upstream of the feed B breaker so generators did not auto-start, UPS runtime about 5 minutes; contributing: failover demand surge in zones a and c, cross-zone control-plane dependencies): https://status.cloud.google.com/incidents/Xs2XTHzAVC9YnafnPyzj
- ITPro, "The Google Cloud outage explained" (21 Oct 2026): https://www.itpro.com/infrastructure/the-google-cloud-outage-explained-what-happened-who-was-affected-and-what-can-we-learn-from-the-incident
- Before publishing: re-check the incident page for a final post-mortem; Google listed remediation items due 13–17 Nov 2026.
- Slides 4–7 are practical analysis, not claims from Google.
