def get_mask_card_number(card_number: str | int) -> str:
    """Маскирует номер банковской карты"""
    return f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"


def get_mask_account(account_number: str | int) -> str:
    """Маскирует номер счета"""
    return f"**{str(account_number)[-4:]}"
