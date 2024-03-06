import requests
from twilio.rest import Client

WEATHER_ENDPOINT = "https://api.openweathermap.org/data/3.0/onecall"
API_KEY = "86d6c928b5c38f7db6a1a04c85270085"
MY_LAT = 4.935770
MY_L0NG = 6.272170
account_sid = "AC691da70962fc0b0e6f245de6196c0c69"
auth_token = "c8e1d5fbaf70b9d998606ed55aab3705"


parameters = {
    "lat": MY_LAT,
    "lon": MY_L0NG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(WEATHER_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_id = weather_data["hourly"][0]["weather"][0]["id"]
weather_list = [weather_data["hourly"][:12]]

will_rain = False

for hour_data in weather_list:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        from_="+16174010603",
        body="Bring an umbrella, it will rain today!!",
        to="+2348106262263",
    )
    print(message.status)
