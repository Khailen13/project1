transactions_1 = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "escription": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "escription": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions: list, currency: str):
    """Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной"""

    i = 0
    currency_lack_message = "Транзакции в запрашиваемой валюте отсутствуют"
    blank_list_message = "Список транзакций пуст"
    inappropriate_structure_message = "Несоответствующая структура данных"
    is_correct_structure = False
    while True:
        if len(transactions) == 0:
            yield blank_list_message
        elif i >= len(transactions) and not is_correct_structure:
            yield inappropriate_structure_message
        elif i >= len(transactions):
            yield currency_lack_message
        elif "operationAmount" in transactions[i]:
            if "currency" in transactions[i]["operationAmount"]:
                if "code" in transactions[i]["operationAmount"]["currency"]:
                    is_correct_structure = True
                    if transactions[i]["operationAmount"]["currency"]["code"] == currency:
                        yield transactions[i]
        i += 1


def transaction_descriptions(transactions: list):
    """Возвращает описание каждой транзакции по очереди"""

    i = 0
    blank_list_message = "Список транзакций пуст"
    inappropriate_structure_message = "Несоответствующая структура данных"
    end_message = "Конец списка транзакций"
    is_correct_structure = False
    while True:
        if len(transactions) == 0:
            yield blank_list_message
        elif i >= len(transactions) and not is_correct_structure:
            yield inappropriate_structure_message
        elif i >= len(transactions):
            yield end_message
        elif "description" in transactions[i]:
            is_correct_structure = True
            yield transactions[i]["description"]
        i += 1


descriptions = transaction_descriptions(transactions_1)
for _ in range(5):
    print(next(descriptions))
