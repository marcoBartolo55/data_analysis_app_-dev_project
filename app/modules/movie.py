import os
import pandas as pd


class Movie:
    def __init__(self, filename: str = 'peliculas.json', load: bool = True):
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.filepath = os.path.join(base_path, '..', '..', 'spyder', 'data', filename)
        self.data = None
        if load:
            self.load_data()

    def load_data(self):
        try:
            self.data = pd.read_json(self.filepath)
        except FileNotFoundError:
            print(f"Error: {self.filepath} not found.")

