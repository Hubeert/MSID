from dataLoader import loadData

if __name__ == "__main__":
    df = loadData("data\gradesData.csv")
    print(df.head())