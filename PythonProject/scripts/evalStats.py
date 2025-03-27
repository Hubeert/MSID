import pandas as pd

from dataLoader import load_data


def compute_statistics(df):


    numCols = df.select_dtypes(include=['number']).columns
    catCols = df.select_dtypes(include=['object']).columns

    statsNum = pd.DataFrame({
        'mean': df[numCols].mean(),
        'median': df[numCols].median(),
        'min': df[numCols].min(),
        'max': df[numCols].max(),
        'std': df[numCols].std(),
        '5th_percentile': df[numCols].quantile(0.05),
        '95th_percentile': df[numCols].quantile(0.95),
        'missing_values': df[numCols].isnull().sum()
    })

    statsCat = pd.DataFrame({
        'missing_values': df[catCols].isnull().sum(),
        'unique_classes': df[catCols].nunique(),
    })

    proportions = []
    for col in df[catCols].columns:
        valueCounts = df[col].value_counts(normalize=True)
        for value, proportion in valueCounts.items():
            proportions.append([col, value, proportion])

    statsCatProp = pd.DataFrame(proportions, columns=["feature", "class", "proportion"])

    return statsNum, statsCat, statsCatProp

def save_statistics(statsNum, statsCat, statsCatProp):
    statsNum.to_csv("pngs/numeric_statistics.csv")
    statsCat.to_csv("pngs/categorical_statistics.csv")
    statsCatProp.to_csv("pngs/class_proportions.csv")

    print("Pliki zapisane poprawnie:")
    print("- numeric_statistics.csv")
    print("- categorical_statistics.csv")
    print("- class_proportions.csv")

if __name__ == "__main__":
    df = load_data("data/oral.csv")
    numStats, catStats, catPropStats = compute_statistics(df)
    print(numStats)
    print(catStats)
    print(catPropStats)
    save_statistics(numStats, catStats, catPropStats)
