import pandas as pd


def loadData(filepath):

    try:
        df = pd.read_csv(filepath)
        print(f"Dane wczytane poprawnie! Liczba wierszy: {df.shape[0]}, kolumn: {df.shape[1]}")
        return df
    except Exception as e:
        print(f"Błąd podczas wczytywania danych: {e}")
        return None