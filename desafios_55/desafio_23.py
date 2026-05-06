intentos_fallidos = 0
clave_correcta = 4031

while True:
    clave_ingresada = int(input("Ingrese su clave de 4 digitos: "))

    if clave_ingresada == clave_correcta:
        print("Clave correcta. Ingresando...")

    else:
        print("Clave incorrecta. Ingrese su clave nuevamente.")
        intentos_fallidos += 1

    if intentos_fallidos == 3:
        print("Bloqueo de Tarjeta.")
        break