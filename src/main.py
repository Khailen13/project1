import os

from src.df_readers import csv_reader, excel_reader
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.search import process_bank_search
from src.utils import json_reader, root_dir_path
from src.widget import get_date, mask_account_card


def requester(question: str, possible_answers: list, positions_name: str = "Вариант") -> str:
    """Запрашивает информацию у пользователя:
    задает вопрос и принимает ответ только из списка возможных, иначе процесс повторяется"""
    print(question)
    user_answer = input("\nПользователь: ")
    while user_answer.upper() not in possible_answers:
        print(f"\nПрограмма: {positions_name} {user_answer} недоступен")
        user_answer = input("\nПользователь: ")
    return user_answer.upper()


def main() -> None:
    """Отвечает за основную логику проекта и связывает функциональности между собой"""

    # Приветствие
    print("Программа: Привет! Добро пожаловать в программу работы\nс банковскими транзакциями.")

    # Выбор формата входного файла о транзакциях и загрузка информации
    question = """Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла"""
    possible_answers = ["1", "2", "3"]
    user_choice = requester(question, possible_answers)
    transactions_files = {
        "1": {"format": "JSON", "file": "operations.json"},
        "2": {"format": "CSV", "file": "transactions.csv"},
        "3": {"format": "XLSX", "file": "transactions_excel.xlsx"},
    }
    print(f"\nПрограмма: Для обработки выбран {transactions_files[user_choice]["format"]}-файл.")
    transactions_file_path = os.path.join(str(root_dir_path), "data", transactions_files[user_choice]["file"])
    if user_choice == "1":
        transactions = json_reader(transactions_file_path)
    elif user_choice == "2":
        transactions = csv_reader(transactions_file_path)
    else:
        transactions = excel_reader(transactions_file_path)

    # Выбор статуса операции
    question = (
        "\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию."
        "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )
    possible_answers = ["EXECUTED", "CANCELED", "PENDING"]
    positions_name = "Статус операции"
    user_choice = requester(question, possible_answers, positions_name)
    transactions = filter_by_state(transactions, user_choice)
    print(f"\nПрограмма: Операции отфильтрованы по статусу {user_choice}")

    # Сортировка по дате
    question = "\nПрограмма: Отсортировать операции по дате? Да/Нет"
    possible_answers = ["ДА", "НЕТ"]
    user_choice = requester(question, possible_answers)
    if user_choice == "ДА":
        question = "\nПрограмма: Отсортировать по возрастанию или по убыванию?"
        possible_answers = ["ПО ВОЗРАСТАНИЮ", "ПО УБЫВАНИЮ"]
        user_choice = requester(question, possible_answers)
        reverse_order = True
        if user_choice == "ПО ВОЗРАСТАНИЮ":
            reverse_order = False
        transactions = sort_by_date(transactions, reverse_order)

    # Фильтрация рублевых транзакций
    question = "\nПрограмма: Выводить только рублевые транзакции? Да/Нет"
    possible_answers = ["ДА", "НЕТ"]
    user_choice = requester(question, possible_answers)
    if user_choice == "ДА":
        transactions_filtered_by_currency = []
        iterator = filter_by_currency(transactions, "RUB")
        end_message = "Конец списка транзакций"
        while next(iterator) != end_message:
            transactions_filtered_by_currency.append(next(iterator))
        transactions = transactions_filtered_by_currency

    # Фильтрация по определенному слову в описании
    question = "\nПрограмма: Отфильтровать список транзакций по определенному слову\nв описании? Да/Нет"
    possible_answers = ["ДА", "НЕТ"]
    user_choice = requester(question, possible_answers)
    if user_choice == "ДА":
        print("\nПрограмма: Введите искомое слово в описании.")
        user_search_word = input("\nПользователь: ")
        transactions = process_bank_search(transactions, user_search_word)
        print(f'\nПрограмма: Операции отфильтрованы по слову "{user_search_word}"')

    # Вывод транзакций
    if len(transactions) == 0:
        print("\nПрограмма: Не найдено ни одной транзакции, подходящей под ваши\nусловия фильтрации")
    else:
        print(
            f"\nПрограмма: Распечатываю итоговый список транзакций..."
            f"\n\nПрограмма:\nВсего банковских операций в выборке: {len(transactions)}"
        )

        for transaction in transactions:
            # Дата и описание
            date = get_date(transaction["date"])
            description = transaction["description"]
            print(f"\n{date} {description}")

            # Замаскированные номера карт и счетов
            masked_from_part = ""
            if "from" in transaction:
                masked_from_part = f"{mask_account_card(transaction["from"])} -> "
            masked_info = masked_from_part + mask_account_card(transaction["to"])
            print(masked_info)

            # Сумма
            amount = transaction["operationAmount"]["amount"]
            currency_name = transaction["operationAmount"]["currency"]["name"]
            print(f"Сумма: {amount} {currency_name}")
