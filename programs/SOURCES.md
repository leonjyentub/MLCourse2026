# 程式來源與修改對照

## 固定來源

| 來源 | 固定 commit | 本地保存與使用方式 |
|---|---|---|
| [ageron/handson-mlp](https://github.com/ageron/handson-mlp) | `47eba45aacc85feae51ba7db68dd1ca66cb25e0a` | Ch.1–9 與 Appendix C 原檔保存在 `upstream/handson-mlp/`；Ch.10–19、Appendix A／B 依同一 commit 核對，縮編來源寫入 12–25 Notebook |
| [leonjyentub/MachineLearning2025](https://github.com/leonjyentub/MachineLearning2025) | `3da2cb56b9efd17d7cd34602589f392554b40603` | 相關 `.py`／`.ipynb` 原檔保存在 `upstream/MachineLearning2025/` |

`upstream/manifest.json` 記錄 44 個本地快照的 URL、commit 與 SHA-256；這些原始檔保持位元組不變。教學改寫只放在 `notebooks/`。作者程式的 cell 編號從 0 起算。

## Notebook 對應

| 教學 Notebook | 主要來源與改編 |
|---|---|
| 00 | 自編環境、資料 hash 與 seed 檢查 |
| 01 | handson Ch.1／Ch.4；教師 regression、batch GD、overfitting、regularization、early stopping；合併原 01、02、08 |
| 02 | handson Ch.2；教師 KFold；合併原房價 EDA 與 Pipeline 兩本 |
| 03 | handson Ch.3／Ch.4；教師 Iris 與 ROC；合併 Iris、threshold、MNIST 三本 |
| 04 | handson Ch.4；教師 batch GD、weight／bias GD、regression |
| 05 | handson Ch.4；教師 regularization 與 scratch logistic |
| 06 | handson Ch.5、Appendix C；教師 decision tree、hinge loss、SVM kernel |
| 07 | handson Ch.6；教師 AdaBoost 與 random forest |
| 08 | handson Ch.7；教師 PCA、SVD、LLE |
| 09 | handson Ch.8 K-means；教師 semi-supervised K-means |
| 10 | handson Ch.8 DBSCAN／GMM；教師 DBSCAN、GMM |
| 11 | handson Ch.9；教師 ANN from scratch、activation functions、舊 Keras 例 |
| 12–13 | handson Ch.11；教師 ANN、batch GD、regularization、early stopping |
| 14–15 | handson Ch.12；教師 ANN 只作 MLP／CNN 結構對照 |
| 16 | handson Ch.13 的時間序列、視窗與 RNN 流程 |
| 17 | handson Ch.14 的 embedding 與 attention |
| 18–19 | handson Ch.15 的位置編碼、mask、decoder 與 sampling |
| 20 | handson Ch.16 的 ViT patch 與 CLIP 圖文嵌入 |
| 21 | handson Ch.17 的 KV cache、projection sharing 與訓練加速 |
| 22 | handson Ch.18；教師 PCA／SVD 作線性自編碼器對照 |
| 23 | handson Ch.19 的 policy、Q-learning 與深度 RL 流程 |
| 24 | handson Appendix A；教師手刻 ANN backward 作對照 |
| 25 | handson Appendix B 的混合精度與量化 |

## 重要修正與取捨

- 教師 ROC 原例的閾值方向與端點另行校正，再與 scikit-learn AUC 互驗。
- 線性代數範例優先用 `lstsq`／SVD，不把顯式反矩陣當成一般實務作法。
- 早停保存並恢復最佳 checkpoint；validation 用於選擇，test 只在流程決定後開啟。
- Pipeline 的前處理在每一折內重新 fit，避免資料洩漏。
- 12–25 不複製需要 GPU、外部模型或長時間下載的完整實驗；改用固定 seed 的小資料隔離同一機制，並在 Notebook 明示證據界線。
- Apache-2.0 來源保留授權與歸屬；MachineLearning2025 快照沒有根目錄 LICENSE，因此不推定額外授權。
