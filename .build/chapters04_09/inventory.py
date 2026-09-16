from pathlib import Path
import fitz,zipfile,xml.etree.ElementTree as E,json,hashlib
root=Path(__file__).resolve().parents[2];out=root/'.build/chapters04_09'
manifest=[]
for p in sorted((root/'book').glob('CHAPTER 0[4-9]*.pdf')):
 d=fitz.open(p);parts=[]
 for i,page in enumerate(d):parts.append(f'\n===== PDF PAGE {i+1} =====\n'+page.get_text())
 (out/(p.stem+'.txt')).write_text(''.join(parts))
 print(p.name,'PDF pages:',len(d),'images:',sum(len(p.get_images()) for p in d))
 print(d[0].get_text()[:650].replace('\n',' / '))
 manifest.append({'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'pages':len(d)})
ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
for p in sorted((root/'source_pptx').glob('*.pptx')):
 with zipfile.ZipFile(p) as z:
  names=sorted([n for n in z.namelist() if n.startswith('ppt/slides/slide') and n.endswith('.xml')],key=lambda n:int(Path(n).stem.replace('slide','')))
  text=[]
  for i,n in enumerate(names):
   tree=E.fromstring(z.read(n));lines=[t.text or '' for t in tree.findall('.//a:t',ns)]
   text.append(f'\n===== SLIDE {i+1} =====\n'+'\n'.join(lines))
  (out/(p.stem+'.txt')).write_text(''.join(text))
  print(p.name,len(names),'slides')
  manifest.append({'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'slides':len(names)})
for p in sorted((root/'slides').glob('*')):
 if p.is_file():manifest.append({'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(out/'input_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
