@@MAD2-9-2
O: Messages will be dropped || Messages will accumulate in the queue || The consumer will speed up automatically || The producer will block until the consumer is ready
S: Messages will accumulate in the queue
@@MAD2-9-3
O: The component will reload when data changes || All function calls become asynchronous || It disables direct access to state || The DOM updates automatically when the underlying reactive data changes
S: The DOM updates automatically when the underlying reactive data changes
@@MAD2-9-4
O: It stores output in session storage || It enables token authentication || It sends compressed response headers || It skips route execution for repeated inputs
S: It skips route execution for repeated inputs
@@MAD2-9-5
O: To encrypt data between client and server || To compress HTTP responses || To authenticate users across applications || To control which domains can access resources
S: To control which domains can access resources
@@MAD2-9-6
O: Storing keys only in environment variables || Version pinning || Using only packages with over 1000 stars on GitHub || Reduce Dependencies
S: Version pinning || Reduce Dependencies
@@MAD2-9-7
O: The number of CSS selectors in the stylesheet || Use of semantic HTML tags || Number of HTTP requests made || File size of resources (like images, JS)
S: Number of HTTP requests made || File size of resources (like images, JS)
@@MAD2-9-8
O: A message broker makes the network scalable for adding more servers || A message broker allows two servers to directly communicate without an intermediary || A message broker is not suited for traffic spikes || A message broker can be used for batch processing
S: A message broker makes the network scalable || A message broker can be used for batch processing
@@MAD2-9-9
O: They enable real-time data delivery || They use HTTP POST requests typically || They're designed for server-to-server communication || They require polling from the client
S: They enable real-time data delivery || They use HTTP POST requests typically || They're designed for server-to-server communication
@@MAD2-9-10
NOTE: question + options were on a missing render page (p005); stem/options from text layer above if present.
@@MAD2-9-11
NOTE: question bodies (Q11-Q12) were on missing renders; stem/options from text layer above if present.
@@MAD2-9-12
NOTE: question bodies (Q11-Q12) were on missing renders; stem/options from text layer above if present.
@@MAD2-9-13
C: const user = { name:'Alice', age:25, city:'Boston', country:'USA' };
C: const { name, city, ...otherInfo } = user;
C: const newUser = { name, location:city, ...otherInfo };
C: console.log(name); console.log(otherInfo); console.log(newUser);
O: Alice { city:'Boston', age:25, country:'USA' } { name:'Alice', location:'Boston', city:'Boston', age:25, country:'USA' } || Alice { age:25, country:'USA' } { name:'Alice', location:'Boston', city:'Boston', age:25, country:'USA' } || Alice { age:25, country:'USA' } { name:'Alice', location:'Boston', age:25, country:'USA' } || undefined { name:'Alice', city:'Boston', age:25, country:'USA' } { name:'Alice', location:'Boston' }
S: Alice { age: 25, country: 'USA' } { name: 'Alice', location: 'Boston', age: 25, country: 'USA' }
@@MAD2-9-14
C: new Promise((resolve, reject) => { const score = 0.45;
C: if (score >= 0.5) { resolve(score); } else { reject(new Error("Score too low")); } })
C: .then(data => { console.log("Stage A:", data); return data * 10; })
C: .catch(error => { console.log("Stage B:", error.message); return 3; })
C: .then(data => { console.log("Stage C:", data); if (data < 5) { throw new Error("Value below threshold"); } return data + 2; })
C: .then(data => { console.log("Stage D:", data); return data / 2; })
C: .catch(error => { console.log("Stage E:", error.message); if (error.message === "Value below threshold") { return "Recovered"; } throw error; })
C: .then(data => { console.log("Stage F:", data); if (data === "Recovered") { return 10; } return data * 4; })
C: .finally(() => { console.log("Stage G: Cleanup completed"); });
O: Stage A: 0.45 Stage C: 4.5 Stage D: 6.5 Stage F: 26 Stage G: Cleanup completed || Stage B: Score too low Stage C: 3 Stage E: Value below threshold Stage F: Recovered Stage G: Cleanup completed || Stage A: 0.45 Stage E: Value below threshold Stage F: Recovered Stage G: Cleanup completed || Stage B: Score too low Stage C: 3 Stage D: 5 Stage F: 20 Stage G: Cleanup completed
S: Stage B: Score too low Stage C: 3 Stage E: Value below threshold Stage F: Recovered Stage G: Cleanup completed
@@MAD2-9-15
C: index.html: <div id="app1">{{ message }}</div><div id="app2">{{ message }}</div>
C: app.js: new Vue({ el:'#app1', data:{ message:'Hello from App 1' } }); new Vue({ el:'#app2', data:{ message:'Hello from App 2' } });
O: App 1 only shows data || Both show "Hello from App 2" || Both show "Hello from App 1" || Each renders its own message independently
S: Each renders its own message independently
@@MAD2-9-16
NOTE: Q16-Q20 bodies were on missing renders (p009/p010); stems/options from text layer above if present.
@@MAD2-9-21
C: Task.vue: tasks [Learn Vue(incomplete), Build Project(incomplete), Test App(complete)]; filteredTasks hides complete unless showCompleted; completedCount counts complete; markComplete(id) flips to complete; toggleShowCompleted flips flag.
@@MAD2-9-22
O: Learn Vue || Learn Vue, Build Project, Test App || Test App only || None
S: Learn Vue
@@MAD2-9-23
O: 1 || 2 || 3 || 0
S: 2
@@MAD2-9-24
O: The filteredTasks logic won't work properly if we used arrow functions for the filter method || Using non-arrow functions in computed properties allows correct this access to Vue instance || filteredTasks and completedCount will both update reactively when a task's status is changed || The @click="markComplete(task.id)" usage correctly preserves reactivity
S: filteredTasks and completedCount will both update reactively || The @click usage correctly preserves reactivity
@@MAD2-9-25
NOTE: body was on missing render (p014); only tail options (25 / 200) visible.
@@MAD2-9-26
C: const TodoApp = { template:`<div><input v-model="newTodo" @keyup.enter="addTodo" /><ul><li v-for="todo in todos" :key="todo.id">{{ todo.text }}</li></ul></div>`,
C: data(){ return { newTodo:'', todos:[] } },
C: methods:{ addTodo(){ if (this.newTodo) { this.todos.push({ id:Date.now(), text:this.newTodo }); this.newTodo = ''; } } } }
O: An error occurs because the todos array is empty || The input is cleared, and Learn Vue appears in the list || Only the input is cleared, no todo is added || The page refreshes
S: The input is cleared, and Learn Vue appears in the list
@@MAD2-9-27
NOTE: Q27 body was on a missing render; stem/options from text layer above if present.
@@MAD2-9-28
O: CORS error occurs || 404 error || The server crashes
S: CORS error occurs
NOTE: question body was on a missing render; tail options only.
@@MAD2-9-29
C: function createCounter(){ let count = 0; return function(){ count++; return count; }; }
C: const counter1 = createCounter(); const counter2 = createCounter();
C: console.log(counter1()); console.log(counter1()); console.log(counter2());
O: 1 2 3 || 1 2 1 || 1 1 1 || undefined undefined undefined
S: 1 2 1
@@MAD2-9-30
NOTE: Q30 body was on a missing render; tail options about slots only.
@@MAD2-9-31
C: (Vue Router config sub-questions parent; routes Home/UserProfile/ProductDetail)
@@MAD2-9-32
C: const routes = [{ path:'/', name:'Home', component:HomeView }, { path:'/user/:id', name:'UserProfile', component:UserProfile }, { path:'/product/:category/:id', name:'ProductDetail', component:ProductDetail }];
NOTE: navigation methods were on a missing render (p020); see tail options at Q33.
@@MAD2-9-33
O: The navigateOne() method will create URL /user/555?tab=settings || The $router.replace() method adds a new entry to the browser history || The $router.go(-1) method navigates to the previous page in browser history
S: The navigateOne() method will create URL /user/555?tab=settings || The $router.go(-1) method navigates to the previous page in browser history
NOTE: question body was on a missing render; options as shown.
@@MAD2-9-34
C: function simulateTasks(){
C: const prashant = new Promise(resolve => setTimeout(() => resolve("Prashant"), 3000));
C: const nikita = new Promise(resolve => setTimeout(() => resolve("Nikita"), 2000));
C: const mayur = new Promise(resolve => setTimeout(() => resolve("Mayur"), 4000));
C: const team = Promise.all([prashant, nikita]).then(() => "Team");
C: Promise.race([team, mayur]).then(winner => { console.log("Winner is:", winner); }); }
NOTE: scenario = Team (3s via Promise.all) vs Mayur (4s); sub-questions Q35-36 were beyond rendered pages.
