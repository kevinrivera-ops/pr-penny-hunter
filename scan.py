import requests
import json
import os


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


def get_home_depot_page(product_id):

    url = f"https://www.homedepot.com/p/{product_id}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers
    )

    return response.text



with open("watchlist.json") as f:
    products = json.load(f)



for product in products:

    page = get_home_depot_page(
        product["product_id"]
    )

    print("PAGE LENGTH:", len(page))

    print(page[:1000])
    
