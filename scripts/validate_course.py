"""Validate authored deck structure, source references and teaching arithmetic."""
from pathlib import Path
import re,json,math,xml.etree.ElementTree as E
def slides(p):
    text=re.sub(r"^---\n.*?\n---\n", "", p.read_text(), count=1, flags=re.S)
    return re.split(r"\n---\s*\n", text)
ROOT=Path(__file__).resolve().parents[1]
expected=[4,36,47,43]
for p,count in zip(sorted((ROOT/'slides').glob('0[0-3]_*.md')),expected,strict=True):
 blocks=slides(p);assert len(blocks)==count,(p,len(blocks))
 for i,b in enumerate(blocks,1):
  assert re.search(r'<!-- 講者提示：',b),(p,i,'missing notes')
  assert re.search(r'^#{1,2} ',b,re.M),(p,i,'missing title')
  for url in re.findall(r'\]\((assets/[^)]+)\)',b):assert (p.parent/url).exists(),(p,i,url)
 print(p.name,count,'slides; notes/assets OK')
for p in (ROOT/'slides/assets').glob('*.svg'):E.parse(p)
# Recompute actual table values and curve points rather than checking only strings.
tn,fp,fn,tp=53892,687,1891,3530
assert tn+fp+fn+tp==60000
assert round((tp+tn)/60000*100,2)==95.70
assert round(tp/(tp+fp)*100,2)==83.71
assert round(tp/(tp+fn)*100,2)==65.12
assert round(2*tp/(2*tp+fp+fn),3)==.733
scores=[.95,.85,.8,.7,.6,.4,.3,.1];ys=[1,0,1,1,0,0,1,0]
for t,expected_cm in [(.8,(2,1,2,3)),(.5,(3,2,1,2)),(.2,(4,3,0,1))]:
 pred=[s>=t for s in scores];tp=sum(p and y for p,y in zip(pred,ys));fp=sum(p and not y for p,y in zip(pred,ys));fn=sum(not p and y for p,y in zip(pred,ys));tn=sum(not p and not y for p,y in zip(pred,ys));assert (tp,fp,fn,tn)==expected_cm
positive=[s for s,y in zip(scores,ys) if y];negative=[s for s,y in zip(scores,ys) if not y]
auc=sum((p>n)+.5*(p==n) for p in positive for n in negative)/(len(positive)*len(negative));assert auc==.6875
curve=json.loads((ROOT/'slides/assets/toy_thresholds.json').read_text())
xy=[(0,0)]+[(q['fpr'],q['recall']) for q in curve];area=sum((x2-x1)*(y2+y1)/2 for (x1,y1),(x2,y2) in zip(xy,xy[1:]));assert area==auc
assert math.isclose(math.sqrt(sum(x*x for x in [-2,2,-2,10])/4),math.sqrt(28))
assert round(90/189*100,1)==47.6
print('SVG XML, confusion matrices, ROC AUC, threshold/cost exercises and regression arithmetic OK')
