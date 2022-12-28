def format_phone(phone: str):
    pn = phone.strip()
    pn: str = pn.replace('(', '')
    pn: str = pn.replace(')', '')
    pn: str = pn.replace(' ', '')
    pn: str = pn.replace('+', '')
    pn: str = pn.replace('%20', '')
    new_phone = pn
    return new_phone

def format_date(date: str):
    day, month, year = date.split(".")
    new_date = f"{year}-{month}-{day}"
    return new_date


def format_string(data: str):
    new_string = data.replace(" ", '')
    return new_string