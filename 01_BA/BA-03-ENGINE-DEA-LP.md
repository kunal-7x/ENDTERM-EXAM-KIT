# 🏭 BA-03 — ENGINE: DEA, HCU Numeric, LP Primal/Dual, Conjoint

## ENGINE D1 — DEA theory (10+ marks of repeats, memorize these verdicts)
1. **DEA measures**: comparing efficiency of similar service units. (NOT quality benchmarking, NOT technology feasibility.)
2. **Efficiency** = weighted outputs ÷ weighted inputs. **Efficient ⟺ efficiency = 1.** Anything < 1 = inefficient.
3. **"X obtained efficiency 1 with the optimal weights of BU-k"** → X **WILL BE efficient**. (The #1 repeated MSQ — "will be", never "may be".)
4. **"X obtained efficiency 0.6/0.9 (< 1) with weights of BU-k"** → X **WILL BE inefficient**; BU-k itself **MAY BE inefficient** (never "will be" for the solved unit — LP only proves others).
5. **Reference units** = the units with NON-ZERO dual variables (lambdas). If λ₃, λ₅ ≠ 0 → reference units are (3,5)/(5,3) — option order varies, match the SET.
6. **LP for weights**: after converting ratio → linear objective + normalizing denominator (= 1) + constraining ALL DMUs' efficiency ≤ 1. MSQ answer = all three + NOT "non-linear".
7. **Economic frontier** = the efficient DMUs (from the graph: the outermost points). Reference units for an inefficient DMU = its frontier neighbors.
8. **Productive efficiency** = "maximizing output under given constraints (without worrying about optimal allocation)". This EXACT sentence is an option in 6+ papers — tick it. The "cannot increase one output without sacrificing another" sentence = the FRONTIER definition — also ticked when paired.
9. **Objective (output-oriented, DMU-k)**: Max Σ y·O_k (its OWN outputs). **Type/normalizing constraint**: Σ x·I_k = 1 (its OWN inputs, = 1 — never ≤ or ≥).
10. **"Not a constraint" questions** (Sales Office LP): every constraint uses the unit's OWN row on the LEFT vs each unit's data on the right — the odd one has a mismatched row (e.g., y₁₂…≤ x…×Budget₁ instead of Budget₃'s row).

## ENGINE D2 — HCU numeric (2 marks, EVERY recent paper, pure recipe) ⭐
**TRIGGER:** "HCU", "dual variables … are non-zero", "efficiency is 0.8", a small table of reference units.

**RECIPE (never fails — verified on 5 PYQ datasets):**
```
HCU_output = (λ₁ × ref₁_output + λ₂ × ref₂_output) ÷ efficiency
```
1. λ's = the dual variables given (non-zero ones only).
2. ref outputs = the table rows for THOSE units (match λ₃ → row of unit 3).
3. Divide by the efficiency. Round per note (usually 2dp, sometimes 4dp-every-step).

**VAULT (copy if numbers match exactly):**
- λ₅=0.3, λ₃=0.5, eff 0.8, Savings(25L, 32.5L), Projects(23, 14) → Savings = (0.3×25L+0.5×32.5L)/0.8 = **2968750** (key 2968749–51); Projects = 13.9/0.8 = **17.38** (key 17.1–17.8)
- λ₂=0.5, λ₅=0.3, eff 0.8, Out(9000/10, 6500/12) → Out1 = 6450/0.8 = **8062.5**; Out2 = 8.6/0.8 = **10.75**
- λ₄=0.35, λ₅=0.4, eff 0.75, Sales(11000, 9000), Loyal(150, 130) → Sales = 7450/0.75 = **9933.33**; Loyal = 104.5/0.75 = **139.33**
- λ₂=0.25, λ₄=0.35, eff 0.6, Out(9000/10, 6500/12) → Out1 = 4525/0.6 = **7541.67**; Out2 = 6.7/0.6 = **11.17**
- λ₂=0.25, λ₄=0.35, eff 0.6, Out(9000/10, 6500/12) HCU3 variant → **7541.67 / 11.17** (same numbers, different paper — PROOF they recycle)
- λ₃=0.5, λ₅=0.3, eff 0.8, Sales(12000, 10000) → **11250**; Loyal(100, 120) → (50+36)/0.8 = **107.5**
- Market-Share variant: (0.35×55 + 0.45×60)/0.8 = **57.8125** (MCQ — tick it)
- Input-side variant (minimize inputs): required input = Σ(λ × ref_input) [NO division when efficiency already applied — follow the worked pattern: (0.65×8 + 0.35×10) = **8.7**?? key says 19?! ⚠️ exact-repeat → key 19; else engine. Flagged.)

## ENGINE D3 — LP primal ↔ dual (counting questions, 1 mark each)
**TRIGGER:** "how many constraints/decision variables in the dual", "valid dual constraint", "non-zero dual variables".

1. #dual_vars = #primal_constraints (excluding non-negativity). #dual_constraints = #primal_vars.
2. Max-primal ↔ Min-dual. ≤ constraints ↔ ≥ dual constraints (for max-primal). RHS ↔ objective coefficients SWAP.
3. Complementary slackness: solved-primal binding constraint ⟺ dual variable can be non-zero. (MSS interviews / Milo ads: "how many dual vars non-zero" = count of BINDING primal constraints at the given solution.)
4. Feasibility check (Milo ads MCQ): test each constraint with the given numbers — ANY violation → "NOT feasible / fraud". (105000+31500+45200 = 181700 ≤ 182000 budget ✓ but media-mix % violated → NOT feasible.)
5. "Maximize (10Y1+…)" as a DUAL objective → WRONG (dual of max is min). Tick the Min version.

**VAULT:** 6-var 5-constraint max-primal → dual has **5** decision vars, **6** constraints. Dual coeff for Constraint-4 (RHS 20) → **20**. Chef Jeff LP → **4** primal vars. Milo solution → **0** non-zero dual vars, primal obj **−791400** (memorize).

## ENGINE D4 — Conjoint (all ratta, zero math)
1. #pairwise preferences for N products = N(N−1)/2. (4 products → **6**; 5 → **10**; 3 variants → **3**.) "4 products 2 attributes" → **6** (asked 4 times; options include 8/16/12 as traps).
2. Pairwise data + continuous attributes → **Statistical/Regression approach** (MSQ: tick Regression + Statistical + "Optimization or Statistical", never "Optimization" alone... note: one paper's key = "Optimization or Statistical approach" single MCQ).
3. Ratings + continuous → Statistical/Regression. Pairwise + categorical → LP/Optimization.
4. Part-worth = **"All of these"** (level utilities + utility for that level + utility for separate parts).
5. Pairwise objective: **minimize violation of wrong preferences + minimize poorness of fit** (both).
6. Ideal-point (O1/O2/x diagram): nearer to x wins → "prefer O1 when d2>d1" ✓ + "prefer O2 when d1<d2" ✓ (both; garbled-option papers: tick the pair).
7. Format needed: Ratings→Statistical; Pairwise→LP/Optimization.
