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
    assert len(notebooks)==17
    code_count=0
    for path in notebooks:
        nb=nbformat.read(path,as_version=4)
        nbformat.validate(nb)
        count=0
        for cell in nb.cells:
            if cell.cell_type=='code':
                ast.parse(cell.source)
                count+=1
                assert cell.execution_count==count, (path.name,count,cell.execution_count)
                assert not any(o.output_type=='error' for o in cell.outputs),path.name
        code_count+=count
        assert (ROOT/'outputs/html'/f'{path.stem}.html').exists()
    for entry in json.loads((ROOT/'upstream/manifest.json').read_text()):
        assert hashlib.sha256((ROOT/entry['local']).read_bytes()).hexdigest()==entry['sha256']
    for name,entry in json.loads((ROOT/'data/manifest.json').read_text()).items():
        assert hashlib.sha256((ROOT/'data'/name).read_bytes()).hexdigest()==entry['sha256']
    pngs=list((ROOT/'outputs/figures').glob('*.png'))
    for path in pngs:
        with Image.open(path) as im:
            im.verify()
        ET.parse(path.with_suffix('.svg'))
    assert len(pngs)>=30
    print(f'PASS: {len(notebooks)} notebooks, {code_count} executed code cells, {len(pngs)} PNG/SVG pairs; source/data hashes verified.')

if __name__=='__main__':
    main()
