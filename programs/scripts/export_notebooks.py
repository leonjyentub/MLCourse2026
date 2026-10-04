"""Export saved notebook outputs to HTML, without executing code."""
from pathlib import Path
import html
import copy
import hashlib
import json
import re
import nbformat
from nbconvert import HTMLExporter

ROOT=Path(__file__).resolve().parents[1]

def reading_banner(body, execution):
    status = (f"本次執行：{execution['executed_at']}；{execution['profile']} 模式；"
              f"{execution['code_cells']} 個程式格；0 個執行錯誤。" if execution else '由已儲存的 Notebook 匯出；本次未執行程式。')
    banner = ('<aside style="margin:20px auto;padding:16px 24px;max-width:1100px;background:#edf5f3;border-left:5px solid #238b8e;font:16px/1.7 system-ui">'
              '<strong>Notebook 程式與結果閱讀版</strong><br>' + html.escape(status) +
              '<br>依序閱讀說明 → 程式 → 輸出；程式代碼可反查投影片頁次。HTML 不會執行 Python。'
              '要修改參數或操作滑桿，請開啟同名 .ipynb。數學排版可能需要網路載入 MathJax。'
              '<br><a href="index.html">全部章節</a> · <a href="../../../output/html/index.html">投影片 PDF／HTML</a></aside>')
    return re.sub(r'<body\b[^>]*>', lambda m: m.group(0)+banner, body, count=1)

def export_notebook(path, notebook=None, execution=None):
    nb=copy.deepcopy(notebook) if notebook is not None else nbformat.read(path,as_version=4)
    # Python callbacks need a live kernel; an exported slider would be misleading.
    nb.metadata.pop('widgets', None)
    for cell in nb.cells:
        if cell.cell_type == 'code':
            for output in cell.get('outputs', []):
                data = output.get('data', {})
                if 'application/vnd.jupyter.widget-view+json' in data:
                    output['data'] = {'text/plain':'互動滑桿需在 Jupyter／Colab 執行；HTML 請閱讀本節固定表格與圖形。'}
    body,_=HTMLExporter().from_notebook_node(nb)
    body=body.replace('<html lang="en">','<html lang="zh-Hant">')
    body=body.replace('<title>Notebook</title>',f'<title>{html.escape(path.stem)}</title>')
    body=reading_banner(body, execution)
    body=body.replace('href="../README.md"','href="../../README.md"')
    body=body.replace('href="../SOURCES.md"','href="../../SOURCES.md"')
    folder=ROOT/'outputs/html'
    folder.mkdir(parents=True,exist_ok=True)
    (folder/f'{path.stem}.html').write_text('\n'.join(line.rstrip() for line in body.splitlines())+'\n')
    manifest_path=folder/'manifest.json'
    manifest=json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    manifest[path.stem]={'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                         'execution':execution}
    manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')

def make_index():
    items=[]
    notebooks=sorted((ROOT/'notebooks').glob('*.ipynb'))
    folder=ROOT/'outputs/html'
    folder.mkdir(parents=True,exist_ok=True)
    manifest_path=folder/'manifest.json'
    manifest=json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    for path in notebooks:
        title=path.stem.replace('_','｜',1)
        record=manifest.get(path.stem, {})
        fresh=record.get('source_sha256')==hashlib.sha256(path.read_bytes()).hexdigest()
        execution=record.get('execution')
        label=(f"已同步並執行 · {execution['profile']} · {execution['code_cells']} 格" if fresh and execution
               else '僅匯出原稿，未重跑' if fresh else '歷史快照，尚未同步')
        items.append(f'<li><a href="{html.escape(path.stem)}.html">{html.escape(title)}</a><br><small>{label}</small></li>')
    body='''<!doctype html><html lang="zh-Hant"><meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>機器學習教學 Notebook</title>
    <style>body{font-family:system-ui,sans-serif;max-width:850px;margin:60px auto;padding:0 24px;line-height:1.8;color:#243744;background:#f7f9fb}h1{line-height:1.3}a{color:#17626b}li{padding:9px 0}main{background:white;border:1px solid #dce4ea;border-radius:14px;padding:30px}small{color:#586d79}</style>
    <main><small>MLCourse2026 · 完整課程配套</small><h1>概念、程式與實際輸出</h1>
    <p>這是 Notebook 的靜態閱讀版：說明 → 程式 → 表格／數字／圖形。各章下方標示是否與目前原稿同步，以及是否重新執行。</p>
    <p><strong>教學用法：</strong>課前找出輸入與目標；課中先預測結果、再展開閱讀；課後回到同名 .ipynb 修改一項參數，交付新圖及解釋。</p>
    <p>In [n] 是執行順序，不是章節或投影片頁碼；表格分數須連同資料切分、模式與指標閱讀。HTML 不會執行 Python；滑桿需 Jupyter／Colab，公式可能需網路載入 MathJax。</p>
    <p><a href="../../../output/html/index.html">投影片 PDF／HTML 入口</a></p><ol>'''
    body+=''.join(items)+'</ol><p><a href="../../HTML_TEACHING_GUIDE.md">HTML 教學使用說明</a> · <a href="../../README.md">操作說明</a> · <a href="../../TEACHING_MAP.md">投影片對照</a> · <a href="../../SOURCES.md">程式來源</a></p></main></html>'
    (ROOT/'outputs/html/index.html').write_text(body)

if __name__=='__main__':
    for path in sorted((ROOT/'notebooks').glob('*.ipynb')):
        export_notebook(path)
    make_index()
    print('Exported slide-aligned notebooks and reading index.')
