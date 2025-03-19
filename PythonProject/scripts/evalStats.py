import pandas as pd

from dataLoader import loadData


def compute_statistics(df):

    # Statystyki dla cech numerycznych
    numCols = df.select_dtypes(include=['number']).columns
    catCols = df.select_dtypes(include=['object']).columns
    nonuniqueCatCols = [col for col in catCols if df[col].nunique() < len(df[col]) * 0.05]

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
    for col in df[nonuniqueCatCols].columns:
        valueCounts = df[col].value_counts(normalize=True)
        for value, proportion in valueCounts.items():
            proportions.append([col, value, proportion])

    statsCatProp = pd.DataFrame(proportions, columns=["feature", "class", "proportion"])

    return statsNum, statsCat, statsCatProp

def save_statistics(statsNum, statsCat, statsCatProp):
    statsNum.to_csv("numeric_statistics.csv")
    statsCat.to_csv("categorical_statistics.csv")
    statsCatProp.to_csv("class_proportions.csv")

    print("Pliki zapisane poprawnie:")
    print("- numeric_statistics.csv")
    print("- categorical_statistics.csv")
    print("- class_proportions.csv")

if __name__ == "__main__":
    numStats, catStats, catPropStats = compute_statistics(loadData("data/gradesData.csv"))
    print(numStats)
    print(catStats)
    print(catPropStats)
    save_statistics(numStats, catStats, catPropStats)
