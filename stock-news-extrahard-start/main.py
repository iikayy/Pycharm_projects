import requests
from twilio.rest import Client
from datetime import date, timedelta


PERCENTAGE = 1.5
STOCK = "Natural Gas"
COMPANY_NAME = "Henry Hub"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
stock_API_KEY = "X6XYA1GN6GHI9BQ8"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_API_KEY = "3223b850ce204258b16d4197fae14dd8"
account_sid = "AC691da70962fc0b0e6f245de6196c0c69"
auth_token = "c8e1d5fbaf70b9d998606ed55aab3705"

today = date.today()
yesterday = today - timedelta(days=1)

stock_parameters = {
    "function": "NATURAL_GAS",
    "interval": "daily",
    "apikey": stock_API_KEY,
}

news_parameters = {
    "q": COMPANY_NAME,
    "from": today,
    "to": yesterday,
    "apikey":  news_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
gas_data = response.json()
today_price = float(gas_data["data"][0]["value"])
yesterday_price = float(gas_data["data"][1]["value"])
percentage_fluctuation = (today_price - yesterday_price)/today_price * 100
up_down = None
if percentage_fluctuation > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if percentage_fluctuation >= PERCENTAGE or percentage_fluctuation <= -PERCENTAGE:
    response = requests.get(NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    news_data = response.json()
    article = news_data["articles"]
    article_slice = article[:3]

    for i in range(0, 3):
        Headline = article_slice[i]["title"]
        Brief = article_slice[i]["description"]

        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            from_="+16174010603",
            body=f"{STOCK}: {up_down}{round(percentage_fluctuation)}%\nHeadline: {Headline}\nBrief: {Brief}",
            to="+2348106262263",
        )
        print(message.status)