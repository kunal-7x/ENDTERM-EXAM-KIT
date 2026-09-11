# 🟣 MLP-00 — Machine Learning Practice: 80/20 Index

**Paper: 100 marks (recent) / 50 (older). ~35-40 Qs. MCQ (1-4m) + MSQ + SA code-output (2-5m). No theory essays — everything is sklearn code or concept.**

## 🔥 TOPIC FREQUENCY (10 papers, ~350 Qs)

| # | Topic | Hits | Engine | Priority |
|---|---|---|---|---|
| 1 | Preprocessing (scalers, imputers, encoders, ColumnTransformer, pipelines) | ~45 | MLP-01 | 🔴 HIGH |
| 2 | Trees + ensembles (DT, RF, Bagging, Boosting, Voting) | ~40 | MLP-02 | 🔴 HIGH |
| 3 | Model selection (GridSearchCV/RandomizedCV counting, CV schemes) | ~30 | MLP-01 | 🔴 HIGH |
| 4 | Metrics (confusion, precision/recall/F1, R², scorers) | ~28 | MLP-01 | 🔴 HIGH |
| 5 | KNN / SVM / SGD / NB / LogisticRegression | ~45 | MLP-02 | 🔴 HIGH |
| 6 | Clustering (KMeans, hierarchical, elbow, silhouette) | ~22 | MLP-02 | 🟡 MED |
| 7 | Pandas output prediction (loc/iloc/groupby/apply) | ~22 | MLP-02 | 🟡 MED |
| 8 | Neural nets (MLPClassifier/Regressor params) | ~18 | MLP-02 | 🟡 MED |
| 9 | NLP/text (Count/TfidfVectorizer) | ~12 | MLP-02 | 🟢 LOW |
| 10 | Time series + recommenders (2025-26 NEW) | ~12 ⬆ | MLP-02 | 🔴 HIGH (rising) |

## 🗺️ FILE MAP
| File | What |
|---|---|
| MLP-01-ENGINE-CORE | Scalers/imputers/encoders/pipelines/metrics/CV/GridSearch counting |
| MLP-02-ENGINE-MODELS | Every model family: answer-rules + code-output recipes |
| MLP-03-RATTA | Concept MCQ/MSQ + answers |
| MLP-04-SA-SOLVED | All numeric/code-output SAs, computed + verified |
| MLP-05-SHEET | API + formula cheatsheet |

## ⚡ MLP EXAM-DAY CHEAT
1. **"What will be the output"** → don't run whole program mentally; find the PRINTED expression, evaluate inside-out.
2. **Scaler questions** → write the formula (z=(x−μ)/σ etc.), compute by hand. 2 marks free.
3. **GridSearchCV "how many"** → combos × cv (× trees for RF-inside).
4. **"Which is TRUE" code MCQ** → test each snippet against the API rule (arg names matter: `n_estimators`, `__` separator).
5. **New 2025 topics**: ADF/stationarity, ARIMA order, cosine similarity, collaborative filtering, confusion-from-lists — all in MLP-02.
