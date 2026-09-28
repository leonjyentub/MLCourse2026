"""Validate Ch.4–9 deliverables and independently check worked examples.
Requires PyMuPDF for PDF page verification; no network access.
"""
from pathlib import Path
import re,json,hashlib,math,ast
import fitz
ROOT=Path(__file__).resolve().parents[1]
report={'decks':[],'worked_examples':{},'input_integrity':[]}
files=sorted(p for p in (ROOT/'slides').glob('*.md') if p.name[:2].isdigit() and 4<=int(p.name[:2])<=11)
assert len(files)==8
all_text=''
for p in files:
 text=p.read_text();all_text+=text
 assert not any(ord(c)<32 and c!='\n' for c in text),f'Control character: {p.name}'
 slides=[s for s in re.split(r'^---\s*$',text,flags=re.M)[2:] if s.strip()]
 metas=[re.search(r'meta: minutes=(\d+); core6=(yes|no); block=(-?\d+);',s) for s in slides]
 assert all(metas),p.name
 duration=sum(int(m[1]) for m in metas);assert duration==180,(p.name,duration)
 for b,target in [(-1,20),(0,50),(1,60),(2,50)]:assert sum(int(m[1]) for m in metas if int(m[3])==b)==target
 assert all('講者提示：' in s and '_footer:' in s for s in slides)
 imgs=re.findall(r'!\[[^\]]*\]\(([^)]+)\)',text)
 for img in imgs:assert (p.parent/img).is_file(),img
 snippets=re.findall(r'```python\n(.*?)```',text,re.S)
 for code in snippets:ast.parse(code)
 pdf=ROOT/'output/pdf'/(p.stem+'.pdf');doc=fitz.open(pdf)
 assert len(doc)==len(slides),(pdf,len(doc),len(slides))
 for pg in doc:
  assert abs(pg.rect.width/pg.rect.height-16/9)<.001
  assert len(pg.get_text().strip())>10
 report['decks'].append({'file':str(p.relative_to(ROOT)),'slides':len(slides),'minutes':duration,'images':len(imgs),'python_snippets_parsed':len(snippets),'pdf_pages':len(doc)})
figures=json.loads((ROOT/'slides/assets/chapters04_09/sources.json').read_text())
assert len(figures)==90
for f in figures:assert f['asset'].split('/')[-1] in all_text
source_map=(ROOT/'SOURCE_MAP.md').read_text()
assert len(re.findall(r'^\| 式 [4-9]-\d+ \|',source_map,re.M))==42
assert len(re.findall(r'^\| 表 [4-9]-\d+ \|',source_map,re.M))==4
report['numbered_figures']=90;report['numbered_equations']=42;report['numbered_tables']=4
# Recompute examples, including a finite-difference check independent of symbolic derivatives.
def near(a,b,tol=1e-8):assert abs(a-b)<tol,(a,b)
# Linear gradient example: two rows [1,0],[1,1], theta=0, y=[1,3].
x=[[1,0],[1,1]];y=[1,3];res=[-v for v in y]
g=[sum(row[j]*r for row,r in zip(x,res)) for j in range(2)]
assert g==[-4,-3]
th=[-.1*v for v in g];pred=[sum(a*b for a,b in zip(row,th)) for row in x]
new_mse=sum((a-b)**2 for a,b in zip(pred,y))/2;near(new_mse,2.825)
report['worked_examples']['gradient_step']={'gradient':g,'theta':th,'mse_before':5,'mse_after':new_mse}
# Gini, entropy, weighted split, regression leaf.
probs=[.75,.25];near(1-sum(p*p for p in probs),.375)
ent=-sum(p*math.log2(p) for p in probs);near(ent,.8112781244591328)
weighted=5/8*(1-.2**2-.8**2);near(weighted,.2)
leaf=[sum((v-a)**2 for v in [1,2,6])/3 for a in [2,3,4]]
assert leaf[1]<leaf[0] and leaf[1]<leaf[2]
report['worked_examples']['tree']={'entropy_3_1':ent,'split_gini':weighted,'leaf_mse':leaf}
# Logistic confusion matrices.
def confusion(threshold):
 yy=[1,0,1,0];pp=[.8,.6,.4,.1];pred=[int(v>=threshold) for v in pp]
 return {name:sum(int(a==yt and b==yp) for a,b in zip(yy,pred)) for name,yt,yp in [('TP',1,1),('FP',0,1),('FN',1,0),('TN',0,0)]}
assert confusion(.5)==dict(TP=1,FP=1,FN=1,TN=1)
assert confusion(.3)==dict(TP=2,FP=1,FN=0,TN=1)
report['worked_examples']['thresholds']={'.5':confusion(.5),'.3':confusion(.3)}
weights=[math.exp(v-2) for v in [0,1,2]];soft=[v/sum(weights) for v in weights]
near(-math.log(soft[2]),.40760596444438046)
report['worked_examples']['softmax']={'p':soft,'loss_class2':-math.log(soft[2])}
# AdaBoost normalized weights.
a=math.log(3);ww=[.25,.25,.25,.25*math.exp(a)];ww=[v/sum(ww) for v in ww];near(ww[3],.5)
report['worked_examples']['adaboost']={'alpha':a,'weights':ww}
# PCA covariance, projections, eigenvalue, reconstruction.
pts=[[-2,-2],[-1,-1],[1,1],[2,2]];c=sum(row[0]**2 for row in pts)/3;near(c,10/3)
w=[1/math.sqrt(2)]*2
reconstructed=[[sum(a*b for a,b in zip(row,w))*v for v in w] for row in pts]
err=sum((a-b)**2 for row,hat in zip(pts,reconstructed) for a,b in zip(row,hat));near(err,0)
report['worked_examples']['pca']={'covariance_entry':c,'eigenvalues':[2*c,0],'reconstruction_sse':err}
# K-means inertia and silhouette.
old=sum(min((v-u)**2 for u in [0,4]) for v in [0,1,4,5]);new=sum(min((v-u)**2 for u in [.5,4.5]) for v in [0,1,4,5])
assert (old,new)==(2,1);near((5-2)/max(5,2),.6);near((3-4)/max(3,4),-.25)
report['worked_examples']['kmeans']={'inertia_initial':old,'inertia_updated':new}
# DBSCAN includes the point itself.
xx=[0,.1,.2,.4,2];counts=[sum(abs(v-u)<=.21 for u in xx) for v in xx];assert counts==[3,3,4,2,1]
report['worked_examples']['dbscan']={'neighbor_counts':counts}
# E/M step and information criteria.
r=.5*.2/(.5*.2+.5*.05);near(r,.8)
mean=.8*0+.2*2;var=.8*(0-mean)**2+.2*(2-mean)**2;near(mean,.4);near(var,.64)
aic=[2*5+200,2*8+192];bic=[5*math.log(100)+200,8*math.log(100)+192]
assert aic[1]<aic[0] and bic[0]<bic[1]
report['worked_examples']['gmm']={'responsibility':r,'mean':mean,'variance':var,'aic':aic,'bic':bic}
# XOR truth table.
step=lambda z:int(z>=0)
xor=[step(-step(a+b-1.5)+step(a+b-.5)-.5) for a,b in [(0,0),(0,1),(1,0),(1,1)]];assert xor==[0,1,1,0]
# Neural gradient independently checked by finite differences.
sig=lambda z:1/(1+math.exp(-z))
loss=lambda w,b:.5*(sig(2*w+b)-1)**2
a=sig(1);dz=(a-1)*a*(1-a);dw=2*dz;db=dz
h=1e-5;near(dw,(loss(.5+h,0)-loss(.5-h,0))/(2*h));near(db,(loss(.5,h)-loss(.5,-h))/(2*h))
wnew=.5-.1*dw;bnew=-.1*db;assert loss(wnew,bnew)<loss(.5,0)
assert 10*50+50+50*3+3==703
report['worked_examples']['neural']={'xor':xor,'dw':dw,'db':db,'new_w':wnew,'new_b':bnew,'new_prediction':sig(2*wnew+bnew),'new_loss':loss(wnew,bnew),'parameter_count':703}
# Protected original sources and earlier slides are verified against pre-work hashes.
manifest=ROOT/'.build/chapters04_09/input_manifest.json'
if manifest.exists():
 for row in json.loads(manifest.read_text()):
  actual=hashlib.sha256((ROOT/row['path']).read_bytes()).hexdigest();assert actual==row['sha256'],f'Protected input changed: {row["path"]}'
  report['input_integrity'].append({'path':row['path'],'sha256':actual,'unchanged':True})
else:report['input_integrity_note']='Pre-work manifest unavailable; no historical comparison claimed.'
layout=ROOT/'.build/qa/layout_report.json'
if layout.exists():
 rows=[r for r in json.loads(layout.read_text()) if r['file'][:2].isdigit() and 4<=int(r['file'][:2])<=11]
 assert len(rows)==8
 assert not any(s['bad'] or s['broken'] or s['mathErrors'] or s['rawMarkdown'] for r in rows for s in r['slides'])
 report['layout_audit']={'decks':8,'slides':sum(len(r['slides']) for r in rows),'issues':0}
report['total_slides']=sum(r['slides'] for r in report['decks']);report['teaching_hours_including_breaks']=24
print(json.dumps({k:report[k] for k in ['total_slides','numbered_figures','numbered_equations','numbered_tables','teaching_hours_including_breaks']},ensure_ascii=False))
print('Worked examples verified:',len(report['worked_examples']),'groups; unchanged originals:',len(report['input_integrity']))
