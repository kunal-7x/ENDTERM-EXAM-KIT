@@MAD2-11-1
C: const calculator = { multiplier:5, calculate:function(a, b){ console.log(`Result: ${(a+b)*this.multiplier}`); return (a+b)*this.multiplier; } };
C: const advancedCalc = { multiplier:10, bonus:20 };
C: const operation1 = calculator.calculate.call(advancedCalc, 3, 5);
C: const operation2 = calculator.calculate.bind(advancedCalc, 4);
C: operation2(8); console.log(operation1); console.log(typeof operation2);
O: Result: 40 / Result: 60 / 40 / object || Result: 80 / Result: 120 / 80 / object || Result: 40 / Result: 60 / 40 / function || Result: 80 / Result: 120 / 80 / function
S: Result: 80 / Result: 120 / 80 / function
@@MAD2-11-2
C: childComponent.$emit('update', 5)
O: Parent can listen with @update || Parent receives payload via $event || Child can directly modify parent state || $emit triggers a DOM event
S: Parent can listen with @update || Parent receives payload via $event
@@MAD2-11-3
C: Promise.resolve(1).then(v => { throw v + 1 }).catch(e => e * 2).then(console.log)
O: 2 || 4 || Undefined || Error
S: 4
@@MAD2-11-4
O: Storing passwords as plain text for quick lookup || Using hashing algorithms like "bcrypt" or "Argon2" to store passwords securely || Including user passwords directly in SQL queries || All of these
S: Using hashing algorithms like "bcrypt" or "Argon2"
@@MAD2-11-5
C: response.set_cookie('session_id', 'abc123', secure=option1, samesite=option2)
O: secure=True and samesite='Strict' || secure=False and samesite='Strict' || secure=True and samesite='None' || secure=False and samesite='Lax'
S: secure=True and samesite='Strict'
@@MAD2-11-6
C: (git sequences: checkout main+merge appdev2 / merge main / checkout appdev2+pull origin main / merge appdev2 main)
O: git checkout main / git merge appdev2 / git commit || git merge main / git commit || git checkout appdev2 / git pull origin main / git commit || git merge appdev2 main / git commit
S: git merge main / git commit -m "Merged main into appdev2"
@@MAD2-11-7
O: Redis can only store strings || Redis is an in-memory data structure store, often used as a cache or message broker || Redis is a relational database queried with SQL || Redis is slower than API databases (in-memory)
S: Redis is an in-memory data structure store, often used as a cache or message broker
@@MAD2-11-8
O: Backend validation of user input; never execute user text as code || Store auth token/JWT in cookies || Use v-html for user data || Send cookies with every request
S: Backend validation of user input; never execute user text as code
@@MAD2-11-12
C: (fetch gets 404; options repeat the stem lines)
O: Promise rejects automatically || Promise resolves and response.ok = true || Promise resolves and response.ok = false || Promise stays as pending
S: Promise resolves and response.ok = false
@@MAD2-11-13
C: const p = Promise.resolve(1)
C: .then(v => { console.log("A", v); return v + 1; })
C: .then(v => { console.log("B", v); throw "err"; })
C: .catch(e => { console.log("C", e); return 10; })
C: .then(v => console.log("D", v));
C: console.log("END");
O: END / A 1 / B 2 / C err / D 10 || A 1 / B 2 / END / C err / D 10 || END / A 1 / C err / D 10 || END / A 1 / B 2 / C err
S: END / A 1 / B 2 / C err / D 10
@@MAD2-11-14
C: let arr = [1, 2, 3]; let result = arr.map(x => x * 2).filter(x => x > 4); console.log(result);
O: [2, 4, 6] || [6] || [4, 6] || [1, 2, 3]
S: [6]
@@MAD2-11-15
C: const obj = { x:50, getX() { return this.x; } }; const fn = obj.getX.bind({ x:7 }); console.log(fn());
O: 50 || undefined || Error || 7
S: 7
@@MAD2-11-16
C: const User = { template:`<div><h2>User {{ $route.params.id }}</h2><router-view></router-view></div>` };
C: const Overview = { template:`<p>User Overview</p>` }; const Orders = { template:`<p>User Orders</p>` };
C: routes: [{ path:"/user/:id", component:User, children:[{ path:"", component:Overview }, { path:"orders", component:Orders }] }]
C: Visit #/user/10/orders.
O: User Orders || User 10 User Overview || User 10 User Orders || Nothing is rendered (siblings overwrite parent)
S: User 10 User Orders
@@MAD2-11-17
C: const setTheme = (theme) => { localStorage.setItem('theme', theme); console.log('Theme set to:', theme); };
C: const getTheme = () => { return localStorage.getItem('theme') || 'light'; };
C: setTheme('dark'); console.log(getTheme());
C: (set dark, refresh once, close tab, reopen)
O: Theme lost (tab close clears localStorage) || Theme preserved as "dark" (localStorage persists) || Theme undefined (refresh clears) || Theme resets to "light" (new tab)
S: Theme preserved as "dark" (localStorage persists)
@@MAD2-11-18
O: v-if removes the element from DOM when false, v-show only changes CSS display || v-show removes from DOM, v-if only changes CSS || Both re-mount and re-run lifecycle hooks || Both identical, different names
S: v-if removes the element from DOM when false, v-show only changes CSS display
@@MAD2-11-19
C: const processString = (str) => { return new Promise((resolve) => { setTimeout(() => resolve(str.toUpperCase()), 100); }); };
C: Promise.resolve('hello').then(processString).then(result => result + ' WORLD').then(console.log).catch(err => console.log('Error:', err));
O: hello || hello WORLD || HELLO WORLD || An error will be thrown
S: HELLO WORLD
@@MAD2-11-20
C: let originalConfig = { apiUrl:'https://api.example.com', timeout:5000 };
C: let configCopy = originalConfig; configCopy.timeout = 10000;
C: configCopy = { apiUrl:'https://api2.example.com', timeout:3000 };
C: console.log(originalConfig.timeout);
O: 5000 || 3000 || 10000 || undefined
S: 10000
@@MAD2-11-21
O: In a regular function, "this" is always bound to the global object || In an arrow function, "this" is inherited from the enclosing lexical scope || The .call() method can explicitly set "this" || In a method called on an object, "this" always refers to that object regardless of definition
S: arrow-inherits option || .call()-sets option
@@MAD2-11-22
O: The component will throw a critical error and crash || The computed property will return undefined (not mounted yet) || The route parameter will not be accessible || The component will display data from the previously loaded route
S: The component will display data from the previously loaded route
@@MAD2-11-23
C: const saveToken = (token) => { sessionStorage.setItem('authToken', token); };
C: const getToken = () => { return sessionStorage.getItem('authToken') || null; };
C: (login, store, close browser completely, reopen)
O: Token preserved in new session || Token cleared (sessionStorage dies on close) || Token partially available || Token moves to localStorage
S: Token cleared (sessionStorage dies on close)
@@MAD2-11-24
C: class BaseComponent { constructor(name){ this.name = name; } }
C: class AdvancedComponent extends BaseComponent { constructor(name, role){ super(name); this.role = role; } }
C: const comp = new AdvancedComponent('Alice', 'admin');
C: console.log(comp.__proto__ === AdvancedComponent.prototype);
C: console.log(comp.__proto__.__proto__ === BaseComponent.prototype);
C: console.log(comp instanceof BaseComponent);
C: console.log(comp instanceof AdvancedComponent);
O: true true true true || true false true true || false true true false || true true false false
S: true true true true
@@MAD2-11-25
O: Webhooks guarantee exact-order processing || Redis suits it (in-memory, fast cache) || Webhooks auto-retry on failure || Webhooks use HTTP POST asynchronously
S: Redis-suits option || Webhooks-POST option
@@MAD2-11-26
C: (expensive computed: s = sum 0..9999999 + a + b; calculate() sets time)
@@MAD2-11-27
O: expensive() runs again because the DOM updates || expensive() does NOT run again (dependencies unchanged) || Vue recomputes all computed on any state change || Nothing is displayed
S: expensive() does NOT run again (dependencies unchanged)
@@MAD2-11-28
O: When this.time changes || The user clicks anywhere on the DOM || Either this.a or this.b changes || When Date.now() changes
S: Either this.a or this.b changes
@@MAD2-11-29
O: Reduced CPU usage || Faster rendering || Avoids unnecessary recomputation || Makes all computations asynchronous
S: Reduced CPU usage || Faster rendering || Avoids unnecessary recomputation
@@MAD2-11-30
C: (User-router-watcher demo: /user/:id, watch $route.params.id → userId)
@@MAD2-11-31
O: The route changes to /user/2 but userId does not update || The watcher updates userId to "2", and the <p> displays it instantly || The router-view still shows User 1 (watchers don't re-render) || An error occurs ($route.params.id cannot be watched)
S: The watcher updates userId to "2", and the <p> displays it instantly
@@MAD2-11-32
O: Without it, userId would never change when the route changes || Required because Vue Router does not auto-update component data || Both of the above are correct
S: Both of the above are correct
@@MAD2-11-33
C: const ProductList = { template:`<div>{{ filteredProducts }}</div>`,
C: data(){ return { allProducts:[{id:1,name:'Laptop',category:'electronics'},{id:2,name:'Novel',category:'books'},{id:3,name:'Phone',category:'electronics'}], displayedProducts:null } },
C: computed:{ filteredProducts(){ return this.allProducts.filter(p => p.category === this.$route.params.category); } },
C: watch:{ '$route.params.category': function(newCategory){ this.displayedProducts = this.filteredProducts; } } }
@@MAD2-11-34
O: An empty array because displayedProducts is initialized as null || All three products because the watch handler hasn't been triggered yet
S: (solved line not shown; computed drives template → filtered list renders)
NOTE: options as printed; template uses filteredProducts (reactive) — watch only syncs the spare copy.
@@MAD2-11-35
NOTE: Q35 was beyond rendered pages; stem/options from text layer above if present.
