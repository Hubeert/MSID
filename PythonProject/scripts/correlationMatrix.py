import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from dataLoader import load_data

def correlation(df, outputFile):

    dfTmp = df.replace({'Male':1, 'Female':0, 'Yes': 1, 'No': 0})

    numCols = dfTmp.select_dtypes(include=['number']).columns
    excludedCols = {"Age","Tobacco Use","Alcohol Consumption","HPV Infection","Betel Quid Use","Chronic Sun Exposure","Poor Oral Hygiene","Family History of Cancer","Compromised Immune System"}
    corrCols = [col for col in numCols if col not in excludedCols]

    corr_matrix = dfTmp[corrCols].corr()

    plt.figure(figsize=(12,12))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Macierz korelacji")
    plt.tight_layout()
    plt.yticks(fontsize=8)
    plt.xticks(fontsize=8)
    plt.savefig(outputFile)
    plt.show()

if __name__ == "__main__":
    df = load_data("data/oral.csv")
    correlation(df, "pngs/CorrelationMatrixOral.png")