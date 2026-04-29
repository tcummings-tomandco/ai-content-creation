#!/usr/bin/env python3
"""
Copy an approved article's preview.html into docs/previews/{slug}/index.html
so GitHub Pages can serve it at:

    https://tcummings-tomandco.github.io/ai-content-creation/previews/{slug}/

Injects <meta name="robots" content="noindex,nofollow"> so search engines and
LLM crawlers do not pick the preview up. Refreshes docs/index.html with the
current list of published previews.

Usage:
    python3 scripts/publish_preview.py <output-folder-name>
    python3 scripts/publish_preview.py 2026-04-29-ai-roi-uk-business-2026
    python3 scripts/publish_preview.py --all          # republish every output/* folder
"""
import argparse
import json
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output"
DOCS = ROOT / "docs"
PREVIEWS = DOCS / "previews"

NOINDEX_META = '<meta name="robots" content="noindex,nofollow">'
PREVIEW_BANNER = """<div style="background:#fff3cd;border-bottom:2px solid #c8a85a;padding:10px 20px;font-family:-apple-system,Helvetica,Arial,sans-serif;font-size:14px;color:#5c4a00;">
<strong>Tom &amp; Co AI Content Engine — Phase 1 preview.</strong>
This page is a draft for internal review only. Not crawled, not indexed, not yet on tomandco.co.uk.
</div>
"""


def slug_from_folder(folder_name):
    # output folders are named "YYYY-MM-DD-slug"; strip the date.
    m = re.match(r"^\d{4}-\d{2}-\d{2}-(.+)$", folder_name)
    return m.group(1) if m else folder_name


def inject_noindex_and_banner(html):
    if NOINDEX_META not in html:
        html = html.replace("<head>", "<head>\n  " + NOINDEX_META, 1)
    if "Phase 1 preview" not in html.split("<body>")[1].split("</body>")[0][:300]:
        html = html.replace("<body>", "<body>\n" + PREVIEW_BANNER, 1)
    return html


def publish_one(folder_name):
    src_dir = OUTPUT / folder_name
    src_html = src_dir / "preview.html"
    src_article = src_dir / "article.json"
    if not src_html.exists():
        print(f"[skip] {folder_name}: no preview.html", file=sys.stderr)
        return None
    if not src_article.exists():
        print(f"[skip] {folder_name}: no article.json", file=sys.stderr)
        return None

    article = json.loads(src_article.read_text())
    slug = article.get("slug") or slug_from_folder(folder_name)

    dest_dir = PREVIEWS / slug
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_html = dest_dir / "index.html"

    html = src_html.read_text()
    html = inject_noindex_and_banner(html)
    dest_html.write_text(html)

    print(f"[ok] {folder_name} -> docs/previews/{slug}/")
    return {
        "slug": slug,
        "title": article["title"],
        "date": article["date"],
        "categories": article.get("categories", []),
        "author": article.get("author", ""),
        "excerpt": article.get("excerpt", ""),
        "folder": folder_name,
    }


def rebuild_index(entries):
    entries = sorted(entries, key=lambda e: e["date"], reverse=True)
    rows = []
    for e in entries:
        rows.append(
            f'    <li><a href="previews/{e["slug"]}/">{e["title"]}</a>'
            f'<br><span class="meta">{e["date"]} &bull; {", ".join(e["categories"])} &bull; {e["author"]}</span>'
            f'<p class="excerpt">{e["excerpt"]}</p></li>'
        )
    body = "\n".join(rows) if rows else "    <li>No previews published yet.</li>"
    html = f"""<!doctype html>
<html lang="en-GB">
<head>
  <meta charset="utf-8">
  <meta name="robots" content="noindex,nofollow">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Tom &amp; Co AI Content Engine — preview library</title>
  <style>
    body {{ font-family: 'Helvetica Neue', Arial, sans-serif; max-width: 760px; margin: 40px auto; padding: 0 20px; line-height: 1.55; color: #1a1a1a; }}
    h1 {{ font-size: 1.8rem; margin-bottom: 0.2em; }}
    .lede {{ color: #555; margin-top: 0; margin-bottom: 2em; }}
    ul.list {{ list-style: none; padding: 0; }}
    ul.list li {{ border-top: 1px solid #eee; padding: 16px 0; }}
    ul.list a {{ color: #1d4ed8; text-decoration: none; font-weight: 600; font-size: 1.05rem; }}
    ul.list a:hover {{ text-decoration: underline; }}
    .meta {{ font-size: 0.85rem; color: #777; }}
    .excerpt {{ font-size: 0.95rem; color: #333; margin: 6px 0 0; }}
    footer {{ font-size: 0.85rem; color: #777; margin-top: 3em; border-top: 1px solid #eee; padding-top: 1em; }}
  </style>
</head>
<body>
  <h1>Tom &amp; Co AI Content Engine</h1>
  <p class="lede">Phase 1 article previews. Internal review only — not yet on tomandco.co.uk and not indexed by search engines or LLM crawlers.</p>
  <ul class="list">
{body}
  </ul>
  <footer>
    Last rebuilt: {datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")}.
    Previews are noindex/nofollow and live only as long as the engine repo.
    Source: <a href="https://github.com/tcummings-tomandco/ai-content-creation">tcummings-tomandco/ai-content-creation</a>.
  </footer>
</body>
</html>"""
    (DOCS / "index.html").write_text(html)
    print(f"[ok] rebuilt docs/index.html with {len(entries)} preview(s)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", nargs="?", help="output/ folder to publish")
    ap.add_argument("--all", action="store_true", help="republish every output/ folder")
    args = ap.parse_args()

    DOCS.mkdir(exist_ok=True)
    PREVIEWS.mkdir(exist_ok=True)

    targets = []
    if args.all:
        targets = sorted(p.name for p in OUTPUT.iterdir() if p.is_dir() and not p.name.startswith("."))
    elif args.folder:
        targets = [args.folder]
    else:
        ap.error("provide a folder name or --all")

    entries = []
    for t in targets:
        e = publish_one(t)
        if e:
            entries.append(e)

    if args.all:
        # rebuild index from the full set of entries
        rebuild_index(entries)
    else:
        # rebuild index from the union of newly published + existing previews
        existing = []
        for d in PREVIEWS.iterdir() if PREVIEWS.exists() else []:
            slug = d.name
            article_path = OUTPUT
            for out in OUTPUT.iterdir():
                if (out / "article.json").exists():
                    a = json.loads((out / "article.json").read_text())
                    if a.get("slug") == slug:
                        existing.append({
                            "slug": slug,
                            "title": a["title"],
                            "date": a["date"],
                            "categories": a.get("categories", []),
                            "author": a.get("author", ""),
                            "excerpt": a.get("excerpt", ""),
                            "folder": out.name,
                        })
                        break
        # union by slug (newly-published wins)
        by_slug = {e["slug"]: e for e in existing}
        for e in entries:
            by_slug[e["slug"]] = e
        rebuild_index(list(by_slug.values()))

    return 0


if __name__ == "__main__":
    sys.exit(main())
