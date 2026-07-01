# QA report: What are the best agentic AI use cases for mid-market firms?

Topic: Agentic AI use cases for mid-market businesses  |  Target keyword: agentic ai use cases  |  Cluster: Strategy & ROI (Listicle + ROI)  |  Format: G (Listicle + ROI)  |  Word count: ~2,160 (body, pre-tags)

## 10-element GEO checklist

1. **Definitive answer paragraph: PASS** — 71 words, sits above the first H2. Answers the headline question on its own: names the seven use cases (customer service triage, finance and operations reconciliation, sales development, IT and security monitoring, HR screening, procurement checks, internal knowledge retrieval), the common thread (high-volume, rules-heavy, human sign-off), and a specific dated figure (Gartner: over 40% of agentic projects cancelled by end of 2027).

2. **Question-format H2s: PASS** — 6 H2s, all end with question marks:
   - What counts as an agentic AI use case, not just automation?
   - Which agentic AI use cases pay back fastest?
   - How do these use cases compare on payback and risk?
   - What is the business value of agentic AI for a mid-market firm?
   - Why do so many agentic AI projects fail?
   - Which agentic AI use case should a mid-market firm start with?
   (The seven use cases are promoted to H3s under the "pay back fastest" H2, per the voice-guide rule on 3+ named sub-topics.)

3. **Comparison table: PASS** — One HTML `<table>` with `<thead>`/`<tbody>`: 7 rows (use cases) x 5 columns (Use case, Typical payback, Complexity, Human oversight needed, Main risk to manage). Every cell populated; no "TBC" or "varies". This is the strongly-recommended summary table for the listicle format.

4. **Authoritative inline citations: PASS** — 7 hyperlinked citations to primary/named sources, plus named-source attributions:
   - DSIT AI Adoption Research (gov.uk) — hyperlinked
   - Gartner 80% customer service resolution by 2029 (gartner.com) — hyperlinked
   - ICO AI and data protection guidance (ico.org.uk) — hyperlinked
   - ONS Business Insights and Conditions Survey (ons.gov.uk) — hyperlinked
   - Gartner 40% cancellation by 2027 (gartner.com) — hyperlinked
   - McKinsey economic potential of generative AI (mckinsey.com) — hyperlinked
   - Deloitte State of AI in the Enterprise 2026 (deloitte.com) — hyperlinked
   Named-source attributions (no link needed): Salesforce Agentforce production figure (vendor self-report, flagged as such); Gartner ~130 genuine vendors. All domains on the approved list (gov.uk, ons.gov.uk, ico.org.uk, gartner, mckinsey, deloitte). No agency blogs or content farms.

5. **Original UK stat: PASS (Layer 2)** — Tom & Co cross-source derivation: combining ONS BICS (44% of 250+ firms use AI, late December 2025) with DSIT AI Adoption Research (7% of AI-using firms use agentic AI, survey Feb-May 2025) gives approximately 3% of UK large/mid-market firms actually running agentic AI in mid-2025 (0.44 x 0.07 = 3.08%). Neither source published the combined figure. Cited in a blockquote as "Tom & Co analysis of ONS and DSIT data (mid-2025)". Workings recorded in sources.md and stat_bank_update.json. (Note: per batch instructions, data/stat_bank.json is NOT edited by this subagent; the central process merges stat_bank_update.json.)

6. **JSON-LD schema: PASS** — Single `<script type="application/ld+json">` block at end of content. Contains: Article schema (headline, datePublished/dateModified 2026-07-01, author Person, publisher Tom & Co, description, mainEntityOfPage), FAQPage schema (5 Q&A pairs), and Person schema for Tom McCaul with sameAs LinkedIn. No empty strings or placeholder URLs.

7. **Author byline + Person schema: PASS** — `author` field in article.json is the plain string "Tom McCaul". Body has `<h3>About the author</h3>` with named author, role (Founder), credential (15+ years digital/agency leadership), and LinkedIn link. Person schema present with name, jobTitle, worksFor, sameAs.

8. **Visible date / dateModified: PASS** — `date` field is "2026-07-01". JSON-LD Article `datePublished` and `dateModified` both "2026-07-01". No "Last reviewed:" line in body. Review-due date: 2026-09-29 (today + 90 days) for the central process to record on the roadmap.

9. **2-4 internal links: PASS** — 4 internal links in `<h3>Related Tom & Co reading</h3>`, all using `/ai-agency-consultancy/blog/{slug}`:
   - /ai-agency-consultancy/blog/what-is-agentic-ai
   - /ai-agency-consultancy/blog/what-are-ai-agents
   - /ai-agency-consultancy/blog/what-are-agentic-workflows
   - /ai-agency-consultancy/blog/risks-of-agentic-ai
   All anchor texts are descriptive noun phrases matching each destination's H1. No banned anchors ("click here", "read more").

10. **Robots.txt check: SITE-LEVEL** — One-time site-level check, not per-article. No block on this article.

---

## Voice-guide spot-check (from scripts/voice_check.py)

- **Em dash count ( — ):** 0 ✓
- **En dash sentence-break count ( – ):** 0 ✓
- **Banned word hits:** 0 ✓
- **Paragraphs over 100 words:** 0 ✓
- **Paragraphs 71-100 words:** 1 (the answer paragraph, 71 words) — this is the front-loaded definitive answer paragraph, which the voice guide explicitly exempts from the ≤70-word body target and specs at 40-80 words. All other body paragraphs are ≤70 words. WARN only, not a FAIL.
- **"We"/"our" frequency:** 0.09% ✓ (well under 1%)
- **Bolded phrases:** 4 (the four numbered starter-step leads in the final H2) ✓
- **H2s ending with ?:** 6/6 ✓

**voice_check.py result: CLEAN (0 failures)**

---

## Decision: SHIP

All 10 elements PASS (element 10 is site-level). voice_check.py CLEAN. Layer 2 original cross-source calculation produced and documented. Word count ~2,160 body, within the 1500-2200 band for a listicle. Comparison table present as proper HTML. Four sibling internal links placed. Do NOT git commit/push or push to Storyblok (central process handles publishing).
