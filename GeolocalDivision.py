import numpy as np
import pandas as pd
deutlschland_laenge = 876
deutschland_breite = 640
linke_raster_grenze = 47.3
rechte_raster_grenze = 54.9
untere_raster_grenze = 6.0
obere_raster_grenze = 15.0
raster_groeße = 100
horizontale_raster_groeße = (rechte_raster_grenze - linke_raster_grenze) / raster_groeße
vertikale_raster_groeße = (obere_raster_grenze - untere_raster_grenze) / raster_groeße
df = pd.read_csv("Geolocal.csv", names=["Breitengrad", "Laengengrad", "Kompassausrichtung"])
df["Breitengrad_rasterpunkt"] = df["Breitengrad"] - linke_raster_grenze
df["Laengengrad_rasterpunkt"] = df["Laengengrad"] - untere_raster_grenze
df["Breitenraster"] = df["Breitengrad_rasterpunkt"] / horizontale_raster_groeße
df["Laengenraster"] = df["Laengengrad_rasterpunkt"] / vertikale_raster_groeße
df["Breitenraster"] = df["Breitenraster"].astype(int)
df["Laengenraster"] = df["Laengenraster"].astype(int)
df["Raster"] = df["Laengenraster"] * 100 + df["Breitenraster"]
df["Steigung"] = np.tan(df["Kompassausrichtung"]* np.pi / 180)
df = df.drop(columns=["Breitengrad_rasterpunkt", "Laengengrad_rasterpunkt"])
#df = df.drop(columns=["Breitenraster", "Laengenraster"])
print(df)