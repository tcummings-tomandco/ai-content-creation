#!/usr/bin/env python3
"""
Push an approved article (output/{folder}/article.json) to the Tom & Co
Storyblok space as a draft `ai_blog_post` story.

Reads:
- output/{folder}/article.json (engine output)
- variables.env or os.environ for credentials

Writes (to Storyblok via Management API):
- A new draft story under /blog/{slug}
- Returns the story ID and the dashboard URL

Required env vars:
- STORYBLOK_OAUTH_TOKEN  (Personal access token)
- STORYBLOK_SPACE_ID
- STORYBLOK_REGION       (defaults to "eu")

Usage:
    python3 scripts/push_to_storyblok.py output/2026-04-29-ai-roi-uk-business-2026/article.json
    python3 scripts/push_to_storyblok.py output/.../article.json --dry-run
"""
import argparse
import html as html_module
import json
import os
import re
import sys
import time
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENV_FILE = ROOT / "variables.env"


# ---------------------------------------------------------------------------
# Env loading
# ---------------------------------------------------------------------------

def load_env(path: Path) -> None:
    """Populate os.environ from a KEY=VALUE file. Existing env vars win."""
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        k = k.strip()
        v = v.strip().strip('"').strip("'")
        if k and k not in os.environ:
            os.environ[k] = v


# ---------------------------------------------------------------------------
# HTML → Storyblok richtext (prosemirror JSON) conversion
# ---------------------------------------------------------------------------

# Known recurring internal links — fills the required `snippet` and the
# optional `meta` and `category` fields on ai_blog_related_card. The engine
# falls back to using the link anchor text as the snippet when a URL is not
# in this table. Add a new entry whenever a Tom & Co destination needs a
# canonical card description.
KNOWN_LINK_SNIPPETS = {
    "https://www.tomandco.co.uk/ai-agency-consultancy": {
        "snippet": "Practical AI work for UK businesses, from bespoke automation and content engines to strategy and adoption advice.",
        "meta": "Service",
        "category": "AI",
    },
    "https://www.tomandco.co.uk/blog/news/are-you-really-getting-the-most-out-of-ai": {
        "snippet": "Tom & Co's small-group sessions for senior leaders. No jargon, no hype. Just practical AI insight over good coffee.",
        "meta": "Event",
        "category": "AI",
    },
}

INLINE_TAGS = {"strong", "b", "em", "i", "a", "code", "br"}
BLOCK_TAGS = {"p", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li",
              "table", "thead", "tbody", "tr", "th", "td", "blockquote",
              "aside", "div", "section", "article", "hr"}


class RichTextBuilder(HTMLParser):
    """Walk HTML and emit Storyblok prosemirror richtext JSON.

    Limited but sufficient for the engine's output: paragraphs, h2/h3,
    bullet/ordered lists, tables, blockquote (mapped from <aside>), inline
    bold, links. Skips <script> blocks (JSON-LD) and the
    "Related Tom & Co reading" trailing section which is rendered as a
    separate ai_blog_related blok instead.
    """

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.doc_content = []
        # stack of currently-open block-level nodes (the dict we are appending children into)
        self.stack = []
        # active inline marks list (each is a Storyblok mark dict)
        self.marks = []
        # set to True once we hit the <h3>Related Tom & Co reading</h3> heading
        # so we stop emitting anything to the main body
        self.suppressing = False
        # detect when we are inside the trailing <h3>About the author</h3>
        # block — also suppressed from the main body (author goes in the
        # post's author_name field)
        self._h3_text_buffer = None  # captures the h3 text to test against
        # buffer for table cell text — Storyblok table cells wrap content in
        # paragraphs, so we collect text into a paragraph node
        self._in_script = False

    # --- helpers ---------------------------------------------------------

    def _current_container(self):
        return self.stack[-1] if self.stack else None

    def _push(self, node):
        """Open a block node and start writing into it."""
        if self.suppressing:
            return
        parent = self._current_container()
        if parent is None:
            self.doc_content.append(node)
        else:
            parent.setdefault("content", []).append(node)
        self.stack.append(node)

    def _pop(self, expected_type=None):
        if self.suppressing:
            return
        if not self.stack:
            return
        if expected_type and self.stack[-1].get("type") != expected_type:
            # tolerate mismatched closures — emit what we have
            pass
        self.stack.pop()

    # Block-level containers that must not have raw text children. Whitespace
    # between siblings of these containers (e.g. the "\n  " between <th> tags
    # inside a <tr>) used to become stray empty text nodes in the richtext,
    # which pollutes the rendered DOM and breaks mobile table layout.
    STRUCTURAL_TYPES = {"table", "tableRow", "tableHeader", "tableCell",
                        "bullet_list", "ordered_list", "list_item",
                        "blockquote"}

    def _emit_text(self, text):
        if self.suppressing or self._in_script:
            return
        if not text:
            return
        parent = self._current_container()
        parent_type = parent.get("type") if parent else None

        # Whitespace at the doc root or inside any structural container should
        # be discarded, not preserved as a text node.
        if parent is None or parent_type in self.STRUCTURAL_TYPES:
            if not text.strip():
                return
            # Non-whitespace text at the root gets wrapped in a paragraph.
            # Non-whitespace text inside a structural container would be a
            # malformed source — drop quietly.
            if parent is None:
                node = {"type": "text", "text": text}
                if self.marks:
                    node["marks"] = list(self.marks)
                self.doc_content.append({"type": "paragraph", "content": [node]})
            return

        node = {"type": "text", "text": text}
        if self.marks:
            node["marks"] = list(self.marks)
        parent.setdefault("content", []).append(node)

    # --- HTMLParser hooks ------------------------------------------------

    def handle_starttag(self, tag, attrs):
        attrs_d = dict(attrs)

        if tag == "script":
            self._in_script = True
            return

        if self.suppressing:
            return

        if tag == "h3":
            # Test downstream: we suppress the body once we hit one of the
            # trailing h3 sections. We don't know the text yet, so we open
            # a heading and check on close. Easier: capture into a buffer.
            self._h3_text_buffer = []
            self._push({"type": "heading", "attrs": {"level": 3}, "content": []})
            return

        if tag in ("p",):
            self._push({"type": "paragraph", "content": []})
        elif tag in ("h1", "h2", "h4", "h5", "h6"):
            level = int(tag[1])
            self._push({"type": "heading", "attrs": {"level": level}, "content": []})
        elif tag == "ul":
            self._push({"type": "bullet_list", "content": []})
        elif tag == "ol":
            self._push({"type": "ordered_list", "content": []})
        elif tag == "li":
            # Storyblok prosemirror schema requires list_item children to be
            # block-level (paragraph), not raw text. Wrap unconditionally.
            self._push({"type": "list_item", "content": []})
            self._push({"type": "paragraph", "content": []})
        elif tag == "blockquote" or tag == "aside":
            self._push({"type": "blockquote", "content": []})
        elif tag == "table":
            self._push({"type": "table", "content": []})
        elif tag == "tr":
            self._push({"type": "tableRow", "content": []})
        elif tag == "th":
            self._push({"type": "tableHeader", "content": []})
            # cells need paragraph wrappers in Storyblok
            self._push({"type": "paragraph", "content": []})
        elif tag == "td":
            self._push({"type": "tableCell", "content": []})
            self._push({"type": "paragraph", "content": []})
        elif tag == "br":
            parent = self._current_container()
            if parent is not None:
                parent.setdefault("content", []).append({"type": "hard_break"})
        elif tag == "hr":
            self.doc_content.append({"type": "horizontal_rule"})
        elif tag in ("strong", "b"):
            self.marks.append({"type": "bold"})
        elif tag in ("em", "i"):
            self.marks.append({"type": "italic"})
        elif tag == "a":
            href = attrs_d.get("href", "")
            self.marks.append({
                "type": "link",
                "attrs": {"href": href, "target": "_self", "uuid": None,
                          "anchor": None, "linktype": "url"},
            })
        elif tag == "code":
            self.marks.append({"type": "code"})
        # silently ignore wrappers like <thead>, <tbody>, <div>, <section>

    def handle_endtag(self, tag):
        if tag == "script":
            self._in_script = False
            return

        if self.suppressing:
            # While suppressing, allow nothing through — but still track
            # heading-close so the suppression flag persists naturally.
            return

        if tag in ("strong", "b", "em", "i", "a", "code"):
            # pop the corresponding inline mark
            target = {"strong": "bold", "b": "bold", "em": "italic",
                      "i": "italic", "a": "link", "code": "code"}[tag]
            for i in range(len(self.marks) - 1, -1, -1):
                if self.marks[i].get("type") == target:
                    self.marks.pop(i)
                    break
            return

        if tag == "br" or tag == "hr":
            return

        if tag == "h3" and self._h3_text_buffer is not None:
            heading_text = "".join(self._h3_text_buffer).strip().lower()
            self._h3_text_buffer = None
            # close the heading we pushed at open
            self._pop("heading")
            # if this is one of the trailing footer h3s, start suppressing
            if heading_text.startswith("about the author") or heading_text.startswith("related tom"):
                self.suppressing = True
                # also drop the heading we just appended (footer content
                # should not appear in the richtext body)
                if self.doc_content and self.doc_content[-1].get("type") == "heading":
                    last = self.doc_content[-1]
                    if last.get("attrs", {}).get("level") == 3:
                        self.doc_content.pop()
            return

        if tag in ("p", "h1", "h2", "h4", "h5", "h6", "ul", "ol",
                   "blockquote", "aside", "table", "tr"):
            self._pop()
        elif tag == "li":
            # Two pops: the wrapping paragraph and the list_item itself.
            self._pop("paragraph")
            self._pop("list_item")
        elif tag == "th":
            self._pop("paragraph")
            self._pop("tableHeader")
        elif tag == "td":
            self._pop("paragraph")
            self._pop("tableCell")
        # ignore thead/tbody/div/section ends

    def handle_data(self, data):
        if self._in_script:
            return
        if self._h3_text_buffer is not None:
            self._h3_text_buffer.append(data)
        self._emit_text(data)

    def document(self):
        # close any open nodes left dangling
        while self.stack:
            self.stack.pop()
        return {"type": "doc", "content": self.doc_content}


# ---------------------------------------------------------------------------
# Article extraction helpers
# ---------------------------------------------------------------------------

def slugify_anchor(text: str) -> str:
    s = text.strip().lower()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"\s+", "-", s)
    return s[:60].strip("-")


def extract_h2_toc(html: str) -> list:
    """Build ai_blog_toc_item bloks from H2 headings in the article body.

    Stops at h3 boundaries (About the author / Related Tom & Co reading) and
    drops anything inside <script>...</script>.
    """
    no_script = re.sub(r"<script[\s\S]*?</script>", "", html)
    no_footer = re.split(r"<h3[^>]*>\s*About the author", no_script)[0]
    no_footer = re.split(r"<h3[^>]*>\s*Related Tom", no_footer)[0]
    items = []
    for i, match in enumerate(re.finditer(r"<h2[^>]*>(.*?)</h2>", no_footer, re.S), start=1):
        label = re.sub(r"<[^>]+>", "", match.group(1)).strip()
        if not label:
            continue
        items.append({
            "component": "ai_blog_toc_item",
            "number": f"{i:02d}",
            "anchor": slugify_anchor(label),
            "label": label,
        })
    return items


def extract_related_cards(html: str) -> list:
    """Find the trailing 'Related Tom & Co reading' UL and turn each link into
    an ai_blog_related_card blok. Best-effort — returns empty list if absent.
    """
    m = re.search(r"<h3[^>]*>\s*Related[\s\S]*?</h3>([\s\S]*?)(?:<script|$)", html, re.I)
    if not m:
        return []
    section = m.group(1)
    cards = []
    for a in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', section, re.S):
        href = html_module.unescape(a.group(1))
        anchor = html_module.unescape(re.sub(r"<[^>]+>", "", a.group(2))).strip()
        if not anchor:
            continue
        known = KNOWN_LINK_SNIPPETS.get(href, {})
        cards.append({
            "component": "ai_blog_related_card",
            "category": known.get("category", "AI"),
            "title": anchor,
            "snippet": known.get("snippet") or anchor,
            "meta": known.get("meta", ""),
            "image": {"id": None, "filename": None, "alt": "", "fieldtype": "asset"},
            "link": {"url": href, "linktype": "url", "cached_url": href,
                     "target": "_self"},
        })
    return cards


def extract_key_stats_from_article(article: dict, article_path: Path) -> list:
    """Build the ai_blog_key_stat items for this article.

    Preferred source: output/{folder}/key_stats.json next to the article.json,
    written by the article skill at draft time. Format:
        {
          "stats": [
            {"value": "54%", "label": "...", "source": "..."},
            ...
          ]
        }

    Fallback (legacy / Layer 2 only): pulls the article's Tom & Co original
    calculation from data/stat_bank.json. Used when the skill did not produce
    a key_stats.json (e.g. older articles). Always includes the stat_bank
    entry if it exists, in addition to any key_stats.json items.

    Returns a list of 0–5 ai_blog_key_stat bloks. The schema accepts more,
    but the rendered tile grid looks best at 3–5.
    """
    items = []

    key_stats_path = article_path.parent / "key_stats.json"
    if key_stats_path.exists():
        try:
            data = json.loads(key_stats_path.read_text())
            for s in data.get("stats", [])[:5]:
                items.append({
                    "component": "ai_blog_key_stat",
                    "value": str(s.get("value", "")).strip(),
                    "label": str(s.get("label", "")).strip(),
                    "source": str(s.get("source", "")).strip(),
                })
        except json.JSONDecodeError:
            pass

    # Always overlay the Layer 2 stat from the bank if it's not already
    # represented by value (avoids duplicates when the skill also includes it
    # in key_stats.json).
    bank_path = ROOT / "data" / "stat_bank.json"
    if bank_path.exists():
        try:
            bank = json.loads(bank_path.read_text())
            matches = [s for s in bank.get("stats", [])
                       if s.get("first_used_in") == article.get("slug")]
            seen_values = {i["value"] for i in items}
            for s in matches:
                unit = (s.get("unit") or "").lower()
                if unit.startswith("gbp billion"):
                    value = f"£{s.get('value')}bn"
                elif unit.startswith("gbp"):
                    value = f"£{s.get('value')}"
                else:
                    value = f"{s.get('value')} {s.get('unit', '')}".strip()
                if value in seen_values:
                    continue
                items.append({
                    "component": "ai_blog_key_stat",
                    "value": value,
                    "label": s.get("stat", "")[:120],
                    "source": (s.get("sources_used") or [{}])[0].get("title", ""),
                })
        except json.JSONDecodeError:
            pass

    return items[:5]


def build_seo_block(metadata: dict) -> dict:
    return {
        "component": "seo",
        "title": metadata.get("title", ""),
        "description": metadata.get("description", ""),
        "og_image": {"id": None, "filename": None, "alt": "", "fieldtype": "asset"},
    }


def build_story_payload(article: dict, *, article_path: Path,
                        parent_id: int | None = None,
                        category_override: str | None = None) -> dict:
    """Build the Storyblok story payload for a Management API POST."""
    html = article.get("content", "")
    metadata = article.get("metadata", {})

    # Strip JSON-LD scripts before parsing — they should not enter richtext.
    html_no_script = re.sub(r"<script[\s\S]*?</script>", "", html)

    # Convert the body HTML to Storyblok richtext.
    builder = RichTextBuilder()
    builder.feed(html_no_script)
    richtext_doc = builder.document()

    toc = extract_h2_toc(html)
    related = extract_related_cards(html)
    key_stats = extract_key_stats_from_article(article, article_path)

    body_bloks = []

    if key_stats:
        body_bloks.append({
            "component": "ai_blog_key_stats",
            "items": key_stats,
        })

    body_bloks.append({
        "component": "ai_blog_article",
        "toc": toc,
        "body": richtext_doc,
    })

    if related:
        body_bloks.append({
            "component": "ai_blog_related",
            "overline": "Related",
            "heading": "Related Tom & Co reading",
            "items": related,
        })

    # Map our category list to the Storyblok category option. Engine output
    # uses "AI"; ai_blog_post.category must include "AI" in its options
    # (one-line schema change in the website repo). Use --category to
    # override at push time (e.g. "Strategy") while waiting for that change.
    if category_override:
        category = category_override
    else:
        categories = article.get("categories") or ["AI"]
        category = categories[0] if categories else "AI"

    # Published_at is required as a datetime. Use the article's `date` field
    # plus a midnight UTC stamp.
    published_at = f"{article['date']} 00:00"

    story = {
        "name": article["title"],
        "slug": article["slug"],
        "content": {
            "component": "ai_blog_post",
            "seo": [build_seo_block(metadata)],
            "title": article["title"],
            "snippet": article.get("excerpt", "")[:240],
            "category": category,
            "published_at": published_at,
            "read_time": article.get("readTime", ""),
            "author_name": article.get("author", ""),
            "card_image": {"id": None, "filename": None, "alt": "", "fieldtype": "asset"},
            "featured": bool(article.get("featured", False)),
            "body": body_bloks,
        },
        "is_folder": False,
        "publish": False,  # always create as draft
    }
    if parent_id is not None:
        story["parent_id"] = parent_id

    return {"story": story, "publish": 0}


# ---------------------------------------------------------------------------
# Storyblok Management API client
# ---------------------------------------------------------------------------

def api_base(region: str) -> str:
    return "https://api-us.storyblok.com" if region == "us" else "https://mapi.storyblok.com"


def api_request(method: str, path: str, body=None, *, token: str, region: str,
                attempt: int = 0):
    url = f"{api_base(region)}{path}"
    data = json.dumps(body).encode("utf-8") if body is not None else None
    headers = {"Authorization": token, "Content-Type": "application/json"}
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            payload = r.read().decode("utf-8") or "{}"
            return r.status, json.loads(payload)
    except HTTPError as e:
        body_text = e.read().decode("utf-8", errors="replace")
        # rate-limit retry
        if e.code == 429 and attempt < 4:
            time.sleep(1.0 * (attempt + 1))
            return api_request(method, path, body, token=token, region=region,
                               attempt=attempt + 1)
        raise SystemExit(f"Storyblok API {method} {path} -> {e.code}\n{body_text}")
    except URLError as e:
        raise SystemExit(f"Network error calling Storyblok: {e}")


def find_story_by_slug(*, slug: str, full_slug: str, token: str, region: str,
                       space_id: str):
    """Return the story dict if a story with this slug or full_slug exists."""
    status, payload = api_request("GET",
        f"/v1/spaces/{space_id}/stories?with_slug={full_slug}",
        token=token, region=region)
    stories = payload.get("stories", [])
    for s in stories:
        if s.get("slug") == slug or s.get("full_slug") == full_slug:
            return s
    return None


def find_or_resolve_parent_id(*, parent_slug: str, token: str, region: str,
                              space_id: str) -> int | None:
    """Look up the numeric ID of a folder story by full_slug. Returns None
    if not found — the new story will be created at the space root in that
    case."""
    if not parent_slug:
        return None
    status, payload = api_request("GET",
        f"/v1/spaces/{space_id}/stories?with_slug={parent_slug}&starts_with={parent_slug}",
        token=token, region=region)
    for s in payload.get("stories", []):
        if s.get("full_slug") == parent_slug and s.get("is_folder"):
            return s.get("id")
    return None


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("article_path", help="path to output/{folder}/article.json")
    ap.add_argument("--parent-slug", default="ai-agency-consultancy/blog",
                    help="folder slug to place the story under (default: ai-agency-consultancy/blog)")
    ap.add_argument("--category", default=None,
                    help="override the category option (e.g. 'Strategy' while the schema "
                         "still lacks an 'AI' option). Defaults to article.json categories[0].")
    ap.add_argument("--dry-run", action="store_true",
                    help="build and print the payload, do not POST to Storyblok")
    ap.add_argument("--env-file", default=str(DEFAULT_ENV_FILE),
                    help="path to env file (default: variables.env)")
    args = ap.parse_args()

    load_env(Path(args.env_file))

    article_path = Path(args.article_path).resolve()
    if not article_path.exists():
        raise SystemExit(f"article.json not found: {article_path}")
    article = json.loads(article_path.read_text())

    token = os.environ.get("STORYBLOK_OAUTH_TOKEN", "").strip()
    space_id = os.environ.get("STORYBLOK_SPACE_ID", "").strip()
    region = os.environ.get("STORYBLOK_REGION", "eu").strip()

    if not args.dry_run:
        if not token or not space_id:
            raise SystemExit(
                "Missing STORYBLOK_OAUTH_TOKEN or STORYBLOK_SPACE_ID. Set in "
                "variables.env or in the environment."
            )

    # Resolve parent folder (e.g. /blog → id N)
    parent_id = None
    if not args.dry_run and args.parent_slug:
        parent_id = find_or_resolve_parent_id(
            parent_slug=args.parent_slug, token=token, region=region,
            space_id=space_id)

    payload = build_story_payload(article, article_path=article_path,
                                  parent_id=parent_id,
                                  category_override=args.category)

    if args.dry_run:
        print(json.dumps(payload, indent=2))
        return 0

    full_slug = f"{args.parent_slug}/{article['slug']}" if args.parent_slug else article["slug"]
    existing = find_story_by_slug(slug=article["slug"], full_slug=full_slug,
                                  token=token, region=region, space_id=space_id)
    if existing:
        print(f"[skip] story already exists at {full_slug} (id={existing['id']}). "
              f"Refusing to overwrite. Delete the draft in Storyblok or rename the article slug.")
        return 1

    status, response = api_request(
        "POST", f"/v1/spaces/{space_id}/stories",
        body=payload, token=token, region=region)
    if status not in (200, 201):
        raise SystemExit(f"Unexpected status {status}: {response}")

    story = response.get("story", {})
    sid = story.get("id")
    name = story.get("name", "")
    fslug = story.get("full_slug", full_slug)

    print(f"\n[ok] story created as draft")
    print(f"     ID:        {sid}")
    print(f"     full_slug: {fslug}")
    print(f"     title:     {name}")
    print(f"     dashboard: https://app.storyblok.com/#/me/spaces/{space_id}/stories/0/0/{sid}")

    # Print a small machine-readable footer the calling routine can grep
    print(f"\nSTORYBLOK_STORY_ID={sid}")
    print(f"STORYBLOK_FULL_SLUG={fslug}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
