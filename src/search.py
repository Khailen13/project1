import re
from collections import Counter


def process_bank_search(transactions: list[dict], search: str) -> list[dict]:
    """Принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка"""

    try:
        corresponding_operations = [
            transaction
            for transaction in transactions
            if re.search(search.lower(), transaction["description"].lower())
        ]
        return corresponding_operations
    except Exception:
        return []


def process_bank_operations(transactions: list[dict], descriptions: list) -> dict:
    """Принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь,
    в котором ключи — это названия категорий, а значения — это количество операций в каждой категории"""

    try:
        descriptions_formatted = [description.lower() for description in descriptions]
        corresponding_transactions_descriptions = [
            transaction["description"]
            for transaction in transactions
            if transaction["description"].lower() in descriptions_formatted
        ]
        counted_descriptions = Counter(corresponding_transactions_descriptions)
        return counted_descriptions
    except Exception:
        return {}
