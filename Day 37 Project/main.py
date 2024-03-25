import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"
user_profile = "https://pixe.la/@permisipaket"
token = "t1kt0kt1kt0kbo1s"
username = "permisipaket"

# response = requests.post(url=pixela_endpoint, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{username}/graphs"
header = {
    "X-USER-TOKEN": token,
}
grap_param = {
    "id": "read1",
    "name": "Reading Progress",
    "unit": "pages",
    "type": "int",
    "color": "sora",
}
# graph_response = requests.post(url=graph_endpoint, json=grap_param, headers=header)
# print(graph_response.text)
date = datetime.datetime.now()
today = date.strftime("%Y%m%d")
pages = input("How many pages you read today?")
pixel_endpt = f"{graph_endpoint}/read1"
pixel_param = {
    "date": today,
    "quantity": pages,
}
pixel_response = requests.post(url=pixel_endpt, json=pixel_param, headers=header)
print(pixel_response.text)

day_to_update = datetime.datetime(year=2024, month=2, day=20)
formatted_day = day_to_update.strftime("%Y%m%d")
pixel_param_update = {
    "quantity": "10",
}
# pixel_response_update = requests.put(url=f"{pixel_endpt}/{formatted_day}", json=pixel_param_update, headers=header)
# print(pixel_response_update.text)

# pixel_delete = requests.delete(url=f"{pixel_endpt}/{formatted_day}", headers=header)
# print(pixel_delete.text)
