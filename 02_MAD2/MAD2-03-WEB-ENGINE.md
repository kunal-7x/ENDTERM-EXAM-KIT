# 🌐 MAD2-03 — WEB ENGINE (HTTP, security, Flask-cache, async-arch)

## ENGINE W1 — HTTP / CORS / cookies / storage
| Trigger | Answer |
|---|---|
| WebSocket handshake method | **GET** (Upgrade request) |
| Same-origin fetch allowed | ONLY same scheme+host+port → `http://origin1.com/api/` ✓ |
| CORS enabled for :5000, fetch from :3000 | **BLOCKED** (origins must match exactly) |
| CORS purpose | **controlled cross-origin access** (NOT XSS/SQL) |
| CORS headers prefix | **Access-Control-Allow-*** |
| CSRF scenario (img tag / hidden transfer via session) | **Cross Site Request Forgery** |
| CSRF token purpose | **validate request comes from authenticated user** |
| Flask CSRF protection by default? | **NO — "enforced by default" is always the FALSE option** |
| Flask returns CORS headers by default? | **NO** (needs flask-cors) |
| Phishing mail asking password / brute force / malware | NOT CSRF |
| Cookie for send-with-every-request | **Cookie** (not local/session storage) |
| Session cookies | sent by default + deleted on browser close |
| `secure=True, samesite='Strict'` | HTTPS-only + no cross-site |
| sessionStorage after close/reopen | **LOST** ("remains available" = FALSE) |
| localStorage vs cookies | localStorage bigger; cookies auto-sent |
| CSP `default-src 'self'` + external script | **blocked + console error** |
| fetch credentials | `credentials` property exists; `omit` = no cookies; `include` = even cross-origin |
| fetch: custom headers / images / Accept header | **All of these** (all TRUE) |
| Webhook HTTP method | **POST** |
| HTTP success codes (MSQ) | **200 + 201** |
| Cache-Control / Expires | **both control caching** (NOT Bearer/Content-Type) |

## ENGINE W2 — JWT / OAuth / auth
| Trigger | Answer |
|---|---|
| JWT > sessions advantage | **stateless, no server-side session storage** |
| JWT payload stores | **claims: identity + expiry** (NOT keys/algorithm/signature) |
| JWT format | **header.payload.signature** |
| JWT sequence | credentials→validate→issue JWT→client stores→client sends JWT per request |
| No token on @jwt_required route | **401 Unauthorized** |
| Valid token, wrong role (student vs admin) | **403 Forbidden** |
| OAuth | protocol for access **on behalf of user** + **authorization** (NOT authentication) |

## ENGINE W3 — Flask caching (TIME questions — read carefully!)
| Shape | Rule | Vault |
|---|---|---|
| `@cache.cached(timeout=T)` + sleep(S), 2 same-URL hits, 2nd within T | 2nd served from cache → diff = **S** | sleep30, 2nd@50s, T=100 → **30 Seconds** |
| Same, but 2nd AFTER T expires | recompute → diff = **0** | sleep30, T=40, 2nd@3min → **0 seconds** |
| `@cache.memoize` + same args | cached per-args → 1st slow, rest fast | sleep5, hits@0/2.5m/3.5m, T=180 → 1st−3rd = **5 seconds** |
| `key_prefix='compute'` FIXED + two DIFFERENT URLs | SAME cache entry → 2nd returns 1st's result | /10/20→200 then /5/10→ **{"result":200} twice** |
| `@cache.cached` (view) + two DIFFERENT paths | cached PER-URL → both slow → diff **0** | /mohan + /sohan → **0 Seconds** |
| `memoize()` vs `cached()` | memoize = by ARGS; cached = whole VIEW | tick this exact sentence |
| Flask MSQ false-set | tick **"memoize ignores params"** + **"GETs without body uncacheable"** (both FALSE) | — |
| `threaded=False` + fetch e1(20s) + fetch e2(30s) | sequential: e2 finishes at **50s** | — |

## ENGINE W4 — Celery / webhooks / polling / WS / SSE / misc-arch
| Trigger | Answer |
|---|---|
| Celery `delay()` vs `apply_async(countdown=10)` | delay = dispatch NOW; apply_async = dispatch now, EXECUTE after 10s |
| Celery needs broker ✓; task queue ✓; scheduling ✓ | MSQ: tick all three |
| Celery sync/async (MSQ) | **async** ✓ (NOT sync) |
| 1000 tasks via .delay × N workers vs 1 task looping | **Approach 1 (parallel) faster**; "approach 2 faster" + "comparable" = FALSE; "comparable if 1 worker" = TRUE |
| Celery best for (MSQ) | periodic emails ✓ + long background jobs ✓ (NOT realtime UI, NOT page rendering) |
| Webhook design order (brute-force job) | **Dispatch job → webhook callback → relieve worker** (III, I, II) |
| Webhook = ? | HTTP push server→server on events; receiver = POST route (snippet **B**); sender does NOT poll |
| Webhook TRUE-set (MSQ) | HTTP requests ✓ + POST ✓ (NOT polling, NOT ordered-exactly-once) |
| Webhooks vs SSE (MSQ) | server↔server vs server→client ✓ + SSE client-initiated ✓ |
| Webhook receiver snippet | **B** (Flask POST route). Pub/Sub snippet → **C** (SSE stream) |
| Short polling | repeated requests, checks async-task state ✓ |
| Long polling | ONE request held open till data ✓; over HTTP ✓; realtime ✓ |
| "Webhook = short polling" | **FALSE, always** |
| WebSocket | full-duplex, persistent; needs NO HTTP per message |
| SSE | HTTP-based ✓, multi-client ✓ (NOT bidirectional, NOT auto-WS) |
| Match: Webhooks/C, WS/chat-A, API/D, Polling/B, PubSub/E | **1-C, 2-A, 3-D, 4-B, 5-E** |
| JAMStack separation | TRUE (frontend/backend independent) |
| "API exists for caching" / "must use token auth" | FALSE (the FALSE-set answers) |
| Avoid verbs in API URLs | TRUE (REST convention) |
| SMTP vs IMAP (MSQ false) | SMTP = SEND; IMAP = RETRIEVE ("SMTP retrieves" + "IMAP delivers" = FALSE) |
| CDN | content-delivery server group (first two options) |
| Celery/Redis specifics | multiple brokers OK; Redis NOT mandatory; periodic scheduling SUPPORTED |
| Point-to-point N servers | links grow **O(n²)** ("O(n)" = FALSE); broker → O(n) |
| GraphQL > REST | **fetch only needed fields** (only this) |
| System state stored | **server-side DB** |
| Vue state management | **Vuex** |
| `async/await` TRUE-set | await-in-async ✓ + waits for fulfillment ✓ + outside code runs meanwhile ✓ → **All of these** |
| Execution context (MSQ) | global at start ✓ + function ctx at CALL ✓ |
| Prototype (MSQ) | has-prototype ✓ + can-be-null ✓ |
| Memoize term | cache fn-result by ARGS ✓; Redis can cache ✓; "only browser" FALSE |
| `t1=new Vue({el:'#app'…})` pattern | standard mount; message renders |
