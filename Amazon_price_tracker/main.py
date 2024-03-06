import requests
from bs4 import BeautifulSoup
import smtplib
import time

MY_EMAIL = "benblacck@gmail.com"
MY_PASSWORD = "nqaonvxsembaeazn"
URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"
accept_language = "en-US,en;q=0.9"

header = {
    "User-Agent": user_agent,
    "Accept-Language": accept_language,

}
response = requests.get(URL, headers=header)
amazon_webpage = response.text
# print(amazon_webpage)

soup = BeautifulSoup(amazon_webpage, "html.parser")
price_tag = soup.find(name="span", class_="a-offscreen")
price_float = float(price_tag.get_text().strip("$"))
# print(price_float)
product_title = soup.find(id="productTitle", class_="a-size-large").getText().strip()


while True:
    time.sleep(3600)
    if price_float > 98:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="benblacck@outlook.com",
                msg=f"Amazon Price Alert!!!\n\n{product_title} is now ${price_float}\n\n{URL}")
