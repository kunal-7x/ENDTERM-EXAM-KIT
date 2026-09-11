# 🔧 MLP-01 — ENGINE CORE (preprocessing, pipelines, metrics, CV, tuning counts)

## ENGINE P1 — Scalers (write the formula, plug numbers)
- **StandardScaler**: z = (x−μ)/σ (population σ, ddof=0). `var_` = population variance. mean_ of [[1,10]…[5,50]] = **[2, 200]**... wait: col1 mean=3 var=2 ✓, col2 mean=30 var=200 ✓ → var_ = [2,200].
- **MinMaxScaler**: (x−min)/(max−min), default range [0,1]. [[2],[6],[10],[14]] → 8 maps to **0.5**.
- **MaxAbsScaler**: x/max|x|. [[-3],[0],[-2],[2],[-1],[-4]] → maxabs 4 → min = **−1.0**. [[-3.5],…] → max = 0.5/… = **0.5**.
- **StandardScaler().fit(X) then transform([[8]])** on [2,6,10,14]: μ=8 → **0.0**.
- Scaler for KNN/SVM: **"distances need equal feature contribution"**.
- ColumnTransformer numeric+OHE first rows: MinMax(2.0 in [1..5]) = **0.25** + OHE(apple)=[1,0,0] → **[0.25,1,0,0]**. Avocado variant (+StandardScaler col, 4 cats): **[0.4,1,0,0,0,0]**.
- ColumnTransformer shapes: Height/Weight+City(3 cats,drop-first) → **(4,4)**. Age/Income+Gender(drop-first) → **(3,3)**.
- FeatureUnion poly(deg2,8 feats,no bias)=44 + PCA(5) → **(20640,49)**. Iris poly(deg3,no bias)=34 + PCA(2) → **36 features**.
- PCA `explained_variance_ratio_[0]` on the 3-point set → **1.0**.

## ENGINE P2 — Imputers / encoders
- **SimpleImputer(mean)**: mean IGNORING nan. [1,2,3,nan,4,nan,5] → **[3.0]**. F3 [9,7,?,5] → **7.0**.
- **KNNImputer(k=2)** on C-row: 2 nearest by other cols (B,D) → (7+5)/2 = **6.0**.
- **OneHotEncoder(drop='first')**: k cats → k−1 cols. ColumnTransformer [2,1] cell → **1** (Green kept). Sparsity 5×5 identity → **80%**.
- **MultiLabelBinarizer(classes=[cold,hot,large,small])** coffee → **[[1 0 1 0],[1 0 0 1],[0 1 0 1],[0 1 1 0]]**.
- **LabelEncoder**: sorted mapping (bird0 cat1 dog2 fish3). `transform(['elephant'])` → **ERROR**. `inverse_transform([2])` → **'dog'**. Zeros in apple/banana/cherry vector → **3**.
- Groupby-impute: `df.groupby('Dept')['Age'].transform(lambda x: x.fillna(x.mean()))` ✓ (transform keeps index; apply BREAKS it).
- `dropna(thresh=45)` of 50 cols → drops rows with >5 missing ✓. `dropna(subset,how='all')` → only both-missing rows ✓.
- Big CSV loop → **`chunksize`** + `partial_fit`.

## ENGINE P3 — Pipelines (order + naming)
- Order: **impute → scale → model**. Reversed (scale→impute) = WRONG. `make_pipeline(SimpleImputer(most_frequent), MinMaxScaler())` ✓.
- GridSearch param for pipeline step: **`stepname__param`** (double underscore): `bc__n_estimators` ✓, `poly__degree` ✓, `estimator__max_depth` (AdaBoost param NAME is `estimator`) ✓.
- `memory=` = caching: saves time ✓ + speeds CV ✓ + speeds tuning ✓ (NOT parallel, NOT better generalization).
- `Pipeline` = SERIES only (ColumnTransformer/FeatureUnion = parallel).
- Missing-part poly-degree4 question → **`model.fit(X_train, y_train)`** (NOT fit_transform, NOT pre-transformed fit).
- `model.fit_transform(X, y)` on a Pipeline → **WRONG** (use .fit); `include_bias` stays False fine; `y` unused by transformers.

## ENGINE P4 — Metrics (confusion first, always)
- Binary vectors → count TP/FP/FN/TN by hand. y_true(7 ones)/y_pred(5 ones) example → TP=3,FP=2,FN=4,TN=6.
- Precision = TP/(TP+FP). Recall = TP/(TP+FN). F1 = 2PR/(P+R).
- **VAULT**: f1([1,1,0,1,0,0,1,0,1],[0,1,0,1,0,1,1,1,1]) = **0.7273 → option 0.72**. f1 class-1 (8-list) = **0.7273 → 0.73**. recall [1,0,1,1,0,1] vs [1,0,0,1,0,1] = **0.75**. 3×3 precision-c1 = **0.25**, recall-c1 = **0.1**.
- Confusion-matrix MCQ from two lists → **recount in exam; options have been misprinted before — trust your count**.
- R² HIGHER = better (NOT RMSE/MAE/MSE). R² range = **−∞ to 1**. R² < 0 ⟺ worse than mean-model.
- r2_score all-10s vs [3..7] → **−12.5**.
- DummyRegressor(mean): MSE([35,40],[20,20]) = **312.5**. DummyClassifier(most_frequent, 650/1000): recall = **1.0**, precision = **0.65**.
- `classification_report` → HAS precision/recall/F1 (NOT MSE/cross-entropy). Class-1 support **105**. f1(y_test,y_pred) = **0.98**.
- Imbalanced + 96% accuracy assertion → **both true, reason NOT the explanation**.
- Rare disease → precision + recall + F1 (NOT accuracy).
- MSE([2,0,3,5],[2.5,0,2,8]) = **2.56**.

## ENGINE P5 — CV + tuning COUNTS (mechanical)
- **Fits = param_combos × cv.** Grid sums DICTS, multiplies INSIDE dicts.
- VAULT: [{5 depths},{3 splits}] cv10 → (5+3)×10 = **80**. [{25},{5},{30}] cv3 → 60 **combos**. RF(n_est=10)+10 depths cv5 → 10×5×10 = **500 trees**. GBM 3×2×3 cv4 → **72 fits**. {4×5×7} → **140 combos**. RF-grid 15+6 → **21 combos**.
- **RandomizedSearchCV n_iter=4 → exactly 4 combos** (NOT all; random_state matters).
- LOOCV on n samples → **n models** (1024 → 1024; 1000 → 1000; 5 → 5). KFold-10 → **10**.
- LeavePOut(p=2, n=10) → C(10,2) = **45**. RepeatedKFold(3,2) → **6**.
- KFold([47,31,18,95,85,77],3) trains = 4-element sets; options with **41** or wrong sizes = impossible.
- OOB needs bootstrap=True (max_samples WITHOUT bootstrap → invalid combo).
- Scorers for regressor-GBM: **r2 / neg_mean_absolute_error** (NOT entropy/weighted_f1). GBM loss: **squared_error/huber** (NOT gini/log_loss).
