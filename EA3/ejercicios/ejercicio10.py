#Crea generar_password(longitud=8) que retorne un string aleatorio de la longitud especificada.
def generar_password(longitud=8):
    import secrets
    import string
    #shotout geekflare por la idea
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation
    caracteres = letras+numeros+simbolos

    contrasena = ''
    for i in range(longitud):  
        contrasena += ''.join(secrets.choice(caracteres))
    
    return (contrasena)

resultado = generar_password()

print (resultado)