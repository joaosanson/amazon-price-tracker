import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
PASSWORD = os.environ.get("TEST_PASSWORD")


amazon_url = "https://www.amazon.com/-/pt/dp/B092L9GF5N/ref=sr_1_2?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=2C3786KMKJB8A&keywords=ryzen+5+5600g&qid=1655304675&sprefix=ryzen+5+5600%2Caps%2C223&sr=8-2"

header = {
    "Accept-Language": "Accept-Language:",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 "
                  "Safari/537.36"
}

response = requests.get(amazon_url, headers=header)
amazon_page = response.text

soup = BeautifulSoup(amazon_page, "lxml")
price_string = soup.find("span", class_="a-offscreen").getText().split("US$")
price_float = float(price_string[1].replace(",", "."))
lowest_price = 165.11

if price_float < lowest_price:

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="joaosanson01@gmail.com",
            msg=f"Subject AMD Ryzen 5600g Price\n\nAmd Ryzen 5600g has arrived the lowest price ${price_float}\n{amazon_url}")

