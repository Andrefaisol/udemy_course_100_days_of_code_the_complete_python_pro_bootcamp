import csv
import pandas
with open("weather_data.csv", mode="r") as file:
    new_list = csv.reader(file)
    temperature = []
    for i in new_list:
        if i[1] != "temp":
            temperature.append(int(i[1]))

data = pandas.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# data_mean = data["temp"].mean()
# print(round(data_mean, 2))
#
# data_max = data["temp"].max()
# print(data_max)

print(data[data.temp == data.temp.max()])
