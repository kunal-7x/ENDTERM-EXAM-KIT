# 🤖 MLP-02 — ENGINE MODELS (every family: rules + vault)

## TREES
- Overfit-king = **lowest ccp_alpha / deepest / min_split=2,leaf=1** (dtc1, tree_1).
- ccp_alpha ↑ → shallower: **d1 ≥ d2 ≥ d3 ≥ d4** (0.0 > 0.03 > 0.06 > 0.1).
- Depth rule: smaller min_split+leaf → DEEPER: **depth(clf1) ≥ depth(clf2)** for (3,2) vs (6,4); **tree_.max_depth ≥** variant same.
- Split BLOCKED if: node < min_split, or any child < min_leaf. (N=15→9+6 ✓ split with (6,4)? 9≥4,6≥4,15≥6 ✓ ALLOWED. N=5→4+2? 5<6 BLOCKED. N=7→4+3? 4≥4,3<4 BLOCKED. N=12→3+9? 3<4 BLOCKED.)
- Balanced depth-3 → max **8** leaves. max_depth purpose → **limit depth**. criterion → **split quality**.
- DecisionTree statements → tick **"depth ≤ max_depth + tree_.max_depth gives actual"**.
- class_weight='balanced' → **auto inverse-frequency weights** (+C still regularizes).
- DT predict [4,120] (depth2) → **1**.

## ENSEMBLES
- Bagging-KNN(bootstrap=False) → **None of these** (no bootstrap, no OOB, distance-weights DO matter, 30 estimators).
- Bagging max_samples=0.5 → **50% per estimator**. max_samples param → **draws per estimator**.
- RF diversity → **high n_est + max_samples<sub** (bootstrap=False+max_samples = INVALID → wrong option).
- RF max_features=5 → **5 features per split**. max_features low → **less variance (option 1)**.
- RF/Boost false-set → tick **without-replacement + bagging-reduces-bias + boosting-parallel** (all three FALSE; boosting DOES cut bias, sequentially).
- AdaBoost overfit → **lower learning_rate**. depth1-vs-3 → **adb1 safer + adb2 low-bias-high-variance**.
- Voting soft [0.4,0.6],[0.25,0.75],[0.9,0.1] → mean [0.52,0.48] → **class 0**. Soft = **average proba**. Hard = majority vote.
- GBM tuning → **CV per combo + best_params_**; fits counted in MLP-01.

## KNN / SVM / SGD / NB / LOGREG
- KNN outputs (verified): [8,9]→**1**, [2,200]k7→**1**, [4,4]→**0**, [6,6]→**0**, [3,2]→**0**, [2.5,66]→**1**.
- KNN rules: low-k = complex + noisy ✓; high-k = smooth ✓; scale matters ✓; bottleneck = **prediction search**; kneighbors → **(distances, indices)**; k > n → **fit OK (classes_=3), predict ERRORS**.
- Perceptron AND → **1**; max-acc on 5-pt set → **0.8**; continue-training → **warm_start=True**.
- SVC(kernel=__) → **'linear'/'rbf'** (NOT lasso/scale). support_ → **indices**. gamma↑ → tight neighborhoods. C↑ → complex + overfit.
- SGD: hinge→SVM ✓, log_loss→logistic ✓, percept→perceptron ✓. shuffle=True ✓, max_iter=1000 ✓, loss='huber' ✓. Ridge-via-SGD → **SGDRegressor(penalty='l2') + sgd__alpha**. adaptive → **÷5 on plateau + stop <1e-6**. warm_start+max_iter=1 loop → **per-iteration train error**. partial_fit → **SGD/GaussianNB/MultinomialNB** (NOT trees/logistic).
- NB: independence ✓; GaussianNB↔continuous ✓ (gender Height/Weight/Age → **GaussianNB**); predict_proba = **posteriors**; prior Yes = **8/12 = 0.667**.
- LogReg: coef_ ✓; C>0 always regularizes ✓; balanced = **equal importance**; penalty = **reg type**; max_iter = **cap not exact**; liblinear↔L1-small ✓ + **CANNOT do multinomial**; elastic-net → **saga**; "for income prediction" → **FALSE** (classification!); L1-reg + small data → **liblinear**.
- LinearRegression s1(with intercept) vs s2 → **s1 > s2**. W1 (5/7-constraint) → **0.331**; (3/4) → **0.294**.
- Scaling-impacted (MSQ) → **LinearRegression + SVM** (+KNN/KMeans). NOT-impacted → **DecisionTree** (only).

## CLUSTERING
- KMeans(n=20,random,10) → **"20 centroids × 10 inits"**. 100 samples zero-inertia → **True, sometimes** (K=n). 8 clusters on 7 pts → **runs fine**.
- inertia_ = **within-cluster SSE**. Tune: **n_clusters + init + max_iter** (NOT lr). k-choice: **elbow + silhouette** (NOT k-fold).
- Elbow code → **append(inertia_), range(1,11), show()**. Elbow statements: bend ✓ + diminishing ✓ + may-blur ✓.
- Silhouette: per-sample ✓ + higher-better ✓ + any-clusterer ✓ (NOT needs-labels).
- Agglomerative = **bottom-up merges**; outliers → **nearest cluster**; geo-distances → **Single linkage**; init-best → **k-means++**.
- Segmentation (spent+items) → **K-means** (×3). Image colors unlabeled → **Unsupervised**. labels_ = **cluster per point**.
- make_blobs(8,2) → **two unequal clusters**. KMeans-eval MCQ/MSQ → **Silhouette + Inertia** (NOT MAE/F1/R²).
- Hierarchical metrics MSQ → **Euclidean + Manhattan + Jaccard + Cosine (all)**.

## NEURAL NETS
- hidden_layer_sizes=(a,b) = **2 layers, a then b neurons**. (3,5) → 3-first/5-second. (50,30) → **50+30**.
- 71 params, 5 feats: **(10,)** single layer. out_activation_ (regression) = **identity**.
- alpha ↑ → **stronger regularization** (helps OVERfit; worsens UNDERfit — trap!).
- MLP purchase-Q → **trial-and-error**. MNIST-MLP essential → **scaling**. Non-linearity → **activation**.
- mlp1-vs-mlp2 → **mlp2 more params + seed matters**. Correct-construction MCQ → **full (128,64)+relu+adam+fit option**.
- ⚠️ `MLPRegressor(hidden_layer_size=(5,3))` (SINGULAR typo, 2 papers) → code ERRORS → tick **"None of the given options"**.

## PANDAS (output prediction — trace row by row)
- `df['Age'].mean()` for average ✓. HR-count → **len(mask) + value_counts** (NOT shape[1], NOT bare mask).
- Salary filter → **df[] + .loc[] + query()** (NOT bare boolean).
- `sort_values(asc=False).iloc[0]` → **highest row**.
- Class-XI & Physics>85 → **df[] + query()** (NOT `and`, NOT unparenthesized &).
- Drop both-missing → **dropna(subset,how='all') + isnull().all mask**.
- Row-mean col → **mean(skipna) + assign()** (NOT sum/2).
- `df.loc[23:25,[...]]` (idx 21-24) → **== iloc[[2,3],[1,2]] == iloc[2:4,1:3]** (tick both).
- Value+value: **120** (Dec25) / **98** (Apr24). `.apply(type).nunique()` on mixed col → **3**.
- ⚠️ `df.apply(getPassing)` (NO axis) → **applies per-COLUMN → KeyError → enter −1**. (axis=1 would give 3.)
- `df.dropna()` → **rows decrease**. df.shape→rows+cols−na: **9**. value_counts()[0] on Insulin → **3**. Age-mean skipna → **34**. query-chain → **64**. float64 cols → **2**.
- groupby-avg-per-category → **groupby(...).mean()**.

## NLP / TEXT
- CountVectorizer(bias/variance corpus) → **(2,15)**. `.vocabulary_` → **dict** (NOT sorted list).
- Bigrams (lowercase=False, 2 docs) → **sum = 6**. Tfidf len → **4**. Tfidf-zeros (1,2)-grams → **10**.
- Tfidf MSQ → **max_features + min_df** (NOT smooth-zero, NOT lowercase-copy).

## TIME SERIES + RECOMMENDERS (new 2025-26 — memorize)
- adfuller/low-p → **stationary** (H₀ = NON-stationary). p=0.03 @5% → **stationary**.
- ARIMA d=1 → **differencing count**. Fit-then-summary order: **fit() → summary()**.
- Multiplicative decomposition → **trend × seasonal × error**.
- Cosine (1,2,3)·(1,0,0) → **0.27**; ·(2,0,1) → **0.60**. Correct numpy form → **(a@b)/(norm·norm)**.
- No-ratings+metadata → **content-based**. SVD on user-item → **reduce dimensionality**. User-based CF needs → **user-item matrix**.
- Collab X (Alfred-Gordon) → **0.92**; Y (Bruce-Robin) → **0.82**; predict Robin-C → **4.289** (truncate).
- PIL (200,200)→gray→flat → **(40000,)**. PIL false-set → tick **256-max + resize-channels + flip**.
- Ridge(alpha=1.0) → **L2 penalty** (NOT L1, NOT no-reg).
