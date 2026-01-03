import analyzer
import matplotlib.pyplot as plt
import seaborn as sns

class Visualizer:

    # Generación de la matriz de correlación
    def display_matrix_correlation(self, matrix):
        plt.figure(figsize=(10,8))
        sns.heatmap(
            matrix,
            annot=True,
            fmt=".2f",
            cmap='coolwarm',
            square=True,
            linewidths=0.5
        )
        plt.title('Matriz de Correlación')
        plt.show()
        plt.savefig('./static/images/correlation_matrix.png')

    def __init__(self, analyzer: analyzer.Analyzer):
        self.analyzer = analyzer
        self.movie = analyzer.movie
        self.data = analyzer.movie.data