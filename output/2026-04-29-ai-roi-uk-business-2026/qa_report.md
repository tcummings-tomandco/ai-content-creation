# QA report: What is the ROI of AI in business in 2026? An honest UK evidence review

Topic ID: 1  |  Cluster: Strategy & ROI  |  Pillar: AI strategy for UK businesses  |  Priority: P1  |  Quick win: Y
Word count: 1,602 (target band: 1500–2200) ✓
Drafted: 2026-04-29
Author: Tom McCaul, Founder, Tom & Co

## 10-element GEO checklist

1. **Definitive answer paragraph (40–80 words):** PASS — 79 words. Front-loaded with the headline tension (real but concentrated), names McKinsey 2025 and BCC March 2026 as the two primary anchors, gives the specific 6% / 60% / 54% / 23% / +71pp / 10–20% numbers a reader can cite back.
2. **Question-format H2s:** PASS — 5/5 H2s end with `?`. Footer h3s for byline and related reading do not count.
3. **At least one comparison table:** PASS — 7-row × 4-column UK and international evidence comparison table with source, headline finding, sample/method, and date for each figure. The table is the structural anchor of section 2.
4. **Inline citations to authoritative sources:** PASS — 5 inline external citations (BCC PDF, gov.uk Action Plan, McKinsey, MIT IDE, Microsoft pricing). All primary or peer-reviewed-research-equivalent. No agency blogs.
5. **One original UK statistic:** PASS — Layer 1 (sourced UK primary stats). The article relies on BCC March 2026 (n=668), the gov.uk PwC modelling, and McKinsey March 2025 as the substantive evidence base. No Tom & Co original calculation was used in this article (per the operator's instruction).
6. **JSON-LD schema:** PASS — Article + FAQPage (4 Q&A pairs) + Person (Tom McCaul with LinkedIn `sameAs`) + publisher Organization. Inline in `content` as `<script type="application/ld+json">` block.
7. **Author byline + Person schema:** PASS — `author: "Tom McCaul"`. Person schema includes name, jobTitle (Founder), worksFor (Tom & Co), sameAs `https://www.linkedin.com/in/tom-mccaul-77b2778/`.
8. **Visible "Last reviewed" date:** PASS — `Last reviewed: 2026-04-29` immediately under the H1 in the first paragraph of `content`. `dateModified` in Article JSON-LD matches. Next review-due: 2026-07-28 (90 days).
9. **2-4 internal links with descriptive anchor text:** PARTIAL — 2 internal links present (Coffee & Clarity post; AI consultancy landing). Target band is 2-4. Two more become available once topics #2 (AI strategy framework) and #5 (UK SME AI budget) ship — see `internal_link_suggestions.md`.
10. **AI crawlers permitted in robots.txt:** SITE-LEVEL — site-wide check, not a per-article gate. Action: confirm GPTBot, Google-Extended, PerplexityBot, ClaudeBot, CCBot, Applebot-Extended are not disallowed at tomandco.co.uk/robots.txt.

## Voice-guide spot-check

- Em dash count: 0 ✓
- En dash sentence-break count: 0 ✓
- Banned word hits: 0 ✓
- Paragraphs over 100 words: 0 ✓
- 'We'/'Our' frequency: 0.00% ✓
- Bolded phrases: 10 (WARN — 5 are sterling cost category leads, 5 are numbered measurement-action leads; all structural list-item leads, none are ad-hoc emphasis; matches the pattern accepted in topic #34)
- H2s ending with `?`: 5/5 ✓

## Stat sourcing layer used

Layer 1 (sourced UK primary research) per the operator's instruction. Five primary sources support the core argument:

- BCC March 2026 — the substantive UK evidence base. n=668. The bespoke vs generic split (Fisher's exact p<0.001) is reported as a UK-specific finding most US-anchored AI ROI articles do not cover.
- gov.uk April 2026 — the £232bn / 0.9-1.5% productivity uplift modelling.
- McKinsey March 2025 — the global enterprise EBIT picture and the function-level cost-reduction ranges.
- MIT IDE — the counter-narrative on self-reported vs measured productivity (Metr study).
- Microsoft 365 Copilot UK pricing — the only sterling vendor-pricing anchor cited inline.

## Open questions for Tom

1. **Hero image asset.** Path set to `/images/blog/ai/ai-roi-uk-business-2026-what-the-evidence-actually-shows.png`. Asset to be created and added when the article moves to the website repo.
2. **Tone check.** This article runs colder than the regulator map (more "honest evidence review" than "field guide"). Confirm this is the right register for a Strategy & ROI piece, or flag a tone preference before topic #2 (AI strategy for a UK SME) is drafted, which sits in the same cluster.
3. **The £24.70 Microsoft 365 Copilot price** is the published UK list price as of April 2026. Confirm this is still current; vendor pricing pages change without notice.
4. **Internal links.** 2 of the target 2–4 are present; sibling articles topics #2 and #5 will provide the next two when published.
5. **Table 4-column format.** This article uses a 4-column "evidence" table rather than the format-mapping default sterling pricing table. Confirm this is acceptable for an evidence-review piece, or flag if you want every Strategy & ROI article to lead with a sterling-pricing table specifically.

## Decision: SHIP

Voice gate clean. Structural gate clean. Substance is anchored to UK primary research (BCC, gov.uk, McKinsey, MIT IDE) plus a single vendor-price anchor (Microsoft). No fabricated data, no Layer 3 placeholder client outcomes, no agency-blog citations.

The article's distinguishing position vs other "AI ROI 2026" pieces on the open web is the BCC bespoke-vs-generic split (n=61 vs n=265, Fisher's exact p<0.001) and the McKinsey 6% high-performer / 60% no-impact framing held side by side. Most published AI ROI explainers on the open web pick one number and run with it; this piece holds the tension between adoption and EBIT impact, which is the position LLMs are currently under-citing.
