# 🖼️ MAD2-02 — VUE ENGINE (Vue, Vuex, Router)

## ENGINE V1 — Reactivity, binding, directives
| Trigger | Answer |
|---|---|
| `:class` with object `{classA:true}` | applies classA. `<div :class="classObj">` ✓; `<div :class="{classA:classA}">` ✓ |
| Array syntax `[isActive?'activeClass':'','errorClass']` | errorClass ALWAYS, activeClass iff isActive |
| `v-if` vs `v-show` (both false) | v-if REMOVES from DOM; v-show keeps with display:none → HTML differs. Both true → same. |
| `v-for="item in items" :id="item.id"` | the one WITH `:id` binding (not `{{item.id}}` literal) |
| `v-for` valid syntaxes (MSQ) | `item in array` ✓, `(item,index) in array` ✓, `item of array` ✓ (+ `(item,index) of array` — valid Vue, tick if present) |
| `v-model` + custom component | needs `value` prop + `$emit('input', …)` → "Searching for: Apple" |
| `v-bind:class="[cond?classA:'', classB]"` | classB always; classA iff cond |
| Lifecycle order | beforeCreate→created→beforeMount→mounted→beforeUpdate→updated→beforeUnmount→unmounted |
| beforeDestroy / destroyed | before = BEFORE removal; destroyed = AFTER |
| `created()` vs `mounted()` sets message | **mounted wins** (runs later) → "Hello from mounted" |
| Two root instances, nested els | inner instance's scope wins inside; outer vars render empty → "FrontendJavaScript" |
| `{{ }}` vs method `{{ greetings() }}` | method CALLS each render; computed is cached property |
| Deep watcher on object + nested change | **triggered**, logs whole object |
| `app.user.name="Dev"`, deep:true | watcher fires (option with full object) |
| `isVisible=false`, v-if/v-else | **hidden paragraph shows** |
| v-model select default 'typeOne' + filter even | renders **246** |
| localStorage + v-model + refresh (no new input) | mounted re-reads SAME stored value → "IIT, Madras" / "AppDev1, 70" (change needs blur/click) |

## ENGINE V2 — Slots, props, components
| Trigger | Answer |
|---|---|
| Named slots usage | `<template v-slot:title>Custom Title</template>` + default content after |
| Unnamed double `<slot></slot><slot></slot>` | default content rendered TWICE (all four texts) |
| `Home class="bold"` + template `class="active"` | classes MERGE → **blue, bold** |
| `this.$refs.custom.name = 'Virat Kohli'` in mounted | child shows **"Welcome Virat Kohli"** (reactive mutation) |
| `$emit('book')` + toggle ×3 (true→false) | **"Slot ID: 1, Slot Status: Not Booked"** (×0/×1 → Booked) |
| Scoped slot `v-slot:header="{ info }"` | destructure form is correct |
| `addItem` pushes `(newItem, newItem)` | item appears TWICE → "1.Apple 2.Banana 3.Orange 4.Orange" |
| `props: true` on `/dashboard/:user` | param injected as prop → **"This is dashboard of 7"** |
| `sort()` in computed + `getDate()` | descending dates → **"1917"**; filter status → **"2"** |
| `availableSlots` (status==param string, id>offset) | compare as STRINGS ('true' vs 'true'); apply offset filter |

## ENGINE V3 — Vuex
| Trigger | Answer |
|---|---|
| `computed: code` for store state | **`...mapState(['stateA',…])`** (spread into computed) |
| `addItemAsync` + setTimeout 1000, check after 2s | action committed → **["React"] / ["Vue.js"]** |
| `dispatch('incrementAsync')` (await sleep + commit) | **state updates AFTER async completes** |
| `commit` payload | SINGLE payload only: `commit('m', count*price)` ✓ or object ✓ (NOT two args) |
| `update_total_cost` placeholders | option with `commit(name, count*price)` + `function(state,total_cost){…}` AND object-payload variant (MSQ: tick both) |
| `mapState/mapMutations` WITHOUT spread (broken code) | still runs per key → count after 3 clicks = **3** |
| Vuex+CLI async fetchValue action | `<p>` shows **'API Value'** after click |
| `addToCart` action variants | **All of these** (all commit addItem correctly) |

## ENGINE V4 — Router
| Trigger | Answer |
|---|---|
| `push({name:'profile',params:{name:'narendra'}})` + `/profile/:name` | **"Welcome narendra"** |
| `mounted(){ this.$router.push('/endpoint2') }` in First; visit endpoint1 | redirects before paint → **"Hello Second Component !!"** |
| `/` with children booked/unbooked/*; visit `#/` | no child matches → **"Page not Found"** (Error); visit `#/booked` → **"Unbooked Slots"** (names SWAPPED — read the template, not the route name!) |
| `path:'*'` placement (MSQ false) | wildcard must be LAST; "put at top" = FALSE |
| `routes` children paths | paths CAN nest (children array) — TRUE |
| `goToProfile`/`router-link to="/foo"` | navigates + renders Foo ("Browser navigates to /foo and displays Foo") |
| `slot/:status` + query offset | filter by BOTH param equality AND id>offset |
| Role-guard mounted (`hasAccess('manager')`) | compare hierarchy numbers; `replace()` navigates without history |
