from unittest.mock import patch

from src.external_api import current_converter


def test_current_converter_RUB(transactions_for_ext_api):
    """Проверка вывода при транзакции в RUB"""

    transaction = transactions_for_ext_api[2]
    assert (current_converter(transaction)) == "43318.34"


def test_current_converter_USD(transactions_for_ext_api):
    """Проверка вывода при транзакции в USD"""

    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {
            "success": True,
            "query": {"from": "USD", "to": "RUB", "amount": 0},
            "info": {"timestamp": 0, "rate": 0},
            "date": "",
            "result": 123,
        }
        assert current_converter(transactions_for_ext_api[1]) == 123
        mock_get.assert_called_once()


def test_current_converter_EUR(transactions_for_ext_api):
    """Проверка вывода при транзакции в EUR"""

    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = {
            "success": True,
            "query": {"from": "EUR", "to": "RUB", "amount": 0},
            "info": {"timestamp": 0, "rate": 0},
            "date": "",
            "result": 123,
        }
        assert current_converter(transactions_for_ext_api[0]) == 123
        mock_get.assert_called_once()
