intentos_fallidos = 0

while True:
    intentos_fallidos += 1
    
    if intentos_fallidos >= 3:
        print("Bloqueo de Tarjeta")
        break
    