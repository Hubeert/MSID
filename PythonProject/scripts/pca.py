import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

from dataLoader import load_data


def plot_PCA(df, output_file):

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    df_numeric = df[numeric_cols].dropna()

    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df_numeric)

    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(df_scaled)

    df["PCA1"] = pca_result[:, 0]
    df["PCA2"] = pca_result[:, 1]

    plt.figure(figsize=(8, 6))
    sns.scatterplot(x="PCA1", y="PCA2", data=df, alpha=0.7, hue="Cancer Stage")
    plt.xlabel("Główna składowa 1")
    plt.ylabel("Główna składowa 2")
    plt.title("PCA - Redukcja do 2D")
    plt.savefig(output_file)
    plt.show()
    print(pca.explained_variance_ratio_)

if __name__ == "__main__":
    df = load_data("data/oral.csv")
    plot_PCA(df, output_file="pngs/PCA.png")
