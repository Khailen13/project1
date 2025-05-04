import pytest

from src.processing import filter_by_state, sort_by_date

def test_filter_by_state_1(initial_transactions):
    incorrect_input_message = "Неправильный ввод данных"
    # Проверка статуса 'EXECUTED' при отсутствии непосредственного ввод статуса
    assert filter_by_state(initial_transactions) == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    # Проверка статуса 'EXECUTED' при вводе строчными буквами
    assert filter_by_state(initial_transactions, 'executed') == [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
    # Проверка статуса 'CANCELED'
    assert filter_by_state(initial_transactions,"CANCELED") == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    # Проверка статуса 'CANCELED' при вводе строчными буквами
    assert filter_by_state(initial_transactions, "canceled") == [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

#Проверка случаев пустового списка, некорректного ввода статуса, отсутствия ключа "state"
@pytest.mark.parametrize("transactions, req_state",
    [([], 'EXECUTED'), ([{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}], "abra"), ([{'id': 594226727, 'date': '2018-09-12T21:27:25.241689'},{'id': 615064591, 'date': '2018-10-14T08:21:33.419441'}], 'EXECUTED')])
def test_filter_by_state_2(transactions, req_state):
        incorrect_input_message = "Неправильный ввод данных"
        assert filter_by_state(transactions, req_state) == incorrect_input_message

