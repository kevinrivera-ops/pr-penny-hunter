import json


with open("watchlist.json") as f:
    products = json.load(f)

with open("stores.json") as f:
    stores = json.load(f)


print("PRODUCTS:")
for product in products:
    print(
        product["name"],
        product["product_id"]
    )


print("\nSTORES:")
for store in stores:
    print(
        store["store"],
        store["store_id"]
    )
    
