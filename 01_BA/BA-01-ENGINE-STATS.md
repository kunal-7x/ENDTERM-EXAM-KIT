# 📐 BA-01 — ENGINE: Stats (Chi-Square, Distributions, Probability/Bayes)

## ENGINE S1 — Chi-square Test of INDEPENDENCE (rows × cols table)
**TRIGGER:** "independent", "expected frequency", table with row labels + column labels (jeans store, brand×city, gender×rating).

**STEPS:**
1. Row totals, column totals, grand total G (add everything).
2. Expected for cell = row_total × col_total ÷ G. ← THE question, 90% of the time.
3. df = (rows − 1) × (cols − 1). ← the follow-up question, always.
4. Decision: computed χ² > tabulated → Reject H₀ (NOT independent). Computed < tabulated → Do NOT reject (independent).
5. "Do not reject" ≠ "accept". Never tick "Accept the null".

**VAULT (exact PYQs):**
- Jeans 3 styles × 4 stores, E(Style-B, Store-3) = 324×315÷835 = **122.23** (key: 121–123)
- Same table, df = (3−1)(4−1) = **6**
- Computed 2.7 < tabulated 5.78 → **Do not reject; sales ARE independent**
- Gender×difficulty rating: E(male, rating 3) = row×col÷200. df = **2** (key)
- Day×Street independence: df = **14** (key)

## ENGINE S2 — Chi-square GOODNESS-OF-FIT (one row of data vs a distribution)
**TRIGGER:** "goodness of fit", "follows uniform/normal", "bins".

**STEPS:**
1. Expected per bin = total_observations ÷ number_of_bins. (Uniform = equal everywhere.)
2. χ² = Σ (Observed − Expected)² ÷ Expected. Compute per bin, add.
3. df = bins − 1 (− extra if parameters estimated from data; uniform = bins−1).
4. Compare with table value → reject / do-not-reject (same as S1).

**VAULT:**
- Ice-cream street-A, 4 bins: E per bin = **3.5** (portal key — memorize for this exact scenario; engine gives n/k)
- Uniform ice-cream-parlour 14 days, 7 bins: computed χ² = **4**, df = **6**, E per bin ≈ **2.0**
- Lenses Normal check: bins given, σ = 1.00 from sample → standardize, use normal table.
- Null for GoF is ALWAYS "data FOLLOWS the distribution" (tick: "uniformly distributed", NOT the "NOT" version).

## ENGINE S3 — Distributions (1-mark theory, always repeats)
- **Mean ≈ Median ≈ Mode + zero skew** → symmetric (Gaussian). **Mean > Median** → right skew. **Mean < Mode** → left skew.
- Moments: 1st = mean, 2nd relates variance, 3rd relates skewness.
- **Poisson**: counts, skew > 0, mean ≈ variance. **Uniform**: all equal. **Exponential**: waiting time, right-skew.
- **Empirical distribution** needs: the actual sample data (nothing else).
- P-P plot vs Q-Q plot: right-tail data → points DON'T fall on the 45° line in EITHER plot (both options with "will not entirely fall" are correct; "will fall" options are wrong).
- p-value = P(observing this sample | H₀ is TRUE). p (0.054) > α (0.05) → **Fail to reject H₀**. Never "accept H₀".

## ENGINE S4 — Total Probability + Bayes (the bulb/factory template)
**TRIGGER:** "Type-A/B/C with %", "factory A/B", "accident prone", "given that it is defective, probability it came from X".

**STEPS:**
1. P(event) = Σ P(typeᵢ) × P(event|typeᵢ). ← first question, always.
2. P(typeₖ|event) = P(typeₖ)×P(event|typeₖ) ÷ answer-from-step-1. ← second question, always.
3. Cost/warranty: Σ P(typeᵢ)×P(bad|typeᵢ)×N×costᵢ.

**VAULT (DMS bulbs — memorize the triple):**
- P(life > 100h) = 0.2×0.7 + 0.3×0.4 + 0.5×0.3 = **0.41**
- P(Type-B | >100h) = 0.12 ÷ 0.41 = **0.29**
- Warranty cost 10,000 bulbs = 1200 + 3150 + 10500 = **14850**
- Insurance: P(accident) = 0.3×0.4 + 0.7×0.2 = **0.26**; P(prone|accident) = 0.12÷0.26 = **0.46**
- ⚠️ Radios (0.05/0.1 factories): engine gives P(2nd def|1st def) = 0.00625÷0.075 = **0.08**; portal key says **0.04–0.05**. Exact-repeat → write key. New numbers → engine.

## ENGINE S5 — Discrete vs Continuous (1-mark gifts)
- Discrete: counts (number of courses, batch size). Continuous: measurements (average weight, average age, height).
- VIF < 1 → **calculation error** (VIF ≥ 1 always). VIF = 1/(1−r²); VIF > 5–10 → multicollinearity problem.
