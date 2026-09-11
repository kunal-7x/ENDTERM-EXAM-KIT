"""Build the ENDTERM EXAM-KIT static site (flat structure, mobile-first)."""
import markdown, re, os, json, shutil

ROOT = r"C:\Users\kunal\Desktop\ENDTERM\EXAM-KIT"
TOOLS = os.path.join(ROOT, "_tools")
OUT = os.path.join(ROOT, "site")
ASSETS = os.path.join(OUT, "assets")

# (out_file, nav_title, section, blurb, kind, src)
PAGES = [
    ("start-tonight.html", "Start Tonight", "Start", "Hour-by-hour battle plan", "md", "START_TONIGHT.md"),
    ("exam-day-os.html", "Exam-Day OS", "Start", "The blank-mind algorithm", "md", "00_EXAM_DAY_OS.md"),
    ("ba-hub.html", "BA Hub", "BA", "All Business Analytics files", "hub", "BA"),
    ("ba-00-index.html", "BA 80/20 Index", "BA", "Topic frequency + file map", "md", "01_BA/BA-00-INDEX-80-20.md"),
    ("ba-01-stats.html", "BA Engine: Stats", "BA", "Chi-square, distributions, Bayes", "md", "01_BA/BA-01-ENGINE-STATS.md"),
    ("ba-02-regression.html", "BA Engine: Regression", "BA", "Regression, demand, confusion metrics", "md", "01_BA/BA-02-ENGINE-REGRESSION.md"),
    ("ba-03-dea-lp.html", "BA Engine: DEA + LP", "BA", "DEA theory, HCU recipe, primal-dual, conjoint", "md", "01_BA/BA-03-ENGINE-DEA-LP.md"),
    ("ba-04-ratta.html", "BA Ratta Q&A", "BA", "Every repeated MCQ/MSQ + answer", "md", "01_BA/BA-04-RATTA.md"),
    ("ba-05-sheet.html", "BA Formula Sheet", "BA", "One-page last-pass", "md", "01_BA/BA-05-SHEET.md"),
    ("ba-06-sa-dump.html", "BA Solved SA Dump", "BA", "All 219 numerics + answers", "md", "01_BA/BA-06-SA-DUMP.md"),
    ("mad2-hub.html", "MAD2 Hub", "MAD2", "All App Dev II files", "hub", "MAD2"),
    ("mad2-00-index.html", "MAD2 80/20 Index", "MAD2", "Topic frequency + file map", "md", "02_MAD2/MAD2-00-INDEX-80-20.md"),
    ("mad2-01-js.html", "MAD2 Engine: JavaScript", "MAD2", "this, scope, async, output tracing", "md", "02_MAD2/MAD2-01-JS-ENGINE.md"),
    ("mad2-02-vue.html", "MAD2 Engine: Vue", "MAD2", "Vue, Vuex, Router tables", "md", "02_MAD2/MAD2-02-VUE-ENGINE.md"),
    ("mad2-03-web.html", "MAD2 Engine: Web", "MAD2", "HTTP, JWT, Flask-cache, Celery", "md", "02_MAD2/MAD2-03-WEB-ENGINE.md"),
    ("mad2-04-mcq.html", "MAD2 MCQ Master", "MAD2", "120 unique MCQs + answers", "md", "02_MAD2/MAD2-04-MCQ-MASTER.md"),
    ("mad2-05-msq.html", "MAD2 MSQ Playbook", "MAD2", "Tick-sets + counting rules", "md", "02_MAD2/MAD2-05-MSQ-PLAYBOOK.md"),
    ("mad2-06-sheet.html", "MAD2 Cheatsheet", "MAD2", "One-page last-pass", "md", "02_MAD2/MAD2-06-SHEET.md"),
    ("mad2-07-dump.html", "MAD2 Full Q Dump", "MAD2", "All 377 questions reference", "md", "02_MAD2/MAD2-07-DUMP.md"),
    ("mlp-hub.html", "MLP Hub", "MLP", "All ML Practice files", "hub", "MLP"),
    ("mlp-00-index.html", "MLP 80/20 Index", "MLP", "Topic frequency + file map", "md", "03_MLP/MLP-00-INDEX-80-20.md"),
    ("mlp-01-core.html", "MLP Engine: Core", "MLP", "Scalers, metrics, CV, counts", "md", "03_MLP/MLP-01-ENGINE-CORE.md"),
    ("mlp-02-models.html", "MLP Engine: Models", "MLP", "Every model family rules", "md", "03_MLP/MLP-02-ENGINE-MODELS.md"),
    ("mlp-03-ratta.html", "MLP Ratta Q&A", "MLP", "Concept MCQ/MSQ + answers", "md", "03_MLP/MLP-03-RATTA.md"),
    ("mlp-04-sa.html", "MLP Solved SA", "MLP", "All numerics, verified", "md", "03_MLP/MLP-04-SA-SOLVED.md"),
    ("mlp-05-sheet.html", "MLP Cheatsheet", "MLP", "API + formula last-pass", "md", "03_MLP/MLP-05-SHEET.md"),
    ("mlp-predicted-paper.html", "MLP Predicted Paper", "MLP", "Predicted practice paper + formula sheet", "graft", "mlp.html"),
    ("mlp-read-and-go.html", "MLP Read-and-Go (70 marks)", "MLP", "Exact predictions + mechanical steps", "fragment", "read-and-go.fragment.html"),
    ("last-6-hours.html", "Last 6 Hours", "Start", "Emergency 6-hour plan", "md", "99_LAST_6_HOURS.md"),
]

CHAIN = ["index.html"] + [p[0] for p in PAGES]

NAV_SECTIONS = [
    ("Start", [("index.html", "Home"), ("start-tonight.html", "Start Tonight"),
               ("exam-day-os.html", "Exam-Day OS"), ("last-6-hours.html", "Last 6 Hours")]),
    ("BA", [("ba-hub.html", "BA Hub")] + [(p[0], p[1]) for p in PAGES if p[2] == "BA" and p[4] in ("md", "fragment", "graft") and "hub" not in p[0]]),
    ("MAD2", [("mad2-hub.html", "MAD2 Hub")] + [(p[0], p[1]) for p in PAGES if p[2] == "MAD2" and p[4] in ("md",) and "hub" not in p[0]]),
    ("MLP", [("mlp-hub.html", "MLP Hub")] + [(p[0], p[1]) for p in PAGES if p[2] == "MLP" and "hub" not in p[0]]),
]

PAGE_TMPL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{TITLE}} Â· ENDTERM EXAM-KIT</title>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<header class="topbar">
<button class="hamburger" id="hamburger" aria-label="Menu">â˜°</button>
<a class="brand" href="index.html">ðŸŽ“ EXAM-KIT</a>
<div class="searchwrap"><input id="search" type="search" placeholder="ðŸ” Search any topicâ€¦" autocomplete="off"><div id="results"></div></div>
<a class="gh" href="https://github.com/kunal-7x/ENDTERM-EXAM-KIT" target="_blank" rel="noopener">GitHub</a>
</header>
<div class="layout">
<aside class="sidebar" id="sidebar">{{NAV}}</aside>
<div class="scrim" id="scrim"></div>
<main class="content">
<div class="crumbs">{{SECTION}} / {{TITLE}}</div>
{{ONPAGE}}
<article class="doc">{{CONTENT}}</article>
<nav class="prevnext">{{PREV}} {{NEXT}}</nav>
<footer class="foot">ENDTERM EXAM-KIT Â· 27 papers Â· 1,100+ questions Â· exact numbers â†’ vault Â· new numbers â†’ engine</footer>
</main>
</div>
<script src="assets/app.js"></script>
</body>
</html>
"""

HUB_TMPL = """<div class="hubhead"><h1>{{H1}}</h1><p>{{DESC}}</p></div>
<div class="cards">{{CARDS}}</div>"""

CARD_TMPL = """<a class="card" href="{url}"><div class="card-t">{title}</div><div class="card-d">{desc}</div><div class="card-go">Open â†’</div></a>"""


def md_to_html(path):
    text = open(os.path.join(ROOT, path), encoding="utf-8").read()
    # '#' shorthand for 'number of' at line start is NOT a heading -> use â„–
    text = re.sub(r"(?m)^#(?!#| )", "№", text)
    text = re.sub(r"(?m)^(\s*(?:\d+\.|[-*])\s+)#(?!#| )", r"\g<1>№", text)
    text = re.sub(r"(?m)^(>\s*)#(?!#| )", r"\g<1>№", text)
    h = markdown.markdown(text, extensions=["extra", "toc", "sane_lists"])
    h = h.replace("<table>", '<div class="table-scroll"><table>').replace("</table>", "</table></div>")
    return h


def onpage_box(h):
    items = re.findall(r'<h2 id="([^"]+)">(.*?)</h2>', h, re.S)
    if len(items) < 3:
        return ""
    lis = "".join('<li><a href="#%s">%s</a></li>' % (i, re.sub(r"<[^>]+>", "", t).strip()[:70]) for i, t in items)
    return '<nav class="onpage"><div class="onpage-t">On this page</div><ul>%s</ul></nav>' % lis


def nav_html():
    parts = []
    for sec, links in NAV_SECTIONS:
        parts.append('<div class="navsec">%s</div><ul>' % sec)
        for url, title in links:
            parts.append('<li><a href="%s" data-href="%s">%s</a></li>' % (url, url, title))
        parts.append("</ul>")
    return "".join(parts)


def build():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(ASSETS)
    shutil.copy(os.path.join(TOOLS, "site-style.css"), os.path.join(ASSETS, "style.css"))
    shutil.copy(os.path.join(TOOLS, "site-app.js"), os.path.join(ASSETS, "app.js"))
    # landing
    landing = open(os.path.join(TOOLS, "landing.fragment.html"), encoding="utf-8").read()
    by_out = {p[0]: p for p in PAGES}
    index = {"index.html": ("ENDTERM EXAM-KIT", "Home")}
    search_idx = [{"t": "Home â€” ENDTERM EXAM-KIT", "u": "index.html"}]
    nav = nav_html()

    def emit(out, title, section, content):
        i = CHAIN.index(out)
        prev = '<a class="pn prev" href="%s">â† %s</a>' % (CHAIN[i - 1], short(CHAIN[i - 1])) if i > 0 else "<span></span>"
        nxt = '<a class="pn next" href="%s">%s â†’</a>' % (CHAIN[i + 1], short(CHAIN[i + 1])) if i < len(CHAIN) - 1 else "<span></span>"
        page = PAGE_TMPL.replace("{{TITLE}}", title).replace("{{SECTION}}", section)
        page = page.replace("{{NAV}}", nav).replace("{{CONTENT}}", content)
        page = page.replace("{{ONPAGE}}", onpage_box(content)).replace("{{PREV}}", prev).replace("{{NEXT}}", nxt)
        open(os.path.join(OUT, out), "w", encoding="utf-8").write(page)

    def short(out):
        if out == "index.html":
            return "Home"
        return by_out[out][1]

    emit("index.html", "ENDTERM EXAM-KIT", "Home", landing)
    for out, title, section, blurb, kind, src in PAGES:
        if kind == "md":
            emit(out, title, section, md_to_html(src))
        elif kind == "fragment":
            emit(out, title, section, open(os.path.join(TOOLS, src), encoding="utf-8").read())
        elif kind == "hub":
            cards = "".join(CARD_TMPL.format(url=p[0], title=p[1], desc=p[3])
                            for p in PAGES if p[2] == src and p[4] in ("md", "fragment", "graft"))
            descs = {"BA": "Business Analytics â€” 45 marks. Engines, ratta, sheets, 219 solved numerics.",
                     "MAD2": "Modern App Dev II â€” 100 marks. JS, Vue, Web engines, MCQ master, MSQ playbook.",
                     "MLP": "ML Practice â€” 100 marks. sklearn engines, ratta, verified answers, predicted paper."}
            h1 = {"BA": "ðŸ“Š Business Analytics", "MAD2": "ðŸŸ¦ Modern App Dev II", "MLP": "ðŸŸ£ ML Practice"}[src]
            emit(out, title, section, HUB_TMPL.replace("{{H1}}", h1).replace("{{DESC}}", descs[src]).replace("{{CARDS}}", cards))
        elif kind == "graft":
            graft_mlp(out, title, section)
        search_idx.append({"t": "%s â€” %s" % (title, section), "u": out})
    json.dump(search_idx, open(os.path.join(ASSETS, "search-index.json"), "w", encoding="utf-8"))
    print("built pages:", len(CHAIN), "| search entries:", len(search_idx))


BACK_BTN = """<a href="mlp-hub.html" style="position:fixed;top:12px;left:12px;z-index:9999;background:#4f46e5;color:#fff !important;padding:10px 16px;border-radius:10px;font:600 15px system-ui;text-decoration:none;box-shadow:0 4px 14px rgba(0,0,0,.3)">â† Back to Kit</a>"""


def graft_mlp(out, title, section):
    src = os.path.join(r"C:\Users\kunal\Desktop\Downloads", "mlp.html")
    h = open(src, encoding="utf-8", errors="replace").read()
    h = re.sub(r"<body([^>]*)>", r"<body\1>\n" + BACK_BTN, h, count=1, flags=re.I)
    open(os.path.join(OUT, out), "w", encoding="utf-8").write(h)
    print("grafted mlp.html:", len(h), "chars")


if __name__ == "__main__":
    build()
