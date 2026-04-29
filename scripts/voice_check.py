#!/usr/bin/env python3
"""
Mechanical voice-guide compliance scan. Runs over the article HTML body.

Exit code is the number of failed checks (0 means clean).
Writes a markdown report fragment to stdout suitable for inlining into qa_report.md.

Usage:
    python3 scripts/voice_check.py path/to/article.html
    python3 scripts/voice_check.py output/2026-04-29-uk-ai-regulation-map/article.json
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path


BANNED_WORDS = [
    # Verbs
    r"\bdelve(s|d|ing)?\b",
    r"\bleverag(e|es|ed|ing)\b",
    r"\bunlock(s|ed|ing)?\b",
    r"\bharness(es|ed|ing)?\b",
    r"\bempower(s|ed|ing)?\b",
    r"\belevat(e|es|ed|ing)\b",
    r"\bsupercharg(e|es|ed|ing)\b",
    r"\bstreamlin(e|es|ed|ing)\b",
    r"\brevolutionis(e|es|ed|ing)\b",
    r"\brevolutioniz(e|es|ed|ing)\b",
    r"\bnavigat(e|es|ed|ing)\b",
    r"\bembark(s|ed|ing)?\b",
    r"\bfoster(s|ed|ing)?\b",
    r"\bspearhead(s|ed|ing)?\b",
    r"\bpropel(s|led|ling)?\b",
    # Adjectives
    r"\brobust\b",
    r"\bcomprehensive\b",
    r"\bholistic\b",
    r"\bseamless(ly)?\b",
    r"\bcutting-edge\b",
    r"\bstate-of-the-art\b",
    r"\bgame-chang(er|ing)\b",
    r"\btransformative\b",
    r"\bunparalleled\b",
    # Phrases
    r"in today'?s fast-paced world",
    r"in the ever-evolving landscape",
    r"it'?s not just .* it'?s",
    r"\bin conclusion\b",
    r"\bto sum up\b",
    r"whether you'?re .* or .*,",
    r"let'?s dive in",
    r"let'?s explore",
    r"let'?s take a closer look",
    r"\bat its core\b",
    r"\bat the heart of\b",
    r"a tapestry of",
    r"stands? out from the crowd",
    r"take your .* to the next level",
]


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []
        self.skip = False

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self.skip = True

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip = False

    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)

    def text(self):
        return "".join(self.parts)


def extract_html(input_path):
    p = Path(input_path)
    if p.suffix == ".json":
        d = json.loads(p.read_text())
        return d.get("content", "")
    return p.read_text()


def split_paragraphs(html):
    parts = re.split(r"</?p[^>]*>", html, flags=re.I)
    return [TextExtractor.__call__ if False else strip_tags(p).strip() for p in parts if p.strip()]


def strip_tags(html):
    e = TextExtractor()
    e.feed(html)
    return e.text()


def count_em_dash(text):
    return len(re.findall(r" — ", text))


def count_en_dash_break(text):
    # En dash flanked by spaces, used as sentence break.
    # Allow numerical ranges like "40–80" (no spaces) and "2024-2026".
    return len(re.findall(r" – ", text))


def count_banned_words(text):
    hits = []
    lc = text.lower()
    for pat in BANNED_WORDS:
        for m in re.finditer(pat, lc):
            hits.append((pat, m.group(0)))
    return hits


def paragraph_word_counts(html):
    text_only = strip_tags(html)
    paras = re.split(r"\n\n+", text_only)
    return [(p.strip(), len(p.split())) for p in paras if p.strip()]


def we_our_frequency(text):
    words = re.findall(r"\b[\w']+\b", text)
    if not words:
        return 0.0
    we_our = sum(1 for w in words if w.lower() in ("we", "our", "we've", "we're", "we'll"))
    return 100.0 * we_our / len(words)


def h2_check(html):
    h2s = re.findall(r"<h2[^>]*>(.*?)</h2>", html, flags=re.I | re.S)
    h2s_text = [strip_tags(h).strip() for h in h2s]
    not_question = [h for h in h2s_text if not h.rstrip().endswith("?")]
    return h2s_text, not_question


def bold_count(html):
    return len(re.findall(r"<(strong|b)\b", html, flags=re.I))


def main():
    if len(sys.argv) != 2:
        print("usage: voice_check.py <article.html|article.json>", file=sys.stderr)
        return 2

    html = extract_html(sys.argv[1])
    text = strip_tags(html)
    failures = 0

    em = count_em_dash(text)
    en_break = count_en_dash_break(text)
    banned = count_banned_words(text)
    para_lengths = paragraph_word_counts(html)
    long_paras = [n for _, n in para_lengths if n > 100]
    we_freq = we_our_frequency(text)
    h2_all, h2_bad = h2_check(html)
    bolds = bold_count(html)

    print("# Voice-guide spot-check\n")
    em_ok = em == 0
    print(f"- Em dash count: {em} {'✓' if em_ok else 'FAIL'}")
    if not em_ok:
        failures += 1

    en_ok = en_break == 0
    print(f"- En dash sentence-break count: {en_break} {'✓' if en_ok else 'FAIL'}")
    if not en_ok:
        failures += 1

    if banned:
        failures += 1
        print(f"- Banned word hits: {len(banned)} FAIL")
        for pat, m in banned[:20]:
            print(f"    - `{m}` (pattern `{pat}`)")
    else:
        print("- Banned word hits: 0 ✓")

    long_ok = len(long_paras) == 0
    print(f"- Paragraphs over 100 words: {len(long_paras)} {'✓' if long_ok else 'FAIL'}")
    if not long_ok:
        failures += 1

    we_ok = we_freq < 1.0
    print(f"- 'We'/'Our' frequency: {we_freq:.2f}% {'✓' if we_ok else 'WARN'}")

    bolds_ok = bolds <= 5
    print(f"- Bolded phrases: {bolds} {'✓' if bolds_ok else 'WARN'}")

    h2_ok = len(h2_bad) == 0 and len(h2_all) > 0
    print(f"- H2s ending with ?: {len(h2_all) - len(h2_bad)}/{len(h2_all)} {'✓' if h2_ok else 'FAIL'}")
    if not h2_ok:
        failures += 1
        for h in h2_bad:
            print(f"    - missing question mark: `{h}`")

    print()
    print(f"**Result: {'CLEAN' if failures == 0 else f'{failures} FAILURES'}**")
    return failures


if __name__ == "__main__":
    sys.exit(main())
