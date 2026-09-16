"""Execute each notebook in a fresh local kernel; preserve outputs and timing."""
from pathlib import Path
import argparse
import json
import os
import sys
import time
import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('names', nargs='*', help='optional notebook stems or prefixes')
    parser.add_argument('--html', action='store_true')
    args = parser.parse_args()
    # Local kernel spec; does not register a kernel in the user account.
    specs = ROOT/'.jupyter/kernels/mlcourse2026'
    specs.mkdir(parents=True, exist_ok=True)
    (specs/'kernel.json').write_text(json.dumps({'argv':[sys.executable,'-m','ipykernel_launcher','-f','{connection_file}'],
        'display_name':'MLCourse2026 (uv)', 'language':'python'}))
    os.environ['JUPYTER_PATH'] = str(ROOT/'.jupyter')
    os.environ['IPYTHONDIR'] = str(ROOT/'.jupyter/ipython')
    os.environ['MPLCONFIGDIR'] = str(ROOT/'.jupyter/matplotlib')
    paths = sorted((ROOT/'notebooks').glob('*.ipynb'))
    if args.names:
        paths = [p for p in paths if any(p.stem.startswith(x) for x in args.names)]
    assert paths, 'No notebooks selected'
    results = []
    for path in paths:
        start = time.monotonic()
        print('RUN', path.name, flush=True)
        nb = nbformat.read(path, as_version=4)
        client = NotebookClient(nb, timeout=1200, kernel_name='mlcourse2026',
                                resources={'metadata':{'path':str(ROOT)}})
        try:
            client.execute()
        except Exception:
            (ROOT/'outputs').mkdir(exist_ok=True)
            nbformat.write(nb, ROOT/'outputs'/f'FAILED_{path.name}')
            raise
        nbformat.write(nb, path)
        if args.html:
            from export_notebooks import export_notebook, make_index
            export_notebook(path)
            make_index()
        row = {'notebook':path.name, 'seconds':round(time.monotonic()-start,2),
               'code_cells':sum(c.cell_type=='code' for c in nb.cells), 'errors':0,
               'profile':os.environ.get('MLCOURSE_PROFILE','fast')}
        results.append(row)
        print('OK', row, flush=True)
        report = ROOT/'outputs/execution.json'
        existing = json.loads(report.read_text()) if report.exists() else []
        existing = [r for r in existing if r['notebook'] != path.name] + [row]
        report.write_text(json.dumps(sorted(existing,key=lambda r:r['notebook']),indent=2)+'\n')

if __name__ == '__main__':
    main()
