"""Changed teaching adaptation of Géron Ch.2 ratio_pipeline (Apache-2.0).

Adds explicit input checks, zero-denominator handling and feature names.
See SOURCES.md for immutable upstream links.
"""
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_array, check_is_fitted

class RatioTransformer(TransformerMixin, BaseEstimator):
    """Two numeric columns -> numerator / denominator; zero yields 0."""
    def fit(self, X, y=None):
        X = check_array(X)
        if X.shape[1] != 2:
            raise ValueError('RatioTransformer requires exactly two columns')
        self.n_features_in_ = X.shape[1]
        return self

    def transform(self, X):
        check_is_fitted(self, 'n_features_in_')
        X = check_array(X)
        if X.shape[1] != self.n_features_in_:
            raise ValueError('Feature count differs from fit')
        return np.divide(X[:, [0]], X[:, [1]],
                         out=np.zeros((len(X), 1)), where=X[:, [1]] != 0)

    def get_feature_names_out(self, input_features=None):
        check_is_fitted(self, 'n_features_in_')
        return np.array(['ratio'], dtype=object)
