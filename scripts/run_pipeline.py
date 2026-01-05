import os
import sys

ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(ROOT, 'app', 'modules'))

from movie import Movie
from analyzer import Analyzer
from visualizer import Visualizer
import matplotlib
matplotlib.use('Agg')

def roi_analysis():
    movie = Movie()
    print('Datos cargados para análisis financiero:', getattr(movie.data, 'shape', None))
    
    analyzer = Analyzer(movie)
    analyzer.clean_budget_revenue()
    print('Filas tras limpieza:', len(analyzer.movie.data))
    
    analyzer.calculate_roi()
    

def succesuful_analysis():
    movie = Movie()
    print(('Datos cargados para análisis de éxito:', getattr(movie.data, 'shape', None)))
    
    analyzer = Analyzer(movie)

def matrix_correlation():
    movie = Movie()
    print('Datos cargados:', getattr(movie.data, 'shape', None))

    analyzer = Analyzer(movie)
    analyzer.clean_budget_revenue()
    analyzer.clean_date()
    analyzer.clean_succesuful()
    analyzer.clean_duration()
    print('Filas tras limpieza:', len(analyzer.movie.data))
    
    num = analyzer.movie.data.select_dtypes(include='number')
    corr = num.corr()
    visualizer = Visualizer(analyzer)

    os.chdir(ROOT)
    visualizer.display_matrix_correlation(corr)
    img_path = os.path.join(ROOT, 'static', 'images', 'correlation_matrix.png')
    print('Imagen guardada:', os.path.exists(img_path), img_path)
    
def roi_chart():
    movie = Movie()
    print('Datos cargados para análisis de ROI:', getattr(movie.data, 'shape', None))
    
    analyzer = Analyzer(movie)
    visualizer = Visualizer(analyzer)
    
    os.chdir(ROOT)
    visualizer.display_roi_chart()
    img_path = os.path.join(ROOT, 'static', 'images', 'general_roi_chart.png')
    print('Imagen guardada:', os.path.exists(img_path), img_path)
    
def roi_chart_by_genre(genre):
    movie = Movie()
    print(f'Datos cargados para análisis de ROI por género ({genre}):', getattr(movie.data, 'shape', None))
    
    analyzer = Analyzer(movie)
    visualizer = Visualizer(analyzer)
    
    os.chdir(ROOT)
    visualizer.display_roi_chart_by_genre(genre)
    img_path = os.path.join(ROOT, 'static', 'images', 'roi_chart_genre.png')
    print('Imagen guardada:', os.path.exists(img_path), img_path)

def scatter_plot(x_var, y_var):
    movie = Movie()
    print(f'Datos cargados para scatter plot ({x_var} vs {y_var}):', getattr(movie.data, 'shape', None))
    
    analyzer = Analyzer(movie)
    visualizer = Visualizer(analyzer)
    
    os.chdir(ROOT)
    visualizer.scatter_plot(x_var, y_var)
    img_path = os.path.join(ROOT, 'static', 'images', 'scatter_varx_vs_vary.png')
    print('Imagen guardada:', os.path.exists(img_path), img_path)



if __name__ == '__main__':
    matrix_correlation()
