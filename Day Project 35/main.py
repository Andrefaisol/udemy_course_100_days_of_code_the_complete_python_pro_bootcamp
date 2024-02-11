import requests

api_key = "003ef806f43b2c49fed4084a0b4d770c"
MY_LAT = -6.822025
MY_LNG = 110.849181
parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": api_key,
    "units": "metric"
}

weather_data = requests.get(url="https://api.openweathermap.org/data/2.5/weather", params=parameters)
weather_data.raise_for_status()
wd_json = weather_data.json()

forecast_data = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
forecast_data.raise_for_status()
fd_json = forecast_data.json()

cur_weather = wd_json["weather"][0]["description"]
cur_temp = wd_json["main"]["temp"]
cur_hum = wd_json["main"]["humidity"]
cur_city = wd_json["name"]

print(f"The weather at {cur_city} now is {cur_weather} with temperature {round(cur_temp)}C and {cur_hum} humidity")

