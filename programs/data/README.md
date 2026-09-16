# 資料來源

| 本機檔案 | 固定來源 | 用途 |
|---|---|---|
| `lifesat.csv` | `ageron/data` commit `9e29abbbea6a3ff7250dea64c43c1d6c723095d7`，`lifesat/lifesat.csv` | 原教材的歷史 GDP／生活滿意度教學例 |
| `housing.csv` | 相同 commit 的 `housing.tgz` 中 `housing/housing.csv` | 20,640 個 California Housing 區域 |
| `mnist_784_v1.npz` | [OpenML dataset 554](https://www.openml.org/d/554)，`mnist_784` version 1 | 70,000×784 像素、0–9 數字標籤 |

固定 URL 與每個本機檔案的 SHA-256 見 [manifest.json](manifest.json)。Housing 只從壓縮檔讀出指定 CSV，沒有將整個 tar 解壓到檔案系統。MNIST 保存為 uint8 的壓縮 NumPy 陣列；Notebook 計算前依用途轉成 float32 或 int16，避免整數溢位。

生活滿意度資料來自主教材的 OECD／World Bank 歷史整理，住房亦是歷史資料；兩者均不能視為目前的官方指標或市價。資料的公開可得性與來源程式的授權是不同事項，外部再散布請保留並核對各原始資料的條件。

`openml_cache/` 是 scikit-learn 下載快取。課堂執行只需表內三個檔案與 manifest；安裝好套件後不需要網路。
