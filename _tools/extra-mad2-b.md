@@MAD2-3-4
O: SMTP is a mail delivery protocol || SMTP is a protocol to retrieve email from an email server || IMAP is a mail delivery protocol || IMAP is a protocol to retrieve email from an email server
@@MAD2-3-5
O: Replit.com is an example of a javascript engine || The language supports the concept of first class functions || The language does not allow the implementation of user defined higher order functions || The language can be used for DOM manipulation
@@MAD2-3-7
O: With point-to-point communication, the number of connection links will grow as O(n) || ...will grow as O(n2) || With a central message broker, links will grow as O(n) || ...will grow as O(n2)
@@MAD2-3-10
O: v-for = "value in obj" || v-for = "(value, name) in obj" || v-for = "(value, name, index) in obj" || None of these
@@MAD2-3-11
O: https://abc.com || https://xyz.abc.com || https://abc.com/page || https://abc8.com
@@MAD2-3-16
C: function goUpDown(num){ return new Promise((res, rej) => { setTimeout(() => {
C: if (num < 20) { return num > 10 ? res('Go Up') : res('Go Down') } else { return rej('Number Too Large') } }, 1000) }) }
C: async function getData(){ const data3 = await goUpDown(8); const data2 = await goUpDown(15); const data1 = await goUpDown(12) }
C: getData().then((data) => { console.log(data) }, (err) => { console.log(err) })
O: Go Up || Go Down || Number Too Large || None of these
@@MAD2-3-17
C: async function getResponse(url){ try{ const response = await fetch(url)
C: try{ const data = await response.json(); if (response.ok) { return data } else { return response.status } }
C: catch{ return 'Network Error' } } catch{ return 'Response is not json' } }
C: getResponse('url').then((data) => { console.log(data) })
O: Response is not json || Network Error || 200 || None of these
@@MAD2-3-18
C: (same getResponse code as Q17; url returns JSON with 500 status)
O: Response is not json || Network Error || 404 || 500
@@MAD2-3-19
NOTE: code/options were on a missing render page (p010).
@@MAD2-3-20
C: (cart app: items Apple(count1,price10), Orange(count1,price5); inscreeaseCount += 2; addToCart pushes item; amount = sum(count*price); buy logs Success if amount <= totalAmount(50))
C: Clicks: Increase+AddToCart for Apple once, then Orange once, then Buy.
O: Success || Failure || NaN || None of these
@@MAD2-3-21
C: const Error = { template:`<div>Result Not Found</div>` }
C: const Dashboard = { template:`<div>This is dashboard of {{user}}</div>`, props:['user'] }
C: routes: [{ path:'/dashboard/:user', component:Dashboard, props:true }, { path:'*', component:Error }]
O: This is dashboard of User || This is dashboard of 7 || Dashboard || Result Not Found
@@MAD2-3-22
C: const Home = { template:`<div><slot name="navbar">This is navbar</slot><slot></slot><slot name="footer"></slot></div>` }
C: new Vue({ el:'#app', template:`<Home><template slot="footer">This is Footer</template><template slot="navbar">This is header</template><div>Welcome to exam</div></Home>`, components:{ Home } })
O: This is Footer / This is Header || This is Footer / This is Header / Welcome to exam || This is Header / This is Footer || This is Header / Welcome to Exam / This is Footer
@@MAD2-3-23
C: (flask_caching RedisCache app: @cache.cached(timeout=40), home() sleeps 30s; user1 visits, user2 visits 3 min later)
O: 0 seconds || 30 seconds || 120 seconds || None of these
@@MAD2-3-24
C: for (var i = 0; i < 3; i++) { setTimeout(() => console.log(i), (i+1)*1000); }
O: 0/1/2, Minimum Time Taken: 6 seconds || 0/1/2, Minimum Time Taken: 12 seconds || 3/3/3, Minimum Time Taken: 12 seconds || 3/3/3, Minimum Time Taken: 6 seconds
@@MAD2-3-25
C: async function func(){ const num = await Promise.resolve(2); console.log("Second"); return num; }
C: console.log("First"); func().then((data) => console.log(data)); console.log("Third");
O: First / Second / Third / 2 || First / Error || First / Third / Second / undefined || First / Third / Second / 2 || The output cannot be predicted
@@MAD2-3-26
NOTE: code/options were on a missing render page (p018).
@@MAD2-3-27
C: (same cart app as Q20; clicks: Increase Count on Apple 5 times, on Orange once, then Buy; nothing added to cart)
O: Success || Failure || NaN || None of these
@@MAD2-3-28
C: const Error = { template:`<div>Result Not Found</div>` }
C: (rest of app.js truncated in render; route /user question)
NOTE: app.js body was cut off in the render; options unknown.
@@MAD2-4-2
C: <table id="table_id"><tr><th>Name</th><th>Standard</th></tr>
C: <tr><td id="cell_id_1">Abhishek</td><td id="cell_id_2">10th</td></tr>
C: <tr><td id="cell_id_3">Narendra</td><td id="cell_id_4">11th</td></tr></table>
C: table listener (capture TRUE): "Table Clicked !!"; cell listener (capture TRUE): "Cell Clicked !!"
C: Click on cell "Abhishek".
O: Cell Clicked !! / Table Clicked !! || Table Clicked !! / Cell Clicked !! || Cell Clicked !! || Table Clicked !!
@@MAD2-4-3
C: (same table; BOTH listeners WITHOUT capture flag; click "Abhishek")
O: Cell Clicked !! / Table Clicked !! || Table Clicked !! / Cell Clicked !! || Cell Clicked !! || Table Clicked !!
@@MAD2-4-4
C: var first = 1;
C: obj1 = { 'first':2, 'second':function some(){ console.log(this.first); } }
C: obj2 = { 'first':3, 'second':function some(){ console.log("Function Invoked !!"); this.second(); } }
C: obj2.second.call(obj1);
O: Function Invoked !! / 1 || Function Invoked !! / 2 || Function Invoked !! / 3 || Infinite loop printing "Function Invoked !!"
@@MAD2-4-5
C: Match: 1.v-bind | 2.v-model | 3.v-cloak | 4.v-on  with  A.hide uncompiled mustache | B.two-way binding | C.bind HTML attribute to data | D.bind events
O: 1-A, 2-B, 3-C, 4-D || 1-C, 2-B, 3-D, 4-A || 1-C, 2-D, 3-A, 4-B || 1-C, 2-B, 3-A, 4-D
@@MAD2-4-6
NOTE: code/options failed to load in render (blank); question unrecoverable from text.
@@MAD2-4-7
C: const First = Vue.component("first", { template:`<div>Hello First Component !!</div>`, mounted(){ this.$router.push("/endpoint2"); } })
C: const Second = Vue.component("second", { template:`<div>Hello Second Component !!</div>` })
C: routes: [{path:"/endpoint1",component:First},{path:"/endpoint2",component:Second}]
C: Click link "Home" (router-link to /endpoint1).
O: Hello First Component !! || Hello Second Component !! || 404 || Blank Page
@@MAD2-4-8
C: new Promise((reject, resolve) => { if ("iitmiitm".split("iitm").length == 3) resolve("Promise is rejected"); else reject("Promise is resolved"); })
C: .then(data => console.log("Promise Rejected :", data), data => console.log("Promise Resolved :", data))
C: .then(data => { console.log("Value received from previous block :", data); return 34 })
C: .catch(error => console.log("Error caused :", error))
C: .finally(data => { console.log("In Finally block :", data); return 39 })
C: .then(data => console.log("Value received from previous block :", data))
O: Promise Resolved : Promise is resolved / Value : undefined / Finally : undefined / Value : 39 || Promise Resolved : Promise is rejected / Value : undefined / Finally : 34 / Value : 39 || Promise Resolved : Promise is rejected / Value : undefined / Finally : undefined / Value : 34 || Promise Rejected : Promise is resolved / Value : undefined / Finally : undefined / Value : 34
@@MAD2-4-9
C: (flask_caching RedisCache app: @cache.cached(timeout=100), get_name sleeps 30s; two hits to /name/mohan within 50s)
O: 30 Seconds || 40 Seconds || 0 Seconds || None of these
@@MAD2-4-10
C: function promoter(cgpa){ return new Promise((res, rej) => { if (cgpa > 9.0) { res() } else { rej() } }) }
C: promoter(8).then(() => { console.log('Promoted') }, () => { console.log('Not Promoted') }).finally(() => { console.log('Job Done') })
O: Not Promoted || Promoted || Not Promoted / Job Done || Promoted / Job Done
@@MAD2-4-11
C: new Vue({ el:'#app', template:`<div>{{message}}</div>`, data:{ message:null },
C: created(){ this.message = 'Hello from created' }, mounted(){ this.message = 'Hello from mounted' } })
O: Hello from created || Hello from mounted || null || None of these
@@MAD2-4-12
NOTE: app.js and options were on a missing render page; header only.
@@MAD2-4-13
O: Global execution context is created when the script starts to run || Function execution context is created when the script starts to run || A function execution context is created when the function is called || All of these
@@MAD2-4-14
O: Every object in JavaScript has a prototype || Prototype of an object can be null || Prototype of an object cannot be null || None of these
@@MAD2-4-15
O: The "await" can only be used inside an async function, except browser console || The "await" keyword is typically used to wait for a promise and get its fulfillment value || The "await" keyword pauses the async function till the promise is pending, while outside code runs || All of these
@@MAD2-4-16
O: A fetch call is capable of sending image data || The "Accept" header tells the server which content the client expects || A fetch call allows custom headers || All of these
@@MAD2-4-21
NOTE: code/options were blank in render (lazy-load failure); unrecoverable.
@@MAD2-4-22
C: (flask app threaded=False: /endpoint1 sleeps 20s, /endpoint2 sleeps 30s; browser fetches both at once)
C: Time for the SECOND fetch (endpoint2) to complete and log?
O: 20 seconds || 30 seconds || 10 seconds || 50 seconds
@@MAD2-4-23
C: (flask_caching RedisCache: @cache.cached(timeout=100) get_name sleeps 30s; hits to /name/mohan AND /name/sohan within 50s)
O: 30 Seconds || 40 Seconds || 0 Seconds || None of these
@@MAD2-4-24
C: new Vue({ el:'#app', template:`<div>Enter a point: <input v-model='point' /><div id='content'>{{(isOnCircle?"On the circle":"Not on the circle")}}</div></div>`,
C: data:{ point:null }, computed:{ isOnCircle(){ if(!this.point){ return false } const [x,y] = this.point.split(','); return x**2 + y**2 == 25 } } })
C: User enters '3,4'.
O: On the circle || Not on the circle || true || False
@@MAD2-4-25
C: (Home component with router-view; app.js code blank in render)
O: Name: std1, Course: mad1 || Name: std2, Course: mad2 || Name: std3, Course: mad1 || std1 / std2 / std3
NOTE: app.js code was blank in render; options as shown.
@@MAD2-4-26
C: (Home router-view app; app.js blank in render; URL /student/20)
O: Name: std1, Course: mad1 || Name: std2, Course: mad2 || Name: std3, Course: mad1 || std1 / std2 / std3
NOTE: app.js code was blank in render; options as shown.
@@MAD2-4-28
O: Approach 1 will finish faster than approach 2 || Approach 2 will finish faster || Both approaches comparable || Both comparable if only 1 worker
@@MAD2-4-29
O: The cache decorator does not include function parameters in the cache key || The memoize decorator does not include function parameters in the cache key || Requests without request bodies are generally not cacheable || Hard refreshing a page clears the browser cache for that page
@@MAD2-4-30
NOTE: code and continuation page missing (lazy-load failure); unrecoverable.
