import movie
import pandas as pd
import numpy as np

#! Limpieza de datos fecha, duración, rating, valoración, presupuesto, recaudación, guionistas, ...
class Analyzer:

# Limpieza de los datos

    # Limpiar valores vacíos de presupuesto y recaudación
    def clean_budget_revenue(self):
        df = self.movie.data
        if df is None:
            return self.movie
        cols = [c for c in ['budget','revenue'] if c in df.columns]
        if cols:
            df = df.loc[df[cols].notna().all(axis=1) & (df[cols] > 0).all(axis=1)]
            self.movie.data = df
        return self.movie
    
    # Limpiar valores vacíos en fecha de lanzamiento                
    def clean_date(self):
        df = self.movie.data
        if df is None:
            return self.movie
        if 'release_date' in df.columns:
            dt = pd.to_datetime(df['release_date'], errors='coerce')
            df = df.assign(release_date=dt).loc[dt.notna()]
            self.movie.data = df
        return self.movie
    
    # Limpiar valores vacíos con rating y votos en cero
    def clean_succesuful(self):
        df = self.movie.data
        if df is None:
            return self.movie
        cols = [c for c in ('votes','rating') if c in df.columns]
        if cols:
            df = df.loc[df[cols].notna().all(axis=1) & (df[cols] > 0).all(axis=1)]
            self.movie.data = df
        return self.movie
    
    # Limpiar valores con duración cero
    def clean_duration(self):
        df = self.movie.data
        if df is None:
            return self.movie
        if 'duration' in df.columns:
            df = df.loc[df['duration'] > 0]
            self.movie.data = df
        return self.movie       
    
# Uso de los datos para obtener información
    
    # Calculo del Retorno de Inversión (ROI)
    def calculate_roi(self):
        df = self.movie.data
        if df is None:
            return df
        cols = ['budget', 'revenue']
        if not all(c in df.columns for c in cols):
            return df
        safe = df.loc[df[cols].notna().all(axis=1) & (df['budget'] > 0)]
        roi_series = ((safe['revenue'] - safe['budget']) / safe['budget']) * 100
        out = safe.copy()
        out = out.assign(roi=roi_series)
        # keep only likely useful columns if present
        keep = [c for c in ['title', 'roi'] if c in out.columns]
        return out[keep] if keep else out

    # Calculo de la covarianza entre dos variables
    #!  Agregar etiquetas select para calcular los valores
    def calculate_covariance(self, var_a, var_b):
        df = self.movie.data
        if df is None or var_a not in df.columns or var_b not in df.columns:
            return None
        covariance = np.cov(df[var_a], df[var_b])
        return covariance

    def calculate_roi_by_genre(self, genre: str):
        df = self.movie.data
        if df is None:
            return df
        # attempt to filter by 'genres' list/str or single 'genre'
        if 'genres' in df.columns:
            def has_gen(x):
                if isinstance(x, list):
                    return genre in x
                if isinstance(x, str):
                    return genre.lower() in x.lower()
                return False
            filtered = df.loc[df['genres'].apply(has_gen)]
        elif 'genre' in df.columns:
            filtered = df.loc[df['genre'].astype(str).str.lower() == genre.lower()]
        else:
            filtered = df
        self.movie.data = filtered
        return self.calculate_roi()
    
    

    def __init__(self, movie_instance: movie.Movie):
        self.movie = movie_instance