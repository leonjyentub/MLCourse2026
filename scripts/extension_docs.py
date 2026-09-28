"""Build navigation, source map, speaker notes, activities from canonical Marp files.
Run after editing slides 04–11. This does not rewrite the slide sources.
"""
from pathlib import Path
import re,json
ROOT=Path(__file__).resolve().parents[1]
def write_section(path, marker, generated, preserve_marker=None):
 text=path.read_text() if path.exists() else ''
 prefix=text.split(marker,1)[0].rstrip() if marker in text else text.rstrip()
 preserved=''
 if preserve_marker and preserve_marker in text:
  preserved='\n\n'+preserve_marker+text.split(preserve_marker,1)[1]
 path.write_text(prefix+'\n\n---\n\n'+marker+'\n\n'+generated.rstrip()+'\n'+preserved)
files=sorted(p for p in (ROOT/'slides').glob('*.md') if p.name[:2].isdigit() and 4<=int(p.name[:2])<=11)
D={}
for f in files:
 parts=re.split(r'^---\s*$',f.read_text(),flags=re.M)[2:]
 ss=[]
 for part in parts:
  if not part.strip():continue
  m=re.search(r'<!-- meta: minutes=(\d+); core6=(yes|no); block=(-?\d+); source=(.*?) -->',part)
  title=re.search(r'^#{1,2} (.+)$',part,re.M).group(1)
  note=re.search(r'<!-- 講者提示：(.*?) -->',part,re.S).group(1)
  body=re.sub(r'<!--.*?-->','',part,flags=re.S).strip();body=body.split('\n',1)[1].strip()
  ss.append(dict(title=title,minutes=int(m[1]),core=m[2]=='yes',block=int(m[3]),source=m[4],note=note,body=body))
 D[int(f.name[:2])]=dict(file=f,slides=ss,title=f.stem[3:])

def label(n):return f"{n:02d}《{D[n]['title']}》"
def link(n):return f"[{label(n)}](slides/{D[n]['file'].name})"
def ranges(seq):
 groups=[]
 for v in seq:
  if groups and groups[-1][-1]+1==v:groups[-1].append(v)
  else:groups.append([v])
 return '、'.join(str(g[0]) if len(g)==1 else f'{g[0]}–{g[-1]}' for g in groups)

plan=['# Ch.4–9 後續課程：六至八週規劃','',
'建議採 **八週、每週三小時，共 24 小時**。內容包括概念、數學、圖表閱讀、手算、程式示範與討論。接續原有三週後，整體為十一週、33 小時。若壓縮為六週（18 小時），須將較長推導、部分應用與程式延伸改成課前／課後，不能只加快播放速度。','',
'前提：學生已完成前面三週的資料切分、Pipeline、驗證與評估；能讀 Python 陣列、內積、平均與平方。微分與線性代數在本教材逐步引入。**無此先備時，八週也需增加預備課或降低推導深度。**','',
'## 八週完整方案','', '| 接續週次 | Marp | 頁數 | 主教材 | 可檢核產出 |','|---|---|---:|---|---|']
chapters={4:'Ch.4 pp.135–158',5:'Ch.4 pp.159–178',6:'Ch.5 pp.179–194',7:'Ch.6 pp.195–220',8:'Ch.7 pp.221–244',9:'Ch.8 pp.245–264',10:'Ch.8 pp.265–282',11:'Ch.9 pp.285–315'}
products={4:'手算梯度與學習曲線診斷',5:'正則化比較、閾值與 Softmax',6:'樹路徑、分割計算與模型比較',7:'單樹／森林／提升樹比較',8:'壓縮率、重建與分類比較',9:'群數證據與代表樣本分析',10:'密度、EM、異常與模型選擇',11:'前向／反向手算與 MLP 比較'}
for n,d in D.items():plan.append(f"| 第 {n} 週 | {link(n)} | {len(d['slides'])} | {chapters[n]} | {products[n]} |")
plan+=['',f"共 **{sum(len(d['slides']) for d in D.values())} 頁**。每週安排 50 分鐘教學、10 分鐘休息、60 分鐘教學、10 分鐘休息、50 分鐘教學；每頁分鐘數與講者提示均保留在 Marp 註解。時間是可調整教學估計，含活動但不含安裝環境或大型資料下載。",'',
'每週可在最後活動前依學習情況停下，將 `core6=no` 的推導延伸留作課後。這個標記表示進階閱讀層，不等於六週版完整排程；六週版以以下指定頁次為準。','',
'## 六週濃縮方案','',
'六週版保留六章主線與基本活動，但縮短練習輪數。每週仍有兩次完整休息；每週另外安排約 60–90 分鐘課前／課後。完整圖表、公式與補充頁仍留在八份 Marp 中供查閱。','',
'頁次指 Marp／PDF 投影片頁碼，從封面起算；此方案不使用原檔的封面、時間表與休息頁，授課者依下面節奏切換兩份簡報。']
# Exact teaching segments for compressed course; each week has 50+60+50 teaching minutes.
six=[('模型訓練、正則化與機率分類',[
 ('線性與梯度',[(4,[4,5,7,10,18,19,20,21,26])],50),
 ('多項式、正則化與早停',[(4,[32,34,35,36]),(5,[3,4,6,8,10,12,13,15,16])],60),
 ('機率分類與決策',[(5,[17,19,20,24,26,27,28,31,33])],50)],
 '課前重看線性模型與驗證；課後完成 04 的 SVD／複雜度、05 的次梯度與 API 尺度、分類程式實作。Softmax 只做一次小例子。'),
 ('決策樹',[
 ('規則與不純度',[(6,list(range(3,11)))],50),
 ('CART 與迴歸樹',[(6,list(range(12,23)))],60),
 ('穩定性與比較實作',[(6,[24,26,31,32,33])],50)],
 'SVM 的四頁補充（06 p.27–30）與 PCA 旋轉案例移課後；課堂比較 Logistic 與樹。'),
 ('集成學習',[
 ('投票、Bagging 與森林',[(7,list(range(3,14)))],50),
 ('Boosting',[(7,list(range(15,28)))],60),
 ('HGB、Stacking 與實作',[(7,[29,30,31,32,33,39,40])],50)],
 '表 6-1 的五頁案例表（07 p.34–38）作課前／課後對照；放大殘差圖逐列快速帶讀，不重複做三次完整計算。'),
 ('降維',[
 ('幾何與 PCA',[(8,list(range(3,13)))],50),
 ('PCA 計算與壓縮實作',[(8,[14,16,17,18,19,20,21,22,23])],60),
 ('隨機投影、流形與視覺化解讀',[(8,[25,28,31,32,34])],50)],
 '共變異拉格朗日推導、JL 維度界、稀疏投影細節、LLE 兩個最佳化式與 t-SNE KL 留課後；課堂仍說明各方法的目標與限制。'),
 ('分群與密度模型',[
 ('K-means 與選 k',[(9,[5,7,8,10,14,17,18,19,20,22,23])],50),
 ('DBSCAN 與 GMM／EM',[(10,[3,4,6,13,15,16,17,18])],60),
 ('異常、模型選擇與綜合討論',[(10,[23,24,25,28,29,30,32,35,36])],50)],
 '影像量化、距離表示、半監督／主動學習、其他分群演算法、似然／MAP 推導與 Bayesian GMM 移課後。EM 手算保留，程式搜尋縮成教師示範。'),
 ('人工神經網路',[
 ('神經元、XOR 與 MLP',[(11,list(range(6,14)))],50),
 ('非線性與反向傳播',[(11,[15,16,17,18,19,20,21,23])],60),
 ('架構、評估與小型實作',[(11,[25,26,27,28,29,30,31,32,34,36,37])],50)],
 '生物背景、矩陣反向遞迴、label smoothing／dropout／TensorBoard 與遷移學習留課後；保留手算與最小 MLP 比較。')]
for week,(title,segments,homework) in enumerate(six,1):
 plan+=['',f'### 濃縮第 {week} 週：{title}','', '| 實際時段 | 指定投影片 | 執行方式 |','|---|---|---|']
 for j,(name,sets,minutes) in enumerate(segments):
  refs='；'.join(f'{label(n)} p.{ranges(pages)}' for n,pages in sets)
  for n,pages in sets:
   assert all(1<=p<=len(D[n]['slides']) and D[n]['slides'][p-1]['block']!=-1 for p in pages),(n,pages)
  timer=['0–50 分','60–120 分','130–180 分'][j]
  plan.append(f'| {timer} | {refs} | {name} |')
  if j<2:plan.append(f'| {"50–60" if j==0 else "120–130"} 分 | 休息 | 保留 10 分鐘 |')
 plan+=['',homework]
plan+=['','## 教學與評量方式','','- 小組討論後，每人先獨立提交一題答案，避免只由熟悉程式的同學操作。','- 活動單與講者答案分開提供；每個程式活動皆有手算或文字設計替代。','- 建議配分：資料角色與流程 30%、數學／圖表解釋 30%、可查核產出 25%、限制與反思 15%。不以是否使用 GPU 或付費工具評分。','- 圖表中的 accuracy、RMSE、迭代次數均標明為教材例子；本次未把它們當作重新執行的實驗結果。','- 程式頁是教學片段，`X_train` 等變數需由前面資料準備流程提供；完整課堂操作可使用已備妥的小資料，避免課中臨時下載大型資料。','- 90 張教材編號圖以原圖保留；公式、表格、正文與講者提示可直接在 Marp 編輯。圖中英文標籤保留，中文解說在圖旁／圖下。','','## 相關檔案','','- [完整講者備註](教學講者備註.md)','- [學生課堂活動單](課堂活動單.md)','- [來源與完整性對照](SOURCE_MAP.md)']
write_section(ROOT/'教學指引.md','<!-- extension-plan -->','\n'.join(plan))
notes=['# 後續八週：講者備註與活動答案','','每頁分鐘數含講解或活動；每份合計 180 分鐘，包含兩次 10 分鐘休息。圖中教材結果非本班重跑結果。']
activities=['# 後續八週：學生課堂活動單','','姓名：＿＿＿＿　日期：＿＿＿＿　組別：＿＿＿＿','','先獨立完成一個小題，再與同組比較。允許計算機；沒有電腦時完成每題的手算或流程設計替代。答案與評分提示另見講者備註。']
source=['# Ch.4–9 來源與知識點對照','','主來源為使用者提供的六份 PDF；舊 PPTX 只補充主教材相關內容或明確標記的延伸。頁尾 p. 指書內印刷頁，PDF 頁另見下表；s. 指舊投影片頁。','','## PDF 定位','','| 主教材檔案 | PDF 頁數 | 印刷頁換算 |','|---|---:|---|']
for chapter,count,offset in [(4,44,134),(5,16,178),(6,26,194),(7,24,220),(8,38,244),(9,34,282)]:
 f=next((ROOT/'book').glob(f'CHAPTER {chapter:02d}*.pdf'))
 source.append(f'| [{f.name}](<book/{f.name}>) | {count} | 印刷頁 = PDF 頁 + {offset} |')
source+=['','Ch.9 PDF 第 1–2 頁為 Part II 扉頁／空白，章正文從 PDF 第 3 頁（p.285）開始；結尾空白不視為教學知識點。','','## 章節主線覆蓋','','| 章 | 已呈現的主要內容 | 對應 Marp |','|---|---|---|',
'| 4 | 線性／正規方程／SVD、三種 GD、多項式與學習曲線、Ridge／Lasso／Elastic Net、早停、Logistic／Softmax | 04、05 |',
'| 5 | 規則與機率、Gini／Entropy、CART、計算與正則化、迴歸樹、方向與變異 | 06 |',
'| 6 | 硬／軟投票、Bagging／Pasting、OOB、特徵抽樣、森林／Extra Trees、重要度、AdaBoost／GB／HGB、Stacking、完整方法表 | 07 |',
'| 7 | 維度災難、投影／流形、PCA／SVD、保留維度／重建、隨機／增量 PCA、隨機投影／JL、LLE 與其他降維 | 08 |',
'| 8 | K-means／初始化／加速／Mini-batch、inertia／silhouette／限制、影像與半監督／主動學習、DBSCAN／其他分群、GMM／EM／共變異、密度／異常／似然／AIC／BIC／Bayesian GMM／其他異常方法 | 09、10 |',
'| 9 | 生物／人工神經元、Perceptron／XOR／MLP、反向傳播與激活、迴歸／分類架構、sklearn MLP、Fashion MNIST／過度自信、容量／學習率／批次／最佳化 | 11 |','',
'## 舊投影片整合','','| PPTX | 採用內容與修正 |','|---|---|',
'| 01_Regressions | 梯度下降與 Logistic 推導脈絡；以主教材式號與符號為準 |',
'| 02_Validation and Regularization | 多項式、正則化與早停；補足最佳參數保存、驗證資料角色 |',
'| 03_SVM_DecistionTree_RandomForest | 樹不純度、剪枝、方向與變異、森林；SVM 明確放補充；更正把 Boosting 包在 Random Forest 之下的分類 |',
'| 04_DimensionReduction | 共變異／特徵值推導、SVD、LLE、t-SNE；修正 PCA 不等於刪原始欄位；LDA 是監督式 |',
'| 05_Clustering | silhouette、GMM／EM 公式、階層分群、DBSCAN；補充機率與密度、責任值差異 |',
'| 06_Artificial Neural Networks | XOR 真值與網路、鏈式法則、初始化、輸出設計；框架／dropout／TensorBoard 留延伸 |',
'| 00_Machine Learning | 已在前三週採用；本次不重複展開一般概論 |','',
'採內容整合與中文重寫；沒有把舊 PPTX 整頁截圖代替可編輯公式。精確頁次見各頁來源與以下逐頁對照。','',
'## 完整圖目錄（90 張編號圖）','','| 圖 | 原 PDF／印刷頁 | Marp 頁次 |','|---|---|---|']
figs=json.loads((ROOT/'slides/assets/chapters04_09/sources.json').read_text())
for f in figs:
 refs=[]
 for n,d in D.items():
  for i,s in enumerate(d['slides'],1):
   if f['asset'].split('/')[-1] in s['body']:refs.append(f'{n:02d} p.{i}')
 assert refs,f['figure']
 source.append(f"| {f['figure']} | PDF {f['pdf_page']}／p.{f['printed_page']} | {', '.join(refs)} |")
source+=['','圖 6-9 另提供三列的放大頁，完整原圖仍保留。所有圖保留坐標、圖例與必要文字；精確裁切範圍見 [圖像來源 JSON](slides/assets/chapters04_09/sources.json) 及 [放大圖 JSON](slides/assets/chapters04_09/detail_sources.json)。','','## 42 個編號公式與四張編號表','','公式與表格依知識點重排，有些公式合在同頁。原書公式常數與實作尺度有差異的地方已特別說明。','','| 主教材標識 | Marp 定位 |','|---|---|']
# Expand source references, including Chinese range marker and abbreviated final numbers.
for ch,end in [(4,24),(5,4),(6,4),(7,5),(8,2),(9,3)]:
 for k in range(1,end+1):
  refs=[]
  for n,d in D.items():
   for i,s in enumerate(d['slides'],1):
    if '式 ' not in s['source']:continue
    ids=set(re.findall(r'(?<!\d)([4-9]-\d+)',s['source'].split('式 ',1)[1]))
    for a,b in re.findall(r'([4-9]-\d+)～([4-9]-\d+)',s['source']):
     ca,ka=map(int,a.split('-'));cb,kb=map(int,b.split('-'))
     if ca==cb:ids.update(f'{ca}-{v}' for v in range(ka,kb+1))
    if f'{ch}-{k}' in ids:refs.append(f'{n:02d} p.{i}')
  assert refs,(ch,k)
  source.append(f'| 式 {ch}-{k} | {"、".join(refs)} |')
for table in ['4-1','6-1','9-1','9-2']:
 refs=[f'{n:02d} p.{i}' for n,d in D.items() for i,s in enumerate(d['slides'],1) if f'表 {table}' in s['source']]
 source.append(f'| 表 {table} | {"、".join(refs)} |')
source+=['','## 內容釐清與證據界線','','- 正規方程的反矩陣形式需滿欄秩；SVD／偽反矩陣補上秩不足情境。','- 線性 MSE 為凸函數，不能用一般非凸圖斷言它會卡局部最小值。','- Elastic Net 原式 4-13 與本機 scikit-learn 1.7.2 文件的 L2 樣本數尺度不同；保留兩者並提示不可直接共用 alpha。','- PCA 逆投影補回資料均值；LLE 補上避免所有點重合的限制。','- AdaBoost 採原書「只增加錯分權重」的二元慣例，不混入另一慣例的 1/2；多類 SAMME 的附加項在講者提示。','- GMM 責任值為後驗機率，score_samples 是對數密度；分位數閾值不是偵測正確率。','- Backprop 在本課狹義指計算梯度，optimizer 另行更新；明確指出教材有廣義用法。','- 一般網路架構表與 scikit-learn MLP 支援範圍分開；不將 Huber、自訂輸出激活或 dropout 冒稱為可直接設定。','- 書中百分比、RMSE、最適維度與迭代數都是原教材示例；自編手算數值另標示。','- 本次交付教學投影片與課程配套說明，未宣稱完成所有章末大型程式作業。','','## 逐頁來源、時間與教學用途']
for n,d in D.items():
 notes+=['',f"## {label(n)}",'']
 activities+=['',f"## {label(n)}",'']
 source+=['',f"### {label(n)}",'', '| 頁 | 分鐘 | 主題 | 來源 |','|---:|---:|---|---|']
 for i,s in enumerate(d['slides'],1):
  notes += [f"### p.{i}｜{s['title']}（{s['minutes']} 分鐘）",'',s['note'],'',f"來源：{s['source']}",'']
  source.append(f"| {i} | {s['minutes']} | {s['title']} | {s['source']} |")
  if s['block']>=0 and ('手算' in s['title'] or '實作' in s['title'] or s['title'].startswith(('診斷工作單','選模工作單','機率不是最後','同樣三個','算一次分割','先猜方向','迴歸葉節點'))):
   activities += [f"### p.{i}｜{s['title']}",'',s['body'],'','我的計算／流程與證據：','', '＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿','','我的限制與下一步：＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿','']
write_section(ROOT/'教學講者備註.md','<!-- extension-notes -->','\n'.join(notes))
write_section(ROOT/'課堂活動單.md','<!-- extension-activities -->','\n'.join(activities))
write_section(ROOT/'SOURCE_MAP.md','<!-- extension-source-map -->','\n'.join(source),
              '<!-- historical-review-06-11 -->')
print('產生六週指定頁次、講者備註、活動單與來源對照。')
