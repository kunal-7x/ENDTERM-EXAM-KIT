@@BA-2-15
O: 1-A, 2-C, 3-B, 4-D || 1-B, 2-C, 3-A, 4-D || 1-C, 2-B, 3-C, 4-D || None of these
NOTE: matching-type question stem was on an unrendered page.
@@BA-2-25
O: Fail to accept the alternative hypothesis and conclude the variables are not independent || Fail to reject the alternative hypothesis and conclude the variables are independent || None of these
NOTE: first options were on an unrendered page; stem = chi-square independence conclusion.
@@BA-6-11
C: Demand for book "PJs": D = 23000 - 10*P1 (P1 = selling price).
@@BA-6-14
C: Factory output mix: A 60%, B 22%, C 7%, D rest. Defective rates: A 12%, B 17%, C 8%, D 10%.
@@BA-6-27
C: Discourse study: 6 terms (Jan-22..Sep-23), 100 IDs each (50M/50F). Categories: followed / not-followed / not-accessed. Male not-followed: 20,30,25,45,25,35. Male not-accessed: 2,10,5,4,5,3. Female followed: 15,22,32,25,20,20. Followers ~ Normal(18, 4). Bins: ≤35 | 36–50 | 51–100.
@@BA-8-15
C: Bulb life ≥100h: Type-A 0.7, Type-B 0.4, Type-C 0.3. Mix: A 20%, B 30%, C 50%. Warranty costs: A Rs.2, B Rs.1.75, C Rs.3 per replaced bulb; 10,000 bulbs/year.
@@BA-9-27
C: Demand–price: D(p) = 780 - 9*P.
@@BA-9-34
C: Insurance classes: accident-prone (accident prob 0.4/year) vs not-prone (0.2/year); 30% of population accident-prone.
@@BA-10-17
C: MTG footballs: R-game needs 6min S1 + 15min S2 + 6min S3; P-game needs 12min S1 + 9min S2 + 6min S3. Available (4 weeks): S1 340h, S2 480h, S3 300h. Extra S1 @ Rs.200/hr. Profit: R Rs.500, P Rs.800. Max sales 3000. Maximize profit as LP.
@@MAD2-1-2
O: JavaScript is a low level programming language || The "const" keyword can be used to declare objects with block level scope || Int, char are some primitive data types in JavaScript || JavaScript supports both first order and higher order functions
@@MAD2-4-18
O: Celery is a task queue || Celery typically runs the tasks asynchronously || Celery typically runs the tasks synchronously || None of these
@@MAD2-4-27
C: const store = new Vuex.Store({ state:{ count:0, total_cost:0, products:[] },
C: mutations:{ update_total_cost : Placeholder2 } })
C: Vue.component("product", { template:`<div>Assume some code</div>`,
C: methods:{ update_store_cost : function(count, price){ Placeholder1 } } })
O: Placeholder1: this.$store.commit("update_total_cost", count * price); / Placeholder2: function (state, total_cost) { state.total_cost = total_cost; } || Placeholder1: this.$store.commit("update_total_cost", count, price); / Placeholder2: function (state, count, price) { state.total_cost = count * price; } || Placeholder1: this.$store.commit("update_total_cost", {"count":count, "price":price}); / Placeholder2: function (state, payload) { state.total_cost = payload.count * payload.price; } || Placeholder1: this.$store.commit("update_total_cost", count, price); / Placeholder2: function (count, price) { total_cost = count * price; }
@@MAD2-8-30
C: app = Flask(__name__); app.config["JWT_SECRET_KEY"] = "supersecretkey"; jwt = JWTManager(app)
C: @app.route("/login", methods=["POST"]): user={"username":"student","role":"student"}; access_token = create_access_token(identity=user); return jsonify(access_token=access_token)
C: @app.route("/protected", methods=["GET"]): @jwt_required(); current_user = get_jwt_identity()
C: if current_user.get("role") != "admin": return jsonify({"message":"Forbidden: Insufficient permissions"}), 403
C: return jsonify(message=f"Hello, {current_user['username']}!")
@@MAD2-8-31
O: Request succeeds, "Hello, student!" returned || 401 Unauthorized || Empty 200 response || 403 Forbidden
NOTE: fetch WITHOUT token.
@@MAD2-8-32
O: Request succeeds, "Hello, student!" returned || 401 Unauthorized || Empty 200 response || 403 Forbidden
NOTE: fetch WITH student Bearer token (role=student, route needs admin).
@@MAD2-8-33
C: (roleHierarchy admin:3, manager:2, user:1; hasAccess compares levels; mounted: !hasAccess('manager') → replace('/unauthorized') else replace('/profile'))
NOTE: start of component code was on a missing render page; tail as shown.
