# QA report: What is RAG (retrieval-augmented generation) in plain English?

Topic: what-is-rag-ai  |  Cluster: Technical & Build  |  Priority: batch (ad-hoc)  |  Word count: 1637 (body, target band 1500–2200)

## 10-element GEO checklist

1. **Definitive answer paragraph:** PASS — 77 words, sits above the first H2, answers "what is RAG" on its own with a concrete definition (look things up before answering, retrieve from a source you control, grounded and traceable). Contains specific detail without a hedge.
2. **Question-format H2s:** PASS — 7/7 end with "?". "What does RAG actually mean in plain English?", "How does RAG work step by step?", "Why do businesses use RAG instead of just asking the model?", "What is the difference between RAG, fine-tuning, and prompting?", "When should a UK business choose RAG?", "What are the limits and risks of RAG?", "What should a UK leader do next?". Three named sub-topics under "How does RAG work" and under "When should a UK business choose RAG" are promoted to H3 / broken to short paragraphs.
3. **Comparison table:** PASS — one HTML `<table>` with `<thead>`/`<tbody>`, 6 rows × 4 columns (Dimension / Prompt engineering / RAG / Fine-tuning). Every cell has data, no "TBC" or "varies". This is the strongly-recommended RAG vs fine-tuning vs prompting table.
4. **Authoritative inline citations:** PASS — 5 inline citations, all primary/vendor/peer-reviewed/UK-official: arxiv.org (Lewis et al. 2020), aws.amazon.com (RAG technical doc), mdpi.com (peer-reviewed Mathematics review), ons.gov.uk (BICS), ico.org.uk (AI + data protection guidance). No agency blogs.
5. **Original UK stat:** PASS — Layer 2. Tom & Co analysis derives UK AI adoption velocity of ~6.7 percentage points/year from ONS BICS 2023 vs 2025 snapshots (Recipe C, year-on-year delta). Attributed inline as "Tom & Co analysis of the ONS 2023 and 2025 figures". Workings recorded in sources.md; a suggested stat_bank.json entry is provided for the central process (this subagent does not write to the shared bank).
6. **JSON-LD schema block:** PASS — single `<script type="application/ld+json">` array at end of content with Article, FAQPage (5 Q&A pairs), and Person schema. No placeholder URLs; author and publisher populated.
7. **Author byline + Person schema:** PASS — `author` field is the string "Tom McCaul". "<h3>About the author</h3>" section names role (Founder), one credential (15+ years in digital commerce and agency leadership), and LinkedIn. Person schema includes name, jobTitle, worksFor Tom & Co, sameAs LinkedIn.
8. **Visible date / dateModified:** PASS — article.json `date` = "2026-07-01"; JSON-LD datePublished and dateModified both "2026-07-01". No "Last reviewed" line in the body. Review-due date: 2026-09-29 (today + 90 days).
9. **2–4 internal links:** PASS — 3 internal links to sibling batch articles using the exact `/ai-agency-consultancy/blog/{slug}` path: what-are-ai-agents, how-do-ai-workflows-work, what-is-agentic-ai. Anchor texts restate each destination H1 ("What are AI agents?", "How do AI workflows work?", "What is agentic AI?"). No banned anchors (no "click here"/"read more"). See internal_link_suggestions.md for the fourth alternate (what-is-an-ai-agent-orchestrator).
10. **Robots.txt check:** SITE-LEVEL — not a per-article check. Flagged once per batch by the central process (verify GPTBot, Google-Extended, PerplexityBot, ClaudeBot, CCBot, Applebot-Extended are allowed at https://www.tomandco.co.uk/robots.txt).

## Voice-guide spot-check (scripts/voice_check.py)

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71–100 words: 1 (the 77-word answer paragraph, which is intentionally dense and exempt) — all body paragraphs are ≤70
- "We"/"our" frequency: 0.00% ✓
- Bolded phrases: 0 ✓ (comparison uses a plain table, not bolded leads)
- H2s ending with ?: 7/7 ✓

**voice_check.py result: CLEAN (exit 0)**

## Decision: SHIP
Rationale: All 10 GEO elements PASS (element 10 is site-level). voice_check reports CLEAN. Body 1637 words within band, 5 primary citations, RAG vs fine-tuning vs prompting table present, Layer 2 UK stat with disclosed workings.
