import json
import os
from playwright.sync_api import sync_playwright


TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]


def send_alert(message):

    import requests

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message
        }
    )


def get_page(product_id):

    url = f"https://www.homedepot.com/p/{product_id}"

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        page = browser.new_page(
            user_agent=(
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64)"
            )
        )

        page.goto(
            url,
            wait_until="networkidle",
            timeout=60000
        )

        content = page.content()

        browser.close()

        return content



with open("watchlist.json") as f:
    products = json.load(f)


for product in products:

    html = get_page(
        product["product_id"]
    )

    print(
        product["name"],
        "HTML LENGTH:",
        len(html)
    )

    if "$0.01" in html or "$0.03" in html:

        send_alert(
f"""
🚨 PENNY DEAL FOUND

{product['name']}

Store:
{product['store']}

Product ID:
{product['product_id']}
"""
        )
    
