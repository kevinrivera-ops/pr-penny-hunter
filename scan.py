import requests
import json


with open("watchlist.json") as f:
    products = json.load(f)


for product in products:

    product_id = product["product_id"]

    url = f"https://www.homedepot.com/p/{product_id}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html"
    }

    r = requests.get(
        url,
        headers=headers,
        timeout=20
    )

    print("\nPRODUCT:")
    print(product["name"])

    print("STATUS:")
    print(r.status_code)

    print("SERVER:")
    print(r.headers.get("server"))

    print("LENGTH:")
    print(len(r.text))

    
