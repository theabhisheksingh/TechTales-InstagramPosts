# 2026-11-22 — Publishing package

**Pillar:** Technology & Architecture
**Headline:** Your client will retry. Make sure your API only charges once.
**Audience:** Architects, senior engineers, engineering managers and TPMs who design or review APIs, payment flows and event-driven systems

## Caption

Your client will retry. Make sure your API only charges once.

A client waits 30 seconds, gives up, and retries. From its side there is no way to know what happened on the server: the request never arrived, it succeeded and the response was lost, or it is still running. Retrying is the only sensible move, and in the second case a naive retry charges the customer twice.

The fix is idempotency: doing something twice has the same effect as doing it once. Reading a record is naturally idempotent, and so is "set status to shipped". "Create a charge" is not, unless the API can recognise a repeat. Networks deliver at least once; make the handler idempotent and the business outcome happens exactly once.

The usual mechanism is an idempotency key. The client sends a key with the request. The server performs the work once and saves the key with the response. When a retry arrives with the same key, it skips the work and returns the saved response. Two requests, one charge. The key identifies the intent, not the attempt.

Stripe's API is a well-documented example: it accepts an Idempotency-Key header on POST requests, and in its v1 API a retry with the same key returns the saved first response (even an error), a reused key with different parameters is rejected, and keys can be pruned once they are at least 24 hours old.

Building it into your own API: the client creates one key per user action and reuses it on every retry; store the key, a request hash and the result in the same transaction as the side effect; return a conflict when the same key is still in flight; keep keys longer than any client, queue or webhook will retry. Avoid three mistakes: a new key per attempt, check-then-write races, and protecting only the API while queue consumers and webhooks redeliver too.

Which operation in your system would hurt most if it ran twice?

Follow @techtaleswithabhi for delivery, architecture and AI, without the hype.

#softwarearchitecture #systemdesign #apidesign #distributedsystems #backendengineering #idempotency #engineeringleadership #tpm #payments

## Alt text (per slide)

1. Dark slide headline: Your client will retry. Make sure your API only charges once. Subtitle: retries are not an edge case, they are how distributed systems survive; duplicates are what happens when nobody designed for them.
2. A timeout is not an answer. The client waited 30 seconds, then gave up. From the client's side there is no way to know what happened: A, the request never arrived; B, it succeeded and the response was lost; C, it is still running. The only sensible move is to retry, and in case B a naive retry charges the customer twice.
3. Idempotent: doing it twice has the same effect as doing it once. Reading a record is naturally idempotent, and so is setting status to shipped. Creating a charge is not, unless the API can recognise a repeat. Networks deliver at least once; make the handler idempotent and the business outcome happens exactly once.
4. Sequence diagram, the idempotency key, between Client and API: the client sends POST /charges with key a1f9; the API charges once and saves the key and response together; the response is lost to a timeout; the client retries with the same key a1f9; the API sees the key, skips the work and returns the saved response; the client receives 200 with the same charge id. Note: two requests, one charge; the key identifies the intent, not the attempt.
5. Real-world example, Stripe's API: Stripe accepts an Idempotency-Key header on POST requests. In its v1 API, a retry with the same key gets the saved first response, even if that was an error; reusing a key with different parameters is rejected; keys can be pruned after 24 hours, after which the same key is a new request. Source: docs.stripe.com/api/idempotent_requests.
6. Building it into your own API: 01 the client creates the key once per user action and reuses it on every retry; 02 save atomically, key, request hash and result in the same transaction as the side effect; 03 handle in-flight repeats, return a conflict rather than running twice; 04 outlive the retries, keep keys longer than any client, queue or webhook will retry.
7. Three mistakes to avoid: a new key for every attempt, which makes every retry look new; check first, write later, where two parallel retries both pass the check; only protecting the API, when queue consumers and webhooks redeliver too.
8. Question: Which operation in your system would hurt most if it ran twice? A payment, an email, a stock update, a provisioning job? Plus save and follow prompts.

## Sources

- Stripe API reference, Idempotent requests (slide 5 and caption): https://docs.stripe.com/api/idempotent_requests — header name, saved status code and body for v1 retries (including 500 errors), parameter comparison that errors on mismatch, and keys removable once at least 24 hours old. Checked 2026-11-22.
- Slides 2–4, 6 and 7 are evergreen practitioner guidance; no statistics are used. The 30-second timeout, the key "a1f9" and the charge flow in the diagram are illustrative.
