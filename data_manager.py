from pprint import pprint
import requests
import os

SHEETY_PRICES_ENDPOINT = os.environ['SHEETY_ENDPOINT']


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=f"{SHEETY_PRICES_ENDPOINT}/sheet1")
        data = response.json()
        self.destination_data = data["sheet1"]
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

    def grab_creds(self):
        response = requests.get(url=f"{SHEETY_PRICES_ENDPOINT}/sheet2")
        sheet = response.json()['sheet2']
        # print(sheet)
        for i in range(0,len(sheet)):
            email = sheet[i]['email']
            return email




