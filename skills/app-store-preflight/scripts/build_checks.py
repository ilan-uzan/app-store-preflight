#!/usr/bin/env python3
"""Parse the reference check files into one machine-readable checks.json.

Usage: python3 -I build_checks.py <references_dir> <out.json> [--batch-size N] [--strict]

Each reference file holds units ("## <ID> <Title>") followed by checks:
    - **[CHECK-ID]** question
      - quote: "..."
      - surface: code | asc | runtime | manual
      - verify: ...
      - fix: ...
--strict exits non-zero on duplicate IDs or malformed checks (used by CI).
"""
import json
import os
import re
import sys

UNIT_RE = re.compile(r"^##\s+(\S+)\s+(.*)$")
CHECK_RE = re.compile(r"^- \*\*\[([^\]]+)\]\*\*\s+(.*)$")
FIELD_RE = re.compile(r"^\s+- (quote|surface|verify|fix):\s?(.*)$")
SURFACES = {"code", "asc", "runtime", "manual"}


def parse_file(path, rel):
    checks, errors = [], []
    unit_id, unit_title, current, field = None, None, None, None
    with open(path, encoding="utf-8") as f:
        lines = f.read().splitlines()
    for n, line in enumerate(lines, 1):
        m = UNIT_RE.match(line)
        if m:
            unit_id, unit_title, current, field = m.group(1), m.group(2).strip(), None, None
            continue
        m = CHECK_RE.match(line)
        if m:
            current = {"id": m.group(1).strip(), "file": rel, "line": n, "unit": unit_id,
                       "unitTitle": unit_title, "question": m.group(2).strip(),
                       "quote": "", "surface": "", "verify": "", "fix": ""}
            checks.append(current)
            field = None
            continue
        if current is None:
            continue
        m = FIELD_RE.match(line)
        if m:
            field = m.group(1)
            current[field] = m.group(2).strip()
            continue
        if field and line.startswith("    ") and line.strip():
            current[field] += " " + line.strip()
        elif not line.strip():
            field = None
    for c in checks:
        c["quote"] = c["quote"].strip().strip('"').strip("“”")
        c["surface"] = c["surface"].strip().strip("`").lower()
        if c["surface"] not in SURFACES:
            errors.append(f"{rel}:{c['line']} {c['id']}: surface '{c['surface']}' is not one of {sorted(SURFACES)}")
        if not c["quote"]:
            errors.append(f"{rel}:{c['line']} {c['id']}: missing quote")
    return checks, errors


def main():
    args = sys.argv[1:]
    strict = "--strict" in args
    batch_size = 20
    if "--batch-size" in args:
        batch_size = int(args[args.index("--batch-size") + 1])
    positional = [a for i, a in enumerate(args) if not a.startswith("--") and (i == 0 or args[i - 1] != "--batch-size")]
    if len(positional) != 2:
        print(__doc__)
        sys.exit(2)
    ref_dir, out_path = positional

    all_checks, errors = [], []
    for sub in ("guidelines", "asc"):
        folder = os.path.join(ref_dir, sub)
        for name in sorted(os.listdir(folder)):
            if name.endswith(".md"):
                checks, errs = parse_file(os.path.join(folder, name), f"{sub}/{name}")
                all_checks.extend(checks)
                errors.extend(errs)

    seen = {}
    for c in all_checks:
        if c["id"] in seen:
            errors.append(f"duplicate check id {c['id']} in {c['file']} and {seen[c['id']]}")
        seen[c["id"]] = c["file"]

    # Batches for the audit phase: code/runtime/manual checks, grouped per file.
    batches = []
    by_file = {}
    for c in all_checks:
        if c["surface"] != "asc":
            by_file.setdefault(c["file"], []).append(c["id"])
    for file, ids in by_file.items():
        for i in range(0, len(ids), batch_size):
            batches.append({"file": file, "checkIds": ids[i:i + batch_size]})

    out = {
        "checks": all_checks,
        "batches": batches,
        "ascCheckIds": [c["id"] for c in all_checks if c["surface"] == "asc"],
        "runtimeCheckIds": [c["id"] for c in all_checks if c["surface"] == "runtime"],
        "counts": {s: sum(1 for c in all_checks if c["surface"] == s) for s in sorted(SURFACES)},
        "total": len(all_checks),
        "errors": errors,
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print(json.dumps({"total": out["total"], "counts": out["counts"], "batches": len(batches),
                      "errors": len(errors)}, indent=2))
    for e in errors[:50]:
        print("ERROR:", e, file=sys.stderr)
    if strict and errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
