from src.masks import get_mask_account, get_mask_card_number
import pytest


def test_get_mask_card_number():
    incorrect_input_message = "Номер карты введен не правильно"
    assert get_mask_card_number(7000792289606361) == "7000 79** **** 6361"
    assert get_mask_card_number('7000792289606361') == "7000 79** **** 6361"
    assert get_mask_card_number("abcd792289606361") == incorrect_input_message
    assert get_mask_card_number('abcd') == incorrect_input_message
    assert get_mask_card_number("") == incorrect_input_message



def test_get_mask_account():
    incorrect_input_message = "Номер счета введен не правильно"
    assert get_mask_account(73654108430135874305) == "**4305"
    assert get_mask_account("abcd4108430135874305") == incorrect_input_message
    assert get_mask_account("792289606361") == incorrect_input_message
    assert get_mask_account("") == incorrect_input_message
