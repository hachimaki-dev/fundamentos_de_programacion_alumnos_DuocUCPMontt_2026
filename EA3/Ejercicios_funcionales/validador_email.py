def es_email_valido(email):
    at = False
    dot = False
    for i in email:
        if i == "@":
            at = True
        if i == ".":
            dot = True
    if at == True and dot == True:
        return True
    else:
        return False