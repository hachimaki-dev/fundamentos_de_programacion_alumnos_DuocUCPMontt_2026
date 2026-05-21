#Crea generar_password(longitud=8) que retorne un string aleatorio de la longitud especificada.

#Primero realizamos las importaciones random para que sea aleatorio y el de strings para que sean caracteres
import random
import string

#Definimos la funcion
def generar_password(longitud = 8):
    #la variable caracteres permite que se consideren letras mayúsculas y minusculas (ascii_letters) y números/dígitos (string.digits)
    caracteres = string.ascii_letters + string.digits
    #generamos la password con un string vacío y usamos la función .join() para unir todos estos caracteres generados aleatoriamente dentro con ayuda del for
    password =  ''.join(random.choice(caracteres) for _ in range (longitud))
    return password

print(generar_password())