# CLAUDE.md — Telecom Gateway Specifications & Integration Docs
**Project Scope (Field Guide)**: Business Operations  
**Master Briefing Reference**: `/home/aria/projects/CLAUDE_PRIME.md`  
**Temporal Baseline**: October 2026 ($1 USD = 280,000 Tomans)  
**Operator**: Ariya Sarrafzadeh (HaroSS)

---

## 01 / STANDING BRIEF (PROJECT INSTRUCTIONS)
* **Outcome**: Standardized OpenAPI/Swagger specifications, Postman collections, and integration guides for carrier gateway.
* **Audience**: External carrier partners, enterprise integration teams.
* **References**: openapi.yaml, collections/, docs/
* **Style**: Precise technical documentation, clear request/response schemas, error code dictionaries.
* **Done means**: openapi.yaml validates with zero lint errors; all sample payloads match API responses.
* **Missing inputs**: Verify status codes and error payloads against actual gateway behavior.
* **Ask before**: Modifying published endpoint paths or parameter definitions.
* **Coordination**: Review documentation diffs before publishing.

---

## 02 / STRICT OPERATIONAL GUARDRAILS (ZERO EXCEPTIONS)
1. **Strict ADHD Versioning (Never Overwrite)**:
   - Never overwrite existing working files, layouts, or build scripts in place.
   - Increment explicitly: `name_v1.ext` -> `name_v2.ext`.
2. **Minimal Code Discipline (YAGNI)**:
   - Shortest correct diff. No unsolicited refactors, no speculative abstractions, no added dependencies without prompt.
3. **Evidence Before Assertion**:
   - Never declare that code works or passes without running verification commands and observing clean output.
   - Verification command for this project: `npx @stoplight/spectral-cli lint openapi.yaml 2>/dev/null || true`.
4. **DEAD INITIATIVE BAN (n8n is DEAD)**:
   - n8n is completely ABANDONED. Never propose, discuss, build, or reference n8n workflows.
5. **Zero Plaintext Secrets**:
   - Never commit, push, or log credentials, private keys, or API tokens.

---

## 03 / RUNNING THE WORK (STEERING TOOLKIT)
- `PLAN FIRST`: Outline tasks and wait for operator approval before touching code.
- `START NOW`: Begin work using the stated scope immediately.
- `LIMIT PARALLEL WORK`: Favor at most two active threads.
- `REDUCE UPDATES`: Report completed work and blockers only.
- `CHECK STATUS`: List active threads, their results, and next steps.
- `KEEP IT SIMPLE`: Solve directly in the active thread; avoid spawning unnecessary subprocesses.
- `CONTINUE THE RIGHT TASK`: Reuse the existing thread for direct follow-ups.
- `REVIEW BEFORE CHANGES`: Describe proposed diffs before applying edits.
