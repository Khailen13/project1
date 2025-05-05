def get_mask_card_number(card_number: str | int) -> str:
    """Маскирует номер банковской карты"""

    if str(card_number).isdigit() and len(str(card_number)) == 16:
        return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"
    else:
        return "Номер карты введен не правильно"


def get_mask_account(account_number: str | int) -> str:
    """Маскирует номер счета"""

    if str(account_number).isdigit() and len(str(account_number)) == 20:
        return f"**{str(account_number)[-4:]}"
    else:
        return "Номер счета введен не правильно"
