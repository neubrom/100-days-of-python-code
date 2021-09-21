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

# data = pd.read_csv("weather_data.csv")
# print(data)
# df = pd.DataFrame(data)
# mean_df_mean = round(df['temp'].mean(), 2)
# mean_df_max = round(df['temp'].max(), 2)
# print("Mean temp:" + f"{mean_df_mean}")
# print("Max temp:" + f"{mean_df_max}")

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
#print(data)
grey_count = len(data[data["Primary Fur Color"] == "Gray"])
red_count = len(data[data["Primary Fur Color"] == "Black"])
black_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, red_count, black_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")