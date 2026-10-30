#!/usr/bin/env python3
"""Plan a preflight run: drop checks the app profile rules out, batch the rest.

Usage: python3 -I plan_checks.py <checks.json> <profile.json> <run_dir> [--only <path-prefix> ...] [--batch-size N]

A check is skipped only when its unit carries "**Requires:** a, b" (taken from
Apple's stated scope) and the profile explicitly lists EVERY one of those flags
under notFlags. Unknown or unmentioned flags never skip anything. Each skipped
check is written to <run_dir>/verdicts/skipped.json as NA with the reason, so
the report shows why it was not evaluated by an agent.

Writes <run_dir>/plan.json and prints a summary.
"""
import json
import os
import sys

# Which App Store Connect browser agent handles which reference files (path prefixes).
ASC_GROUPS = {
    "app": ["guidelines/", "asc/metadata-and-media.md", "asc/product-page-extras.md",
            "asc/platforms-and-app-types.md", "asc/app-review-help.md"],
    "privacy": ["asc/app-privacy-details.md", "asc/privacy-manifests.md",
                "asc/submission-and-compliance.md", "asc/accounts-permissions-technical.md"],
    "monetization": ["asc/iap-and-subscriptions.md", "asc/iap-pricing-and-operations.md",
                     "asc/agreements-pricing-availability.md", "asc/testflight-builds-statuses.md"],
}


def main():
    args = sys.argv[1:]
    if len(args) < 3:
        print(__doc__)
        sys.exit(2)
    checks_path, profile_path, run_dir = args[:3]
    only = [args[i + 1] for i, a in enumerate(args) if a == "--only" and i + 1 < len(args)]
    batch_size = int(args[args.index("--batch-size") + 1]) if "--batch-size" in args else 20

    checks = json.load(open(checks_path, encoding="utf-8"))["checks"]
    profile = json.load(open(profile_path, encoding="utf-8"))
    present = set(profile.get("flags", []))
    ruled_out = set(profile.get("notFlags", [])) - present
    evidence = profile.get("evidence", {}) or {}

    kept, skipped = [], []
    for c in checks:
        if only and not any(c["file"].startswith(p) for p in only):
            continue
        req = c.get("requires") or []
        if req and all(f in ruled_out for f in req):
            why = "; ".join(f"{f}: {evidence[f]}" for f in req if evidence.get(f))
            skipped.append({
                "id": c["id"], "verdict": "NA", "evidence": why,
                "location": "", "fixable": False, "fixPlan": "",
                "reason": f"Applies only to apps with {', '.join(req)} (Apple's stated scope); "
                          f"the app profile rules {'it' if len(req) == 1 else 'all of them'} out.",
            })
        else:
            kept.append(c)

    batches, by_file = [], {}
    for c in kept:
        if c["surface"] != "asc":
            by_file.setdefault(c["file"], []).append(c["id"])
    for file, ids in by_file.items():
        for i in range(0, len(ids), batch_size):
            batches.append({"file": file, "checkIds": ids[i:i + batch_size]})

    asc = {g: [c["id"] for c in kept if c["surface"] == "asc" and any(c["file"].startswith(p) for p in prefixes)]
           for g, prefixes in ASC_GROUPS.items()}
    runtime = [c["id"] for c in kept if c["surface"] == "runtime"]

    os.makedirs(os.path.join(run_dir, "verdicts"), exist_ok=True)
    with open(os.path.join(run_dir, "verdicts", "skipped.json"), "w", encoding="utf-8") as f:
        json.dump(skipped, f, indent=1)
    plan = {"batches": batches, "asc": asc, "runtime": runtime,
            "counts": {"total": len(checks), "inScope": len(kept) + len(skipped), "kept": len(kept),
                       "skippedByProfile": len(skipped), "batches": len(batches),
                       "asc": sum(len(v) for v in asc.values()), "runtime": len(runtime)}}
    with open(os.path.join(run_dir, "plan.json"), "w", encoding="utf-8") as f:
        json.dump(plan, f, indent=1)
    print(json.dumps(plan["counts"]))


if __name__ == "__main__":
    main()
