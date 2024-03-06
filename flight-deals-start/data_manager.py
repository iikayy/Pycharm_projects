import requests
from pprint import pprint

sheet_ENDPOINT = "https://api.sheety.co/9c878535945b55a2d9735e35783b403d/flightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.sheet_data = {}

    def destination_data(self):
        response = requests.get(sheet_ENDPOINT)
        result = response.json()
        self.sheet_data = result["prices"]
        return self.sheet_data

    def add_iata_code(self):
        for city in self.sheet_data:
            data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{sheet_ENDPOINT}/{city['id']}", json=data)
            pprint(response.text)

