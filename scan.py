import requests
import json


with open("watchlist.json") as f:
    products = json.load(f)

with open("stores.json") as f:
    stores = json.load(f)


for product in products:

    print("\nPRODUCT:")
    print(product["name"])
    print(product["product_id"])


    for store in stores:

        print("\nCHECKING STORE:")
        print(store["store"])


        url = (
            "https://www.homedepot.com/"
            "services/buybox"
            f"?itemId={product['product_id']}"
            f"&storeId={store['zip']}"
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
    
