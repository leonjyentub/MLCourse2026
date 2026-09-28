"""Small, notebook-specific Colab setup cells for the classroom notebooks."""

from __future__ import annotations

import ast


REQUIREMENTS = {
    "numpy": ("numpy", "numpy>=1.26,<3"),
    "pandas": ("pandas", "pandas>=2.0,<3"),
    "matplotlib": ("matplotlib", "matplotlib>=3.7,<4"),
    "scipy": ("scipy", "scipy>=1.11,<2"),
    "sklearn": ("sklearn", "scikit-learn>=1.4,<2"),
    "cloudpickle": ("cloudpickle", "cloudpickle>=3,<4"),
    "ipywidgets": ("ipywidgets", "ipywidgets>=8,<9"),
}


def install_cell(code_sources: list[str]) -> str:
    """Install only third-party modules imported by this notebook."""
    # Every setup cell imports these three packages.
    modules = {"numpy", "pandas", "matplotlib"}
    for source in code_sources:
        for node in ast.walk(ast.parse(source)):
            if isinstance(node, ast.Import):
                modules.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                modules.add(node.module.split(".")[0])
    needed = {module: spec for module, (module, spec) in REQUIREMENTS.items()
              if module in modules}
    return (
        "# 第 1 格：安裝本 Notebook 實際使用的套件。\n"
        "import importlib.util, subprocess, sys\n"
        f"_needed = {needed!r}\n"
        "_missing = [spec for module, spec in _needed.items() "
        "if importlib.util.find_spec(module) is None]\n"
        "if _missing:\n"
        "    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-q', *_missing])\n"
    )


BASE_SETUP = '''# 第 2 格：本 Notebook 的輸出位置與繪圖設定。
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SEED = 42
ROOT = Path.cwd()
OUT = ROOT / ("outputs" if (ROOT / "pyproject.toml").exists() else "mlcourse_outputs")
plt.rcParams.update({"figure.figsize": (8, 4.5), "figure.dpi": 110,
                     "axes.grid": True, "grid.alpha": 0.2, "font.size": 11})

def savefig(name):
    folder = OUT / "figures"
    folder.mkdir(parents=True, exist_ok=True)
    plt.gcf().savefig(folder / f"{name}.png", dpi=150, bbox_inches="tight")
    plt.gcf().savefig(folder / f"{name}.svg", bbox_inches="tight")
    plt.show()
'''

REPORT = '''
def report(name, values):
    folder = OUT / "reports"
    folder.mkdir(parents=True, exist_ok=True)
    (folder / f"{name}.json").write_text(
        json.dumps(values, ensure_ascii=False, indent=2, default=float) + "\\n")
'''

DATA_ROOT = '''
DATA = ROOT / ("data" if (ROOT / "pyproject.toml").exists() else "mlcourse_data")
DATA.mkdir(parents=True, exist_ok=True)
'''

LIFESAT = '''
# 固定資料版本與 SHA-256，讓每次課堂下載的是同一份資料。
import hashlib
import urllib.request
_DATA_URL = "https://raw.githubusercontent.com/ageron/data/9e29abbbea6a3ff7250dea64c43c1d6c723095d7/lifesat/lifesat.csv"
_DATA_SHA256 = "e247f7f6c19b0d8c55fb2af293f4fb3b710e31476534ad8e9b7e06ea546a2099"

def data_path(name):
    if name != "lifesat.csv":
        raise ValueError(f"此 Notebook 不使用 {name}")
    path = DATA / name
    if not path.exists():
        with urllib.request.urlopen(_DATA_URL, timeout=180) as response:
            blob = response.read()
        if hashlib.sha256(blob).hexdigest() != _DATA_SHA256:
            raise ValueError("下載資料校驗失敗")
        path.write_bytes(blob)
    if hashlib.sha256(path.read_bytes()).hexdigest() != _DATA_SHA256:
        raise ValueError("本機資料校驗失敗")
    return path
'''

HOUSING = '''
# 固定資料版本與 SHA-256，讓每次課堂下載的是同一份資料。
import hashlib
import io
import tarfile
import urllib.request
_DATA_URL = "https://raw.githubusercontent.com/ageron/data/9e29abbbea6a3ff7250dea64c43c1d6c723095d7/housing.tgz"
_DATA_SHA256 = "2364609dc48bec7df3ba9dbb7041478e704ecddcee70ef1827ec3fc49d22c0cc"

def data_path(name):
    if name != "housing.csv":
        raise ValueError(f"此 Notebook 不使用 {name}")
    path = DATA / name
    if not path.exists():
        with urllib.request.urlopen(_DATA_URL, timeout=180) as response:
            archive_bytes = response.read()
        with tarfile.open(fileobj=io.BytesIO(archive_bytes), mode="r:gz") as archive:
            member = archive.extractfile("housing/housing.csv")
            if member is None:
                raise ValueError("資料壓縮檔缺少 housing.csv")
            blob = member.read()
        if hashlib.sha256(blob).hexdigest() != _DATA_SHA256:
            raise ValueError("下載資料校驗失敗")
        path.write_bytes(blob)
    if hashlib.sha256(path.read_bytes()).hexdigest() != _DATA_SHA256:
        raise ValueError("本機資料校驗失敗")
    return path

def housing_split():
    from sklearn.model_selection import train_test_split
    frame = pd.read_csv(data_path("housing.csv"))
    income = pd.cut(frame.median_income, [0, 1.5, 3, 4.5, 6, np.inf],
                    labels=[1, 2, 3, 4, 5])
    train, test = train_test_split(frame, test_size=0.2,
                                   random_state=SEED, stratify=income)
    assert not set(train.index) & set(test.index)
    return train, test
'''

MNIST = '''
# MNIST 只供分類示範使用，首次執行時由 OpenML 下載。
def data_path(name):
    if name != "mnist_784_v1.npz":
        raise ValueError(f"此 Notebook 不使用 {name}")
    path = DATA / name
    if not path.exists():
        from sklearn.datasets import fetch_openml
        ds = fetch_openml("mnist_784", version=1, as_frame=False,
                          data_home=DATA / "openml_cache", parser="auto")
        X, y = ds.data.astype(np.uint8), ds.target.astype(np.uint8)
        assert X.shape == (70000, 784) and y.shape == (70000,)
        np.savez_compressed(path, X=X, y=y)
    with np.load(path) as archive:
        assert archive["X"].shape == (70000, 784)
        assert archive["y"].shape == (70000,)
    return path
'''


def setup_cell(number: int) -> str:
    source = BASE_SETUP
    if number != 0:
        source += REPORT
    if number in {1, 2, 3, 7}:
        source += DATA_ROOT
    if number == 1:
        source += LIFESAT
    elif number == 2:
        source += HOUSING
    elif number in {3, 7}:
        source += MNIST
    if number in {2, 3}:
        source += '''
import os
FAST = os.environ.get("MLCOURSE_PROFILE", "fast") != "full"
'''
    if number in {16, 19, 23}:
        source += "\nrng = np.random.default_rng(SEED)\n"
    return source
