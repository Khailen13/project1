import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


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

    blank_list_message = "Список транзакций пуст"
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


def test_filter_by_currency_5(transactions):
    """Проверка случая превышения количества запросов соответствующего количества транзакций"""

    end_message = "Конец списка транзакций"
    filter_function = filter_by_currency(transactions, "RUB")
    assert next(filter_function) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }
    assert next(filter_function) == {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    }
    assert next(filter_function) == end_message


def test_transaction_descriptions_1(transactions):
    """Проверка вывода описаний 5 транзакций"""

    transaction_description = transaction_descriptions(transactions)
    assert (next(transaction_description)) == "Перевод организации"
    assert (next(transaction_description)) == "Перевод со счета на счет"
    assert (next(transaction_description)) == "Перевод со счета на счет"
    assert (next(transaction_description)) == "Перевод с карты на карту"
    assert (next(transaction_description)) == "Перевод организации"


def test_transaction_descriptions_2(transactions):
    """Проверка вывода описаний транзакций большего количества, чем в исходном списке"""

    end_message = "Конец списка транзакций"
    transaction_description = transaction_descriptions(transactions)
    assert (next(transaction_description)) == "Перевод организации"
    assert (next(transaction_description)) == "Перевод со счета на счет"
    assert (next(transaction_description)) == "Перевод со счета на счет"
    assert (next(transaction_description)) == "Перевод с карты на карту"
    assert (next(transaction_description)) == "Перевод организации"
    assert (next(transaction_description)) == end_message


def test_transaction_descriptions_3():
    """Проверка случая пустого списка транзакций"""

    blank_list_message = "Список транзакций пуст"
    transaction_description = transaction_descriptions([])
    assert (next(transaction_description)) == blank_list_message


def test_transaction_descriptions_4():
    """Проверка на несоответствие структуры входного списка ожидаемой"""

    inappropriate_structure_message = "Несоответствующая структура данных"
    transaction_description = transaction_descriptions(
        [
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188",
            }
        ]
    )
    assert (next(transaction_description)) == inappropriate_structure_message


# Проверка вывода номеров карт в интервале [1;5]
generator_1 = card_number_generator(1, 5)


@pytest.mark.parametrize(
    "generated_number",
    [
        ("0000 0000 0000 0001"),
        ("0000 0000 0000 0002"),
        ("0000 0000 0000 0003"),
        ("0000 0000 0000 0004"),
        ("0000 0000 0000 0005"),
    ],
)
def test_card_number_generator_1(generated_number: str):
    assert next(generator_1) == generated_number


# Проверка случаев по порядку:
# 1. Ввод отрицательного значения;
# 2. Конечное значение больше начального;
# 3. Конечное значение больше 9999_9999_9999_9999
@pytest.mark.parametrize(
    "start, stop, message",
    [(-1, 5, "Некорректный диапазон"), (5, 1, "Некорректный диапазон"), (1, 10**16, "Некорректный диапазон")],
)
def test_card_number_generator_5(start, stop, message):
    generator = card_number_generator(start, stop)
    assert next(generator) == message
