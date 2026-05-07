intentos_fallidos = 0

clave = 2243

while True:
    ingreso = int(input("Ingrese su clave: "))
    if ingreso != clave:
        intentos_fallidos = intentos_fallidos + 1
        if intentos_fallidos == 3:
            print("Bloqueo de tarjeta.")
            break
    else:
        print("Clave correcta.")
        break