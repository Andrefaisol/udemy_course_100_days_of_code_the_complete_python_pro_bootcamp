import requests

location = requests.get(url="http://api.open-notify.org/iss-now.json")
location.raise_for_status()
data_loc = location.json()
longitude = data_loc["iss_position"]["longitude"]
latitude = data_loc["iss_position"]["latitude"]
iss_pos = (latitude, longitude)
print(iss_pos)
