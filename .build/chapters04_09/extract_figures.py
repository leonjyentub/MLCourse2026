from pathlib import Path
import fitz,json
root=Path(__file__).resolve().parents[2];work=root/'.build/chapters04_09';out=root/'slides/assets/chapters04_09';out.mkdir(parents=True,exist_ok=True)
figs=json.loads((work/'figure_inventory.json').read_text());docs={};base={4:134,5:178,6:194,7:220,8:244,9:282}
assert len({f['figure'] for f in figs})==90
for f in figs:
 if f['source'] not in docs:docs[f['source']]=fitz.open(root/f['source'])
 doc=docs[f['source']];page=doc[f['pdf_page']-1];rect=fitz.Rect(f['bbox'])
 dest=out/f'book_fig_{f["figure"].replace("-","_")}.png'
 page.get_pixmap(matrix=fitz.Matrix(3,3),clip=rect,alpha=False).save(dest)
 f['asset']=str(dest.relative_to(root));f['printed_page']=f['pdf_page']+base[int(f['figure'].split('-')[0])]
 f['method']='PDF 圖形區域高解析擷取，保留原圖坐標與圖例；中文解說另寫於 Marp'
(out/'sources.json').write_text(json.dumps(figs,ensure_ascii=False,indent=2)+'\n')
print('Extracted',len(figs),'book figures')
