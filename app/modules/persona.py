import pandas as pd
import os

class Person:
    def __init__(self, id, name, roles=None):
        self.id = id
        self.name = name
        self.roles = set(roles or [])

    def add_role(self, role):
        self.roles.add(role)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "roles": list(self.roles),
        }

    def __init__(self, filename='peliculas.json'):
        base_path = os.path.dirname(os.path.abspath(__file__))
        self.filepath = os.path.join(base_path, '..', '..', 'spyder', 'data', filename)
        self.data = None

    def load_data(self):
        try:
            self.data = pd.read_json(self.filepath)
        except FileNotFoundError:
            print(f"Error: {self.filepath} not found.")
