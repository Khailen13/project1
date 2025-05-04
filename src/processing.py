def filter_by_state(transactions: list, req_state: str = "EXECUTED") -> list:
    """Принимает список словарей и опционально значение для ключа state"""

    incorrect_input_message = "Неправильный ввод данных"
    correct_input = False
    if len(transactions) > 0: # Непустой список
        relevant_transcations = []
        for transaction in transactions:
            if (("state" in transaction) and (req_state.upper() == "EXECUTED" or req_state.upper() == "CANCELED")): # условия наличия ключа "state", правильности заправшиваемого статуса
                correct_input = True
                if transaction["state"].upper() == req_state.upper(): # При соответствии запрашиваемому статусу
                    relevant_transcations.append(transaction)
        if correct_input:
            return relevant_transcations
        else:
            return incorrect_input_message
    else:
        return incorrect_input_message


def sort_by_date(transactions: list, reverse_order: bool = True) -> list:
    """принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)"""

    return sorted(
        transactions,
        key=lambda x: (
            int(x["date"].split("-")[0]),
            int(x["date"].split("-")[1]),
            int(x["date"].split("-")[2].split("T")[0]),
            int(x["date"].split("T")[1].split(":")[0]),
            int(x["date"].split(":")[1]),
            float(x["date"].split(":")[2]),
        ),
        reverse=reverse_order,
    )
