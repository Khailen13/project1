def filter_by_state(list_of_dictionaries: list, req_state="EXECUTED") -> list:
    """Принимает список словарей и опционально значение для ключа state"""

    return [i for i in list_of_dictionaries if i["state"] == req_state]
