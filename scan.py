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


with open("watchlist.json") as f:
    products = json.load(f)


for product in products:

    print(
        "Watching:",
        product["name"]
    )


        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0",
                "Accept": "application/json"
            }
        )


        print(
            "STATUS:",
            response.status_code
        )


        print(
            response.text[:300]
        )
    
