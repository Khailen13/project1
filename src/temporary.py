from src.masks import get_mask_account, get_mask_card_number
card_number = 7000792289606361
# print(get_mask_card_number(7000792289606361))
print(str(card_number).isdigit())
print(len(str(card_number)))