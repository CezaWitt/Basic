import pandas as pd
df = pd.read_csv("Auto.csv", sep=";", decimal=",", index_col=["Hersteller","Modell"])
print(df.sort_index())