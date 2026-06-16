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


def get_product_data(product_id):

    url = f"https://www.homedepot.com/StorefrontService/catalog/v2/p/{product_id}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    response = requests.get(
        url,
        headers=headers
    )

    print("STATUS:", response.status_code)

    return response.json()



with open("watchlist.json") as f:
    products = json.load(f)



for product in products:

    try:

        data = get_product_data(
            product["product_id"]
        )


        print(
            json.dumps(
                data,
                indent=2
            )[:1000]
        )


    except Exception as e:

        print(
            "ERROR:",
            product["name"],
            e
        )
        
    
