#!/usr/bin/env python3
"""Print the full definition of checks by ID (or every check of a surface).

Usage: python3 -I show_checks.py <checks.json> <ID> [<ID> ...]
       python3 -I show_checks.py <checks.json> --surface asc [--file asc/metadata-and-media.md --file guidelines/ ...]
       python3 -I show_checks.py <checks.json> --batch <N>     (the Nth audit batch in checks.json)
       python3 -I show_checks.py <checks.json> --plan <plan.json> --batch <N> | --asc-group <name> | --runtime
(--file matches a path prefix and may repeat)
"""
import json
import sys


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(2)
    with open(sys.argv[1], encoding="utf-8") as f:
        checks = json.load(f)["checks"]
    args = sys.argv[2:]
    if args[0] == "--plan":
        with open(args[1], encoding="utf-8") as f:
            plan = json.load(f)
        rest = args[2:]
        if rest[0] == "--batch":
            args = plan["batches"][int(rest[1])]["checkIds"]
        elif rest[0] == "--asc-group":
            args = plan["asc"][rest[1]]
        elif rest[0] == "--runtime":
            args = plan["runtime"]
        if not args:
            print("(no checks)")
            return
    elif args[0] == "--batch":
        with open(sys.argv[1], encoding="utf-8") as f:
            wanted_ids = json.load(f)["batches"][int(args[1])]["checkIds"]
        args = wanted_ids
    if args[0] == "--surface":
        surface = args[1]
        files = [args[i + 1] for i, a in enumerate(args) if a == "--file" and i + 1 < len(args)]
        chosen = [c for c in checks if c["surface"] == surface and (not files or any(c["file"].startswith(f) for f in files))]
    else:
        wanted = set(args)
        chosen = [c for c in checks if c["id"] in wanted]
        missing = wanted - {c["id"] for c in chosen}
        if missing:
            print("UNKNOWN IDS:", ", ".join(sorted(missing)), file=sys.stderr)
    for c in chosen:
        print(f"[{c['id']}] ({c['surface']}) {c['unit']} {c['unitTitle']}")
        print(f"  question: {c['question']}")
        print(f"  quote:    \"{c['quote']}\"")
        print(f"  verify:   {c['verify']}")
        print(f"  fix:      {c['fix']}")
        print(f"  source:   references/{c['file']}:{c['line']}\n")


if __name__ == "__main__":
    main()
