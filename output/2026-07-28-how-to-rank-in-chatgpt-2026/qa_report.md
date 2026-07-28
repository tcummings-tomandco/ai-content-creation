# QA report: How do you rank in ChatGPT in 2026?

Topic ID: 22  |  Cluster: Marketing & Sales  |  Priority: P1 (quick win)  |  Word count: 2251

## 10-element GEO checklist

1. Definitive answer paragraph: PASS — 58 words, sits above the first H2, names a specific figure (87% Bing-citation-match, Profound) and answers the H1 standalone.
2. Question-format H2s: PASS — 9/9 H2s end with `?` (voice_check.py confirms). Slightly above the 4-7 band for a 1500-2200 word piece but the article sits in the 2200-3000 band (near-pillar), and the how-to/5-step format template calls for an overview + 5 steps + a "how long" section + a tools section, plus one added nuance section (Google AI Overviews vs ChatGPT).
3. Comparison table: PASS — one table, 5 rows x 4 columns (Tool / What it checks / Cost / Best for), every cell populated, no "TBC" or "varies".
4. Authoritative inline citations: PASS — 8 inline citations across 7 distinct primary/named-research-firm sources: Profound (x2 URLs), OpenAI Developer Platform, Ofcom (x2 reports), British Chambers of Commerce/University of Essex, arxiv (Princeton GEO study). All domains are on the approved list (named research firm with disclosed methodology, gov-adjacent regulator, vendor's own technical docs, academic preprint, britishchambers.org.uk).
5. Original UK stat: PASS — Layer 2. Tom & Co calculation: UK visits to ChatGPT grew roughly 4.9x (about 389%) between the first eight months of 2024 and 2025, derived from two snapshot totals Ofcom published but did not itself convert into a growth multiple. Appended to `data/stat_bank.json` as stat_013.
6. JSON-LD schema: PASS — Article, HowTo (5 steps), FAQPage (4 Q&A pairs), Person, all with populated required fields, no placeholder URLs.
7. Author byline + Person schema: PASS — `author: "Tom McCaul"` string field; "About the author" H3 with role and 15-years credential; Person schema includes name, jobTitle, worksFor, sameAs LinkedIn.
8. Visible date / dateModified: PASS — `article.json` date = 2026-07-28 (today); JSON-LD `datePublished`/`dateModified` match; no "Last reviewed" line in the body.
9. 2-4 internal links: PASS — 3 distinct links (up-link to the GEO pillar's `what-is-geo-vs-seo`, cross-cluster to `chatgpt-vs-claude-vs-gemini-for-business`, up-link to `ai-roi-uk-business-2026-what-the-evidence-actually-shows`), each inline in the body and repeated in "Related Tom & Co reading". Anchor text restates each destination's H1. No banned anchor text.
10. Robots.txt check: SITE-LEVEL — not re-verified this run; last checked in a prior batch. Flagged per playbook, not a per-article blocker.

## Voice-guide spot-check (scripts/voice_check.py output)

```
- Em dash count: 0 ✓
- En dash sentence-break count: 0 ✓
- Banned word hits: 0 ✓
- Paragraphs over 100 words: 0 ✓
- Paragraphs 71-100 words (target ≤70): 0 ✓
- 'We'/'Our' frequency: 0.35% ✓
- Bolded phrases: 0 ✓
- H2s ending with ?: 9/9 ✓

Result: CLEAN
```

## Decision: SHIP

Rationale: all 10 checklist elements PASS or are SITE-LEVEL/non-blocking; voice gate is CLEAN with zero iterations required beyond one fix (a literal "navigating" inside a quoted bad-example phrase, and one 97-word paragraph split in two). Element 5 carries an honest Layer 2 calculation, not an invented figure.
