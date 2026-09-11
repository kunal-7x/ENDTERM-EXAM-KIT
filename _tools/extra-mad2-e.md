@@MAD2-10-1
O: "this" in an arrow function refers to the global object || "this" inside a regular function refers to the object that owns the function || Arrow functions do not have their own "this" and inherit it from the surrounding scope || "this" always points to the window object in browser environments
S: Arrow functions do not have their own "this" and inherit it from the surrounding scope
@@MAD2-10-2
C: let arr = [1, 2, 3]; let sum = arr.reduce((acc, val, idx, array) => acc + val, 0); console.log(sum);
O: 0 || 3 || 6 || 9 || 12
S: 6
@@MAD2-10-3
O: JWTs require server-side storage for each session || JWTs are stateless and eliminate the need for server-side session storage || JWTs are longer and contain more data than session IDs || JWTs automatically handle token expiration without additional logic
S: JWTs are stateless and eliminate the need for server-side session storage
@@MAD2-10-4
O: GET || POST || PUT || DELETE
S: GET
@@MAD2-10-5
C: export const strikeRate = (runs, balls) => { return (runs / balls) * 100; };
C: export const playerName = "Virat Kohli";
O: import strikeRate, playerName from "./battingStats.js"; || import { strikeRate, playerName } from "./battingStats.js"; || import * as stats from "./battingStats.js"; || require("./battingStats.js");
S: import { strikeRate, playerName } from "./battingStats.js";
@@MAD2-10-6
O: Encryption keys used to secure the token || User-related data (claims) such as identity and expiration time || The algorithm used for signing the token || The hashed signature of the token
S: User-related data (claims) such as identity and expiration time
@@MAD2-10-7
C: const promise = new Promise((resolve, reject) => { resolve('Success!'); reject('Error!'); });
C: promise.then(console.log).catch(console.log);
O: Success! || Error! || Success! Error! || Error! Success!
S: Success!
@@MAD2-10-8
C: const store = new Vuex.Store({ state:{ items:['Angular','Vue'] },
C: mutations:{ addItem(state, item){ state.items.push(item); } },
C: actions:{ addItemAsync({ commit }, item){ setTimeout(() => { commit('addItem', item); }, 500); } } });
O: ['Angular','Vue'] || ['Angular','Vue','React'] || ['React'] || ['Angular']
S: ['Angular','Vue','React']
@@MAD2-10-9
C: routes: [{ path:'/home', component:Home }, { path:'/about', component:About }, { path:'*', redirect:'/about' }]
O: Browser navigates to /random and shows a blank page || Browser navigates to /random but renders nothing || Browser redirects to /about and displays "About" || Error: No matching route
S: Browser redirects to /about and displays "About"
@@MAD2-10-10
C: console.log(typeof NaN); console.log(typeof null); console.log(NaN == null); console.log(NaN === null);
O: number, object, false, false || NaN, null, true, true || number, object, true, false || NaN, null, false, false
S: number, object, false, false
@@MAD2-10-11
NOTE: question body was on a missing render (p007); stem/options from text layer above if present.
@@MAD2-10-12
C: const person = { firstName:'John', lastName:'Doe', age:30, city:'New York' };
C: const { firstName, city, ...rest } = person;
C: const newPerson = { firstName, location:city, ...rest };
C: console.log(firstName); console.log(rest); console.log(newPerson);
O: John { city:'New York', lastName:'Doe', age:30 } { firstName:'John', location:'New York', city:'New York', lastName:'Doe', age:30 } || John { lastName:'Doe', age:30 } { firstName:'John', location:'New York', lastName:'Doe', age:30 } || John { lastName:'Doe', age:30 } { firstName:'John', location:'New York', city:'New York', lastName:'Doe', age:30 } || undefined { firstName:'John', city:'New York', lastName:'Doe', age:30 } { firstName:'John', location:'New York' }
S: John { lastName: 'Doe', age: 30 } { firstName: 'John', location: 'New York', lastName: 'Doe', age: 30 }
@@MAD2-10-13
C: (flask_caching SimpleCache: @cache.memoize(timeout=300) compute_data sleeps 5s; requests for user IDs 1, 2, 1 within 5 min)
O: 15 seconds || 10 seconds || 5 seconds || 0 seconds
S: 10 seconds
@@MAD2-10-14
C: const CAPACITY = 75; const TOTAL_PEOPLE = 213;
C: function allocatePeople(){ return new Promise((resolve, reject) => { let slots = [0,0,0]; let remaining = TOTAL_PEOPLE;
C: for (let i = 0; i < slots.length; i++) { if (remaining >= CAPACITY) { slots[i] = CAPACITY; remaining -= CAPACITY; } else { slots[i] = remaining; remaining = 0; } }
C: reject(slots); }); }
C: async function startAllocation(){ try{ const result = await allocatePeople(); console.log("Passed " + JSON.stringify(result)); }
C: catch(error){ console.log("Failed " + JSON.stringify(error)); } }
C: startAllocation();
O: Passed [75,75,63] || Failed [0,0,0] || Failed [75,75,63] || Passed [0,0,0]
S: Failed [75,75,63]
@@MAD2-10-15
C: Match: 1.v-if→? 2.v-for→? 3.v-bind→? 4.v-model→? with A.two-way binding | B.conditional render | C.bind attributes | D.render list
O: 1-A, 2-D, 3-C, 4-B || 1-D, 2-B, 3-C, 4-A || 1-B, 2-C, 3-D, 4-A || 1-B, 2-D, 3-C, 4-A
S: 1-B, 2-D, 3-C, 4-A
@@MAD2-10-18
C: new Vue({ el:'#app', template:'<div>Status: {{status}}<br>Value: {{value}}</div>', data:{ status:"Initial", value:10 },
C: beforeCreate(){ this.status = this.status + " -> Created"; this.value = this.value + 5 },
C: beforeMount(){ this.status = this.status + " -> Ready"; this.value = this.value - 2 },
C: created(){ this.status = this.status + " -> Mounted"; this.value = this.value * 2 },
C: mounted(){ this.status = this.status + " -> Done"; this.value = this.value / 2 } })
O: Status: Initial → Created → Ready → Mounted → Done Value: 13 || Status: Initial → Ready → Mounted → Done Value: 8 || Status: Initial → Created → Mounted → Ready → Done Value: 14 || Status: Initial → Mounted → Ready → Done Value: 9
S: Status: Initial → Mounted → Ready → Done Value: 9
NOTE: hook ORDER in output follows data-mutation sequence quirk; solved value as shown.
@@MAD2-10-19
C: (@app.route('/api/open') open; @auth_required('token') /api/secure; @auth_required + @roles_required('superuser') /api/superuser)
C: Requests: GET /api/open (no auth) → ?; GET /api/secure (no auth) → ?; GET /api/superuser (valid token, role 'basic') → ?
O: 200, 200, 200 || 200, 401, 403 || 200, 403, 401 || 401, 403, 403
S: 200, 401, 403
@@MAD2-10-20
C: function inventory(){ const item = { name:"Polycab", stats:{ power:20 } };
C: const ref1 = item; const ref2 = { ...item }; const ref3 = { name:item.name, stats:{ ...item.stats } };
C: ref1.name = "Ambrane"; ref2.stats.power = 50; ref3.stats.power = 30;
C: console.log(item.name); console.log(item.stats.power); console.log(ref2.stats.power); console.log(ref3.stats.power); }
C: inventory();
O: Ambrane 20 50 30 || Polycab 50 50 30 || Ambrane 50 50 30 || Ambrane 50 30 30
S: Ambrane 50 50 30
@@MAD2-10-21
C: const obj = { value:100, outerFunc:function(){ const innerFunc = () => { console.log(this.value); }; return innerFunc; },
C: otherFunc:function(){ console.log(this.value); } };
C: const func1 = obj.outerFunc(); const func2 = obj.outerFunc; const func3 = obj.otherFunc;
C: func1(); func2()(); func3();
O: 100 100 100 || 100 undefined 100 || undefined undefined undefined || 100 undefined undefined
S: 100 undefined undefined
@@MAD2-10-22
NOTE: question body was on a missing render (p015); only partial options (50, 50) visible.
@@MAD2-10-23
C: (Vuex store: state.packed [], ADD_ITEM mutation; component computed Line X, methods packItem Line Y)
O: Line X packedItems() { return this.store.state.packed; } / Line Y this.store.commit || Line X packedItems() { return this.$store.state.packed; } / Line Y this.$store.commit || Line X packedItems() { return this.$store.packed; } / Line Y this.commit || Line X packedItems: this.$store.state.packed / Line Y dispatch
S: Line X packedItems() { return this.$store.state.packed; } / Line Y this.$store.commit("ADD_ITEM", item)
@@MAD2-10-25
C: (Flask + Flask-JWT-Extended: POST /login {username:Jassi} → token; GET /stats @jwt_required returns Welcome user)
O: /stats returns "Welcome Jassi" only with valid JWT in Authorization header || No token → unauthorized error || Token must be sent as JSON in body || None of these
S: Valid-JWT-header option || No-token-unauthorized option
@@MAD2-10-26
O: git checkout -b feature-branch || git add . || git commit -m "Initial commit" || git push origin feature-branch || git branch feature-branch && git checkout main || git push feature-branch origin
S: git checkout -b feature-branch || git add . || git commit -m "Initial commit" || git push origin feature-branch
@@MAD2-10-27
C: (Assignments component fetches /api/assignments in created(); sidebar instant, main slow)
O: The sidebar is likely part of a parent component already rendered || The Assignments component waits for the API response || Vue blocks rendering of all components until API calls complete || The delay is caused by async fetch after created
S: sidebar-parent option || waits-for-API option || async-fetch option
@@MAD2-10-28
C: new Vue({ el:"#app", data:{ a:1, b:2, time:0 },
C: computed:{ bigNumber(){ console.log("computed run"); let s = 0; for (let i = 0; i < 10000000; i++) s += i; return s + this.a + this.b; } },
C: methods:{ calculate(){ this.time = Date.now(); } } })
@@MAD2-10-29
O: 0 || 1 || Multiple times due to the loop || Depends on user interaction
S: 1
@@MAD2-10-30
C: calculate() { this.a = this.a + 1; }
O: bigNumber() will not run again || bigNumber() will run again because a dependency changed || Only time will update || Vue will throw an error
S: bigNumber() will run again because a dependency changed
@@MAD2-10-31
O: Computed properties are always faster than methods || Methods cannot access data properties || Computed properties are cached based on their dependencies || Computed properties run only once
S: Computed properties are cached based on their dependencies
@@MAD2-10-32
C: const Item = { template:'<p>Item ID from route: {{ $route.params.id }}</p>', updated(){ console.log("updated hook called"); } };
C: routes: [{ path:"/item/:id", component:Item }]; watch: { "$route.params.id"(newId){ this.currentId = newId; } }
C: Load #/item/1, click Item 2 link.
@@MAD2-10-33
O: The Item component is destroyed and recreated, so updated() is never called || The route changes, the component is reused, and updated() is called || The route changes, but neither watcher nor lifecycle hooks run || A new Vue instance is created for the route
S: The route changes, the component is reused, and updated() is called
@@MAD2-10-34
NOTE: question body was beyond rendered pages (p022+); stem/options from text layer above if present.
