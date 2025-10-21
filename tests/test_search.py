from src.search import process_bank_operations, process_bank_search


def test_process_bank_search_success(transactions):
    """Проверка в случае наличия соответствующих транзакций"""

    expected_result = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
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
    assert process_bank_search(transactions, "Перевод организ") == expected_result
    assert process_bank_search(transactions, "перевод Организ") == expected_result


def test_process_bank_search_not_found(transactions):
    """Проверка при отсутствии соответствующих транзакций"""

    expected_result = []
    assert process_bank_search(transactions, "Отсутствующая операция") == expected_result


def test_process_bank_search_exceptions(initial_transactions):
    """Проверка при пустом списке транзакций"""

    expected_result = []
    assert process_bank_search(initial_transactions, "Перевод") == expected_result


def test_process_bank_operations_success(transactions):
    """Проверка в случае наличия соответствующих транзакций"""

    descriptions_list = ["Перевод организации", "Перевод со счета на счет", "Перевод с карты на карту"]
    expected_result = {"Перевод организации": 2, "Перевод со счета на счет": 2, "Перевод с карты на карту": 1}
    assert process_bank_operations(transactions, descriptions_list) == expected_result


def test_process_bank_operations_not_found(transactions):
    """Проверка при отсутствии соответствующих транзакций"""

    descriptions_list = ["Открытие вклада"]
    expected_result = {}
    assert process_bank_operations(transactions, descriptions_list) == expected_result


def test_process_bank_operations_exception(transactions):
    """Проверка при пустом списке транзакций и типе запрашиваемого содержания int"""

    descriptions_list = [5]
    expected_result = {}
    assert process_bank_operations([], descriptions_list) == expected_result
