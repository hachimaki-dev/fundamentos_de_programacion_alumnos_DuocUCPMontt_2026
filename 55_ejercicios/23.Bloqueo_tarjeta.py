intentos_fallidos = 0

while True:
    intentos_fallidos += 1
    print("Clave incorrecta")
    if intentos_fallidos == 3:
        print("Bloqueo de tarjeta")
        break