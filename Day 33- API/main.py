import time
import requests
import datetime as dt
import smtplib

MY_LAT = 4.935770
MY_L0NG = 6.272170
MY_EMAIL = "benblacck@gmail.com"
MY_PASSWORD = "nqaonvxsembaeazn"


def position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    if MY_LAT + 5 <= iss_latitude or MY_LAT - 5 >= iss_latitude and MY_L0NG + 5 <= iss_longitude or MY_L0NG -5 >= iss_longitude:
        return True


def iss_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_L0NG,
        "formatted": 0,
    }

    response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    for num in range(sunset, sunrise, -1):
        return True


while True:
    time.sleep(60)
    if position() and iss_dark():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="benblacck@outlook.com",
                msg=f"Subject:Prepare to be amazed\n\nLook up!!!")
