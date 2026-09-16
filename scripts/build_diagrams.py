"""Editable SVG diagrams. Coordinates and teaching numbers are explicit and reproducible."""
from pathlib import Path
from html import escape
import math, json
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'slides/assets'
NAVY='#153e56';TEAL='#147d81';GOLD='#d18a32';GRAY='#687a86';LIGHT='#e6f0ed';RED='#bd4a3c'
def t(x,y,txt,size=24,color=NAVY,anchor='middle',weight='normal'):
 return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" text-anchor="{anchor}" font-weight="{weight}">{escape(txt)}</text>'
def rect(x,y,w,h,fill=LIGHT,stroke='none'):
 return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{fill}" stroke="{stroke}"/>'
def line(x1,y1,x2,y2,color=GRAY,width=2,dash=None,arrow=False):
 return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+(' marker-end="url(#arrow)"' if arrow else '')+'/>'
def poly(points,color=TEAL,width=3,dash=None):
 return '<polyline points="'+' '.join(f'{x:.2f},{y:.2f}' for x,y in points)+f'" fill="none" stroke="{color}" stroke-width="{width}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def dot(x,y,color=TEAL,r=5):return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{color}"/>'
def save(name,w,h,body,desc):
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img"><title>{escape(desc)}</title><defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="{GRAY}"/></marker></defs><g font-family="Noto Sans CJK TC, PingFang TC, Microsoft JhengHei, sans-serif">{body}</g></svg>'''
 (OUT/(name+'.svg')).write_text(svg)
# Comparison process
b=''
for y,label,items in [(40,'規則程式',['資料 + 人寫規則','程式執行','預測結果']),(180,'機器學習',['資料 + 已知答案','訓練演算法','學到的模型'])]:
 b+=t(100,y+44,label,25,TEAL,weight='bold')
 for i,txt in enumerate(items):
  x=230+i*285;b+=rect(x,y,240,82)+t(x+120,y+49,txt,25)
  if i<2:b+=line(x+247,y+41,x+274,y+41,arrow=True)
b+=t(720,310,'學到的模型再接收新資料，產生預測',24)
save('rules_learning',1100,330,b,'規則程式與資料學習的流程比較；依主教材圖1-1至1-4改繪')
# RL
b=rect(80,65,260,100)+t(210,125,'代理人／策略',29)+rect(660,65,260,100)+t(790,125,'環境',29)
b+=line(350,90,650,90,arrow=True)+t(500,64,'行動',24)
b+=line(650,145,350,145,arrow=True)+t(500,187,'新狀態 + 獎勵',24)
b+=t(500,245,'互動產生學習資料，策略影響後續取得的經驗',23,GRAY)
save('reinforcement',1000,270,b,'強化學習的代理人與環境互動；依主教材圖1-12改繪')
# residual toy plot
b=line(65,265,495,265,arrow=True)+line(65,265,65,25,arrow=True)+t(490,300,'x',24)+t(28,35,'y',24)
fx=lambda x:75+x*65;fy=lambda y:255-y*32
b+=line(fx(0),fy(1),fx(6),fy(5.2),TEAL,3)
for x,y in [(1,2.9),(2,1.7),(3,4.1),(4,3.0),(5,5.5)]:
 pred=1+.7*x;b+=line(fx(x),fy(y),fx(x),fy(pred),GOLD,3,'6 4')+dot(fx(x),fy(y),NAVY,6)
b+=t(265,32,'誤差 = 預測 − 真值',22)+t(410,238,'預測直線',21,TEAL)
save('residuals',530,320,b,'自編線性預測與垂直誤差示意')
# split
b=''
for x,w,col,txt,sub in [(20,636,TEAL,'訓練 60%','學習參數'),(656,212,GOLD,'驗證 20%','挑選設定'),(868,212,NAVY,'測試 20%','最終評估')]:
 b+=rect(x,45,w,90,col)+t(x+w/2,99,txt,28,'white',weight='bold')+t(x+w/2,180,sub,27)
b+=line(25,220,860,220,TEAL,3)+t(445,260,'開發階段可使用的資料',25,TEAL)+t(980,260,'先隔離',25,NAVY)
save('data_split',1100,290,b,'訓練驗證測試分工；60/20/20僅為課堂示例')
# project flow
b='';labels=['定義問題','取得資料','探索視覺化','準備資料','選擇與訓練','調整模型','最終測試','部署與監測']
for i,label in enumerate(labels):
 row=i//4;col=i%4;x=20+col*275;y=25+row*155
 b+=t(x+120,y+28,f'{i+1:02d}',23,TEAL,weight='bold')+rect(x,y+44,240,70)+t(x+120,y+87,label,27)
 if col<3:b+=line(x+246,y+80,x+267,y+80,arrow=True)
b+=t(550,332,'開發中的探索與調整可以迭代，最終測試須保留獨立性',23,GRAY)
save('project_flow',1100,355,b,'依主教材Ch2順序排列的八階段專案流程；由上列至下列閱讀')
# preprocessing
b=rect(20,112,155,76,NAVY)+t(98,158,'資料欄位',27,'white')
for y,lbl,txt in [(15,'數值欄','補值、縮放、特徵組合'),(210,'類別欄','補值、編碼')]:
 b+=line(185,150,220,150)+line(220,150,220,y+43)+line(220,y+43,260,y+43,arrow=True)
 b+=rect(270,y,415,88)+t(340,y+52,lbl,25,TEAL,weight='bold')+t(480,y+115,txt,23)
 b+=line(695,y+43,755,y+43)+line(755,y+43,755,150)
b+=line(755,150,795,150,arrow=True)+rect(805,112,125,76)+t(867,158,'合併',26)+line(940,150,965,150,arrow=True)+rect(977,112,115,76,NAVY)+t(1035,158,'模型',27,'white')
save('preprocessing',1110,345,b,'數值及類別分支前處理後合併並交給模型；依主教材Pipeline概念改繪')
# CV
b=t(520,26,'只在開發資料內分折',25,TEAL,weight='bold')+t(988,26,'獨立測試',24,NAVY)
for i in range(5):
 y=55+i*52;b+=t(77,y+30,f'第 {i+1} 折',23)
 for j in range(5):
  x=150+j*140;is_val=i==j;b+=rect(x,y,128,40,GOLD if is_val else LIGHT)+t(x+64,y+27,'驗證' if is_val else '訓練',22,'white' if is_val else NAVY)
 b+=rect(926,y,124,40,'#e4e9ef')+t(988,y+27,'不使用',22,GRAY)
b+=t(560,349,'每折重新估計：補值 + 編碼 + 縮放 + 模型',24)
save('cross_validation',1100,375,b,'五折交叉驗證，驗證輪替而外部測試始終隔離')
# sigmoid chart
b='';xl,yt,w,h=65,40,400,225
sx=lambda x:xl+(x+6)/12*w;sy=lambda p:yt+h-p*h
for v in [0,.5,1]:b+=line(xl,sy(v),xl+w,sy(v),'#d8e1e5',1)+t(xl-12,sy(v)+7,str(v),21,anchor='end')
b+=line(xl,yt+h,xl+w+15,yt+h,arrow=True)+line(xl,yt+h,xl,yt-15,arrow=True)
b+=poly([(sx(-6+i*.05),sy(1/(1+math.exp(6-i*.05)))) for i in range(241)],TEAL,4)
b+=line(sx(0),yt+h,sx(0),sy(.5),GOLD,2,'5 4')+dot(sx(0),sy(.5),GOLD,6)
for v in [-6,0,6]:b+=t(sx(v),yt+h+30,str(v),22)
b+=t(490,yt+h+30,'z',24)+t(20,23,'p̂',24)+t(300,20,'σ(0) = 0.5',23,TEAL)
save('sigmoid',530,320,b,'邏輯斯函數，z=0時機率估計0.5；自編函數圖')
# early stopping (illustrative)
b='';sx=lambda x:100+x*43;sy=lambda y:300-y*250
b+=line(100,300,1000,300,arrow=True)+line(100,300,100,20,arrow=True)+t(1000,340,'訓練輪數',24,anchor='end')+t(100,22,'損失',24,anchor='end')
train=[.85*math.exp(-.22*x)+.10 for x in range(21)];val=[.65*math.exp(-.35*x)+.20+.0014*x*x for x in range(21)];best=min(range(21),key=lambda i:val[i])
b+=poly([(sx(x),sy(y)) for x,y in enumerate(train)],TEAL,4)+poly([(sx(x),sy(y)) for x,y in enumerate(val)],GOLD,4)
b+=line(sx(best),300,sx(best),sy(val[best]),GRAY,2,'7 5')+dot(sx(best),sy(val[best]),GOLD,7)+t(sx(best),336,'保留此時模型',23,GOLD)
b+=t(975,sy(train[-1])-13,'訓練',24,TEAL)+t(975,sy(val[-1])-13,'驗證',24,GOLD)+t(780,32,'示意曲線，非實驗結果',21,GRAY)
save('early_stopping',1050,365,b,'以驗證損失選停止時間的自編示意')
# exact 8-case ROC & PR
scores=[.95,.85,.8,.7,.6,.4,.3,.1];ys=[1,0,1,1,0,0,1,0];points=[]
for i in range(8):
 tp=sum(ys[:i+1]);fp=i+1-tp;points.append(dict(threshold=scores[i],tp=tp,fp=fp,fn=4-tp,tn=4-fp,precision=tp/(i+1),recall=tp/4,fpr=fp/4))
b=''
for side,title,xlab,ylab in [(0,'ROC','FPR','TPR'),(1,'Precision–Recall','Recall','Precision')]:
 left=85+side*550;top=50;width=420;height=270
 xx=lambda v:left+v*width;yy=lambda v:top+height-v*height
 b+=t(left+width/2,28,title,26,TEAL,weight='bold')
 for v in [0,.25,.5,.75,1]:b+=line(xx(v),top,xx(v),top+height,'#dce5e6',1)+line(left,yy(v),left+width,yy(v),'#dce5e6',1)+t(xx(v),top+height+30,str(v),19)+t(left-12,yy(v)+6,str(v),19,anchor='end')
 b+=line(left,top+height,left+width+12,top+height,arrow=True)+line(left,top+height,left,top-10,arrow=True)+t(left+width/2,top+height+65,xlab,23)+t(left-50,top-15,ylab,23,anchor='start')
 if side==0:
  b+=line(xx(0),yy(0),xx(1),yy(1),GRAY,2,'6 5');ps=[(0,0)]+[(q['fpr'],q['recall']) for q in points]
 else:
  b+=line(xx(0),yy(.5),xx(1),yy(.5),GRAY,2,'6 5');ps=[(q['recall'],q['precision']) for q in points]
 b+=poly([(xx(x),yy(y)) for x,y in ps],TEAL,3)
 for x,y in ps:b+=dot(xx(x),yy(y),TEAL,4)
 q=points[4];x,y=(q['fpr'],q['recall']) if side==0 else(q['recall'],q['precision']);b+=dot(xx(x),yy(y),GOLD,7)+t(xx(x)+8,yy(y)-18,'t = 0.5',21,GOLD,anchor='start')
b+=t(550,423,'橘點：TP 3、FP 2、FN 1、TN 2（採 s ≥ 0.5）',24)
save('toy_roc_pr',1120,448,b,'同一組八筆自編資料的ROC及PR曲線，ROC AUC為0.6875')
(OUT/'toy_thresholds.json').write_text(json.dumps(points,ensure_ascii=False,indent=2)+'\n')
print('Generated 10 editable SVG diagrams')
