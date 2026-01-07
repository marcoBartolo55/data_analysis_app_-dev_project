import movie
import numpy as np
import pandas as pd
from typing import Optional, Tuple

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.base import BaseEstimator


class MachineLearning:
    def __init__(self, movie_instance: movie.Movie):
        self.movie = movie_instance
        self.model: Optional[BaseEstimator] = None
        self.feature_names: Optional[list] = None
        self.numeric_features = ['budget', 'rating', 'votes', 'duration', 'release_year']
        self.categorical_features = ['primary_genre', 'lan-detected']

    def _extract_primary_genre(self, df: pd.DataFrame) -> pd.Series:
        if 'genres' in df.columns:
            def to_primary(x):
                if isinstance(x, list) and x:
                    return str(x[0]).strip()
                if isinstance(x, str):
                    tokens = [t.strip() for t in x.replace('|', ',').split(',') if t.strip()]
                    return tokens[0] if tokens else None
                return None
            return df['genres'].apply(to_primary)
        elif 'genre' in df.columns:
            return df['genre'].astype(str).str.strip()
        else:
            return pd.Series([None] * len(df), index=df.index)

    def _prepare_dataframe(self) -> pd.DataFrame:
        df = self.movie.data
        if df is None or df.empty:
            return pd.DataFrame()

        cols = set(df.columns)
        out = pd.DataFrame(index=df.index)
        for c in ['budget', 'revenue', 'rating', 'votes', 'duration', 'release_date', 'lan-detected']:
            if c in cols:
                out[c] = df[c]

        if 'release_date' in out.columns:
            dt = pd.to_datetime(out['release_date'], errors='coerce')
            out['release_year'] = dt.dt.year
        else:
            out['release_year'] = np.nan

        out['primary_genre'] = self._extract_primary_genre(df)

        req = ['budget', 'revenue']
        mask_req = out[req].notna().all(axis=1)
        mask_pos = (out['budget'] > 0)
        cleaned = out.loc[mask_req & mask_pos].copy()

        return cleaned

    def fit(self) -> Tuple[int, list]:
        df = self._prepare_dataframe()
        if df.empty:
            raise ValueError('No hay datos suficientes para entrenar el modelo.')

        # Log-transform target to stabilize variance: y = log(1 + revenue)
        y = np.log1p(df['revenue'].astype(float))
        X = df.copy()
        # Ensure numeric feature columns exist
        for c in self.numeric_features:
            if c not in X.columns:
                X[c] = np.nan
        # Median + sensible fallback if median is NaN (e.g., entire column missing)
        medians = X[self.numeric_features].median(numeric_only=True)
        fill_vals = {}
        for c in self.numeric_features:
            val = medians.get(c)
            if pd.isna(val):
                val = 2000.0 if c == 'release_year' else 0.0
            fill_vals[c] = float(val)
        X[self.numeric_features] = X[self.numeric_features].fillna(fill_vals)

        for c in self.categorical_features:
            if c not in X.columns:
                X[c] = None
        for c in self.categorical_features:
            X[c] = X[c].astype(str).str.lower()

        preprocessor = ColumnTransformer(
            transformers=[
                ('num', StandardScaler(), self.numeric_features),
                ('cat', OneHotEncoder(handle_unknown='ignore'), self.categorical_features),
            ]
        )

        reg = RandomForestRegressor(
            n_estimators=150,
            random_state=42,
            n_jobs=-1
        )

        self.model = Pipeline(steps=[
            ('preprocess', preprocessor),
            ('regressor', reg)
        ])
        self.model.fit(X, y)

        self.feature_names = self.numeric_features + self.categorical_features
        return len(X), self.feature_names

    def predict_revenue_by_genre(self, invest_budget: float, genre: str) -> float:
        if self.model is None:
            self.fit()

        df = self._prepare_dataframe()
        if df.empty:
            raise ValueError('No hay datos para realizar la predicción.')

        # Ensure numeric features exist to avoid KeyErrors
        for c in self.numeric_features:
            if c not in df.columns:
                df[c] = np.nan
        medians = df[self.numeric_features].median(numeric_only=True)
        # Fallbacks if medians are NaN
        def fallback(c):
            v = medians.get(c)
            if pd.isna(v):
                return 2000.0 if c == 'release_year' else 0.0
            return float(v)
        row = {
            'budget': float(invest_budget),
            'rating': fallback('rating'),
            'votes': fallback('votes'),
            'duration': fallback('duration'),
            'release_year': fallback('release_year'),
            'primary_genre': str(genre).lower(),
            'lan-detected': 'es'
        }

        X_pred = pd.DataFrame([row])
        for c in self.numeric_features:
            if c not in X_pred.columns:
                X_pred[c] = fallback(c)
            else:
                if pd.isna(X_pred.loc[0, c]):
                    X_pred.loc[0, c] = fallback(c)
        for c in self.categorical_features:
            if c not in X_pred.columns:
                X_pred[c] = ''

        # Model predicts log(1 + revenue); invert transform
        y_pred_log = self.model.predict(X_pred)[0]
        revenue = float(np.expm1(y_pred_log))
        return max(0.0, revenue)

    def predict_roi_by_genre(self, invest_budget: float, genre: str) -> float:
        revenue = self.predict_revenue_by_genre(invest_budget, genre)
        if invest_budget <= 0:
            return np.nan
        roi_pct = ((revenue - invest_budget) / invest_budget) * 100.0
        return float(roi_pct)