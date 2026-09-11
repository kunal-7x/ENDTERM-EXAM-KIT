"""Merge vision extras into papers/*.md at [[EXTRA:SUBJ:P:Q]] anchors."""
import re, os, glob

ROOT = r"C:\Users\kunal\Desktop\ENDTERM\EXAM-KIT"
PP = os.path.join(ROOT, "papers")
TP = os.path.join(ROOT, "_tools")


def parse_extras(path):
    blocks = {}
    cur = None
    mode = None
    for raw in open(path, encoding="utf-8").read().split("\n"):
        m = re.match(r"^@@(\w+)-(\d+)-(\d+)\s*$", raw)
        if m:
            cur = (m.group(1), int(m.group(2)), int(m.group(3)))
            blocks[cur] = []
            mode = None
            continue
        if cur is None:
            continue
        tm = re.match(r"^(TB|C|O|T|A|S|NOTE):\s?(.*)$", raw)
        if tm:
            mode = tm.group(1)
            blocks[cur].append((mode, tm.group(2)))
        elif raw.strip() == "":
            continue
        elif mode in ("C", "T", "NOTE"):
            blocks[cur].append((mode + "+", raw))
    return blocks


def render_block(items):
    out = []
    tb_rows = [v for k, v in items if k == "TB"]
    if tb_rows:
        out.append("**Data table:**")
        out.append("")
        out.append(tb_rows[0])
        ncols = tb_rows[0].count("|") - 1
        out.append("|" + "---|" * max(ncols, 1))
        out.extend(tb_rows[1:])
        out.append("")
    code = []
    for k, v in items:
        if k == "C":
            code.append(v)
        elif k == "C+":
            code.append(v)
    if code:
        out.append("**Code / figure:**")
        out.append("")
        out.append("```")
        out.extend(code)
        out.append("```")
        out.append("")
    for k, v in items:
        if k == "O":
            out.append(("OPTS", v))
        elif k == "T":
            out.append(("STEM", v))
        elif k == "A":
            out.append(("ACC", v))
        elif k == "S":
            out.append("*Solved in practice render (unofficial, verify with kit): %s*" % v)
            out.append("")
        elif k == "NOTE":
            out.append("*Note: %s*" % v)
            out.append("")
    return out


def apply(paper_path, blocks, key_prefix):
    lines = open(paper_path, encoding="utf-8").read().split("\n")
    used = set()
    orphans = []
    out = []
    # group file lines into Q sections by '## Q' headers + anchor lines
    i = 0
    remaining_anchors = []
    while i < len(lines):
        m = re.match(r"^\[\[EXTRA:(\w+):(\d+):(\d+)\]\]\s*$", lines[i])
        if m:
            key = (m.group(1), int(m.group(2)), int(m.group(3)))
            if key in blocks:
                # find current Q section option bullets count (scan back to ## Q)
                j = len(out) - 1
                bullets = 0
                has_acc = False
                has_stem_placeholder = False
                while j >= 0 and not out[j].startswith("## Q"):
                    if out[j].startswith("- "):
                        bullets += 1
                    if "Accepted answer (paper key)" in out[j]:
                        has_acc = True
                    if "[stem on image" in out[j]:
                        has_stem_placeholder = True
                    j -= 1
                rendered = render_block(blocks[key])
                for r in rendered:
                    if isinstance(r, tuple):
                        tag, val = r
                        if tag == "OPTS":
                            if bullets < 2:
                                out.append("**Options:**")
                                out.append("")
                                for o in val.split("||"):
                                    out.append("- " + o.strip())
                                out.append("")
                        elif tag == "STEM":
                            if has_stem_placeholder:
                                for k in range(len(out)):
                                    if "[stem on image" in out[k]:
                                        out[k] = val
                                        break
                        elif tag == "ACC":
                            if not has_acc:
                                out.append("**Accepted answer (paper key):** `%s`" % val)
                                out.append("")
                    else:
                        out.append(r)
                used.add(key)
            else:
                remaining_anchors.append(lines[i])
                out.append("*[figure/code image — see kit engine pattern]*")
                out.append("")
            i += 1
        else:
            out.append(lines[i])
            i += 1
    open(paper_path, "w", encoding="utf-8").write("\n".join(out))
    return used, remaining_anchors


all_blocks = {}
for ef in glob.glob(os.path.join(TP, "extra-*.md")):
    all_blocks.update(parse_extras(ef))
print("extras blocks:", len(all_blocks))
used_all = set()
residue = []
for pf in sorted(glob.glob(os.path.join(PP, "*", "*.md"))):
    used, rem = apply(pf, all_blocks, None)
    used_all |= used
    if rem:
        residue.append((pf, rem))
unused = [k for k in all_blocks if k not in used_all]
print("used:", len(used_all), "| unused extras:", len(unused))
for k in sorted(unused)[:30]:
    print("  UNUSED:", k)
print("files with leftover anchors:", len(residue))
for pf, rem in residue:
    print("  ", os.path.basename(pf), [r.split(":")[-1].strip("]") for r in rem][:12])
