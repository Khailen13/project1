def filter_by_state(list_of_dictionaries: list, req_state: str = "EXECUTED") -> list:
    """Принимает список словарей и опционально значение для ключа state"""

    return [i for i in list_of_dictionaries if i["state"] == req_state]


def sort_by_date(list_of_dictionaries: list, reverse_order: bool = True) -> list:
    """принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)"""

    return sorted(
        list_of_dictionaries,
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
