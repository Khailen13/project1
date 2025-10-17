import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/masks.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str | int) -> str:
    """Маскирует номер банковской карты"""

    if str(card_number).isdigit() and len(str(card_number)) == 16:
        masked_card_number = f"{str(card_number)[0:4]} {str(card_number)[4:6]}** **** {str(card_number)[-4:]}"
        logger.info("The card number successfully masked.")
        return masked_card_number
    else:
        logger.error("Invalid card number.")
        return "Номер карты введен не правильно"


def get_mask_account(account_number: str | int) -> str:
    """Маскирует номер счета"""

    if str(account_number).isdigit() and len(str(account_number)) == 20:
        masked_account_number = f"**{str(account_number)[-4:]}"
        logger.info("The account number successfully masked.")
        return masked_account_number
    else:
        logger.error("Invalid account number.")
        return "Номер счета введен не правильно"
