def hide(card_number):
    s = str(card_number)
    if len(s) != 16 or not s.isdigit():
        raise ValueError("Card number must be a 16-digit number")
    return s[:6] + "*" * 6 + s[-4:]