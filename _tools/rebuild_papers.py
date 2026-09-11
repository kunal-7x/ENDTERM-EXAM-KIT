"""Clean rebuild: regenerate BA/MAD2 bases, merge extras, correct second pass."""
import re, os, glob, shutil, sys
sys.path.insert(0, r"C:\Users\kunal\Desktop\ENDTERM\EXAM-KIT\_tools")
from merge_extras import parse_extras, render_block, apply

ROOT = r"C:\Users\kunal\Desktop\ENDTERM\EXAM-KIT"
PP = os.path.join(ROOT, "papers")

# files per subject in paper-index order
def paper_file(subj, p):
    files = sorted(glob.glob(os.path.join(PP, subj, "*.md")))
    return files[p - 1]

all_blocks = {}
for ef in glob.glob(os.path.join(ROOT, "_tools", "extra-*.md")):
    all_blocks.update(parse_extras(ef))
print("extras blocks:", len(all_blocks))

used_all = set()
for pf in sorted(glob.glob(os.path.join(PP, "*", "*.md"))):
    if "/MLP/" in pf.replace("\\", "/"):
        continue
    used, _ = apply(pf, all_blocks, None)
    used_all |= used
print("pass1 used:", len(used_all))

# correct second pass
unused = {k: v for k, v in all_blocks.items() if k not in used_all}
appended = 0
for (subj, p, q) in sorted(unused):
    items = unused[(subj, p, q)]
    keep = [(k, v) for k, v in items if k in ("TB", "C", "C+", "S", "NOTE")]
    if not keep:
        continue
    try:
        target = paper_file(subj, p)
    except IndexError:
        print("  NO-FILE:", subj, p, q)
        continue
    rendered = [r for r in render_block(keep) if isinstance(r, str)]
    if not rendered:
        continue
    lines = open(target, encoding="utf-8").read().split("\n")
    try:
        start = next(i for i, l in enumerate(lines) if re.match(r"^## Q%d \u00b7" % q, l))
    except StopIteration:
        print("  NO-Q:", subj, p, q)
        continue
    end = len(lines)
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("## Q"):
            end = i
            break
    section_text = "\n".join(lines[start:end])
    if keep[0][0] == "TB" and "|---" in section_text:
        continue
    # avoid re-adding identical code/note
    gevoeg = "\n".join(rendered)
    if gevoeg.strip() and gevoeg.strip() in section_text:
        continue
    lines[start:end] = lines[start:end] + [""] + rendered
    open(target, "w", encoding="utf-8").write("\n".join(lines))
    appended += 1
print("pass2 appended:", appended)

# anchor cleanup
FAILSAFE = "*[figure/code image — see kit engine pattern]*"
cleaned = kept = 0
for pf in sorted(glob.glob(os.path.join(PP, "*", "*.md"))):
    if "/MLP/" in pf.replace("\\", "/"):
        continue
    lines = open(pf, encoding="utf-8").read().split("\n")
    out = []
    cur_q, cur_type = None, ""
    for l in lines:
        m = re.match(r"^## Q(\d+) \u00b7 `[^`]+` \u00b7 (\w+)", l)
        if m:
            cur_q, cur_type = int(m.group(1)), m.group(2)
        if l.strip() == FAILSAFE:
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
                if out[j] and not out[j].startswith(("*[", "**Options", "**Accepted", "**Data", "**Code", "```")):
                    stem_len += len(out[j])
                j -= 1
            drop = (cur_q == 1) or (stem_len > 80 and (bullets >= 2 or cur_type == "SA" or has_table or has_code or has_acc)) or (cur_type == "COMPREHENSION" and (has_table or has_code or stem_len > 80))
            if drop:
                cleaned += 1
                continue
            kept += 1
        out.append(l)
    # also drop any surviving [[EXTRA]] markers (shouldn't be any)
    out = [l for l in out if not l.strip().startswith("[[EXTRA")]
    open(pf, "w", encoding="utf-8").write("\n".join(out))
print("failsafe dropped:", cleaned, "| kept (honest gaps):", kept)

for pf in sorted(glob.glob(os.path.join(PP, "*", "*.md"))):
    txt = open(pf, encoding="utf-8").read()
    nq = len(re.findall(r"^## Q", txt, re.M))
    print(f"{os.path.basename(os.path.dirname(pf))}/{os.path.basename(pf)}: {nq}q notes={txt.count(FAILSAFE)}")
