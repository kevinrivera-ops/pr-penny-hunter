import json
import os
import requests


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

    # Temporary placeholder
    # Later this connects to product data

    print(
        "Checking:",
        product["name"]
    )



with open("watchlist.json") as f:

    products = json.load(f)



for product in products:

    check_product(product)
    
