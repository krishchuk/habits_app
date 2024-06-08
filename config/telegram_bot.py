import os
import requests

# Получите токен бота из переменной окружения
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")


def send_telegram_message(chat_id, text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text
    }
    response = requests.post(url, json=data)
    return response.json()
