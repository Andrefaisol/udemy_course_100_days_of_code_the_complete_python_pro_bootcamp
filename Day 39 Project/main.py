# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

flight_search = FlightSearch()
data_manager = DataManager()
notification = NotificationManager()

data = data_manager.get_sheet()
sheet_data = data["prices"]

if sheet_data[0]["iataCode"] == "":
    for i in sheet_data:
        i["iataCode"] = flight_search.get_destination_code(i["city"])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.data = sheet_data
    data_manager.update_destination_codes()

for des in sheet_data:
    flight = flight_search.get_price(to=des["iataCode"])
    if flight[1] < des["lowestPrice"]:
        notification.send_email(city=des["city"], price=flight[1], seats=flight[2])

