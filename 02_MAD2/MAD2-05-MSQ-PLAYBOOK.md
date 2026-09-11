# ☑️ MAD2-05 — MSQ PLAYBOOK (tick-sets + counting rules)

## 📏 TICK-COUNT RULES (from 89 MSQs across 12 papers)
- **Default: 2 ticks.** ~70% of MAD2 MSQs have exactly 2 correct.
- 3-tick MSQs exist (Vuex, caching, webhooks). 4-tick: almost never.
- **"All of these"** as last option: tick it ONLY with 3 verified trues. It's correct ~40% when offered.
- **"None of these"** as last option: tick it when every other option is visibly broken (code MSQs) — correct ~60% then.

## 📚 VERIFIED TICK-SETS (topic → tick these)

**JS theory:** const-block ✓ + first/higher-order ✓ (NOT low-level, NOT int/char) · JAMStack-separate ✓ + verbs-avoided ✓ (FALSE-set: token-mandatory + API-for-caching) · hoisting: decl-with-def ✓ + TDZ ✓ · getters: `prop()` throws ✓ + `prop(x)` throws ✓ · `v-for` syntaxes: in ✓ + (i,idx) in ✓ + of ✓ · execution ctx: global-at-start ✓ + fn-at-call ✓ · prototype: has ✓ + nullable ✓ · closure def ✓ + created-always ✓
**Async:** await-rules → **all three** · event-loop: non-blocking ✓ + task-queue ✓ (NOT separate-thread) · fetch-creds: prop ✓ + omit ✓ + include-cross ✓
**Vue:** class-binding: `{classA:classA}` ✓ + `classObj` ✓ · v-if-removes ✓ + same-when-true ✓ · array-class: `[ternary,'errorClass']` ✓ + `[{activeClass:isActive},'errorClass']` ✓ · client-only-no-DB FALSE-set: always-lost ✓ + no-reload ✓ + cross-machine ✓ · Vuex-placeholders: single-payload ✓ + object-payload ✓ · cart-actions: **All of these**
**Vuex/Router false-sets:** separate-stores ✓ + wildcard-on-top ✓ + must-use-Vuex ✓ (all FALSE) · force-reload trio (all FALSE)
**Web:** caching-helps-perf ✓ (shared-cache-personalized = FALSE) · caching-benefits: latency ✓ + load ✓ + scale ✓ (NOT security) · SSE: HTTP ✓ + multi ✓ · webhooks: HTTP ✓ + POST ✓ · webhooks-vs-SSE: s2s-vs-s2c ✓ + client-initiated ✓ · polling: short-tracks-tasks ✓ + long-realtime ✓ · SMTP/IMAP: the SWAPPED pair ✓✓ · CDN: acronym ✓ + server-group ✓ (NOT always-closest) · Celery: queue ✓ + broker ✓ + schedule ✓ · Celery-sync? NO: async ✓ only · celery-use: periodic-mail ✓ + background-jobs ✓ · scaling-false: always-scale-out ✓ + diagonal ✓ · flask-false: memoize-ignores-params ✓ + GET-uncacheable ✓ · long/short: short ✓ + long ✓ · memoize-vs-cached sentence ✓ · thread/fetch/CMS: 500-ok-true ✓ + headless-manages-frontend ✓
**Design:** webhook-order **III,I,II** · match-table **1-C,2-A,3-D,4-B,5-E** · celery-parallel: approach-2-faster ✓ + comparable ✓ (both FALSE)

## 🔍 60-SECOND MSQ METHOD (when memory fails)
1. Read the QUESTION word: true-set or false-set? (Most MAD2 MSQs ask "false".)
2. Kill the obviously-true (in false-sets) / obviously-false (in true-sets) options.
3. Count survivors: 2 → tick both. 3 → tick the 2 surest + the 3rd only if engine-verified.
4. "All/None of these": apply the counting rule above — never tick on gut feel.
