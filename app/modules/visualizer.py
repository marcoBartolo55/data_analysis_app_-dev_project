import matplotlib.pyplot as plt
import seaborn as sns

import os

from app.modules.analyzer import Analyzer

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

class Visualizer:

    # Generación de la matriz de correlación
    def display_matrix_correlation(self, matrix):
        plt.figure(figsize=(20,10))
        try:
            if matrix is None or getattr(matrix, 'empty', False):
                plt.text(0.5, 0.5, 'Sin datos numéricos para correlación', ha='center', va='center')
                plt.axis('off')
            else:
                sns.heatmap(
                    matrix,
                    annot=True,
                    fmt=".2f",
                    cmap='coolwarm',
                    square=True,
                    linewidths=0.5
                )
            plt.title('Matriz de Correlación')
        finally:
            out = os.path.join(ROOT, 'static', 'images', 'correlation_matrix.png')
            plt.savefig(out, bbox_inches='tight')
            plt.close()
        
    def display_roi_chart(self):
        roi_data = self.analyzer.calculate_roi()
        plt.figure(figsize=(80,15))
        if roi_data is not None and not roi_data.empty:
            sns.barplot(x='title', y='roi', data=roi_data)
        plt.xticks(rotation=90)
        plt.title('Return on Investment (ROI) por Película')
        plt.xlabel('Título de la Película')
        plt.ylabel('ROI')
        plt.tight_layout()
        out = os.path.join(ROOT, 'static', 'images', 'general_roi_chart.png')
        plt.savefig(out, bbox_inches='tight')
        plt.close()
        
    def display_roi_chart_by_genre(self, genre):
        roi_data = self.analyzer.calculate_roi_by_genre(genre)
        plt.figure(figsize=(80,15))
        if roi_data is not None and not roi_data.empty:
            sns.barplot(x='title', y='roi', data=roi_data)
        plt.xticks(rotation=90)
        plt.title(f'Return on Investment (ROI) para Género: {genre}')
        plt.xlabel('Título de la Película')
        plt.ylabel('ROI')
        plt.tight_layout()
        out = os.path.join(ROOT, 'static', 'images', 'roi_chart_genre.png')
        plt.savefig(out, bbox_inches='tight')
        plt.close()
        
    def scatter_plot(self, x_var, y_var):
        plt.figure(figsize=(20,15))
        try:
            if self.data is None:
                plt.text(0.5, 0.5, 'Sin datos para graficar', ha='center', va='center')
                plt.axis('off')
            elif x_var in self.data.columns and y_var in self.data.columns:
                sns.scatterplot(x=self.data[x_var], y=self.data[y_var])
            else:
                plt.text(0.5, 0.5, 'Columnas no válidas para scatter', ha='center', va='center')
                plt.axis('off')
            plt.title(f'Scatter Plot de {x_var} vs {y_var}')
            plt.xlabel(x_var)
            plt.ylabel(y_var)
            plt.tight_layout()
        finally:
            out = os.path.join(ROOT, 'static', 'images', 'scatter_varx_vs_vary.png')
            plt.savefig(out, bbox_inches='tight')
            plt.close()

    def __init__(self, analyzer: Analyzer):
        self.analyzer = analyzer
        self.movie = analyzer.movie
        self.data = analyzer.movie.data


        