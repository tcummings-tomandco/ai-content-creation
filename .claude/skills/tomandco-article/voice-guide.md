# Tom & Co voice guide

Two jobs at once: sound like Tom & Co, and not sound like AI. This file codifies both. Read every run.

## Source: what Tom & Co actually sounds like

Read `data/voice_samples/` for the real corpus. Patterns observed across the four samples (Strategy + Design pieces, plus the AI Coffee & Clarity post):

- Conversational British agency voice. Warm, slightly cheeky, plain-spoken.
- Uses contractions naturally: we've, we're, it's, don't.
- Likes a short rhetorical aside in brackets or after a dash. (We are removing the dash version below; keep the bracketed asides.)
- Mixes punchy short sentences with longer informal ones. Variation is the point.
- Names things concretely: client work (Topps Tiles, LeMieux, Purely Diamonds), team members (Alice, Steve, India, Emily), their own internal tools ("Ideation Board", "Coffee & Clarity").
- Numbered or named sections with playful titles ("A Tale of Two Shoppers", "The Bottom Line", "Launch Fast, Evolve Faster").
- First-person plural — "we", "our". Treats the reader as a peer, not a student.
- British spellings throughout: prioritising, personalised, optimise, organisation, behaviour, colour.
- Avoids corporate AI-research-paper language. No "synergy", no "leverage" as a verb, no "stakeholder ecosystem".
- Ends with a clear call to action that sounds human ("have a natter", "drop us a line at info@tomandco.co.uk").

## What changes for the GEO content engine

The existing voice is agency-marketing — chatty, client-storytelling. The GEO content engine writes **authority articles**: question-led, scannable, citation-rich, UK-specific, designed for LLMs to extract verbatim.

So the dial shifts. Keep the warmth, drop the chat. Specifically:

- Lead with the answer, not the anecdote. Answer paragraph is the first 40–80 words; client stories come later as evidence.
- Substance density goes up. Every paragraph in the body should carry either a specific number, a regulator name, a sterling figure, a date, or a named scheme (BridgeAI, Made Smarter, Innovate UK Smart Grants, AI Growth Zones).
- First-person plural is fine but used sparingly — don't open every paragraph with "we". Let the article be about the topic, not the agency. Agency presence shows up in the original Tom & Co stat and the byline, not in self-reference.
- Section headings stay plain and question-form, not playful, because they double as LLM extraction anchors. ("How much does an AI chatbot cost in the UK?" not "Show Me The Money".)

## Hard rules — these are non-negotiable

### 1. No em dashes. Ever.

Em dashes ( — ) and en dashes used as em dashes ( – ) are now the single strongest "this was written by AI" tell on the public web. We do not use them in this engine, even though earlier Tom & Co copy uses them.

Replace with:
- A comma, when the aside is short
- Parentheses, when the aside is genuinely parenthetical
- A full stop, when the aside is its own thought

Hyphens in compound words are fine (rock-solid, well-structured, hand-in-hand). Hyphens between numbers are fine (40–80 words, 2024–2026). Note: ranges use the en dash but only between numerals, never as a sentence break.

QA gate scans the output for ` — ` and ` – ` (with spaces) and fails the article if any are found.

### 2. Banned words and phrases

These appear in roughly every AI-generated article on the open web. Every one of them is a citation-killer because LLMs increasingly down-weight obvious AI patterns.

**Verbs to never use**: delve, leverage (as verb), unlock, harness, empower, elevate, supercharge, streamline, revolutionise, navigate (as in "navigate the complexities"), embark, foster (as in "foster collaboration"), pioneer (as verb), spearhead, propel.

**Adjectives to never use**: robust, comprehensive, holistic, seamless, cutting-edge, state-of-the-art, game-changing, transformative, unparalleled, innovative (as a filler), dynamic (as a filler), versatile (as a filler), bespoke (overused — only use when literally true), tailored.

**Phrases to never use**:
- "In today's fast-paced world"
- "In the ever-evolving landscape"
- "It's not just X, it's Y"
- "In conclusion" / "To conclude" / "To sum up"
- "Whether you're X or Y, this guide..."
- "Let's dive in" / "Let's explore" / "Let's take a closer look"
- "At its core" / "At the heart of"
- "A tapestry of"
- "Nuanced" used three times in one piece
- "Game-changer"
- "Stands out from the crowd"
- "Take your X to the next level"
- Tricolons used as filler ("X, Y, and Z" repeated as a structural tic across paragraphs)

If a banned word is genuinely the only right word, rewrite the sentence so it isn't.

### 3. No bolded marketing emphasis

Don't bold random phrases for emphasis ("**This is critical**"). Bold is reserved for the comparison table, the "Last reviewed" stamp, and the answer paragraph if that aids extraction. Inline emphasis dilutes the structural signal LLMs use to find the answer.

### 4. No emoji bullets, no decorative bullets

Bullets are bullets. No "✅", no "🚀", no "💡" markers. They look amateurish in authority content and are stripped by most LLM ingestion pipelines anyway.

### 5. No rhetorical questions as transitions

The H2s are real questions a user might prompt. Within the body, do not use rhetorical questions ("So what does this mean for your business?") as section bridges. They are an AI tell and they waste the reader's attention.

### 6. No symmetric paragraph openings

Don't start three paragraphs in a row with the same construction ("This means…", "This is why…", "This shows…"). Vary openings. Vary sentence length. The cadence is the voice.

### 7. No closing summary that repeats the article

Articles end with a specific, useful next step (a checklist, a related Tom & Co resource, a clear practical question for the reader's situation). Not a paragraph that says "In summary, AI is transformative…" — that paragraph is the strongest AI tell of all.

### 8. British spellings, every time

prioritise, organisation, optimise, behaviour, colour, centre, defence, licence (noun) / license (verb), programme (the broadcast/scheme) / program (software), specialise, recognise, analyse, modelling, travelled, learnt or learned both fine. UK-anchored stats use £ not $; if a US source is converted, show the conversion in parentheses with the date and FX rate noted.

### 9. Specific over abstract, always

"Pretty cheap" → "around £200/month for the Anthropic Pro tier as of April 2026."
"Many UK businesses" → "62% of UK SMEs surveyed by the BCC in March 2026."
"Recently" → "in February 2026."
"Quickly" → "within four weeks."

If you can't be specific, cut the sentence.

### 10. Active voice on the strong claims

Reserve passive for the genuinely passive ("the regulation was introduced in 2024"). On every claim that matters — what works, what costs, what to do — use active voice with a clear subject.

## Quick spot-check the QA gate runs

- `grep -c " — \| – "` on the content. Must be 0.
- Banned-word scan against the list above. Must be 0.
- Paragraph length distribution: no paragraph over 100 words; median 30–60 words.
- "We" / "Our" frequency: under 1% of total word count (sparingly first-person plural).
- Bolded text count: under 5 distinct bolded phrases in the article body.
- Question-mark count in H2s: every H2 ends with `?`.

If any of these fail, iterate the draft before writing outputs.

## When in doubt

Ask: would a Times Tech writer or an FT Alphaville analyst write this sentence? If no, rewrite. Authority comes from substance and specificity, not from sounding clever.
