# 06–11 投影片內容檢查與修訂紀錄

檢查日期：2026-09-20。以 `book/` 的章節順序作主線，逐章核對可教學的概念、公式、例題、方法限制與操作流程，再整合舊 PPTX 和原始程式。以下頁碼均為**修訂後 Marp 頁碼，含封面、休息與選讀頁**；不沿用既有 PDF 的頁碼。

## 檢查結論與範圍

原稿已涵蓋大部分書本主線，並非整章缺漏；主要不足是部分原理只列名稱、舊稿推導未完整銜接、程式與數學慣例不同未解釋，以及少數示例解讀不準確。本次已補入教學頁並重排。這六份對應書中 **Ch.5–9**：06→Ch.5、07→Ch.6、08→Ch.7、09–10→Ch.8、11→Ch.9。

舊教材的內容以概念等價整合、手算重寫或選讀導引保留，不逐張複製重複引言、空白頁及工具截圖。Ch.10–11 的框架與深層訓練只作後續閱讀銜接；其餘書本章節不屬於本次六週的完整涵蓋範圍。

來源位置已核實：

- 參考書：`book/CHAPTER 05 Decision Trees.pdf` 至 `CHAPTER 09 Introduction to Artificial Neural Networks.pdf`。
- 原課程程式：實際目錄是 [`programs/upstream/MachineLearning2025/`](programs/upstream/MachineLearning2025/)，不是根目錄的 `upstream/`。本次對照 16 份相關 `.py`／`.ipynb`，未修改或執行它們。
- 原投影片：[`source_pptx/`](source_pptx/) 中 03、04、05、06 四份 PPTX，合計 172 頁，其中 ANN 第 39 頁為空白。文字與 Office 數學文字均納入比對。
- upstream 的 inventory 沒有 PPTX 項目，因此只確認本機舊 PPTX 的內容，沒有宣稱它們與 upstream 某次提交完全相同。舊投影片提到、但這份快照沒有的檔名，也不標成「已移植程式」。

## 每週修訂摘要

| 投影片 | 原頁數 → 新頁數 | 選讀頁 | 本次補充重點 |
|---|---:|---:|---|
| [06 決策樹與SVM補充](<slides/06_決策樹與SVM補充.md>) | 33 → 43 | 4 | 特徵型態、資訊增益／演算法、樹的成本、原 80 筆手算、SVM 損失與核推導 |
| [07 集成學習與隨機森林](<slides/07_集成學習與隨機森林.md>) | 40 → 46 | 1 | Voting／Bagging／Stacking 操作、森林重要度、AdaBoost 慣例對照、GBRT／HGB 差異 |
| [08 降維與資料表示](<slides/08_降維與資料表示.md>) | 34 → 43 | 4 | 高維機率、SVD 尺度與原矩陣手算、手刻／函式庫比較、Pipeline、LDA、t-SNE |
| [09 分群與表示應用](<slides/09_分群與表示應用.md>) | 34 → 38 | 0 | 應用界線、K-means API、K-means++ 機率、加速、影像分割、代表標註操作 |
| [10 密度分群與機率模型](<slides/10_密度分群與機率模型.md>) | 36 → 42 | 1 | DBSCAN 擴張、樹狀圖、K-means／GMM 差異、穩定 EM、參數計數、異常資料假設 |
| [11 人工神經網路入門](<slides/11_人工神經網路入門.md>) | 37 → 51 | 7 | 歷史與限制、梯度消失／輸出梯度、訓練流程、批次／容量、激活／Dropout／紀錄與框架選讀 |

合計 **214 → 263 頁，新增 49 頁**。其中 17 頁明確標為選讀，放在對應概念旁；可以課後閱讀，或替換同段內容。各週課堂主線仍為 180 分鐘：50 分鐘＋休息 10 分鐘＋60 分鐘＋休息 10 分鐘＋50 分鐘。選讀的 `minutes=0` 表示不計入課堂主線，並非不需閱讀時間；新增主線頁的時間由同段講解與活動重新分配。

## 參考書教學內容覆蓋

「補充」表示原稿較簡略、只有名稱或缺少操作關係，本次已加強；「保留」表示原有內容足以支撐本週教學。章末的大型實驗以作業安排，不宣稱已執行。

| 書本主題 | 修訂後位置 | 檢查與處理 |
|---|---|---|
| Ch.5 決策路徑、分類區域、葉節點機率 | 06 p.3–7 | 保留圖 5-1、5-2；補特徵型態、類別編碼及缺失值條件 |
| Ch.5 Gini、Entropy、CART、資訊增益 | 06 p.8–18 | 補指標與 ID3／C4.5／CART 的區別、計算成本、遞迴與原 80 筆分割例 |
| Ch.5 正則化、剪枝、迴歸樹 | 06 p.19–27 | 保留原圖與加權 MSE；補預剪枝與 `ccp_alpha` 的差別 |
| Ch.5 座標方向、PCA 旋轉、變異 | 06 p.29–31、42–43 | 圖 5-9 修正為相同資料重訓的隨機性；與資料擾動概念區分 |
| Ch.6 硬／軟投票、大數法則 | 07 p.3–8 | 補機率條件及 `VotingClassifier`；避免把多樣性說成必勝保證 |
| Ch.6 Bagging／Pasting、OOB、特徵抽樣 | 07 p.9–13 | 補訓練、OOB 查詢與無放回抽樣的限制 |
| Ch.6 Random Forest／Extra Trees、重要度 | 07 p.14–16 | 補每節點候選特徵、重要度計算與 bootstrap 差異 |
| Ch.6 AdaBoost | 07 p.18–24 | 保留四個公式與手算；補舊程式的對稱更新等價條件 |
| Ch.6 Gradient Boosting、早停、隨機化 | 07 p.25–31 | 保留殘差圖、逐輪放大與學習率取捨 |
| Ch.6 HGB、其他提升樹框架 | 07 p.33–34、43–44 | 補 GBRT 與 HGB 參數名稱差異；外部框架僅作方法導引 |
| Ch.6 Stacking 與方法總表 | 07 p.35–46 | 保留 OOF、防洩漏與完整方法比較；補操作介面 |
| Ch.7 維度災難、投影、流形 | 08 p.3–10 | 補高維落在邊界附近的機率手算；保留 Swiss roll 圖 |
| Ch.7 PCA 目標、SVD、中心化 | 08 p.11–20 | 補特徵值與奇異值的樣本數尺度、手刻比較與舊矩陣手算 |
| Ch.7 解釋變異、保留維度、壓縮／逆投影 | 08 p.21–25 | 保留累積曲線、重建與均值還原；154 維等仍是來源示例 |
| Ch.7 隨機／增量 PCA、選參數 | 08 p.26–29 | 補 partial_fit 後固定投影、PCA 與分類器一起 CV，放在實作前 |
| Ch.7 隨機投影、JL、稀疏投影 | 08 p.31–33 | 保留維度界線、機率界線與成本取捨 |
| Ch.7 LLE、其他方法、練習 | 08 p.34–43 | 保留 LLE 兩步與限制；補 LDA、t-SNE 相似度／困惑度和實驗安排 |
| Ch.8 分群用途、K-means 演算法 | 09 p.3–12 | 補推薦／搜尋等應用界線與 labels／distance／score 的區別 |
| Ch.8 初始化、多次啟動、加速／Mini-batch | 09 p.14–17 | 補 K-means++ 的 D² 抽樣、Elkan 三角不等式與每輪成本 |
| Ch.8 選 k、silhouette、限制與縮放 | 09 p.18–25 | 保留肘部圖、輪廓圖、手算與非球狀分群限制 |
| Ch.8 影像分割、距離表示 | 09 p.27–30 | 補顏色／語意／實例分割的差異；保留陣列形狀 |
| Ch.8 半監督、代表樣本、傳播／主動學習 | 09 p.31–38 | 補陣列操作；釐清 98.9% 是偽標籤品質，不是測試分類成績 |
| Ch.8 DBSCAN | 10 p.3–9 | 補核心連通、邊界不作橋、暫時雜訊、最壞記憶體成本 |
| Ch.8 其他分群方法 | 10 p.10–13 | 保留方法比較；補階層分群的合併高度與切群例 |
| Ch.8 GMM、EM、共變異 | 10 p.15–25 | 保留密度與 E/M 公式；補與 K-means 的差異及穩定計算 |
| Ch.8 機率／密度、生成、異常、似然 | 10 p.27–32 | 保留 API 角色；補離群偵測與新穎偵測的訓練資料假設 |
| Ch.8 AIC／BIC、Bayesian GMM | 10 p.33–38 | 補模型自由參數計數與同一觀測空間的比較條件 |
| Ch.8 其他異常方法與練習 | 10 p.39–42 | 保留 LOF／隔離森林／單類方法等概覽與 PCA 重建銜接 |
| Ch.9 歷史、生物啟發、Perceptron、XOR、MLP | 11 p.3–15 | 補發展條件、線性可分／收斂限制；保留 XOR 手算 |
| Ch.9 非線性、反向傳播、初始化 | 11 p.17–28 | 保留鏈式法則與形狀；補梯度消失／爆炸及更多激活的選讀 |
| Ch.9 迴歸／分類架構、損失、MLP API | 11 p.30–39 | 保留表 9-1、9-2；補 Softmax 梯度、原 MNIST 損失配對及分類 Pipeline |
| Ch.9 指標、早停、過度自信 | 11 p.40–42 | 補 epoch／批次／驗證角色；指出原書單例跳過 scaler，不能單憑其斷言校準品質 |
| Ch.9 容量、學習率、批次、遷移與練習 | 11 p.43–51 | 補參數量、學習率範圍測試；以選讀銜接正則化、紀錄與後續框架 |

## 舊投影片的位置判斷

| 舊 PPTX／頁 | 內容 | 修訂後位置與安排理由 |
|---|---|---|
| 03 s.1–16 | 線性可分、距離／margin、原始與對偶問題 | 06 p.32、35–36；在樹的限制之後作模型邊界比較 |
| 03 s.17–23 | 軟間隔、C、hinge、次梯度 | 06 p.33–34、40；先辨認違反間隔，再看最佳化 |
| 03 s.24–33 | 多項式／RBF／核實作 | 06 p.37–38、40；置於對偶之後，修正數例與 API 歸屬 |
| 03 s.34–36 | Logistic 比較、OvR／OvO | 06 p.39–42；在模型原理之後才比較限制與操作 |
| 03 s.37–51 | 節點型態、不純度、80 筆手算、剪枝與不穩定性 | 06 p.3–31；原圖 5-9 的重訓隨機性與舊稿刪樣本例分開說明 |
| 03 s.52–60 | 投票、OOB、森林、AdaBoost | 07 p.3–24；森林與 Boosting 分開，避免錯把 AdaBoost 歸為森林 |
| 04 s.1–14 | 降維動機、PCA／共變異／特徵向量 | 08 p.3–18；一般非對稱矩陣特徵值例整合為共變異手算，減少與 PCA 正半定矩陣混淆 |
| 04 s.15–24 | 手刻／sklearn PCA、MNIST、解釋變異 | 08 p.19、21–29；先對齊前處理，再比較算法與分類指標 |
| 04 s.25–29 | SVD 推導、原 3×2 矩陣、MNIST 壓縮 | 08 p.15、17、20–25；原矩陣手算保留為選讀 |
| 04 s.30–35 | LDA、LLE 與近鄰數 | 08 p.34–39、42；LDA 明確標為監督式，LLE 接流形主線 |
| 04 s.36–46 | t-SNE、KL／梯度、困惑度、PCA→t-SNE、UMAP | 08 p.40–42；公式在選讀，梯度放講者提示，UMAP 僅原稿層級的延伸導引 |
| 05 s.1–11 | 分群用途、K-means、選 k、silhouette | 09 p.3–25；完整接到後續應用 |
| 05 s.12–20 | GMM、EM 與 API | 10 p.15–27；依書本次序放在 DBSCAN／其他分群之後 |
| 05 s.21–23 | 階層分群／樹狀圖 | 10 p.10–12；置於其他分群方法段，不插斷 K-means 迭代 |
| 05 s.24–27 | DBSCAN 核心、擴張與示例 | 10 p.3–9；接續第 09 週的非球狀群限制 |
| 06 s.1–13 | 歷史、Perceptron、XOR、MLP、Playground | 11 p.3–15、51；Playground 為章末延伸 |
| 06 s.14–25 | Backprop、激活、梯度消失、初始化 | 11 p.17–28；先鏈式法則，再梯度問題與初始化 |
| 06 s.26–32 | 回歸／分類、Softmax／交叉熵梯度 | 11 p.30–39；補出激活與損失必須配對的條件 |
| 06 s.33–38 | 過擬合、Dropout、TensorBoard | 11 p.43–49；一般調參在主線，工具與深層正則化放選讀 |
| 06 s.39 | 空白 | 不納入教學內容 |

## upstream 16 份程式／Notebook 對照

下列均以 `programs/upstream/MachineLearning2025/` 為根目錄；「對應」代表已把演算法、流程或教學注意事項納入投影片，不表示已修好或重跑原程式。

| 原檔案 | 修訂後位置 | 納入與釐清 |
|---|---|---|
| `03_Decision_Tree_from_scratch.py` | 06 p.13–18 | 不純度、最佳分割、停止與遞迴；保留原 80 筆講解 |
| `03_Decision_Tree_sklearn_moon.py` | 06 p.19–21、42 | 葉節點限制與同一切分的比較 |
| `03_hingeloss.ipynb` | 06 p.33–34、40 | 分對仍可有損失、次梯度與目標尺度 |
| `03_svm_kernel.py` | 06 p.37–40、42 | 顯式展開、核模型、C／gamma；`degree` 不是 `LinearSVC` 的參數 |
| `03_Random_Forest.py` | 07 p.14–16、45 | 森林訓練、候選特徵與重要度；標準化非樹的必要條件 |
| `03_Adaboost_from_scratch.ipynb` | 07 p.21–24 | 1/2 log 對稱更新與書本慣例的等價條件 |
| `04_PCA_from_scratch.py` | 08 p.16–19、23 | 共變異特徵分解、排序、投影；函式庫比較必須用同一中心化／縮放 |
| `04_SVD_from_scratch.py` | 08 p.15、17、19–20 | 區分原資料奇異值與樣本共變異特徵值；補尺度和正交性檢查 |
| `04_LLE_swiss_roll.ipynb` | 08 p.34–36、42 | 兩步重建、近鄰數與短路／碎片化問題 |
| `05_Kmeans+SemiSupervisedLearning.ipynb` | 09 p.30–35 | 代表樣本、人工標註、labels_ 傳播與挑選可信樣本；不可硬套另一切分的標籤陣列 |
| `05_Clustering_DBSCAN.py` | 10 p.3–9 | eps、min_samples、核心與雜訊；min_samples 包含自身 |
| `05_DBSCAN.ipynb` | 10 p.3–9 | 邊界點擴張與不同參數比較 |
| `05_GMM_from_scratch.py` | 10 p.16–25 | E/M 更新與穩定對數運算；`pdf + epsilon` 不等於完整的數值穩定解法 |
| `06_ANN_from_Scratch_MNIST.py` | 11 p.23–28、37、41 | 形狀／反向傳播、Sigmoid＋MSE 配對、批次尾端資料 |
| `06_Activation_functions.py` | 11 p.18–21 | 基本激活與 Leaky／ELU／Softplus／GELU／Swish／Mish 延伸 |
| `06_neural_nets_with_keras.ipynb` | 11 p.30–39、46–49 | 分類／回歸、模型組合、保存／callbacks／TensorBoard／調參；框架完整程式留後續章 |

舊投影片另提到的 `04_SVD_MNIST.py`、`16.Cluter_Hierarchical_Clustering.py`、`18.ANN_from_Scratch_HousePrice.py` 等檔案，在這份 upstream 對照快照未找到。本次保留其教學概念與相應例題，不建立不存在的程式連結，也不宣稱已移植其程式內容。

## 重要修正與未直接沿用的說法

- **SVM 多項式數例**：原稿已有 √2 交叉項，但 `(1,1)` 的映射數例誤寫為 `(1,1,1)`；已改為 `(1,√2,1)`，並保留 XOR 分隔式。
- **SVM 比較**：移除不受離群點影響、較小 C 必然泛化較好等保證性說法；區分 SVC 的 OvO 訓練與 `decision_function_shape` 顯示格式。
- **樹與森林**：Entropy 不代表 sklearn 就在跑 ID3；Boosting 不屬於 Random Forest；圖 5-9 的現象不應錯寫為必須改資料。
- **SVD 尺度**：若共變異是 `Xc.T @ Xc / (m-1)`，則原資料奇異值為 `sqrt((m-1)*lambda)`。舊程式直接對共變異特徵值開根號，不能據此宣稱得到正交 U；資料投影方向本身另行判斷。
- **PCA／LDA／t-SNE**：PCA 不要求資料服從高斯；LDA 使用標籤；t-SNE 不保證遠距離比例，先 PCA 也不保證固定加速倍數。
- **半監督指標**：98.9% 偽標籤正確率與最終分類器測試正確率不同；原書的「前 50 筆」基準不改稱隨機抽樣。
- **GMM 選模**：補全混合權重、平均與共變異的自由參數；AIC／BIC 比較需同一觀測資料與表示空間。
- **ANN 訓練**：Backprop 計算梯度、optimizer 更新參數；Sigmoid＋MSE 不能直接沿用 Softmax＋交叉熵的輸出梯度。
- **原書 MLP 例子**：p.307 的單例呼叫 `mlp_clf.predict(X_new)` 跳過外層 scaler；教學改成 Pipeline 推論，保留書中測試約 87.1% 為來源結果，但不以該錯誤流程的高信心單例單獨證明校準品質。
- **ANN 結果與延伸**：RMSE 0.53 的房價目標單位為十萬美元；Dropout 不保證固定改善幅度；舊 Keras API 不作這週的必跑環境。

API 差異以 scikit-learn 1.7 文件核對：[決策樹](https://scikit-learn.org/1.7/modules/tree.html)、[SVC](https://scikit-learn.org/1.7/modules/generated/sklearn.svm.SVC.html)、[MLPClassifier](https://scikit-learn.org/1.7/modules/generated/sklearn.neural_network.MLPClassifier.html)、[HGB](https://scikit-learn.org/1.7/modules/generated/sklearn.ensemble.HistGradientBoostingRegressor.html)、[LDA](https://scikit-learn.org/1.7/modules/lda_qda.html)。t-SNE 相似度與梯度另對照[原始論文](https://www.jmlr.org/papers/v9/vandermaaten08a.html)。

## 驗證與交付界線

- 六份 Marp 保留原 front matter、`ml-course` 主題、16:9 與頁碼設定；來源、講者提示與時間資訊已整理於本紀錄及 `SOURCE_MAP_CH04_09.md`，投影片本身不再保留 `_footer` 與 `meta` 註解。
- 263 頁來源與頁次已同步至 [SOURCE_MAP_CH04_09.md](SOURCE_MAP_CH04_09.md)；該文件 04、05 逐頁段落保持原樣。
- 17 段 Python 片段通過 AST 語法檢查；片段所需資料與既有模型在上下文／提示中說明，未宣稱每段都是獨立可執行程式。
- 233 個公式運算式通過 KaTeX 語法檢查；手算分割、核內積、SVD、Softmax 梯度、網路參數與 GMM 參數數例另作數值核對。
- 67 個本機圖片連結有效；所有原有圖檔保持不變。
- 與修改前 21,520 份檔案的 SHA-256 基準比對，`slides/` 只有指定六份 Markdown 改變；其餘投影片、`programs/`、`book/`、`source_pptx/` 及既有 PDF 均未改動。
- 本次交付 Marp 原稿與兩份來源文件，未輸出 HTML／PDF，因此尚未做修訂後的實際投影版面檢視。既有 PDF 和其他舊課程配套中的頁碼不代表本次修訂版；本次以兩份來源文件及 Marp 為準。
