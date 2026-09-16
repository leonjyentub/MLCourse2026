from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[2]
SL=ROOT/'slides'
FIG={r['figure']:r for r in json.loads((SL/'assets/chapters04_09/sources.json').read_text())}
DECKS=[]
class Deck:
 def __init__(self,num,title,subtitle,source,ppt):
  self.num=num;self.title=title;self.source=source;self.ppt=ppt;self.slides=[];self.block=0
  self.add(title,subtitle+'\n\n後續八週課程｜每週 180 分鐘（含兩次 10 分鐘休息）',source,cls='cover',weight=1)
 def add(self,title,body,source=None,note='',cls='',weight=3,core=True):
  self.slides.append(dict(title=title,body=body,source=source or self.source,note=note,cls=cls,weight=weight,block=self.block,core=core));return self
 def fig(self,key,title,explain,note='',core=True):
  f=FIG[key]; src=f"主教材 Ch.{key.split('-')[0]} p.{f['printed_page']}，圖 {key}"
  return self.add(title,f"![h:390 {f['caption']}](assets/chapters04_09/book_fig_{key.replace('-','_')}.png)\n\n{explain}",src,note,'figure',2,core)
 def table(self,title,headers,rows,source=None,note='',core=True):
  body='| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+'\n'.join('| '+' | '.join(r)+' |' for r in rows)
  return self.add(title,body,source,note,'small',3,core)
 def activity(self,title,body,note,weight=12,core=True):return self.add(title,body,None,note,'activity',weight,core)
 def br(self):
  self.slides.append(dict(title='休息 10 分鐘',body='離開座位、休息眼睛。回來後先用一句話回答上一段的核心問題。',source=self.source,note='保留完整休息；不要用來補講延伸內容。',cls='activity',weight=10,block=-1,core=True,minutes=10));self.block+=1
 def finish(self):
  # Three teaching blocks total 160 minutes. Largest-remainder allocation preserves exact totals.
  for b,target in enumerate([50,60,50]):
   ss=[s for s in self.slides if s['block']==b]; total=sum(s['weight'] for s in ss)
   vals=[target*s['weight']/total for s in ss]; mins=[max(1,int(v)) for v in vals]
   while sum(mins)<target:
    j=max(range(len(ss)),key=lambda j:vals[j]-mins[j]);mins[j]+=1
   while sum(mins)>target:
    j=max((j for j in range(len(ss)) if mins[j]>1),key=lambda j:mins[j]-vals[j]);mins[j]-=1
   for s,m in zip(ss,mins):s['minutes']=m
  filename=f'{self.num:02d}_{self.title}.md';self.path=SL/filename
  out=['---\nmarp: true\ntheme: ml-course\nsize: 16:9\npaginate: true\nmath: katex\ntitle: '+self.title+'\n---']
  for i,s in enumerate(self.slides,1):
   if i>1:out.append('---')
   cl='<!-- _class: '+s['cls']+' -->\n' if s['cls'] else ''
   footer=s['source']+'；舊稿 '+self.ppt if i==1 else s['source']
   out.append(cl+'<!-- _footer: "'+footer.replace('"',"'")+'" -->\n'+f'<!-- meta: minutes={s["minutes"]}; core6={"yes" if s["core"] else "no"}; block={s["block"]}; source={s["source"]} -->\n'+('# ' if s['cls']=='cover' else '## ')+s['title']+'\n\n'+s['body']+'\n\n<!-- 講者提示：'+(s['note'] or '先讓學生說明本頁符號或圖形，再連結前後概念。圖表中的教材結果僅作來源示例，不能當作本班重跑結果。')+' -->')
  self.path.write_text('\n\n'.join(out)+'\n');DECKS.append(self)

def build():
 exec((Path(__file__).parent/'content04_05.py').read_text(),globals())
 exec((Path(__file__).parent/'content06_07.py').read_text(),globals())
 exec((Path(__file__).parent/'content08_09.py').read_text(),globals())
 exec((Path(__file__).parent/'content10_11.py').read_text(),globals())
 data=[dict(file=str(d.path.relative_to(ROOT)),title=d.title,source=d.source,ppt=d.ppt,slides=d.slides) for d in DECKS]
 (ROOT/'.build/chapters04_09/decks.json').write_text(json.dumps(data,ensure_ascii=False,indent=2))
 print([(d.num,len(d.slides),sum(s['minutes'] for s in d.slides)) for d in DECKS])
if __name__=='__main__':build()
