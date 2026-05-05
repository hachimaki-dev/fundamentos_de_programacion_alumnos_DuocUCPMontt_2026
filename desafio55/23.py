#ejercicio 23: Bloqueo de Seguridad (Cajero)

intentos_fallidos = 0
clave_secreta ="gatito"


while True:
    clave = input("Ingrese el nombre de clave secrete:")
    if clave != clave_secreta:
        intentos_fallidos += 1
    else:
        print("Clave correcta")
        break

    if intentos_fallidos == 3:
        print("Bloqueo de tarjeta")
        break
