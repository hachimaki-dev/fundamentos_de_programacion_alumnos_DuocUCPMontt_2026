#Crea generar_password(longitud=8) que retorne un string aleatorio de la longitud especificada.

import random

def generar_password(longitud=8):
    
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    password = ""

    for i in range(longitud):
        password += random.choice(caracteres)

    return password

print(generar_password())
print(generar_password(12))


