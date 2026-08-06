# QA report: What is MCP and how does it change enterprise AI integration?

Topic ID: 49  |  Cluster: Technical & Build  |  Priority: P1 (quick win)  |  Word count: 1864

## 10-element GEO checklist

1. Definitive answer paragraph: PASS — 63 words, sits above the first H2, names the standard, the donation/2026 date, and a concrete 15-system worked example (105 to 15 connections). Answers the headline question standalone.
2. Question-format H2s: PASS — 6 H2s, all end in `?`: "What problem does MCP actually solve for enterprise integration?", "How does MCP's architecture work under the hood?", "How does MCP compare with point-to-point APIs and iPaaS?", "How fast is enterprise MCP adoption running in 2026?", "What security and governance risks come with adopting MCP?", "What should a UK enterprise IT team do before rolling out MCP?"
3. Comparison table: PASS — one table, 3 rows (point-to-point API, iPaaS/ESB, MCP) x 5 columns (approach, integration count, where logic sits, 2026 auth model, best for). Every cell populated, no "TBC"/"varies".
4. Authoritative inline citations: PASS — 7 inline citations: anthropic.com, blog.modelcontextprotocol.io (MCP's own spec, explicitly sanctioned for the Technical & Build cluster), ons.gov.uk, techuk.org, fca.org.uk, computerweekly.com, gds.blog.gov.uk. All primary/protocol-native sources, no agency blogs. Two secondary-source claims (Gartner MCP-support projection; Linux Foundation/PR Newswire governance detail) were researched but deliberately excluded because the underlying primary source wasn't verifiable or wasn't on the approved domain list — see sources.md "Sources considered and not used".
5. Original UK stat: PASS (Layer 2) — Tom & Co worked example applying the M x N vs M + N integration-complexity formula to a stated 15-system scenario: 105 point-to-point connections vs 15 MCP connections, an 86% reduction. Appended to `stat_bank_update.json` as stat_016. Presented explicitly as an illustrative worked example (stated assumption), not as a claimed UK-wide average, per the honesty requirement in stat-sourcing.md.
6. JSON-LD schema: PASS — Article + FAQPage (4 Q&A pairs) + Person. No HowTo (format is definition/architecture, not a numbered how-to).
7. Author byline + Person schema: PASS — `author` field is the string "Tom McCaul". "About the author" H3 present with role, 15+ years credential, LinkedIn link. Person schema includes name, jobTitle, worksFor, sameAs.
8. Visible date / dateModified: PASS — article.json `date` = 2026-08-06 (today). JSON-LD `datePublished` and `dateModified` both 2026-08-06. No "Last reviewed" line in the body. Next review due: 2026-11-04 (today + 90 days, supporting article cadence) — to be recorded in the roadmap row's Notes when marked done.
9. 2-4 internal links: PASS with caveat — 3 links chosen (sibling non-technical MCP article, adjacent Technical & Build sibling, cross-cluster bridge to Strategy & ROI), plus 2 alternates listed for the injector. No pillar-hub up-link is possible because no "P5: Building with AI" pillar article has been published yet; flagged in `internal_link_suggestions.md` for Tom.
10. Robots.txt check: SITE-LEVEL, not re-verified this run — `scripts/check_robots.py` is not present in this repo checkout. Carrying forward the prior batches' assumption that this is tracked separately; flagging so Tom can confirm cadence.

## Voice-guide spot-check (from `scripts/voice_check.py`)

- Em dash count: 0/0 ✓
- En dash sentence-break count: 0/0 ✓
- Banned word hits: none
- Paragraphs over 100 words: 0
- Paragraphs 71-100 words: 2 (both under the "one per major section" guidance headroom; content genuinely needed the length)
- "We"/"our" frequency: 0.00%
- Bolded phrases: 5 (all numbered-list item leads in the final checklist, structural)
- H2s ending with ?: 6/6 ✓

**voice_check.py result: CLEAN**

## Decision: SHIP

Rationale: all 10 elements PASS or PASS-with-caveat (caveats are structural, not content quality issues — no P5 pillar page exists yet, and the site-level robots check script isn't in this checkout), the voice gate reports CLEAN, and the original Layer 2 stat is honestly derived and disclosed as a worked example.
