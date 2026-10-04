# 碩士班機器學習：Marp 教學教材

依 `book/` 的主教材順序編製，以 `source_pptx/` 的相關概念、圖表及案例補充。採繁體中文、16:9 Marp 格式。原始 PDF 與 PPTX 保持原樣。目前包含 `slides/00–25` 的完整課程與附錄。

## 編修與產出約定

`slides/` 的 Marp 檔是唯一的日常編修對象。新增或修改投影片時，先只處理 Marp 原稿與必要的原始碼語法檢查；**不產生 HTML、PDF 或 `programs/` 教學範例程式**。PDF 僅在教師檢視、修正 Marp 並明確要求後才輸出；`programs/` 的抓取、產生與正確性檢查也同樣必須另行明確要求。2026-10-04 已依明確要求更新第 02–25 章的 PDF 與 HTML。

## 目前匯出檔與教學閱讀版

2026-10-04 更新第 **02–25 章，24 份 PDF／HTML，共 980 頁**。

- [投影片 PDF／HTML 入口](output/html/index.html)：用於投影、翻頁、註記與列印；投影片 HTML 內嵌圖片與數學字型。
- [Notebook 程式與結果閱讀版](programs/outputs/html/index.html)：02–25 共 265 個程式格已在新的 Jupyter 核心以 `fast` 模式執行通過；原 `.ipynb` 保持不變。
- [HTML 如何解讀與用於教學](programs/HTML_TEACHING_GUIDE.md)：閱讀順序、版本辨識與 20 分鐘閾值活動。

00–01 的 Notebook HTML 與既有全課程合併壓縮 PDF 仍是歷史快照；本次新版請使用上述各章入口。

一次輸出指定章節的兩種投影片格式，例如第 03、04 章：

```sh
python3 scripts/build_slides.py --pdf --html --weeks 3 4
```

## 後續八週：Ch.4–9

現有 **8 份 Marp、370 頁、24 小時**，建議接續為第 4–11 週。完整保留主教材 90 張編號圖，呈現 42 個編號公式的知識點與四張編號表；另整合舊稿的 SVM、PCA 推導、EM、XOR、反向傳播與配套程式實驗。

- [六至八週課程規劃](教學指引.md)：八週主方案與六週濃縮的指定頁次、休息及課後範圍。
- [學生活動單](課堂活動單.md)／[講者備註與答案](教學講者備註.md)。
- [Ch.4–9 來源對照](SOURCE_MAP.md)：逐頁來源、全部編號圖／公式／表格定位與內容釐清。

Marp 原稿位於 `slides/04_*.md` 至 `slides/11_*.md`。公式與表格可編輯，教材圖保留原圖並附中文解說。六週版需將進階推導與部分實作移至課外；完整授課建議採八週。

重新輸出新增教材：

```sh
python3 scripts/build_slides.py --pdf --extended
python3 scripts/extension_docs.py
python3 scripts/validate_extension.py
```

只重建特定週可用 `--pdf --extended --weeks 7 9`；只帶 `--pdf` 或 `--html` 時處理 00–03；完全不帶輸出參數時不產生檔案。

## 前三週投影片

| 檔案 | 頁數 | 教學時間 | 內容 |
|---|---:|---:|---|
| [00 課程導覽](slides/00_課程導覽.md) | 4 | 10 分鐘 | 教材定位、三週目標與閱讀方式 |
| [01 機器學習概觀](slides/01_機器學習概觀.md) | 36 | 150 分鐘 | ML 類型、資料特性、線性模型、正則化、驗證與泛化 |
| [02 端到端機器學習專案](slides/02_端到端機器學習專案.md) | 47 | 160 分鐘 | 房價資料、視覺化、前處理、迴歸誤差、CV 與模型選擇 |
| [03 分類與模型評估](slides/03_分類與模型評估.md) | 43 | 160 分鐘 | 線性分數銜接、MNIST、混淆矩陣、閾值、PR／ROC、多類別及錯誤分析 |

共 **130 頁、480 分鐘教學與活動**，另含每週兩次 10 分鐘休息，合計 **540 分鐘／九小時**。第一週先使用 00，再使用 01。時間為可調整的教學估計，無額外程式安裝時間。

- [課堂活動單](課堂活動單.md)：學生用題目與手算表格。
- [教學指引](教學指引.md)：分段進度、活動、學習產出與課後任務。
- [教學講者備註](教學講者備註.md)：每頁建議時間、提問、答案及常見誤解。
- [來源對照](SOURCE_MAP.md)：逐頁來源、PDF 印刷／檔案頁碼、舊 PPTX 頁次及修正說明。
- [圖片來源清單](slides/assets/sources.json)：原始內嵌圖片的精確定位。

## 線性模型推導與手算教材

- [04 線性模型與最佳化](slides/04_線性模型與最佳化.md)：52 頁，含簡單／多元迴歸、連鎖律、正規方程、同步梯度更新及延伸推導。
- [05 正則化與機率分類](slides/05_正則化與機率分類.md)：43 頁，補入 sigmoid、Bernoulli 概似、交叉熵梯度與 Logistic 手算。
- [手算工作單](materials/04_線性迴歸與梯度下降_手算工作單.md)／[教師解答](materials/04_線性迴歸與梯度下降_教師解答.md)：A–D 核心題約 28 分鐘，E–F 延伸題約 12 分鐘，含逐步解答與評分提示。

兩章各維持 180 分鐘安排；完整工作單可另作課後練習。新增公式來源與教學時間記錄在 Marp 講者註解，頁次以目前投影片為準。

## 配套教學程式

[programs/](programs/README.md) 提供 **26 本可獨立在 Colab 執行的 Jupyter Notebook**。每一本都與 `slides/00–25` 的 Marp 檔同名，投影片內也有純文字的對應檔名、精簡程式與實際輸出圖。內容固定參考 `handson-mlp` commit `47eba45…`，並整合 `MachineLearning2025` 的教學程式。

- `01–03`：把原本分散的 8 本基礎實作依投影片主線合併，保留生活滿意度、房價 Pipeline、Iris、ROC、MNIST 與評估陷阱。
- `04–11`：沿用已驗證的線性模型、樹與集成、降維、分群及 ANN 實作，檔名改為與投影片一致。
- `12–25`：新增 CPU 可快速重跑的短實驗，涵蓋梯度裁剪、最佳化、CNN、偵測、序列、attention、Transformer、生成、RL、自動微分與量化。大型 GPU 實驗仍以作者原 Notebook 作延伸閱讀。

既有成果可依 [操作說明](programs/README.md) 啟動 Jupyter；使用位置見 [Notebook／投影片對照](programs/TEACHING_MAP.md)，來源與修正見 [程式來源](programs/SOURCES.md)。未經明確要求，不因 Marp 投影片變動而自動抓取、產生或檢查程式。

## 開啟與編輯

使用 VS Code 的 Marp 預覽開啟 `slides/*.md`。工作區設定已登錄 [theme.css](slides/theme.css)，並開啟部分雙欄版面所需的 HTML。公式使用 KaTeX，表格使用 Markdown。十張圖以 SVG 保留可編輯內容，十八張圖由提供的 PDF／PPTX 擷取。

若顯示未知主題，確認已以本資料夾作為 VS Code 工作區，而非只開單一 Markdown 檔。

## 重新輸出

環境需要 Python 3、Marp CLI 與 Google Chrome。此處使用 Marp CLI 4.5.0／Marp Core 4.4.0。

```sh
python3 scripts/build_slides.py --pdf
python3 scripts/course_index.py
```

此命令必須明確帶入 `--pdf` 或 `--html`，避免在 Marp 尚未確認時誤產生檔案。Chrome 位於其他位置時，使用 `ML_COURSE_CHROME` 指定可執行檔。

重新產生可編輯 SVG：

```sh
python3 scripts/build_diagrams.py
```

重新擷取原教材圖片另需 PyMuPDF：

```sh
python3 scripts/extract_assets.py
```

修改後先檢視 Marp；僅在要求交付 PDF 時再執行輸出命令與版面確認。`scripts/validate_course.py` 檢查頁數、時間、圖片、SVG 與手算數字。

## 教學資料的解讀

頁尾的 `p.` 指主教材印刷頁，`s.` 指舊投影片頁次。教材與舊稿報告值、自編示意數值均分開標示，未將擷取圖表或書中成效宣稱為本次重新執行的實驗。正則化、梯度下降與邏輯斯迴歸只補充必要概念，完整推導依主教材安排在後續 Ch.4。

## 第三方程式授權與來源

`programs/upstream/handson-mlp/` 保存自 [ageron/handson-mlp](https://github.com/ageron/handson-mlp) 的原始 Notebook 快照（Apache License 2.0）；其完整授權文字位於 [`programs/upstream/handson-mlp/LICENSE`](programs/upstream/handson-mlp/LICENSE)。來源版本、逐本改編對照與重用時的授權注意事項見 [`programs/SOURCES.md`](programs/SOURCES.md) 與 [`programs/THIRD_PARTY_NOTICES.md`](programs/THIRD_PARTY_NOTICES.md)。原始快照與課程改編 Notebook 應分開辨識；教材中其他來源的授權須各自核對。

`programs/notebooks/` 26 本教學 Notebook 現已逐檔補上授權與來源說明；僅作者自編及具有再授權權利的程式與文字採 [`programs/LICENSE`](programs/LICENSE) 的 Apache License 2.0。作者自有的 [`MachineLearning2025`](https://github.com/leonjyentub/MachineLearning2025) 已補設根目錄 LICENSE；原始快照與第三方資產仍依其各自權利處理。詳見 [`programs/NOTICE.md`](programs/NOTICE.md) 與 [`programs/THIRD_PARTY_NOTICES.md`](programs/THIRD_PARTY_NOTICES.md)。


---

## 第 12～19 章教材導覽（原投影片資料夾說明）

第 12～19 章與附錄 A、B：教學投影片

接續既有 `12_`、`13_`（書本第 11 章）教材。**檔名前綴是課程順序，不等於書本章號。**

所有投影片使用繁體中文、16:9 與既有 `ml-course` 主題，文字、表格、公式、程式皆保留可編輯格式。以 VS Code 的 Marp Preview 開啟下列 `.md` 檔；目前 PDF／HTML 可由上方匯出入口開啟。

| 課程序號 | 書本 | 教材 | 頁數 | 建議時間 |
| --- | --- | --- | --- | --- |
| 14 | Ch.12 | `14_卷積神經網路_影像特徵與架構` | 38 | 180 分 |
| 15 | Ch.12 | `15_電腦視覺_遷移學習與偵測分割` | 30 | 180 分 |
| 16 | Ch.13 | `16_序列模型_RNN與時間序列預測` | 36 | 180 分 |
| 17 | Ch.14 | `17_自然語言處理_詞嵌入與注意力` | 37 | 180 分 |
| 18 | Ch.15 | `18_Transformer_注意力架構與預訓練` | 32 | 180 分 |
| 19 | Ch.15 | `19_大型語言模型_生成與聊天系統` | 30 | 180 分 |
| 20 | Ch.16 | `20_視覺與多模態Transformer` | 37 | 180 分 |
| 21 | Ch.17 | `21_Transformer加速_推論與參數高效微調` | 38 | 180 分 |
| 22 | Ch.18 | `22_生成模型_自編碼器GAN與擴散` | 47 | 240 分 |
| 23 | Ch.19 | `23_強化學習_策略價值與深度RL` | 43 | 240 分 |
| 24 | 附錄A | `24_附錄A_自動微分與計算圖` | 21 | 90 分 |
| 25 | 附錄B | `25_附錄B_混合精度與量化` | 28 | 120 分 |

合計 **12 份、417 頁**。時間含活動與休息，完整安排約 35.5 小時；第 18、19 章各可分兩次上課。進階模型比較與大型訓練可安排選讀。

## 來源與編排

- 主線以 `book/` 第 12～19 章為序，另補齊書中附錄 A、B；Index 是查找索引，不另編為授課單元。
- 本地第 17 章只有兩頁導讀；本份另參考作者公開的 [完整第 17 章](https://ageron.github.io/homlp/HOMLP_Chapter_17.pdf)，並清楚區分線上版 PDF 頁碼。
- `source_pptx/` 依內容補強 CNN、RNN、POS、attention、圖片描述、LLM 與 Q-learning；同主題重複檔案不決定課程順序。
- MachineLearning2025 的本地程式用於 MLP、PCA、SVD、手刻反向傳播等適合的對照。後續架構以作者相應章節 Notebook 作實作來源。
- [來源與章節對照](slides/assets/chapters12_19/SOURCE_MAP.md) 列出閱讀範圍、程式位置與原圖來源。每張投影片的註解另含來源、講者提示或活動答案。

## 程式如何使用

每份 `slides/12–25` 都有同名的 `programs/notebooks/12–25` 配套檔。投影片前段的「程式實驗與實際輸出」可離線快速重跑；較長的模型片段仍用於讀碼，並以純文字標示作者 Notebook 檔名與指定區段。Cell 編號從 **0** 起算。

作者 Notebook 的核對版本固定於 `47eba45aacc85feae51ba7db68dd1ca66cb25e0a`，避免課堂定位隨主分支變動。先閱讀每本 Notebook 的 Setup，再依課程指定區段執行。部分章節的作者習題解答仍標為 Work in progress，本課活動不依賴未完成的解答。

- 張量尺寸、手算與 autograd 小例子適合課堂練習。
- 預訓練視覺或文字模型通常需首次下載權重及資料。
- LLM 微調、BLIP-2、擴散、Atari 等完整實驗可需 GPU、較大記憶體與較長執行時間；課堂可先讀程式與分析作者結果。
- 本次已執行本地 CPU 短實驗並保存輸出；未執行作者完整 GPU／大型模型訓練。書中結果、作者結果、本地實際輸出與自編數例均分開標示。

## 教學銜接

各份依序提供學習成果、觀念與原圖、公式或程式導讀、課堂活動、離堂檢核。附錄 A 可在學生需要理解梯度時提早使用；附錄 B 可接在加速與 LoRA 之後。

本批主線涵蓋各章主要小節，並將分支架構放入比較表或選讀。長篇證明、完整模型訓練與作者所有課後習題仍以原書及 Notebook 作延伸。


---

## 第 02–04 章投影片與 Notebook 對照

[逐圖與逐程式格對照](programs/SLIDE_NOTEBOOK_MAP_02_04.md) 列出三章 45 個圖檔引用的對應程式，並區分教材原圖、同概念重做與相同數值驗算。三份 Notebook 共 80 個程式格，新增末尾導讀頁供程式課或課後閱讀；原核心教學時段不變。本次更新 Marp、Notebook 與程式輸出圖；2026-10-04 已另行同步 PDF／HTML。

## 2026-09-28 Notebook 獨立執行檢查

26 本 Notebook 已在專案外的暫存目錄中，各自以全新 Python 核心由第一格執行到底。測試使用本機交付的三份資料檔，沒有在真正的 Google Colab GPU 環境執行，也沒有測試首次從網路下載資料。第 02 本儲存的 `housing_pipeline.pkl` 已在另一個 Python 行程載入並完成預測。26 份投影片的同名 Notebook 路徑均為純文字，且檔案存在。

## 歷史驗證紀錄（2026-09-22，本機舊版）

本次執行與驗證紀錄

驗證日期：2026-09-22。環境：macOS arm64、Python 3.12.10、NumPy 2.3.3、pandas 2.3.3、scikit-learn 1.7.2。模式為 `fast`，每一本 Notebook 都在新的本機核心由第一格執行到底並保存輸出。

## 執行結果

| 範圍 | Notebook | Code cells | 結果 |
|---|---:|---:|---|
| 00 | 1 | 4 | PASS |
| 01–03 合併主線 | 3 | 63 | PASS |
| 04–11 傳統 ML | 8 | 66 | PASS |
| 12–25 CPU 短實驗 | 14 | 42 | PASS |
| **總計** | **26** | **175** | **零執行錯誤** |

合併後的 01–03 分別包含 22、18、23 個 code cells；執行時間約 4.43、14.37、24.12 秒。04–11 每本約 2.2–14.0 秒；12–25 每本約 0.9–1.7 秒。時間包含核心啟動與 HTML 輸出，會隨硬體與快取改變。

## 新增實驗的實際結果摘錄

- 12：梯度 `[3,4,12]` 的範數由 13 裁剪為 5；十層 sigmoid 導數上界連乘約 `9.54e-7`。
- 13：同一狹長二次損失面上，80 步後 GD loss `2.87e-2`，Momentum loss `7.74e-7`。
- 14：2D 互相關輸出 `[[0,-1],[-1,1]]`，與投影片手算一致。
- 15：前兩框 IoU `0.716`，NMS 保留框 0 與 2。
- 16：12 點視窗 RMSE `0.120`，persistence 基準 `0.142`。
- 18：causal mask 後未來注意力總量為 `0`。
- 21：`d=4096, r=8` 時 LoRA 參數 65,536，為完整矩陣 16,777,216 的 `0.391%`。
- 22：digits 壓到 12 維後平均重建 MSE `0.0158`。
- 23：300 次 bandit 互動後，兩臂估計值約 `0.156／0.805`，較佳臂被選 279 次。
- 25：對稱 int8 量化 scale `0.00945`，最大反量化絕對誤差 `0.00465`。

完整數據見 `programs/outputs/reports/*.json`；逐本時間見 `programs/outputs/execution.json`。這些數值是縮編教學實驗，不與原書完整模型或不同硬體設定直接比較。

## 驗證項目

- 26 個 Notebook stem 與 26 個編號 Marp stem 完全一致。
- 175 個 code cells 可解析、execution count 連續且沒有 error output。
- 每份投影片都有可解析的同名 Notebook 連結；01–25 各有一張實際輸出頁。
- 72 組 PNG／SVG 結構有效，12–25 的新增圖均由對應 Notebook 產生。
- 44 個上游快照與 3 組本機資料的 SHA-256 符合 manifest。
- HTML 閱讀版與索引已更新為 26 本；舊檔名不再出現在索引。
- `pytest`、`programs/scripts/validate_deliverables.py` 與 `scripts/validate_course.py` 已通過。
- 26 份 Marp 已轉為暫存 HTML；01–25 的第 3 頁均無溢出、破圖、KaTeX 錯誤或裸露 Markdown。
- 另人工檢視 01、03、12、18、21、25 的第 3 頁截圖，程式、觀察文字與實際輸出圖的雙欄配置可讀。

## 結論界線

12–25 的 NumPy／scikit-learn 小例用於解釋機制，不等於完成 PyTorch／Hugging Face 的大型訓練。模型保存只示範本機載入與原始欄位推論，未建置外部服務。修改資料、套件或模式後，必須重新執行並以新的 Notebook／JSON 輸出更新本紀錄。
