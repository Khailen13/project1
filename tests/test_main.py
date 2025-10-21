from unittest.mock import patch

from src.main import requester


def test_requester():
    """Проверка на принятие лишь того ответа, который присутствует в списке возможных"""

    user_input = ["1", "2", "да"]
    expected_result = "ДА"
    question = "Да/Нет?"
    possible_answers = ["ДА", "НЕТ"]
    positions_name = "Вариант"
    with patch("builtins.input", side_effect=user_input):
        answer = requester(question, possible_answers, positions_name)
    assert answer == expected_result
