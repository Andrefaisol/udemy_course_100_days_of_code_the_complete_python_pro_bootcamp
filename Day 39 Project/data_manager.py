import requests
from pprint import pprint


class DataManager:  # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.shiety_get = "https://api.sheety.co/95aabfd8be11a1b64b16e245c64e968f/flightDeals/prices"
        self.data = {}

    def get_sheet(self):
        response = requests.get(url=self.shiety_get)
        self.data = response.json()
        return self.data

    def update_destination_codes(self):
        for i in self.data:
            new_data = {
                "price": {
                    "iataCode": i["iataCode"]
                }
            }
            response = requests.put(
                url=f"https://api.sheety.co/95aabfd8be11a1b64b16e245c64e968f/flightDeals/prices/{i['id']}",
                json=new_data
            )
            print(response.text)
