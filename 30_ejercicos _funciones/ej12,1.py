def es_email_valido(email):
    if "." in email and "@" in email:
        return True
    else:
        return False
direccion_email = es_email_valido(input("ingrese su direccion de email: "))
print(direccion_email)