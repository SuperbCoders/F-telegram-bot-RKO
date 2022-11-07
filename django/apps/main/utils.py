def format_phone(phone: str):
    pn = phone.strip()
    pn: str = pn.replace('(', '')
    pn: str = pn.replace(')', '')
    pn: str = pn.replace(' ', '')
    pn: str = pn.replace('+', '')
    pn: str = pn.replace('%20', '')
    new_phone = pn
    return new_phone