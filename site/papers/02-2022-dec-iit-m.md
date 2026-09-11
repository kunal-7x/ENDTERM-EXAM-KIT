# MAD2 — 2022 Dec  IIT M

*37 questions · transcribed from official practice paper (text layer + vision-checked)*

Legend: **Accepted answer** = the paper's own key (SA numerics). MCQ/MSQ keys are NOT printed in papers — answers: see the kit's RATTA / MCQ-MASTER files.

## Q1 · `640653451609` · MCQ · 0.0 marks

THIS IS QUESTION PAPER FOR THE SUBJECT "DIPLOMA LEVEL: MODERN APPLICATION DEVELOPMENT 2 (COMPUTER BASED EXAM)". ARE YOU SURE YOU HAVE TO WRITE EXAM FOR THIS SUBJECT?

**Options:**

- YES

- NO

*Answer: YES (0-mark confirmation — click YES and move on).*

## Q2 · `640653451617` · MCQ · 2.0 marks

*[stem on image — see EXTRA below]*

**Options:**
- …mapState(['state_1', 'state_2', 'state_3'])
- mapState(['state_1', 'state_2', 'state_3'])
- Both …mapState(['state_1', 'state_2', 'state_3']) and mapState(['state_1','state_2', 'state_3'])
- A Vue component cannot access Vuex store state.


**Code / figure:**

```
const store = new Vuex.Store({ state:{ stateA:10, stateB:20, stateC:30 } })
Vue.component('Vuex-demo', { template:`<div>state A:{{stateA}} state B:{{stateB}} state C:{{stateC}}</div>`, computed: code })
```

## Q3 · `640653451619` · MCQ · 2.0 marks

Suppose you are writing an application to be used by lakhs of people, which will run a brute force algorithm and gives back the result to the user of the application when ready. Considering this context, arrange the below set of actions/operations to achieve a desirable and practical design. I. Invoke the webhook II. Relieve the worker III. Dispatch a backend job

**Options:**
- I, III, II
- III, I, II
- I, II, III
- The polling will be a better design.


## Q4 · `640653451622` · MCQ · 2.0 marks

Which of the following statements is true?

**Options:**
- The CSRF protection is enforced by the flask framework, by default.
- The data stored in local storage is synchronized across the devices for a givenuser.
- A flask application returns CORS headers for cross domain javascript requests,by default.
- None of these

## Q5 · `640653451625` · MCQ · 2.0 marks

Suppose you want to store some data on the client, which has to be sent back to the server with every subsequent request. Which of the following is the most suited for this purpose?

**Options:**
- Local Storage
- Session Storage
- Cookie
- Any of these can be used


## Q6 · `640653451627` · MCQ · 2.0 marks

*[stem on image — see EXTRA below]*

**Options:**

- http://origin2.com
- http://api.origin2.com
- http://origin1.com/api/
- All of these


## Q7 · `640653451628` · MCQ · 2.0 marks

Which of the following is true regarding session cookies?

**Options:**
- They get deleted once the user closes the browser’s window.
- They will be sent to the origin server with each request, by default.
- They will not be sent to the origin server with each request, by default.
- All of these.

## Q8 · `640653451611` · MCQ · 3.0 marks

*[stem on image — see EXTRA below]*

**Code / figure:**

```
for (var i=1; i<4; i+=2) setTimeout(() => console.log(i), 0)
```

**Options:**

- 13
- 123
- 55
- 555


## Q9 · `640653451629` · MCQ · 3.0 marks

*[stem on image — see EXTRA below]*

**Options:**
- Cross Site Scripting
- Cross Site Request Forgery
- Session Hijacking
- None of these

## Q10 · `640653451630` · MCQ · 3.0 marks

*[stem on image — see EXTRA below]*

**Options:**

- Name: Rohit, City: Mumbai 277403
- None of these

*Note: question body was on a missing render page; only tail options visible.*


## Q11 · `640653451631` · MCQ · 3.0 marks

*[stem on image — see EXTRA below]*

**Options:**
- Name: , City: , Pin:
- Name: Rohit, City: Mumbai, Pin: 277403

## Q12 · `640653451632` · MCQ · 3.0 marks

*[stem on image — see EXTRA below]*

**Options:**
- Boiling Water ….
- Boiling Water ….Making Coffee
- Boiling Water ….Making Tea
- Making CoffeeBoiling Water ….


**Code / figure:**

```
const promiseFactory = (isShopOpen) => { return new Promise((resolve, reject) => {
setTimeout(() => { if (isShopOpen) { resolve('Making Coffee') } else { reject('Making Tea') } }, 1000) }) }
const bringTea = promiseFactory(true)
bringTea.then((data) => { console.log(data) }).catch((data) => { console.log(data) })
console.log('Boiling Water ....')
```

## Q13 · `640653451636` · MCQ · 3.0 marks

*[stem on image — see EXTRA below]*

*Note: question body was on a missing render page (p008).*




## Q14 · `640653451615` · MCQ · 4.5 marks

*[stem on image — see EXTRA below]*

**Options:**
- Rejected [‘quiz1]Minimum Time taken: 10 seconds
- Rejected [‘quiz1]Minimum Time taken: 8 seconds
- Resolved [‘quiz1]Minimum Time taken: 8 seconds
- Resolved [‘quiz1]Minimum Time taken: 10 seconds


**Code / figure:**

```
exams = ['quiz1', 'quiz2', 'enterm']
new Promise((rej, res) => { let count = 2; let a = setInterval(() => { count += 3; exams.pop();
if (count % 2) { exams.push('endterm') } else if (count % 7 == 0) { clearInterval(a); rej(); } }, 2000) })
.then(d => console.log("Rejected", exams)).catch(e => console.log("Resolved", exams))
```

## Q15 · `640653451616` · MCQ · 4.5 marks

Suppose you open “index.html” file in a browser, and type the text “EndTermExam” in the text box shown (after removing the previous text, if any), and hard refresh the page thrice, without clicking anywhere. What will be the value shown in the text box, and the “marks” placeholder, respectively?

**Code / figure:**

```
(localStorage AppDev/marks app; typing without clicking, hard refresh thrice)
mounted resets subject="AppDev", marks=50; if(localStorage.marks){subject+="2"; marks=localStorage.marks+20} else{subject+="1"; marks+=20}
```

**Options:**

- AppDev1, 80
- AppDev2, 80
- AppDev1, 70
- AppDev2, 70


## Q16 · `640653451623` · MCQ · 4.5 marks

*[stem on image — see EXTRA below]*

*Note: question body was on missing render pages (p011/p012).*




## Q17 · `640653451624` · MCQ · 4.5 marks

*[stem on image — see EXTRA below]*

**Options:**
- Checkpoint 4 11Checkpoint 6 undefinedCheckpoint 2 25
- Checkpoint 4 11Checkpoint 6 25Checkpoint 2 125
- Checkpoint 3 5Checkpoint 4 ErrorCheckpoint 6 undefinedCheckpoint 2 NaN
- Checkpoint 3 5Checkpoint 4 ErrorCheckpoint 6 NaNCheckpoint 2 NaN

## Q18 · `640653451618` · MSQ · 2.0 marks

Which of the following statement(s) is/are true in the context of point-to-point communication and message broker?

**Options:**
- In point-to-point communication, the number of connections grow with theorder of O(nlogn).
- If a central message broker is used, the number of connections grow with theorder of O(logn).
- If a central message broker is used, the number of connections grow with theorder of O(n).
- A message broker makes the network more scalable, if compared with point-to-point communication.

## Q19 · `640653451620` · MSQ · 2.0 marks

Which of the following statement(s) is/are true regarding caching?

**Options:**
- A shared cache is generally suitable for storing the personalized responses.
- A private cache is usually tied to a specific client.
- The caching helps in improving the performance of a web application.
- All of these

## Q20 · `640653451610` · MSQ · 3.0 marks

Which of the following statement(s) is/are true regarding javascript language?

**Options:**
- JavaScript is a high level programming language.
- JavaScript moves the declaration of all the arrow functions to the top of theirscope.
- The language does not allow the global declaration of user defined functions.
- A function can be invoked inside another function in the language.


## Q21 · `640653451612` · MSQ · 3.0 marks

*[stem on image — see EXTRA below]*

**Options:**
- The classes, namely “classA” and “classB” will always be applied to the divelement.
- The class, namely “classB” will always be applied to the div element.
- The class, namely “classA” will only be applied to the div element, if the variable“isClassA” evaluates to true.
- The class, namely “classB” will only be applied to the div element, if no variablewith name “isClassA” exists.

## Q22 · `640653451614` · MSQ · 3.0 marks

If an application is entirely built on the client end using javascript (without a database). Which of the following statements is/are false?

**Options:**
- All the progress will always be lost on the force reload of the page.
- All the progress may not necessarily be lost on the force reload of the page.
- The application will not allow force reload of the page.
- The progress made in a machine can be accessed on another machine.


## Q23 · `640653451621` · MSQ · 3.0 marks

Which of the following statement(s) is/are false in the context of scaling a web application?

**Options:**
- Scaling out is always a preferred choice when the network traffic is growing.
- The horizontal scaling will typically clone the application as many times asrequired, and add a load balancer to maintain
- uniform traffic across the servers.
- The horizontal partitioning splits a given table into multiple tables, with eachtable having the same structure.
- The diagonal scaling refers to cloning the application first, and then scaling upthe different servers to meet the
- requirements.

## Q24 · `640653451626` · MSQ · 3.0 marks

Which of the following statement(s) is/are false?

**Options:**
- A flask application runs in a threaded mode by default.
- A fetch API call always returns a promise.
- The promise returned by fetch API resolves to an HTTP response status 500,with the “ok” property of the response set to
- true.
- A headless CMS aims to manage both the content and frontend via APIs.

## Q25 · `640653451613` · MSQ · 4.5 marks

*[stem on image — see EXTRA below]*

**Options:**
- This : 39 , Normal : 39
- This : undefined , Normal : 39
- This : undefined , Normal : 50
- This : 39 , Normal : 50

## Q26 · `640653451637` · COMPREHENSION · 0.0 marks

*[stem on image — see EXTRA below]*

**Code / figure:**

```
(book-slot component: currentslot prop, $emit('book'), status toggle; slot starts {id:1, status:true})
```


## Q27 · `640653451638` · MCQ · 3.0 marks

*[stem on image — see EXTRA below]*

**Options:**

- Slot ID: 1, Slot Status: Booked
- Slot ID: 1, Slot Status: Not Booked
- Slot ID: 1
- Slot Status: Booked


## Q28 · `640653451639` · MCQ · 3.0 marks

Suppose the application is running on ‘http://localhost:8080'. What will be rendered by the browser inside the div element with ID ‘slot-detail’, when user clicks on the button with the text ‘Book’ 3 times (except the button)?”

**Options:**
- Slot ID: 1, Slot Status: Booked
- Slot ID: 1, Slot Status: Not Booked
- Slot ID: 1
- Slot Status: Booked

## Q29 · `640653451643` · COMPREHENSION · 0.0 marks

Based on the above data, answer the given subquestions.

**Code / figure:**

```
const Booking = { template:`<div><div>Slot Booking</div><router-view /></div>` }
const Error = { template:`<div>Page not Found</div>` }; const Booked = { template:`<div>Unbooked Slots</div>` }
const unBooked = { template:`<div>Booked Slots</div>` }
routes: [{ path:'/', component:Booking, children:[{path:'booked',component:Booked},{path:'unbooked',component:unBooked},{path:'*',component:Error}] }]
```


## Q30 · `640653451644` · MCQ · 3.0 marks

*[stem on image — see EXTRA below]*

**Options:**

- Page not Found
- Booked Slots
- Unbooked Slots
- None of these


## Q31 · `640653451645` · MCQ · 3.0 marks

*[stem on image — see EXTRA below]*

**Options:**
- Page not Found
- Booked Slots
- Unbooked Slots
- None of these

## Q32 · `640653451633` · COMPREHENSION · 0.0 marks

*[stem on image — see EXTRA below]*

**Code / figure:**

```
new Vue({ el:'#app', data:{ slots:[{id:1,date:new Date('December 19'),status:false},{id:2,date:new Date('December 17'),status:true}] },
computed:{ recent(){ return this.slots.sort((a,b) => b.date - a.date) }, booked(){ return this.slots.filter(slot => slot.status) } } })
template: v-for slot in recent → slot.date.getDate(); v-for slot in booked → slot.id
```


## Q33 · `640653451634` · MCQ · 4.5 marks

*[stem on image — see EXTRA below]*

**Options:**

- 1917
- 19
- 17
- 1719


## Q34 · `640653451635` · MCQ · 3.0 marks

*[stem on image — see EXTRA below]*

**Options:**
- 12
- 1
- 2
- None of these

## Q35 · `640653451640` · COMPREHENSION · 0.0 marks

*[stem on image — see EXTRA below]*

**Code / figure:**

```
(slotComp: slots with string status 'true'/'false'; availableSlots filters status == $route.params.status && id > offset)
```


## Q36 · `640653451641` · MCQ · 4.5 marks

*[stem on image — see EXTRA below]*

*Note: question body/options were on a missing render page (p023).*




## Q37 · `640653451642` · MCQ · 4.5 marks

*[stem on image — see EXTRA below]*

**Options:**
- 1. Slot12. Slot2
- 1. Slot22. Slot3
- 1. Slot1
- 1. Slot2
