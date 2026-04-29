# Format mapping — which structural template for which article

Each topic in the roadmap has a `Format` column (e.g. "Definition + benchmark table", "Decision tree", "5-step framework", "Comparison table"). This file translates each format into a concrete article skeleton with section ordering, what goes in the body, and where the GEO levers (answer paragraph, comparison table, original stat, internal links) sit.

## Universal article skeleton

Every article, regardless of format, opens with the same three components in this order:

1. **H1**: the headline question, ≤70 characters, mirroring the strongest user prompt.
2. **Last reviewed line**: `Last reviewed: {YYYY-MM-DD}` immediately under the H1.
3. **Definitive answer paragraph**: 40–80 words, no surrounding context required, contains a specific number/regulator/scheme. This is the single most important paragraph in the article.

Then the format-specific body. Then the universal close:

- **About the author** — one paragraph naming the author, role, one credential, LinkedIn link.
- **Related Tom & Co articles** — 2 to 4 internal links with descriptive anchor text (covered in element 9).
- **JSON-LD `<script>` block** — Article + FAQPage (if applicable) + HowTo (if applicable) + Person.

## Format templates

### A. Definition + benchmark table

Used for: ROI, cost guides, "what is X" topics that need a number to be useful (#1, #5, #15, #21, #49, #75).

Body:
1. H2: What does {term} mean in 2026? — definition with units and date.
2. H2: How much does it cost in the UK? — sterling pricing table (this is the comparison table for element 3).
3. H2: What does the data show? — Layer 1 or 2 stat, prominently placed.
4. H2: Where does {term} fit in a UK SME's stack? — practical mapping.
5. H2: What should a UK leader do this quarter? — 3–5 bullet next steps.

### B. Decision tree

Used for: applicability questions where the answer depends on the reader's situation (#33 EU AI Act, #4 build vs buy, #45 RAG vs fine-tuning vs prompting, #53 on-prem vs cloud).

Body:
1. H2: Does {situation} apply to your business? — the answer paragraph already gave the headline answer; this section opens the tree.
2. The decision tree itself, rendered as a numbered branching list with explicit yes/no at each node. (Visual diagram is a Phase 2 enhancement.)
3. H2: What if you're a {category 1}? — case-walked outcome.
4. H2: What if you're a {category 2}? — case-walked outcome.
5. H2: What if you're a {category 3}? — case-walked outcome.
6. H2: What are the next steps for each case? — a comparison table summarising the actions per branch (this is element 3's table).

### C. Regulator map / framework explainer

Used for: #34 (UK AI regulation map — flagship), #2 (AI strategy framework), #6 (maturity model), #42 (governance for SMEs).

Body:
1. H2: Who regulates AI in the UK in 2026? — list and one-line role of each regulator.
2. The map itself: a comparison table with rows = AI use cases (chatbot, automated decisioning, biometric, generative content) and columns = regulator, statutory basis, sterling penalty range, latest guidance link.
3. H2: How does the EU AI Act overlap? — explicit overlap section.
4. H2: What does an SME do first? — 3–5 actions ordered by leverage.
5. H2: Which industries face the toughest scrutiny? — sector breakdown with citations.

### D. Comparison / "vs" / "best" / "alternative"

Used for: #11 (AI agents vs RPA), #47 (ChatGPT vs Claude vs Gemini vs Copilot), #48 (Copilot vs ChatGPT Enterprise), #51 (agent platforms), #73 (AI agent toolkit).

Body:
1. H2: What are the options? — one-paragraph each on the named alternatives.
2. The comparison table — rows = options, columns = price (sterling), best for, weaknesses, latest version date, sources. **This table is the article**, the rest supports it.
3. H2: Which one wins on {dimension 1}? — single-dimension verdict.
4. H2: Which one wins on {dimension 2}? — single-dimension verdict.
5. H2: Which is right for a UK SME? — practical recommendation by reader scenario.

### E. 5-step framework / how-to

Used for: #2, #22 (rank in ChatGPT), #23 (AEO), #29 (track LLM citations), #36 (DPIA template).

Body:
1. H2: What is the {framework name}? — overview.
2. H2: Step 1 — {action} — sub-bullets, what good looks like.
3. H2: Step 2 — {action}.
4. H2: Step 3 — {action}.
5. H2: Step 4 — {action}.
6. H2: Step 5 — {action}.
7. H2: How long does it take? — realistic UK SME estimate using a Layer 2 calculation.
8. Comparison table: tooling options for each step (element 3).

The HowTo JSON-LD schema is required for this format.

### F. Sector report

Used for: #58 (UK financial services), #59 (accountants), #60 (UK law firms), #61 (retail/ecommerce), #62 (NHS-adjacent), #63 (manufacturing), #64 (creative agencies), #65 (public sector), #66 (insurance).

Body:
1. H2: What is the state of AI in {sector} in 2026? — adoption stat, regulator overlay.
2. H2: What are the top 3 use cases that pay back? — named, costed, with a UK case reference where possible.
3. H2: Which regulators apply? — sector regulator table (element 3).
4. H2: What funding is available? — UK funding lines specific to the sector.
5. H2: What does a 90-day plan look like? — practical sequencing.

### G. Listicle + ROI

Used for: #3 (use cases that pay back in year 1), #56 (MCP servers to build first).

Body:
1. H2: How did we shortlist these? — methodology.
2. Item 1: {name} — what, who, sterling payback, evidence, source.
3. Item 2: ...
4. Item N (5–10 items typical).
5. H2: Which one to start with? — decision rule for the reader.
6. Comparison table summarising all items by payback time, complexity, regulatory load.

### H. Analysis / counter-narrative

Used for: #7 (95% AI failure rate), #20 (Context Gap), #24 (AI for content marketing), #37 (hallucination risk), #71 (productivity paradox).

Body:
1. H2: What does the data actually show? — primary-source numbers, in tension with the popular narrative.
2. H2: Why does the popular narrative get it wrong? — three specific reasons.
3. H2: What does this mean for a UK SME? — practical implication, not a hedge.
4. H2: How should you decide? — concrete decision rule.
5. Comparison table contrasting the popular view with the evidence-based view (element 3).

### I. Template / checklist

Used for: #9 (CFO ROI scorecard), #10 (vendor contract checklist), #36 (DPIA template), #43 (AI risk register).

Body:
1. H2: When do you need this? — one paragraph trigger.
2. The template itself, as a numbered list or a downloadable structure.
3. H2: How to use it. — three-step process.
4. H2: What to do with the output. — escalation paths and examples.
5. Comparison table: what fields appear / don't appear in this template vs the standard one (element 3).

### J. Glossary / definition list

Used for: #75 (2026 AI glossary).

Special-case format. Treated as evergreen content with quarterly refresh. Each term gets a 40–80 word definition that itself meets element 1 criteria. Comparison table compares closely-confused terms (e.g. RAG vs fine-tuning vs prompt engineering) — this is the structural anchor that earns citations.

## UK source preferences by cluster

| Cluster | First-choice sources |
|---|---|
| Strategy & ROI | ONS, Bain, BCC, MIT IDE, Deloitte UK, Innovate UK |
| Operations & Efficiency | gov.uk, Innovate UK, BridgeAI, Made Smarter, ONS productivity |
| Marketing & Sales | Marketing Week, IPA, ConvertMate, SemRush, Profound, Princeton GEO paper |
| Risk, Governance & Legal | ICO, FCA, MHRA, SRA, CMA, Ofcom, gov.uk, parliament.uk, Lords Library |
| Technical & Build | arxiv, Anthropic/OpenAI/Google docs, llm-stats, Vellum leaderboard, MCP spec |
| UK Industry Verticals | sector regulator + sector trade body (e.g. UK Finance, NHS England, ABI, Law Society) + Made Smarter for manufacturing |
| Workforce | ONS, BCC, CIPD, ACAS, British Progress reports |
| Tools / emerging vocabulary | Vendor docs, peer-reviewed where applicable, plus the same Marketing/SEO research firms |

The roadmap row's `UK angle` column is a strong signal; honour it.

## Length bands

| Suggested length | Target | Acceptable range |
|---|---|---|
| 1500-2200 | 1800 | 1500–2200 |
| 2000-3000 | 2400 | 2000–3000 |
| Pillar (3000–5000) | 3500 | 3000–5000 |
| Newsroom / fast-react | 700–1000 | 700–1200 |

Going substantially over the band reduces structural clarity for LLMs. Going substantially under fails the semantic-completeness threshold. Stay in the band.
