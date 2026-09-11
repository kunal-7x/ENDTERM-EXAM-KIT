# 📝 MAD2-04 — MCQ MASTER (rapid-fire: trigger → tick this)

**Every row = one unique question family across 12 papers. Engines have the why; this is the WHAT.**

## JS (2m theory)
- `this` keyword → **None of these** · Arrow has own this → **FALSE**
- JS hoisting: `let/const` → **also hoisted (TDZ)** · undeclared var → **not hoisted at all**
- First-class + higher-order → **both supported** · `const` = block scope ✓ · int/char primitives → **FALSE**
- Replit = JS engine → **FALSE** · first-class fns ✓ · user HOFs allowed ✓ · DOM ✓
- `myQual.qualification()` etc → **calling getter as fn throws**
- `for(const i…)` → **throws first iteration** · `for(let…)` same body → **logs all 3**
- `typeof` mixed array → **all logged, no error**

## JS (3m output)
- `i=1;i<4;i+=2` timeouts → **55** · `i=0;i<3;i++` → **333, 6s** · `i<=3,(i+1)*1500` → **4444, 6s**
- Promise swapped params, a=8 b=0 → **Failed: 8 / About to finish / Finished !! undefined**
- `some()` await → **Executing / Execution Started / Excution Started / 0s**
- `promoter(8)` → **Not Promoted / Job Done**
- `goUpDown` (no return) → **None of these**
- fetch fail → **'Response is not json'** · 500+JSON → **500** · missing await .json → **JSON data**
- propA trio → **10 20** · `call()` empty → **This:39, Normal:39** · detached method → **NaN**
- `bind` Jane → **Jane Smith** · bind() global (var2=35 global!) → **70 / 91**
- nested arrow → **25 / 45** (56-ver → 56 / 24) · regular+arrow value-undefined → **both undefined**
- Dog class → **Rex barks, true, true** · delete prototype-method → **still works twice**
- closure add(5)(10) → **15** · parentFunc → **Arpan/Beli/Beli**
- `obj2.second.call(obj1)` → **Function Invoked !! / 2**
- map-cube-filter → **[8,27,125,343,512]** · reduce+next → **NaN**
- localStorage loop → **0222 then null** · cart×3 loads → **3× Laptop**
- `Promise.resolve(1)…catch(e=>e+4)` → **error4**
- Start/End/Promise/Timeout → **Start, End, Inside Promise, Inside Timeout**
- Begin/test/Finish → **Begin, Finish, Start, 5, End** · `p(1);p(2)` sequential → **['Outer']**
- nested timeouts → **variable1, variable4, variable2, variable3**
- `iitmiitm` split → len 3 → reject-path → **"Promise Resolved : Promise is rejected / …undefined / …undefined / …34"**
- title war A@1s+B@2s → **approach 2 toggles** · dynamic script → **ReferenceError FIRST**
- `placeholder` in prototype method → **this**

## Vue (3m render)
- localStorage v-model refresh → **IIT, Madras** / **AppDev1, 70**
- run 24 even → **Blue + 24** · Home bold+active → **blue, bold**
- v-for contributions → **Rohit: 100/210Kohli: 110/210** · custom-input Apple → **Searching for: Apple**
- profile push narendra → **Welcome narendra** · Movies route → **MoviesSome Error**
- `$refs` rename → **Welcome Virat Kohli** · cart Orange-twice → **3.Orange 4.Orange**
- First→mounted→endpoint2 → **Hello Second Component !!** · `/` no-child → **Page not Found** · `#/booked` → **Unbooked Slots**
- `sort()` desc → **1917** · booked filter → **2** · select typeOne even → **246**
- `created+mounted` message → **Hello from mounted** · app1⊂app2 → **FrontendJavaScript**
- double default slot → **all four texts** · slots usage → **v-slot:title template**
- `availableSlots` → string-compare status + id>offset
- `slot/:status` + query → **apply BOTH filters**

## Vue (4.5m) — slow down, trace twice
- book-slot ×0 → **Booked**; ×3 → **Not Booked**
- `isOnCircle` '3,4' → **On the circle** (9+16=25)
- `buy()` empty cart (amount 0 ≤ 50) → **Success**
- Apple×5+Orange×1, NO addToCart → cart empty → **Success**
- my-button emit → **Button then Parent**
- Home child-router `#/` → option with **std1/mad1 set** (mounted-redirect pattern)
- `/student/20` variant → **Name: std2, Course: mad2**-family (id%5 pattern)
- role-guard first load → compare hierarchy numbers, `replace()` target

## Web (2m)
- WS handshake → **GET** · same-origin → **origin1.com/api only** · CORS :3000→:5000 → **blocked**
- CORS purpose → **controlled cross-origin access** · headers → **Access-Control-Allow**
- Flask CSRF default → **NO** · Flask CORS default → **NO**
- CSRF token → **validate request source** · img-delete → **CSRF** · bank-transfer → **CSRF**
- phishing/bruteforce/malware → **NOT CSRF**
- Cookie-every-request → **Cookie** · session cookie → **sent + dies on close**
- `secure+samesite` → **True + Strict** · sessionStorage reopened → **lost**
- CSP self + external → **blocked + error** · webhook method → **POST**
- 2xx codes → **200, 201** · cache headers → **Cache-Control, Expires**
- OAuth → **behalf-of-user + authorization** (NOT authentication)
- JWT>session → **stateless** · payload → **claims** · format → **header.payload.signature**
- no-token → **401** · wrong-role → **403** · JWT steps → **option 1**
- Vue state → **Vuex** · system state → **server DB** · GraphQL → **no over-fetch**
- SMTP=send, IMAP=retrieve (MSQ-false: swapped pair)

## Flask-cache (3m/4.5m)
- cached T=100 sleep30 same-URL → diff **30** · T=40 expired → **0**
- memoize same-args → 1st slow → 1st−3rd = **5**
- fixed `key_prefix` + 2 URLs → **200 and 200** (shared entry!)
- `cached` + 2 paths → per-URL → diff **0**
- memoize=**args**, cached=**views** · threaded=False e1+e2 → **50s**
