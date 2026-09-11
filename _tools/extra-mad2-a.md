@@MAD2-1-4
NOTE: question content was on a missing render page (p003); stem/options from text layer above if present.
@@MAD2-1-5
NOTE: question content was on a missing render page (p003); stem/options from text layer above if present.
@@MAD2-1-6
NOTE: question content was on a missing render page (p003); stem/options from text layer above if present.
@@MAD2-1-7
O: It is a protocol to allow access to resources, hosted on a different server, on behalf of a user || It is used for authorization || It is used for authentication || None of these
@@MAD2-1-8
O: Closure is the state of the outer function || Closure is the state of a variable || Closure is a function along with its lexical environment or surrounding state || Closures are created every time a function is created in JavaScript
@@MAD2-1-9
C: const arr = [1, 2, 3, 4, 5, 6, 7, 8]
C: const arr1 = arr.map(r => r**3)
C: const arr2 = arr1.filter(r => ((r % 3 == 2) || (r % 4 == 3)))
C: console.log(arr2)
O: [1, 8, 125, 343, 512] || [8, 27, 64, 343, 512] || [8, 27, 125, 343, 512] || None of these
@@MAD2-1-10
C: index.html: <div id="app"><input v-model="name" @input="do_something"><p>{{age}}</p></div>
C: app.js: new Vue({ el:"#app", data:{ name:"#app", age:0 },
C: mounted(){ try{ this.name = localStorage.getItem("name").split(" ")[0]; this.age = localStorage.getItem("name").split(" ")[1]; }
C: catch{ this.name="Default"; this.age="Default"; } },
C: methods:{ do_something(){ localStorage.setItem("name", this.name); localStorage.setItem("age", this.age); } } })
O: The app will show an error in the console || Default, Default || IIT, Madras || None of these
@@MAD2-1-11
O: The flask framework enforces CSRF protection by default || The CORS mechanism allows a developer to secure a web application from external origins || The CORS headers are generally prefixed with the value "Access-Control-Allow" || An anti CSRF token must be sent with the request, if CSRF protection is enabled
@@MAD2-1-12
C: index.html: <div id="app"><div :class="{onstrike:changeStrike}" id="run">{{run}}</div>
C: <button @click="run+=4">Six</button><button @click="run+=3">Four</button></div>
C: app.js: new Vue({ el:'#app', data:{ run:0 }, computed:{ changeStrike(){ return this.run % 2 === 0 ? true : false } } })
C: CSS: .onstrike { color: blue; }
O: Black || Blue || White || None of these
@@MAD2-1-13
C: index.html: <div id="app"><Home class="bold" /></div>
C: app.js: Vue.component('Home', { template: `<div class='active'>IITM online degree</div>` }); new Vue({ el:'#app' })
C: CSS: .active{color:blue} .bold{font-weight:bold}
O: blue, normal || black, normal || blue, bold || black, bold
@@MAD2-1-14
C: app.js: new Vue({ el:'#app', data:{ partnerShip:210, contributions:[{player:'Rohit',run:100},{player:'Kohli',run:110}] } })
C: template: v-for="cont in contributions": {{cont.player}}: {{cont.run}}/{{partnerShip}}
O: Rohit: 100/210Kohli: 110/210 || Rohit: 0.48Kohli: 0.52 || Rohit: 100Kohli: 110 || None of these
@@MAD2-1-15
O: 23467 || 246 || 37 || None of these
NOTE: app.js code was on a missing render page; same family as Q31 (Numbers filter → 246).
@@MAD2-1-16
C: Vue.component('custom-input', { props:['value'], template:`<input v-bind:value="value" v-on:input="$emit('input', $event.target.value)">` })
C: new Vue({ el:'#app', data:{ searchText:'type something ...' } }); div#result shows "Searching for: {{searchText}}"
O: Searching for: || Apple || Searching for: 'type something ...' || Searching for: Apple
@@MAD2-1-17
C: const Profile = { template: `<div>Welcome {{this.$route.params.name}}</div>` }
C: const Home = { template:`<div>This is home page <button @click='goToProfile'>Go to profile</button></div>`,
C: methods:{ goToProfile(){ this.$router.push({ name:'profile', params:{ name:'narendra' } }) } } }
C: routes: [{ path:'/profile/:name', name:'profile', component:Profile }, { path:'/', component:Home }]
O: Welcome narendra || Welcome || narendra || None of these
@@MAD2-1-18
O: MoviesSome Error || MoviesSoley || MoviesDexter
NOTE: app.js was on a missing render page; options transcribed from image.
@@MAD2-1-19
C: Vue.component('custom-comp', { data(){ return { name:'Rohit Sharma' } }, template:`<div>Welcome {{name}}</div>` })
C: new Vue({ el:'#app', mounted(){ this.$refs.custom.name = 'Virat Kohli' } })
O: Welcome Rohit Sharma || Welcome Virat Kohli || Welcome || None of these
@@MAD2-1-20
C: data: { classObj:{ classA:true, classB:false }, classA:true, classB:false }
O: <div :class='{classA : classA, classB : classB}'> </div> || <div :class="{classA : 'classA', classB : 'classB'}"></div> || <div :class="classObj"> </div> || <div :class="(classObj)"></div>
@@MAD2-1-22
O: The approach 1 will wait for a user input before dispatching the task || The approach 2 will dispatch after waiting 10 seconds and start execution || The approach 2 will immediately dispatch but start execution after 10 seconds || The approach 1 will immediately dispatch and start execution
@@MAD2-1-25
C: new Promise((reject, resolve) => { let a = 2*4 || 0/4; let b = 3*4 && 0/4; if (a > b) resolve(a); else reject(b); })
C: .then(d => console.log("Passed:", d)).catch(e => console.log("Failed:", e))
C: .finally(d => { console.log("About to finish"); return "Over"; }).then(d => console.log("Finished !!", d))
O: Failed: 2About to finishFinished !! Over || Passed: 0About to finishFinished !! undefined || Passed: 0About to finishFinished !! Over || Failed: 8About to finishFinished !! undefined
@@MAD2-1-26
NOTE: Vuex shortlist code image was on a missing render page (p019).
@@MAD2-1-27
C: let propA = 10;
C: const obj1 = { propA:20, propB:function(){ console.log(propA, this.propA) } }
C: const obj2 = { propA:30, propB:function(){ let func = () => console.log(propA, this.propA); func() } }
C: obj2.propB.call(obj1);
O: 10 30 || 10 20 || 10 undefined || The program will raise an error
@@MAD2-1-28
C: async function some(){ let promise = await new Promise((res, rej) => { setTimeout(() => res("Execution Started"), 1000) });
C: let a = await promise; let b = a.replace("e", ""); return new Promise((rej, res) => { let c = a + "\n" + b; rej(c); }) }
C: some().then(d => console.log(d)).catch(e => console.log("Error")); console.log("Executing")
O: ExecutingExecution StartedExecution StartedTime: 2 seconds || Execution StartedExcution StartedExecutingTime: 2 seconds || ExecutingExecution StartedExcution StartedTime: 0 seconds || Execution StartedExcution StartedExecutingTime: 0 seconds
@@MAD2-1-29
C: const p = function(t){ return new Promise((resolve, reject) => { setTimeout(() => { resolve(t) }, t*1000) }) }
C: data = []; asyncFunc = async function(){ p1 = await p(1); p2 = await p(2); data.push(p2); data.push(p1) }
C: asyncFunc(); data.push('Outer'); console.log(data)
O: ['Outer', 2, 1] || ['Outer', 1, 2] || [2, 1, 'Outer'] || ['Outer']
@@MAD2-1-30
C: (same run-computed app as Q12: run 0, Six→run+=4, Four→run+=3)
O: 24 || 34 || 48 || None of these
@@MAD2-1-31
C: Vue.component('Numbers', { template:`<div><span v-for="num in numbers">{{num}}</span></div>`, props:['numbers'] })
C: new Vue({ el:'#app', data:{ numbers:[2,3,4,6,7], collType:'typeOne' },
C: computed:{ typeOne(){ return this.numbers.filter((num) => num % 2 === 0) }, typeTwo(){ return this.numbers.filter((num) => num % 2 != 0) } } })
C: template shows Numbers with v-show per collType
O: 23467 || 246 || 37 || None of these
@@MAD2-1-32
NOTE: question body/options were on missing pages; header only.
@@MAD2-2-2
C: const store = new Vuex.Store({ state:{ stateA:10, stateB:20, stateC:30 } })
C: Vue.component('Vuex-demo', { template:`<div>state A:{{stateA}} state B:{{stateB}} state C:{{stateC}}</div>`, computed: code })
O: ...mapState(['state_1', 'state_2', 'state_3']) || mapState(['state_1', 'state_2', 'state_3']) || Both || A Vue component cannot access Vuex store state
@@MAD2-2-3
O: I, III, II || III, I, II || I, II, III || The polling will be a better design
@@MAD2-2-5
O: Local Storage || Session Storage || Cookie || Any of these can be used
@@MAD2-2-6
O: http://origin2.com || http://api.origin2.com || http://origin1.com/api/ || All of these
@@MAD2-2-8
C: for (var i=1; i<4; i+=2) setTimeout(() => console.log(i), 0)
O: 13 || 123 || 55 || 555
@@MAD2-2-10
O: Name: Rohit, City: Mumbai 277403 || None of these
NOTE: question body was on a missing render page; only tail options visible.
@@MAD2-2-12
C: const promiseFactory = (isShopOpen) => { return new Promise((resolve, reject) => {
C: setTimeout(() => { if (isShopOpen) { resolve('Making Coffee') } else { reject('Making Tea') } }, 1000) }) }
C: const bringTea = promiseFactory(true)
C: bringTea.then((data) => { console.log(data) }).catch((data) => { console.log(data) })
C: console.log('Boiling Water ....')
O: Boiling Water .... || Boiling Water ....Making Coffee || Boiling Water ....Making Tea || Making CoffeeBoiling Water ....
@@MAD2-2-13
NOTE: question body was on a missing render page (p008).
@@MAD2-2-14
C: exams = ['quiz1', 'quiz2', 'enterm']
C: new Promise((rej, res) => { let count = 2; let a = setInterval(() => { count += 3; exams.pop();
C: if (count % 2) { exams.push('endterm') } else if (count % 7 == 0) { clearInterval(a); rej(); } }, 2000) })
C: .then(d => console.log("Rejected", exams)).catch(e => console.log("Resolved", exams))
O: Rejected ['quiz1']Minimum Time taken: 10 seconds || Rejected ['quiz1']Minimum Time taken: 8 seconds || Resolved ['quiz1']Minimum Time taken: 8 seconds || Resolved ['quiz1']Minimum Time taken: 10 seconds
@@MAD2-2-15
C: (localStorage AppDev/marks app; typing without clicking, hard refresh thrice)
C: mounted resets subject="AppDev", marks=50; if(localStorage.marks){subject+="2"; marks=localStorage.marks+20} else{subject+="1"; marks+=20}
O: AppDev1, 80 || AppDev2, 80 || AppDev1, 70 || AppDev2, 70
@@MAD2-2-16
NOTE: question body was on missing render pages (p011/p012).
@@MAD2-2-20
O: JavaScript is a high level programming language || JavaScript moves the declaration of all the arrow functions to the top of their scope || The language does not allow the global declaration of user defined functions || A function can be invoked inside another function in the language
@@MAD2-2-22
O: The caching helps in improving the performance of a web application (single TRUE option; others about shared/private cache)
@@MAD2-2-26
C: (book-slot component: currentslot prop, $emit('book'), status toggle; slot starts {id:1, status:true})
@@MAD2-2-27
O: Slot ID: 1, Slot Status: Booked || Slot ID: 1, Slot Status: Not Booked || Slot ID: 1 || Slot Status: Booked
@@MAD2-2-28
O: Slot ID: 1, Slot Status: Booked || Slot ID: 1, Slot Status: Not Booked || Slot ID: 1 || Slot Status: Booked
@@MAD2-2-29
C: const Booking = { template:`<div><div>Slot Booking</div><router-view /></div>` }
C: const Error = { template:`<div>Page not Found</div>` }; const Booked = { template:`<div>Unbooked Slots</div>` }
C: const unBooked = { template:`<div>Booked Slots</div>` }
C: routes: [{ path:'/', component:Booking, children:[{path:'booked',component:Booked},{path:'unbooked',component:unBooked},{path:'*',component:Error}] }]
@@MAD2-2-30
O: Page not Found || Booked Slots || Unbooked Slots || None of these
@@MAD2-2-31
O: Page not Found || Booked Slots || Unbooked Slots || None of these
@@MAD2-2-32
C: new Vue({ el:'#app', data:{ slots:[{id:1,date:new Date('December 19'),status:false},{id:2,date:new Date('December 17'),status:true}] },
C: computed:{ recent(){ return this.slots.sort((a,b) => b.date - a.date) }, booked(){ return this.slots.filter(slot => slot.status) } } })
C: template: v-for slot in recent → slot.date.getDate(); v-for slot in booked → slot.id
@@MAD2-2-33
O: 1917 || 19 || 17 || 1719
@@MAD2-2-34
O: 12 || 1 || 2 || None of these
@@MAD2-2-35
C: (slotComp: slots with string status 'true'/'false'; availableSlots filters status == $route.params.status && id > offset)
@@MAD2-2-36
NOTE: question body/options were on a missing render page (p023).
