def format_phone(phone: str):
    pn = phone.strip()
    pn: str = pn.replace('(', '')
    pn: str = pn.replace(')', '')
    pn: str = pn.replace(' ', '')
    pn: str = pn.replace('+', '')
    new_phone = pn
    return new_phone