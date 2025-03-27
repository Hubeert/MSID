import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

from dataLoader import load_data


def plot_errorBars(df, catX, catY, output_file):
    plt.figure(figsize=(8, 5))
    #df["Survival Group"] = pd.cut(df["Survival Rate (5-Year, %)"], bins=5,
                               #labels=["0-20", "20-40", "40-60", "60-80", "80-100"])
    sns.barplot(x=catX, y=catY,hue = catX,
                data=df, errorbar="sd")

    plt.savefig(output_file)
    plt.show()

if __name__ == '__main__':
    df = load_data("data/oral.csv")
    plot_errorBars(df, "Treatment Type", "Cost of Treatment (USD)", "pngs/errBarTreatmentCost2.png")