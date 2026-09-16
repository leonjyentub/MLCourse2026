# 程式來源與修改對照

所有來源固定在 2026-09-09 擷取的 commit。`upstream/` 原始檔保持下載位元組不變，`upstream/manifest.json` 記錄 URL／commit／SHA-256；教學修改在 `notebooks/`，不覆寫原檔。

| 來源 | 固定 commit | 擷取範圍 |
|---|---|---|
| [Aurélien Géron — handson-mlp](https://github.com/ageron/handson-mlp) | `47eba45aacc85feae51ba7db68dd1ca66cb25e0a` | Ch.1–9 Notebook 與 Appendix C（SVM）、README、LICENSE、pyproject |
| [Leonjye — MachineLearning2025](https://github.com/leonjyentub/MachineLearning2025) | `3da2cb56b9efd17d7cd34602589f392554b40603` | 迴歸、GD、sigmoid、Iris、ROC、正則化、早停、切分、決策樹／AdaBoost／隨機森林、SVM 核、PCA／SVD／LLE、DBSCAN／GMM、ANN 手寫與激活函數等範例與專案說明 |

原始程式依來源授權／使用者授權保留歸屬，詳見 [NOTICE.md](NOTICE.md)。未將教師來源與混合產物一律重新授權。Notebook 標註的來源 cell 索引從 0 起算；章節名稱可配合原檔搜尋。

## 逐本改編

| 教學 Notebook | 核心來源 | 本次修改／補充 |
|---|---|---|
| 00 | 自編 | uv 核心、版本與資料 hash 檢查，seed 示例 |
| 01 | Géron Ch.1 cell 10；Ch.4 GD；教師 batchgradientDescent | 原 GDP／生活滿意度 LinearRegression + k-NN；標準化座標的手算梯度，與 least squares 驗證 |
| 02 | 教師 overfitting／Regularization／Early_stopping；Géron Ch.4 | 保留二次資料思路，建立 train/val/test、相同 CV folds、L1/L2/ElasticNet、恢復最佳 checkpoint；新增 80 次偏差變異數實驗 |
| 03 | Géron Ch.2 下載、切分、EDA、比率特徵 | 本機 CSV、明確 test 界線、完整 training EDA；補永久 ID 哈希示例 |
| 04 | Géron Ch.2 cells 139–154、159–212；教師 KFold | 自訂 RatioTransformer、fold 內完整 Pipeline、縮小搜尋、最終 RMSE/MAE/CI、可跨程序載入 |
| 05 | 教師 Iris1 cells 3–8、Iris2 cells 3–7；Géron Ch.3/4 分類 | stable sigmoid/log loss、平均梯度、先切分再縮放、正確類別映射與平手政策 |
| 06 | 教師 `01_ROC_AUC.py`；Géron Ch.3 metrics | 原 20 筆資料保留，修正 ROC 方向／端點／ties；與 sklearn 及成對排序驗證；加入投影片八筆資料與滑桿 |
| 07 | Géron Ch.3 cells 11–115 | 真 MNIST 快取、fast 分層子樣本、OOF 模型選擇、獨立 val 選閾值、最後完整 test；縮小多標籤／多輸出去噪 |
| 08 | 自編；延續兩來源的 estimator／Pipeline API | 歸納偏好、隨機標籤洩漏、群組／時間切分、train-dev、prequential 漂移、Huber／MAPE |
| 09 | Géron Ch.4（Normal Equation／GD／SGD／Polynomial／Learning Curves）；教師 batchgradientDescent、gradientDescent_weight_bias、regression | 正規方程／`lstsq`／SVD 三解法互驗、共線最小範數解、標準化批次 GD 三種學習率、SGD 排程與參數空間路徑、`learning_curve` 欠／過擬合，並驗算投影片兩個手算 |
| 10 | Géron Ch.4（Ridge／Lasso／ElasticNet／Early Stopping／Logistic／Softmax）；教師 Regularization_Regression、Logistic_Regression_scratch_Iris1 | 12 次多項式係數路徑、明示 sklearn ElasticNet 與教材 alpha 尺度差異、`expit`／`logaddexp` 手寫 logistic、穩定 softmax（減最大值），驗算懲罰／閾值／softmax 三個手算 |
| 11 | Géron Ch.5、Appendix C；教師 Decision_Tree_from_scratch、svm_kernel、Decision_Tree_sklearn_moon | `export_text` 可讀規則、Gini／Entropy 小函數、CART 加權不純度增益、moons 正則化邊界、PCA 旋轉降低樹深度、RBF SVM `gamma`／`C`，驗算純度／分割／迴歸葉三個手算 |
| 12 | Géron Ch.6；教師 Adaboost_from_scratch、Random_Forest | 硬／軟投票、`BaggingClassifier` OOB、森林像素重要度、手算 AdaBoost 第一輪、逐棵 gradient boosting 殘差與累加、`StackingClassifier` 與 in-sample 特徵洩漏對照 |
| 13 | Géron Ch.7；教師 PCA_from_scratch、SVD_from_scratch、LLE_swiss_roll | 維度災難統計、共變異矩陣特徵分解手算、累積解釋變異選 d、`inverse_transform` 重建、Swiss roll PCA vs LLE 鄰居保留、`SparseRandomProjection` 與 `johnson_lindenstrauss_min_dim` |
| 14 | Géron Ch.8（K-means 段）；教師 Kmeans+SemiSupervisedLearning、Cluster_1 | 手寫指派／更新兩步、K-means++ 與 `n_init`、肘部與輪廓分數、橢圓／小群限制、`flower.jpg` 顏色量化、digits 少量標註挑代表樣本並傳播，驗算一維 K-means 與輪廓係數手算 |
| 15 | Géron Ch.8（DBSCAN／GMM 段）；教師 GMM_from_scratch、DBSCAN、Clustering_DBSCAN | DBSCAN `eps` 破碎↔連續、核心點最近鄰延伸並拒絕過遠點、手寫 E／M 一步、`covariance_type` 比較、`score_samples` 百分位異常、AIC／BIC 數例與曲線、PCA 重建誤差異常，驗算鄰域與軟指派手算 |
| 16 | Géron Ch.9；教師 ANN_from_Scratch_MNIST、Activation_functions、neural_nets_with_keras | Perceptron 學習規則、XOR 網路四組輸入、激活函數與導數、單一 sigmoid 神經元前向／反向手算、`TinyMLP`（numpy forward／backward）於 digits、`MLPClassifier`／`MLPRegressor` 與標準化 logistic 比較 |

## 修正原程式與評估差異

- **ROC 積分方向：**教師原程式用遞增閾值，FPR 由大到小，直接 `np.trapezoid(tpr,fpr)` 可能產生負 AUC，且缺 all-negative 端點。本版採 `inf → unique scores descending`，同分一起移動。保留原陣列後，AUC 分別為 **0.95、0.57**。
- **縮放洩漏：**Iris2 原版在 split 前對全體 fit StandardScaler。本版先切分，scaler 只 fit training；CV 中則包進 Pipeline。
- **早停資料與模型：**原範例以名為 test 的集合逐輪選 epoch，並存在最佳模型／最後模型分開使用的問題。本版明確設 validation、deep-copy 最佳 checkpoint，斷言恢復後驗證誤差等於最低值，最後才評估 test。
- **數值穩定：**手寫 logistic 改以 expit 與 logaddexp，並使用平均 loss／梯度；學習率不與原加總梯度版本直接對比。原多項式 50 次縮到 12 次，降低條件數帶來的教學干擾。
- **不反覆選 test：**正則化候選以同一 CV 選擇；房價搜尋在 training；MNIST 以 OOF AP 選模型、獨立 validation 選閾值。不同 notebook 的預先指定示範任務不被宣稱為相互獨立的正式研究。
- **RMSE CI 的意義：**沿用 Géron bootstrap 思路，明示這是固定模型測試誤差的抽樣區間，不是個別房價預測區間、不是假設檢定，且未涵蓋地理相依／選模／重新訓練變異。
- **多輸出像素：**MNIST 快取是 uint8；加噪音前轉 int16，避免溢位。保留 KNeighborsClassifier 的 784 個像素類別輸出，不以回歸去噪冒充相同任務。
- **效能比較界線：**fast 資料量、特徵工程、模型規模、seed 與 scikit-learn 版本不同，本次數字不替換書中或舊投影片數字。完整模式也只擴大資料量，不會復刻原書所有搜尋。
- **09–16 的內建資料：**`load_iris`／`load_digits`／`load_sample_image('flower.jpg')` 隨 scikit-learn 安裝、不需下載；`make_moons`／`make_blobs`／`make_swiss_roll` 為合成資料且 seed 固定。這些不進 `data/manifest.json`。
- **教師手寫演算法改編：**決策樹、AdaBoost、PCA、GMM、`NeuralNetMLP` 等原檔多為腳本層級示範（含中文字型與 `plt.show()`）。本課只取核心數學步驟改寫成可斷言的教學段落，並與 scikit-learn 對應實作交叉驗證，不整段搬運。
- **不安裝深度學習框架：**deck 11／Notebook 16 對應教材 Ch.9，但本課以 numpy 與 `sklearn.neural_network` 取代 Keras／PyTorch；`upstream/` 仍保留 `06_neural_nets_with_keras.ipynb` 原檔供對照。

## 原始檔案清單

完整 44 個擷取原檔的 URL、commit 與 SHA-256 見機器可讀的 [`upstream/manifest.json`](upstream/manifest.json)；每個 repo 的完整路徑 inventory 見 `upstream/<repo>/inventory.json`。下表列出主要檔案（`09–16` 新增者標註）。

| Repository | 檔案與固定來源 | 本機原檔 |
|---|---|---|
| `ageron/handson-mlp` | [README.md](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/README.md) | [原檔](upstream/handson-mlp/README.md) |
| `ageron/handson-mlp` | [LICENSE](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/LICENSE) | [原檔](upstream/handson-mlp/LICENSE) |
| `ageron/handson-mlp` | [pyproject.toml](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/pyproject.toml) | [原檔](upstream/handson-mlp/pyproject.toml) |
| `ageron/handson-mlp` | [01_the_machine_learning_landscape.ipynb](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/01_the_machine_learning_landscape.ipynb) | [原檔](upstream/handson-mlp/01_the_machine_learning_landscape.ipynb) |
| `ageron/handson-mlp` | [02_end_to_end_machine_learning_project.ipynb](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/02_end_to_end_machine_learning_project.ipynb) | [原檔](upstream/handson-mlp/02_end_to_end_machine_learning_project.ipynb) |
| `ageron/handson-mlp` | [03_classification.ipynb](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/03_classification.ipynb) | [原檔](upstream/handson-mlp/03_classification.ipynb) |
| `ageron/handson-mlp` | [04_training_linear_models.ipynb](https://github.com/ageron/handson-mlp/blob/47eba45aacc85feae51ba7db68dd1ca66cb25e0a/04_training_linear_models.ipynb) | [原檔](upstream/handson-mlp/04_training_linear_models.ipynb) |
| `leonjyentub/MachineLearning2025` | [README.md](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/README.md) | [原檔](upstream/MachineLearning2025/README.md) |
| `leonjyentub/MachineLearning2025` | [pyproject.toml](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/pyproject.toml) | [原檔](upstream/MachineLearning2025/pyproject.toml) |
| `leonjyentub/MachineLearning2025` | [00_whatisSigmoid.py](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/00_whatisSigmoid.py) | [原檔](upstream/MachineLearning2025/00_whatisSigmoid.py) |
| `leonjyentub/MachineLearning2025` | [00_sklearn_shuffle.py](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/00_sklearn_shuffle.py) | [原檔](upstream/MachineLearning2025/00_sklearn_shuffle.py) |
| `leonjyentub/MachineLearning2025` | [01_regression.ipynb](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/01_regression.ipynb) | [原檔](upstream/MachineLearning2025/01_regression.ipynb) |
| `leonjyentub/MachineLearning2025` | [01_batchgradientDescent.ipynb](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/01_batchgradientDescent.ipynb) | [原檔](upstream/MachineLearning2025/01_batchgradientDescent.ipynb) |
| `leonjyentub/MachineLearning2025` | [01_gradientDescent_weight_bias.ipynb](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/01_gradientDescent_weight_bias.ipynb) | [原檔](upstream/MachineLearning2025/01_gradientDescent_weight_bias.ipynb) |
| `leonjyentub/MachineLearning2025` | [01_Logistic_Regression_scratch_Iris1.ipynb](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/01_Logistic_Regression_scratch_Iris1.ipynb) | [原檔](upstream/MachineLearning2025/01_Logistic_Regression_scratch_Iris1.ipynb) |
| `leonjyentub/MachineLearning2025` | [01_Logistic_Regression_scratch_Iris2.ipynb](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/01_Logistic_Regression_scratch_Iris2.ipynb) | [原檔](upstream/MachineLearning2025/01_Logistic_Regression_scratch_Iris2.ipynb) |
| `leonjyentub/MachineLearning2025` | [01_Logistic_Regression_sklearn_iris3.py](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/01_Logistic_Regression_sklearn_iris3.py) | [原檔](upstream/MachineLearning2025/01_Logistic_Regression_sklearn_iris3.py) |
| `leonjyentub/MachineLearning2025` | [01_ROC_AUC.py](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/01_ROC_AUC.py) | [原檔](upstream/MachineLearning2025/01_ROC_AUC.py) |
| `leonjyentub/MachineLearning2025` | [02_Polynomial_Regression_Early_stopping.ipynb](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/02_Polynomial_Regression_Early_stopping.ipynb) | [原檔](upstream/MachineLearning2025/02_Polynomial_Regression_Early_stopping.ipynb) |
| `leonjyentub/MachineLearning2025` | [02_Polynomial_Regression_overfitting.ipynb](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/02_Polynomial_Regression_overfitting.ipynb) | [原檔](upstream/MachineLearning2025/02_Polynomial_Regression_overfitting.ipynb) |
| `leonjyentub/MachineLearning2025` | [02_Regularization_Regression.ipynb](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/02_Regularization_Regression.ipynb) | [原檔](upstream/MachineLearning2025/02_Regularization_Regression.ipynb) |
| `leonjyentub/MachineLearning2025` | [02_kfold_StratifiedKFold.py](https://github.com/leonjyentub/MachineLearning2025/blob/3da2cb56b9efd17d7cd34602589f392554b40603/02_kfold_StratifiedKFold.py) | [原檔](upstream/MachineLearning2025/02_kfold_StratifiedKFold.py) |
| `ageron/handson-mlp` | *（09–16 新增）* `05_decision_trees.ipynb`、`06_ensemble_learning_and_random_forests.ipynb`、`07_dimensionality_reduction.ipynb`、`08_unsupervised_learning.ipynb`、`09_artificial_neural_networks.ipynb`、`Appendix_C_support_vector_machines.ipynb` | `upstream/handson-mlp/` |
| `leonjyentub/MachineLearning2025` | *（09–16 新增）* `03_Decision_Tree_from_scratch.py`、`03_Decision_Tree_sklearn_moon.py`、`03_Adaboost_from_scratch.ipynb`、`03_hingeloss.ipynb`、`03_svm_kernel.py`、`03_Random_Forest.py`、`04_PCA_from_scratch.py`、`04_SVD_from_scratch.py`、`04_LLE_swiss_roll.ipynb`、`05_GMM_from_scratch.py`、`05_DBSCAN.ipynb`、`05_Clustering_DBSCAN.py`、`05_Kmeans+SemiSupervisedLearning.ipynb`、`06_ANN_from_Scratch_MNIST.py`、`06_Activation_functions.py`、`06_neural_nets_with_keras.ipynb` | `upstream/MachineLearning2025/` |

完整 repository 路徑 inventory 也保留，僅擷取相關原檔，未下載／執行不相干專案。重建快照可先執行 `scripts/fetch_upstream.py` 再執行 `scripts/download_sources.py`；前者固定上述 commits，不會自動追蹤最新 main。

## API 補充參考

- [scikit-learn 1.7 common pitfalls](https://scikit-learn.org/1.7/common_pitfalls.html)：前處理／選特徵的洩漏與 Pipeline。
- [scikit-learn 1.7 cross-validation](https://scikit-learn.org/1.7/modules/cross_validation.html)：分層、群組與時間切分。
- [uv locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/)：lockfile 與環境同步。

API 說明僅用來確認本次實作；原始教學程式的主要來源仍為上列兩個 GitHub 專案。
