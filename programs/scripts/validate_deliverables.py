"""Validate executable notebook delivery, figures, data and immutable sources."""
from pathlib import Path
import ast
import hashlib
import json
import xml.etree.ElementTree as ET
import nbformat
from PIL import Image

ROOT=Path(__file__).resolve().parents[1]

def main():
    notebooks=sorted((ROOT/'notebooks').glob('*.ipynb'))
    slides=sorted((ROOT.parent/'slides').glob('[0-9][0-9]_*.md'))
    assert len(notebooks)==26 and len(slides)==26
    assert [p.stem for p in notebooks]==[p.stem for p in slides]
    code_count=0
    for path,slide in zip(notebooks,slides):
        nb=nbformat.read(path,as_version=4)
        nbformat.validate(nb)
        first_markdown=next(cell.source for cell in nb.cells if cell.cell_type=='markdown')
        assert first_markdown.startswith(f'# {path.stem[:2]}｜')
        all_code='\n'.join(cell.source for cell in nb.cells if cell.cell_type=='code')
        assert 'mlcourse.common' not in all_code and 'mlcourse.transformers' not in all_code
        code_cells=[cell.source for cell in nb.cells if cell.cell_type=='code']
        assert code_cells[0].startswith('# 第 1 格：安裝本 Notebook 實際使用的套件。')
        assert 'pip' in code_cells[0] and '_DATA_URL' not in code_cells[0]
        assert code_cells[1].startswith('# 第 2 格：本 Notebook 的輸出位置與繪圖設定。')
        needs_data=path.stem[:2] in {'01','02','03','07'}
        assert ('def data_path(name):' in code_cells[1])==needs_data
        count=0
        for cell in nb.cells:
            if cell.cell_type=='code':
                ast.parse(cell.source)
                count+=1
                assert cell.execution_count is None, (path.name,count,cell.execution_count)
                assert not any(o.output_type=='error' for o in cell.outputs),path.name
        code_count+=count
        text=slide.read_text()
        assert f'`programs/notebooks/{path.name}`' in text
        assert f'](../programs/notebooks/{path.name})' not in text
        if path.stem!='00_課程導覽':
            assert 'notebook-result-slide' in text
    for entry in json.loads((ROOT/'upstream/manifest.json').read_text()):
        assert hashlib.sha256((ROOT/entry['local']).read_bytes()).hexdigest()==entry['sha256']
    for name,entry in json.loads((ROOT/'data/manifest.json').read_text()).items():
        assert hashlib.sha256((ROOT/'data'/name).read_bytes()).hexdigest()==entry['sha256']
    pngs=list((ROOT/'outputs/figures').glob('*.png'))
    for path in pngs:
        with Image.open(path) as im:
            im.verify()
        ET.parse(path.with_suffix('.svg'))
    assert len(pngs)>=72
    print(f'PASS: {len(notebooks)} slide-aligned notebooks, {code_count} parseable code cells, '
          f'{len(pngs)} PNG/SVG pairs; plain-text slide references and source/data hashes verified.')

if __name__=='__main__':
    main()
