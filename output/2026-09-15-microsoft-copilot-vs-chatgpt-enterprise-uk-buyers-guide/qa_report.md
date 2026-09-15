# QA report: Copilot or ChatGPT Enterprise: which is right for your UK business?

Topic ID: 48  |  Cluster: Technical & Build  |  Priority: P1  |  Word count: 2037

## 10-element GEO checklist

1. **Definitive answer paragraph**: PASS — 64 words, sits above the first H2, answers the headline question standalone, contains specific numbers (£30/user/month) and named entities (Microsoft 365, ChatGPT Enterprise).
2. **Question-format H2s**: PASS — 6/6 H2s end in `?` (within the 4-7 range for this length band). Each mirrors the topic row's likely query phrasings ("Copilot vs ChatGPT business", "Copilot UK pricing").
3. **Comparison table**: PASS — one table, 5 rows x 4 columns (Dimension, Microsoft 365 Copilot, ChatGPT Business, ChatGPT Enterprise), proper `<table>`/`<thead>`/`<tbody>` markup, every cell populated (no "TBC"/"varies"), sterling and dollar pricing with a "last checked" date row.
4. **Authoritative inline citations**: PASS — 7 distinct primary sources cited inline: ONS, GOV.UK/DBT, ICO, NCSC (all approved-domain UK regulators/statistics bodies), plus Microsoft's and OpenAI's own pricing/privacy pages (first-party vendor documentation, cited for vendor-specific pricing and data-control claims that only the vendor can authoritatively state). No agency blogs or content-farm figures were cited directly; see `sources.md` for the aggregator sources used only for triangulation.
5. **Original UK statistic**: PASS — Layer 2. New Tom & Co calculation: approximately 46,000 UK businesses with 10+ employees already run an LLM day to day (ONS 18% adoption figure applied to DBT's 2024 business population estimate). Appended to `stat_bank_update.json` as `stat_026`.
6. **JSON-LD schema**: PASS — Article, FAQPage (6 Q&A pairs matching the 6 H2s), and Person schema included. No HowTo (not a step-by-step format). All fields populated, no placeholder URLs.
7. **Author byline + Person schema**: PASS — `author` field is the string "Tom McCaul". Body has an "About the author" H3 with role, 15+ years credential, and LinkedIn link. JSON-LD Person schema matches (name, jobTitle, worksFor, sameAs).
8. **Visible date / dateModified**: PASS — `article.json` `date` field set to 2026-09-15 (today). JSON-LD `datePublished` and `dateModified` both match. No "Last reviewed" line in the body. Next review due: 2026-12-14 (today + 90 days).
9. **2-4 internal links**: PASS — 4 distinct internal destinations used: `chatgpt-vs-claude-vs-gemini-for-business` (same-pillar up-link), `what-is-mcp-model-context-protocol` (same-cluster), `ai-uk-gdpr-ico-guidance-2026` (cross-cluster, Risk/Governance/Legal), `how-much-should-a-uk-sme-budget-for-ai-in-2026` (cross-cluster, Strategy & ROI). No banned anchor text. See `internal_link_suggestions.md`.
10. **Robots.txt check**: SITE-LEVEL / NOT RE-VERIFIED THIS RUN — `scripts/check_robots.py` does not exist in this repository yet and no `output/_robots_status.txt` file is present. Flagging for Tom: the one-time site-level robots.txt check described in the skill has not yet been implemented or run. Does not block this article.

## Voice-guide spot-check

Ran `python3 scripts/voice_check.py output/2026-09-15-microsoft-copilot-vs-chatgpt-enterprise-uk-buyers-guide/article.json`:

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words (warn band): 1 (78 words, "Factor in switching cost..." — allowed under the "one 80-100 word paragraph per major section" rule)
- "We"/"our" frequency: 0.15% ✓ (well under 1%)
- Bolded phrases: 5, all structural (numbered-list item leads in the final checklist) ✓
- H2s ending with `?`: 6/6 ✓

**Script result: CLEAN**

## Decision: SHIP

Rationale: all 10 checklist elements pass or are correctly flagged as site-level/not-applicable; the mechanical voice gate returned CLEAN; the one Layer 2 original stat is honestly derived from two named ONS/DBT publications with workings disclosed, not fabricated.
