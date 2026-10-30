#!/usr/bin/env python3
"""Merge a preflight run directory into PREFLIGHT_REPORT.md and results.json.

Usage: python3 -I render_report.py <run_dir> <checks.json> <guidelines_source.md>

Reads from <run_dir>:
  profile.json                 app profile (optional)
  verdicts/*.json              arrays of {id, verdict, evidence, location, reason, fixable, fixPlan}
  verdicts/verify-*.json       {id, upheld, correctedVerdict, reason}
  fixes/*.json                 arrays of {id, status, files, summary, howToVerify, reverified}
Writes <run_dir>/results.json and <run_dir>/PREFLIGHT_REPORT.md.
"""
import glob
import json
import os
import re
import sys

ICON = {"PASS": "✅", "FAIL": "❌", "WARN": "⚠️", "NA": "➖", "MANUAL": "✋", "ASC": "🌐",
        "FIXED": "🔧", "SKIPPED": "⏭️", "UNKNOWN": "❔"}
ORDER = ["FAIL", "WARN", "ASC", "MANUAL", "FIXED", "PASS", "NA", "SKIPPED", "UNKNOWN"]


def load(path, default):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError):
        return default


def cell(text, limit=220):
    text = re.sub(r"\s+", " ", str(text or "")).replace("|", "\\|").strip()
    return text if len(text) <= limit else text[: limit - 1] + "…"


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(2)
    run_dir, checks_path, source_md = sys.argv[1:]
    catalog = load(checks_path, {"checks": []})
    checks = {c["id"]: c for c in catalog["checks"]}
    profile = load(os.path.join(run_dir, "profile.json"), {})
    bad_files = []

    verdicts = {}
    for path in sorted(glob.glob(os.path.join(run_dir, "verdicts", "*.json"))):
        if os.path.basename(path).startswith("verify-"):
            continue
        data = load(path, None)
        if not isinstance(data, list):
            bad_files.append(os.path.relpath(path, run_dir))
            continue
        for v in data:
            if isinstance(v, dict) and v.get("id") in checks:
                prev = verdicts.get(v["id"])
                # A definite verdict (e.g. from the ASC or runtime pass) replaces a deferral.
                if prev is None or prev.get("verdict") in ("ASC", "MANUAL", "UNKNOWN", None):
                    verdicts[v["id"]] = v

    for path in glob.glob(os.path.join(run_dir, "verdicts", "verify-*.json")):
        v = load(path, None)
        if not isinstance(v, dict) or v.get("id") not in verdicts:
            continue
        verdicts[v["id"]]["verification"] = v
        if v.get("upheld") is False and v.get("correctedVerdict"):
            verdicts[v["id"]]["originalVerdict"] = verdicts[v["id"]]["verdict"]
            verdicts[v["id"]]["verdict"] = v["correctedVerdict"]

    fixes = {}
    reverify = {}
    for path in glob.glob(os.path.join(run_dir, "fixes", "reverify-*.json")):
        v = load(path, None)
        if isinstance(v, dict) and v.get("id"):
            reverify[v["id"]] = v
    for path in sorted(glob.glob(os.path.join(run_dir, "fixes", "fix-*.json"))):
        data = load(path, None)
        if not isinstance(data, list):
            bad_files.append(os.path.relpath(path, run_dir))
            continue
        for f in data:
            if isinstance(f, dict) and f.get("id"):
                fixes[f["id"]] = f
    for cid, f in fixes.items():
        if cid in reverify:
            f["reverified"] = bool(reverify[cid].get("reverified"))
            f["reverifyNotes"] = reverify[cid].get("notes", "")
        if cid in verdicts and f.get("status") == "fixed" and f.get("reverified"):
            verdicts[cid]["fixedFrom"] = verdicts[cid]["verdict"]
            verdicts[cid]["verdict"] = "FIXED"

    results = []
    for cid, c in checks.items():
        v = verdicts.get(cid, {})
        default = "ASC" if c["surface"] == "asc" else "UNKNOWN"  # browser pass skipped: the developer checks these
        results.append({**c, "verdict": v.get("verdict", default), "evidence": v.get("evidence", ""),
                        "location": v.get("location", ""), "reason": v.get("reason", ""),
                        "fixPlan": v.get("fixPlan", ""), "fix": fixes.get(cid), "verification": v.get("verification")})
    with open(os.path.join(run_dir, "results.json"), "w", encoding="utf-8") as f:
        json.dump({"profile": profile, "results": results}, f, indent=2)

    counts = {k: 0 for k in ORDER}
    for r in results:
        counts[r["verdict"] if r["verdict"] in counts else "UNKNOWN"] += 1

    updated = ""
    try:
        m = re.search(r"Last Updated:\s*(.+)", open(source_md, encoding="utf-8").read())
        updated = m.group(1).strip() if m else ""
    except OSError:
        pass

    if counts["FAIL"]:
        status = f"❌ NOT READY — {counts['FAIL']} failed check(s) to fix"
    elif counts["WARN"] or counts["ASC"] or counts["MANUAL"] or counts["UNKNOWN"]:
        status = "⚠️ READY AFTER YOU CONFIRM THE ITEMS BELOW"
    else:
        status = "✅ READY TO SUBMIT"

    out = []
    w = out.append
    w(f"# App Store Preflight Report — {profile.get('appName', 'Your app')}\n")
    w(f"**Status:** {status}  ")
    w(f"**Guidelines version:** App Review Guidelines, Last Updated {updated or 'unknown'}  ")
    w(f"**Checks evaluated:** {len(results)}\n")
    w("| " + " | ".join(f"{ICON[k]} {k}" for k in ORDER if counts[k]) + " |")
    w("|" + "---|" * sum(1 for k in ORDER if counts[k]))
    w("| " + " | ".join(str(counts[k]) for k in ORDER if counts[k]) + " |\n")
    w("Legend: ✅ pass · ❌ fail (rejection risk) · ⚠️ warning · 🌐 needs App Store Connect check · "
      "✋ only you can confirm · 🔧 fixed by preflight · ➖ not applicable · ❔ not evaluated\n")
    if bad_files:
        w(f"> ⚠️ Unreadable result files (their checks show as ❔): {', '.join(bad_files)}\n")
    if profile.get("summary"):
        w(f"**App profile:** {profile['summary']}\n")

    def table(title, rows, cols, collapsed=False):
        if not rows:
            return
        if collapsed:
            w(f"<details><summary><b>{title}</b> ({len(rows)})</summary>\n")
        else:
            w(f"## {title}\n")
        w("| " + " | ".join(h for h, _ in cols) + " |")
        w("|" + "---|" * len(cols))
        for r in rows:
            w("| " + " | ".join(cell(fn(r)) for _, fn in cols) + " |")
        w("\n</details>\n" if collapsed else "")

    def issue_key(r):
        # Findings that cite the same place are one issue: first path[:line] or App Store Connect location.
        loc = (r["location"] or r["evidence"] or "").strip()
        first = re.split(r"[;,]| and ", loc)[0].strip().lower()
        m = re.match(r"([\w./ +-]+\.[a-z0-9]+)(?::(\d+))?", first)
        return f"{m.group(1)}:{m.group(2) or ''}" if m else (first or r["id"])

    def grouped(rows):
        groups = {}
        for r in rows:
            groups.setdefault(issue_key(r), []).append(r)
        return sorted(groups.values(), key=lambda g: (-len(g), g[0]["id"]))

    gl = lambda r: f"{r['unit']} {r['unitTitle']}"
    ids = lambda g: ", ".join(x["id"] for x in g)
    gls = lambda g: "; ".join(dict.fromkeys(gl(x) for x in g))
    fails = grouped([r for r in results if r["verdict"] == "FAIL"])
    warns = grouped([r for r in results if r["verdict"] == "WARN"])
    fails_n = sum(len(g) for g in fails)
    if fails:
        w(f"## ❌ Blocking issues: {len(fails)} issue(s) from {fails_n} failed check(s)\n")
        w("Fix these before submitting. Checks that cite the same place are merged into one issue.\n")
        w("| # | Issue | Guideline(s) | Evidence | How to fix | Checks |")
        w("|---|---|---|---|---|---|")
        for i, g in enumerate(fails, 1):
            r = g[0]
            w(f"| {i} | {cell(r['reason'] or r['question'])} | {cell(gls(g), 120)} | {cell(r['location'] or r['evidence'], 120)} | "
              f"{cell(r['fixPlan'] or r['fix'])} | {cell(ids(g), 80)} |")
        w("")
    table("🔧 Fixed by preflight", [r for r in results if r["verdict"] == "FIXED"],
          [("Check", lambda r: r["id"]), ("Guideline", gl), ("Change", lambda r: (r["fix"] or {}).get("summary", "")),
           ("Files", lambda r: ", ".join((r["fix"] or {}).get("files", []))),
           ("Verify by", lambda r: (r["fix"] or {}).get("howToVerify", ""))])
    if warns:
        w(f"## ⚠️ Warnings: {len(warns)} issue(s)\n")
        w("Probable problems or Apple \"should\" advice not followed. Confirmed ones first.\n")
        w("| Issue | Guideline(s) | Evidence | Status | Checks |")
        w("|---|---|---|---|---|")
        for g in sorted(warns, key=lambda g: (not any((x.get("verification") or {}).get("upheld") for x in g), -len(g))):
            r = g[0]
            status_w = "✔ skeptic upheld" if any((x.get("verification") or {}).get("upheld") for x in g) else "not cross-examined"
            w(f"| {cell(r['reason'] or r['question'])} | {cell(gls(g), 100)} | {cell(r['location'] or r['evidence'], 100)} | {status_w} | {cell(ids(g), 60)} |")
        w("")
    table("🌐 Check in App Store Connect", [r for r in results if r["verdict"] == "ASC"],
          [("Check", lambda r: r["id"]), ("Guideline", gl), ("What to confirm", lambda r: r["reason"] or r["question"]),
           ("Where", lambda r: r["verify"])], collapsed=True)
    table("✋ Only you can confirm", [r for r in results if r["verdict"] == "MANUAL"],
          [("Check", lambda r: r["id"]), ("Guideline", gl), ("Question", lambda r: r["reason"] or r["question"])], collapsed=True)
    unknown = [r for r in results if r["verdict"] == "UNKNOWN"]
    if unknown:
        files = {}
        for r in unknown:
            files[r["file"]] = files.get(r["file"], 0) + 1
        w("## ❔ Not evaluated\n")
        w(f"{len(unknown)} checks have no verdict (an audit batch was skipped or failed). Re-run the preflight to cover them:\n")
        for f, n in sorted(files.items()):
            w(f"- `{f}`: {n}")
        w("")

    if profile.get("reviewNotesDraft"):
        w("## Draft notes for App Review\n")
        w("Paste into App Store Connect → your version → App Review Information → Notes (edit first):\n")
        w("```\n" + profile["reviewNotesDraft"].strip() + "\n```\n")

    w("## Full checklist\n")
    w("<details><summary>Every check, grouped by guideline</summary>\n")
    by_file = {}
    for r in results:
        by_file.setdefault(r["file"], []).append(r)
    for file, rows in by_file.items():
        w(f"\n### {file}\n")
        w("| | Check | Guideline | Question | Evidence |")
        w("|---|---|---|---|---|")
        for r in rows:
            w(f"| {ICON.get(r['verdict'], '❔')} | {r['id']} | {cell(gl(r), 60)} | {cell(r['question'], 160)} | "
              f"{cell(r['location'] or r['evidence'] or r['reason'], 140)} |")
    w("\n</details>\n")
    w("---\nGenerated by [app-store-preflight](https://github.com/ilan-uzan/app-store-preflight). "
      "This report does not guarantee approval; App Review makes the final decision.")

    path = os.path.join(run_dir, "PREFLIGHT_REPORT.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print(json.dumps({"report": path, "status": status, "counts": counts}, indent=2))


if __name__ == "__main__":
    main()
