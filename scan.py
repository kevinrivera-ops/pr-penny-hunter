import requests
import json


with open("watchlist.json") as f:
    products = json.load(f)


for product in products:

    keyword = product["name"]

    url = "https://www.homedepot.com/s/" + keyword.replace(" ", "%20")

    r = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    )

    print("SEARCH:")
    print(keyword)

    print("STATUS:")
    print(r.status_code)

    print("LENGTH:")
    print(len(r.text))

    print(r.text[:300])
