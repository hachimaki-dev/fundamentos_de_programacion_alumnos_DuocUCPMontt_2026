#Crea es_email_valido(email) que retorne True solo si el texto contiene al menos un "@" y un "."

def es_email_valido(email):
    check=0
    for i in email:
        if i == '@':
            check += 1
        if check == 1:
            if i == '.':
                check +=1
    
    if check >= 2:
        return 'Valido'
    else: 
        return 'Invalido'

resultado= es_email_valido('asdsadsad@sasasa.com')

print(resultado)