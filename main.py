import random
import csv
writer = csv.writer(open("Geolocal.csv","w"))
WertA = float
WertB = float
WertC = float
Punkt = 0
while Punkt < 20:
    WertA = round(random.uniform(47.300,54.900), 3)
    WertB = round(random.uniform(6.000,15.000), 3)
    WertC = round(random.uniform(0.000,360.000), 3)
    writer.writerow([WertA,WertB,WertC])
    Punkt += 1