"""Checks for actual failure boundaries in the teaching pipeline."""
import json
import subprocess
import sys
import numpy as np
import pandas as pd
import pytest
from sklearn.base import clone
from sklearn.exceptions import NotFittedError
from sklearn.impute import SimpleImputer
from sklearn.pipeline import make_pipeline
from mlcourse.common import ROOT, DATA, OUT, housing_split
from mlcourse.transformers import RatioTransformer

def test_ratio_rejects_unfitted_and_wrong_width():
    ratio = RatioTransformer()
    with pytest.raises(NotFittedError):
        ratio.transform([[1,2]])
    with pytest.raises(ValueError):
        ratio.fit([[1,2,3]])
    ratio.fit([[1,2]])
    with pytest.raises(ValueError):
        ratio.transform([[1,2,3]])

def test_ratio_zero_denominator_clone_and_no_input_mutation():
    data = np.array([[6.,3.],[4.,0.]])
    before = data.copy()
    ratio = RatioTransformer().fit(data)
    np.testing.assert_array_equal(ratio.transform(data),[[2.],[0.]])
    np.testing.assert_array_equal(data,before)
    assert ratio.get_feature_names_out().tolist()==['ratio']
    assert not hasattr(clone(ratio),'n_features_in_')

def test_imputation_does_not_learn_from_inference_rows():
    pipe = make_pipeline(SimpleImputer(strategy='median'),RatioTransformer())
    pipe.fit([[2.,1.],[6.,3.],[np.nan,2.]])
    before = pipe[0].statistics_.copy()
    result = pipe.transform([[np.nan,2.],[100000.,1.]])
    np.testing.assert_allclose(result[:,0],[2.,100000.])
    np.testing.assert_array_equal(pipe[0].statistics_,before)

def test_housing_split_disjoint_complete_and_repeatable():
    a,b = housing_split()
    c,d = housing_split()
    assert len(a)==16512 and len(b)==4128
    assert not set(a.index)&set(b.index)
    assert set(a.index)|set(b.index)==set(range(20640))
    assert a.index.equals(c.index) and b.index.equals(d.index)

def test_original_source_snapshots_unchanged():
    import hashlib
    manifest = json.loads((ROOT/'upstream/manifest.json').read_text())
    assert len(manifest)==44
    for item in manifest:
        assert hashlib.sha256((ROOT/item['local']).read_bytes()).hexdigest()==item['sha256']

def test_saved_pipeline_predicts_in_separate_python_process():
    if not (OUT/'models/housing_pipeline.joblib').exists():
        pytest.skip('Run notebook 04 to create the model before persistence validation')
    output = subprocess.check_output([sys.executable,str(ROOT/'scripts/predict_housing.py')],text=True,cwd=ROOT)
    result = json.loads(output)
    assert result['rows']==5
    assert np.isfinite(result['predictions_USD']).all()

def test_saved_pipeline_handles_missing_and_unknown_category():
    import joblib
    path = OUT/'models/housing_pipeline.joblib'
    if not path.exists():
        pytest.skip('Run notebook 04 first')
    model = joblib.load(path)
    frame = pd.read_csv(DATA/'housing.csv').head(3).drop(columns='median_house_value')
    frame.loc[0,'total_bedrooms']=np.nan
    frame.loc[1,'ocean_proximity']='NEW_UNSEEN_CATEGORY'
    assert np.isfinite(model.predict(frame)).all()
