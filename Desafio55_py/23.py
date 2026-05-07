intentos_fallidos = 0

while True:
    clave = input("INGRESE SU CLAVE : ").lower()

    intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("BLOQUEO DE TARJETA")
        break