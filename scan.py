import requests
import json
import os
from bs4 import BeautifulSoup


TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]


def send_alert(message):

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        }
    )


def check_product(product):

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        product["url"],
        headers=headers
    )

    page = response.text

    soup = BeautifulSoup(
        page,
        "html.parser"
    )

    text = soup.get_text()

    if "$0.01" in text or "$0.03" in text:

        send_alert(
            f"""
🚨 PENNY DEAL FOUND

Item:
{product['name']}

Store:
{product['store']}

Link:
{product['url']}
"""
        )


with open("watchlist.json") as file:
    products = json.load(file)


for product in products:

    try:
        check_product(product)

    except Exception as error:

        print(
            product["name"],
            error
        )
