import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def correlation():
    df = pd.read_csv("data/players_22.csv")

    numCols = df.select_dtypes(include=['number'])

    corr_matrix = numCols.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=False, cmap="crest", fmt=".2f")
    plt.title("Macierz korelacji")
    plt.show()

if __name__ == "__main__":
    correlation()