"""可直接執行的房價超參數搜尋示例；只讀取專案內附資料。"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import randint
from sklearn.compose import make_column_selector, make_column_transformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


DATA = Path(__file__).resolve().parents[1] / "data" / "housing.csv"


def build_pipeline() -> object:
    numeric = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
    categorical = make_pipeline(
        SimpleImputer(strategy="most_frequent"),
        OneHotEncoder(handle_unknown="ignore"),
    )
    preprocessing = make_column_transformer(
        (numeric, make_column_selector(dtype_include=np.number)),
        (categorical, make_column_selector(dtype_exclude=np.number)),
    )
    return make_pipeline(
        preprocessing,
        RandomForestRegressor(n_estimators=60, random_state=42, n_jobs=1),
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="比較 GridSearchCV 與 RandomizedSearchCV")
    parser.add_argument("--rows", type=int, default=3000, help="抽樣列數，預設 3000")
    parser.add_argument("--cv", type=int, default=3, help="交叉驗證折數，預設 3")
    parser.add_argument("--n-iter", type=int, default=4, help="隨機搜尋候選數，預設 4")
    args = parser.parse_args()

    housing = pd.read_csv(DATA)
    if args.rows < len(housing):
        housing = housing.sample(args.rows, random_state=42)
    X = housing.drop(columns="median_house_value")
    y = housing["median_house_value"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    grid = GridSearchCV(
        build_pipeline(),
        {
            "randomforestregressor__max_features": [0.5, 1.0],
            "randomforestregressor__min_samples_leaf": [1, 4],
        },
        cv=args.cv,
        scoring="neg_root_mean_squared_error",
        n_jobs=-1,
    )
    random = RandomizedSearchCV(
        build_pipeline(),
        {
            "randomforestregressor__max_features": [0.4, 0.6, 0.8, 1.0],
            "randomforestregressor__min_samples_leaf": randint(1, 8),
        },
        n_iter=args.n_iter,
        cv=args.cv,
        scoring="neg_root_mean_squared_error",
        random_state=42,
        n_jobs=-1,
    )

    searches = {"grid": grid, "random": random}
    for name, search in searches.items():
        search.fit(X_train, y_train)
        print(f"{name:>6} CV RMSE: {-search.best_score_:,.0f}")
        print(f"       best params: {search.best_params_}")

    winner_name, winner = max(searches.items(), key=lambda item: item[1].best_score_)
    test_rmse = root_mean_squared_error(y_test, winner.predict(X_test))
    print(f"winner: {winner_name}; final test RMSE: {test_rmse:,.0f}")
    print("注意：測試集只在搜尋方法與超參數定案後使用一次。")


if __name__ == "__main__":
    main()
