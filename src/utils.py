import json


def json_reader(file_path: str) -> list:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    try:
        with open(file_path, encoding="utf-8") as file:
            transactions = json.load(file)
            if type(transactions) is not list or transactions is None or transactions == []:
                transactions = []
    except FileNotFoundError:
        transactions = []
    return transactions
