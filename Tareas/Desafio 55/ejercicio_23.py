# Bloqueo de Seguridad (Cajero)
clave_correcta = 1122
intentos_fallidos = 0
123
while True:

    clave = input("Ingrese su clave: ")

    if clave == clave_correcta:
        print("Clave correcta")
        print("Acceso permitido")
        intentos_fallidos = 0

    else:
        intentos_fallidos += 1

        print("Clave incorrecta")
        print(f"Intentos fallidos: {intentos_fallidos}")

        if intentos_fallidos == 3:
            print("Bloqueo de Tarjeta")
            break