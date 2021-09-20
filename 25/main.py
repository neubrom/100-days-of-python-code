# import csv
#
# with open("weather_data.csv") as weather_data:
#     weather_read = csv.reader(weather_data)
#     print(weather_read)
#     temperature = []
#     for row in weather_read:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import numpy
import pandas as pd

data = pd.read_csv("weather_data.csv")
#print(data)