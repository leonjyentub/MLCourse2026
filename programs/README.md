# 機器學習教學程式

以 **26 本可編輯 Jupyter Notebook** 配合 `slides/00–25`。檔名與投影片完全一致；投影片中的「配套 Notebook」以純文字標示對應檔名。各本可單獨上傳 Colab，從第一個程式格執行。

Notebook 的既有輸出已清空，避免把舊環境的結果誤認為 Colab 本次執行。教師可在對應段落重新執行程式並展示圖表；[教學對照與取捨](TEACHING_MAP.md) 說明每本的使用位置。

## Notebook 導覽

### 基礎與傳統機器學習（00–11）

| 檔案 | 使用時機 | 主要內容 |
|---|---|---|
| [00 課程導覽](notebooks/00_課程導覽.ipynb) | 課前 | 樣本、特徵、目標與訓練／測試切分 |
| [01 機器學習概觀](notebooks/01_機器學習概觀.ipynb) | Ch.1 | 生活滿意度、k-NN／線性模型、泛化、正則化、評估陷阱 |
| [02 端到端機器學習專案](notebooks/02_端到端機器學習專案.ipynb) | Ch.2 | 房價 EDA、分層切分、完整 Pipeline、CV、搜尋、final test |
| [03 分類與模型評估](notebooks/03_分類與模型評估.ipynb) | Ch.3 | Iris、MNIST、混淆矩陣、PR／ROC、閾值與錯誤分析 |
| [04 線性模型與最佳化](notebooks/04_線性模型與最佳化.ipynb) | Ch.4 | 最小平方、GD／SGD、學習率與學習曲線 |
| [05 正則化與機率分類](notebooks/05_正則化與機率分類.ipynb) | Ch.4 | Ridge／Lasso／ElasticNet、logistic、softmax |
| [06 決策樹與 SVM 補充](notebooks/06_決策樹與SVM補充.ipynb) | Ch.5 | CART、不純度、正則化與 RBF SVM |
| [07 集成學習與隨機森林](notebooks/07_集成學習與隨機森林.ipynb) | Ch.6 | voting、bagging、forest、boosting、stacking |
| [08 降維與資料表示](notebooks/08_降維與資料表示.ipynb) | Ch.7 | PCA、重建、LLE、隨機投影 |
| [09 分群與表示應用](notebooks/09_分群與表示應用.ipynb) | Ch.8 | K-means、輪廓、量化、少量標註 |
| [10 密度分群與機率模型](notebooks/10_密度分群與機率模型.ipynb) | Ch.8 | DBSCAN、GMM／EM、異常、AIC／BIC |
| [11 人工神經網路入門](notebooks/11_人工神經網路入門.ipynb) | Ch.9 | Perceptron、XOR、反向傳播、numpy MLP |

### 深度學習、Transformer 與附錄（12–25）

| 檔案 | 課堂短實驗 |
|---|---|
| [12 梯度與遷移](notebooks/12_深層神經網路訓練_梯度與遷移.ipynb) | 導數連乘與梯度範數裁剪 |
| [13 最佳化與正則化](notebooks/13_深層神經網路訓練_最佳化與正則化.ipynb) | GD 與 Momentum 的損失曲線 |
| [14 CNN](notebooks/14_卷積神經網路_影像特徵與架構.ipynb) | 2D 互相關、ReLU 與 pooling |
| [15 遷移、偵測與分割](notebooks/15_電腦視覺_遷移學習與偵測分割.ipynb) | IoU 與 NMS |
| [16 RNN 與時間序列](notebooks/16_序列模型_RNN與時間序列預測.ipynb) | 視窗預測與 persistence 基準 |
| [17 詞嵌入與注意力](notebooks/17_自然語言處理_詞嵌入與注意力.ipynb) | scaled dot-product attention |
| [18 Transformer](notebooks/18_Transformer_注意力架構與預訓練.ipynb) | 位置編碼與 causal mask |
| [19 LLM](notebooks/19_大型語言模型_生成與聊天系統.ipynb) | temperature、greedy 與 top-k sampling |
| [20 視覺與多模態 Transformer](notebooks/20_視覺與多模態Transformer.ipynb) | patchify 與圖文餘弦相似度 |
| [21 Transformer 加速與 PEFT](notebooks/21_Transformer加速_推論與參數高效微調.ipynb) | KV cache 與 LoRA 參數量 |
| [22 生成模型](notebooks/22_生成模型_自編碼器GAN與擴散.ipynb) | 欠完備表示與重建誤差 |
| [23 強化學習](notebooks/23_強化學習_策略價值與深度RL.ipynb) | epsilon-greedy bandit |
| [24 自動微分](notebooks/24_附錄A_自動微分與計算圖.ipynb) | 解析梯度與有限差分 |
| [25 混合精度與量化](notebooks/25_附錄B_混合精度與量化.ipynb) | 對稱 int8 量化 |

先前產生的 [HTML 閱讀入口](outputs/html/index.html) 保留作歷史快照；Notebook 目前已清空舊執行輸出，請重新執行後再將新結果用於授課。互動滑桿需 Jupyter，HTML 的數學排版可能需要瀏覽器載入 MathJax。

## 環境與開啟方式

每本 Notebook 現可直接上傳 Google Colab，從第一個程式格依序執行。第一格只安裝該本需要的 Python 套件；第二格準備本章的繪圖、輸出與資料讀取程式。01、02 在首次需要時下載並核對固定版本的 CSV，03、07 在首次需要時下載 MNIST；其餘 Notebook 不會下載外部資料。這些 NumPy／scikit-learn 的 CPU 實驗沒有可直接切換的 CUDA 後端。若需重現舊版套件環境，本機仍可使用 `uv.lock`。

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

本機交付附有 `data/lifesat.csv`、`data/housing.csv`、`data/mnist_784_v1.npz`。Colab 的檔案是暫時的；01、02、03、07 會在首次需要時自動下載各自使用的資料。前兩份 CSV 依固定來源的 SHA-256 驗證，MNIST 由 OpenML 下載並檢查資料維度。若要在本機預先備妥資料，可執行：

```sh
uv run python scripts/fetch_data.py
uv run python scripts/fetch_data.py --verify-only
```

`data/manifest.json` 記錄固定來源、版本及 SHA-256；異動檔案會報錯。已附資料與已安裝環境可離線重跑；第一次安裝套件或重新下載資料需要網路。MNIST 額外的 `data/openml_cache/` 是下載快取，不是 Notebook 的必要讀取檔案。

`04–25` 另使用 scikit-learn 內建、隨套件安裝、不需下載的資料，以及固定 seed 的合成資料。`12–25` 刻意採 NumPy／scikit-learn 的小型機制實驗，完整 PyTorch／Hugging Face 訓練仍參考固定版本的作者 Notebook。

| 模式 | Housing 開發／test | MNIST fit／validation／test |
|---|---|---|
| 預設 `fast`，本次已驗證 | 6,000／4,128 | 9,000／3,000／10,000 |
| `full`，較耗時，未完整執行驗證 | 16,512／4,128 | 45,000／15,000／10,000 |

Housing 02 的 EDA 始終使用完整 16,512 筆 training；同一本的 fast 模式再由其分層抽 6,000 筆作模型開發。MNIST 使用真正的 70,000 張資料；fast 只縮減開發量。完整模式仍採相同小型模型與搜尋範圍，不等於原書完整實驗。

設定模式須在啟動核心前完成：

```sh
MLCOURSE_PROFILE=full uv run jupyter lab
```

## 重跑、圖表與驗證

各本可獨立執行，無需先執行前一本。以 `.ipynb` 為正式編修來源；編修後執行「Restart Kernel and Run All」。以下本機批次命令會覆寫 Notebook 的執行輸出；首次執行可能需下載套件或資料：

```sh
uv run python scripts/execute_notebooks.py --html
uv run pytest -q
uv run python scripts/validate_deliverables.py
```

只執行指定前綴，例如端到端專案與 CNN：

```sh
uv run python scripts/execute_notebooks.py 02 14 --html
```

若要在課堂上快速示範網格搜尋、隨機搜尋與 n-fold 成本，不必開啟 Notebook：

```sh
uv run python scripts/hyperparameter_search_demo.py
```

示例只讀本機 `data/housing.csv`，預設抽樣 3,000 列、使用 3-fold；可用
`--rows`、`--cv` 與 `--n-iter` 調整規模。程式先以 CV 比較兩種搜尋，再由勝出者對保留測試集做一次最終評估。

- `outputs/figures/`：PNG 與可編輯 SVG。
- `outputs/reports/`：機器可讀的實際數據。
- `outputs/execution.json`：逐本執行時間與成功狀態。
- `outputs/models/`：02 產生的完整房價管線及中繼資料，可重新生成，不納入 Git。
- 舊環境的驗證紀錄已整併於根目錄 `README.md`，不代表 Colab 版已完成全套執行。

本機推論示範：

```sh
uv run python scripts/predict_housing.py
uv run python scripts/predict_housing.py --csv your_raw_housing_features.csv
```

無 `--csv` 時使用原 CSV 前五列，只作載入與 API 示範，不是新增泛化評估。推論 CSV 需有九個原始特徵；缺欄會明確報錯。

## 來源與閱讀界線

[SOURCES.md](SOURCES.md) 記錄固定 commit、逐本改編、原程式修正與授權；`upstream/` 保存傳統 ML 章節所需的原始檔案。原始資料、書中數字、舊 PPTX 數字與本次重跑結果均分開閱讀。

這些實驗用來解釋與檢查方法，不能宣稱某模型普遍最好；少量資料、不同切分與縮小後的模型設定會影響結果。測試資料只用於事先指定流程的最後評估，不能拿來反覆選參數。

## License 與第三方來源

本課程 `notebooks/00–25` 的作者自編／具有授權權利的改編程式及文字採 [Apache License 2.0](LICENSE)。來源、改編或參考範圍及授權集中記錄於 [NOTICE.md](NOTICE.md)、[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)、[SOURCES.md](SOURCES.md)；這不代表原作者程式均由本課程作者獨立創作。`upstream/handson-mlp/` 仍保留上游原始授權。`MachineLearning2025` 為作者自有專案，現已補設 Apache-2.0 LICENSE；其本地固定 commit 快照仍保留歷史原貌，不更動 checksum。第三方資料、圖片、字型與外部模型不因本程式授權而重新授權。
