def es_email_valido(email):
    check=0
    for i in email:
        if i == '@':
            check += 1
        if check == 1:
            if i in '.':
                check += 1
    if check >= 2:
        return 'Valido'
    else:
        return 'Invalido'
resultado = es_email_valido('dskaldsaksldan@jskandjk.com')
print(resultado)