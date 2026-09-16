"""Fetch teaching data once. Existing files are hash-checked, never silently replaced."""
from pathlib import Path
import argparse
import hashlib
import io
import json
import tarfile
import urllib.request
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    DATA.mkdir(exist_ok=True)
    manifest_path = DATA / 'manifest.json'
    manifest = json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    if args.verify_only:
        for name, entry in manifest.items():
            assert sha(DATA / name) == entry['sha256'], name
        assert {'housing.csv', 'lifesat.csv', 'mnist_784_v1.npz'} <= manifest.keys()
        print('All 3 datasets verified.')
        return
    for name, entry in manifest.items():
        if (DATA/name).exists():
            assert sha(DATA/name) == entry['sha256'], f'Existing data changed: {name}'
    if any(name not in manifest or not (DATA/name).exists() for name in ['housing.csv','lifesat.csv']):
        commit = '9e29abbbea6a3ff7250dea64c43c1d6c723095d7'
        for name, remote in [('housing.csv', 'housing.tgz'), ('lifesat.csv', 'lifesat/lifesat.csv')]:
            if name in manifest and (DATA/name).exists():
                continue
            url = f'https://raw.githubusercontent.com/ageron/data/{commit}/{remote}'
            blob = urllib.request.urlopen(url, timeout=120).read()
            if name == 'housing.csv':
                with tarfile.open(fileobj=io.BytesIO(blob), mode='r:gz') as archive:
                    blob = archive.extractfile('housing/housing.csv').read()
            if name in manifest:
                assert hashlib.sha256(blob).hexdigest() == manifest[name]['sha256'], f'Remote data changed: {name}'
            (DATA/name).write_bytes(blob)
            manifest[name] = {'url':url, 'commit':commit, 'sha256':sha(DATA/name)}
            manifest_path.write_text(json.dumps(manifest, indent=2)+'\n')
            print('Saved', name, flush=True)
    name = 'mnist_784_v1.npz'
    if name not in manifest or not (DATA/name).exists():
        from sklearn.datasets import fetch_openml
        ds = fetch_openml('mnist_784', version=1, as_frame=False, data_home=DATA/'openml_cache', parser='auto')
        X, y = ds.data.astype(np.uint8), ds.target.astype(np.uint8)
        assert X.shape == (70000, 784) and y.shape == (70000,)
        np.savez_compressed(DATA/name, X=X, y=y)
        if name in manifest:
            assert sha(DATA/name) == manifest[name]['sha256'], f'Redownload differs: {name}'
        manifest[name] = {'url':'https://www.openml.org/d/554', 'openml_id':554, 'version':1, 'shape':list(X.shape), 'sha256':sha(DATA/name)}
        manifest_path.write_text(json.dumps(manifest, indent=2)+'\n')
        print('Saved', name, flush=True)
    for name, entry in manifest.items():
        assert sha(DATA/name) == entry['sha256'], name
    print('All datasets ready.', flush=True)

if __name__ == '__main__':
    main()
