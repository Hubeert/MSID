import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from dataLoader import load_data


def plot_boxplots(df, categoryX, categoryY, output_file, rotationX = 0, rotationY = 0):

    plt.figure(figsize=(12, 8))
    sns.boxplot(x=df[categoryX], y=df[categoryY], hue=df[categoryX], legend=False)
    plt.xlabel(categoryX)
    plt.ylabel(categoryY)
    plt.xticks(rotation=rotationX)
    plt.yticks(rotation=rotationY)

    plt.tight_layout()
    plt.savefig(output_file)


def plot_violinplots(df, categoryX, categoryY, output_file, rotationX = 0, rotationY = 0):

    plt.figure(figsize=(12, 8))
    sns.violinplot(x=df[categoryX], y=df[categoryY], hue=df[categoryX], legend=False)
    plt.xlabel(categoryX)
    plt.ylabel(categoryY)
    plt.xticks(rotation = rotationX)
    plt.yticks(rotation = rotationY)

    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()

if __name__ == "__main__":
    df = load_data("data/oral.csv")
    df = df[df["Oral Cancer (Diagnosis)"] == "Yes"]
    plot_boxplots(df, "Tobacco Use", "Cancer Stage", "pngs/boxplotsSmokeStage.png", rotationX = 90)
