import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from dataLoader import load_data


def plotErrorBars(df, output_file="errorBars.png"):
    plt.figure(figsize=(8, 5))
    df["Study_Group"] = pd.cut(df["Study_Hours_per_Week"], bins=[0, 5, 10, 15, 20, 25, float('inf')],
                               labels=["0-5", "5-10", "10-15", "15-20", "20-25", "25+"])
    sns.barplot(x="Study_Group", y="Final_Score", data=df, errorbar="sd")
    plt.show()

if __name__ == '__main__':
    df = load_data("data/gradesData.csv")
    plotErrorBars(df)