"""Execute each notebook in a fresh local kernel; preserve outputs and timing."""
from pathlib import Path
import argparse
import json
import os
import sys
import time
import hashlib
import shutil
import tempfile
from datetime import datetime, timezone
import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('names', nargs='*', help='optional notebook stems or prefixes')
    parser.add_argument('--html', action='store_true')
    parser.add_argument('--preserve-source', action='store_true',
                        help='在暫存目錄執行並匯出 HTML，不覆寫 .ipynb、圖檔或報告')
    args = parser.parse_args()
    if args.preserve_source and not args.html:
        parser.error('--preserve-source 請搭配 --html')
    # Local kernel spec; does not register a kernel in the user account.
    specs = ROOT/'.jupyter/kernels/mlcourse2026'
    specs.mkdir(parents=True, exist_ok=True)
    (specs/'kernel.json').write_text(json.dumps({'argv':[sys.executable,'-m','ipykernel_launcher','-f','{connection_file}'],
        'display_name':'MLCourse2026 (uv)', 'language':'python'}))
    os.environ['JUPYTER_PATH'] = str(ROOT/'.jupyter')
    os.environ['IPYTHONDIR'] = str(ROOT/'.jupyter/ipython')
    os.environ['MPLCONFIGDIR'] = str(ROOT/'.jupyter/matplotlib')
    paths = sorted((ROOT/'notebooks').glob('*.ipynb'))
    valid_notebooks = {p.name for p in paths}
    if args.names:
        paths = [p for p in paths if any(p.stem.startswith(x) for x in args.names)]
    assert paths, 'No notebooks selected'
    results = []
    for path in paths:
        start = time.monotonic()
        print('RUN', path.name, flush=True)
        nb = nbformat.read(path, as_version=4)
        source_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        nb.metadata.pop('widgets', None)
        temporary = tempfile.TemporaryDirectory(prefix=f'mlcourse-{path.stem[:2]}-') if args.preserve_source else None
        run_root = Path(temporary.name) if temporary else ROOT
        if temporary:
            cached = {'01':['lifesat.csv'], '02':['housing.csv'],
                      '03':['mnist_784_v1.npz'], '07':['mnist_784_v1.npz']}
            (run_root/'mlcourse_data').mkdir()
            for name in cached.get(path.stem[:2], []):
                source = ROOT/'data'/name
                if source.exists():
                    shutil.copy2(source, run_root/'mlcourse_data'/name)
        client = NotebookClient(nb, timeout=1200, kernel_name='mlcourse2026',
                                resources={'metadata':{'path':str(run_root)}})
        try:
            client.execute()
        except Exception:
            (ROOT/'outputs').mkdir(exist_ok=True)
            nbformat.write(nb, ROOT/'outputs'/f'FAILED_{path.name}')
            raise
        if not args.preserve_source:
            nbformat.write(nb, path)
        row = {'notebook':path.name, 'seconds':round(time.monotonic()-start,2),
               'code_cells':sum(c.cell_type=='code' for c in nb.cells), 'errors':0,
               'profile':os.environ.get('MLCOURSE_PROFILE','fast'),
               'source_sha256':source_hash,
               'executed_at':datetime.now(timezone.utc).isoformat(),
               'source_preserved':args.preserve_source}
        if args.html:
            from export_notebooks import export_notebook, make_index
            export_notebook(path, notebook=nb, execution=row)
            make_index()
        if temporary:
            temporary.cleanup()
        results.append(row)
        print('OK', row, flush=True)
        report = ROOT/'outputs'/('html_execution.json' if args.preserve_source else 'execution.json')
        existing = json.loads(report.read_text()) if report.exists() else []
        existing = [r for r in existing
                    if r['notebook'] in valid_notebooks and r['notebook'] != path.name] + [row]
        report.write_text(json.dumps(sorted(existing,key=lambda r:r['notebook']),indent=2)+'\n')

if __name__ == '__main__':
    main()
