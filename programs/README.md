# 機器學習教學程式

以 **17 本可編輯 Jupyter Notebook** 配合投影片：`00–08` 對應原三週九小時（主教材 Ch.1–3），`09–16` 對應後續八週投影片（主教材 Ch.4–9）。以 Aurélien Géron 的 `handson-mlp` 第 1–9 章與附錄 C 程式為主，搭配 Leonjye 的 `MachineLearning2025` 迴歸、GD、Iris、ROC、決策樹、集成、降維、分群與 ANN 手寫範例。

Notebook 已保留本次實際執行的圖表、數值與練習答案。教師可在對應段落使用程式圖表取代部分講解，補充實驗安排課後。[教學對照與取捨](TEACHING_MAP.md) 說明每本的使用位置。

## Notebook 導覽

### 三週主線（Ch.1–3）

| 檔案 | 使用時機 | 主要內容 |
|---|---|---|
| [00 環境與重現性](notebooks/00_環境與重現性.ipynb) | 課前 | 核心、版本、資料 hash、seed |
| [01 從資料到線性模型](notebooks/01_從資料到線性模型.ipynb) | 第一週主線 | GDP／生活滿意度、線性模型、k-NN、GD |
| [02 驗證正則化與早停](notebooks/02_驗證正則化與早停.ipynb) | 第一週補充 | 多項式、CV、L1／L2／ElasticNet、最佳 checkpoint、偏差與變異數 |
| [03 房價資料探索與切分](notebooks/03_房價資料探索與切分.ipynb) | 第二週主線 | 分層切分、地理圖、相關、比率、穩定 ID |
| [04 房價 Pipeline 與模型選擇](notebooks/04_房價Pipeline與模型選擇.ipynb) | 第二週主線 | 前處理、自訂轉換器、CV、搜尋、test、CI、joblib、常數基準、R² |
| [05 Iris 邏輯斯迴歸與多類別](notebooks/05_Iris邏輯斯迴歸與多類別.ipynb) | 第三週補充 | 穩定手寫 GD、sigmoid、決策區域、OvR／OvO |
| [06 混淆矩陣閾值與 ROC](notebooks/06_混淆矩陣閾值與ROC.ipynb) | 第三週主線 | 八筆手算、容量與成本、修正原 ROC、互動滑桿 |
| [07 MNIST 分類與錯誤分析](notebooks/07_MNIST分類與錯誤分析.ipynb) | 第三週主線 | OOF、PR／ROC、閾值、macro／weighted／micro、多標籤與去噪 |
| [08 研究延伸與常見陷阱](notebooks/08_研究延伸與常見陷阱.ipynb) | 課後選做 | 洩漏、群組／時間切分、train-dev、漂移、穩健指標 |

### 後續八週（Ch.4–9）

| 檔案 | 對應投影片 | 主要內容 |
|---|---|---|
| [09 線性模型與最佳化](notebooks/09_線性模型與最佳化.ipynb) | 04 | 正規方程／lstsq／SVD、共線、批次 GD 學習率、SGD 排程、多項式、學習曲線 |
| [10 正則化與機率分類](notebooks/10_正則化與機率分類.ipynb) | 05 | Ridge／Lasso／ElasticNet 係數路徑、手寫 logistic、閾值、穩定 softmax、選 C |
| [11 決策樹與 SVM](notebooks/11_決策樹與SVM.ipynb) | 06 | `export_text`、Gini／Entropy、CART 分割增益、正則化、迴歸樹、旋轉不穩定、RBF SVM |
| [12 集成學習與隨機森林](notebooks/12_集成學習與隨機森林.ipynb) | 07 | 硬／軟投票、bagging＋OOB、森林特徵重要度、手算 AdaBoost、逐棵 GB、stacking 洩漏 |
| [13 降維與資料表示](notebooks/13_降維與資料表示.ipynb) | 08 | 維度災難、PCA 手算、累積解釋變異、重建、Swiss roll＋LLE、隨機投影與 JL |
| [14 分群與表示應用](notebooks/14_分群與表示應用.ipynb) | 09 | K-means 兩步手算、K-means++、肘部／輪廓、限制、顏色量化、少量標註傳播 |
| [15 密度分群與機率模型](notebooks/15_密度分群與機率模型.ipynb) | 10 | DBSCAN 鄰域手算、延伸規則、GMM／EM 手算、covariance_type、密度異常、AIC／BIC、PCA 重建誤差 |
| [16 人工神經網路入門](notebooks/16_人工神經網路入門.ipynb) | 11 | Perceptron、XOR 手算、激活函數、單神經元前向／反向手算、numpy MLP、`MLPClassifier` 比較 |

無需啟動核心即可閱讀 [HTML 閱讀入口](outputs/html/index.html)。圖表與文字已嵌入；互動滑桿需 Jupyter，HTML 的數學排版可能需要瀏覽器載入 MathJax。

## 環境與開啟方式

本資料夾已建立 `.venv`，採 Python **3.12.10**；主要科學套件版本固定在 `pyproject.toml`，完整相依版本由 `uv.lock` 固定。使用 CPU，無需安裝 PyTorch／CUDA。

從專案根目錄執行：

```sh
cd programs
uv sync --frozen
uv run jupyter lab
```

若系統尚未安裝 uv，依 [uv 官方安裝說明](https://docs.astral.sh/uv/getting-started/installation/) 安裝。`--frozen` 使用現有 lockfile；更新相依套件另依 [uv locking／syncing 文件](https://docs.astral.sh/uv/concepts/projects/sync/)。

VS Code 直接開啟 `.ipynb`，在「選取核心」選擇 `programs/.venv/bin/python`。不必向使用者帳號全域註冊 kernel。換電腦時不要複製 `.venv`，以 `uv sync --frozen` 重建。

若受限環境無法寫預設 uv 快取，可暫用可寫目錄，例如 macOS：

```sh
UV_CACHE_DIR=/private/tmp/mlcourse2026-uv-cache uv sync --frozen
```

## 資料與離線使用

交付已附 `data/lifesat.csv`、`data/housing.csv`、`data/mnist_784_v1.npz`。每本只讀本機檔案，不在儲存格中臨時下載。首次建立資料或補回缺檔時執行：

```sh
uv run python scripts/fetch_data.py
uv run python scripts/fetch_data.py --verify-only
```

`data/manifest.json` 記錄固定來源、版本及 SHA-256；異動檔案會報錯。已附資料與已安裝環境可離線重跑；第一次安裝套件或重新下載資料需要網路。MNIST 額外的 `data/openml_cache/` 是下載快取，不是 Notebook 的必要讀取檔案。

`09–16` 另使用 scikit-learn 內建、隨套件安裝、不需下載的資料：`load_iris`、`load_digits`、`load_sample_image('flower.jpg')`，以及 `make_moons`／`make_blobs`／`make_swiss_roll` 等合成資料（seed 固定）。`12` 的森林特徵重要度沿用本機 MNIST 快取子樣本。

| 模式 | Housing 開發／test | MNIST fit／validation／test |
|---|---|---|
| 預設 `fast`，本次已驗證 | 6,000／4,128 | 9,000／3,000／10,000 |
| `full`，較耗時，未完整執行驗證 | 16,512／4,128 | 45,000／15,000／10,000 |

Housing 03 的 EDA 始終使用完整 16,512 筆 training；04 的 fast 模式再由其分層抽 6,000 筆作模型開發。MNIST 使用真正的 70,000 張資料；fast 只縮減開發量。完整模式仍採相同小型模型與搜尋範圍，不等於原書完整實驗。

設定模式須在啟動核心前完成：

```sh
MLCOURSE_PROFILE=full uv run jupyter lab
```

## 重跑、圖表與驗證

各本可獨立執行，無需先執行前一本。以 `.ipynb` 為正式編修來源；編修後執行「Restart Kernel and Run All」。全套批次執行每本使用新的本機核心：

```sh
uv run python scripts/execute_notebooks.py --html
uv run pytest -q
uv run python scripts/validate_deliverables.py
```

只執行指定前綴，例如房價兩本：

```sh
uv run python scripts/execute_notebooks.py 03 04 --html
```

- `outputs/figures/`：PNG 與可編輯 SVG。
- `outputs/reports/`：機器可讀的實際數據。
- `outputs/execution.json`：逐本執行時間與成功狀態。
- `outputs/models/`：04 產生的完整房價管線及中繼資料，可重新生成，不納入 Git。
- `VERIFICATION.md`：本次驗證範圍、實際結果與限制。

本機推論示範：

```sh
uv run python scripts/predict_housing.py
uv run python scripts/predict_housing.py --csv your_raw_housing_features.csv
```

無 `--csv` 時使用原 CSV 前五列，只作載入與 API 示範，不是新增泛化評估。推論 CSV 需有九個原始特徵；缺欄會明確報錯。

## 來源與閱讀界線

[SOURCES.md](SOURCES.md) 記錄固定 commit、逐本改編、原程式修正與授權；`upstream/` 保存 22 個相關原始檔案，不直接執行整個來源專案。原始資料、書中數字、舊 PPTX 數字與本次重跑結果均分開閱讀。

這些實驗用來解釋與檢查方法，不能宣稱某模型普遍最好；少量資料、不同切分與縮小後的模型設定會影響結果。測試資料只用於事先指定流程的最後評估，不能拿來反覆選參數。
