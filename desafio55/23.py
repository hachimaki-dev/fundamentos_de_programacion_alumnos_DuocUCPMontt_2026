intentos_fallidos = 0
clave_correcta = "secreto"
while True:
    clave_ingresada = "1234"
    if clave_ingresada != clave_correcta:
        intentos_fallidos += 1
    if intentos_fallidos == 3:
        print("Bloqueo de tarjeta")
        break