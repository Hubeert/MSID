import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from dataLoader import load_data


def plot_histplots(df, categoryX, catHue, output_file):

    #df = df[df["Oral Cancer (Diagnosis)"] == "Yes"]
    plt.figure(figsize=(8, 5))
    sns.histplot(df,x=categoryX, hue=catHue, multiple="dodge")
    plt.savefig(output_file)
    plt.show()

    '''df1 = df[df["Treatment Type"] == "Chemotherapy"]
    df1 = df1[50 < df1["Survival Rate (5-Year, %)"]]
    df1 = df1[df1["Survival Rate (5-Year, %)"] < 60]
    print(df1)'''


if __name__ == "__main__":
    df = load_data("data/oral.csv")
    plot_histplots(df, categoryX="Oral Cancer (Diagnosis)", catHue="Alcohol Consumption", output_file="pngs/histplotCancerAlcohol.png")