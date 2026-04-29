#!/usr/bin/env python3
"""
Pick the next topic for the engine to write.

Tiebreaker order:
  1. P0 by ID ascending
  2. P1 with Quick win == 'Y' by ID ascending
  3. P1 by ID ascending
  4. P2 by ID ascending
  5. P3 by ID ascending

Skips rows whose Status is anything other than empty/None/Backlog.

Usage:
    python3 scripts/pick_next_topic.py            # prints the next topic JSON
    python3 scripts/pick_next_topic.py --id 34    # prints topic with that ID
    python3 scripts/pick_next_topic.py --list 5   # prints next 5 in queue order
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ROADMAP = ROOT / "data" / "roadmap.json"


def is_open(row):
    status = (row.get("Status") or "").strip().lower()
    return status in ("", "backlog", "none")


def queue_order(roadmap):
    p0 = [r for r in roadmap if r.get("Priority") == "P0" and is_open(r)]
    p1_qw = [r for r in roadmap if r.get("Priority") == "P1" and r.get("Quick win") == "Y" and is_open(r)]
    p1 = [r for r in roadmap if r.get("Priority") == "P1" and r.get("Quick win") != "Y" and is_open(r)]
    p2 = [r for r in roadmap if r.get("Priority") == "P2" and is_open(r)]
    p3 = [r for r in roadmap if r.get("Priority") == "P3" and is_open(r)]
    for bucket in (p0, p1_qw, p1, p2, p3):
        bucket.sort(key=lambda r: int(r.get("ID") or 99999))
    return p0 + p1_qw + p1 + p2 + p3


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", type=int, help="pick the topic with this ID")
    ap.add_argument("--list", type=int, default=0, help="print next N topics in queue order")
    args = ap.parse_args()

    data = json.loads(ROADMAP.read_text())
    roadmap = data["roadmap"]

    if args.id is not None:
        for r in roadmap:
            if int(r.get("ID") or -1) == args.id:
                print(json.dumps(r, indent=2, default=str))
                return 0
        print(f"No topic with ID {args.id}", file=sys.stderr)
        return 1

    queue = queue_order(roadmap)

    if args.list:
        for r in queue[: args.list]:
            qw = " [QW]" if r.get("Quick win") == "Y" else ""
            print(f"  #{r['ID']:>2}  {r['Priority']}{qw:<5}  [{r.get('Cluster','?')}]  {r['Topic']}")
        return 0

    if not queue:
        print("Queue is empty — every topic has a Status set.", file=sys.stderr)
        return 1

    print(json.dumps(queue[0], indent=2, default=str))
    return 0


if __name__ == "__main__":
    sys.exit(main())
