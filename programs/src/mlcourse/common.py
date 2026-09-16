"""Small I/O utilities. Statistical/teaching code stays in the notebooks."""
from pathlib import Path
import hashlib
import json
import os
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / 'data'
OUT = ROOT / 'outputs'
SEED = 42
FAST = os.environ.get('MLCOURSE_PROFILE', 'fast') != 'full'

def setup():
    import matplotlib.pyplot as plt
    plt.rcParams.update({'figure.figsize':(8, 4.5), 'figure.dpi':110,
                         'axes.grid':True, 'grid.alpha':0.2, 'font.size':11})
    OUT.mkdir(exist_ok=True)
    return {'profile':'fast' if FAST else 'full', 'seed':SEED, 'data':str(DATA)}

def savefig(name):
    import matplotlib.pyplot as plt
    folder = OUT / 'figures'
    folder.mkdir(exist_ok=True)
    plt.gcf().savefig(folder/f'{name}.png', dpi=150, bbox_inches='tight')
    plt.gcf().savefig(folder/f'{name}.svg', bbox_inches='tight')
    plt.show()

def report(name, values):
    folder = OUT / 'reports'
    folder.mkdir(exist_ok=True)
    (folder/f'{name}.json').write_text(json.dumps(values, ensure_ascii=False, indent=2, default=float)+'\n')

def data_path(name):
    path = DATA / name
    if not path.exists():
        raise FileNotFoundError('先在 programs 執行 uv run python scripts/fetch_data.py')
    manifest = json.loads((DATA/'manifest.json').read_text())
    assert hashlib.sha256(path.read_bytes()).hexdigest() == manifest[name]['sha256'], f'Data changed: {name}'
    return path

def housing_split():
    from sklearn.model_selection import train_test_split
    frame = pd.read_csv(data_path('housing.csv'))
    income = pd.cut(frame.median_income, [0,1.5,3,4.5,6,np.inf], labels=[1,2,3,4,5])
    train, test = train_test_split(frame, test_size=0.2, random_state=SEED, stratify=income)
    assert not set(train.index) & set(test.index)
    return train, test
