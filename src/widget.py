from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Возвращает строку с замаскированным номером"""
    incorrect_input_message = 'Неправильный ввод данных'
    if type_and_number == '': # Пустая строка - некорректный ввод
        return incorrect_input_message
    else:
        splited_items = type_and_number.split()
        parts_count = len(splited_items)
        if (not (splited_items[0]).isalpha): # Строка начинается не с букв - некорректный ввод
            return incorrect_input_message
        else: # Количество цифровой части отлична от единицы - некорректный ввод
            digits_presence = 0
            for item in splited_items:
                if item.isdigit():
                    digits_presence += 1
            if digits_presence != 1:
                return incorrect_input_message
            else: # В остальных случаях
                masked_number = ""
                for item in splited_items:
                    if item.isalpha(): # включение буквенной части
                        masked_number += f"{item} "
                    elif item.isdigit(): # включение цифровой части
                        if splited_items[0] == "Счет":
                            masked_number += get_mask_account(item)
                        else:
                            masked_number += get_mask_card_number(item)
                if 'введен не правильно' in masked_number: # Некорректные номера по сообщению модуля masks
                    return incorrect_input_message
                else:
                    return masked_number


def get_date(initial_format_date: str) -> str:
    """Изменяет формат даты"""

    new_format_date = ""
    splited_items = initial_format_date.split("-")
    year = splited_items[0]
    month = splited_items[1]
    day = splited_items[2].split("T")[0]
    new_format_date = f"{day}.{month}.{year}"
    return new_format_date
