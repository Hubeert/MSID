import seaborn as sns
import matplotlib.pyplot as plt

from dataLoader import load_data


def plot_regplot(df,catX, catY, output_file):
    dfTmp = df[df["Oral Cancer (Diagnosis)"] == "Yes"]
    plt.figure(figsize=(12, 8))
    sns.regplot(data=dfTmp, x=catX, y = catY, scatter_kws={"alpha": 0.5, "s": 30},line_kws={"color": "red", "lw": 2})
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.savefig(output_file)
    plt.show()

if __name__ == "__main__":
    df = load_data("data/oral.csv")
    plot_regplot(df,"Survival Rate (5-Year, %)","Cancer Stage", output_file="pngs/regplotStageSurvival.png")