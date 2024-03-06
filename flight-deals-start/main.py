#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import date, datetime, timedelta
from data_manager import DataManager
from pprint import pprint
from flight_search import FlightSearch
from flight_data import FlightData
import requests

data_manager = DataManager()
sheet_data = data_manager.destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "LON"

for i in range(0, len(sheet_data)):
    if sheet_data[i]["iataCode"] == "":
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
            data_manager.destination_data = sheet_data
            data_manager.add_iata_code()

today = date.today()
day = today + timedelta(days=1)
tomorrow = day.strftime("%d/%m/%Y")

months = day + timedelta(days=6*30)
six_months = months.strftime("%d/%m/%Y")

# tomorrow = datetime.now() + timedelta(days=1)
# six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months
    )

