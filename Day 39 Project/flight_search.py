import datetime
import datetime as dt
import requests


class FlightSearch:  # This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.endpoint_search = "https://api.tequila.kiwi.com/v2/search"
        self.apikey = {"apikey": "RgtNv02L8kpxL-ijM0h-YubY6C1zKvbL"}
        self.from_city = "JKT"
        self.to_city = ""
        self.date_now = dt.datetime.now().strftime("%d/%m/%Y")
        self.date_to = dt.datetime.now() + datetime.timedelta(days=6 * 30)

    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        term = {"term": city_name,
                "limit": 1}
        response = requests.get(url=self.endpoint, headers=self.apikey, params=term)
        result = response.json()["locations"]
        code = result[0]["code"]
        return code

    def get_price(self, to):
        para = {
            "fly_from": self.from_city,
            "fly_to": to,
            "date_from": self.date_now,
            "date_to": self.date_to.strftime("%d/%m/%Y"),
            "limit": 1,
            "curr": "IDR"
        }
        response = requests.get(url=self.endpoint_search, headers=self.apikey, params=para)
        data = response.json()
        city = data['data'][0]["cityTo"]
        price = data['data'][0]["price"]
        seat = data['data'][0]["availability"]['seats']
        flight_list = [city, price, seat]
        return flight_list
