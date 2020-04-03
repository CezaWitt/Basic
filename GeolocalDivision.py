import numpy as np
import pandas as pd
import matplotlib as mlp
import matplotlib.pyplot as plt
winkelumrechung = np.pi / 180
reichweite  = 200 / 1.852
entfernung = reichweite *(np.pi / (180*60))
df = pd.read_csv("Geolocal.csv", names=["Breitengrad", "Laengengrad", "Kompassausrichtung"])
df["Breite"] = df["Breitengrad"] * winkelumrechung
df["Laenge"] = df["Laengengrad"] * winkelumrechung
df["Richtung"] = df["Kompassausrichtung"] * winkelumrechung
df["Lat"] = np.arcsin(np.sin(df["Breite"]) * np.cos(entfernung) + np.cos(df["Breite"]) * np.sin(entfernung) * np.cos(df["Richtung"]))
df["x_1"] = np.cos(entfernung)-(np.sin(df["Breite"])*np.sin(df["Lat"]))
df["y_1"] = np.sin(df["Richtung"])*np.sin(entfernung)*np.cos(df["Breite"])
df["dLon"] = (-1) * (np.arctan2(df["y_1"],df["x_1"]))
df["Lon"] = (df["Laenge"] - df["dLon"] + np.pi) - np.trunc((df["Laenge"] - df["dLon"] + np.pi) / 2 / np.pi) - np.pi
df["x_2"] = df["Lon"] / winkelumrechung
df["y_2"] = df["Lat"] / winkelumrechung
df.to_csv("Geolocalkomplex.csv")
print(df)
plt.ylabel("Längengrad")
plt.xlabel("Breitengrad")
plt.figure(figsize=(6,6), dpi=80)
plt.subplot(111)
plt.plot([df["Laengengrad"], df["x_2"]], [df["Breitengrad"], df["y_2"]], color='blue', linestyle='-', marker='o')
plt.axis([6, 16, 46, 56])
plt.grid(True)
#ax = plt.gca()
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#ax.spines['left'].set_position(('data',0))
#ax.spines['bottom'].set_position(('data',0))
#ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('left')
#plt.show()
plt.savefig("Koordinatensystem.png")