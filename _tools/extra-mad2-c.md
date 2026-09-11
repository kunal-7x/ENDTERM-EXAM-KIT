@@MAD2-5-2
C: let langName = 'Python'; function showLanguage(){ let langName = "JavaScript"; let message = 'Learn ' + langName; console.log(message); }
C: let message = 'Learn ' + langName; console.log(message); console.log(showLanguage());
O: Learn JavaScript / Learn Python || Learn JavaScript / Learn JavaScript / undefined || Learn Python / Learn JavaScript || Learn Python / Learn JavaScript / undefined
@@MAD2-5-3
C: let x = [1, 'p', a => a + 1]; for (const i = 0; i<x.length; i++) { console.log(i, x[i], typeof(x[i])) }
O: It will throw error on the console for the very first iteration || It will display index/value/type for the first item then throw error || It will display the indices, values and types of all the items || None of these
@@MAD2-5-5
O: The language supports both first class and higher order functions || The language supports higher order functions, but not first class functions || A variable declared without var/let/const is not hoisted at all || Variables declared with let and const are also hoisted
@@MAD2-5-6
O: Client Side local storage || In Memory Cache || Session Cookies || Server Side Database
@@MAD2-5-8
C: let myQual = { degree:"B-tech", college:"IIT Delhi",
C: get qualification(){ return `degree: ${this.degree}, college: ${this.college}` },
C: set qualification(q){ let components = q.split(' '); this.degree = components[0]; this.college = components[1]; } }
O: console.log(myQual.qualification()) || console.log(myQual.qualification) || console.log(myQual.qualification = 'M-tech IIT-Madras') || console.log(myQual.qualification('M-tech IIT-Madras'))
@@MAD2-5-10
C: script.js: var app = new Vue({ el:'#app', data:{ result:false, final:false } })
C: index1.html: <h1 v-if="result">Hello am I visible?</h1>; index2.html: <h1 v-show="final">Hello am I visible?</h1>
O: <h2 v-for="item in items">{{item.name}}</h2> || <h2 v-for="item in items" {{item.id}}>{{item.name}}</h2> || <h2 v-for="item in items" :id="item.id">{{item.name}}</h2> || <h2 v-for="items" :id="item.id">item.name</h2>
NOTE: options belong to the v-for mad1/mad2/mad3 sub-question (script.js items list); correct = :id binding option.
@@MAD2-5-13
C: class Twowheeler { constructor(name){ this.name=name; this.gear=4; this.seating=2; }
C: get description(){ return `${this.name} has ${this.gear} gear and has ${this.engine} engine.` } }
C: class Moped extends Twowheeler { constructor(name){ super(name); this.engine='4 stroke' } }
C: let myBike = new Twowheeler("Discover"); let myDrive = new Moped("Activa")
C: console.log(myDrive.description); console.log(myBike.description)
O: Discover...4 stroke / Activa...4 stroke || Activa...undefined / Discover...4 stroke || Activa...4 stroke / Discover...undefined || Discover...undefined / Activa...undefined
@@MAD2-5-14
C: function parentFunc(name){ return { sayHello:()=>"Hi! "+name, sayBye:()=>"Bye! "+name, changeName:(newName)=>{ name=newName; } }; }
C: const arpan = parentFunc("Arpan"); const beli = parentFunc("Beli")
C: console.log(arpan.sayHello()); console.log(beli.sayHello()); arpan.changeName("Beli"); console.log(arpan.sayBye());
O: Hi! Arpan / Bye! Arpan || Hi! Arpan / Hi! Beli / Bye! Beli || Hi! Arpan / reference Error || Reference Error
@@MAD2-5-15
C: (two Vue instances #app1 (title App No 1, computed greetings) and #app2 (title App No 2); #app1 nested inside #app2 element)
O: App No 1 / hello from App No 1 / App No 2 / hello from App No 2 || App No 2 / hello from App No 2 || App No 1 / App No 2 || Blank page
@@MAD2-5-16
C: var var1 = 25; var var2 = 35;
C: const myObj = { var2:45, var1:35, ObjFunc:function(var3){ let var4 = var3**2; return 10 + this.var2 + var4; } }
C: let m = myObj.ObjFunc; console.log(m.bind()(5)); console.log(m.call(myObj,6))
O: 70 / 81 || 70 / 91 || 80 / 81 || 80 / 91
@@MAD2-5-23
O: To prevent unauthorized access to confidential data || To mitigate cross-site scripting (XSS) attacks || To enable controlled access to resources from different origins || To protect against SQL injection attacks
@@MAD2-5-24
C: let Obj1 = { subject:'Mechanics', stream:'Physics' }; let Obj2 = Obj1; let Obj3 = {};
C: for (let key in Obj1){ Obj3[key] = Obj1[key]; }
C: Obj2.subject = 'Thermodynamics'; Obj3.stream = 'Chemistry'; console.log(Obj1)
O: { subject:'Thermodynamics', stream:'Physics' } || { subject:'Mechanics', stream:'Chemistry' } || { subject:'Mechanics', stream:'Physics' } || { subject:'Thermodynamics', stream:'Chemistry' }
@@MAD2-5-25
C: var var1 = 25;
C: const exObj = { var2:45, var1:35, inObj:{ var1:45, inObjFunc:()=>{ return "Value is " + this.var1; } },
C: exObjFunc:function(){ let var2 = 10; return "Value is " + this.var2; } }
C: let x = exObj.inObj; console.log(x.inObjFunc()); console.log(exObj.exObjFunc())
O: Value is 35 / Value is 10 || Value is 35 / Value is 45 || Value is 25 / Value is 10 || Value is 25 / Value is 45
@@MAD2-5-26
O: Uncaught ReferenceError: extFunc is not defined / Now I am loaded, let's support / callback function executed here / loaded and run from external script
NOTE: only this option was visible; scenario = dynamic script + immediate extFunc() call (throws first).
@@MAD2-5-27
C: Array.prototype.double = function(arr){ const res = []; for (let i=0; i<placeholder.length; i++) res.push(placeholder[i]*2); return res; }
C: const arr = [2, 3, 7, 8]; console.log(arr.double()); // target output [4, 6, 14, 16]
O: arr || Array || this || The program cannot yield such an output
@@MAD2-5-28
NOTE: question content was blank in render (lazy-load failure); unrecoverable.
@@MAD2-5-29
C: const cartModule = { state:{ items:[] }, mutations:{ addItem(state, item){ state.items.push(item); } },
C: actions:{ async addToCart({ commit }, item){ /* TODO */ } } }
O: addToCart({ commit }, item) { commit('addItem', item); } || addToCart({ state, commit }, item) { const existingItem = state.items.find(i => i.id === item.id); if (existingItem) { commit('addItem', existingItem); } else { commit('addItem', item); } } || addToCart({ commit }, item) { commit('addItem', { ...item }); } || All of these
@@MAD2-5-30
NOTE: question content was blank in render; continuation page missing; unrecoverable.
@@MAD2-6-2
O: A closure can access variables from its outer function even after the outer function has returned || A closure can be created when a function is defined inside another function || Closures are useful for data encapsulation and controlling access to private data || All of these
@@MAD2-6-3
C: console.log("Start"); setTimeout(function(){ console.log("Inside Timeout"); }, 0)
C: Promise.resolve().then(function(){ console.log("Inside Promise"); }); console.log("End");
O: StartInside Timeout Inside Promise End || StartInside Promise Inside Timeout End || StartEnd Inside Timeout Inside Promise || StartEnd Inside Promise Inside Timeout
@@MAD2-6-4
C: function Person(name){ this.name = name; }
C: Person.prototype.greet = function(){ console.log("Hello, " + this.name); };
C: const john = new Person("John"); john.greet(); delete john.greet; john.greet();
O: Hello, JohnTypeError: john.greet is not a function || Hello, JohnHello, undefined || TypeError...TypeError... || Hello, JohnHello, John
@@MAD2-6-5
C: new Vue({ el:'#app', data:{ user:{ name:'Abhi', age:30 } },
C: watch:{ user:{ handler(newValue, oldValue){ console.log('User object changed:', newValue); }, deep:true } } })
C: Execute: app.user.name = "Dev"
O: The watcher will not be triggered (nested property) || The watcher will be triggered and log the changed user object || The watcher will trigger but log only the new name value || The watcher will throw an error (deep watching unsupported)
@@MAD2-6-6
C: <template><div><p v-if="isVisible">This paragraph is visible</p><p v-else>This paragraph is hidden</p></div></template>
C: data: isVisible:true. Execute: this.isVisible = false
O: The "visible" paragraph will be displayed || The "hidden" paragraph will be displayed || Both paragraphs will be displayed || No change will happen
@@MAD2-6-7
C: response.set_cookie('session_id', 'abc123', secure=option1, samesite=option2)
O: secure=True and samesite='Strict' || secure=False and samesite='Strict' || secure=True and samesite='None' || secure=False and samesite='Lax'
@@MAD2-6-8
C: function addItemToCart(item){ let cart = JSON.parse(localStorage.getItem('cart')) || []; cart.push(item); localStorage.setItem('cart', JSON.stringify(cart)); }
C: function getCartItems(){ return JSON.parse(localStorage.getItem('cart')) || []; }
C: addItemToCart({ id:1, name:'Laptop' }.name); console.log(getCartItems());
C: (page loaded fresh, then refreshed twice = 3 runs)
O: [] || ['Laptop', 'Laptop', 'Laptop'] || [{ id:1, name:'Laptop' }] || [undefined]
@@MAD2-6-9
O: Long polling opens multiple connections, server continuously pushes realtime || Long polling = client repeatedly sends requests at fixed intervals || Long polling = single request held open until data available || Long polling uses WebSockets for persistent bidirectional connection
@@MAD2-6-10
O: All of these
NOTE: question body was on a missing render page; only tail option visible.
@@MAD2-6-12
C: Vue.component('child', { template:`<div><slot name="header" :info="info"></slot><slot :info="info"></slot></div>`,
C: data(){ return { info:{ title:'Hello', desc:'World' } } } })
O: <template v-slot:header="data">{{data.title}}</template> || <template v-slot:header="{ info }">{{info.title}}</template> || <template v-slot:header>{{info.title}}</template> || <template v-slot:header=info>{{info.title}}</template>
@@MAD2-6-13
C: Promise.resolve(1).then(x => x + 1).then(x => Promise.resolve(x + 1)).then(x => { throw 'error' }).catch(e => e + 4).then(x => console.log(x))
O: error4 || 7 || error || undefined
@@MAD2-6-14
C: async function test(){ console.log("Start"); const val = await Promise.resolve(5); console.log(val); return "End"; }
C: console.log("Begin"); test().then(data => console.log(data)); console.log("Finish");
O: Begin, Start, 5, End, Finish || Begin, Finish, Start, 5, End || Begin, Finish, Start, End, 5 || Begin, Start, Finish, 5, End
@@MAD2-6-15
O: @cache.memoize() caches function results based on arguments, while @cache.cached() caches entire views || @cache.cached() caches by arguments, while @cache.memoize() caches entire views || Both cache entire views, memoize uses Redis by default || Both identical, different syntax
@@MAD2-6-16
C: let x = [100, 'x', num => num + 1]; for (const i = 0; i<x.length; i++) { console.log(i, x[i], typeof(x[i])) }
O: It will display the indices, values and types of all the items || It will throw error for the very first iteration || It will display the first item then throw error || None of these
@@MAD2-6-18
C: const obj = { name:"Abhi", greet:function(){ console.log(this.name); } }; const greet = obj.greet; greet();
O: Abhi || undefined || null || Reference Error || Garbage Value
@@MAD2-6-19
C: const person = { firstName:"John", lastName:"Doe", fullName:function(){ return this.firstName + " " + this.lastName; } }
C: const newPerson = person.fullName.bind({ firstName:"Jane", lastName:"Smith" }); console.log(newPerson());
O: John Doe || Jane Smith || John Smith || Jane Doe || undefined || null || Reference Error
@@MAD2-6-21
C: function add(x){ return function(y){ return x + y; }; }; const addFive = add(5); console.log(addFive(10));
O: 5 || 10 || 15 || 20
@@MAD2-6-23
C: CSP Header: Content-Security-Policy: default-src 'self'; HTML: <script src="https://otherurl.com/code.js"></script>
O: The script from otherurl.com will load normally || The script will fail to load, and an error will be logged in the console || The browser will display a warning and allow the script to load || Nothing will happen; the CSP only affects inline scripts
@@MAD2-6-24
C: (grandparent > parent > child divs; ALL THREE listeners with capture:true logging GrandParent/Parent/Child; click "Child")
O: ChildParent GrandParent || Child || GrandParentParent Child || None of these
@@MAD2-6-25
C: const store = new Vuex.Store({ state:{ counter:0 }, mutations:{ increment(state){ state.counter++; } },
C: actions:{ async incrementAsync({ commit }){ await new Promise(resolve => setTimeout(resolve, 1000)); commit('increment'); } } })
C: Execute: this.$store.dispatch('incrementAsync');
O: The increment mutation will be called immediately after the dispatch || The state will be updated after the asynchronous operation completes || The action will execute synchronously, committing before the promise resolves || The action will be skipped since mutations cannot be called inside actions
@@MAD2-6-26
C: Vue.component('my-button', { template:`<button @click="handleClick"><slot></slot></button>`,
C: methods:{ handleClick(){ console.log('Button'); this.$emit('click') } } })
C: new Vue({ el:'#app', template:`<my-button @click="parentClick">Click me</my-button>`, methods:{ parentClick(){ console.log('Parent') } } })
C: Button pressed once.
O: Parent || Button || ButtonParent || ParentButton
@@MAD2-6-27
O: User: null || The error will be logged, Nothing will be displayed || User: Luke
NOTE: question body was on a missing render page; only options visible.
@@MAD2-6-29
C: let bsCourses = { subject:'MAD II', stream:'Programming' }; let esCourses = bsCourses; let msCourses = {};
C: for (let course in bsCourses){ msCourses[key] = bsCourses[key]; }
C: esCourses.subject = 'Embedded C'; msCourses.stream = 'Electronics'; console.log(msCourses)
O: { subject:'MAD II', stream:'Programming' } || { subject:'Embedded C', stream:'Electronics' } || { subject:'MAD II', stream:'Electronics' } || { subject:'Embedded C', stream:'Programming' }
NOTE: loop uses undefined variable `key` (ReferenceError in strict reading); options as printed.
@@MAD2-6-30
C: var var1 = 56;
C: const exObj = { var2:24, var1:15, inObj:{ var1:75, inObjFunc:()=>{ return "Value is " + this.var1; } },
C: exObjFunc:function(){ let var2 = 14; return "Value is " + this.var2; } }
C: let x = exObj.inObj; console.log(x.inObjFunc()); console.log(exObj.exObjFunc())
O: Value is 75 / Value is 24 || Value is 56 / Value is 24 || Value is 15 / Value is 14 || Value is 56 / Value is 14
@@MAD2-6-31
C: (same getter/setter myBox object as paper-5 Q8 with tool/cutter)
O: console.log(myBox.tools) || console.log(myBox.tools()) || console.log(myBox.tools('ScrewDriver Grinder')) || console.log(myBox.tools = 'ScrewDriver Grinder')
@@MAD2-6-32
C: (same v-if/v-show index1/index2 pair as paper-5 Q9)
O: When the directive v-if is falsy, it removes the entire element from the DOM || The raw HTML will be exactly the same when both values are set to true || The raw HTML will be exactly the same for the current state of data || When the directive v-show is falsy, it removes the entire element from the DOM
@@MAD2-6-33
NOTE: question content was blank in render; continuation page missing; unrecoverable.
@@MAD2-7-4
NOTE: question bodies were on a missing render page (p003); stems/options from text layer above if present.
@@MAD2-7-5
NOTE: question bodies were on a missing render page (p003); stems/options from text layer above if present.
@@MAD2-7-6
NOTE: question bodies were on a missing render page (p003); stems/options from text layer above if present.
@@MAD2-7-9
NOTE: question body was on a missing render page (p005); stem/options from text layer above if present.
@@MAD2-7-10
NOTE: question body was on a missing render page (p005); stem/options from text layer above if present.
@@MAD2-7-12
O: regularResult = 40, arrowResult = 40 || regularResult = undefined, arrowResult = undefined || regularResult = 40, arrowResult = undefined || regularResult = undefined, arrowResult = 40
NOTE: code = obj with num:40, regularFunction returning this.value, arrowFunction returning this.value.
@@MAD2-7-13
C: Approach 1: setInterval(title="Title A", 2000) + setInterval(title="Title B", 1000)
C: Approach 2: setInterval(title="Title A", 1000) + setInterval(title="Title B", 2000)
O: The approach 1 will toggle the page title between "Title A" and "Title B" after every 1 second (approx) || The approach 2 will toggle the page title between "Title A" and "Title B" after every 1 second (approx) || None of the approaches will toggle the page title after every 1 second || None of these
@@MAD2-7-18
O: <div :class="[isActive ? 'activeClass' : '', 'errorClass']"></div> || <div :class="[{ isActive : 'activeClass' }, 'errorClass']"></div> || <div :class="['activeClass' ? isActive : '', 'errorClass']"></div> || <div :class="[{'activeClass' : isActive }, 'errorClass']"></div>
@@MAD2-7-22
C: (Vue2 CDN component: input v-model newItem, Add button; addItem pushes (newItem, newItem); list starts ['Apple','Banana'])
C: Enter "Orange", click Add.
O: 1. Apple 2. Banana 3. Orange 4. Orange || 1. Apple 2. Banana 3. Orange || 1. Apple 2. Banana 3. Orange 3. Orange || 1. Apple 2. Banana
@@MAD2-7-23
C: localStorage.setItem('counter','0'); sessionStorage.setItem('total','5')
C: for (let i=0;i<3;i++){ let counter=localStorage.getItem('counter'); let total=sessionStorage.getItem('total'); counter+=2; total*=2; localStorage.setItem('counter',counter); sessionStorage.setItem('total',total); }
C: sessionStorage.clear(); console.log(localStorage.getItem('counter')); console.log(sessionStorage.getItem('total'));
O: 640 || null40 || 6null || 0222null
@@MAD2-7-24
C: class Animal { constructor(name){ this.name=name; } speak(){ console.log(`${this.name} makes a noise.`); } }
C: class Dog extends Animal { speak(){ console.log(`${this.name} barks`); } }
C: const d = new Dog('Rex'); d.speak(); console.log(d.__proto__ === Dog.prototype); console.log(d.__proto__.__proto__ === Animal.prototype);
O: Rex barkstrue true || Rex barksfalse true || Rex barks.true false || Rex barks.false false
@@MAD2-7-25
C: (flask_caching SimpleCache app: @cache.memoize(timeout=180) get_data sleeps 5s; visits at t=0, +2.5min, +3.5min same param)
O: 5 seconds || 0 seconds || 10 seconds || 180 seconds
@@MAD2-7-26
NOTE: question body was on a missing render page (p015); stem/options from text layer above if present.
@@MAD2-7-27
C: (Vuex store src/store/index.js: state.value, setValue mutation, fetchValue action resolving 'API Value'; App.vue dispatches on button, shows value)
O: (options on unrendered p017)
NOTE: options were on a missing render page; pattern = async action commits after await.
@@MAD2-7-29
C: (flask_caching redis app: @cache.cached(timeout=60, key_prefix='compute'); compute_value returns x*y; hits /compute/10/20 then /compute/5/10 within 60s)
O: {"result": 200} and {"result": 50} || {"result": 50} and {"result": 200} || {"result": 100} and {"result": 100} || {"result": 200} and {"result": 200}
@@MAD2-7-30
C: Snippet A: requests.get('https://some-api') + print json (plain API call)
C: Snippet B: Flask route POST /server-route reading request.json (webhook receiver shape)
C: Snippet C: Flask Response(stream(), mimetype='text/event-stream') yielding time lines (SSE shape)
C: Snippet D: while True: requests.get + sleep(10) (polling shape)
@@MAD2-7-31
O: A || B || C || D
@@MAD2-7-32
O: A || B || C || D
@@MAD2-7-33
C: index.html: <div id="app"><router-view></router-view></div><script src="script.js"></script>
NOTE: script.js and sub-questions were on a missing render page (p021).
@@MAD2-7-34
NOTE: sub-question was on a missing render page (p021).
@@MAD2-8-4
NOTE: question body was on a missing render page (p003); stem/options from text layer above if present.
@@MAD2-8-5
NOTE: only a tail option was visible ("WebSockets require an HTTP request for every message sent" — FALSE).
@@MAD2-8-6
NOTE: question body was on a missing render page (p003); stem/options from text layer above if present.
@@MAD2-8-7
O: GET || POST || DELETE || PATCH
@@MAD2-8-8
C: let arr = [1, 2, 3]; let sum = arr.reduce((acc, val, idx, array) => acc + array[idx + 1], 0); console.log(sum);
O: 6 || NaN || undefined || 0 || NULL
@@MAD2-8-9
C: const obj = { num:5, multiply:function(){ return this.num * 2; } }; const multiply = obj.multiply; console.log(multiply());
O: 10 || undefined || NaN || NULL || Error
@@MAD2-8-10
C: const store = new Vuex.Store({ state:{ items:[] }, mutations:{ addItem(state, item){ state.items.push(item); } },
C: actions:{ addItemAsync({ commit }, item){ setTimeout(() => { commit('addItem', item); }, 1000); } } })
C: Dispatch addItemAsync with "Vue.js"; state after 2 seconds?
O: [] || ["Vue.js", "Vue.js"] || ["Vue.js"] || [object]
@@MAD2-8-12
O: <alert-box title="Custom Title">Custom content</alert-box> || <alert-box><slot name="title">Custom Title</slot>Custom content</alert-box> || <alert-box><template v-slot:title>Custom Title</template>Custom content</alert-box> || <alert-box>Custom Title - Custom content</alert-box>
NOTE: component has named slot title + default slot.
@@MAD2-8-13
NOTE: question body/options were on a missing render page (p008); stem/options from text layer above if present.
@@MAD2-8-14
C: (same propA/propB/call(obj1) program as paper-1 Q27)
O: 10 30 || 10 undefined || 10 20 || The program will raise an error
@@MAD2-8-15
C: (flask_caching RedisCache: @cache.cached(timeout=100), get_data sleeps 25s; two hits to /data/apple within 50s)
O: 25 seconds || 35 seconds || 0 seconds || 15 seconds
@@MAD2-8-16
C: async function fetchData(){ try{ const response = await fetch('https://api.example.com/data');
C: if (!response.ok) throw new Error('HTTP error'); const data = response.json(); return data; }
C: catch(error){ if (error.name === 'TypeError') { return { status:'network error' }; } return { status:'http error' }; } }
C: Called; request gives 200 OK.
O: { status:'http error' } || { status:'network error' } || JSON data || The promise will remain pending
@@MAD2-8-17
C: console.log("variable1"); setTimeout(() => { console.log("variable2"); setTimeout(() => { console.log("variable3") }, 500); }, 2000); console.log("variable4")
O: variable1 / variable2 / variable3 / variable4 || variable1 / variable4 / variable3 / variable2 || variable1 / variable4 / variable2 / variable3 || variable1 / variable3 / variable4 / variable2
@@MAD2-8-19
C: (CORS Flask app allows origins http://localhost:5000 for /api/*; Vue frontend at :3000 fetches /api/data)
O: The request will be blocked due to CORS policy || The request will succeed and return {"message": "Hello from Flask"} || The request will fail because Vue.js does not support CORS || The server will crash due to incorrect CORS settings
@@MAD2-8-20
NOTE: Vuex setup body was on a missing render page (p014); stem/options from text layer above if present.
@@MAD2-8-21
O: [27, 125, 343] || None of these
NOTE: only tail options visible (map-cube-filter family).
@@MAD2-8-22
NOTE: question body was on a missing render page (p016); stem/options from text layer above if present.
@@MAD2-8-23
C: (two Vue instances: app1 (#app1, value1 VueJS value2 Frontend) nested inside app2 element (#app2, value3 JavaScript))
O: Frontend || VueJSFrontend || VueJSJavaScript || FrontendJavaScript
@@MAD2-8-24
C: index.html: <div id="app"><my-comp><slot>Hello Frontend</slot><slot>Hello VueJS</slot></my-comp></div>
C: script.js: const myComp = { template:`<div><slot></slot><slot></slot></div>` }
C: const app = new Vue({ components:{ "my-comp": myComp } }).$mount('#app')
O: Hello Frontend Hello Frontend || Hello VueJS Hello VueJS || Hello Frontend Hello Vue JS || Hello Frontend Hello Vue JS Hello Frontend Hello Vue JS
@@MAD2-8-25
NOTE: question body was on a missing render page (p019); stem/options from text layer above if present.
@@MAD2-8-28
O: The event loop runs on a separate thread from the main JavaScript execution || The event loop allows JavaScript to perform non-blocking operations despite being single-threaded || Callbacks from setTimeout are placed in the task queue and executed after the call stack is empty || All of these
@@MAD2-8-29
C: (Vuex store: state.count 0, increment mutation; component uses mapState(['count'])/mapMutations(['increment']) WITHOUT spread; Increment clicked 3 times)
O: (numeric answer input; paper key: 3)
NOTE: kit-verified answer 3 (spread dropped in render; code runs).
