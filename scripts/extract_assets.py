"""Extract only selected teaching figures. Run with Python + PyMuPDF."""
from pathlib import Path
import fitz, json, shutil
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'slides/assets'; OUT.mkdir(parents=True,exist_ok=True)
items=[
 ('01',12,1,'book_fig_1_7','1-7'),('01',13,0,'book_fig_1_8','1-8'),('01',15,0,'book_fig_1_11','1-11'),
 ('01',25,0,'book_fig_1_19','1-19'),('01',30,0,'book_fig_1_22','1-22'),('01',33,0,'book_fig_1_24','1-24'),
 ('02',16,0,'book_fig_2_8','2-8'),('02',25,0,'book_fig_2_13','2-13'),('02',27,0,'book_fig_2_15','2-15'),('02',39,0,'book_fig_2_17','2-17'),
 ('03',4,0,'book_fig_3_2','3-2'),('03',10,0,'book_fig_3_4','3-4'),('03',11,0,'book_fig_3_5','3-5'),('03',17,0,'book_fig_3_8','3-8'),('03',21,0,'book_fig_3_9','3-9'),('03',23,0,'book_fig_3_11','3-11'),('03',27,0,'book_fig_3_12','3-12')]
manifest=[]
for ch,page,idx,name,figure in items:
 p=next((ROOT/'book').glob('CHAPTER '+ch+'*.pdf'))
 d=fitz.open(p); b=[b for b in d[page-1].get_text('dict')['blocks'] if b['type']==1][idx]
 out=OUT/(name+'.'+b['ext']);out.write_bytes(b['image'])
 manifest.append(dict(asset=str(out.relative_to(ROOT)),source=str(p.relative_to(ROOT)),pdf_page=page,printed_page=page+{'01':0,'02':40,'03':106}[ch],figure=figure,method='原始內嵌影像擷取，未重畫'))
# Selected images are found through the source slide relationships, not by guessed media names.
import zipfile,xml.etree.ElementTree as E,posixpath
ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
for stem,n,j,name in [('00_Machine Learning',7,0,'ppt_supervised_regression'),('00_Machine Learning',8,0,'ppt_supervised_classification'),('01_Regressions',42,0,'ppt_iris_pairplot'),('01_Regressions',48,0,'ppt_logistic_regions'),('02_Validation and Regularization',8,0,'ppt_polynomial_fit'),('02_Validation and Regularization',11,0,'ppt_l1_l2_geometry')]:
 p=ROOT/'source_pptx'/(stem+'.pptx')
 with zipfile.ZipFile(p) as z:
  s=E.fromstring(z.read(f'ppt/slides/slide{n}.xml'));rel=E.fromstring(z.read(f'ppt/slides/_rels/slide{n}.xml.rels'));rs={x.attrib['Id']:x.attrib['Target'] for x in rel}
  b=s.findall('.//a:blip',ns)[j];rid=b.attrib['{'+ns['r']+'}embed'];src=posixpath.normpath(posixpath.join('ppt/slides',rs[rid]));out=OUT/(name+Path(src).suffix);out.write_bytes(z.read(src))
  manifest.append(dict(asset=str(out.relative_to(ROOT)),source=str(p.relative_to(ROOT)),slide=n,media=src,method='內嵌影像擷取；教材示例，不視為本次實驗'))
(OUT/'sources.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Extracted',len(manifest),'figures')
