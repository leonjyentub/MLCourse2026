"""Generate traceability tables and readable speaker notes from canonical Marp sources."""
from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parents[1]
def slides(p):
 text=p.read_text();text=re.sub(r'^---\n.*?\n---\n','',text,count=1,flags=re.S)
 return re.split(r'\n---\s*\n',text)
source_intro='''# 教材與素材來源對照

主要教材：Aurélien Géron，*Hands-On Machine Learning with Scikit-Learn and PyTorch*，使用本資料夾提供的版本。以下頁碼均指檔案中的印刷頁碼，並非沿用其他版本。

| 縮寫 | 原始檔案 | 頁碼換算 |
|---|---|---|
| TOC | [00_Table of Contents.pdf](book/00_Table%20of%20Contents.pdf) | 印刷 v–vii 為 PDF 第 7–9 頁 |
| B1 | [CHAPTER 01 The Machine Learning Landscape.pdf](book/CHAPTER%2001%20The%20Machine%20Learning%20Landscape.pdf) | 印刷 p.3–39 對應 PDF 第 3–39 頁 |
| B2 | [CHAPTER 02 End-to-End Machine Learning Project.pdf](book/CHAPTER%2002%20End-to-End%20Machine%20Learning%20Project.pdf) | PDF 頁 = 印刷頁 − 40 |
| B3 | [CHAPTER 03 Classification.pdf](book/CHAPTER%2003%20Classification.pdf) | PDF 頁 = 印刷頁 − 106 |
| P0 | [00_Machine Learning.pptx](source_pptx/00_Machine%20Learning.pptx) | s. 指投影片順序，從 1 起算 |
| P1 | [01_Regressions.pptx](source_pptx/01_Regressions.pptx) | 同上 |
| P2 | [02_Validation and Regularization.pptx](source_pptx/02_Validation%20and%20Regularization.pptx) | 同上 |

B1–B3 為章節主線；P0–P2 作概念、表格及圖片補充。每頁頁尾標示來源，講者備註補充解讀限制。自編算例皆明確標示，教材數字未宣稱為本次執行結果。

'''
sm=[source_intro];notes=['# 三週教學講者備註\n\n由 Marp 原始檔的備註彙整。直接修改投影片後，可執行 `python3 scripts/course_index.py` 更新本檔。時間含討論、計算與回饋，不含休息。\n'];records=[]
for p in sorted((ROOT/'slides').glob('0[0-3]_*.md')):
 blocks=slides(p);sm+=['\n## '+p.stem+'\n\n| 頁 | 標題 | 分鐘 | 主來源及補充 |\n|---:|---|---:|---|\n'];notes+=['\n## '+p.stem+'\n'];cum=0
 for i,b in enumerate(blocks,1):
  heading=re.search(r'^#{1,2} (.+)',b,re.M).group(1);meta=re.search(r'<!-- meta: (.*?) -->',b,re.S).group(1);m=int(re.search(r'minutes=(\d+)',meta).group(1));ref=re.sub(r'^minutes=\d+; ','',meta).replace('source=','').replace('supplement=','補充：');cum+=m
  sm.append(f'| {i} | {heading} | {m} | {ref} |\n')
  speaker=re.search(r'<!-- 講者提示：(.*?) -->',b,re.S)
  notes.append(f'\n### {i:02}　{heading}\n\n{m} 分鐘，本檔累計 {cum} 分鐘。來源：{ref}。\n\n'+(speaker.group(1).strip() if speaker else '')+'\n')
  records.append(dict(deck=p.stem,slide=i,title=heading,minutes=m,cumulative=cum,source=ref))
 sm.append(f'\n共 {len(blocks)} 頁，{cum} 分鐘。\n')
sm.append('\n## 原始圖片來源\n\n| 素材 | 原始檔 | 定位 | 處理方式 |\n|---|---|---|---|\n')
for a in json.loads((ROOT/'slides/assets/sources.json').read_text()):
 pos=f'印刷 p.{a["printed_page"]} / PDF 第 {a["pdf_page"]} 頁 / 圖 {a["figure"]}' if 'figure' in a else f'投影片 {a["slide"]} / {a["media"]}'
 sm.append(f'| {Path(a["asset"]).name} | {Path(a["source"]).name} | {pos} | {a["method"]} |\n')
sm.append('''
## 重繪圖與公式

| SVG | 對應內容與性質 |
|---|---|
| rules_learning.svg | B1 圖 1-1–1-4 的規則／學習流程，概念改繪 |
| reinforcement.svg | B1 圖 1-12 的互動迴圈，概念改繪 |
| residuals.svg | B1 損失概念與 P1 s.4 的自編誤差示意 |
| data_split.svg | B1 p.35–36 與 P2 s.3 的分工，比例為自編 |
| early_stopping.svg | P2 s.9 的早停概念，自編示意曲線 |
| project_flow.svg | B2 p.41–43 的八階段流程摘要 |
| preprocessing.svg | B2 p.86–90 的 Pipeline 概念改繪 |
| cross_validation.svg | B2 圖 2-20、P2 s.5–6，改為 5 折示意 |
| sigmoid.svg | P1 s.27 的邏輯斯函數，依公式重繪 |
| toy_roc_pr.svg | B3 PR／ROC 概念，採自編八筆分數計算，非教材實驗 |

公式以 KaTeX／LaTeX 保存於 Marp 原始檔，表格使用 Markdown。自編八筆分數與所有閾值計算另存 `slides/assets/toy_thresholds.json`。SVG 產生方式保存在 `scripts/build_diagrams.py`。

## 素材取捨與必要修正

- P0 的學習類型與監督式案例融入 Ch.1；不使用未清楚對應課程的裝飾圖片及漫畫。
- P0 s.13 的「不需給機器任何資料」改為互動軌跡提供資料。P0 s.11 的非監督學習不再描述成無法評估正確性。
- P1 s.2–4、8–14 補充線性模型、損失與梯度下降直覺；大段微分推導、優化器實作與完整程式碼留待 Ch.4。
- P1 s.23 與 P2 s.10 混用的 normalization／regularization 分別統一為特徵縮放／正規化與正則化。
- P1 s.25–40 簡化為邏輯斯函數與二元交叉熵。教學計算統一採自然對數，不照抄底數混雜的熵數字。
- P1 s.42 的 Iris 圖用於散布矩陣；s.48 的二類機率背景圖用於決策邊界。P1 s.49 的 100% 分類結果沒有推廣為一般成效。
- P1 s.50 原矩陣軸向與教材相反，本次統一為真實類別在列、預測類別在欄，負類在前。
- P1 s.55–59 的 ROC 概念重整；使用可手算的八筆資料與完整端點，而不複製缺少完整端點的舊程式。
- P1 s.64「整數或文字標籤不能使用」修正為依介面接受標籤索引或獨熱表示。
- P2 s.8 圖與 RMSE 表保留並標明教材單次示例。P2 s.11 幾何圖保留，更早的圖源在該頁未交代，不虛構外部歸屬。
- P2 s.14 的單次 Lasso／Ridge 成效不作普遍優劣結論，改用公式、幾何與可驗算的懲罰算例說明。
- 主教材 Ch.3 示範的前處理，在本課程統一要求每折內重新擬合，避免學生把全資料縮放後交叉驗證當成標準流程。

## 範圍與順序

依目錄、Ch.1、Ch.2、Ch.3 順序分檔。Ch.1 保留學習類型、資料挑戰、正則化、測試驗證與分布不一致的順序；Ch.2 依問題定義、取資料、探索、準備、選模、調參、測試、部署；Ch.3 依 MNIST、二元分類、評估、閾值、ROC、多類別、錯誤分析、多標籤、多輸出。

補充素材插入相關概念當下，均標示補充，不另開與主教材平行的重複主線。Colab 操作、自訂 Transformer 類別、完整搜尋程式、ClassifierChain 實作與教材程式習題僅概述或列為後續閱讀，以符合三週概念導向的教學時間。
'''.replace('旧','舊').replace('补充','補充'))
def write_base_with_extension(path, base, marker):
 old=path.read_text() if path.exists() else ''
 extension=('\n\n---\n\n'+marker+old.split(marker,1)[1]) if marker in old else ''
 path.write_text(base.rstrip()+'\n'+extension)
write_base_with_extension(ROOT/'SOURCE_MAP.md',''.join(sm),'<!-- extension-source-map -->')
write_base_with_extension(ROOT/'教學講者備註.md',''.join(notes),'<!-- extension-notes -->')
(ROOT/'.build').mkdir(exist_ok=True)
(ROOT/'.build/course_index.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Indexed',len(records),'slides;',sum(x['minutes'] for x in records),'teaching minutes')
