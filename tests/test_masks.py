from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> str:
    """Набор тестов для get_mask_card_number"""

    incorrect_input_message = "Номер карты введен не правильно"
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"  # Корректный номер в виде цифр
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"  # Корректный номер в виде строки
    assert get_mask_card_number("abcd792289606361") == incorrect_input_message  # Некорректный ввод: буквы+цифры
    assert get_mask_card_number("abcd") == incorrect_input_message  # Некорректный ввод: только буквы, 4 шт.
    assert get_mask_card_number("") == incorrect_input_message  # Некорректный ввод: пустая строка


def test_get_mask_account() -> str:
    incorrect_input_message = "Номер счета введен не правильно"
    assert get_mask_account(73654108430135874305) == "**4305"  # Корректный номер в виде цифр
    assert get_mask_account("abcd4108430135874305") == incorrect_input_message  # Некорректный ввод: буквы+цифры
    assert get_mask_account("792289606361") == incorrect_input_message  # Некорректный ввод: недостаточное количество
    assert get_mask_account("") == incorrect_input_message  # Некорректный ввод: пустая строка
