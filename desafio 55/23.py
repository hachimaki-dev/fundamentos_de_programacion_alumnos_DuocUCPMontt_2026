intentos_fallidos = 0

while True:
    # simulamos ingreso incorrecto
    clave_ingresada = "1234"

    if clave_ingresada != "secreto":
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Bloqueo de Tarjeta")
        break