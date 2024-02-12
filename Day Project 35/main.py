import requests

api_key = ""  # type for api key
MY_LAT = -6.822025
MY_LNG = 110.849181
parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "units": "metric",
    "cnt": 4,
}

weather_data = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
weather_data.raise_for_status()
wd_json = weather_data.json()

forecast_data = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
forecast_data.raise_for_status()
fd_json = forecast_data.json()

# cur_weather = wd_json["weather"][0]["description"]
# cur_temp = wd_json["main"]["temp"]
# cur_hum = wd_json["main"]["humidity"]
# cur_city = wd_json["name"]
#
# print(f"The weather at {cur_city} now is {cur_weather} with temperature {round(cur_temp)}C and {cur_hum} humidity")

for i in range(0, 4):
    cur_id = int(fd_json["list"][i]["weather"][0]["id"])
    cur_weather = fd_json["list"][i]["weather"][0]["description"]
    time = fd_json["list"][i]["dt_txt"]
    if cur_id >= 200 and cur_id <= 531:
        print(f"at time {time} bring umbrella because {cur_weather}")
    else:
        print(f"{time} the weather is {cur_weather}")

