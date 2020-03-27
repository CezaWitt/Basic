import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
deutlschland_laenge = 876
deutschland_breite = 640
linke_raster_grenze = 47.3
rechte_raster_grenze = 54.9
untere_raster_grenze = 6.0
obere_raster_grenze = 15.0
raster_groeße = 100
korrekturwert = 270
spiegelung = (-1)
winkelumrechung = np.pi / 180
reichweite  = 2.375
horizontale_raster_groeße = (rechte_raster_grenze - linke_raster_grenze) / raster_groeße
vertikale_raster_groeße = (obere_raster_grenze - untere_raster_grenze) / raster_groeße
df = pd.read_csv("Geolocal.csv", names=["Breitengrad", "Laengengrad", "Kompassausrichtung"])
df["x_1"] = df["Breitengrad"] - linke_raster_grenze
df["y_1"] = df["Laengengrad"] - untere_raster_grenze
df["Breitenraster"] = df["x_1"] / horizontale_raster_groeße
df["Laengenraster"] = df["y_1"] / horizontale_raster_groeße
df["Breitenraster"] = df["Breitenraster"].astype(int)
df["Laengenraster"] = df["Laengenraster"].astype(int)
df["Start_Raster"] = df["Laengenraster"] * raster_groeße + df["Breitenraster"]
df["Steigung"] = np.tan(((df["Kompassausrichtung"] - korrekturwert) * spiegelung) * winkelumrechung)
df["yAchsenabschnitt"] = (df["y_1"] - (df["Steigung"] * df["x_1"]))
df["Ankathete"] = (np.cos((df["Kompassausrichtung"] - korrekturwert) * winkelumrechung) * reichweite)
df["x_2"] = df["x_1"] - df["Ankathete"]
df["y_2"] = (df["Steigung"] * df["x_2"]) + df["yAchsenabschnitt"]
df.to_csv("Geolocalkomplex.csv")
#df = df.drop(columns=["x_1", "y_1"])
df = df.drop(columns=["Breitenraster", "Laengenraster", "Steigung", "yAchsenabschnitt", "Ankathete"])
print(df)
plt.ylabel("Längengrad")
plt.xlabel("Breitengrad")
plt.figure(figsize=(6,6), dpi=80)
plt.subplot(111)
plt.plot([df["x_1"], df["x_2"]], [df["y_1"], df["y_2"]], color='blue', linestyle='-', marker='o')
plt.axis([-3, 8, -2, 10])
plt.grid(True)
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
plt.show()
plt.savefig("Koordinatensystem.png")