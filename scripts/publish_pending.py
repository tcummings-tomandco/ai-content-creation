#!/usr/bin/env python3
"""
Publish roadmap topics that are marked "Draft pending Storyblok" to the
Tom & Co Storyblok space as draft stories.

This is the publishing half of the Option B pipeline:
- The cloud routine WRITES the article (output/{folder}/) and marks the
  roadmap row Status = "Draft pending Storyblok", then commits to the repo.
- This script (run by the publish-to-storyblok GitHub Action) reads those
  pending rows and pushes each article to Storyblok, then flips the row to
  "Approved — draft in Storyblok" with the story id.

Secrets come from the environment (GitHub Actions secrets). Locally it falls
back to variables.env via push_to_storyblok.load_env.

Idempotent: if a story already exists at the target slug, it is not
re-created — the roadmap row is just reconciled to the existing story id.

Env: STORYBLOK_OAUTH_TOKEN, STORYBLOK_SPACE_ID, STORYBLOK_REGION (default eu)

Usage:
    python3 scripts/publish_pending.py
    python3 scripts/publish_pending.py --dry-run
"""
import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from push_to_storyblok import (  # noqa: E402
    build_story_payload,
    find_or_resolve_parent_id,
    find_story_by_slug,
    api_request,
    load_env,
)

ROADMAP = ROOT / "data" / "roadmap.json"
OUTPUT = ROOT / "output"
PARENT_SLUG = "ai-agency-consultancy/blog"
CATEGORY_OVERRIDE = "Strategy"  # temporary until "AI" lands in the schema
PENDING_STATUS = "Draft pending Storyblok"
DONE_STATUS = "Approved — draft in Storyblok"


def today_str():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def find_output_folder_for_slug(slug):
    """Return the output/{folder} Path whose article.json has this slug."""
    if not OUTPUT.exists():
        return None
    for folder in sorted(OUTPUT.iterdir()):
        art = folder / "article.json"
        if art.exists():
            try:
                if json.loads(art.read_text()).get("slug") == slug:
                    return folder
            except json.JSONDecodeError:
                continue
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="list what would be published; do not call Storyblok or write roadmap")
    args = ap.parse_args()

    data = json.loads(ROADMAP.read_text())
    rows = data.get("roadmap", [])
    pending = [r for r in rows if (r.get("Status") or "").strip() == PENDING_STATUS]

    # Check for work BEFORE requiring credentials, so a push that touches
    # output/ or roadmap.json but has nothing pending exits cleanly even
    # before the Storyblok secrets are configured.
    if not pending:
        print("No topics in 'Draft pending Storyblok' state. Nothing to publish.")
        return 0

    print(f"Found {len(pending)} pending topic(s).")

    load_env(ROOT / "variables.env")  # no-op in Actions (env already set)
    token = os.environ.get("STORYBLOK_OAUTH_TOKEN", "").strip()
    space = os.environ.get("STORYBLOK_SPACE_ID", "").strip()
    region = os.environ.get("STORYBLOK_REGION", "eu").strip()

    if not args.dry_run and (not token or not space):
        print("Missing STORYBLOK_OAUTH_TOKEN / STORYBLOK_SPACE_ID. "
              "Add them to the repo's Actions secrets.", file=sys.stderr)
        return 1

    parent_id = None
    if not args.dry_run:
        parent_id = find_or_resolve_parent_id(
            parent_slug=PARENT_SLUG, token=token, region=region, space_id=space)

    published, reconciled, errors = [], [], []

    for row in pending:
        topic_id = row.get("ID")
        slug = (row.get("Slug") or "").strip()
        if not slug:
            errors.append((topic_id, "no Slug field on the roadmap row"))
            continue
        folder = find_output_folder_for_slug(slug)
        if folder is None:
            errors.append((topic_id, f"no output folder with slug {slug!r}"))
            continue

        full_slug = f"{PARENT_SLUG}/{slug}"

        if args.dry_run:
            print(f"  WOULD publish topic #{topic_id}: {slug}  (from {folder.name})")
            continue

        # Idempotency: if the story already exists, reconcile the roadmap row
        # to it rather than creating a duplicate.
        existing = find_story_by_slug(slug=slug, full_slug=full_slug,
                                      token=token, region=region, space_id=space)
        if existing:
            sid, fslug = existing["id"], existing.get("full_slug", full_slug)
            reconciled.append((topic_id, slug, sid))
        else:
            article = json.loads((folder / "article.json").read_text())
            payload = build_story_payload(article, article_path=folder / "article.json",
                                          parent_id=parent_id,
                                          category_override=CATEGORY_OVERRIDE)
            status, resp = api_request("POST", f"/v1/spaces/{space}/stories",
                                       body=payload, token=token, region=region)
            story = resp.get("story", {})
            sid, fslug = story.get("id"), story.get("full_slug", full_slug)
            published.append((topic_id, slug, sid))
            print(f"  [published] #{topic_id} {slug} -> story {sid}")

        # Flip the roadmap row to done with the story id.
        row["Status"] = DONE_STATUS
        row["Owner"] = "Routine"
        row["Target publish date"] = today_str()
        row["Notes"] = f"slug: {slug}; Storyblok story {sid}; at /{fslug}"

    if not args.dry_run:
        ROADMAP.write_text(json.dumps(data, indent=2, default=str))

    print()
    print(f"Published {len(published)}, reconciled {len(reconciled)} existing, "
          f"{len(errors)} error(s).")
    for tid, slug, sid in reconciled:
        print(f"  reconciled #{tid} {slug} -> existing story {sid}")
    for tid, msg in errors:
        print(f"  ERROR #{tid}: {msg}")

    # Surface errors as a non-zero exit so the Action run is marked failed.
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
