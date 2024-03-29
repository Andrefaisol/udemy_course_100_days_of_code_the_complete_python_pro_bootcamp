from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/95aabfd8be11a1b64b16e245c64e968f/flightDeals/prices"
user_get_endpoint = "https://api.sheety.co/95aabfd8be11a1b64b16e245c64e968f/flightDeals/users"

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_data(self):
        response = requests.get(url=user_get_endpoint)
        self.customer_data = response.json()["users"]
        return self.customer_data

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
