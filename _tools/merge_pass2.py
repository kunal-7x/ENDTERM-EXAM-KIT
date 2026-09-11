"""Pass 2: apply unused TB/C/S/NOTE blocks; clean leftover anchors; rename files."""
import re, os, glob, sys
sys.path.insert(0, r"C:\Users\kunal\Desktop\ENDTERM\EXAM-KIT\_tools")
from merge_extras import parse_extras, render_block

ROOT = r"C:\Users\kunal\Desktop\ENDTERM\EXAM-KIT"
PP = os.path.join(ROOT, "papers")

# 1. re-run main merge for gapfill file
all_blocks = {}
for ef in glob.glob(os.path.join(ROOT, "_tools", "extra-*.md")):
    all_blocks.update(parse_extras(ef))

from merge_extras import apply
used_all = set()
for pf in sorted(glob.glob(os.path.join(PP, "*", "*.md"))):
    used, _ = apply(pf, all_blocks, None)
    used_all |= used

# 2. second pass: unused blocks with TB/C/S/NOTE -> append to matching Q section
unused = {k: v for k, v in all_blocks.items() if k not in used_all}
print("unused total:", len(unused))
appended = 0
for (subj, p, q), items in sorted(unused.items()):
    keep = [(k, v) for k, v in items if k in ("TB", "C", "C+", "S", "NOTE")]
    if not keep:
        continue
    # find paper file for (subj, p): match by ## Q header presence
    cands = sorted(glob.glob(os.path.join(PP, subj, "*.md")))
    target = None
    for pf in cands:
        txt = open(pf, encoding="utf-8").read()
        if re.search(r"^## Q%d \u00b7" % q, txt, re.M):
            # verify paper index matches filename order
            target = pf
            break
    if not target:
        print("  NO-TARGET:", subj, p, q)
        continue
    rendered = render_block(keep)
    # drop OPTS/STEM/ACC tuples (JSON already has them)
    rendered = [r for r in rendered if isinstance(r, str)]
    if not rendered:
        continue
    lines = open(target, encoding="utf-8").read().split("\n")
    # locate section end: after ## Q header, before next ## Q or EOF
    start = next(i for i, l in enumerate(lines) if re.match(r"^## Q%d \u00b7" % q, l))
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("## Q"):
            end = i
            break
    # avoid duplicate tables
    section_text = "\n".join(lines[start:end])
    if keep and keep[0][0] == "TB" and "|---" in section_text:
        continue
    lines[start:end] = lines[start:end] + [""] + rendered
    open(target, "w", encoding="utf-8").write("\n".join(lines))
    appended += 1
print("appended blocks:", appended)

# 3. clean leftover anchors
FAILSAFE = "*[figure/code image — see kit engine pattern]*"
cleaned = 0
for pf in sorted(glob.glob(os.path.join(PP, "*", "*.md"))):
    lines = open(pf, encoding="utf-8").read().split("\n")
    out = []
    cur_q = None
    cur_type = ""
    # first pass: map sections
    for i, l in enumerate(lines):
        m = re.match(r"^## Q(\d+) \u00b7 `[^`]+` \u00b7 (\w+)", l)
        if m:
            cur_q, cur_type = int(m.group(1)), m.group(2)
        if l.strip() == FAILSAFE:
            # gather section stats
            j = len(out) - 1
            stem_len, bullets, has_table, has_code, has_acc = 0, 0, False, False, False
            while j >= 0 and not out[j].startswith("## Q"):
                if out[j].startswith("- "):
                    bullets += 1
                if "|---" in out[j]:
                    has_table = True
                if out[j].strip() == "```":
                    has_code = True
                if "Accepted answer (paper key)" in out[j]:
                    has_acc = True
                if not out[j].startswith(("**", "##", "- ", "```", "*[", "")) :
                    stem_len += len(out[j])
                elif out[j] and not out[j].startswith(("*[", "**Options", "**Accepted", "**Data", "**Code", "```")):
                    stem_len += len(out[j])
                j -= 1
            drop = False
            if cur_q == 1:
                drop = True  # boilerplate confirmation Q
            elif stem_len > 80 and (bullets >= 2 or cur_type in ("SA",) or has_table or has_code or has_acc):
                drop = True
            elif cur_type == "COMPREHENSION" and (has_table or has_code or stem_len > 80):
                drop = True
            if drop:
                cleaned += 1
                continue
        out.append(l)
    open(pf, "w", encoding="utf-8").write("\n".join(out))
print("failsafe notes dropped (complete sections):", cleaned)

# 4. renames
ren = {
    "BA/01-2022.md": "BA/01-2022-aug.md", "BA/02-2022.md": "BA/02-2022-dec.md",
    "BA/03-2023.md": "BA/03-2023-apr30.md", "BA/04-2023.md": "BA/04-2023-dec24.md",
    "BA/05-2023.md": "BA/05-2023-sep03.md", "BA/06-2024.md": "BA/06-2024-apr28.md",
    "BA/07-2024.md": "BA/07-2024-dec22.md", "BA/08-2024.md": "BA/08-2024-sep01.md",
    "BA/09-2025.md": "BA/09-2025-apr13.md", "BA/10-2025.md": "BA/10-2025-aug31.md",
    "BA/11-busi.md": "BA/11-2026-may06.md",
    "MAD2/10-modern-applicat.md": "MAD2/10-2026-may06.md",
    "MAD2/11-modern-applicat.md": "MAD2/11-2025-dec18.md",
}
for a, b in ren.items():
    sa, sb = os.path.join(PP, a), os.path.join(PP, b)
    if os.path.exists(sa):
        os.rename(sa, sb)
        print("renamed:", a, "->", b)

# 5. final residue report
for pf in sorted(glob.glob(os.path.join(PP, "*", "*.md"))):
    txt = open(pf, encoding="utf-8").read()
    anchors = re.findall(r"\[\[EXTRA:[^\]]+\]\]", txt)
    notes = txt.count(FAILSAFE)
    nq = len(re.findall(r"^## Q", txt, re.M))
    print(f"{os.path.basename(os.path.dirname(pf))}/{os.path.basename(pf)}: {nq}q anchors={len(anchors)} notes={notes}")
