def validar_isbn_v1(isbn):
    if len(isbn) != 13:
        return False
    for caracter in isbn:
        if caracter not in "0123456789":
            return False
        else:
            return True
    else:
        return True
def validar_isbn_v2(isbn):
    if len(isbn) == 13 and isbn.isdigit():
        return True
    else:
        return False