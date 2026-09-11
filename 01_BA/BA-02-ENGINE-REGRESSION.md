# 📈 BA-02 — ENGINE: Regression, Demand/Profit, Logistic & Confusion Metrics

## ENGINE R1 — Demand curve D = a − bP (repeats EVERY paper)
**TRIGGER:** "demand", "D(p) = …", "satiating price", "market size", "elasticity", "maximize revenue/profit".

**STEPS (memorize these 4 formulas):**
1. Market size = a (demand at P = 0).
2. Satiating price = a ÷ b (price where demand hits 0).
3. Revenue-max price = a ÷ 2b. (Revenue R = P×D; derivative zero.)
4. Profit-max price (unit cost c) = (a/b + c) ÷ 2. Max profit = (P* − c)(a − bP*).
5. Elasticity at price P = b × P ÷ D(P). (Positive number; drop the minus.)

**VAULT:**
- D = 100 − 10p → revenue-max p* = **5**
- D = 780 − 9P, cost 30 → P* = (86.67+30)/2 = **58.33** (key 58–59) ⚠️ key's max-profit **20424** ≠ engine 7225 — exact repeat → write key; new numbers → engine.
- Books D = 23000 − 10P → revenue-max **1150**; cost 420 → profit-max P = (2300+420)/2 = **1360**?? key says 440?! ⚠️ exact-repeat → key; else engine. (Keys for this family are shaky — engine is mathematically certain.)
- May-2026 ice cream: satiating **375**, market **1500**, elasticity at 175 = **0.875** (= 4×175÷800)
- Elasticity from regression output: |price coef| × P ÷ D(P). (BA06: 3.836 → **3.84**)

## ENGINE R2 — R², Adjusted R², correlation (free marks)
**TRIGGER:** "R-square", "adjusted", "correlation", "variability explained", "VIF".

1. Simple regression (ONE x): R² = r². (% variability = R² × 100.)
2. Adjusted R² = 1 − (1−R²)(n−1)/(n−k−1), n = observations, k = predictors. (Always < R². Adding junk variables → adjR² FALLS.)
3. % variability captured = R² × 100 (as number, no % sign).
4. F-statistic = [R²/k] ÷ [(1−R²)/(n−k−1)].
5. VIF(x) = 1 ÷ (1 − R²_x). VIF > 5–10 = multicollinearity.
6. SE inflation when adding correlated var = (1/√(1−r²) − 1) × 100%.

**VAULT:**
- r(BP,Age) = 0.695 → variability = 0.695² = **48.30%**
- VIF(Weight|Age), r = 0.507 → 1/(1−0.257) = **1.35**
- n = 25, k = 3, R² = 0.6 → adjR² = **0.54**
- n = 50, k = 7, R² = 0.85 → adjR² = **0.825–0.83**
- r = −0.51 (Conduct vs PrizeMoney) → R² = **26.01%**
- Ambience + PrizeMoney (r = 0.55) → SE increase = **19.74%** (key 18–20)
- Model explains 82.3% (n = 8, k = 2) → F = (0.823/2)/(0.177/5) = **11.6** (key 11–12)
- Marginal = partial slopes ⟺ explanatory vars are **INDEPENDENT** (if "dependent" in stem → FALSE).
- High correlation among x's = **Collinearity/Multicollinearity**.
- "Adjusted R² > R²" in options → **calculation error**, always wrong.

## ENGINE R3 — Direct / indirect / total effects (path model)
**TRIGGER:** "direct effect of X on Y", "effect of X on Z", "total effect".

Total = direct + Σ (each indirect path multiplied).
**VAULT:** price→sales: 0.4 + (0.2×0.2) + (0.4×0.1) = 0.4+0.04+0.04 = **0.48**.

## ENGINE R4 — Confusion table → accuracy/precision/recall (BIGGEST BA ENGINE)
**TRIGGER:** any table with Predicted vs Actual / y_pred vs y_actual / Purchased vs Not.

**STEPS:**
1. Label the 4 cells: TP (pred ✓, act ✓), FP (pred ✓, act ✗), FN (pred ✗, act ✓), TN (pred ✗, act ✗). **Positive = the named class** (Purchased / Loyal / Pass / class 1).
2. Accuracy = (TP+TN) ÷ total. (×100 if they ask %.)
3. Precision(class) = TP ÷ (all PREDICTED as that class) = TP ÷ (TP+FP).
4. Recall(class) = TP ÷ (all ACTUALLY that class) = TP ÷ (TP+FN).
5. Threshold reading (logistic table with probabilities): predicted = 1 if prob ≥ threshold, else 0. Then count.
6. Multi-class matrix: accuracy = diagonal ÷ total. Precision(class C) = cell(C,C) ÷ column-C total. TN for class B = everything NOT row-B and NOT col-B.

**VAULT (banking 12-row table — this exact table repeats across papers):**
- Rows: TP = rows 1,4,5,7,12 = **5**; FP = rows 6,9 = **2**; FN = rows 3,8 = **2**; TN = rows 2,10,11 = **3**. Total 12.
- Accuracy = 8/12 = **66.67%** (2024 paper variant key: 58.1–58.6 — that variant's table differs; use engine on YOUR table)
- Precision(class 1) = 5/7 = **71.43%**; Recall(class 1) = 5/7 = **71.43%**
- Logistic-threshold: students table, threshold 0.7, "fail" as target → Recall = **66.0–67.0** (key)
- 3×3 Cat/Dog/Pig: accuracy = 14/30 = **46.67%**; precision(Dog) = 5/9 = **55.56%**
- TN for class B in 3×3 (100/0/10; 10/80/10; 30/0/70): everything except row B & col B = 100+10+30+70 = **210**?? paper key options: 0/10/20/110 → **110**?? Hmm: TN(B) = total − rowB − colB + cell(B,B) = 310−100−80+80 = 210. Options max 110?! ⚠️ Exact-repeat → tick **110**?? No wait — recompute: total = 100+0+10+10+80+10+30+0+70 = 310. Not-row-B = 100+0+10+30+0+70 = 210. Not-col-B of those = 100+10+30+70 = 210. Hmm 210 not in options. UNLESS table reads differently (maybe rows are Predicted). If rows = Predicted: TN(B) = actual-not-B & pred-not-B = same 210. Still 210. Options 0/10/20/110 → closest?? This key/options pair is broken; **if repeated, tick 110** (only sane "large" option) — flagged.
- **Cancer → Recall** (missing a case kills). **Spam → Precision** (false alarm hurts). **R²/MAPE for classification → NEVER correct.**

## ENGINE R5 — Logistic coefficients (interpretation MSQs, repeat verbatim)
- β₁ = 0.3: "log-odds increase by 0.3 per unit X₁" ✓ AND "odds increase by 35% (e^0.3 = 1.35)" ✓ AND "higher X₁ → more likely positive" ✓. (All three ticked in May-2026 MSQ.)
- β₂ = −0.35: "log-odds decrease by 0.35" ✓, "odds decrease ≈29% (e^−0.35 ≈ 0.71)" ✓, "higher X₂ → less likely" ✓.
- Logistic Regression CAN create non-linear boundary (with transformed features) → TRUE.
- ROC: higher curve = better. AUC 0.67-type SA: count squares under the step curve.
