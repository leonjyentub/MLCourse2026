import json
import re
import uuid
from pathlib import Path

root = Path(__file__).resolve().parents[2]
notebooks = root / 'programs/notebooks'
from notebook_bootstrap import install_cell, setup_cell

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
        if any('# 第 1 格：安裝本 Notebook 實際使用的套件。' in ''.join(c.get('source', [])) for c in cells):
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
        # 第一格只安裝本檔需要的套件；第二格才準備繪圖、資料與輸出。
        first = next(i for i, c in enumerate(cells) if c['cell_type'] == 'code')
        sources = [''.join(c['source']) for c in cells if c['cell_type'] == 'code']
        number = int(path.stem[:2])
        for offset, source in enumerate((install_cell(sources), setup_cell(number))):
            cells.insert(first + offset, {'cell_type': 'code', 'id': uuid.uuid4().hex[:8],
                                         'execution_count': None, 'metadata': {},
                                         'outputs': [], 'source': source.splitlines(keepends=True)})
        intro = next(c for c in cells if c['cell_type'] == 'markdown' and ''.join(c['source']).startswith('# '))
        text = ''.join(intro['source']).rstrip() + '\n\n從上到下執行程式格。第一格安裝缺少的套件，第二格準備本章所需設定。\n'
        intro['source'] = text.splitlines(keepends=True)
        nb['metadata']['kernelspec'] = {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}
        nb['metadata']['language_info'] = {'name': 'python'}
        nb['metadata'].pop('mlcourse', None)
        # 清空既有執行結果，避免被誤認為目前 Colab 環境的輸出。
        for cell in cells:
            if cell['cell_type'] == 'code':
                cell['execution_count'] = None
                cell['outputs'] = []
        path.write_text(json.dumps(nb, ensure_ascii=False, indent=1) + '\n')
        print(path.name)


if __name__ == "__main__":
    main()
