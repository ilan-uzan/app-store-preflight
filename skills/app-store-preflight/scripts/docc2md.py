#!/usr/bin/env python3
"""Render Apple DocC JSON (developer.apple.com/tutorials/data/documentation/*.json) as plain text.

Usage: python3 -I docc2md.py <page.json>
"""
import json
import sys


def inline(items, refs):
    out = []
    for it in items or []:
        t = it.get("type")
        if t == "text":
            out.append(it.get("text", ""))
        elif t == "codeVoice":
            out.append(it.get("code", ""))
        elif t in ("emphasis", "strong", "newTerm", "inlineHead", "superscript", "subscript", "strikethrough"):
            out.append(inline(it.get("inlineContent"), refs))
        elif t == "reference":
            ref = refs.get(it.get("identifier"), {})
            out.append(inline(it.get("overridingTitleInlineContent"), refs) if it.get("overridingTitleInlineContent")
                       else ref.get("title") or it.get("overridingTitle") or ref.get("url", ""))
        elif t == "link":
            out.append(it.get("title") or it.get("destination", ""))
        elif t == "image":
            pass
    return "".join(out)


def blocks(items, refs, out, depth=0):
    for b in items or []:
        t = b.get("type")
        if t == "paragraph":
            out.append(inline(b.get("inlineContent"), refs))
        elif t == "heading":
            out.append("#" * min(6, b.get("level", 2) + 1) + " " + b.get("text", ""))
        elif t == "aside":
            label = b.get("name") or (b.get("style") or "note").capitalize()
            sub = []
            blocks(b.get("content"), refs, sub, depth)
            out.append(f"[{label}]")
            out.append(f"{label}: " + " ".join(sub))
        elif t in ("unorderedList", "orderedList"):
            for k, item in enumerate(b.get("items", []), b.get("start", 1)):
                sub = []
                blocks(item.get("content"), refs, sub, depth + 1)
                out.append((f"{k}. " if t == "orderedList" else "- ") + " ".join(sub))
        elif t == "links":
            for ident in b.get("items", []):
                r = refs.get(ident, {})
                out.append(f"- {r.get('title', '')}: {inline(r.get('abstract'), refs)}")
        elif t == "codeListing":
            out.append("\n".join(b.get("code", [])))
        elif t == "table":
            for row in b.get("rows", []):
                cells = []
                for c in row:
                    sub = []
                    blocks(c, refs, sub, depth + 1)
                    cells.append(" ".join(sub))
                out.append("| " + " | ".join(cells) + " |")
        elif t == "termList":
            for item in b.get("items", []):
                term = inline(item.get("term", {}).get("inlineContent"), refs)
                sub = []
                blocks(item.get("definition", {}).get("content"), refs, sub, depth + 1)
                out.append(f"{term}: " + " ".join(sub))
        elif "content" in b:
            blocks(b.get("content"), refs, out, depth)


def main():
    d = json.load(open(sys.argv[1], encoding="utf-8"))
    refs = d.get("references", {})
    out = ["# " + d.get("metadata", {}).get("title", "")]
    out.append(inline(d.get("abstract"), refs))
    meta = d.get("metadata", {})
    plats = [f"{p.get('name')} {p.get('introducedAt', '')}".strip() for p in meta.get("platforms", [])]
    if plats:
        out.append(", ".join(plats))
    for sec in d.get("primaryContentSections", []):
        if sec.get("kind") == "content":
            blocks(sec.get("content"), refs, out)
        elif sec.get("kind") in ("details", "plistDetails") or "ideTitle" in sec.get("details", {}):
            det = sec.get("details", sec)
            for k in ("name", "ideTitle", "titleStyle"):
                if det.get(k):
                    out.append(f"{k}: {det[k]}")
            for v in det.get("value", []) if isinstance(det.get("value"), list) else []:
                out.append(str(v.get("baseType", "")) if isinstance(v, dict) else str(v))
        elif sec.get("kind") == "possibleValues":
            out.append("## " + sec.get("title", "Possible Values"))
            for val in sec.get("values", []):
                out.append("### " + val.get("name", ""))
                blocks(val.get("content"), refs, out)
        elif sec.get("tokens"):
            out.append(f"{sec.get('title', '')}: " + "".join(t.get("text", "") for t in sec["tokens"]))
        elif sec.get("kind") == "properties" or sec.get("items"):
            for item in sec.get("items", []):
                sub = []
                blocks(item.get("content"), refs, sub)
                head = item.get("name") or str(item.get("status", "")) + " " + str(item.get("reason", ""))
                out.append(f"{head}: " + " ".join(sub))
    for sec in d.get("topicSections", []) + d.get("seeAlsoSections", []):
        out.append("## " + sec.get("title", ""))
        for ident in sec.get("identifiers", []):
            r = refs.get(ident, {})
            out.append(f"- {r.get('title', '')}: {inline(r.get('abstract'), refs)}")
    print("\n\n".join(x for x in out if x is not None))


if __name__ == "__main__":
    main()
