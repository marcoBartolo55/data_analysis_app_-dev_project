import os
import sys

ROOT = os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0, os.path.join(ROOT, 'app', 'modules'))

from movie import Movie
from analyzer import Analyzer
from visualizer import Visualizer
import matplotlib
matplotlib.use('Agg')

 
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

def detect_and_translate_titles(save_csv=False):
    movie = Movie()
    print('Datos cargados para detección/traducción:', getattr(movie.data, 'shape', None))

    analyzer = Analyzer(movie)
    analyzer.detect_language()

    df = analyzer.movie.data
    print('Columnas disponibles:', list(df.columns))
    if 'lan-detected' in df.columns:
        counts = df['lan-detected'].value_counts(dropna=False).to_dict()
        print('Idiomas detectados (conteo):', counts)
    else:
        print('No se pudo detectar idioma: columna lan-detected ausente')

    if 'title-translated' in df.columns:
        preview = df[['title', 'lan-detected', 'title-translated']].head(10)
        print('Vista previa traducciones (primeras 10 filas):')
        print(preview)

    if save_csv:
        out_path = os.path.join(ROOT, 'static', 'translations.csv')
        try:
            df.to_csv(out_path, index=False)
            print('CSV guardado:', os.path.exists(out_path), out_path)
        except Exception as e:
            print('Error al guardar CSV:', e)

def ml_train():
    # Importar perezosamente para no romper otros endpoints si ML no está disponible
    try:
        from machine_learning import MachineLearning
    except Exception as e:
        raise RuntimeError(f"Machine Learning no disponible: {e}")

    movie = Movie()
    print('Datos cargados para ML:', getattr(movie.data, 'shape', None))

    ml = MachineLearning(movie)
    try:
        rows, features = ml.fit()
        print('Modelo entrenado con filas:', rows)
        print('Features usadas:', features)
        return {
            'rows': rows,
            'features': features
        }
    except Exception as e:
        print('Error entrenando ML:', e)
        raise

def ml_predict(budget: float, genre: str):
    # Importar perezosamente para no romper otros endpoints si ML no está disponible
    try:
        from machine_learning import MachineLearning
    except Exception as e:
        raise RuntimeError(f"Machine Learning no disponible: {e}")

    movie = Movie()
    ml = MachineLearning(movie)
    try:
        # Ensure model trained
        ml.fit()
        revenue = ml.predict_revenue_by_genre(budget, genre)
        roi = ml.predict_roi_by_genre(budget, genre)
        print(f'Predicción -> género: {genre}, presupuesto: {budget}, ingreso: {revenue}, ROI: {roi}%')
        return {
            'genre': genre,
            'budget': budget,
            'predicted_revenue': revenue,
            'predicted_roi_pct': roi
        }
    except Exception as e:
        print('Error prediciendo ML:', e)
        raise