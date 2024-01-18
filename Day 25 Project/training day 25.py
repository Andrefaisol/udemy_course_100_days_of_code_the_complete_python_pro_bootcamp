import csv
import pandas
# with open("weather_data.csv", mode="r") as file:
#     new_list = csv.reader(file)
#     temperature = []
#     for i in new_list:
#         if i[1] != "temp":
#             temperature.append(int(i[1]))
#
# data = pandas.read_csv("weather_data.csv")
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# #
# # data_mean = data["temp"].mean()
# # print(round(data_mean, 2))
# #
# # data_max = data["temp"].max()
# # print(data_max)
#
# # print(data[data.temp == data.temp.max()])
# # data.to_csv("new_weather.csv")
# #
# # class_dict = {
# #     "students": ["George", "Lara", "Sieghart"],
# #     "score": [77, 78, 82]
# # }
# # to_new = pandas.DataFrame(class_dict)
# # to_new.to_csv("class_score.csv")
# to_read = pandas.read_csv("class_score.csv")
# print(to_read)

squirel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
total_gray = len(squirel_data[squirel_data["Primary Fur Color"] == 'Gray'])
total_black = len(squirel_data[squirel_data["Primary Fur Color"] == 'Black'])
total_cinnamon = len(squirel_data[squirel_data["Primary Fur Color"] == 'Cinnamon'])

squi_new_dict = {
    "Color": ["Gray", "Black", "Cinnamon"],
    "Population": [total_gray, total_black, total_cinnamon]
}
new_data = pandas.DataFrame(squi_new_dict)
new_data.to_csv("squirrel_population")
