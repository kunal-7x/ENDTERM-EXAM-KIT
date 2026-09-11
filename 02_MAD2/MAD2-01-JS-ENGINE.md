# ⚡ MAD2-01 — JS ENGINE (this, scope, async, output tracing)

## ENGINE J1 — `this` (8+ questions, never changes)
| Code shape | `this` is | Example answer |
|---|---|---|
| `obj.method()` | `obj` | `person.fullName()` → "John Doe" |
| `const f = obj.method; f()` | window → `undefined.x` → **NaN** (sloppy) / Error (strict) | `multiply()` → **NaN** |
| Arrow function | **outer scope's this** (never its own) | arrow in obj → window → `undefined` |
| `.call(X)` / `.bind(X)` / `.apply(X)` | **X** | `propB.call(obj1)` → "10 20" (global 10, obj1's 20) |
| `.call()` with nothing (sloppy script) | **window/global** | `func.call()` → "This: 39, Normal: 39" |
| `new` constructor | the new object | — |
| Event listener (regular) | the element | — |
| **"this keyword" theory MCQ** | — | **None of these** (arrows have NO own this; listener ≠ window; not always global) |

**VAULT (verified in node + browser semantics):**
- propA=10/obj1(20)/obj2(30), `obj2.propB.call(obj1)` → **"10 20"**
- `var a=39; obj1.func.call()` → **"This : 39, Normal : 39"**
- `const multiply = obj.multiply` (num:5) → **NaN**
- `fullName.bind({Jane, Smith})()` → **"Jane Smith"**
- `m.bind()(5)` (no obj) → this=window, var2=undefined→NaN?? → 10+undefined+25 = **NaN**?? — wait: `myObj.ObjFunc`, m.bind() → window; `m.call(myObj,6)` → 10+45+36=**91**. First: this.var2 = window.var2 = undefined → 10+undefined+25 = NaN. Options: 70/81, 70/91, 80/81, 80/91 — NO NaN?! Hmm. `let m = myObj.ObjFunc; m.bind()(5)`: bind() with no arg → sloppy → window. this.var2 → undefined. 10 + undefined + 25 → NaN. But options lack NaN… UNLESS var2 global exists? Code: `var var1=25; var var2=35;` — YES, global var2=35! So this.var2=35 → 10+35+25=**70**. Second: 10+45+36=**91**. → **"70 / 91"** ✓. (Lesson: check for GLOBAL vars with same name!)
- Nested arrow (var1=25 global): `x.inObjFunc()` → **"Value is 25"**; `exObj.exObjFunc()` → this=exObj, var2=45 (local 10 shadowed) → **"Value is 45"**. (56-version → "Value is 56 / Value is 24".)
- `regularFunction` returns this.value → undefined (no `value` key!); arrow → undefined. → **both undefined**.
- class Dog: `d.speak()` → **"Rex barks"**; `__proto__===Dog.prototype` → **true**; `__proto__.__proto__===Animal.prototype` → **true**.
- `delete john.greet` (prototype method!) → delete on instance does NOTHING → still works → **"Hello, JohnHello, John"**.
- `add(5)(10)` closure → **15**.
- `parentFunc` closure trio → **"Hi! Arpan / Hi! Beli / Bye! Beli"**.
- obj2.second.call(obj1): prints "Function Invoked !!", then this.second() with this=obj1 → obj1.second exists? obj1.second logs this.first=**2** → **"Function Invoked !! / 2"**.

## ENGINE J2 — var/let/const + hoisting + event loop (output order)
1. **`var` in loop + setTimeout** → ALL callbacks see the FINAL value. `for(var i=1;i<4;i+=2)` → i ends 5 → **"55"**. `for(var i=0;i<3;i++)` → **"333"**, min time = last timer = 3×1000 = **6s**. `i<=3` variant → **"4444"**, 4×1500 = **6s**.
2. **Order**: sync → microtasks (Promise.then) → macrotasks (setTimeout). `Start/End/Promise/Timeout` → **Start, End, Inside Promise, Inside Timeout**.
3. `async` fn: sync until `await`, rest is microtask. `Begin/test/Finish` → **Begin, Finish, Start, 5, End**.
4. `await p(1); await p(2)` = SEQUENTIAL (3s total); data logged before resolve → **['Outer']**.
5. `for(const i=0;…)` → **TypeError, throws immediately** (const can't reassign).
6. Nested setTimeout(2000→500): **variable1, variable4, variable2, variable3**.
7. `Promise.resolve(1).then(+1).then(+1).then(throw).catch(+4)` → **"error4"**.
8. Hoisting MSQ: tick **"function declarations hoisted with definitions"** + **"let/const hoisted but uninitialized (TDZ)"**. NEVER tick "var hoisted with initialization".
9. `let x=[1,'p',fn]; for(const…)` → throws (same rule 5). `for(let…)` same code → logs **all 3 index/value/type** (functions are values, typeof 'function').
10. `reduce((acc,val,idx,arr)=>acc+arr[idx+1],0)` on [1,2,3] → 0+2+3+undefined = **NaN**.
11. `arr.map(r=>r**3).filter(r=>r%3==2||r%4==3)` on 1..8 → cubes: 1,8,27,64,125,216,343,512 → keep 8,27,125,343,512 → **[8,27,125,343,512]**.
12. localStorage loop: counter is STRING → '0'→'02'→'022'→'0222'; sessionStorage.clear() → null → **"0222" then null**.
13. `Promise` executor params SWAPPED `(reject,resolve)`: first param is the REAL resolve. `new Promise((reject,resolve)=>{…resolve(a)})` with a=8,b=0 → actually REJECTS(8) → **"Failed: 8 / About to finish / Finished !! undefined"**.
14. `some()` async: sync "Executing" FIRST (0s) → then "Execution Started" + "Excution Started" (first "e" removed!) → **"ExecutingExecution StartedExcution Started, Time: 0"**.
15. `promoter(8)` (needs >9) → reject-handler then finally → **"Not Promoted / Job Done"**.
16. `goUpDown`: getData awaits 8→"Go Down",15→"Go Up",12→"Go Up" but RETURNS undefined → then logs **undefined** → answer **"None of these"**.
17. `fetch` fail → outer catch → **'Response is not json'**; 500+JSON → **500** (response.status, ok=false path).
18. `fetchData` missing `await` on `.json()` → still resolves → **JSON data**.
19. `setInterval` title war: A@1000+B@2000 → **toggles every ~1s** (A wins odd secs… A registered first: at t=2 A then B → B; sequence A,B,A,B = toggle ✓). A@2000+B@1000 → stuck on B.
20. Dynamic `<script>` + immediate call → **"Uncaught ReferenceError: extFunc is not defined" FIRST**, then loaded-script output, then callback. (ConceptBank-confirmed.)

## ENGINE J3 — prototype / class / getters (theory)
- Closure = **function + lexical environment**; created **every** time a function is created.
- Every object HAS prototype; prototype CAN be null.
- Global ctx at script start; function ctx at CALL (MSQ: tick 1&3).
- Getter/setter object: calling `obj.prop()` → **throws**; `obj.prop` → getter value; `obj.prop = x` → setter runs.
- `Array.prototype.double` placeholder → **`this`**.
