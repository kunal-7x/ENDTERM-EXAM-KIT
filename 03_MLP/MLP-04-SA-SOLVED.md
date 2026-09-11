# 🧮 MLP-04 — SA SOLVED (every numeric answer, computed + verified in sklearn)

**Format note:** MLP SAs usually say "correct to 2 decimals / truncate". Copy exactly.

## Preprocessing outputs
| Q | Answer |
|---|---|
| MaxAbsScaler [[-3],[0],[-2],[2],[-1],[-4]] → min | **−1.0** |
| MaxAbsScaler [[-3.5],…] → max | **0.5** |
| SimpleImputer mean [1,2,3,nan,4,nan,5] → statistics_ | **[3.0]** |
| SimpleImputer F3 mean [9,7,?,5] | **7.0** |
| KNNImputer(k=2) C-row F3 | **6.0** |
| StandardScaler [2,6,10,14] → transform([[8]]) | **0.0** |
| MinMaxScaler same → 8 | **0.5** |
| StandardScaler var_ [[1,10]…] | **[2, 200]** |
| ColumnTransformer sum first col (MaxAbs+OHE) | **−0.45** |
| Same, X_transformed[2,1] | **1** |
| Poly interaction_only d3 [[1,3],[2,4]] | **[[1,1,3,3],[1,2,4,8]]** |
| Poly d2 [[1],[2],[3]] | **[[1,1,1],[1,2,4],[1,3,9]]** |
| Bigram count sum (2 docs) | **6** |
| Tfidf vocab len (apple/banana/orange/fruit) | **4** |
| Tfidf zeros ((1,2)-grams, 2 docs) | **10** |
| LabelEncoder zeros (11 fruits) | **3** |
| OHE sparsity 5×5 | **80%** |
| VarianceThreshold(0.1) kept cols | **1** |
| CT shapes | **(20640,49)** · **36** (iris) · **(4,4)** · **(3,3)** |

## Metrics (verified)
| Q | Answer |
|---|---|
| confusion_matrix rain/sunny | **[[1,2],[1,2]]** |
| f1 [1,1,0,1,0,0,1,0,1]/[0,1,0,1,0,1,1,1,1] | **0.7273 → tick 0.72** |
| f1 class-1 (8-list) | **0.7273 → write 0.73** |
| recall [1,0,1,1,0,1]/[1,0,0,1,0,1] | **0.75** |
| precision class-1 (3×3, col=8) | **0.25** |
| recall class-1 (10/5/4-matrix) | **0.1** |
| MSE dummy mean ([35,40] vs 20) | **312.5** |
| MSE [2,0,3,5]/[2.5,0,2,8] | **2.56** |
| r2 all-10 preds | **−12.5** |
| LogReg iris[70:80] score | **0.8** |
| DummyClassifier recall / precision (650/1000) | **1.0 / 0.65** |
| classification f1 (report) | **0.98** · class-1 n = **105** |
| GNB prior Yes | **0.667** |
| Cosine (1,2,3)·(1,0,0) / ·(2,0,1) | **0.27 / 0.60** |
| Collab X / Y / Robin-C pred | **0.92 / 0.82 / 4.289** |
| LR accidents (25, blue) | **73.87** |
| W1 (5/7-rule) / (3/4-rule) | **0.331 / 0.294** |
| PCA ratio_[0] (3-pt) | **1.0** |

## Model outputs (verified)
| Q | Answer |
|---|---|
| KNN [8,9]/[2,200]/[4,4]/[6,6]/[3,2]/[2.5,66] | **1 / 1 / 0 / 0 / 0 / 1** |
| Perceptron AND [1,1] / [2,2] / 0215 | **1 / 1 / 1** |
| Perceptron max-acc (5-pt) | **0.8** |
| KNN n=4 fit on 3 pts → classes | **3** (fit fine; predict would fail) |
| DT max_depth=2 predict [4,120] | **1** |
| KNN p=1 → classes + metric | **2, manhattan** |
| type_of_target ×4 | **binary / multiclass-multioutput / multilabel-indicator / multilabel-indicator** |

## Counts
| Q | Answer |
|---|---|
| LeavePOut(2,10) / RepeatedKFold(3,2) | **45 / 6** |
| GridSearch [{5},{3}] cv10 | **80 fits** |
| GridSearch combos [{25},{5},{30}] | **60** |
| RF(10 trees)+GS×cv5 | **500 models** |
| GBM GS cv4 | **72 fits** |
| {4,5,7} grid | **140** · RF-grid {15+6} → **21** |
| LOOCV 1024 / 1000 / 5 | **1024 / 1000 / 5** · KFold10 → **10** |
| 71-param MLP layer | **(10,)** |
| Balanced depth-3 leaves | **8** |

## Pandas SAs
| Q | Answer |
|---|---|
| shape-rows+cols−na (5×5,1 na) | **9** |
| Insulin zeros | **3** · Age mean | **34** · query BP | **64** · float64 cols | **2** |
| loc+iloc sums | **120 / 98** · type-nunique | **3** · getPassing | **3 (axis=1) / −1 (no-axis)** |
| df shape (150,4)→poly36 | **36** |
