# 第 05–25 章：投影片與 Notebook 雙向對照

範圍：21 份同名 Marp 與 Notebook，按章序檢查。頁次以本次 Marp 原始碼為準；每個程式格使用穩定程式代碼，可由投影片講者提示反查。

## 如何使用

- 從 Notebook 的第一個程式格依序執行；前兩格負責該本依賴與設定。程式圖存到 `outputs/figures/`（課程 programs 目錄）或 `mlcourse_outputs/figures/`（獨立執行）。
- **同程式輸出**：投影片引用 `programs/outputs/figures/` 的檔案，可由對應格產生。
- **同概念重做**：保留教材原圖，另用小型資料重畫；不保證原書的像素、分數、資料切分相同。
- **數值驗算**：指定手算例使用相同輸入，以 assertion 比較結果。
- **機制／形狀對照**：架構圖對應可執行的張量、遮罩、損失或更新程序，並非完整模型訓練。生物背景、CartPole 幾何、Atari 合成影格等另明列邊界。
- 12–25 主要以 NumPy CPU 範例驗算；PyTorch/Keras/Transformers/TRL/Gym 等完整框架片段保留為讀碼案例，不要求安裝或下載大型模型。沒有將玩具範例冒充預訓練模型成效。
- 每章新增末尾導讀頁供程式課或課後使用；保留原核心授課時間。

## 依序補齊摘要

| 章 | 補齊與修正 |
|---|---|
| 05 | L1/L2 幾何、Ridge/Lasso 曲線、早停快照、Sigmoid/交叉熵微分。 |
| 06 | 樹決策區域、迴歸樹節點、旋轉與穩定性、手刻 CART、SVM margin/hinge/kernel。 |
| 07 | 大數法則、bootstrap/OOB、AdaBoost 重加權、boosting 曲線、OOF 評估範圍。 |
| 08 | 邊界體積、平面投影、SVD/IPCA、LLE 權重、多法降維與 JL 平方距離。 |
| 09 | Lloyd 迭代、初始化與 k、逐群輪廓、代表數字、部分傳播與標註需求。 |
| 10 | DBSCAN 延伸、共變異形狀、穩定 EM、似然/MAP、階層樹與異常評估切分。 |
| 11 | 神經元與 XOR 架構、Softmax/MLP 梯度、迴歸散點、digits 錯誤與訓練控制。 |
| 12 | 激活/初始化、BN/LN、凍結/解凍、線性預訓練與圖片描述介面。 |
| 13 | 六種最佳化器、排程、Dropout/MC、Max-norm、早停與 CSV 記錄。 |
| 14 | NCHW 卷積、padding/pooling、Inception/Residual/Depthwise/SE 前向與增強。 |
| 15 | IoU/NMS 手算、逐框配對與 AP、分割/上採樣、轉置線性算子、追蹤。 |
| 16 | RNN/BPTT、固定起點多步預測、LSTM/GRU 與擴張因果卷積。 |
| 17 | Token 位移/embedding、padding/雙向RNN、beam、Luong cross-attention。 |
| 18 | 完整小型 attention block、兩種 mask、MLM/任務頭/QA 與蒸餾。 |
| 19 | 條件生成/top-p、答案遮罩/SFT/DPO、本地檢索與工具介面。 |
| 20 | Patch/視窗/金字塔、DETR 配對、對比/自蒸餾、latent queries 與門控。 |
| 21 | KV 等價、GQA/分塊 softmax、推測驗證、LoRA、MoE、packing/梯度累積。 |
| 22 | 測試重建/去噪、VAE/VQ、GAN 交替梯度、加噪及解析高斯反向取樣。 |
| 23 | 回報/Q 手算、LineWorld/Bellman/DQN、policy gradient/PPO、影格介面。 |
| 24 | 對偶數、可執行反向引擎、計算圖、分支累積與 detach。 |
| 25 | 浮點位元/BF16 模擬、loss scaling、量化粒度/PTQ/QAT/STE。 |

## 驗證範圍

每本在專案外的新 Python 程序依序執行全部程式格；使用本機既有套件，第 07 章使用既有 MNIST 快取。Notebook 執行輸出清空，重跑圖另存 PNG/SVG。此驗證不等同 Colab、首次安裝／網路下載、完整 GPU／預訓練模型訓練。

2026-10-04 驗證結果：

- 21 本 Notebook、185 個程式格全部執行通過，執行版本與最終檔案 SHA-256 一致。
- 182 個投影片圖檔引用均有對應程式與範圍說明；新增 81 組 PNG/SVG 圖表。
- Marp 共 838 頁完成瀏覽器渲染檢查，未偵測到公式解析錯誤、遺失圖片或內容超出頁面；另目視檢查 35 個新增／改寫頁面與 81 張新增圖表。
- 全課程 Notebook／圖檔驗證與 `git diff --check` 通過。第 02–04 章的投影片與 Notebook、教材原始檔及既有 PDF／HTML 與本次修改前一致。

後續匯出（2026-10-04）：已依目前原稿更新 05–25 的投影片 PDF／HTML，並以真正的 Jupyter 核心重跑全部程式格，更新含結果的 Notebook HTML；原 `.ipynb` 保留空白輸出。

## 05｜正則化與機率分類

投影片 43 頁；Notebook 13 個程式格。

L1/L2 幾何、Ridge/Lasso 曲線、早停快照、Sigmoid/交叉熵微分。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/10_regularization_paths.png` | 05-03 | 同程式輸出；`10_regularization_paths` |
| 6 正則化的幾何直覺 | `assets/ppt_l1_l2_geometry.jpeg` | 05-06 | 同概念重做；`c05_regularization_geometry` |
| 8 Ridge 的強度如何改變直線與曲線？ | `assets/chapters04_09/book_fig_4_18.png` | 05-06 | 同概念重做；`c05_regularization_geometry` |
| 10 Lasso 在多項式模型中壓掉部分項 | `assets/chapters04_09/book_fig_4_19.png` | 05-06 | 同概念重做；`c05_regularization_geometry` |
| 11 L1 與 L2 的幾何：角點與圓滑邊界 | `assets/chapters04_09/book_fig_4_20.png` | 05-06 | 同概念重做；`c05_regularization_geometry` |
| 17 早停：保留驗證表現最好的參數 | `assets/chapters04_09/book_fig_4_21.png` | 05-07 | 同概念重做；`c05_early_stopping` |
| 20 Sigmoid 把任意實數映射到 0 與 1 之間 | `assets/chapters04_09/book_fig_4_22.png` | 05-09 | 同概念重做；`c05_sigmoid_derivative` |
| 30 Iris 案例：定義正類，才能解讀機率 | `assets/chapters04_09/book_fig_4_23.png` | 05-08 | 同概念重做；`10_logistic_probability` |
| 31 一個特徵的機率曲線與 0.5 決策界線 | `assets/chapters04_09/book_fig_4_24.png` | 05-08 | 同概念重做；`10_logistic_probability` |
| 32 兩個特徵的線性決策邊界 | `assets/chapters04_09/book_fig_4_25.png` | 05-11 | 同概念重做；`10_logistic_boundary_2d` |
| 38 Softmax 的三類決策區域 | `assets/chapters04_09/book_fig_4_26.png` | 05-12 | 同概念重做；`10_softmax_regions` |

本章 11 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 05-01 / `47ea4806` | 2 | 本週任務與節奏 |
| 05-02 / `course05` | 2 | 本週任務與節奏 |
| 05-03 / `da13bd11` | 3、4、5、7、9、13、15 | 程式實驗與實際輸出；正則化：把參數大小也放入訓練目標；L1 與 L2 正則化；Ridge：平方懲罰讓係數平滑縮小；Lasso：絕對值懲罰可以產生零係數；Elastic Net：同時限制 L1 與 L2；Ridge、Lasso、Elastic Net 如何選？ |
| 05-04 / `9c76290e` | 14 | 同叫 alpha，目標函數尺度可能不同 |
| 05-05 / `830d6f78` | 5、11、15 | L1 與 L2 正則化；L1 與 L2 的幾何：角點與圓滑邊界；Ridge、Lasso、Elastic Net 如何選？ |
| 05-06 / `c05-penalty` | 6、8、10、11、12、43 | 正則化的幾何直覺；Ridge 的強度如何改變直線與曲線？；Lasso 在多項式模型中壓掉部分項；L1 與 L2 的幾何：角點與圓滑邊界；零點不可微，仍可使用次梯度；Notebook 導讀：懲罰、早停與評估範圍 |
| 05-07 / `c05-early-stop` | 17、18、43 | 早停：保留驗證表現最好的參數；早停需要「監看、耐心、保存、回復」；Notebook 導讀：懲罰、早停與評估範圍 |
| 05-08 / `fb8e534e` | 19、23、26、27、30、31 | Logistic：先算分數，再轉成正類機率；二元交叉熵：每筆損失與整體平均；Logistic 梯度：形式像殘差，但預測已轉機率；梯度下降：同樣的更新規則，不同的損失；Iris 案例：定義正類，才能解讀機率；一個特徵的機率曲線與 0.5 決策界線 |
| 05-09 / `c05-calculus` | 20、21、22、23、24、25、26、27、28、29、43 | Sigmoid 把任意實數映射到 0 與 1 之間；Sigmoid 的導數：外層與內層分開算；Bernoulli 概似：真實類別得到多少機率？；二元交叉熵：每筆損失與整體平均；交叉熵先對預測機率微分；連鎖律：機率梯度如何變成分數梯度？；Logistic 梯度：形式像殘差，但預測已轉機率；梯度下降：同樣的更新規則，不同的損失；手算 Logistic 的第一次更新；手算解答：損失下降，accuracy 可以不變；Notebook 導讀：懲罰、早停與評估範圍 |
| 05-10 / `412a71d5` | 33、40 | 機率不是最後決策：比較兩個閾值；把分數、機率、類別與評估分開 |
| 05-11 / `664040ba` | 32 | 兩個特徵的線性決策邊界 |
| 05-12 / `98328db0` | 35、36、37、38 | Softmax：每一類先得到自己的分數；穩定的 Softmax：先減掉最大分數；多類別交叉熵：看正確類別拿到多少機率；Softmax 的三類決策區域 |
| 05-13 / `e2bab0f2` | 39、41、42 | 用 Pipeline 選正則化強度；綜合實作：三類分類的完整流程；離堂檢核：梯度、決策與泛化 |

## 06｜決策樹與SVM補充

投影片 45 頁；Notebook 14 個程式格。

樹決策區域、迴歸樹節點、旋轉與穩定性、手刻 CART、SVM margin/hinge/kernel。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/11_tree_regularization.png` | 06-06 | 同程式輸出；`11_tree_regularization` |
| 4 從根節點走到葉節點：Iris 決策樹 | `assets/chapters04_09/book_fig_5_1.png` | 06-03 | 同概念重做；`11_iris_tree` |
| 6 樹把空間切成一塊一塊的區域 | `assets/chapters04_09/book_fig_5_2.png` | 06-08 | 同概念重做；`c06_tree_regions`、`c06_regression_nodes`、`c06_regression_regularization` |
| 22 正則化前後：彎月資料的邊界 | `assets/chapters04_09/book_fig_5_3.png` | 06-06 | 同概念重做；`11_tree_regularization` |
| 24 讀迴歸樹：追蹤規則與葉內平均 | `assets/chapters04_09/book_fig_5_4.png` | 06-08 | 同概念重做；`c06_tree_regions`、`c06_regression_nodes`、`c06_regression_regularization` |
| 26 增加深度：階梯更細，表達能力更強 | `assets/chapters04_09/book_fig_5_5.png` | 06-07 | 同概念重做；`11_regression_tree` |
| 27 迴歸樹也需要正則化 | `assets/chapters04_09/book_fig_5_6.png` | 06-08 | 同概念重做；`c06_tree_regions`、`c06_regression_nodes`、`c06_regression_regularization` |
| 30 座標軸方向會影響樹的複雜度 | `assets/chapters04_09/book_fig_5_7.png` | 06-10 | 同概念重做；`c06_rotation_stability` |
| 31 PCA 旋轉後，樹可能更容易分割 | `assets/chapters04_09/book_fig_5_8.png` | 06-10 | 同概念重做；`c06_rotation_stability` |
| 32 相同資料重訓，也可能得到不同的樹 | `assets/chapters04_09/book_fig_5_9.png` | 06-10 | 同概念重做；`c06_rotation_stability` |

本章 10 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 06-01 / `938a91c9` | 2 | 本週成果與三段安排 |
| 06-02 / `course06` | 2 | 本週成果與三段安排 |
| 06-03 / `8380145d` | 4、5、7、8、12 | 從根節點走到葉節點：Iris 決策樹；讀懂節點上的四種資訊；葉節點的機率來自到達此處的樣本；特徵型態與樹的資料準備；建立一棵可閱讀的樹 |
| 06-04 / `05e40a72` | 9、10、11 | Gini：隨機抽兩個標籤會多常不同？；Entropy：標籤越難猜，資訊量越大；手算：哪個節點比較純？ |
| 06-05 / `e54adfc6` | 14、15、18 | CART：挑選加權子節點不純度最小的分割；資訊增益與決策樹演算法；算一次分割，不能只比較左右平均 |
| 06-06 / `ae84951b` | 3、20、21、22 | 程式實驗與實際輸出；限制樹的成長：先控制葉節點有多少證據；其他停止條件與剪枝；正則化前後：彎月資料的邊界 |
| 06-07 / `49b5fc67` | 23、25、26、28 | 迴歸樹：葉節點改成輸出數值平均；CART 迴歸目標：比較子節點的加權 MSE；增加深度：階梯更細，表達能力更強；迴歸葉節點：為什麼預測平均值？ |
| 06-08 / `c06-tree-plots` | 6、24、27、45 | 樹把空間切成一塊一塊的區域；讀迴歸樹：追蹤規則與葉內平均；迴歸樹也需要正則化；Notebook 導讀：樹的幾何與 SVM 驗算 |
| 06-09 / `26a106c3` | 30、31、32 | 座標軸方向會影響樹的複雜度；PCA 旋轉後，樹可能更容易分割；相同資料重訓，也可能得到不同的樹 |
| 06-10 / `c06-rotation` | 30、31、32、45 | 座標軸方向會影響樹的複雜度；PCA 旋轉後，樹可能更容易分割；相同資料重訓，也可能得到不同的樹；Notebook 導讀：樹的幾何與 SVM 驗算 |
| 06-11 / `9861802f` | 33、34、38、39、41 | 補充 SVM：用間隔比較不同的分隔面；補充 SVM：軟間隔與 hinge loss；補充 SVM：核函數與 RBF 的 gamma；補充 SVM：多項式特徵與核技巧；選讀｜SVM 的次梯度與核參數實驗 |
| 06-12 / `edd63a11` | 40、42、43、44 | 補充 SVM：多類別與模型比較；三種分類模型的比較；比較實作：同一切分，兩種模型；離堂檢核與作業 |
| 06-13 / `c06-scratch` | 14、15、16、17、18、19、45 | CART：挑選加權子節點不純度最小的分割；資訊增益與決策樹演算法；訓練成本與預測成本；選讀｜手刻決策樹的遞迴流程；算一次分割，不能只比較左右平均；選讀｜原課程 80 筆資料的分割比較；Notebook 導讀：樹的幾何與 SVM 驗算 |
| 06-14 / `c06-svm-math` | 33、34、35、36、37、38、39、41、45 | 補充 SVM：用間隔比較不同的分隔面；補充 SVM：軟間隔與 hinge loss；補充 SVM：分對仍可能有損失；補充 SVM：原始問題與對偶的關係；選讀｜SVM 對偶如何得到預測函數；補充 SVM：核函數與 RBF 的 gamma；補充 SVM：多項式特徵與核技巧；選讀｜SVM 的次梯度與核參數實驗；Notebook 導讀：樹的幾何與 SVM 驗算 |

## 07｜集成學習與隨機森林

投影片 48 頁；Notebook 12 個程式格。

大數法則、bootstrap/OOB、AdaBoost 重加權、boosting 曲線、OOF 評估範圍。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/12_gradient_boosting_stages.png` | 07-09 | 同程式輸出；`12_gradient_boosting_stages` |
| 4 投票分類器：不同模型提供不同觀點 | `assets/chapters04_09/book_fig_6_1.png` | 07-03、07-05 | 同概念重做；`c07_large_numbers`、`c07_bootstrap_membership` |
| 5 硬投票：每個模型先投一個類別 | `assets/chapters04_09/book_fig_6_2.png` | 07-03 | 同概念重做；數值／表格／流程與形狀 |
| 7 大數法則的前提：錯誤不能完全同步 | `assets/chapters04_09/book_fig_6_3.png` | 07-05 | 同概念重做；`c07_large_numbers`、`c07_bootstrap_membership` |
| 10 Bagging：每個模型用不同抽樣資料訓練 | `assets/chapters04_09/book_fig_6_4.png` | 07-05、07-04 | 同概念重做；`c07_large_numbers`、`c07_bootstrap_membership`、`12_bagging_boundary` |
| 11 很多棵不同的樹，邊界通常更平滑 | `assets/chapters04_09/book_fig_6_5.png` | 07-04 | 同概念重做；`12_bagging_boundary` |
| 17 特徵重要度：哪些像素參與較多有效分割？ | `assets/chapters04_09/book_fig_6_6.png` | 07-06 | 同概念重做；`12_forest_importance` |
| 20 AdaBoost 的權重更新流程 | `assets/chapters04_09/book_fig_6_7.png` | 07-08 | 同概念重做；`c07_adaboost_weights` |
| 21 後續分類器更注意先前的難分樣本 | `assets/chapters04_09/book_fig_6_8.png` | 07-08 | 同概念重做；`c07_adaboost_weights` |
| 27 逐棵加入：左邊學殘差，右邊累加預測 | `assets/chapters04_09/book_fig_6_9.png` | 07-09 | 同概念重做；`12_gradient_boosting_stages` |
| 28 圖 6-9 放大：第 1 輪殘差與累加 | `assets/chapters04_09/book_fig_6_9_detail_1.png` | 07-09 | 同概念重做；`12_gradient_boosting_stages` |
| 29 圖 6-9 放大：第 2 輪殘差與累加 | `assets/chapters04_09/book_fig_6_9_detail_2.png` | 07-09 | 同概念重做；`12_gradient_boosting_stages` |
| 30 圖 6-9 放大：第 3 輪殘差與累加 | `assets/chapters04_09/book_fig_6_9_detail_3.png` | 07-09 | 同概念重做；`12_gradient_boosting_stages` |
| 31 學習率較小，通常需要更多棵樹 | `assets/chapters04_09/book_fig_6_10.png` | 07-12 | 同概念重做；`c07_boosting_rounds` |
| 36 Stacking：讓第二層模型學會如何組合 | `assets/chapters04_09/book_fig_6_11.png` | 07-10、07-12 | 機制／形狀對照；`c07_boosting_rounds` |
| 37 用折外預測建立第二層訓練資料 | `assets/chapters04_09/book_fig_6_12.png` | 07-10 | 機制／形狀對照；數值／表格／流程與形狀 |
| 38 多層 Stacking：多個 blender 還可再組合 | `assets/chapters04_09/book_fig_6_13.png` | 07-10、07-12 | 機制／形狀對照；`c07_boosting_rounds` |

本章 17 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 07-01 / `b9c05c42` | 2 | 本週節奏與成果 |
| 07-02 / `course07` | 2、17 | 本週節奏與成果；特徵重要度：哪些像素參與較多有效分割？ |
| 07-03 / `e3bc4d6e` | 4、5、6、8、9、41 | 投票分類器：不同模型提供不同觀點；硬投票：每個模型先投一個類別；軟投票：先平均機率，再選最大值；同樣三個模型，硬投票與軟投票會相同嗎？；投票分類器的機率條件；表 6-1：投票方法的適用條件與案例 |
| 07-04 / `34dcc9df` | 10、11、12、13、14、42 | Bagging：每個模型用不同抽樣資料訓練；很多棵不同的樹，邊界通常更平滑；袋外 OOB：這棵樹沒看過哪些樣本？；Bagging 與 OOB 的實作對照；資料與特徵，都可以隨機抽樣；表 6-1：抽樣集成的適用條件與案例 |
| 07-05 / `c07-sampling` | 4、5、7、10、12、14、48 | 投票分類器：不同模型提供不同觀點；硬投票：每個模型先投一個類別；大數法則的前提：錯誤不能完全同步；Bagging：每個模型用不同抽樣資料訓練；袋外 OOB：這棵樹沒看過哪些樣本？；資料與特徵，都可以隨機抽樣；Notebook 導讀：抽樣、加權與第二層評估 |
| 07-06 / `ceea9bae` | 15、16、17、43 | Random Forest 與 Extra Trees 的差別；森林的隨機性與重要度計算；特徵重要度：哪些像素參與較多有效分割？；表 6-1：隨機樹的適用條件與案例 |
| 07-07 / `e746c855` | 20、22、23、24、25 | AdaBoost 的權重更新流程；AdaBoost：加權錯誤率與模型權重；AdaBoost：更新樣本權重，再做加權投票；手算 AdaBoost 的第一輪；選讀｜手刻 AdaBoost 為何多了二分之一 |
| 07-08 / `c07-adaboost` | 20、21、22、23、25、48 | AdaBoost 的權重更新流程；後續分類器更注意先前的難分樣本；AdaBoost：加權錯誤率與模型權重；AdaBoost：更新樣本權重，再做加權投票；選讀｜手刻 AdaBoost 為何多了二分之一；Notebook 導讀：抽樣、加權與第二層評估 |
| 07-09 / `a36600ad` | 3、19、26、27、28、29、30、31、32、44 | 程式實驗與實際輸出；Boosting：新模型接著處理前面的不足；Gradient Boosting：平方損失時學殘差；逐棵加入：左邊學殘差，右邊累加預測；圖 6-9 放大：第 1 輪殘差與累加；圖 6-9 放大：第 2 輪殘差與累加；圖 6-9 放大：第 3 輪殘差與累加；學習率較小，通常需要更多棵樹；Boosting 的停止條件與隨機化；表 6-1：Boosting 的適用條件與案例 |
| 07-10 / `9104d3d3` | 36、37、38、39、40、45 | Stacking：讓第二層模型學會如何組合；用折外預測建立第二層訓練資料；多層 Stacking：多個 blender 還可再組合；Stacking 洩漏：看似完美的訓練特徵；Stacking 的訓練與推論介面；表 6-1：HGB 與 Stacking 的條件與案例 |
| 07-11 / `45a5232e` | 34、35、45、46、47 | Histogram Gradient Boosting：先把連續值分箱；GBRT 與 HGB 的參數不能直接互抄；表 6-1：HGB 與 Stacking 的條件與案例；綜合比較：單樹、森林與提升樹；離堂檢核：辨認三種「下一個模型」 |
| 07-12 / `c07-boosting-curve` | 31、32、34、35、36、37、38、40、48 | 學習率較小，通常需要更多棵樹；Boosting 的停止條件與隨機化；Histogram Gradient Boosting：先把連續值分箱；GBRT 與 HGB 的參數不能直接互抄；Stacking：讓第二層模型學會如何組合；用折外預測建立第二層訓練資料；多層 Stacking：多個 blender 還可再組合；Stacking 的訓練與推論介面；Notebook 導讀：抽樣、加權與第二層評估 |

## 08｜降維與資料表示

投影片 45 頁；Notebook 12 個程式格。

邊界體積、平面投影、SVD/IPCA、LLE 權重、多法降維與 JL 平方距離。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/13_pca_reconstruction.png` | 08-06 | 同程式輸出；`13_pca_scree`、`13_pca_reconstruction` |
| 4 維度增加：大部分空間可能靠近邊界 | `assets/chapters04_09/book_fig_7_1.png` | 08-10 | 同概念重做；`c08_boundary_volume`、`c08_pca_projection`、`c08_projection_variance`、`c08_manifold_boundary` |
| 7 投影：資料是否接近某個低維子空間？ | `assets/chapters04_09/book_fig_7_2.png` | 08-10 | 同概念重做；`c08_boundary_volume`、`c08_pca_projection`、`c08_projection_variance`、`c08_manifold_boundary` |
| 8 在投影平面建立新的座標 | `assets/chapters04_09/book_fig_7_3.png` | 08-10 | 同概念重做；`c08_boundary_volume`、`c08_pca_projection`、`c08_projection_variance`、`c08_manifold_boundary` |
| 9 Swiss roll：彎曲流形無法靠平面直接攤開 | `assets/chapters04_09/book_fig_7_4.png` | 08-10 | 同概念重做；`c08_boundary_volume`、`c08_pca_projection`、`c08_projection_variance`、`c08_manifold_boundary` |
| 10 攤開流形：保留局部鄰近關係 | `assets/chapters04_09/book_fig_7_5.png` | 08-10、08-08 | 同概念重做；`c08_boundary_volume`、`c08_pca_projection`、`c08_projection_variance`、`c08_manifold_boundary`、`13_swiss_roll` |
| 11 降維之後，分類邊界不一定更簡單 | `assets/chapters04_09/book_fig_7_6.png` | 08-10 | 同概念重做；`c08_boundary_volume`、`c08_pca_projection`、`c08_projection_variance`、`c08_manifold_boundary` |
| 12 PCA：選擇投影後變異最大的方向 | `assets/chapters04_09/book_fig_7_7.png` | 08-10 | 同概念重做；`c08_boundary_volume`、`c08_pca_projection`、`c08_projection_variance`、`c08_manifold_boundary` |
| 23 用累積曲線選 d：壓縮與保真之間的折衷 | `assets/chapters04_09/book_fig_7_8.png` | 08-06 | 同概念重做；`13_pca_scree`、`13_pca_reconstruction` |
| 26 圖像壓縮：重建仍像數字，但細節已減少 | `assets/chapters04_09/book_fig_7_9.png` | 08-06 | 同概念重做；`13_pca_scree`、`13_pca_reconstruction` |
| 35 LLE：用鄰居重建每個點，再保持重建關係 | `assets/chapters04_09/book_fig_7_10.png` | 08-08、08-12 | 同概念重做；`13_swiss_roll`、`c08_embedding_comparison` |
| 38 同一資料用不同降維方法，圖形可能很不同 | `assets/chapters04_09/book_fig_7_11.png` | 08-12 | 同概念重做；`c08_embedding_comparison` |

本章 12 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 08-01 / `68e39996` | 2 | 本週成果與三段安排 |
| 08-02 / `course08` | 2 | 本週成果與三段安排 |
| 08-03 / `a4b045f4` | 4、5、6 | 維度增加：大部分空間可能靠近邊界；維度災難帶來三個問題；高維空間靠近邊界的機率 |
| 08-04 / `d24b56b3` | 13、14、16、17、18、19、20 | PCA 的兩個等價觀點；先猜方向，再計算；PCA 的 SVD 寫法與矩陣形狀；從共變異矩陣推導第一主成分；共變異特徵值與奇異值的關係；手算例：同一條線的共變異矩陣；選讀｜手刻 PCA 與函式庫的比較 |
| 08-05 / `23ff80da` | 22、30 | 解釋變異比例與保留維度；實作：壓縮率與辨識品質是否一起變好？ |
| 08-06 / `d7f93d4b` | 3、23、24、25、26 | 程式實驗與實際輸出；用累積曲線選 d：壓縮與保真之間的折衷；PCA 程式：先切分，再學投影；逆投影：重建時要把平均值加回去；圖像壓縮：重建仍像數字，但細節已減少 |
| 08-07 / `442d0dcf` | 29、30、43、44 | PCA 維度與分類器一起驗證；實作：壓縮率與辨識品質是否一起變好？；PCA、LLE 與 t-SNE 的實驗安排；離堂檢核與作業 |
| 08-08 / `d835e611` | 9、10、35、43 | Swiss roll：彎曲流形無法靠平面直接攤開；攤開流形：保留局部鄰近關係；LLE：用鄰居重建每個點，再保持重建關係；PCA、LLE 與 t-SNE 的實驗安排 |
| 08-09 / `f8f3e6d1` | 32、33、34 | 隨機投影：不用先找到主方向；Johnson–Lindenstrauss 維度界線；稀疏隨機投影：大部分矩陣元素為零 |
| 08-10 / `c08-projection` | 4、6、7、8、9、10、11、12、13、45 | 維度增加：大部分空間可能靠近邊界；高維空間靠近邊界的機率；投影：資料是否接近某個低維子空間？；在投影平面建立新的座標；Swiss roll：彎曲流形無法靠平面直接攤開；攤開流形：保留局部鄰近關係；降維之後，分類邊界不一定更簡單；PCA：選擇投影後變異最大的方向；PCA 的兩個等價觀點；Notebook 導讀：降維圖與數值怎麼核對 |
| 08-11 / `c08-svd` | 16、18、20、21、27、28、32、33、34、45 | PCA 的 SVD 寫法與矩陣形狀；共變異特徵值與奇異值的關係；選讀｜手刻 PCA 與函式庫的比較；選讀｜原課程的 3×2 矩陣 SVD 手算；PCA 的計算選項；選讀｜分批 PCA 的訓練與固定投影；隨機投影：不用先找到主方向；Johnson–Lindenstrauss 維度界線；稀疏隨機投影：大部分矩陣元素為零；Notebook 導讀：降維圖與數值怎麼核對 |
| 08-12 / `c08-manifold-methods` | 35、36、37、38、39、40、41、42、43、45 | LLE：用鄰居重建每個點，再保持重建關係；LLE 第一步：找到局部重建權重；LLE 第二步：保持權重，移動低維座標；同一資料用不同降維方法，圖形可能很不同；其他方法與解讀界線；LDA：使用標籤選擇投影方向；補充 t-SNE：相似度不是原始距離的等比例縮圖；選讀｜t-SNE 相似度與困惑度；PCA、LLE 與 t-SNE 的實驗安排；Notebook 導讀：降維圖與數值怎麼核對 |

## 09｜分群與表示應用

投影片 40 頁；Notebook 11 個程式格。

Lloyd 迭代、初始化與 k、逐群輪廓、代表數字、部分傳播與標註需求。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/14_kmeans_selection.png` | 09-05 | 同程式輸出；`14_kmeans_selection` |
| 4 沒有標籤時，資料自己呈現什麼結構？ | `assets/chapters04_09/book_fig_8_1.png` | 09-09 | 同概念重做；`c09_iris_unlabeled`、`c09_lloyd_iterations`、`c09_initialization_and_k` |
| 6 K-means：把點指派給最近的中心 | `assets/chapters04_09/book_fig_8_2.png` | 09-04 | 同概念重做；`14_kmeans_voronoi` |
| 7 最近中心形成 Voronoi 分區 | `assets/chapters04_09/book_fig_8_3.png` | 09-04 | 同概念重做；`14_kmeans_voronoi` |
| 10 觀察迭代：中心移動，群邊界跟著改變 | `assets/chapters04_09/book_fig_8_4.png` | 09-09 | 同概念重做；`c09_iris_unlabeled`、`c09_lloyd_iterations`、`c09_initialization_and_k` |
| 15 不同初始化，可能得到不同局部解 | `assets/chapters04_09/book_fig_8_5.png` | 09-09 | 同概念重做；`c09_iris_unlabeled`、`c09_lloyd_iterations`、`c09_initialization_and_k` |
| 19 k 選錯：可能切碎一群，或合併不同群 | `assets/chapters04_09/book_fig_8_6.png` | 09-09 | 同概念重做；`c09_iris_unlabeled`、`c09_lloyd_iterations`、`c09_initialization_and_k` |
| 20 肘部法：找 inertia 改善開始遞減的位置 | `assets/chapters04_09/book_fig_8_7.png` | 09-05 | 同概念重做；`14_kmeans_selection` |
| 21 平均輪廓分數：把群內與群外距離一起比較 | `assets/chapters04_09/book_fig_8_8.png` | 09-05 | 同概念重做；`14_kmeans_selection` |
| 23 輪廓圖：不要只看整體平均 | `assets/chapters04_09/book_fig_8_9.png` | 09-10 | 同概念重做；`c09_silhouette_profiles` |
| 25 K-means 的限制：橢圓、密度與群大小差異 | `assets/chapters04_09/book_fig_8_10.png` | 09-06 | 同概念重做；`14_kmeans_limits` |
| 28 用 K-means 做顏色量化與影像分割 | `assets/chapters04_09/book_fig_8_11.png` | 09-07 | 同概念重做；`14_color_quantization` |
| 33 代表樣本：每群挑一張最接近中心的圖 | `assets/chapters04_09/book_fig_8_12.png` | 09-11 | 同概念重做；`c09_representative_digits` |

本章 13 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 09-01 / `86c4c60f` | 2 | 本週成果與節奏 |
| 09-02 / `course09` | 2 | 本週成果與節奏 |
| 09-03 / `eb9b76db` | 8、9、11、12 | 目標函數：最小化群內平方距離；兩步交替：指派與更新；手算一維 K-means 的兩步；群編號沒有天然大小與固定語義 |
| 09-04 / `393ea5d7` | 6、7、15、16 | K-means：把點指派給最近的中心；最近中心形成 Voronoi 分區；不同初始化，可能得到不同局部解；K-means++ 與多次初始化 |
| 09-05 / `bf12b6a5` | 3、19、20、21、22、24 | 程式實驗與實際輸出；k 選錯：可能切碎一群，或合併不同群；肘部法：找 inertia 改善開始遞減的位置；平均輪廓分數：把群內與群外距離一起比較；輪廓係數：群內近，群外遠；手算輪廓係數，並質疑平均值 |
| 09-06 / `c894fd34` | 25、26 | K-means 的限制：橢圓、密度與群大小差異；縮放之前，先定義什麼叫「相似」 |
| 09-07 / `482e4bf0` | 5、28、29、30 | 分群可用於哪些任務？；用 K-means 做顏色量化與影像分割；顏色、語意與實例分割；影像轉換的陣列形狀 |
| 09-08 / `51e0164b` | 32、34、35、36、38、39 | 只有 50 個標籤：先標哪些資料？；代表樣本與標籤傳播的陣列操作；教材少量標註實驗：每一步改變了什麼？；標籤傳播需要「群內標籤一致」的假設；實作與報告：群數不是一個神奇答案；離堂檢核與下週預告 |
| 09-09 / `c09-iterations` | 4、6、7、8、9、10、12、13、15、16、17、18、19、40 | 沒有標籤時，資料自己呈現什麼結構？；K-means：把點指派給最近的中心；最近中心形成 Voronoi 分區；目標函數：最小化群內平方距離；兩步交替：指派與更新；觀察迭代：中心移動，群邊界跟著改變；群編號沒有天然大小與固定語義；K-means 的群號、距離與分數；不同初始化，可能得到不同局部解；K-means++ 與多次初始化；K-means++ 的抽樣機率；加速方式：避開多餘距離，或改用小批次；k 選錯：可能切碎一群，或合併不同群；Notebook 導讀：從群中心走到標註策略 |
| 09-10 / `c09-silhouette` | 21、22、23、24、26、40 | 平均輪廓分數：把群內與群外距離一起比較；輪廓係數：群內近，群外遠；輪廓圖：不要只看整體平均；手算輪廓係數，並質疑平均值；縮放之前，先定義什麼叫「相似」；Notebook 導讀：從群中心走到標註策略 |
| 09-11 / `c09-representatives` | 5、31、32、33、34、35、36、37、38、40 | 分群可用於哪些任務？；把距離轉成新的特徵表示；只有 50 個標籤：先標哪些資料？；代表樣本：每群挑一張最接近中心的圖；代表樣本與標籤傳播的陣列操作；教材少量標註實驗：每一步改變了什麼？；標籤傳播需要「群內標籤一致」的假設；主動學習：讓模型提出下一筆標註需求；實作與報告：群數不是一個神奇答案；Notebook 導讀：從群中心走到標註策略 |

## 10｜密度分群與機率模型

投影片 44 頁；Notebook 13 個程式格。

DBSCAN 延伸、共變異形狀、穩定 EM、似然/MAP、階層樹與異常評估切分。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/15_gmm_ellipses.png` | 10-06 | 同程式輸出；`15_gmm_ellipses` |
| 6 改變 eps：同一資料會從破碎變成連續 | `assets/chapters04_09/book_fig_8_13.png` | 10-03 | 同概念重做；`15_dbscan_eps` |
| 10 新點的延伸分類：距離過遠應拒絕 | `assets/chapters04_09/book_fig_8_14.png` | 10-11 | 同概念重做；`c10_dbscan_extension`、`c10_covariance_shapes`、`c10_information_criteria`、`c10_moons_components` |
| 18 GMM 同時給群邊界與密度等高線 | `assets/chapters04_09/book_fig_8_15.png` | 10-06 | 同概念重做；`15_gmm_ellipses` |
| 26 tied 與 spherical：限制形狀會改變結果 | `assets/chapters04_09/book_fig_8_16.png` | 10-11 | 同概念重做；`c10_dbscan_extension`、`c10_covariance_shapes`、`c10_information_criteria`、`c10_moons_components` |
| 29 低密度異常：先估分數，再選閾值 | `assets/chapters04_09/book_fig_8_17.png` | 10-09 | 同概念重做；`15_gmm_anomaly` |
| 32 Likelihood：固定資料，比較不同參數 | `assets/chapters04_09/book_fig_8_18.png` | 10-12 | 同概念重做；`c10_em_convergence`、`c10_density_vs_likelihood` |
| 37 同時搜尋成分數與共變異假設 | `assets/chapters04_09/book_fig_8_19.png` | 10-11 | 同概念重做；`c10_dbscan_extension`、`c10_covariance_shapes`、`c10_information_criteria`、`c10_moons_components` |
| 39 彎月資料：多個高斯也可能切出很多小橢圓 | `assets/chapters04_09/book_fig_8_20.png` | 10-11 | 同概念重做；`c10_dbscan_extension`、`c10_covariance_shapes`、`c10_information_criteria`、`c10_moons_components` |

本章 9 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 10-01 / `bdecfc66` | 2 | 本週成果與三段安排 |
| 10-02 / `course10` | 2 | 本週成果與三段安排 |
| 10-03 / `a598df10` | 4、5、6、7 | DBSCAN：密集區域透過核心點連成一群；DBSCAN 的擴張與邊界點；改變 eps：同一資料會從破碎變成連續；讀取 DBSCAN 結果 |
| 10-04 / `289cdaff` | 8 | 手算鄰域：誰是核心，誰是雜訊？ |
| 10-05 / `0e919912` | 9、10 | DBSCAN 沒有原生 predict，延伸要另訂規則；新點的延伸分類：距離過遠應拒絕 |
| 10-06 / `236d0bb6` | 3、16、17、18、23 | 程式實驗與實際輸出；GMM：先選一個成分，再從該高斯分布取樣；多變量高斯：平均與共變異各控制什麼？；GMM 同時給群邊界與密度等高線；收斂不等於找到全域最優 |
| 10-07 / `caf21d52` | 19、20、21、22 | EM 的 E-step：每個成分分擔多少責任？；EM 的 M-step：用責任值重新估計參數；K-means 與 GMM 的更新差異；手算軟指派與更新 |
| 10-08 / `eff182a7` | 25、26、35 | 限制共變異：容量與成本的折衷；tied 與 spherical：限制形狀會改變結果；GMM 的自由參數如何計數 |
| 10-09 / `3f07a219` | 29、30、31、34、36、37 | 低密度異常：先估分數，再選閾值；異常閾值如何決定？；離群偵測與新穎偵測的資料假設；AIC 與 BIC：擬合收益要付出複雜度代價；數例：比較兩個 GMM 的複雜度代價；同時搜尋成分數與共變異假設 |
| 10-10 / `11f94289` | 41、42、43 | 用重建誤差找異常：接回上一週的 PCA；選模工作單：形狀、機率與用途一起決定；離堂檢核與作業 |
| 10-11 / `c10-density-views` | 9、10、25、26、34、35、37、38、39、44 | DBSCAN 沒有原生 predict，延伸要另訂規則；新點的延伸分類：距離過遠應拒絕；限制共變異：容量與成本的折衷；tied 與 spherical：限制形狀會改變結果；AIC 與 BIC：擬合收益要付出複雜度代價；GMM 的自由參數如何計數；同時搜尋成分數與共變異假設；Bayesian GMM：給成分上限，讓權重收縮；彎月資料：多個高斯也可能切出很多小橢圓；Notebook 導讀：生成、選模與異常分數 |
| 10-12 / `c10-em-likelihood` | 16、17、19、20、21、22、23、24、28、32、33、44 | GMM：先選一個成分，再從該高斯分布取樣；多變量高斯：平均與共變異各控制什麼？；EM 的 E-step：每個成分分擔多少責任？；EM 的 M-step：用責任值重新估計參數；K-means 與 GMM 的更新差異；手算軟指派與更新；收斂不等於找到全域最優；選讀｜手刻 EM 的數值穩定性；機率、密度與生成：三個 API 回答不同問題；Likelihood：固定資料，比較不同參數；最大似然與 MAP：從乘積改成對數和；Notebook 導讀：生成、選模與異常分數 |
| 10-13 / `c10-other-clusters` | 11、12、13、14、30、31、40、41、42、44 | 密度與階層方法：結構假設不同；階層式分群補充：連結方式決定合併順序；樹狀圖的合併高度與切群；Mean-shift、代表點與相似圖分群；異常閾值如何決定？；離群偵測與新穎偵測的資料假設；異常與新穎偵測方法概覽；用重建誤差找異常：接回上一週的 PCA；選模工作單：形狀、機率與用途一起決定；Notebook 導讀：生成、選模與異常分數 |

## 11｜人工神經網路入門

投影片 53 頁；Notebook 12 個程式格。

神經元與 XOR 架構、Softmax/MLP 梯度、迴歸散點、digits 錯誤與訓練控制。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/16_tiny_mlp_training.png` | 11-08 | 同程式輸出；`16_tiny_mlp_training` |
| 5 從生物神經元得到啟發 | `assets/chapters04_09/book_fig_9_1.png` | 11-10 | 背景類比／計算單元對照；`c11_xor_network` |
| 6 很多單元組合，形成更複雜的處理 | `assets/chapters04_09/book_fig_9_2.png` | 11-10 | 背景類比／計算單元對照；`c11_xor_network` |
| 7 人工神經元可組合簡單邏輯 | `assets/chapters04_09/book_fig_9_3.png` | 11-10 | 同概念重做；`c11_xor_network` |
| 8 TLU：加權和，加偏置，再套階躍函數 | `assets/chapters04_09/book_fig_9_4.png` | 11-03、11-10 | 同概念重做；`16_perceptron`、`c11_xor_network` |
| 10 Perceptron 層：每個輸出都看所有輸入 | `assets/chapters04_09/book_fig_9_5.png` | 11-10 | 機制／形狀對照；`c11_xor_network` |
| 13 XOR：一條線不夠，但組合多個單元可以 | `assets/chapters04_09/book_fig_9_6.png` | 11-04、11-10 | 同概念重做；`c11_xor_network` |
| 16 MLP：輸入、隱藏層與輸出層 | `assets/chapters04_09/book_fig_9_7.png` | 11-07、11-08 | 機制／形狀對照；`16_tiny_mlp_training` |
| 19 Sigmoid、tanh、ReLU 與它們的導數 | `assets/chapters04_09/book_fig_9_8.png` | 11-05 | 同概念重做；`16_activations` |
| 33 MLP 迴歸：預測與真值散點 | `assets/chapters04_09/book_fig_9_9.png` | 11-12 | 同概念重做；`c11_regression_predictions`、`c11_digit_errors`、`c11_lr_probe` |
| 36 分類 MLP：隱藏層 ReLU，輸出層 Softmax | `assets/chapters04_09/book_fig_9_10.png` | 11-08、11-09、11-11 | 機制／形狀對照；`16_tiny_mlp_training`、`c11_smooth_activations` |
| 39 Fashion MNIST：由像素到服飾類別 | `assets/chapters04_09/book_fig_9_11.png` | 11-12 | 機制／形狀對照；`c11_regression_predictions`、`c11_digit_errors`、`c11_lr_probe` |

本章 12 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 11-01 / `4ace4586` | 2 | 本週成果與節奏 |
| 11-02 / `course11` | 2 | 本週成果與節奏 |
| 11-03 / `54a6bbf3` | 8、9、11、12 | TLU：加權和，加偏置，再套階躍函數；階躍函數與單層輸出；Perceptron 學習規則：答錯才修正；Perceptron 的學習限制 |
| 11-04 / `c6308b34` | 7、13、14、15 | 人工神經元可組合簡單邏輯；XOR：一條線不夠，但組合多個單元可以；XOR 真值表：把每一列實際走過網路；手算 XOR 網路的四組輸入 |
| 11-05 / `84f36656` | 19、20、21、22 | Sigmoid、tanh、ReLU 與它們的導數；激活函數：用公式連結曲線與梯度；選讀｜Leaky ReLU、ELU 與平滑激活；選讀｜Swish 與 Mish 的門控形式 |
| 11-06 / `13343146` | 23、24、25、26 | 一次訓練步驟要分清楚四件事；鏈式法則：沿路相乘，分支相加；手算範例：一個 Sigmoid 神經元；接續手算：把梯度傳給權重與偏置 |
| 11-07 / `0fd73a4c` | 10、16、27、46 | Perceptron 層：每個輸出都看所有輸入；MLP：輸入、隱藏層與輸出層；多層網路的形狀與反向遞迴；學習率、批次與參數量的調整 |
| 11-08 / `28390271` | 3、27、28、29、38、40、41、42 | 程式實驗與實際輸出；多層網路的形狀與反向遞迴；梯度消失與梯度爆炸；初始化：打破隱藏神經元的對稱；選讀｜原 MNIST 手刻網路的損失配對；分類 MLP 的訓練與預測流程；訓練損失、驗證分數與測試指標不能混用；Epoch、批次與早停的資料角色 |
| 11-09 / `7c0cb784` | 31、32、34、35、36、40、43、44、45、46、51、52 | 表 9-1：迴歸 MLP 的典型架構（1/2）；表 9-1：輸出範圍與損失（2/2）；用 scikit-learn 建立小型迴歸 MLP；表 9-2：分類的輸出層與損失；分類 MLP：隱藏層 ReLU，輸出層 Softmax；分類 MLP 的訓練與預測流程；教材案例提醒：高信心可能仍然答錯；調參次序：先讓模型學得動，再增加容量；深度、寬度與遷移學習；學習率、批次與參數量的調整；綜合實作：小型 MLP 與簡單模型比較；離堂檢核：把八週串回同一個學習流程 |
| 11-10 / `c11-neuron-geometry` | 5、6、7、8、9、10、13、14、15、16、18、53 | 從生物神經元得到啟發；很多單元組合，形成更複雜的處理；人工神經元可組合簡單邏輯；TLU：加權和，加偏置，再套階躍函數；階躍函數與單層輸出；Perceptron 層：每個輸出都看所有輸入；XOR：一條線不夠，但組合多個單元可以；XOR 真值表：把每一列實際走過網路；手算 XOR 網路的四組輸入；MLP：輸入、隱藏層與輸出層；沒有非線性，堆再多層也會折成一層；Notebook 導讀：架構、梯度與成效分開檢查 |
| 11-11 / `c11-calculus` | 20、21、22、23、24、27、35、36、37、38、53 | 激活函數：用公式連結曲線與梯度；選讀｜Leaky ReLU、ELU 與平滑激活；選讀｜Swish 與 Mish 的門控形式；一次訓練步驟要分清楚四件事；鏈式法則：沿路相乘，分支相加；多層網路的形狀與反向遞迴；表 9-2：分類的輸出層與損失；分類 MLP：隱藏層 ReLU，輸出層 Softmax；Softmax 與交叉熵的輸出梯度；選讀｜原 MNIST 手刻網路的損失配對；Notebook 導讀：架構、梯度與成效分開檢查 |
| 11-12 / `c11-predictions-controls` | 31、32、33、34、39、40、41、42、43、47、48、49、50、51、53 | 表 9-1：迴歸 MLP 的典型架構（1/2）；表 9-1：輸出範圍與損失（2/2）；MLP 迴歸：預測與真值散點；用 scikit-learn 建立小型迴歸 MLP；Fashion MNIST：由像素到服飾類別；分類 MLP 的訓練與預測流程；訓練損失、驗證分數與測試指標不能混用；Epoch、批次與早停的資料角色；教材案例提醒：高信心可能仍然答錯；選讀｜學習率範圍測試；選讀｜Dropout 的訓練與推論；選讀｜訓練紀錄、早停與模型回復；選讀｜Keras 舊案例與後續 PyTorch 的銜接；綜合實作：小型 MLP 與簡單模型比較；Notebook 導讀：架構、梯度與成效分開檢查 |

## 12｜深層神經網路訓練_梯度與遷移

投影片 50 頁；Notebook 7 個程式格。

激活/初始化、BN/LN、凍結/解凍、線性預訓練與圖片描述介面。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/12_gradient_transfer_demo.png` | 12-04 | 同程式輸出；`12_gradient_transfer_demo` |
| 13 圖 11-1：Sigmoid 飽和與小梯度 | `assets/chapter11/book_fig_11_1.png` | 12-05 | 同概念重做；`c12_activation_family`、`c12_initialization_signal` |
| 20 圖 11-2：Leaky ReLU 保留負半軸斜率 | `assets/chapter11/book_fig_11_2.png` | 12-05 | 同概念重做；`c12_activation_family`、`c12_initialization_signal` |
| 22 圖 11-3：ELU 與 SELU | `assets/chapter11/book_fig_11_3.png` | 12-05 | 同概念重做；`c12_activation_family`、`c12_initialization_signal` |
| 24 圖 11-4：平滑激活函數的差異 | `assets/chapter11/book_fig_11_4.png` | 12-05 | 同概念重做；`c12_activation_family`、`c12_initialization_signal` |
| 39 圖 11-5：重用已學到的特徵 | `assets/chapter11/book_fig_11_5.png` | 12-07 | 機制／參數更新對照；`c12_transfer_training` |
| 45 舊稿補充：圖片描述的預訓練 Encoder | `assets/chapter11/ppt_caption_example.png` | 12-07 | 機制／形狀對照；`c12_transfer_training` |
| 46 圖 11-6：無監督預訓練的想法 | `assets/chapter11/book_fig_11_6.png` | 12-07 | 機制／線性預訓練對照；`c12_transfer_training` |

本章 8 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 12-01 / `6b0fba04` | 2 | 本次成果與節奏 |
| 12-02 / `course12` | 2 | 本次成果與節奏 |
| 12-03 / `1bdd0437` | 12、14、37、38 | 深層網路的四個訓練困難；梯度為何會消失或爆炸？；梯度裁剪：限制一次更新的梯度；梯度裁剪放在 backward 與 step 之間 |
| 12-04 / `1bc915d2` | 3、14 | 程式實驗與實際輸出；梯度為何會消失或爆炸？ |
| 12-05 / `c12-activations-init` | 13、15、16、17、18、20、21、22、23、24、25、26、27、50 | 圖 11-1：Sigmoid 飽和與小梯度；表 11-1：初始化尺度與激活函數；初始化手算：100 個輸入、50 個輸出；PyTorch：隱藏層與輸出層分開初始化；選讀｜手刻 MLP 的初始化尺度；圖 11-2：Leaky ReLU 保留負半軸斜率；ReLU 變體與初始化配對；圖 11-3：ELU 與 SELU；SELU 自我正規化的條件；圖 11-4：平滑激活函數的差異；GELU、SiLU、Mish 與 ReLU²；選讀｜激活函數：把公式對到原始碼；選讀｜SwiGLU 的形狀與門控；Notebook 導讀：可執行的機制與驗收 |
| 12-06 / `c12-norm` | 28、29、30、31、32、33、34、35、50 | BatchNorm：先算批次統計，再學尺度；BatchNorm 手算：四筆資料的一個特徵；BatchNorm 的訓練與推論；PyTorch：Linear、BatchNorm、ReLU；BN 的統計軸：向量與影像；LayerNorm：每筆資料自己算統計；LayerNorm 手算：一筆資料的四個特徵；BatchNorm 與 LayerNorm 比較；Notebook 導讀：可執行的機制與驗收 |
| 12-07 / `c12-transfer` | 5、6、7、8、9、10、11、37、38、39、40、41、42、43、44、45、46、47、48、49、50 | PyTorch 銜接：資料形狀與角色；PyTorch 銜接：最小分類模型；選讀｜Keras 舊例：輸出與損失要一起看；PyTorch 銜接：一次批次更新；PyTorch 銜接：驗證與訓練模式；讀碼檢核：哪一步需要修正？；選讀｜手刻 MLP：前向、反向與參數更新；梯度裁剪：限制一次更新的梯度；梯度裁剪放在 backward 與 step 之間；圖 11-5：重用已學到的特徵；遷移學習：凍結與解凍的順序；書中範例：Fashion MNIST 的任務 A 與 B；PyTorch：複製骨幹，先只訓練新頭；PyTorch：解凍後建立分組學習率；書中成效：為何 92.5% 不能直接當保證？；舊稿補充：圖片描述的預訓練 Encoder；圖 11-6：無監督預訓練的想法；輔助任務與自監督預訓練；小組設計：只有少量服飾標註時；離堂檢核：方法與問題要配對；Notebook 導讀：可執行的機制與驗收 |

## 13｜深層神經網路訓練_最佳化與正則化

投影片 53 頁；Notebook 7 個程式格。

六種最佳化器、排程、Dropout/MC、Max-norm、早停與 CSV 記錄。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/13_optimizer_regularization_demo.png` | 13-04 | 同程式輸出；`13_optimizer_regularization_demo` |
| 7 圖 11-7：Nesterov 提前看動量方向 | `assets/chapter11/book_fig_11_7.png` | 13-05 | 同概念重做；`c13_optimizer_paths` |
| 9 圖 11-8：AdaGrad 對各方向調整步幅 | `assets/chapter11/book_fig_11_8.png` | 13-05 | 同概念重做；`c13_optimizer_paths` |
| 21 圖 11-9：固定學習率的取捨 | `assets/chapter11/book_fig_11_9.png` | 13-06 | 同概念重做；`c13_lr_schedules`、`c13_fixed_lr` |
| 23 圖 11-10：餘弦退火 | `assets/chapter11/book_fig_11_10.png` | 13-06 | 同概念重做；`c13_lr_schedules`、`c13_fixed_lr` |
| 26 圖 11-11：餘弦退火與暖重啟 | `assets/chapter11/book_fig_11_11.png` | 13-06 | 同概念重做；`c13_lr_schedules`、`c13_fixed_lr` |
| 38 圖 11-12：Dropout 的隨機遮罩 | `assets/chapter11/book_fig_11_12.png` | 13-07 | 同概念重做；`c13_dropout_mc`、`c13_early_stopping` |

本章 7 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 13-01 / `491f56ec` | 2 | 本次成果與節奏 |
| 13-02 / `course13` | 2 | 本次成果與節奏 |
| 13-03 / `77f72bd2` | 4、5、6 | 梯度、最佳化器與排程的分工；Momentum：累積前幾步的方向；Momentum 手算：連續兩次相同梯度 |
| 13-04 / `f6f60d5a` | 3、5 | 程式實驗與實際輸出；Momentum：累積前幾步的方向 |
| 13-05 / `c13-optimizers` | 4、5、6、7、8、9、10、11、12、13、14、16、17、18、19、20、33、34、53 | 梯度、最佳化器與排程的分工；Momentum：累積前幾步的方向；Momentum 手算：連續兩次相同梯度；圖 11-7：Nesterov 提前看動量方向；Nesterov 的更新式與 PyTorch；圖 11-8：AdaGrad 對各方向調整步幅；AdaGrad：累積梯度平方；RMSProp：保留較近的梯度尺度；Adam：一階矩與二階原點矩；Adam：偏差修正與更新；Adam 手算：第一步為何需要修正？；Adam 的變體：改動了哪個部分？；AdamW：分開處理權重衰減；表 11-2：最佳化器比較（1/2）；表 11-2：最佳化器比較（2/2）；選讀｜二階資訊與稀疏模型；L1、L2 與手動加入懲罰；AdamW 分組：只衰減本例的線性權重；Notebook 導讀：可執行的機制與驗收 |
| 13-06 / `c13-schedules` | 21、22、23、24、25、26、27、28、29、30、53 | 圖 11-9：固定學習率的取捨；指數衰減：每輪乘上一個比例；圖 11-10：餘弦退火；依表現降學習率：ReduceLROnPlateau；Warmup：開始幾輪逐步提高學習率；圖 11-11：餘弦退火與暖重啟；1cycle：在訓練預算內先升後降；Scheduler 呼叫時機總表；選讀｜舊 mini-batch 範例的排程計數；診斷活動：排程為什麼失去作用？；Notebook 導讀：可執行的機制與驗收 |
| 13-07 / `c13-regularization` | 32、33、34、35、36、37、38、39、40、41、42、43、44、45、46、47、48、49、53 | 正則化：用驗證集判斷是否改善泛化；L1、L2 與手動加入懲罰；AdamW 分組：只衰減本例的線性權重；早停與最佳參數回復；選讀｜原早停範例：保存後要回復哪一版？；選讀｜Keras callback：停止與回復最佳權重；圖 11-12：Dropout 的隨機遮罩；Dropout 手算：為什麼要除以保留率？；PyTorch：Dropout 與評估公平性；MC Dropout：保留遮罩，多次預測；選讀｜MC Dropout 只打開需要的層；Max-norm：限制每個神經元的權重範數；選讀｜只對 Linear 權重施加 Max-norm；舊稿補充：資料擴增要保留標籤意義；表 11-3：深層網路的起始設定；綜合實驗：每次只回答一個比較問題；實驗提交與離線替代；選讀｜原 Keras 的 TensorBoard 訓練紀錄；Notebook 導讀：可執行的機制與驗收 |

## 14｜卷積神經網路_影像特徵與架構

投影片 38 頁；Notebook 7 個程式格。

NCHW 卷積、padding/pooling、Inception/Residual/Depthwise/SE 前向與增強。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/14_convolution_demo.png` | 14-04 | 同程式輸出；`14_convolution_demo` |
| 7 局部感受野 | `assets/chapters12_19/book_fig_12_2.png` | 14-05 | 同概念重做；`c14_feature_maps`、`c14_padding` |
| 9 濾波器與特徵圖 | `assets/chapters12_19/book_fig_12_5.png` | 14-05 | 同概念重做；`c14_feature_maps`、`c14_padding` |
| 12 Padding 保留邊界附近的資訊 | `assets/chapters12_19/book_fig_12_3.png` | 14-05 | 同概念重做；`c14_feature_maps`、`c14_padding` |
| 14 多個通道如何合成輸出 | `assets/chapters12_19/book_fig_12_6.png` | 14-05 | 同概念重做；`c14_feature_maps`、`c14_padding` |
| 17 Max pooling | `assets/chapters12_19/book_fig_12_9.png` | 14-03、14-05 | 同概念重做；`c14_feature_maps`、`c14_padding` |
| 20 分類 CNN 的典型組成 | `assets/chapters12_19/book_fig_12_12.png` | 14-06 | 機制／形狀對照；`c14_architecture_channels` |
| 24 資料增強改變訓練影像 | `assets/chapters12_19/book_fig_12_13.png` | 14-07 | 同概念重做；`c14_augmentation` |
| 26 Inception 的平行分支 | `assets/chapters12_19/book_fig_12_14.png` | 14-06 | 機制／形狀對照；`c14_architecture_channels` |
| 28 Residual learning | `assets/chapters12_19/book_fig_12_16.png` | 14-06 | 機制／形狀對照；`c14_architecture_channels` |
| 31 Depthwise separable convolution | `assets/chapters12_19/book_fig_12_20.png` | 14-06 | 機制／形狀對照；`c14_architecture_channels` |
| 33 Squeeze-and-Excitation | `assets/chapters12_19/book_fig_12_22.png` | 14-06 | 機制／形狀對照；`c14_architecture_channels` |

本章 12 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 14-01 / `05af86dc` | 2 | 學習成果與課堂安排 |
| 14-02 / `course14` | 2 | 學習成果與課堂安排 |
| 14-03 / `07bbec96` | 8、10、11、17 | 參數共用的效果；卷積手算：一個位置；卷積手算：完整輸出；Max pooling |
| 14-04 / `1180e400` | 3、10、11 | 程式實驗與實際輸出；卷積手算：一個位置；卷積手算：完整輸出 |
| 14-05 / `c14-convolution` | 4、5、7、8、9、10、11、12、13、14、15、16、17、18、19、38 | 影像分類的輸入與輸出；MLP 與 CNN 的銜接；局部感受野；參數共用的效果；濾波器與特徵圖；卷積手算：一個位置；卷積手算：完整輸出；Padding 保留邊界附近的資訊；輸出尺寸公式；多個通道如何合成輸出；Conv2d 的形狀檢查；讀碼練習：影像軸的順序；Max pooling；池化與平移的關係；Pooling 的 PyTorch 實作；Notebook 導讀：可執行的機制與驗收 |
| 14-06 / `c14-architectures` | 20、21、22、23、26、27、28、29、30、31、32、33、34、35、36、37、38 | 分類 CNN 的典型組成；小型 CNN：先追蹤每一層尺寸；分類損失與評估；LeNet-5 與 AlexNet；Inception 的平行分支；1×1 卷積的計算量例子；Residual learning；殘差相加的尺寸條件；殘差連接：一般化的尺寸判斷；Depthwise separable convolution；一般卷積與可分離卷積；Squeeze-and-Excitation；其他 CNN 架構的設計焦點；課堂活動：小影像分類設計；離堂檢核；課後程式與延伸閱讀；Notebook 導讀：可執行的機制與驗收 |
| 14-07 / `c14-augmentation` | 22、24、25、35、38 | 分類損失與評估；資料增強改變訓練影像；增強的標籤檢查；課堂活動：小影像分類設計；Notebook 導讀：可執行的機制與驗收 |

## 15｜電腦視覺_遷移學習與偵測分割

投影片 30 頁；Notebook 7 個程式格。

IoU/NMS 手算、逐框配對與 AP、分割/上採樣、轉置線性算子、追蹤。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/15_detection_demo.png` | 15-04 | 同程式輸出；`15_detection_demo` |
| 12 IoU：框的交集與聯集 | `assets/chapters12_19/book_fig_12_24.png` | 15-03、15-04、15-05 | 同概念重做；`15_detection_demo`、`c15_detection_ap` |
| 15 全卷積網路處理不同尺寸 | `assets/chapters12_19/book_fig_12_26.png` | 15-06 | 機制／形狀對照；`c15_segmentation_upsampling` |
| 22 語意分割的像素標籤 | `assets/chapters12_19/book_fig_12_27.png` | 15-06 | 合成像素標籤對照；`c15_segmentation_upsampling` |
| 24 轉置卷積與上採樣 | `assets/chapters12_19/book_fig_12_28.png` | 15-06 | 線性轉置數值驗算；`c15_segmentation_upsampling` |
| 25 跳接保留細節 | `assets/chapters12_19/book_fig_12_29.png` | 15-06 | 機制／形狀對照；`c15_segmentation_upsampling` |

本章 6 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 15-01 / `ba9387d8` | 2 | 學習成果與課堂安排 |
| 15-02 / `course15` | 2 | 學習成果與課堂安排 |
| 15-03 / `6ed5d6c7` | 12、17、20 | IoU：框的交集與聯集；NMS 手算；偵測程式導讀 |
| 15-04 / `f4aff2f7` | 3、12、17 | 程式實驗與實際輸出；IoU：框的交集與聯集；NMS 手算 |
| 15-05 / `c15-metrics` | 12、13、16、17、18、19、20、30 | IoU：框的交集與聯集；IoU 手算；YOLO 的偵測流程；NMS 手算；Precision、Recall 與 AP；mAP 的定義要寫清楚；偵測程式導讀；Notebook 導讀：可執行的機制與驗收 |
| 15-06 / `c15-segmentation` | 4、11、14、15、22、23、24、25、26、27、30 | 影像任務的輸出差異；定位需要額外的監督訊號；滑動視窗的重複運算；全卷積網路處理不同尺寸；語意分割的像素標籤；語意、實例與全景分割；轉置卷積與上採樣；跳接保留細節；其他卷積層的用途；課堂活動：校園垃圾辨識；Notebook 導讀：可執行的機制與驗收 |
| 15-07 / `c15-transfer-tracking` | 5、6、7、8、9、10、21、27、28、29、30 | 模型選擇的比較表；推論與訓練的記憶體；預訓練模型與前處理成對使用；預訓練類別與目標類別；遷移學習：凍結主幹與更換分類頭；凍結參數與 train／eval；物件追蹤與身分切換；課堂活動：校園垃圾辨識；離堂檢核；課後程式與延伸閱讀；Notebook 導讀：可執行的機制與驗收 |

## 16｜序列模型_RNN與時間序列預測

投影片 36 頁；Notebook 7 個程式格。

RNN/BPTT、固定起點多步預測、LSTM/GRU 與擴張因果卷積。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/16_sequence_demo.png` | 16-04 | 同程式輸出；`16_sequence_demo` |
| 4 循環層沿時間重用參數 | `assets/chapters12_19/book_fig_13_2.png` | 16-05 | 同概念重做；`c16_recurrent_states` |
| 7 四種序列輸入與輸出 | `assets/chapters12_19/book_fig_13_4.png` | 16-05 | 機制／形狀對照；`c16_recurrent_states` |
| 9 Backpropagation through time | `assets/chapters12_19/book_fig_13_5.png` | 16-05 | 共享權重梯度驗算；`c16_recurrent_states` |
| 10 時間序列的季節性 | `assets/chapters12_19/book_fig_13_6.png` | 16-03、16-04、16-06 | 同概念重做；`16_sequence_demo`、`c16_multistep_forecast` |
| 17 深層 RNN 的兩種深度 | `assets/chapters12_19/book_fig_13_10.png` | 16-05 | 機制／形狀對照；`c16_recurrent_states` |
| 19 遞迴式多步預測 | `assets/chapters12_19/book_fig_13_11.png` | 16-06 | 同概念重做；`c16_multistep_forecast` |
| 25 LSTM 的記憶路徑 | `assets/chapters12_19/book_fig_13_12.png` | 16-07 | 機制／門控驗算；`c16_gates_causality` |
| 28 GRU 的精簡門控 | `assets/chapters12_19/book_fig_13_13.png` | 16-07 | 機制／門控驗算；`c16_gates_causality` |
| 32 WaveNet 的擴張卷積 | `assets/chapters12_19/book_fig_13_14.png` | 16-07 | 機制／因果性驗算；`c16_gates_causality` |

本章 10 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 16-01 / `f9bd9423` | 2 | 學習成果與課堂安排 |
| 16-02 / `course16` | 2 | 學習成果與課堂安排 |
| 16-03 / `0c8ffaaf` | 10、11、13、14、15 | 時間序列的季節性；先建立樸素基準；時間切分與洩漏；單步預測的滑動視窗；線性基準與公平比較 |
| 16-04 / `cb7397bd` | 3、10、11、15 | 程式實驗與實際輸出；時間序列的季節性；先建立樸素基準；線性基準與公平比較 |
| 16-05 / `c16-recurrent` | 4、5、6、7、8、9、16、17、24、36 | 循環層沿時間重用參數；RNN 的狀態更新；循環狀態手算；四種序列輸入與輸出；Hidden state 與 output；Backpropagation through time；RNN 的張量形狀；深層 RNN 的兩種深度；長序列訓練的困難；Notebook 導讀：可執行的機制與驗收 |
| 16-06 / `c16-horizons` | 10、11、12、13、14、15、18、19、20、21、22、23、33、36 | 時間序列的季節性；先建立樸素基準；ARMA、ARIMA 與 SARIMA；時間切分與洩漏；單步預測的滑動視窗；線性基準與公平比較；多變量預測的可用性；遞迴式多步預測；多步預測的三種設計；遞迴預測的時間軸；Seq2seq 預測的標籤對齊；評估多步預測；課堂實作：兩週運量預測；Notebook 導讀：可執行的機制與驗收 |
| 16-07 / `c16-gates-causal` | 24、25、26、27、28、29、30、31、32、34、35、36 | 長序列訓練的困難；LSTM 的記憶路徑；LSTM 的核心更新；LSTM 門值手算；GRU 的精簡門控；RNN、LSTM、GRU 的介面差異；一維卷積處理序列；因果卷積只在左側補值；WaveNet 的擴張卷積；離堂檢核；課後程式與延伸閱讀；Notebook 導讀：可執行的機制與驗收 |

## 17｜自然語言處理_詞嵌入與注意力

投影片 37 頁；Notebook 7 個程式格。

Token 位移/embedding、padding/雙向RNN、beam、Luong cross-attention。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/17_attention_demo.png` | 17-04 | 同程式輸出；`17_attention_demo` |
| 5 輸入與目標相差一個位置 | `assets/chapters12_19/book_fig_14_1.png` | 17-05 | 同概念重做；`c17_embedding_padding` |
| 7 Embedding 是可學習的查表 | `assets/chapters12_19/book_fig_14_2.png` | 17-03、17-05 | 查表數值與形狀對照；`c17_embedding_padding` |
| 19 雙向 RNN 的上下文 | `assets/chapters12_19/book_fig_14_4.png` | 17-06 | 機制／形狀對照；`c17_bidirectional_states` |
| 25 Encoder–decoder 翻譯 | `assets/chapters12_19/book_fig_14_5.png` | 17-07 | 機制／形狀對照；`c17_cross_attention` |
| 28 Beam search 保留多條候選 | `assets/chapters12_19/book_fig_14_7.png` | 17-07 | 相同玩具機率搜尋；`c17_cross_attention` |
| 30 Attention 動態讀取來源序列 | `assets/chapters12_19/book_fig_14_8.png` | 17-03、17-04、17-07 | 機制／遮罩對照；`17_attention_demo`、`c17_cross_attention` |

本章 7 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 17-01 / `2f963de5` | 2 | 學習成果與課堂安排 |
| 17-02 / `course17` | 2 | 學習成果與課堂安排 |
| 17-03 / `b7aab10f` | 7、8、30、31 | Embedding 是可學習的查表；Embedding 的輸入與輸出；Attention 動態讀取來源序列；注意力的三個步驟 |
| 17-04 / `c2da3d52` | 3、30、31 | 程式實驗與實際輸出；Attention 動態讀取來源序列；注意力的三個步驟 |
| 17-05 / `c17-tokens` | 4、5、6、7、8、9、13、14、15、16、18、20、21、22、23、37 | 字元語言模型的任務；輸入與目標相差一個位置；字元視窗手算；Embedding 是可學習的查表；Embedding 的輸入與輸出；舊稿補充：One-hot、詞袋與詞向量；情感分類的標籤單位；三種子詞 tokenizer；Tokenizer 必須搭配預訓練模型；Padding 與截斷；情感分類頭的損失與形狀；POS tagging 的逐 token 標籤；Stemming、lemmatization 與任務需求；預訓練表示的兩個層次；Task-specific class、Trainer 與 pipeline；Notebook 導讀：可執行的機制與驗收 |
| 17-06 / `c17-rnn-interface` | 10、11、12、16、17、18、19、20、22、37 | Char-RNN 的模型結構；Temperature 與抽樣；Stateful RNN 的資料順序；Padding 與截斷；Packed sequence 避免讀入尾端補值；情感分類頭的損失與形狀；雙向 RNN 的上下文；POS tagging 的逐 token 標籤；預訓練表示的兩個層次；Notebook 導讀：可執行的機制與驗收 |
| 17-07 / `c17-decoding` | 24、25、26、27、28、29、30、31、32、33、34、35、36、37 | 偏差與公平性檢查；Encoder–decoder 翻譯；Teacher forcing 的位移；翻譯的固定向量瓶頸；Beam search 保留多條候選；Greedy 不一定選到整句高機率；Attention 動態讀取來源序列；注意力的三個步驟；注意力加權平均手算；程式導讀：Luong attention；課堂活動：可重現的情感分類比較；離堂檢核；課後程式與延伸閱讀；Notebook 導讀：可執行的機制與驗收 |

## 18｜Transformer_注意力架構與預訓練

投影片 32 頁；Notebook 7 個程式格。

完整小型 attention block、兩種 mask、MLM/任務頭/QA 與蒸餾。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/18_transformer_mask_demo.png` | 18-04 | 同程式輸出；`18_transformer_mask_demo` |
| 5 原始 Transformer 的完整架構 | `assets/chapters12_19/book_fig_15_3.png` | 18-05 | 機制／形狀對照；`c18_multihead_masks`、`c18_position_encoding` |
| 13 多頭注意力分別學習不同投影 | `assets/chapters12_19/book_fig_15_4.png` | 18-05 | 機制／形狀對照；`c18_multihead_masks`、`c18_position_encoding` |
| 22 BERT 的預訓練目標 | `assets/chapters12_19/book_fig_15_5.png` | 18-06 | 機制／損失位置對照；`c18_mlm_task_heads` |
| 25 分類頭與逐 token 任務頭 | `assets/chapters12_19/book_fig_15_7.png` | 18-06 | 機制／任務頭對照；`c18_mlm_task_heads` |
| 27 DistilBERT 的知識蒸餾 | `assets/chapters12_19/book_fig_15_9.png` | 18-07 | 機制／蒸餾損失對照；`c18_distillation_loss` |

本章 6 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 18-01 / `43be4957` | 2 | 學習成果與課堂安排 |
| 18-02 / `course18` | 2 | 學習成果與課堂安排 |
| 18-03 / `a85b5cd1` | 6、8、15、16 | 序列沒有循環，仍需要位置資訊；固定位置編碼的概念；兩種遮罩處理不同問題；Causal mask 手算 |
| 18-04 / `73a783b2` | 3、15、16 | 程式實驗與實際輸出；兩種遮罩處理不同問題；Causal mask 手算 |
| 18-05 / `c18-attention-block` | 4、5、6、7、8、9、10、11、12、13、14、15、16、17、18、19、20、24、29、30、32 | 三種 Transformer 家族；原始 Transformer 的完整架構；序列沒有循環，仍需要位置資訊；可學習位置向量；固定位置編碼的概念；Q、K、V 的分工；Scaled dot-product attention；點積注意力手算；四行看懂 attention 核心；多頭注意力分別學習不同投影；多頭的維度追蹤；兩種遮罩處理不同問題；Causal mask 手算；Feed-forward network 與殘差；LayerNorm 手算：舊稿的四維例子；Pre-norm 與 post-norm；翻譯 Transformer 的遮罩位置；小型 BERT：區分隨機初始化與預訓練；課堂活動：找出注意力錯誤；離堂檢核；Notebook 導讀：可執行的機制與驗收 |
| 18-06 / `c18-pretraining-heads` | 21、22、23、24、25、26、32 | Encoder-only 模型與 BERT；BERT 的預訓練目標；MLM 的遮蔽規則；小型 BERT：區分隨機初始化與預訓練；分類頭與逐 token 任務頭；問答任務的輸出設計；Notebook 導讀：可執行的機制與驗收 |
| 18-07 / `c18-distillation` | 27、28、31、32 | DistilBERT 的知識蒸餾；Encoder 模型的改良方向；課後程式與延伸閱讀；Notebook 導讀：可執行的機制與驗收 |

## 19｜大型語言模型_生成與聊天系統

投影片 30 頁；Notebook 7 個程式格。

條件生成/top-p、答案遮罩/SFT/DPO、本地檢索與工具介面。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/19_sampling_demo.png` | 19-04 | 同程式輸出；`19_sampling_demo` |
| 4 Decoder-only 逐 token 生成 | `assets/chapters12_19/book_fig_15_12.png` | 19-05 | 機制／自迴歸流程對照；`c19_autoregressive_sampling` |
| 14 聊天模型的訓練階段 | `assets/chapters12_19/book_fig_15_17.png` | 19-06 | 機制／訓練損失對照；`c19_dpo_loss` |

本章 3 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 19-01 / `6ad371cc` | 2 | 學習成果與課堂安排 |
| 19-02 / `course19` | 2 | 學習成果與課堂安排 |
| 19-03 / `8f7926e1` | 7、8 | 小模型生成：明確限制輸出長度；生成參數的效果 |
| 19-04 / `db7761bb` | 3、8 | 程式實驗與實際輸出；生成參數的效果 |
| 19-05 / `c19-generation` | 4、5、6、7、8、9、10、11、12、13、30 | Decoder-only 逐 token 生成；語言模型的機率分解；GPT-1、GPT-2、GPT-3 的閱讀重點；小模型生成：明確限制輸出長度；生成參數的效果；Prompting 與微調；可檢查的提示範例；模型載入與資源估算；Base model 與聊天模型；對話歷史與 context window；Notebook 導讀：可執行的機制與驗收 |
| 19-06 / `c19-alignment-losses` | 14、15、16、17、18、19、20、30 | 聊天模型的訓練階段；SFT：用示範回答教模型；RLHF 與 DPO 的差異；DPO 損失的意義；DPO 手算；答案 log probability 的位移；TRL 訓練流程導讀；Notebook 導讀：可執行的機制與驗收 |
| 19-07 / `c19-rag-tools` | 21、22、23、24、25、26、27、28、29、30 | 完整聊天系統的組成；RAG 的工作流程；工具呼叫與程式執行的邊界；MCP 與結構化生成；框架與執行環境的分工；Encoder–decoder 的 text-to-text 任務；課堂活動：課程規則問答；離堂檢核；課後程式與延伸閱讀；Notebook 導讀：可執行的機制與驗收 |

## 20｜視覺與多模態Transformer

投影片 37 頁；Notebook 7 個程式格。

Patch/視窗/金字塔、DETR 配對、對比/自蒸餾、latent queries 與門控。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/20_multimodal_demo.png` | 20-04 | 同程式輸出；`20_multimodal_demo` |
| 5 DETR：用集合預測做偵測 | `assets/chapters12_19/book_fig_16_2.png` | 20-06 | 機制／形狀與損失對照；`c20_matching_contrast` |
| 7 ViT 把影像切成 token 序列 | `assets/chapters12_19/book_fig_16_3.png` | 20-03、20-05 | 機制／形狀與損失對照；`c20_patches_windows` |
| 11 DeiT 的蒸餾 token | `assets/chapters12_19/book_fig_16_4.png` | 20-05、20-06 | 機制／形狀與損失對照；`c20_patches_windows`、`c20_matching_contrast` |
| 12 PVT 的金字塔表示 | `assets/chapters12_19/book_fig_16_5.png` | 20-05 | 機制／形狀與損失對照；`c20_patches_windows` |
| 13 Swin 的視窗注意力 | `assets/chapters12_19/book_fig_16_6.png` | 20-05 | 機制／形狀與損失對照；`c20_patches_windows` |
| 15 DINO 的自蒸餾 | `assets/chapters12_19/book_fig_16_7.png` | 20-06 | 機制／形狀與損失對照；`c20_matching_contrast` |
| 20 CLIP 的圖文對比學習 | `assets/chapters12_19/book_fig_16_13.png` | 20-03、20-04、20-06 | 機制／形狀與損失對照；`20_multimodal_demo`、`c20_matching_contrast` |
| 25 Perceiver 的 latent bottleneck | `assets/chapters12_19/book_fig_16_15.png` | 20-07 | 機制／形狀與損失對照；數值／表格／流程與形狀 |
| 27 Flamingo 的交錯圖文輸入 | `assets/chapters12_19/book_fig_16_17.png` | 20-07 | 機制／形狀與損失對照；數值／表格／流程與形狀 |
| 29 BLIP-2 的 Q-Former | `assets/chapters12_19/book_fig_16_18.png` | 20-07 | 機制／形狀與損失對照；數值／表格／流程與形狀 |

本章 11 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 20-01 / `81b55fd9` | 2 | 學習成果與課堂安排 |
| 20-02 / `course20` | 2 | 學習成果與課堂安排 |
| 20-03 / `90d43894` | 7、8、20、21、22 | ViT 把影像切成 token 序列；Patch 數量手算；CLIP 的圖文對比學習；CLIP 的相似度矩陣；Zero-shot 分類依賴候選文字 |
| 20-04 / `24ac9cc5` | 3、20、21 | 程式實驗與實際輸出；CLIP 的圖文對比學習；CLIP 的相似度矩陣 |
| 20-05 / `c20-vision-tokens` | 4、7、8、9、10、11、12、13、14、17、37 | 視覺注意力的早期脈絡；ViT 把影像切成 token 序列；Patch 數量手算；以 Conv2d 完成 patch embedding；ViT 的模型結構導讀；DeiT 的蒸餾 token；PVT 的金字塔表示；Swin 的視窗注意力；全域與視窗注意力的成本；其他視覺 Transformer 的路線；Notebook 導讀：可執行的機制與驗收 |
| 20-06 / `c20-matching-contrast` | 5、6、11、15、16、20、21、22、23、37 | DETR：用集合預測做偵測；DETR 的配對概念；DeiT 的蒸餾 token；DINO 的自蒸餾；自監督表示與 attention 圖；CLIP 的圖文對比學習；CLIP 的相似度矩陣；Zero-shot 分類依賴候選文字；CLIP 推論介面；Notebook 導讀：可執行的機制與驗收 |
| 20-07 / `c20-latent-queries` | 18、19、24、25、26、27、28、29、30、31、32、33、34、35、36、37 | 多模態的四種關係；VideoBERT 與 ViLBERT；DALL·E 與 DALL·E 2 的差異；Perceiver 的 latent bottleneck；Perceiver IO 的輸出查詢；Flamingo 的交錯圖文輸入；BLIP 與 BLIP-2 的銜接；BLIP-2 的 Q-Former；BLIP-2 的兩階段學習；舊稿圖片描述程式的閱讀路線；其他多模態任務的分類；多模態評估：看得見與推測的差別；課堂活動：圖片檢索與描述；離堂檢核；課後程式與延伸閱讀；Notebook 導讀：可執行的機制與驗收 |

## 21｜Transformer加速_推論與參數高效微調

投影片 38 頁；Notebook 7 個程式格。

KV 等價、GQA/分塊 softmax、推測驗證、LoRA、MoE、packing/梯度累積。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/21_transformer_efficiency_demo.png` | 21-04 | 同程式輸出；`21_transformer_efficiency_demo` |
| 6 KV cache 重用先前的投影 | `assets/chapters12_19/book_fig_17_1.png` | 21-03、21-04、21-05 | 數值等價與快取流程對照；`21_transformer_efficiency_demo`、`c21_sparse_mask` |
| 10 推測解碼先提案再驗證 | `assets/chapters12_19/book_fig_17_2.png` | 21-06 | 驗證規則與分布驗算；`c21_lora_training` |
| 17 MHA、MQA 與 GQA | `assets/chapters12_19/book_fig_17_11.png` | 21-05 | 機制／形狀對照；`c21_sparse_mask` |
| 25 LoRA 的低秩參數更新 | `assets/chapters12_19/book_fig_17_15.png` | 21-03、21-06 | 機制／低秩訓練對照；`c21_lora_training` |
| 30 Packing 與 bucketing 減少補值 | `assets/chapters12_19/book_fig_17_16.png` | 21-07 | 機制／遮罩對照；`c21_packing_mask` |

本章 6 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 21-01 / `4fc5420c` | 2 | 教材範圍與學習成果 |
| 21-02 / `course21` | 2 | 教材範圍與學習成果 |
| 21-03 / `e52edb8a` | 5、6、7、25、26 | 先辨認瓶頸；KV cache 重用先前的投影；為何不必快取全部 Q；LoRA 的低秩參數更新；LoRA 的參數量手算 |
| 21-04 / `b9e7d011` | 3、5、6 | 程式實驗與實際輸出；先辨認瓶頸；KV cache 重用先前的投影 |
| 21-05 / `c21-cache-attention` | 6、7、8、9、13、14、15、16、17、18、19、20、21、22、38 | KV cache 重用先前的投影；為何不必快取全部 Q；KV cache 記憶體手算；Cache 的功能比較；注意力分數的平方成本；稀疏注意力：限制可見位置；近似注意力的不同路線；Performer 的重排概念；MHA、MQA 與 GQA；共享 K／V 的尺寸比較；GQA 的讀碼尺寸；MLA 與潛在快取（選讀）；FlashAttention 的重點；分塊 Softmax 的穩定性；Notebook 導讀：可執行的機制與驗收 |
| 21-06 / `c21-speculation-lora` | 10、11、12、23、24、25、26、27、28、38 | 推測解碼先提案再驗證；Greedy 與抽樣的驗證不同；平行生成與動態批次；MoE 的稀疏啟用；MoE 的訓練問題（選讀）；LoRA 的低秩參數更新；LoRA 的參數量手算；PEFT：指定要加 LoRA 的模組；Adapters 與其他 PEFT 方法；Notebook 導讀：可執行的機制與驗收 |
| 21-07 / `c21-batching` | 29、30、31、32、33、34、35、36、37、38 | Activation checkpointing；Packing 與 bucketing 減少補值；Packing 的文件邊界；Gradient accumulation；累積梯度：處理最後不足一組；平行訓練的切分方式；課堂活動：兩種瓶頸的方案；離堂檢核；課後程式與延伸閱讀；Notebook 導讀：可執行的機制與驗收 |

## 22｜生成模型_自編碼器GAN與擴散

投影片 47 頁；Notebook 8 個程式格。

測試重建/去噪、VAE/VQ、GAN 交替梯度、加噪及解析高斯反向取樣。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/22_generative_demo.png` | 22-04 | 同程式輸出；`22_generative_demo` |
| 6 線性 Autoencoder 與 PCA | `assets/chapters12_19/book_fig_18_2.png` | 22-03、22-05 | 線性子空間對照；`c22_denoising_pairs`、`c22_sparse_kl` |
| 11 重建圖要與原圖成對檢查 | `assets/chapters12_19/book_fig_18_4.png` | 22-04、22-05 | 測試影像同概念重做；`22_generative_demo`、`c22_denoising_pairs`、`c22_sparse_kl` |
| 17 Denoising AE 的訓練配對 | `assets/chapters12_19/book_fig_18_9.png` | 22-05 | 線性去噪配對對照；`c22_denoising_pairs`、`c22_sparse_kl` |
| 21 VAE 學習潛在分布 | `assets/chapters12_19/book_fig_18_12.png` | 22-06 | 重參數化／KL 驗算；`c22_latent_interpolation` |
| 27 Latent interpolation | `assets/chapters12_19/book_fig_18_14.png` | 22-06 | PCA decoder 插值機制；`c22_latent_interpolation` |
| 30 GAN 的兩個模型 | `assets/chapters12_19/book_fig_18_15.png` | 22-07 | 一維交替梯度對照；`c22_gan_collapse` |
| 34 Mode collapse | `assets/chapters12_19/book_fig_18_17.png` | 22-07 | 刻意構造的崩塌診斷；`c22_gan_collapse` |
| 36 擴散模型的正向與反向過程 | `assets/chapters12_19/book_fig_18_18.png` | 22-08 | 解析高斯反向流程；`c22_forward_noise`、`c22_noise_schedule`、`c22_reverse_gaussian` |
| 38 噪聲排程與剩餘訊號 | `assets/chapters12_19/book_fig_18_19.png` | 22-08 | 加噪排程重做；`c22_forward_noise`、`c22_noise_schedule`、`c22_reverse_gaussian` |

本章 10 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 22-01 / `d6f0188c` | 2 | 學習成果與課堂安排 |
| 22-02 / `course22` | 2 | 學習成果與課堂安排 |
| 22-03 / `d51f8ee1` | 4、5、6、7、8、9、12 | 重建與生成的差別；Autoencoder 的表示學習；線性 Autoencoder 與 PCA；與本地 PCA 程式的連結；SVD 程式的可用部分與限制；線性 AE 的最小結構；AE 異常偵測的假設 |
| 22-04 / `34cdc5e6` | 3、11 | 程式實驗與實際輸出；重建圖要與原圖成對檢查 |
| 22-05 / `c22-autoencoding` | 5、6、7、8、9、10、11、12、13、14、15、16、17、18、19、20、47 | Autoencoder 的表示學習；線性 Autoencoder 與 PCA；與本地 PCA 程式的連結；SVD 程式的可用部分與限制；線性 AE 的最小結構；Stacked AE 的瓶頸；重建圖要與原圖成對檢查；AE 異常偵測的假設；重建誤差閾值活動；表示視覺化與無監督預訓練；Tied weights 與逐層預訓練；卷積 Autoencoder；Denoising AE 的訓練配對；去噪任務的實作檢查；稀疏 AE 的約束；稀疏懲罰的 KL 形式；Notebook 導讀：可執行的機制與驗收 |
| 22-06 / `c22-latent` | 21、22、23、24、25、26、27、28、29、47 | VAE 學習潛在分布；Reparameterization trick；VAE 的抽樣；VAE 的重建與 KL 平衡；標準常態先驗的 KL；從先驗生成與重建的不同；Latent interpolation；離散 VAE 與 Gumbel-Softmax；VQ-VAE 的 codebook；Notebook 導讀：可執行的機制與驗收 |
| 22-07 / `c22-gan` | 30、31、32、33、34、35、47 | GAN 的兩個模型；GAN 的訓練目標；訓練 D 時隔開 generator 梯度；訓練 G 時仍須通過 D；Mode collapse；GAN 的不穩定與 DCGAN；Notebook 導讀：可執行的機制與驗收 |
| 22-08 / `c22-diffusion` | 36、37、38、39、40、41、42、43、44、45、46、47 | 擴散模型的正向與反向過程；任意時間步的加噪公式；噪聲排程與剩餘訊號；擴散訓練的輸入與標籤；去噪網路需要知道時間；DDPM 與 DDIM 取樣；Latent diffusion 與條件生成；生成程式的閱讀路線；課堂活動：生成模型比較；離堂檢核；課後程式與延伸閱讀；Notebook 導讀：可執行的機制與驗收 |

## 23｜強化學習_策略價值與深度RL

投影片 43 頁；Notebook 7 個程式格。

回報/Q 手算、LineWorld/Bellman/DQN、policy gradient/PPO、影格介面。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/23_rl_demo.png` | 23-04 | 同程式輸出；`23_rl_demo` |
| 7 CartPole 的任務 | `assets/chapters12_19/book_fig_19_4.png` | 23-05 | 觀測角色／幾何示意；`c23_return_observation` |
| 11 Credit assignment 的回報分配 | `assets/chapters12_19/book_fig_19_6.png` | 23-05 | 相同回報手算；`c23_return_observation` |
| 17 Markov decision process | `assets/chapters12_19/book_fig_19_8.png` | 23-06 | 小型 MDP 機制對照；`c23_bellman_dqn` |
| 33 Atari 的影格前處理 | `assets/chapters12_19/book_fig_19_11.png` | 23-07 | 合成影格／形狀對照；`c23_ppo_clip`、`c23_frame_preprocessing` |

本章 5 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 23-01 / `b4bd891b` | 2 | 學習成果與課堂安排 |
| 23-02 / `course23` | 2 | 學習成果與課堂安排 |
| 23-03 / `99dd478d` | 4、5、24 | Agent 與環境的互動；Reward、return 與 policy；探索與利用 |
| 23-04 / `bf753cb5` | 3、24、39 | 程式實驗與實際輸出；探索與利用；RL 實驗的評估方式 |
| 23-05 / `c23-returns-environment` | 4、5、7、8、9、10、11、12、13、16、21、22、23、40、43 | Agent 與環境的互動；Reward、return 與 policy；CartPole 的任務；Gymnasium 的一步互動；Terminated 與 truncated；折扣回報；Credit assignment 的回報分配；回報手算：10、0、−50；折扣回報的小函式；Markov 性與 observation；舊稿手算：一般移動；舊稿手算：抵達終點；舊稿手算：碰牆但尚未終止；課堂活動：迷宮與 CartPole；Notebook 導讀：可執行的機制與驗收 |
| 23-06 / `c23-mdp-dqn` | 16、17、18、19、20、24、25、26、27、28、29、36、37、40、43 | Markov 性與 observation；Markov decision process；Value iteration 與 Bellman 最優性；TD learning 用樣本更新；Q-learning 的更新式；探索與利用；DQN 用網路近似 Q 函數；DQN 的兩個動作輸出；Replay buffer 與 target network；DQN 的 TD target；DQN 的常見改善；演算法比較；On-policy、off-policy 與環境模型；課堂活動：迷宮與 CartPole；Notebook 導讀：可執行的機制與驗收 |
| 23-07 / `c23-policy-preprocessing` | 6、14、15、30、31、32、33、34、35、36、37、38、39、41、42、43 | Policy search 與神經網路策略；REINFORCE 的更新方向；Policy gradient 程式導讀；Actor–critic 的兩個角色；Actor loss 與 critic loss 分開；PPO 限制策略一次改太多；Atari 的影格前處理；Stable-Baselines3 的小型介面示例；Atari 完整實驗的閱讀路線；演算法比較；On-policy、off-policy 與環境模型；連續動作與其他演算法（選讀）；RL 實驗的評估方式；離堂檢核；課後程式與延伸閱讀；Notebook 導讀：可執行的機制與驗收 |

## 24｜附錄A_自動微分與計算圖

投影片 21 頁；Notebook 6 個程式格。

對偶數、可執行反向引擎、計算圖、分支累積與 detach。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/24_autodiff_demo.png` | 24-04 | 同程式輸出；`24_autodiff_demo` |
| 9 前向模式沿計算順序傳遞導數 | `assets/chapters12_19/book_fig_A_1.png` | 24-05、24-06 | 對偶數／前向圖驗算；`c24_computation_graph` |
| 12 反向模式由輸出往回傳 | `assets/chapters12_19/book_fig_A_3.png` | 24-06 | 反向計算圖驗算；`c24_computation_graph` |

本章 3 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 24-01 / `026b5b57` | 2 | 學習成果與使用時機 |
| 24-02 / `course24` | 2 | 學習成果與使用時機 |
| 24-03 / `a37f8d8c` | 4、5、6、7 | 同一函式的三種求導方式；手算梯度；有限差分與步長；有限差分的可執行小例子 |
| 24-04 / `9571d31e` | 3、6、7 | 程式實驗與實際輸出；有限差分與步長；有限差分的可執行小例子 |
| 24-05 / `c24-dual` | 4、5、8、9、10、11、14、18、21 | 同一函式的三種求導方式；手算梯度；計算圖與中間變數；前向模式沿計算順序傳遞導數；前向模式手算；對偶數的表示；前向與反向模式的選擇；課堂活動：梯度檢查；Notebook 導讀：可執行的機制與驗收 |
| 24-06 / `c24-reverse` | 8、9、12、13、14、15、16、17、18、19、20、21 | 計算圖與中間變數；前向模式沿計算順序傳遞導數；反向模式由輸出往回傳；反向模式手算；前向與反向模式的選擇；PyTorch autograd 驗算；梯度累積與計算圖生命週期；與手刻反向傳播程式對照；課堂活動：梯度檢查；離堂檢核；課後程式與延伸閱讀；Notebook 導讀：可執行的機制與驗收 |

## 25｜附錄B_混合精度與量化

投影片 28 頁；Notebook 7 個程式格。

浮點位元/BF16 模擬、loss scaling、量化粒度/PTQ/QAT/STE。

### 每個圖檔引用的程式位置

| 頁次／主題 | 圖檔 | 程式代碼 | 對應範圍與輸出 |
|---|---|---|---|
| 3 程式實驗與實際輸出 | `../programs/outputs/figures/25_quantization_demo.png` | 25-04 | 同程式輸出；`25_quantization_demo` |
| 4 數值格式的位元分配 | `assets/chapters12_19/book_fig_B_1.png` | 25-05 | 位元配置重畫；`c25_float_bit_layout` |
| 8 混合精度訓練 | `assets/chapters12_19/book_fig_B_2.png` | 25-05 | loss scaling／順序數值驗算；`c25_float_bit_layout` |
| 14 對稱量化 | `assets/chapters12_19/book_fig_B_3.png` | 25-03、25-04、25-06 | 同概念量化重做；`25_quantization_demo`、`c25_quantization_granularity` |

本章 4 個圖檔引用均列於上表。

### 每個程式格反查投影片

| 程式代碼／cell id | 頁次 | 教學內容 |
|---|---|---|
| 25-01 / `69b461ca` | 2 | 學習成果與課堂安排 |
| 25-02 / `course25` | 2 | 學習成果與課堂安排 |
| 25-03 / `a4e90a9c` | 12、14、16 | 線性量化與反量化；對稱量化；對稱 INT8 權重量化 |
| 25-04 / `1665f6c8` | 3、14、16 | 程式實驗與實際輸出；對稱量化；對稱 INT8 權重量化 |
| 25-05 / `c25-formats-scaling` | 4、5、6、7、8、9、10、11、25、28 | 數值格式的位元分配；FP32、FP16 與 BF16；模型權重大小估算；降低精度的不同位置；混合精度訓練；AMP 與 loss scaling；CUDA FP16 的 AMP 訓練步驟；AMP 與梯度裁切的順序；課堂活動：精度比較表；Notebook 導讀：可執行的機制與驗收 |
| 25-06 / `c25-quantization` | 12、13、14、15、16、18、25、26、28 | 線性量化與反量化；量化手算；對稱量化；對稱、非對稱與粒度；對稱 INT8 權重量化；動態與靜態量化；課堂活動：精度比較表；離堂檢核；Notebook 導讀：可執行的機制與驗收 |
| 25-07 / `c25-ptq-qat` | 17、18、19、20、21、22、23、24、25、26、27、28 | PTQ 與 QAT；動態與靜態量化；靜態 PTQ 的工作流程；書中量化程式的版本邊界；QAT 的 fake quantization；BitsAndBytes 與低位元 LLM；量化設定與計算精度分開指定；預先量化模型與格式；課堂活動：精度比較表；離堂檢核；課後程式與延伸閱讀；Notebook 導讀：可執行的機制與驗收 |
