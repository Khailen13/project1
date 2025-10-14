import os

import requests
from dotenv import load_dotenv

load_dotenv()


def current_converter(transaction_info: dict) -> float:
    """Принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях"""

    currency = transaction_info["operationAmount"]["currency"]["code"]
    amount = transaction_info["operationAmount"]["amount"]
    if currency == "RUB":
        return amount
    elif currency == "EUR" or currency == "USD":
        url = "https://api.apilayer.com/exchangerates_data/convert"
        api_key = os.getenv("API_KEY")
        payload = {"amount": amount, "from": currency, "to": "RUB"}
        headers = {"apikey": api_key}
        response = requests.get(url, headers=headers, params=payload)
        result = response.json()
        print(result)
        amount_converted = result["result"]
        return amount_converted
