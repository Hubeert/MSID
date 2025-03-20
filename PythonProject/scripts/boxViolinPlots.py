import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from dataLoader import load_data


def plot_boxplots(df, category, output_file="boxplots.png"):
    num_cols = df.select_dtypes(include=['number']).columns

    plt.figure(figsize=(12, 8))
    for i, col in enumerate(num_cols, 1):
        plt.subplot(2, (len(num_cols) + 1) // 2, i)
        sns.boxplot(x=df[category], y=df[col], hue=df[category], legend=False)
        plt.xlabel(category)
        plt.ylabel(col)

    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()

def plot_violinplots(df, category, output_file="violinplots.png"):
    num_cols = df.select_dtypes(include=['number']).columns

    plt.figure(figsize=(12, 8))
    for i, col in enumerate(num_cols, 1):
        plt.subplot(2, (len(num_cols) + 1) // 2, i)
        sns.violinplot(x=df[category], y=df[col], hue=df[category], legend=False)
        plt.xlabel(category)
        plt.ylabel(col)

    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()

def plot_exact_violinplot(df, categoryX, categoryY, output_file="exact_violinplot.png"):
    df["Study_Group"] = pd.cut(df["Study_Hours_per_Week"], bins=[5,10,15,20,25,float('inf')],
                             labels=["5-10", "10-15", "15-20", "20-25", "25+"])
    plt.figure(figsize=(12, 8))
    #plt.subplot(1,2,1)
    sns.violinplot(x=df[categoryX], y=df[categoryY], hue=df[categoryX], legend=False)
    '''plt.subplot(1,2,2)
    sb.violinplot(x=df[categoryX], y=df[categoryY], hue=df[categoryX], legend=False)
    plt.xlabel(categoryX)
    plt.ylabel(categoryY)'''

    plt.tight_layout()
    plt.savefig(output_file)
    plt.show()

if __name__ == "__main__":
    df = load_data("data/gradesData.csv")
    #plot_boxplots(df, category="Gender")
    #plot_boxplots(df, category="Age")
    plot_exact_violinplot(df, categoryX="Study_Group", categoryY="Final_Score")