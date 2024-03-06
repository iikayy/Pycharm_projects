# with open("weather_data.csv", "r") as file:
#     content = file.readlines()
#     print(content)
#
# import csv
# with open("weather_data.csv", "r") as file:
#     data = csv.reader(file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             a = int(row[1])
#             temperature.append(a)
#     print(temperature)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# #print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# monday = data[data.day == "Monday"]
# print(monday.temp)
#print(data[data.temp == data.temp.max()])






# with open("weather_data.csv") as weather_file:
#     data = weather_file.readlines()
# print(data)

# import csv
#
# with open("weather_data.csv") as weather_file:
#     data = csv.reader(weather_file)
#     temperatures = []
#     for row in data:
#         if "temp" != row[1]:
#             temperatures.append(int(row[1]))
#     print(temperatures)

#
# import pandas
#
# data = pandas.read_csv('weather_data.csv')
# # print(data.temp)
#
# data_dict = data.to_dict()
# temp_list = data.temp.tolist()
# # print(sum(temp_list) / len(temp_list))
# # print(data.temp.max())
#
# # print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#

# pandas.DataFrame()

import pandas

data = pandas.read_csv("2018.csv")

gray = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

squirrel = {
    "fur color": ["Gray", "Cinnamon", "Black"],
    " Count" : [gray, red, black]
}

dicti = pandas.DataFrame(squirrel)

dicti.to_csv("squirrel_count.csv")














