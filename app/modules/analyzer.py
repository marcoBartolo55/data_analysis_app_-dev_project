import movie
import pandas as pd
import numpy as np
import os
from googletrans import Translator

#! Limpieza de datos fecha, duración, rating, valoración, presupuesto, recaudación, guionistas, ...

translator = Translator()

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
        keep = [c for c in ['title', 'roi'] if c in out.columns]
        return out[keep] if keep else out

    # Calculo de la covarianza entre dos variables
    def calculate_covariance(self, var_a, var_b):
        df = self.movie.data
        if df is None or var_a not in df.columns or var_b not in df.columns:
            return None
        covariance = np.cov(df[var_a], df[var_b])
        return covariance

    # Calculo del ROI por género
    def calculate_roi_by_genre(self, genre: str):
        df = self.movie.data
        if df is None:
            return df
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
    
    
    def detect_language(self):
        df = self.movie.data
        if df is None:
            return self.movie
        if 'title' in df.columns:
            titles = df['title'].astype(str)
            cache = {}
            trans_cache = {}

            def detect_one(t):
                if not t or t.lower() == 'nan':
                    return None
                if t in cache:
                    return cache[t]
                try:
                    res = translator.detect(t)
                    lang = getattr(res, 'lang', None)
                    cache[t] = lang
                    return lang
                except Exception:
                    return None

            df = df.assign(**{'lan-detected': titles.apply(detect_one)})

            def translate_if_needed(t, lang):
                if not t or t.lower() == 'nan':
                    return None
                if lang is None:
                    return None
                if str(lang).lower() in ('es', 'en'):
                    return t
                key = (t, 'es')
                if key in trans_cache:
                    return trans_cache[key]
                try:
                    res = translator.translate(t, dest='es')
                    text = getattr(res, 'text', t)
                    trans_cache[key] = text
                    return text
                except Exception:
                    return t

            df = df.assign(**{
                'title-translated': df.apply(lambda row: translate_if_needed(str(row['title']), row['lan-detected']), axis=1)
            })
            self.movie.data = df
            return self.movie
        else:
            df = df.copy()
            df['lan-detected'] = None
            df['title-translated'] = None
            self.movie.data = df
            return self.movie
        
        
    def translate_titles(self):
        df = self.movie.data
        if df is None:
            return self.movie
        if 'title' in df.columns:
            titles = df['title'].astype(str)
            cache = {}
            
            def translate_one(t):
                if not t or t.lower() == 'nan':
                    return t
                if t in cache:
                    return cache[t]
                try:
                    res = translator.translate(t, dest='en')
                    translated = getattr(res, 'text', t)
                    cache[t] = translated
                    return translated
                except Exception:
                    return t

            df = df.assign(**{'title-translated': titles.apply(translate_one)})
            self.movie.data = df
            return self.movie
        else:
            df = df.copy()
            df['title-translated'] = None
            self.movie.data = df
            return self.movie
        
    def transform_to_json(self, path: str = None, filename: str = 'peliculas_procesadas.json', orient: str = None, lines: bool = False, date_format: str = 'iso', force_ascii: bool = False):
        df = self.movie.data
        if df is None:
            return None
        orient = orient or getattr(self.movie, 'json_orientation', 'records')
        
        df2 = df.copy()
        import json as _json
        for col in df2.columns:
            try:
                if df2[col].apply(lambda x: isinstance(x, (list, tuple))).any():
                    df2[col] = df2[col].apply(lambda x: ', '.join(map(str, x)) if isinstance(x, (list, tuple)) else x)
                elif df2[col].apply(lambda x: isinstance(x, dict)).any():
                    df2[col] = df2[col].apply(lambda x: _json.dumps(x, ensure_ascii=force_ascii) if isinstance(x, dict) else x)
            except Exception:
                continue
        
        if path:
            out_dir = os.path.abspath(path)
        else:
            base_dir = os.path.dirname(os.path.abspath(self.movie.filepath))
            out_dir = os.path.join(base_dir, 'processed')
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, filename)
        # Ensure we write with UTF-8 and proper options for grid.js (array of objects)
        df2.to_json(path_or_buf=out_path, orient=orient, lines=lines, date_format=date_format, force_ascii=force_ascii)
        return out_path


    def __init__(self, movie_instance: movie.Movie):
        self.movie = movie_instance