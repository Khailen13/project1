def filter_by_currency(transactions: list, currency: str):
    i = 0
    currency_lack_message = "Транзакции в запрашиваемой валюте отсутствуют"
    blank_list_message = "Список транзакций пуст"
    inappropriate_structure_message = "Несоответствующая структура данных"
    is_correct_structure = False
    while True:
        if len(transactions) == 0:
            yield blank_list_message
        elif i >= len(transactions) and not is_correct_structure:
            yield inappropriate_structure_message
        elif i >= len(transactions):
            yield currency_lack_message
        elif "operationAmount" in transactions[i]:
            if "currency" in transactions[i]["operationAmount"]:
                if "code" in transactions[i]["operationAmount"]["currency"]:
                    is_correct_structure = True
                    if transactions[i]["operationAmount"]["currency"]["code"] == currency:
                        yield transactions[i]
        i += 1
