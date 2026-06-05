def generar_password(longitud=8):
    import secrets
    import string

    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation
    caracter = letras+numeros+simbolos
    contraseña = ''
    for i in range(longitud):
        contraseña += ''.join(secrets.choice(caracter))
    
    return(contraseña)
resultado = generar_password()
print(resultado)