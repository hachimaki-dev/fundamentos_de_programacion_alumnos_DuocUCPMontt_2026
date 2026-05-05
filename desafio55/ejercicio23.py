contador_intentos_fallidos = 0
clave = "Malono12"
while True:
    clave_ingresada = input("Ingrese clave")
    if clave_ingresada != clave:
        contador_intentos_fallidos = contador_intentos_fallidos + 1
        print("Clave incorrecta")
        print("")
        if contador_intentos_fallidos == 3:
            print("Bloqueo de Tarjeta")
            break
    elif clave_ingresada == clave:
        print("Contraseña correcta")
    

