# 碩士班機器學習：Marp 教學教材

依 `book/` 的主教材順序編製，以 `source_pptx/` 的相關概念、圖表及案例補充。採繁體中文、16:9 Marp 格式。原始 PDF 與 PPTX 保持原樣。目前包含 `slides/00–25` 的完整課程與附錄。

## 編修與產出約定

`slides/` 的 Marp 檔是唯一的日常編修對象。新增或修改投影片時，先只處理 Marp 原稿與必要的原始碼語法檢查；**不產生 HTML、PDF 或 `programs/` 教學範例程式**。PDF 僅在教師檢視、修正 Marp 並明確要求後才輸出；`programs/` 的抓取、產生與正確性檢查也同樣必須另行明確要求。先前投影片的 HTML 產物已移除。

## 後續八週：Ch.4–9

現有 **8 份 Marp、344 頁、24 小時**，建議接續為第 4–11 週。完整保留主教材 90 張編號圖，呈現 42 個編號公式的知識點與四張編號表；另整合舊稿的 SVM、PCA 推導、EM、XOR、反向傳播與配套程式實驗。

- [六至八週課程規劃](後續課程_6至8週規劃.md)：八週主方案與六週濃縮的指定頁次、休息及課後範圍。
- [學生活動單](後續課程_活動單.md)／[講者備註與答案](後續課程_講者備註.md)。
- [Ch.4–9 來源對照](SOURCE_MAP_CH04_09.md)：逐頁來源、全部編號圖／公式／表格定位與內容釐清。

Marp 原稿位於 `slides/04_*.md` 至 `slides/11_*.md`。公式與表格可編輯，教材圖保留原圖並附中文解說。六週版需將進階推導與部分實作移至課外；完整授課建議採八週。

重新輸出新增教材：

```sh
python3 scripts/build_slides.py --pdf --extended
python3 scripts/extension_docs.py
python3 scripts/validate_extension.py
```

只重建特定週可用 `--pdf --extended --weeks 7 9`；原本不帶參數的輸出命令仍只處理前三週。

## 前三週投影片

| 檔案 | 頁數 | 教學時間 | 內容 |
|---|---:|---:|---|
| [00 課程導覽](slides/00_課程導覽.md) | 4 | 10 分鐘 | 教材定位、三週目標與閱讀方式 |
| [01 機器學習概觀](slides/01_機器學習概觀.md) | 36 | 150 分鐘 | ML 類型、資料特性、線性模型、正則化、驗證與泛化 |
| [02 端到端機器學習專案](slides/02_端到端機器學習專案.md) | 43 | 160 分鐘 | 房價資料、視覺化、前處理、迴歸誤差、CV 與模型選擇 |
| [03 分類與模型評估](slides/03_分類與模型評估.md) | 39 | 160 分鐘 | MNIST、混淆矩陣、閾值、PR／ROC、多類別及錯誤分析 |

共 **122 頁、480 分鐘教學與活動**，另含每週兩次 10 分鐘休息，合計 **540 分鐘／九小時**。第一週先使用 00，再使用 01。時間為可調整的教學估計，無額外程式安裝時間。

- [課堂活動單](課堂活動單.md)：學生用題目與手算表格。
- [教學指引](教學指引.md)：分段進度、活動、學習產出與課後任務。
- [教學講者備註](教學講者備註.md)：每頁建議時間、提問、答案及常見誤解。
- [來源對照](SOURCE_MAP.md)：逐頁來源、PDF 印刷／檔案頁碼、舊 PPTX 頁次及修正說明。
- [圖片來源清單](slides/assets/sources.json)：原始內嵌圖片的精確定位。

## 配套教學程式

[programs/](programs/README.md) 提供 **26 本已執行的 Jupyter Notebook**。每一本都與 `slides/00–25` 的 Marp 檔同名，投影片內也有可點擊的對應路徑、精簡程式與實際輸出圖。內容固定參考 `handson-mlp` commit `47eba45…`，並整合 `MachineLearning2025` 的教學程式。

- `01–03`：把原本分散的 8 本基礎實作依投影片主線合併，保留生活滿意度、房價 Pipeline、Iris、ROC、MNIST 與評估陷阱。
- `04–11`：沿用已驗證的線性模型、樹與集成、降維、分群及 ANN 實作，檔名改為與投影片一致。
- `12–25`：新增 CPU 可快速重跑的短實驗，涵蓋梯度裁剪、最佳化、CNN、偵測、序列、attention、Transformer、生成、RL、自動微分與量化。大型 GPU 實驗仍連回作者原 Notebook。

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

此命令必須明確帶入 `--pdf`，避免在 Marp 尚未確認時誤產生 PDF。Chrome 位於其他位置時，使用 `ML_COURSE_CHROME` 指定可執行檔。

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
