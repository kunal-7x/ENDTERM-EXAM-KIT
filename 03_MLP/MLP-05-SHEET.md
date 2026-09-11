# 📋 MLP-05 — CHEATSHEET (last-pass page)

## Preprocessing
- Standard z=(x−μ)/σ(pop) · MinMax (x−min)/(max−min) · MaxAbs x/max|x|
- Impute BEFORE scale · transform keeps index, apply breaks it
- OHE drop-first = k−1 · MultiLabelBinarizer alphabetical · LabelEncoder sorted
- Pipeline = series · `step__param` · memory = cache(time/CV/tune)

## Metrics
- Prec=TP/(TP+FP) · Rec=TP/(TP+FN) · F1=2PR/(P+R) · R²∈(−∞,1]
- Dummy-mean → MSE · Dummy-frequent → rec 1.0 · Report has P/R/F1

## Counts
- Fits = combos × cv (×trees if RF inside) · LOO = n · LPO = C(n,p)
- Randomized n_iter = EXACTLY that many

## Models
- Trees: low-ccp/deep = overfit · split needs min_split + min_leaf both
- RF decorrelate via max_features · AdaBoost: ↓lr fixes overfit
- KNN: small-k complex · scale matters · bottleneck = predict
- SVM: C↑ complex · gamma↑ tight · support_ = indices
- SGD: shuffle/max_iter/loss names · warm_start resumes · partial_fit ∈ {SGD,GNB,MNB}
- NB: indep + Gauss-cont + Multi-text · LogReg: coef_, C>0 regs, saga=elastic, liblinear≠multi
- KMeans: inertia=SSE · k-means++ · elbow=inertia · silhouette label-free
- MLP: (a,b)=layers · alpha=reg · seed matters · typo-param → None
- Pandas: loc≡iloc-slice · no-axis apply → −1 · query/transform keep shape
- Text: vocab dict · bigrams count · min_df/max_features only
- TS: low-p ADF = stationary · d = differencing · multiplicative = ×
- Reco: content = metadata · SVD = dim-reduce · cosine = (a@b)/(|a||b|)
