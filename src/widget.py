from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Возвращает строку с замаскированным номером"""

    incorrect_input_message = "Неправильный ввод данных"
    if type_and_number == "":  # Пустая строка - некорректный ввод
        return incorrect_input_message
    else:
        splited_items = type_and_number.split()
        if not splited_items[0].isalpha():  # Строка начинается не с букв - некорректный ввод
            return incorrect_input_message
        else:  # Подсчет количества непрерывных цифровых частей
            digits_presence = 0
            for item in splited_items:
                if item.isdigit():
                    digits_presence += 1
            if digits_presence != 1:  # Если количество цифровой части отлична от единицы - некорректный ввод
                return incorrect_input_message
            else:  # В остальных случаях
                masked_number = ""
                for item in splited_items:
                    if item.isalpha():  # Включение в маску буквенной части
                        masked_number += f"{item} "
                    elif item.isdigit():  # Включение  в маску цифровой части
                        if splited_items[0] == "Счет":
                            masked_number += get_mask_account(item)
                        else:
                            masked_number += get_mask_card_number(item)
                if "введен не правильно" in masked_number:  # Некорректные номера по сообщению модуля masks
                    return incorrect_input_message
                else:
                    return masked_number


def get_date(initial_format_date: str) -> str:
    """Принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")"""

    incorrect_input_message = "Неправильный ввод данных"
    if len(initial_format_date) < 10:  # Если менее 10 символов в строке - некорректный ввод
        return incorrect_input_message
    else:
        year = initial_format_date[0:4]
        month = initial_format_date[5:7]
        day = initial_format_date[8:10]
        if (  # Проверка соответствия формата ожидаемому
            year.isdigit()
            and initial_format_date[4] == "-"
            and month.isdigit()
            and 1 <= int(month) <= 12
            and initial_format_date[7] == "-"
            and day.isdigit()
            and 1 <= int(day) <= 31
        ):
            return f"{day}.{month}.{year}"
        else:
            return incorrect_input_message
