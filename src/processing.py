def filter_by_state(transactions: list, req_state: str = "EXECUTED") -> list | str:
    """Принимает список словарей и опционально значение для ключа state"""

    incorrect_input_message = "Неправильный ввод данных"  # Сообщение при неправильном вводе
    correct_input = False
    if len(transactions) > 0:  # Непустой список
        relevant_transcations = []  # Возвращаемый список
        for transaction in transactions:
            if ("state" in transaction) and (
                req_state.upper() == "EXECUTED" or req_state.upper() == "CANCELED"
            ):  # Наличие ключа "state" и правильность заправшиваемого статуса
                correct_input = True
                if transaction["state"].upper() == req_state.upper():  # Соответствие запрашиваемому статусу
                    relevant_transcations.append(transaction)
        if correct_input:  # При правильном вводе
            return relevant_transcations
        else:  # При отсутствии ключа "state" или ошибке в запрашиваемом статусе
            return incorrect_input_message
    else:  # При пустом входном списке
        return incorrect_input_message


def sort_by_date(transactions: list, reverse_order: bool = True) -> list:
    """Принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)"""
    # {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    # Проверка соотвествия входного формата
    incorrect_input_message = "Некорректные данные"
    correct_transaction_presence = False  # признак наличия в списке транзакции с корректной датой
    correct_transactions = []  # список транзакций с корректыными датами
    if len(transactions) == 0:  # пустой список
        return incorrect_input_message
    else:
        for transaction in transactions:
            if "date" in transaction: # наличие ключа "date"
                if len(transaction["date"]) >= 18:  # не менее 18 символов - признак корректности данных
                    year = transaction["date"][0:4]
                    month = transaction["date"][5:7]
                    day = transaction["date"][8:10]
                    hours = transaction["date"][11:13]
                    minutes = transaction["date"][14:16]
                    seconds = transaction["date"][17:]
                    if (
                        year.isdigit()  # проверка частей даты ожидаемому формату
                        and transaction["date"][4] == "-"
                        and month.isdigit()
                        and 1 <= int(month) <= 12
                        and transaction["date"][7] == "-"
                        and day.isdigit()
                        and 1 <= int(day) <= 31
                        and transaction["date"][10] == "T"
                        and 0 <= int(hours) <= 23
                        and transaction["date"][13] == ":"
                        and 0 <= int(minutes) <= 59
                        and transaction["date"][16] == ":"
                        and 0 <= float(seconds) <= 60
                    ):
                        correct_transaction_presence = True
                        correct_transactions.append(transaction)
    if correct_transaction_presence:
        return sorted(
            correct_transactions,
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
