from dataLoader import load_data

if __name__ == "__main__":
    df = load_data("../data/gradesData.csv")
    print(df.head())