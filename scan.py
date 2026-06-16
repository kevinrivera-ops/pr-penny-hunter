import requests
import os


TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]


message = "🚨 TEST SUCCESS - Penny Hunter is connected!"


url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"


response = requests.post(
    url,
    data={
        "chat_id": CHAT_ID,
        "text": message
    }
)


print(response.text)
