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
            df = df.loc[(df[cols] > 0).all(axis=1)]
            self.movie.data = df
        return self.movie
    
    # Limpiar valores vacíos en fecha de lanzamiento                
    def clean_date(self):
        df = self.movie.data
        if df is None:
            return self.movie
        if 'release_date' in df.columns:
            dt = pd.to_datetime(df['release_date'], errors='coerce')
            df = df.loc[dt.notna()]
            self.movie.data = df
        return self.movie
    
    # Limpiar valores vacíos con rating y votos en cero
    def clean_succesuful(self):
        df = self.movie.data
        if df is None:
            return self.movie
        cols = [c for c in ('votes','rating') if c in df.columns]
        if cols:
            df = df.loc[df[cols].notna().all(axis=1)]
            self.movie.data = df
        return self.movie

    # Limpiar roles de las personas (directores, guionistas,...)
    def clean_roles(self):
        pass
     
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
    
    def calculata_roi(self):
        pass

    def calculta_covariance(self):
        pass

    def __init__(self):
        self.movie = movie
        


# Aplicación de funciones para limpiar los datos



# Análisis de los datos

