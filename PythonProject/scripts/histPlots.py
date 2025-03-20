import matplotlib.pyplot as plt
import seaborn as sns

from dataLoader import load_data


def plot_histPlots(df, categoryX, output_file="histPlots.png"):

    plt.figure(figsize=(8, 5))
    sns.histplot(df,x=categoryX , hue="Gender", bins=10, multiple="dodge")
    plt.show()


if __name__ == "__main__":
    df = load_data("data/gradesData.csv")
    plot_histPlots(df, categoryX="Study_Hours_per_Week")