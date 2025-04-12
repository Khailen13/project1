from masks import get_mask_card_number
from masks import get_mask_account

def mask_account_card(type_and_number:str) -> str:
    """Возвращает строку с замаскированным номером"""

    masked_number = ''
    splited_items = type_and_number.split()
    for item in splited_items:
        if item.isalpha():
            masked_number += f'{item} '
        elif item.isdigit():
            if splited_items[0] == "Счет":
               masked_number += get_mask_account(item)
            else:
               masked_number += get_mask_card_number(item)
    return masked_number


def get_date(initial_format_date:str) -> str:
    """Изменяет формат даты"""

    new_format_date = ''
    splited_items = initial_format_date.split("-")
    year = splited_items[0]
    month = splited_items[1]
    day = splited_items[2].split('T')[0]
    new_format_date = f"{day}.{month}.{year}"
    return new_format_date
