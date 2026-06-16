import requests
import json


with open("watchlist.json") as f:
    products = json.load(f)


for product in products:

    product_id = product["product_id"]

    urls = [
        f"https://www.homedepot.com/p/{product_id}",
        f"https://www.homedepot.com/p/{product_id}?irgwc=1",
        f"https://www.homedepot.com/p/{product_id}?MERCH=REC"
    ]


    for url in urls:

        print("\nTESTING:")
        print(url)

        r = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0",
                "Accept-Language": "en-US,en;q=0.9"
            }
        )

        print("STATUS:", r.status_code)
        print("LENGTH:", len(r.text))
        print(r.text[:200])
        
    
