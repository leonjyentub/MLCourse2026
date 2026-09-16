"""Export saved notebook outputs to HTML, without executing code."""
from pathlib import Path
import html
import nbformat
from nbconvert import HTMLExporter

ROOT=Path(__file__).resolve().parents[1]

def export_notebook(path):
    nb=nbformat.read(path,as_version=4)
    body,_=HTMLExporter().from_notebook_node(nb)
    body=body.replace('href="../README.md"','href="../../README.md"')
    body=body.replace('href="../SOURCES.md"','href="../../SOURCES.md"')
    folder=ROOT/'outputs/html'
    folder.mkdir(parents=True,exist_ok=True)
    (folder/f'{path.stem}.html').write_text(body)

def make_index():
    items=[]
    for path in sorted((ROOT/'notebooks').glob('*.ipynb')):
        title=path.stem.replace('_','｜',1)
        items.append(f'<li><a href="{html.escape(path.stem)}.html">{html.escape(title)}</a></li>')
    body='''<!doctype html><html lang="zh-Hant"><meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>機器學習教學 Notebook</title>
    <style>body{font-family:system-ui,sans-serif;max-width:850px;margin:60px auto;padding:0 24px;line-height:1.8;color:#243744;background:#f7f9fb}h1{line-height:1.3}a{color:#17626b}li{padding:9px 0}main{background:white;border:1px solid #dce4ea;border-radius:14px;padding:30px}small{color:#586d79}</style>
    <main><small>MLCourse2026 · 三週教學配套</small><h1>從資料到可信的評估</h1>
    <p>九本 Notebook 的已執行閱讀版。編修請開啟 notebooks/ 中的 .ipynb；互動滑桿需在 Jupyter 使用。</p><ol>'''
    body+=''.join(items)+'</ol><p><a href="../../README.md">操作說明</a> · <a href="../../TEACHING_MAP.md">投影片對照</a> · <a href="../../SOURCES.md">程式來源</a></p></main></html>'
    (ROOT/'outputs/html/index.html').write_text(body)

if __name__=='__main__':
    for path in sorted((ROOT/'notebooks').glob('*.ipynb')):
        export_notebook(path)
    make_index()
    print('Exported 9 notebooks and reading index.')
