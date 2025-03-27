from dataLoader import load_data
from boxViolinPlots import plot_boxplots, plot_violinplots
from evalStats import compute_statistics, save_statistics
from errorBars import plot_errorBars
from histPlots import plot_histplots
from correlationMatrix import correlation
from reglin import plot_regplot
from pca import plot_PCA


def main():
    #Ładowanie danych (tych komentarzy nie pisał chat gpt jak coś)
    df = load_data("data/oral.csv")
    dfOnlyCancer = df[df["Oral Cancer (Diagnosis)"] == "Yes"]

    #Przykładowe użycie evalStats
    numStats, catStats, catPropStats = compute_statistics(df)
    print(numStats)
    print(catStats)
    print(catPropStats)
    save_statistics(numStats, catStats, catPropStats)

    #Przykładowe użycie boxplotów
    plot_boxplots(dfOnlyCancer, "Tobacco Use", "Cancer Stage", "pngs/boxplotsSmokeStagev2.png", rotationX = 90)

    #Przykładowe użycie violinplotów
    plot_violinplots(dfOnlyCancer, "Tobacco Use", "Cancer Stage", "pngs/violinplotsSmokeStagev2.png", rotationX = 90)

    #Przykładowe użycie errorBars
    plot_errorBars(df, "Treatment Type", "Cost of Treatment (USD)", "pngs/errBarTreatmentCost2v2.png")

    #Przykładowe użycie histplots
    plot_histplots(df, categoryX="Oral Cancer (Diagnosis)", catHue="Alcohol Consumption", output_file="pngs/histplotCancerAlcoholv2.png")

    #Przykładowe użycie Correlation Matrix
    correlation(df, "pngs/CorrelationMatrixOralv2.png")

    #Przykładowe użycie reglin
    plot_regplot(df,"Survival Rate (5-Year, %)","Cancer Stage", output_file="pngs/regplotStageSurvivalv2.png")

    #Przykładowe użycie PCA
    plot_PCA(df, output_file="pngs/PCAv2.png")

if __name__ == "__main__":
    main()

