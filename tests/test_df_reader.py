import os
from unittest.mock import mock_open, patch

import pandas as pd

from src.df_readers import csv_reader, excel_reader


def test_csv_reader_FileNotFoundError():
    """Проверка функции csv_reader при отсутствии файла"""
    assert csv_reader("non-existent_file") == []


def test_csv_reader_success():
    """Проверка преобразования csv-данных функцией csv_reader в список словарей"""
    mock_data = "Column_1;Column_2\nValue_1;Value_2"
    mock = mock_open(read_data=mock_data)
    with patch("builtins.open", mock):
        excepted_result = [{"Column_1": "Value_1", "Column_2": "Value_2"}]
        assert csv_reader("") == excepted_result


def test_excel_reader_FileNotFoundError():
    """Проверка функции excel_reader при отсутствии файла"""
    assert excel_reader("non-existent_file") == []


def test_excel_reader_success():
    """Проверка преобразования данных функцией excel_reader в список словарей"""

    mock_data = {
        "id": [650703],
        "state": ["EXECUTED"],
        "date": ["2023-09-05T11:30:32Z"],
        "amount": [16210],
        "currency_name": ["Sol"],
        "currency_code": ["PEN"],
        "from": ["Счет 58803664561298323391"],
        "to": ["Счет 39745660563456619397"],
        "description": ["Перевод организации"],
    }
    mock_df = pd.DataFrame.from_dict(mock_data)
    with patch("pandas.read_excel") as mock_excel_reader:
        mock_excel_reader.return_value = mock_df
        expected_result = [
            {
                "id": 650703,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]

        result = excel_reader(f"{os.path.realpath(__file__)}")
        assert result == expected_result
