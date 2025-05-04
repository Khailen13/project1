import pytest

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_1(initial_transactions):
    incorrect_input_message = "Неправильный ввод данных"
    # Проверка статуса 'EXECUTED' при отсутствии непосредственного ввод статуса
    assert filter_by_state(initial_transactions) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    # Проверка статуса 'EXECUTED' при вводе строчными буквами
    assert filter_by_state(initial_transactions, "executed") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    # Проверка статуса 'CANCELED'
    assert filter_by_state(initial_transactions, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    # Проверка статуса 'CANCELED' при вводе строчными буквами
    assert filter_by_state(initial_transactions, "canceled") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


# Проверка случаев пустового списка, некорректного ввода статуса, отсутствия ключа "state"
@pytest.mark.parametrize(
    "transactions, req_state",
    [
        ([], "EXECUTED"),
        (
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
            "abra",
        ),
        (
            [
                {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
        ),
    ],
)
def test_filter_by_state_2(transactions, req_state):
    incorrect_input_message = "Неправильный ввод данных"
    assert filter_by_state(transactions, req_state) == incorrect_input_message


def test_sort_by_date_1(initial_transactions: list, reverse_order: bool = True):
    # Проверка сортировки по убыванию
    assert sort_by_date(initial_transactions) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_2(initial_transactions: list, reverse_order: bool = True):
    # Проверка сортировки по возрастанию
    assert sort_by_date(initial_transactions, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]

def test_sort_by_date_3(same_day_transactions: list, reverse_order: bool = True):
    # Проверка сортировки по убыванию при одинаковых датах - сортировка по часам-минутам-секундам
    assert sort_by_date(same_day_transactions) == [
        {"id": 594226727, "state": "CANCELED", "date": "2019-07-03T21:27:25.241689"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2019-07-03T08:21:33.419441"},
        {"id": 939719570, "state": "EXECUTED", "date": "2019-07-03T02:08:58.425572"},
    ]