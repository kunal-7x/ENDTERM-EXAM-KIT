# 📋 MAD2-06 — CHEATSHEET (last-pass page)

## JS
- this: caller obj · detached→window(NaN) · arrow→outer · call/bind→arg · call()=window
- var-loop+timeout → FINAL value ×N · promise-then BEFORE setTimeout
- sync→micro→macro · `await` splits async fn · swapped executor params: 1st IS resolve
- const-loop → throws · reduce past end → NaN · string+=num → concat
- closure = fn + env · prototype nullable · getter called as fn → throws

## Vue
- :class obj/array · v-if REMOVES, v-show HIDES · v-for needs :key/:id binding
- v-model custom = value+$emit · mounted AFTER render (wins over created)
- $refs mutation reactive · $emit→parent · slots merge classes · double slot = double content
- Vuex: ...mapState · actions async→commit · commit ONE payload
- Router: push(params) renders · mounted-redirect wins · `*` LAST · `#/`+no-child → Error · names can LIE (read template!)

## Web
- WS=GET · same-origin = scheme+host+port · CORS: exact-origin or BLOCKED
- Flask: NO default CSRF/CORS · CSRF = session-riding (img/hidden req)
- Cookie=auto-sent · sessionStorage dies on close · CSP-self blocks external
- JWT: stateless · claims · header.payload.signature · none→401, wrong-role→403
- cached=per-URL · memoize=per-args · fixed key_prefix=SHARED · expired=0 diff
- threaded=False → sequential adds up
- Celery: delay=now, countdown=later · broker needed · parallel .delay wins
- Webhook=POST push · receiver=Flask-POST(B) · order III,I,II
- polling: short=repeats, long=holds · SSE=HTTP push multi · WS=full-duplex
- SMTP sends, IMAP fetches · 200/201 · Cache-Control+Expires
- OAuth=behalf+authZ · GraphQL=no-overfetch · JAMStack split TRUE
