def rule_length(string: str, length: int) -> bool:
    if len(string) >= length:
        return True
    else:
        return False

def rule_has_upper(string: str, quantity: int) -> bool:
    counter = 0
    for character in string:
        if character == character.upper():
            counter += 1

    if counter >= quantity:
        return True
    else:
        return False

def rule_has_number(string: str, quantity: int) -> bool:
    counter = 0
    for character in string:
        if character.isdigit():
            counter += 1

    if counter >= quantity:
        return True
    else:
        return False

def rule_has_symbol(string: str, quantity: int) -> bool:
    symbols = "!@#$%^&*"
    counter = 0
    for character in string:
        if character in symbols:
            counter += 1

    if counter >= quantity:
        return True
    else:
        return False


def validate_password(password: str) -> tuple[bool, str]:
    