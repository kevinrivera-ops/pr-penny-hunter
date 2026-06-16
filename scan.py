import requests
import json
import os
import re
from bs4 import BeautifulSoup


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


def get_price(product_url):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64)"
        )
    }

    response = requests.get(
        product_url,
        headers=headers
    )

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    text = soup.get_text(" ")

    # Find dollar amounts
    prices = re.findall(
        r"\$[\d,]+\.\d{2}",
        text
    )

    clean_prices = []

    for p in prices:
        try:
            value = float(
                p.replace("$", "")
                 .replace(",", "")
            )
            clean_prices.append(value)

        except:
            pass


    if clean_prices:
        return min(clean_prices)

    print("NO PRICE FOUND")
    print(text[:1000])

    return None



with open("watchlist.json") as f:
    products = json.load(f)



with open("prices.json") as f:
    old_prices = json.load(f)



for product in products:

    try:

        current_price = get_price(
            product["url"]
        )


        if current_price is None:
            print(
                "No price found:",
                product["name"]
            )
            continue



        name = product["name"]


        previous = old_prices.get(
            name
        )


        print(
            name,
            current_price
        )


        alert = False


        if current_price <= 5:
            alert = True


        if previous:

            drop = (
                (previous - current_price)
                / previous
            ) * 100


            if drop >= 50:
                alert = True



        if alert:

            send_alert(
f"""
🚨 DEAL ALERT

{name}

Store:
{product['store']}

Old price:
${previous if previous else "N/A"}

New price:
${current_price}

Link:
{product['url']}
"""
            )



        old_prices[name] = current_price



    except Exception as e:

        print(
            "ERROR:",
            product["name"],
            e
        )



with open(
    "prices.json",
    "w"
) as f:

    json.dump(
        old_prices,
        f,
        indent=2
    )
    
