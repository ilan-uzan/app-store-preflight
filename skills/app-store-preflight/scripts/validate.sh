#!/usr/bin/env bash
# Repository checks: references parse, quotes are verbatim, workflow copies match, scripts compile.
set -euo pipefail
SKILL="$(cd "$(dirname "$0")/.." && pwd)"
ROOT="$(cd "$SKILL/../.." && pwd)"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
python3 -I "$SKILL/scripts/build_checks.py" "$SKILL/references" "$TMP/checks.json" --strict
python3 -I "$SKILL/scripts/verify_quotes.py" "$SKILL"
for f in "$SKILL"/references/data/*.json "$ROOT"/.claude-plugin/*.json; do python3 -I -m json.tool "$f" > /dev/null; done
python3 -I -m py_compile "$SKILL"/scripts/*.py
if [ -f "$ROOT/workflows/preflight.js" ]; then
  cmp -s "$SKILL/workflow/preflight.js" "$ROOT/workflows/preflight.js" || { echo "workflows/preflight.js differs from skills/app-store-preflight/workflow/preflight.js (run: cp skills/app-store-preflight/workflow/preflight.js workflows/)"; exit 1; }
fi
echo "All checks passed."
