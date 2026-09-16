---
marp: true
theme: ml-course
size: 16:9
paginate: true
math: katex
title: 決策樹與SVM補充
---

<!-- _class: cover -->
<!-- _footer: "主教材 Ch.5 pp.179–194；舊稿 03 s.1–51" -->
<!-- meta: minutes=1; core6=yes; block=0; source=主教材 Ch.5 pp.179–194 -->
# 決策樹與SVM補充

第 6 週｜從可解釋的分割規則，走到模型邊界比較

後續八週課程｜每週 180 分鐘（含兩次 10 分鐘休息）

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _footer: "主教材 Ch.5 pp.179–194" -->
<!-- meta: minutes=1; core6=yes; block=0; source=主教材 Ch.5 pp.179–194 -->
## 本週成果與三段安排

0–50 分：走訪決策樹、機率與不純度。

60–120 分：CART、正則化與迴歸樹。

130–180 分：穩定性、SVM 補充與模型比較。

能交付：一條預測路徑、一個分割計算，以及有理由的模型選擇。

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _class: figure -->
<!-- _footer: "主教材 Ch.5 p.180，圖 5-1" -->
<!-- meta: minutes=3; core6=yes; block=0; source=主教材 Ch.5 p.180，圖 5-1 -->
## 從根節點走到葉節點：Iris 決策樹

![h:390 Iris decision tree](assets/chapters04_09/book_fig_5_1.png)

每次只回答一個特徵閾值問題；最終葉節點提供類別分布。

<!-- 講者提示：左支代表条件成立。圖中 samples 與 value 是教材訓練資料計數；不同版本 API 的 value 可能顯示比例。 -->

---

<!-- _footer: "主教材 Ch.5 pp.180–181；舊稿 03 s.37–40" -->
<!-- meta: minutes=5; core6=yes; block=0; source=主教材 Ch.5 pp.180–181；舊稿 03 s.37–40 -->
## 讀懂節點上的四種資訊

- 規則：例如花瓣長度是否小於等於 2.45 cm。
- `samples`：到達此節點的訓練樣本數。
- `value`：各類別的計數或比例，依顯示工具而異。
- `gini`：混雜程度；0 表示節點內只有一類。

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _class: figure -->
<!-- _footer: "主教材 Ch.5 p.182，圖 5-2" -->
<!-- meta: minutes=3; core6=yes; block=0; source=主教材 Ch.5 p.182，圖 5-2 -->
## 樹把空間切成一塊一塊的區域

![h:390 Decision tree decision boundaries](assets/chapters04_09/book_fig_5_2.png)

第一次分割作用於全區域；後續分割只作用於相應子區域。

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _footer: "主教材 Ch.5 p.182" -->
<!-- meta: minutes=5; core6=yes; block=0; source=主教材 Ch.5 p.182 -->
## 葉節點的機率來自到達此處的樣本

若葉節點有 $[0,49,5]$ 共 54 筆，則

$$\hat p=(0,49/54,5/54)\approx(0,.907,.093)$$

輸出最多的類別；機率是區域內的訓練頻率估計，並非個體的確定性。

<!-- 講者提示：花瓣長 5、寬 1.5 的例子走到此葉。小葉的機率可能很極端且不穩定。 -->

---

<!-- _footer: "主教材 Ch.5 p.181，式 5-1；舊稿 03 s.41–46" -->
<!-- meta: minutes=5; core6=yes; block=0; source=主教材 Ch.5 p.181，式 5-1；舊稿 03 s.41–46 -->
## Gini：隨機抽兩個標籤會多常不同？

$$G_i=1-\sum_{k=1}^K p_{i,k}^2$$

二元節點各一半時 $G=0.5$；單一類別時 $G=0$。

三類均等時 $G=2/3$，因此 Gini 的最大值不固定為 0.5。

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _footer: "主教材 Ch.5 p.185，式 5-3；舊稿 03 s.41–46" -->
<!-- meta: minutes=5; core6=yes; block=0; source=主教材 Ch.5 p.185，式 5-3；舊稿 03 s.41–46 -->
## Entropy：標籤越難猜，資訊量越大

$$H_i=-\sum_{k:p_{i,k}>0}p_{i,k}\log_2p_{i,k}$$

約定 $0\log 0=0$。二元各一半時是 1 bit；單一類別是 0。

Gini 與 Entropy 常給出相近分割，但不保證完全相同。

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _class: activity -->
<!-- _footer: "主教材 Ch.5 pp.179–194" -->
<!-- meta: minutes=18; core6=yes; block=0; source=主教材 Ch.5 pp.179–194 -->
## 手算：哪個節點比較純？

A 節點標籤數 `[4,0]`，B 為 `[2,2]`，C 為 `[3,1]`。

1. 各算 Gini 與 Entropy。
2. 用一句話解释「純度」與「預測是否正確」的差別。

<!-- 講者提示：Gini：0、.5、.375；Entropy：0、1、.811278。純度只描述該節點訓練標籤，不能保證未來樣本正確。 -->

---

<!-- _class: small -->
<!-- _footer: "主教材 Ch.5 pp.179–182；舊稿 03 s.47" -->
<!-- meta: minutes=4; core6=yes; block=0; source=主教材 Ch.5 pp.179–182；舊稿 03 s.47 -->
## 建立一棵可閱讀的樹

```python
from sklearn.tree import DecisionTreeClassifier, export_text
tree = DecisionTreeClassifier(max_depth=2, random_state=42)
tree.fit(X_train, y_train)
print(export_text(tree, feature_names=feature_names))
proba = tree.predict_proba(X_test[:2])
```

先限制深度方便閱讀；正式選擇仍要比較驗證表現。

<!-- 講者提示：X_train 只放對應 feature_names 的欄位。類別機率欄順序查 classes_，不要假定標籤一定是 0,1,2。 -->

---

<!-- _class: activity -->
<!-- _footer: "主教材 Ch.5 pp.179–194" -->
<!-- meta: minutes=10; core6=yes; block=-1; source=主教材 Ch.5 pp.179–194 -->
## 休息 10 分鐘

離開座位、休息眼睛。回來後先用一句話回答上一段的核心問題。

<!-- 講者提示：保留完整休息；不要用來補講延伸內容。 -->

---

<!-- _footer: "主教材 Ch.5 p.184，式 5-2" -->
<!-- meta: minutes=4; core6=yes; block=1; source=主教材 Ch.5 p.184，式 5-2 -->
## CART：挑選加權子節點不純度最小的分割

$$J(k,t_k)=\frac{m_L}{m}G_L+\frac{m_R}{m}G_R$$

在候選特徵 $k$ 與閾值 $t_k$ 中選最小值，再遞迴處理子節點。

這是貪婪的二元分割；每步最佳不代表整棵樹全域最佳。

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _class: activity -->
<!-- _footer: "主教材 Ch.5 pp.179–194" -->
<!-- meta: minutes=16; core6=yes; block=1; source=主教材 Ch.5 pp.179–194 -->
## 算一次分割，不能只比較左右平均

父節點有 `[4,4]`，共 8 筆。

方案 A：左 `[3,0]`，右 `[1,4]`。
方案 B：左 `[2,2]`，右 `[2,2]`。

計算兩方案加權 Gini 與相對父節點的下降量。

<!-- 講者提示：父 Gini=.5。A 左0、右.32，加權3/8×0+5/8×.32=.2，下降.3；B 加權.5，下降0。分割應選A，注意權重是樣本數而非左右各半。 -->

---

<!-- _class: small -->
<!-- _footer: "主教材 Ch.5 pp.184–185；舊稿 03 s.48–49" -->
<!-- meta: minutes=4; core6=yes; block=1; source=主教材 Ch.5 pp.184–185；舊稿 03 s.48–49 -->
## 限制樹的成長：先控制葉節點有多少證據

| 參數 | 作用 | 加強正則化的方向 |
| --- | --- | --- |
| max_depth | 最大深度 | 調小 |
| min_samples_split | 允許分割的最少樣本數 | 調大 |
| min_samples_leaf | 葉節點最少樣本數 | 調大 |
| max_leaf_nodes | 葉節點數上限 | 調小 |

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _class: small -->
<!-- _footer: "主教材 Ch.5 pp.184–185；剪枝整合" -->
<!-- meta: minutes=4; core6=no; block=1; source=主教材 Ch.5 pp.184–185；剪枝整合 -->
## 其他停止條件與剪枝

| 設定 | 控制的內容 |
| --- | --- |
| min_weight_fraction_leaf | 葉節點最少權重占比 |
| min_impurity_decrease | 分割帶來的最小加權不純度下降 |
| max_features | 每次候選特徵數 |
| ccp_alpha | 成本複雜度剪枝強度；越大通常樹越小 |

<!-- 講者提示：非參數模型是參數數量不預先固定，不是沒有超參數。ccp_alpha 在訓練資料內用 CV 選擇。 -->

---

<!-- _class: figure -->
<!-- _footer: "主教材 Ch.5 p.188，圖 5-3" -->
<!-- meta: minutes=3; core6=yes; block=1; source=主教材 Ch.5 p.188，圖 5-3 -->
## 正則化前後：彎月資料的邊界

![h:390 Decision boundaries of an unregularized tree (left) and a regularized tree
(right)](assets/chapters04_09/book_fig_5_3.png)

增加葉節點最少樣本數，可以減少為個別樣本切出的細碎區域。

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _footer: "主教材 Ch.5 pp.186–187" -->
<!-- meta: minutes=4; core6=yes; block=1; source=主教材 Ch.5 pp.186–187 -->
## 迴歸樹：葉節點改成輸出數值平均

$$\hat y_{\rm node}=\frac1{m_{\rm node}}\sum_{i\in\rm node}y^{(i)}$$

在平方誤差目標下，葉內平均值最小化該葉的總平方殘差。

輸出通常是分段常數；不會自然外插出向上延伸的直線。

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _class: figure -->
<!-- _footer: "主教材 Ch.5 p.189，圖 5-4" -->
<!-- meta: minutes=3; core6=yes; block=1; source=主教材 Ch.5 p.189，圖 5-4 -->
## 讀迴歸樹：追蹤規則與葉內平均

![h:390 A decision tree for regression](assets/chapters04_09/book_fig_5_4.png)

每個葉節點顯示預測平均值及其平方誤差；不再顯示類別 Gini。

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _footer: "主教材 Ch.5 p.190，式 5-4" -->
<!-- meta: minutes=4; core6=yes; block=1; source=主教材 Ch.5 p.190，式 5-4 -->
## CART 迴歸目標：比較子節點的加權 MSE

$$J(k,t_k)=\frac{m_L}{m}\operatorname{MSE}_L+\frac{m_R}{m}\operatorname{MSE}_R$$

$$\operatorname{MSE}_{\rm node}=\frac1{m_{\rm node}}\sum_{i\in\rm node}(y^{(i)}-\hat y_{\rm node})^2$$

<!-- 講者提示：這裡平均與權重配合，使目標等同全部樣本的平方誤差平均。 -->

---

<!-- _class: figure -->
<!-- _footer: "主教材 Ch.5 p.189，圖 5-5" -->
<!-- meta: minutes=3; core6=yes; block=1; source=主教材 Ch.5 p.189，圖 5-5 -->
## 增加深度：階梯更細，表達能力更強

![h:390 Predictions of two decision tree regression models](assets/chapters04_09/book_fig_5_5.png)

深度增加可降低訓練誤差，也可能開始追逐雜訊。

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _class: figure -->
<!-- _footer: "主教材 Ch.5 p.190，圖 5-6" -->
<!-- meta: minutes=3; core6=yes; block=1; source=主教材 Ch.5 p.190，圖 5-6 -->
## 迴歸樹也需要正則化

![h:390 Predictions of an unregularized regression tree (left) and a regularized tree
(right)](assets/chapters04_09/book_fig_5_6.png)

限制最小葉樣本數，能減少尖銳、短促的階梯。

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _class: activity -->
<!-- _footer: "主教材 Ch.5 pp.179–194" -->
<!-- meta: minutes=12; core6=yes; block=1; source=主教材 Ch.5 pp.179–194 -->
## 迴歸葉節點：為什麼預測平均值？

同一葉中的目標是 `[1, 2, 6]`。

比較預測 2、3、4 的 MSE，找出最佳值。

再討論：如果損失改成絕對誤差，最佳常數會改成什麼？

<!-- 講者提示：平均=3；三個 MSE 分別 17/3、14/3、17/3。絕對誤差以中位數2最小。這說明輸出規則取決於損失。 -->

---

<!-- _class: activity -->
<!-- _footer: "主教材 Ch.5 pp.179–194" -->
<!-- meta: minutes=10; core6=yes; block=-1; source=主教材 Ch.5 pp.179–194 -->
## 休息 10 分鐘

離開座位、休息眼睛。回來後先用一句話回答上一段的核心問題。

<!-- 講者提示：保留完整休息；不要用來補講延伸內容。 -->

---

<!-- _class: figure -->
<!-- _footer: "主教材 Ch.5 p.191，圖 5-7" -->
<!-- meta: minutes=3; core6=yes; block=2; source=主教材 Ch.5 p.191，圖 5-7 -->
## 座標軸方向會影響樹的複雜度

![h:390 Sensitivity to training set rotation](assets/chapters04_09/book_fig_5_7.png)

樹的分割通常平行於特徵軸；旋轉資料後，原本簡單的斜線可能需很多階梯。

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _class: figure -->
<!-- _footer: "主教材 Ch.5 p.192，圖 5-8" -->
<!-- meta: minutes=3; core6=no; block=2; source=主教材 Ch.5 p.192，圖 5-8 -->
## PCA 旋轉後，樹可能更容易分割

![h:390 A tree’s decision boundaries on the scaled and PCA-rotated iris dataset](assets/chapters04_09/book_fig_5_8.png)

縮放與旋轉不同：單調縮放通常保持排序，旋轉會改變分割方向。

<!-- 講者提示：若採 PCA，必須把 PCA 與樹一起放入交叉驗證；不可先對全資料 fit。 -->

---

<!-- _class: figure -->
<!-- _footer: "主教材 Ch.5 p.192，圖 5-9" -->
<!-- meta: minutes=3; core6=yes; block=2; source=主教材 Ch.5 p.192，圖 5-9 -->
## 小幅改動訓練資料，樹可能換一套規則

![h:390 Retraining the same model on the same data may produce a very different
model](assets/chapters04_09/book_fig_5_9.png)

單棵樹具有高變異傾向；下一週用多棵不同的樹降低不穩定性。

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _footer: "舊稿 03 s.1–16（補充；不屬於本次 Ch.4–9 主線）" -->
<!-- meta: minutes=5; core6=no; block=2; source=舊稿 03 s.1–16（補充；不屬於本次 Ch.4–9 主線） -->
## 補充 SVM：用間隔比較不同的分隔面

$$f(x)=w^Tx+b,\qquad\hat y=\operatorname{sign}(f(x))$$

線性可分時，將邊界兩側最近點的函數間隔規範為 $\pm1$，兩條支持超平面距離為 $2/\|w\|$。

<!-- 講者提示：y 使用 -1,+1；支持向量是影響邊界的樣本，不是所有資料平均。 -->

---

<!-- _footer: "舊稿 03 s.17–23（補充）" -->
<!-- meta: minutes=4; core6=no; block=2; source=舊稿 03 s.17–23（補充） -->
## 補充 SVM：軟間隔與 hinge loss

$$\min_{w,b}\frac12\|w\|^2+C\sum_i\max(0,1-y^{(i)}f(x^{(i)}))$$

$C$ 越大，越重視違反間隔的代價；越小，越容許違反以換取較大間隔。

特徵尺度會改變距離與懲罰，通常要先標準化。

<!-- 講者提示：hinge 非零不一定分類錯：位於正確側但在 margin 內也有損失。 -->

---

<!-- _footer: "舊稿 03 s.24–33（補充）" -->
<!-- meta: minutes=4; core6=no; block=2; source=舊稿 03 s.24–33（補充） -->
## 補充 SVM：核函數與 RBF 的 gamma

$$K(x,z)=\phi(x)^T\phi(z),\qquad K_{\rm RBF}(x,z)=e^{-\gamma\|x-z\|^2}$$

核技巧以相似度取代顯式高維展開。$\gamma$ 越大，單點影響越局部，邊界可能更細碎。

<!-- 講者提示：gamma 與 C 需一起驗證；核 SVM 在大樣本時訓練成本可能高。 -->

---

<!-- _class: small -->
<!-- _footer: "舊稿 03 s.13–16、35–36（推導延伸）" -->
<!-- meta: minutes=4; core6=no; block=2; source=舊稿 03 s.13–16、35–36（推導延伸） -->
## 補充 SVM：原始問題與對偶的關係

硬間隔：$\min\frac12\|w\|^2$，限制 $y_i(w^Tx_i+b)\ge1$。

對偶：$\max_a\sum_i a_i-\frac12\sum_{i,j}a_ia_jy_iy_jK(x_i,x_j)$。

限制 $a_i\ge0,\ \sum_i a_iy_i=0$；軟間隔再加 $a_i\le C$。

支持向量對應非零對偶係數；可延伸 OvR／OvO 處理多類別。

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _class: small -->
<!-- _footer: "主教材 Ch.4–5；舊稿 03 s.34、50–51" -->
<!-- meta: minutes=4; core6=yes; block=2; source=主教材 Ch.4–5；舊稿 03 s.34、50–51 -->
## 三種分類模型的比較

| 模型 | 典型邊界 | 重要檢查 |
| --- | --- | --- |
| Logistic | 線性分數＋機率 | 正則化、校準、閾值 |
| SVM（補充） | 線性或核邊界 | 縮放、C、gamma；分數不等於機率 |
| 決策樹 | 軸平行分區 | 深度、葉樣本數、穩定性 |

<!-- 講者提示：先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。 -->

---

<!-- _class: activity -->
<!-- _footer: "主教材 Ch.5 pp.179–194" -->
<!-- meta: minutes=17; core6=yes; block=2; source=主教材 Ch.5 pp.179–194 -->
## 比較實作：同一切分，兩種模型

使用同一份訓練與測試資料。

1. CV 比較樹深度 `[2,4,8,None]`。
2. 比較標準化 Logistic；八週版再加入標準化 SVM。
3. 除指標外，報告模型規則、錯誤案例與訓練時間。
4. 離線：解釋斜向邊界為何可能讓淺樹吃虧。

<!-- 講者提示：評分：同一資料切分、前處理在 CV 內、測試一次、有證據的邊界解釋。SVM 是補充，六週版移課後。 -->

---

<!-- _footer: "主教材 Ch.5 pp.179–194" -->
<!-- meta: minutes=3; core6=yes; block=2; source=主教材 Ch.5 pp.179–194 -->
## 離堂檢核與作業

1. CART 為何要依樣本數加權？
2. 為什麼葉節點很純，仍可能測試表現差？
3. 哪一種資料改動可能明顯改變樹的規則？

課後：Ch.5 練習 1–7；進階以多個抽樣子集比較樹的穩定性。

<!-- 講者提示：答案：各樣本權重一致；過度適配少量資料；資料抽樣／移除關鍵點／旋轉特徵。 -->
