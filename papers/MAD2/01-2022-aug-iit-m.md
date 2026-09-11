# MAD2 — 2022 Aug  IIT M

*33 questions · transcribed from official practice paper (text layer + vision-checked)*

Legend: **Accepted answer** = the paper's own key (SA numerics). MCQ/MSQ keys are NOT printed in papers — answers: see the kit's RATTA / MCQ-MASTER files.

## Q1 · `640653354794` · MCQ · 0.0 marks

THIS IS QUESTION PAPER FOR THE SUBJECT "DIPLOMA LEVEL: MODERN APPLICATION DEVELOPMENT 2 (COMPUTER BASED EXAM)". ARE YOU SURE YOU HAVE TO WRITE EXAM FOR THIS SUBJECT?

**Options:**

- YES

- NO

*Answer: YES (0-mark confirmation — click YES and move on).*

## Q2 · `640653354795` · MSQ · 2.0 marks

Which of the following statement(s) is/are true regarding JavaScript language?

**Options:**
- JavaScript is a low level programming language.
- The “const” keyword can be used to declare objects with block level scope.
- Int, char are some primitive data types in the JavaScript language.
- The JavaScript language supports both the first order and higher orderfunctions.


## Q3 · `640653354801` · MSQ · 2.0 marks

Which of the following statement(s) is/are false?

**Options:**
- A web application must implement token based authentication to make theapplication secure.
- The JAMStack approach separates out the frontend from the backend, andthey both can be updated/modified
- independently without affecting the other.
- It is recommended to avoid the usage of verbs in the API data URLs.
- The idea behind bringing an API is to implement caching.

## Q4 · `640653354802` · MSQ · 2.0 marks

Which of the following statement(s) is/are true regarding Celery and Redis?

**Options:**
- A Celery system can only use Redis as the message broker.
- A Celery system may consist of a number of batch jobs.
- A Celery system needs worker(s) to execute tasks.
- All of these


*Note: question content was on a missing render page (p003); stem/options from text layer above if present.*

## Q5 · `640653354810` · MSQ · 2.0 marks

Which of the following statement(s) is/are true regarding webhooks and polling?

**Options:**
- A webhook uses HTTP protocol.
- The term “polling” generally refers to short polling.
- Webhooks are used for 1 way communication, unlike web sockets.
- In polling, the connection to the server is kept open, until the data is available.


*Note: question content was on a missing render page (p003); stem/options from text layer above if present.*

## Q6 · `640653354811` · MSQ · 2.0 marks

Which of the following statement(s) is/are true regarding cookies?

**Options:**
- Cookies are stored on the server.
- Cookies are stored on the browser.
- Browser sends the cookies to the origin server automatically in general.
- Client has to include cookies manually with the request, in general.


*Note: question content was on a missing render page (p003); stem/options from text layer above if present.*

## Q7 · `640653354813` · MSQ · 2.0 marks

Which of the following statement(s) is/are true regarding OAuth?

**Options:**
- It is a protocol to allow access to resources, hosted on a different server, onbehalf of a user.
- It is used for authorization.
- It is used for authentication.
- None of these

## Q8 · `640653354814` · MSQ · 2.0 marks

Which of the following is true regarding the Closure in JavaScript?

**Options:**
- Closure is the state of the outer function.
- Closure is the state of a variable.
- Closure is a function along with its lexical environment or surrounding state.
- Closures are created every time a function is created in JavaScript.


## Q9 · `640653354796` · MCQ · 3.0 marks

Which of the following shows the correct output if the javascript program written below is executed? Which of the following shows the correct output if the javascript program written below is executed?

**Options:**
- [1, 8, 125, 343, 512]
- [8, 27, 64, 343, 512]
- [8, 27, 125, 343, 512]
- None of these

**Code / figure:**

```
const arr = [1, 2, 3, 4, 5, 6, 7, 8]
const arr1 = arr.map(r => r**3)
const arr2 = arr1.filter(r => ((r % 3 == 2) || (r % 4 == 3)))
console.log(arr2)
```


## Q10 · `640653354799` · MCQ · 3.0 marks

Consider the following Vue application with markup “index.html” and javascript file “app.js”. Consider the following Vue application with markup “index.html” and javascript file “app.js”. Suppose you open “index.html” file in a browser, and type the text “IIT Madras” in the text box shown (after removing the previous text, if any), and hard refresh the page twice, without clicking anywhere. What will be the value shown in the text box, and the “age” placeholder, respectively?

**Options:**
- The app will show an error in the console
- Default, Default
- IIT, Madras
- None of these

**Code / figure:**

```
index.html: <div id="app"><input v-model="name" @input="do_something"><p>{{age}}</p></div>
app.js: new Vue({ el:"#app", data:{ name:"#app", age:0 },
mounted(){ try{ this.name = localStorage.getItem("name").split(" ")[0]; this.age = localStorage.getItem("name").split(" ")[1]; }
catch{ this.name="Default"; this.age="Default"; } },
methods:{ do_something(){ localStorage.setItem("name", this.name); localStorage.setItem("age", this.age); } } })
```


## Q11 · `640653354804` · MCQ · 3.0 marks

Which of the following statements is false regarding CORS and CSRF?

**Options:**
- The flask framework enforces CSRF protection by default.
- The CORS mechanism allows a developer to secure a web application fromexternal origins.
- The CORS headers are generally prefixed with the value “Access-Control-Allow”.
- An anti CSRF token must be sent with the request, if CSRF protection isenabled.

## Q12 · `640653354817` · MCQ · 3.0 marks

Consider the following Vue application with markup “index.html” and javascript file “app.js”. Consider the following Vue application with markup “index.html” and javascript file “app.js”.

**Code / figure:**

```
index.html: <div id="app"><div :class="{onstrike:changeStrike}" id="run">{{run}}</div>
<button @click="run+=4">Six</button><button @click="run+=3">Four</button></div>
app.js: new Vue({ el:'#app', data:{ run:0 }, computed:{ changeStrike(){ return this.run % 2 === 0 ? true : false } } })
CSS: .onstrike { color: blue; }
```

**Options:**

- Black
- Blue
- White
- None of these


## Q13 · `640653354818` · MCQ · 3.0 marks

Consider the following Vue application with markup “index.html” and javascript file “app.js”.

**Code / figure:**

```
index.html: <div id="app"><Home class="bold" /></div>
app.js: Vue.component('Home', { template: `<div class='active'>IITM online degree</div>` }); new Vue({ el:'#app' })
CSS: .active{color:blue} .bold{font-weight:bold}
```

**Options:**

- blue, normal
- black, normal
- blue, bold
- black, bold


## Q14 · `640653354819` · MCQ · 3.0 marks

Consider the following Vue application with markup “index.html” and javascript file “app.js”. Consider the following Vue application with markup “index.html” and javascript file “app.js”.

**Code / figure:**

```
app.js: new Vue({ el:'#app', data:{ partnerShip:210, contributions:[{player:'Rohit',run:100},{player:'Kohli',run:110}] } })
template: v-for="cont in contributions": {{cont.player}}: {{cont.run}}/{{partnerShip}}
```

**Options:**

- Rohit: 100/210Kohli: 110/210
- Rohit: 0.48Kohli: 0.52
- Rohit: 100Kohli: 110
- None of these


## Q15 · `640653354821` · MCQ · 3.0 marks

Consider the following Vue application with markup “index.html” and javascript file “app.js”.

**Options:**

- 23467
- 246
- 37
- None of these

*Note: app.js code was on a missing render page; same family as Q31 (Numbers filter → 246).*


## Q16 · `640653354822` · MCQ · 3.0 marks

Consider the following Vue application with markup “index.html” and javascript file “app.js”. Consider the following Vue application with markup “index.html” and javascript file “app.js”. Suppose the user types “Apple” in the input box (after removing the existing text, if any). What will be rendered inside the div with ID “result”?

**Options:**
- Searching for:
- Apple
- Searching for: ‘type something …’

**Code / figure:**

```
Vue.component('custom-input', { props:['value'], template:`<input v-bind:value="value" v-on:input="$emit('input', $event.target.value)">` })
new Vue({ el:'#app', data:{ searchText:'type something ...' } }); div#result shows "Searching for: {{searchText}}"
```


## Q17 · `640653354823` · MCQ · 3.0 marks

Consider the following Vue application with markup “index.html” and javascript file “app.js”. Consider the following Vue application with markup “index.html” and javascript file “app.js”.

**Code / figure:**

```
const Profile = { template: `<div>Welcome {{this.$route.params.name}}</div>` }
const Home = { template:`<div>This is home page <button @click='goToProfile'>Go to profile</button></div>`,
methods:{ goToProfile(){ this.$router.push({ name:'profile', params:{ name:'narendra' } }) } } }
routes: [{ path:'/profile/:name', name:'profile', component:Profile }, { path:'/', component:Home }]
```

**Options:**

- Welcome narendra
- Welcome
- narendra
- None of these


## Q18 · `640653354824` · MCQ · 3.0 marks

Consider the following Vue application with markup “index.html” and javascript file “app.js”. Consider the following Vue application with markup “index.html” and javascript file “app.js”.

**Options:**

- MoviesSome Error
- MoviesSoley
- MoviesDexter

*Note: app.js was on a missing render page; options transcribed from image.*


## Q19 · `640653354826` · MCQ · 3.0 marks

Consider the following Vue application with markup “index.html” and javascript file “app.js”. Consider the following Vue application with markup “index.html” and javascript file “app.js”. What will be rendered inside the “custom-comp” component?

**Options:**
- Welcome Rohit Sharma
- Welcome Virat Kohli
- Welcome
- None of these

**Code / figure:**

```
Vue.component('custom-comp', { data(){ return { name:'Rohit Sharma' } }, template:`<div>Welcome {{name}}</div>` })
new Vue({ el:'#app', mounted(){ this.$refs.custom.name = 'Virat Kohli' } })
```


## Q20 · `640653354797` · MSQ · 3.0 marks

Which of the following is the correct way to do class binding in Vue (to apply ‘classA’ on the div element), if the data object in the Vue constructor is defined as below? Which of the following is the correct way to do class binding in Vue (to apply ‘classA’ on the div element), if the data object in the Vue constructor is defined as below?

**Code / figure:**

```
data: { classObj:{ classA:true, classB:false }, classA:true, classB:false }
```

**Options:**

- <div :class='{classA : classA, classB : classB}'> </div>
- <div :class="{classA : 'classA', classB : 'classB'}"></div>
- <div :class="classObj"> </div>
- <div :class="(classObj)"></div>


## Q21 · `640653354803` · MSQ · 3.0 marks

Which of the following statement(s) is/are false?

**Options:**
- The server sent events is a mechanism for a server to push events, and it mustrequire service workers on the client to
- function properly.
- In general, a webhook is meant to pull message(s) from an application.
- The usage of a message broker over “point-to-point” communication makesthe application scalable.
- There is no difference between webhooks and short polling.

## Q22 · `640653354806` · MSQ · 3.0 marks

*[stem on image — see EXTRA below]*

**Options:**

- The approach 1 will wait for a user input before dispatching the task
- The approach 2 will dispatch after waiting 10 seconds and start execution
- The approach 2 will immediately dispatch but start execution after 10 seconds
- The approach 1 will immediately dispatch and start execution


## Q23 · `640653354809` · MSQ · 3.0 marks

Which of the following statement(s) is/are false regarding Vuex and Vue router?

**Options:**
- In general, an application should have separate Vuex stores for all thecomponents.
- A path defined in the routes array in Vue router can consist of a number ofchildren paths.
- The wildcard (*) should be put at the top of the routes array in the Vue router,so that it matches with all the paths, which
- are not implemented.
- A Vuex store must be used with all Vue applications.

## Q24 · `640653354812` · MSQ · 3.0 marks

Which of the following statement(s) is/are true regarding fetch API?

**Options:**
- The credentials property of the Request interface allows the user agent tosend or receive cookies in cross-origin requests.
- The value “omit” of “credentials” will force the browser not to send cookies withthe request.
- The value “include” of “credentials” will allow the browser to send credentialseven in cross-origin requests.
- The value “include” of “credentials” will allow the browser to send credentialsonly for same origin requests.

## Q25 · `640653354798` · MCQ · 4.5 marks

*[stem on image — see EXTRA below]*

**Code / figure:**

```
new Promise((reject, resolve) => { let a = 2*4 || 0/4; let b = 3*4 && 0/4; if (a > b) resolve(a); else reject(b); })
.then(d => console.log("Passed:", d)).catch(e => console.log("Failed:", e))
.finally(d => { console.log("About to finish"); return "Over"; }).then(d => console.log("Finished !!", d))
```

**Options:**

- Failed: 2About to finishFinished !! Over
- Passed: 0About to finishFinished !! undefined
- Passed: 0About to finishFinished !! Over
- Failed: 8About to finishFinished !! undefined


## Q26 · `640653354800` · MCQ · 4.5 marks

*[stem on image — see EXTRA below]*

*Note: Vuex shortlist code image was on a missing render page (p019).*




## Q27 · `640653354805` · MCQ · 4.5 marks

Consider the following javascript program, and predict the output, if executed. Consider the following javascript program, and predict the output, if executed.

**Options:**
- 10 30
- 10 20
- 10 undefined
- The program will raise an error

**Code / figure:**

```
let propA = 10;
const obj1 = { propA:20, propB:function(){ console.log(propA, this.propA) } }
const obj2 = { propA:30, propB:function(){ let func = () => console.log(propA, this.propA); func() } }
obj2.propB.call(obj1);
```


## Q28 · `640653354807` · MCQ · 4.5 marks

Consider the following javascript program, and predict the output, if executed. Also, predict the minimum time taken (in seconds) to log the value “Executing” on the console.

**Code / figure:**

```
async function some(){ let promise = await new Promise((res, rej) => { setTimeout(() => res("Execution Started"), 1000) });
let a = await promise; let b = a.replace("e", ""); return new Promise((rej, res) => { let c = a + "\n" + b; rej(c); }) }
some().then(d => console.log(d)).catch(e => console.log("Error")); console.log("Executing")
```

**Options:**

- ExecutingExecution StartedExecution StartedTime: 2 seconds
- Execution StartedExcution StartedExecutingTime: 2 seconds
- ExecutingExecution StartedExcution StartedTime: 0 seconds
- Execution StartedExcution StartedExecutingTime: 0 seconds


## Q29 · `640653354815` · MCQ · 4.5 marks

Consider the following JavaScript program. Consider the following JavaScript program. What will be logged on to the console?

**Code / figure:**

```
const p = function(t){ return new Promise((resolve, reject) => { setTimeout(() => { resolve(t) }, t*1000) }) }
data = []; asyncFunc = async function(){ p1 = await p(1); p2 = await p(2); data.push(p2); data.push(p1) }
asyncFunc(); data.push('Outer'); console.log(data)
```

**Options:**

- ['Outer', 2, 1]
- ['Outer', 1, 2]
- [2, 1, 'Outer']
- ['Outer']


## Q30 · `640653354816` · MCQ · 4.5 marks

Consider the following Vue application with markup “index.html” and javascript file “app.js”. Consider the following Vue application with markup “index.html” and javascript file “app.js”. Consider the following Vue application with markup “index.html” and javascript file “app.js”. What will be rendered inside the div for ID “run”, if the user clicks on the button with text “Six”, 3 times and the button with text “Four”, 4 times?

**Code / figure:**

```
(same run-computed app as Q12: run 0, Six→run+=4, Four→run+=3)
```

**Options:**

- 24
- 34
- 48
- None of these


## Q31 · `640653354820` · MCQ · 4.5 marks

Consider the following Vue application with markup “index.html” and javascript file “app.js”. Consider the following Vue application with markup “index.html” and javascript file “app.js”.

**Code / figure:**

```
Vue.component('Numbers', { template:`<div><span v-for="num in numbers">{{num}}</span></div>`, props:['numbers'] })
new Vue({ el:'#app', data:{ numbers:[2,3,4,6,7], collType:'typeOne' },
computed:{ typeOne(){ return this.numbers.filter((num) => num % 2 === 0) }, typeTwo(){ return this.numbers.filter((num) => num % 2 != 0) } } })
template shows Numbers with v-show per collType
```

**Options:**

- 23467
- 246
- 37
- None of these


## Q32 · `640653354825` · MCQ · 4.5 marks

Consider the following Vue application with markup “index.html” and javascript file “app.js”.

*Note: question body/options were on missing pages; header only.*




## Q33 · `640653354808` · MCQ · 2.0 marks

Which of the following statement(s) is/are correct regarding cookies, local storage, and session storage?

**Options:**
- The local storage is a browser based persistent storage.
- Cookies are preferred over session or local storage, when the data needs to besent with every request.
- The cookies can be set from the server as well as using javascript on the client.
- All of these
