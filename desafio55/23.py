intentos_fallidos = 0 
while True:
    intentos_fallidos = intentos_fallidos + 1
    if intentos_fallidos == 3:
        print("Bloqueo de tarjeta")
        break