import json
import re
import uuid
from pathlib import Path

root = Path(__file__).resolve().parents[2]
notebooks = root / 'programs/notebooks'
bootstrap = '''# 獨立執行：Colab 上傳此檔後，從這一格依序執行；無需掛載 Git 專案。
import importlib.util, subprocess, sys
_needed = {"numpy": "numpy>=1.26,<3", "pandas": "pandas>=2.0,<3", "matplotlib": "matplotlib>=3.7,<4", "scipy": "scipy>=1.11,<2", "sklearn": "scikit-learn>=1.4,<2", "joblib": "joblib>=1.3,<2", "cloudpickle": "cloudpickle>=3,<4", "ipywidgets": "ipywidgets>=8,<9"}
_missing = [spec for module, spec in _needed.items() if importlib.util.find_spec(module) is None]
if _missing:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", *_missing])

from pathlib import Path
import hashlib, io, json, os, tarfile, urllib.request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path.cwd()
# 本機在 programs/ 執行時沿用 data/、outputs/；Colab 則使用自己的工作目錄。
DATA = ROOT / ("data" if (ROOT / "pyproject.toml").exists() else "mlcourse_data")
OUT = ROOT / ("outputs" if (ROOT / "pyproject.toml").exists() else "mlcourse_outputs")
SEED = 42
FAST = os.environ.get("MLCOURSE_PROFILE", "fast") != "full"
_SOURCE_COMMIT = "9e29abbbea6a3ff7250dea64c43c1d6c723095d7"
_SOURCES = {
    "housing.csv": (f"https://raw.githubusercontent.com/ageron/data/{_SOURCE_COMMIT}/housing.tgz", "2364609dc48bec7df3ba9dbb7041478e704ecddcee70ef1827ec3fc49d22c0cc"),
    "lifesat.csv": (f"https://raw.githubusercontent.com/ageron/data/{_SOURCE_COMMIT}/lifesat/lifesat.csv", "e247f7f6c19b0d8c55fb2af293f4fb3b710e31476534ad8e9b7e06ea546a2099"),
}

def setup():
    plt.rcParams.update({"figure.figsize": (8, 4.5), "figure.dpi": 110,
                         "axes.grid": True, "grid.alpha": 0.2, "font.size": 11})
    OUT.mkdir(parents=True, exist_ok=True)
    return {"profile": "fast" if FAST else "full", "seed": SEED, "data": str(DATA)}

def savefig(name):
    folder = OUT / "figures"
    folder.mkdir(parents=True, exist_ok=True)
    plt.gcf().savefig(folder / f"{name}.png", dpi=150, bbox_inches="tight")
    plt.gcf().savefig(folder / f"{name}.svg", bbox_inches="tight")
    plt.show()

def report(name, values):
    folder = OUT / "reports"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{name}.json").write_text(json.dumps(values, ensure_ascii=False, indent=2, default=float) + "\\n")

def data_path(name):
    if name not in (*_SOURCES, "mnist_784_v1.npz"):
        raise ValueError(f"未知資料檔：{name}")
    DATA.mkdir(parents=True, exist_ok=True)
    path = DATA / name
    if name in _SOURCES:
        url, expected_sha = _SOURCES[name]
        if not path.exists():
            print(f"下載 {name} …")
            with urllib.request.urlopen(url, timeout=180) as response:
                blob = response.read()
            if name == "housing.csv":
                with tarfile.open(fileobj=io.BytesIO(blob), mode="r:gz") as archive:
                    blob = archive.extractfile("housing/housing.csv").read()
            if hashlib.sha256(blob).hexdigest() != expected_sha:
                raise ValueError(f"資料校驗失敗：{name}")
            path.write_bytes(blob)
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected_sha:
            raise ValueError(f"本機資料校驗失敗：{name}")
        info = {"url": url, "sha256": expected_sha}
    else:
        if not path.exists():
            print("從 OpenML 下載 MNIST（首次約需數分鐘）…")
            from sklearn.datasets import fetch_openml
            ds = fetch_openml("mnist_784", version=1, as_frame=False,
                              data_home=DATA / "openml_cache", parser="auto")
            X, y = ds.data.astype(np.uint8), ds.target.astype(np.uint8)
            assert X.shape == (70000, 784) and y.shape == (70000,)
            np.savez_compressed(path, X=X, y=y)
        with np.load(path) as archive:
            assert archive["X"].shape == (70000, 784)
            assert archive["y"].shape == (70000,)
        info = {"url": "https://www.openml.org/d/554",
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    manifest_file = DATA / "manifest.json"
    manifest = json.loads(manifest_file.read_text()) if manifest_file.exists() else {}
    manifest[name] = info
    manifest_file.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\\n")
    return path

def housing_split():
    from sklearn.model_selection import train_test_split
    frame = pd.read_csv(data_path("housing.csv"))
    income = pd.cut(frame.median_income, [0, 1.5, 3, 4.5, 6, np.inf], labels=[1, 2, 3, 4, 5])
    train, test = train_test_split(frame, test_size=0.2, random_state=SEED, stratify=income)
    assert not set(train.index) & set(test.index)
    return train, test

setup()
'''
ratio = '''# 本 Notebook 自帶前處理器，儲存的模型可由同一份 Notebook 重新載入。
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_array, check_is_fitted

class RatioTransformer(TransformerMixin, BaseEstimator):
    """兩個數值欄位的比值；分母為 0 時傳回 0。"""
    def fit(self, X, y=None):
        X = check_array(X)
        if X.shape[1] != 2:
            raise ValueError("RatioTransformer requires exactly two columns")
        self.n_features_in_ = X.shape[1]
        return self

    def transform(self, X):
        check_is_fitted(self, "n_features_in_")
        X = check_array(X)
        if X.shape[1] != self.n_features_in_:
            raise ValueError("Feature count differs from fit")
        return np.divide(X[:, [0]], X[:, [1]],
                         out=np.zeros((len(X), 1)), where=X[:, [1]] != 0)

    def get_feature_names_out(self, input_features=None):
        check_is_fitted(self, "n_features_in_")
        return np.array(["ratio"], dtype=object)
'''
def main():
    for path in sorted(notebooks.glob('*.ipynb')):
        nb = json.loads(path.read_text())
        cells = nb['cells']
        if any('獨立執行：Colab 上傳此檔後' in ''.join(c.get('source', [])) for c in cells):
            print('unchanged', path.name)
            continue
        for cell in cells:
            if cell['cell_type'] != 'code':
                continue
            source = ''.join(cell['source'])
            source = re.sub(r'^from mlcourse\.common import .*\n?', '', source, flags=re.M)
            source = re.sub(r'^from mlcourse\.transformers import RatioTransformer\n?', ratio, source, flags=re.M)
            source = re.sub(r'^setup\(\)\n?', '', source, flags=re.M)
            source = source.replace('assert sys.version_info[:2] == (3,12)\n', '')
            source = source.replace("'matplotlib','nbclient'", "'matplotlib'")
            source = source.replace('import inspect\n', '')
            source = source.replace('print(inspect.getsource(RatioTransformer))', 'print(RatioTransformer.__doc__)')
            if path.name.startswith('02_'):
                source = source.replace('import joblib, json, sklearn', 'import cloudpickle, json, sklearn')
                source = source.replace("model_dir/'housing_pipeline.joblib'", "model_dir/'housing_pipeline.pkl'")
                source = source.replace('joblib.dump(final_model,model_file)',
                                        'with model_file.open("wb") as file:\n    cloudpickle.dump(final_model, file)')
                source = source.replace('loaded=joblib.load(model_file)',
                                        'with model_file.open("rb") as file:\n    loaded=cloudpickle.load(file)')
            cell['source'] = source.splitlines(keepends=True)
        # 第一個程式格前放置完整、可重入的啟動格；每本都能在空白 Colab 執行。
        first = next(i for i, c in enumerate(cells) if c['cell_type'] == 'code')
        cells.insert(first, {'cell_type': 'code', 'id': uuid.uuid4().hex[:8], 'execution_count': None, 'metadata': {},
                             'outputs': [], 'source': bootstrap.splitlines(keepends=True)})
        intro = next(c for c in cells if c['cell_type'] == 'markdown' and ''.join(c['source']).startswith('# '))
        text = ''.join(intro['source']) + '\n\n**Colab 示範**：直接上傳此 `.ipynb`，從上到下執行；第一個程式格會安裝缺少的套件，所需資料在使用時自動下載。NumPy 與 scikit-learn 實驗使用 CPU；這些程式沒有可直接切換的 CUDA 後端。輸出存於目前工作目錄。\n'
        intro['source'] = text.splitlines(keepends=True)
        nb['metadata']['kernelspec'] = {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}
        nb['metadata']['language_info'] = {'name': 'python'}
        # 舊執行結果來自修改前的環境，清空以免被誤認為 Colab 本次輸出。
        for cell in cells:
            if cell['cell_type'] == 'code':
                cell['execution_count'] = None
                cell['outputs'] = []
        path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + '\n')
        print(path.name)


if __name__ == "__main__":
    main()
