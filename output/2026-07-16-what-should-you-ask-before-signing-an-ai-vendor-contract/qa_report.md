# QA report: What should you ask before signing an AI vendor contract?

Topic ID: 10  |  Cluster: Strategy & ROI  |  Priority: P1 (Quick win)  |  Word count: 1676

## 10-element GEO checklist

1. Definitive answer paragraph: PASS — 69 words, sits above the first H2, answers the headline question standalone, names UK GDPR Article 28, the EU AI Act, and the Data (Use and Access) Act 2025 with its 5 February 2026 in-force date.
2. Question-format H2s: PASS — 5/5 H2s end with `?`, each mirrors a real query phrasing ("AI vendor questions", "AI procurement checklist").
3. Comparison table: PASS — "How is an AI vendor contract different from a standard software contract?" table, 6 rows x 3 columns, every cell filled, no "TBC"/"varies".
4. Authoritative inline citations: PASS — 6 external citations: ico.org.uk (x3), gov.uk/Cabinet Office PPN 017, assets.publishing.service.gov.uk (Crown Commercial Service), eur-lex.europa.eu (EU AI Act official text). All primary regulator/government/official-EU-legislative sources, no agency blogs.
5. Original UK stat: PASS (Layer 2, reused) — Tom & Co's existing `stat_002` calculation (EU AI Act penalty-tier break-even, ~£420m turnover) reused and re-attributed in the "Who carries the liability" checklist item. No new calculation performed this run, so no `stat_bank_update.json` produced.
6. JSON-LD schema: PASS — Article, FAQPage (4 Q&A pairs), and Person schemas included inline at the end of `content`. No HowTo schema (format is Template/Checklist, not step-by-step how-to).
7. Author byline + Person schema: PASS — `author: "Tom McCaul"` (string) in article.json; "About the author" H3 with role, 15+ years credential, LinkedIn link; Person schema with name, jobTitle, worksFor, sameAs.
8. Visible date / dateModified: PASS — `date: "2026-07-16"` in article.json; JSON-LD `datePublished` and `dateModified` both 2026-07-16; no "Last reviewed" line in the body.
9. 2-4 internal links: PASS — 4 links in "Related Tom & Co reading": one up-link to the P1: AI strategy pillar (`how-to-build-an-ai-strategy-for-a-uk-sme`), three cross-cluster/same-cluster links with descriptive anchors matching destination H1s. No banned anchor text.
10. Robots.txt check: SITE-LEVEL — not yet run this batch (`scripts/check_robots.py` has not produced `output/_robots_status.txt`). Flagging for a site-wide check; does not block this article.

## Voice-guide spot-check

Full automated output from `scripts/voice_check.py`:

```
# Voice-guide spot-check

- Em dash count: 0 ✓
- En dash sentence-break count: 0 ✓
- Banned word hits: 0 ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words (target ≤70): 2 WARN
    [77 words] Picture a 40-person UK retailer buying a customer-service chatbot licence...
    [71 words] What changes if the tool makes decisions about people?...
- 'We'/'Our' frequency: 0.12% ✓
- Bolded phrases: 18 WARN (numbered-list item leads, structural per voice-guide.md; script does not exclude them from the raw count but they are not a FAIL)
- H2s ending with ?: 5/5 ✓

**Result: CLEAN**
```

## Decision: SHIP

Rationale: All 9 per-article checklist elements PASS (element 10 is a site-level, non-blocking check); voice gate reports CLEAN with zero failures. The two paragraph-length WARNs sit at 71 and 77 words, within the guide's allowance of one longer paragraph per major section, and the bold-count WARN reflects numbered-list item leads which the voice guide explicitly treats as structural rather than marketing emphasis.
