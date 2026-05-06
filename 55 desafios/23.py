intentos_fallidos = 0
contraseña = 1234


while True:
    intento_user = int(input("ingrese la clave numerica"))
    if intento_user != contraseña:
        intentos_fallidos += 1
        print(intentos_fallidos)
        if intentos_fallidos == 3:
            print("Bloqueo de Tarjeta")
            break
    elif intento_user == contraseña:
        print("Aceptado")
        break