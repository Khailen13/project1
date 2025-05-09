import pytest

from src.generators import filter_by_currency


def test_filter_by_currency_1(transactions):
    """Проверка вывода двух первых транзакций по валюте(code) 'USD'"""

    filter_function = filter_by_currency(transactions, "USD")
    assert next(filter_function) == {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    assert next(filter_function) == {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }


def test_filter_by_currency_2():
    """Проверка на пустой входной список транзакций"""

    currency_lack_message = "Транзакции в запрашиваемой валюте отсутствуют"
    blank_list_message = "Список транзакций пуст"
    inappropriate_structure_message = "Несоответствующая структура данных"
    filter_function = filter_by_currency([], "USD")
    assert next(filter_function) == blank_list_message


def test_filter_by_currency_3(transactions):
    """Проверка на запрос отсутствующей валюты"""

    currency_lack_message = "Транзакции в запрашиваемой валюте отсутствуют"
    filter_function = filter_by_currency(transactions, "EUR")
    assert next(filter_function) == currency_lack_message


def test_filter_by_currency_4():
    """Проверка на соответствие структуры входного списка ожидаемой"""

    inappropriate_structure_message = "Несоответствующая структура данных"
    filter_function = filter_by_currency(
        [
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            }
        ],
        "USD",
    )
    assert next(filter_function) == inappropriate_structure_message
