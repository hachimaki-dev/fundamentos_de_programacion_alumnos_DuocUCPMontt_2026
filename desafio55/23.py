intentos_fallidos = 0
clave_secreta = 4122
while True:
    clave_ingresada = int(input("Ingrese la clave :\n"))
    if clave_ingresada != clave_secreta:
        intentos_fallidos += 1
    if intentos_fallidos == 3:
        print("Bloqueo de tarjeta.")
        break