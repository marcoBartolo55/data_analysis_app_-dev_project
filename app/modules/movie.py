import pandas as pd
import os

class Movie:
    def __init__(self, filename='peliculas.json'):
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.filepath = os.path.join(base_path, '..', '..', 'spyder', 'data', filename)
        self.data = None
        self.load_data()

    def load_data(self):
        try:
            self.data = pd.read_json(self.filepath)
        except FileNotFoundError:
            print(f"Error: {self.filepath} not found.")
