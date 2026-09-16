# 本次執行與驗證紀錄

驗證日期：2026-09-09（`00–08`）／2026-09-09 擴充（`09–16`）。環境：macOS arm64、Python 3.12.10、scikit-learn 1.7.2，使用本資料夾 uv 環境。各 Notebook 在全新的本機核心由第一格執行到底，保存實際輸出。**驗證模式為 fast**；full 的資料量分支已提供，但未作完整執行驗證。

## 執行結果

| Notebook | Code cells | 本機秒數 | 結果 |
|---|---:|---:|---|
| 00_環境與重現性.ipynb | 4 | 1.38 | PASS |
| 01_從資料到線性模型.ipynb | 5 | 1.87 | PASS |
| 02_驗證正則化與早停.ipynb | 8 | 2.56 | PASS |
| 03_房價資料探索與切分.ipynb | 8 | 2.71 | PASS |
| 04_房價Pipeline與模型選擇.ipynb | 10 | 13.04 | PASS |
| 05_Iris邏輯斯迴歸與多類別.ipynb | 7 | 1.86 | PASS |
| 06_混淆矩陣閾值與ROC.ipynb | 6 | 1.92 | PASS |
| 07_MNIST分類與錯誤分析.ipynb | 10 | 23.01 | PASS |
| 08_研究延伸與常見陷阱.ipynb | 9 | 2.53 | PASS |
| 09_線性模型與最佳化.ipynb | 8 | 2.56 | PASS |
| 10_正則化與機率分類.ipynb | 9 | 2.46 | PASS |
| 11_決策樹與SVM.ipynb | 9 | 3.20 | PASS |
| 12_集成學習與隨機森林.ipynb | 8 | 10.82 | PASS |
| 13_降維與資料表示.ipynb | 8 | 3.22 | PASS |
| 14_分群與表示應用.ipynb | 7 | 3.03 | PASS |
| 15_密度分群與機率模型.ipynb | 9 | 2.44 | PASS |
| 16_人工神經網路入門.ipynb | 8 | 2.51 | PASS |

總計 **17 本、133 個 code cells、零執行錯誤**。時間包含核心啟動與 HTML 輸出；不同硬體、快取與執行順序會改變耗時。00 初次建立 Matplotlib 字型快取的提示屬正常訊息。

`00–08` 對齊投影片補充（2026-09-09）：02 加 (3,0)／(1.5,1.5) L1／L2 快算；05 加 $y=1$、$\hat p=0.9/0.6/0.1$ 交叉熵對照；04 CV 表加常數均值基準列並補 `test_R2`；07 補 `multiclass_test_micro_F1` 並 assert 等於 accuracy。

`09–16` 新增（對應投影片 04–11／主教材 Ch.4–9）：每本內含該週手算活動的 `assert` 驗算格（三點決定線、GD 更新、L1／L2、閾值、softmax、Gini／分割、迴歸葉、投票、AdaBoost、PCA 共變異、解釋變異、一維 K-means、輪廓、DBSCAN 鄰域、EM 軟指派、AIC／BIC、XOR、sigmoid 神經元、參數數目），全部通過。`16` 以 numpy 與 `sklearn.neural_network` 取代 Keras／PyTorch。

## 其他檢查

- `pytest -q`：**7 passed**；包含未 fit／欄數錯誤、零分母、clone 狀態、推論不重新估計填補統計、固定切分、原檔 hash（44 個）、跨 Python 程序載入、未知類別與缺失值處理等檢查。
- `validate_deliverables.py`：**17 本 Notebook**、所有 code cell 語法、連續 execution counts、零 error outputs、HTML 存在、PNG／SVG 結構與來源／資料雜湊皆通過（`PASS: 17 notebooks, 133 executed code cells, 58 PNG/SVG pairs`）。
- **44 個**擷取原始檔 SHA-256 與 `upstream/manifest.json` 相符；三組本機資料亦相符。
- **58 組 PNG／SVG** 已產生；早停曲線加上最佳 epoch 附近的局部放大。
- HTML 圖片為內嵌；`09–16` 的內建資料（iris／digits／sample image）與合成資料 seed 固定，可離線重跑。數學排版與 widget 前端不包含在離線瀏覽保證中。

## 實際結果摘錄

以下是本次縮小規模的教學實驗，不與原書或舊投影片的不同設定直接比較。

- GDP 33,442.8 美元的線性模型生活滿意度預測：**6.0161**。
- 教師原 ROC 兩組陣列，修正積分順序後 AUC：**0.95／0.57**；手算八筆案例 AUC：**0.6875**。
- 早停最佳 epoch：**514**，於第 594 輪觸發 patience；使用已保存的最佳模型。
- Housing：開發 6,000、test 4,128；RMSE **53,174.85 美元**，MAE **35,352.76 美元**，$R^2$ **0.789**；固定模型 RMSE 的 percentile bootstrap 95% CI **[50,976.83, 55,673.42]**。常數均值基準 CV RMSE 約 **115,526 美元**，四個模型都明顯優於它。
- MNIST 二元辨識 5：fit 9,000、validation 3,000、test 10,000；OOF AP 選出 RandomForest，validation 閾值 **0.3167**。test precision **94.38%**、recall **90.36%**；CM `[[9060,48],[86,806]]`，列為真實、欄為預測，負例在前。
- MNIST 固定多類別 SGD：test accuracy **86.38%**、macro F1 **0.8621**、weighted F1 **0.8646**、micro F1 **0.8638**（＝accuracy）；沒有宣稱復現原書的成效。
- 合成亂數標籤、8 次重複：洩漏流程平均 CV accuracy **75.36%**，正確 Pipeline **50.83%**。

後續八週（`09–16`，皆為縮小規模的教學示例）：

- 09：批次 GD 學習率 0.02／0.3／1.05 的最終記錄 MSE 約 **1.43／1.02／3.9e6**（1.05 發散）；正規方程／`lstsq`／`pinv` 係數一致。
- 10：手寫 logistic（virginica、花瓣寬度）0.5 決策邊界約 **1.67 cm**；softmax `[0,1,2]` → `[.09003,.24473,.66524]`，class-2 loss **0.40761**；`GridSearchCV` 選 `C=1`，test accuracy **0.911**。
- 11：Gini `[4,0]/[2,2]/[3,1]` = **0／.5／.375**；分割方案 A 相對父節點下降 **0.3**、B 下降 **0**；PCA 旋轉後樹深度 **5→4**。
- 12：AdaBoost 第一輪 $r=0.25$、$\alpha=\ln 3\approx1.0986$；bagging OOB **0.891**；stacking in-sample 特徵 blender train acc **1.0** vs 折外 **≈0.87**。
- 13：digits 保留 95% 變異需 **28／64** 維；2／10／30 主成分的重建 MSE **13.43／4.91／0.76**、分類 CV **0.60／0.92／0.96**；JL 最小維度（n=600, eps=0.2）**1476**。
- 14：一維 K-means `[0,1,4,5]` inertia **2→1**；輪廓分數選 **k=5**；digits 50 標籤預算 accuracy 隨機 **0.837** → 代表樣本 **0.878** → 傳播全訓練 **0.933**。
- 15：一維鄰域計數 `[3,3,4,2,1]`；EM 軟指派 `[.8,.2]`、M-step μ_A=**0.4**、var_A=**0.64**；AIC 偏好 B（208<210）、BIC 偏好 A（223.0<228.8）；GMM BIC 在合成資料選 **3** 成分；PCA 重建誤差對「非 8」數字標出率 **0.98** vs 保留 8 的 **0.06**。
- 16：XOR 網路四組輸入與真值表一致；單一 sigmoid 神經元 L **0.036165 → 0.034789**（一次更新後下降）；10→50→3 參數共 **703**；numpy `TinyMLP` 於 digits test accuracy **0.962**；`MLPClassifier` 與標準化 logistic 在此小資料上互有高低。

原始數據見 `outputs/reports/*.json`；本檔為此次結果快照。修改程式、資料或模式並重跑後，應以新 JSON／Notebook 輸出為準，再更新此紀錄。

## 結論界線

模型只完成本機儲存／載入與原始欄位推論示範，未建置外部服務。CI 未涵蓋重新訓練、選模、地理相依及未來漂移；validation 上選出的 precision 閾值也不構成部署保證。合成實驗用來隔離機制，不是普遍方法排名或 NFL 定理證明。
