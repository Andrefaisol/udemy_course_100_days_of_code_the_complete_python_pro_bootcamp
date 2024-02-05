import requests
import datetime as dt

MY_LAT = -6.822025
MY_LNG = 110.849181


def iss_above():
    location = requests.get(url="http://api.open-notify.org/iss-now.json")
    location.raise_for_status()
    data_loc = location.json()
    longitude = data_loc["iss_position"]["longitude"]
    latitude = data_loc["iss_position"]["latitude"]
    if MY_LAT - 5 <= float(latitude) <= MY_LAT + 5 and MY_LNG - 5 <= float(longitude) <= MY_LNG + 5:
        return True


def night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "tzid": "Asia/Jakarta",
        "formatted": 0
    }
    response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    response_json = response.json()
    sunrise_hour = response_json["results"]["sunrise"].split("T")[1].split(":")[0]
    sunset_hour = response_json["results"]["sunset"].split("T")[1].split(":")[0]
    current_hour = dt.datetime.now().hour
    if current_hour > int(sunset_hour) or current_hour < int(sunrise_hour):
        return True


def checking():
    if night() and iss_above():
        print("ISS above you")


checking()
