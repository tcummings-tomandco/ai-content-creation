#!/usr/bin/env python3
"""
Record the result of a successful publish run in data/roadmap.json.

After scripts/push_to_storyblok.py creates the draft story, the routine
calls this to stamp:

- Status               = "Approved — draft in Storyblok"
- Owner                = "Routine"
- Target publish date  = today (YYYY-MM-DD)
- Notes                = "Storyblok story <id> at <full_slug>"

The xlsx remains the source of truth for editing — this script writes only
the working JSON copy. Tom syncs the xlsx by hand at his convenience.

Usage:
    python3 scripts/mark_topic_done.py 34 \\
        --slug uk-ai-regulation-2026-principles-based-field-guide \\
        --storyblok-id 12345678 \\
        --storyblok-full-slug blog/uk-ai-regulation-2026-principles-based-field-guide
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "data" / "roadmap.json"


def today_str() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("id", type=int, help="Roadmap topic ID (column 'ID')")
    ap.add_argument("--slug", required=True, help="article slug, for the Notes field")
    ap.add_argument("--storyblok-id", type=int,
                    help="Storyblok story ID returned by push_to_storyblok.py")
    ap.add_argument("--storyblok-full-slug",
                    help="Storyblok full_slug, e.g. blog/uk-ai-regulation-...")
    ap.add_argument("--status",
                    default="Approved — draft in Storyblok",
                    help="value to write to the Status column")
    args = ap.parse_args()

    if not ROADMAP.exists():
        raise SystemExit(f"roadmap.json not found: {ROADMAP}")

    data = json.loads(ROADMAP.read_text())
    rows = data.get("roadmap", [])

    matched = None
    for r in rows:
        if int(r.get("ID") or -1) == args.id:
            matched = r
            break
    if not matched:
        raise SystemExit(f"No topic with ID {args.id} in roadmap.json")

    notes_parts = [f"slug: {args.slug}"]
    if args.storyblok_id is not None:
        notes_parts.append(f"Storyblok story {args.storyblok_id}")
    if args.storyblok_full_slug:
        notes_parts.append(f"at /{args.storyblok_full_slug}")

    previous_status = matched.get("Status")
    matched["Status"] = args.status
    matched["Owner"] = "Routine"
    matched["Target publish date"] = today_str()
    matched["Notes"] = "; ".join(notes_parts)
    # Persist the slug as its own field so downstream tooling (the
    # publish-to-storyblok Action) can map a roadmap row to its output
    # folder without parsing the free-text Notes.
    matched["Slug"] = args.slug

    ROADMAP.write_text(json.dumps(data, indent=2, default=str))

    print(f"[ok] topic #{args.id} marked {args.status!r}")
    print(f"     was: {previous_status or '(empty)'}")
    print(f"     now: {matched['Status']}")
    print(f"     notes: {matched['Notes']}")
    print()
    print(f"Remember to mirror this to Tom&Co_AI_Content_Roadmap.xlsx when you next "
          f"touch the spreadsheet (xlsx is the canonical source).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
