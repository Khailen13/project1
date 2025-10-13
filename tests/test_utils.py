import pytest
import json
import unittest
from unittest.mock import Mock, patch, mock_open

from src.utils import json_reader

def test_json_reader_None_nolist():
    """Проверка на пустое содержание - не-список"""
    mock = mock_open(read_data="null")
    with patch("builtins.open", mock):
        assert (json_reader("")) == []

def test_json_reader_success():
    """Проверка на успешность работы при корректном содержании"""
    coorect_contetnt = '[{"id": 441945886}]'
    mock = mock_open(read_data=coorect_contetnt)
    with patch("builtins.open", mock):
        assert (json_reader("")) == json.loads(coorect_contetnt)

def test_json_reader_FileNotFoundError():
    """Проверка при отсутствии файла"""
    assert json_reader("non-existent_file") == []

