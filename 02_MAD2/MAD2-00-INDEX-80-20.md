# 🟦 MAD2-00 — Modern App Dev II: 80/20 Index

**Paper: 100 marks, ~35 questions. ALL MCQ (2/3/4.5m) + MSQ (2/3/4.5m). No numeric entry. Pure recognition + code-tracing.**

## 🔥 TOPIC FREQUENCY (counted from all 12 papers, 377 questions)

| # | Topic | Hits | Engine | Priority |
|---|---|---|---|---|
| 1 | Vue core (binding, directives, slots, lifecycle, computed) | 95 | MAD2-02 | 🔴 HIGH |
| 2 | Web concepts (REST, HTTP, CDN, scaling, APIs) | 71 | MAD2-03 | 🔴 HIGH |
| 3 | Async arch (Celery, webhooks, polling, WS, SSE, GraphQL) | 46 | MAD2-03 | 🔴 HIGH |
| 4 | Vuex (store, mutations, actions) | 40 | MAD2-02 | 🔴 HIGH |
| 5 | Flask + caching (time/latency questions) | 38 | MAD2-03 | 🔴 HIGH |
| 6 | HTTP/CORS/CSRF/cookies/JWT/auth | 37 | MAD2-03 | 🔴 HIGH |
| 7 | JS this/scope/closure/prototype | 34 | MAD2-01 | 🔴 HIGH |
| 8 | JS output tracing (map/filter/typeof) | 34 | MAD2-01 | 🔴 HIGH |
| 9 | JS async (promises, event loop, fetch) | 21 | MAD2-01 | 🟡 MED |
| 10 | Vue Router | 15 | MAD2-02 | 🟡 MED |

## 🗺️ FILE MAP

| File | What | When |
|---|---|---|
| MAD2-01-JS-ENGINE | this/scope/hoisting/async/event-loop + output-tracing recipes | Study 1st (3m+4.5m Qs = 50 marks) |
| MAD2-02-VUE-ENGINE | Vue/Vuex/Router trigger→answer tables | Study 2nd |
| MAD2-03-WEB-ENGINE | HTTP/CORS/cookies/JWT/Flask-cache/Celery/webhooks trigger→answer | Study 3rd |
| MAD2-04-MCQ-MASTER | ~120 unique MCQs + verified answers, topic-grouped | Memorize |
| MAD2-05-MSQ-PLAYBOOK | Every MSQ pattern + tick-sets | Memorize |
| MAD2-06-SHEET | One-page cheatsheet | Before sleep + exam |
| MAD2-07-DUMP | All 377 Qs + options (reference) | Search when doubtful |

## ⚡ MAD2 EXAM-DAY CHEAT (the 6 moves)

1. **JS output Q**: trace ONLY the asked line backwards. `var` in loops → final value repeats. Microtasks (promises) before macrotasks (setTimeout).
2. **"this" Q**: regular function → caller object; arrow → outer scope; detached (`const f = obj.m`) → window/undefined; `.call(X)` → X.
3. **Vue render Q**: computed runs on render; mounted runs AFTER first render; v-if removes, v-show hides; class merges on component root.
4. **Flask cache Q**: `@cache.cached` = per-URL; `@cache.memoize` = per-args; `key_prefix` fixed = ALL URLs share one entry; expired timeout = full recompute.
5. **Theory MCQ**: memorized trigger→answer tables in engines. 60% repeat verbatim.
6. **MSQ**: usually 2 ticks. "All of these" only if you verified each. "None of these" when all others visibly broken.
