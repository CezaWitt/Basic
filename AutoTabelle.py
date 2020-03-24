import pandas as pd
df = pd.read_csv("Auto.csv", sep=";", decimal=",", skiprows=5, names = ["Hersteller", "Modell", "Kilometerstand", "Baujahr", "PS", "Zustand", "Kraftstoff", "Verbruach", "Preis"])
print(df)