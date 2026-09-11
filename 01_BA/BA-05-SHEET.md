# 📋 BA-05 — FORMULA SHEET (read before sleep + before exam)

## DEA
- Efficiency = Σy·O ÷ Σx·I · Efficient ⟺ = 1 · Reference units = λ≠0 units
- **HCU = Σ(λᵢ·refᵢ) ÷ efficiency** · "eff 1 with k's weights" → WILL BE efficient

## LP / Dual
- #dual_vars = #primal_constraints · #dual_constraints = #primal_vars
- Max→Min · ≤→≥ · RHS↔obj-coeffs swap · Non-zero dual = binding primal

## Demand D = a − bP
- Market = a · Satiating = a/b · Rev-max P = a/2b · Profit-max P = (a/b+c)/2 · Elasticity = bP/D

## Regression
- R² = r² (1 x) · adjR² = 1−(1−R²)(n−1)/(n−k−1) · %var = R²×100
- F = (R²/k)/((1−R²)/(n−k−1)) · VIF = 1/(1−r²) · SE↑% = (1/√(1−r²)−1)×100
- Total effect = direct + Σ(indirect legs multiplied)

## Confusion (TP/FP/FN/TN from table)
- Acc = (TP+TN)/N · Prec = TP/(TP+FP) · Rec = TP/(TP+FN)
- Threshold: prob ≥ t → 1 · Cancer→Recall · Spam→Precision

## Chi-square
- Independence: E = row×col/G · df = (r−1)(c−1) · computed>tab → Reject
- GoF: E = n/k · χ² = Σ(O−E)²/E · df = k−1 · H₀: "follows distribution"

## Bayes
- P(E) = ΣP(Tᵢ)P(E|Tᵢ) · P(Tₖ|E) = P(Tₖ)P(E|Tₖ)/P(E)

## Conjoint
- Pairs = N(N−1)/2 (4→6, 5→10) · Pairwise+continuous → Statistical/Regression
- Part-worth = All of these · Objective = min violations + min poorness of fit

## Decisions
- p > α → fail to reject (never "accept") · p-value = P(sample|H₀)
- Mean>Median → right skew · VIF<1 / adjR²>R² → calculation error
- Marginal=partial ⟺ x's INDEPENDENT · Correlated x's = Collinearity
