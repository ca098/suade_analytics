import os
import pandas as pd


class CsvService:
    def __init__(self):
        self.dir_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

    def read_csv(self, filename):
        try:
            df = pd.read_csv(os.path.join(self.dir_path, filename))
            return df
        except OSError as e:
            print(f'Could not read/open file: {e}')

