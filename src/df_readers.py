import pandas as pd


def csv_reader(file_path: str) -> list:
    """Функция для считывания финансовых операций из CSV:
    принимает путь к файлу CSV в качестве аргумента и выдает список словарей с транзакциями."""

    try:
        with open(file_path, encoding="utf-8"):
            transactions = pd.read_csv(file_path, delimiter=";")
            transactions_dict = transactions.to_dict(orient="records")
            return transactions_dict
    except FileNotFoundError:
        return []


def excel_reader(file_path: str) -> list:
    """Функция для считывания финансовых операций из Excel:
    принимает путь к файлу Excel в качестве аргумента и выдает список словарей с транзакциями."""

    try:
        with open(file_path, encoding="utf-8"):
            transactions = pd.read_excel(file_path)
            print(transactions)
            transactions_dict = transactions.to_dict(orient="records")
            return transactions_dict
    except FileNotFoundError:
        return []
