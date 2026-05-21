#Crea es_email_valido(email) que retorne True solo si el texto contiene al menos un "@" y un "."
 
email = input("Introduce tu email: ")

def es_email_valido(email):
    #Usa in para que el programa verifique que se encuentren dentro del email
    for caracter in email:
        if "@" in email and "." in email:
            return True
        else:
            return False
        
validacion = es_email_valido(email)
print(validacion)