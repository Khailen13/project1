from typing import Generator


def filter_by_currency(transactions: list, currency: str) -> Generator:
    """Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""

    i = 0
    blank_list_message = "Список транзакций пуст"
    inappropriate_structure_message = "Несоответствующая структура данных"
    currency_lack_message = "Транзакции в запрашиваемой валюте отсутствуют"
    end_message = "Конец списка транзакций"
    is_correct_structure = False
    transaction_found = False
    while True:
        if len(transactions) == 0:
            yield blank_list_message
        elif i >= len(transactions) and not is_correct_structure:
            yield inappropriate_structure_message
        elif i >= len(transactions) and transaction_found:
            yield end_message
        elif i >= len(transactions):
            yield currency_lack_message
        elif "operationAmount" in transactions[i]:
            if "currency" in transactions[i]["operationAmount"]:
                if "code" in transactions[i]["operationAmount"]["currency"]:
                    is_correct_structure = True
                    if transactions[i]["operationAmount"]["currency"]["code"] == currency:
                        transaction_found = True
                        yield transactions[i]
        i += 1


def transaction_descriptions(transactions: list) -> Generator:
    """Возвращает описание каждой транзакции по очереди"""

    i = 0
    blank_list_message = "Список транзакций пуст"
    inappropriate_structure_message = "Несоответствующая структура данных"
    end_message = "Конец списка транзакций"
    is_correct_structure = False
    if len(transactions) == 0:
        yield blank_list_message
    else:
        while True:
            if i >= len(transactions) and not is_correct_structure:
                yield inappropriate_structure_message
            elif i >= len(transactions):
                yield end_message
            elif "description" in transactions[i]:
                is_correct_structure = True
                yield transactions[i]["description"]
            i += 1


def card_number_generator(start: int, stop: int) -> Generator:
    """Выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""

    incorrect_input_message = "Некорректный диапазон"
    if start <= 0 or start > stop or stop >= 10**16:
        yield incorrect_input_message
    else:
        card_numbers_count = 16
        for number in range(start, stop + 1):
            numbers_count = len(str(number))
            blank_pos_count = card_numbers_count - numbers_count
            card_number_conjoint = f'{blank_pos_count*"0"}{number}'
            card_number = (
                f"{card_number_conjoint[0:4]} {card_number_conjoint[4:8]} {card_number_conjoint[8:12]} "
                f"{card_number_conjoint[12:]}"
            )
            yield card_number
