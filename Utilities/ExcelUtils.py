import pandas as pd

class Pandas:
    @staticmethod
    def dataframe():
        sheet_id = '1yEy53W2-ORurY8IWkxCglpHDN7OvixeQuqAeGZsUDB0'
        df = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv')
        return df