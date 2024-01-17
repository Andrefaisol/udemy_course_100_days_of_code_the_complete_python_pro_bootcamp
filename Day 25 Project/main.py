import csv
import pandas
with open("weather_data.csv", mode="r") as file:
    new_list = csv.reader(file)
    temperature = []
    for i in new_list:
        if i[1] != "temp":
            temperature.append(int(i[1]))

print(temperature)

data = pandas.read_csv("weather_data.csv")
print(data)
