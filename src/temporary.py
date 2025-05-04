from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(type_and_number: str) -> str:
    """Возвращает строку с замаскированным номером"""
    incorrect_input_message = 'Неправильный ввод данных'
    if type_and_number == '': #Пустая строка - некорректный ввод
        return incorrect_input_message
    else:
        splited_items = type_and_number.split()
        parts_count = len(splited_items)
        if (not (splited_items[0]).isalpha): #Строка начинается не с букв - некорректный ввод
            return incorrect_input_message
        else: #Количество цифровой части отлична от единицы - некорректный ввод
            digits_presence = 0
            for item in splited_items:
                if item.isdigit():
                    digits_presence += 1
            if digits_presence != 1:
                return incorrect_input_message
            else: # в остальных случаях
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
input_data = "absb 1213"

print (mask_account_card(input_data))

# @pytest.mark.parametrize(
#     "input_data, masked_data",
#     [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
#      ("Счет 64686473678894779589", "Счет **9589"),
#      ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
#      ('Счет 35383033474447895560', 'Счет **5560'),
#      ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
#      ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
#      ('Visa Gold 5999414228426353', 'Visa Gold 5999 41** **** 6353'),
#      ('Счет 73654108430135874305', 'Счет **4305'),
#      ('73654108430135874305', 'Неправильный ввод данных'),
#      ('Visa Gold', 'Неправильный ввод данных'),
#      ('', 'Неправильный ввод данных')],
# )