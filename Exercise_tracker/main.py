import requests
from datetime import datetime
import os

APP_ID = os.environ.get("NUTRITION_IX_APP_ID")
API_KEY = os.environ.get("NUTRITION_IX_API_KEY")
exercise_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_ENDPOINT = os.environ.get("SHEETY_API_ENDPOINT")
USERNAME = os.environ.get("SHEETY_WORKOUTS_USERNAME")
PASSWORD = os.environ.get("SHEETY_WORKOUTS_PASSWORD")
GENDER = "male"
WEIGHT = "72"
HEIGHT = "170"
AGE = "30"

query_input = input("Tell me which exercises you did: ")
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

request_body = {
     "query": query_input,
     "gender": GENDER,
     "weight_kg": WEIGHT,
     "height_cm": HEIGHT,
     "age": AGE,
}

response = requests.post(exercise_ENDPOINT, json=request_body, headers=header)
response.raise_for_status()
result = response.json()

today = datetime.now()
date_string = today.strftime("%d/%m/%Y")
time_string = today.strftime("%X")

for exercise in result["exercises"]:
    data_for_sheet = {
        "workout": {
            "date": date_string,
            "time": time_string,
            "exercise": exercise["user_input"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(sheet_ENDPOINT, json=data_for_sheet,  auth=(USERNAME, PASSWORD))
    sheet_response.raise_for_status()

    print(sheet_response.json())
