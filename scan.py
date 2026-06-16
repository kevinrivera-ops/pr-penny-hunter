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


def get_home_depot_price(product_id):

    url = f"https://www.homedepot.com/p/{product_id}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(
        url,
        headers=headers
    )

    return r.text



with open("watchlist.json") as f:
    products = json.load(f)



for product in products:

    page = get_home_depot_price(
        product["product_id"]
    )

    print(
        product["name"],
        len(page)
    )


    if "0.01" in page or "0.03" in page:

        send_alert(
f"""
🚨 PENNY DEAL FOUND

{product['name']}

Store:
{product['store']}

Product:
{product['product_id']}
"""
        )    
    
