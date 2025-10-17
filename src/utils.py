import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/utils.log", "w")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def json_reader(file_path: str) -> list:
    """Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""

    try:
        with open(file_path, encoding="utf-8") as file:
            transactions = json.load(file)
            logger.info("The file successfully opened.")
            if type(transactions) is not list or transactions is None or transactions == []:
                logger.error("The file doesn't contain a list or is empty")
                transactions = []
    except FileNotFoundError as err:
        logger.error(f"File not found: {err}.")
        transactions = []
    if transactions != []:
        logger.info("The content of the file is correct.")
    return transactions
