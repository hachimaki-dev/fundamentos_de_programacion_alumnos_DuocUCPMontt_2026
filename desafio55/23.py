intentos_fallidos = 0
password = "1234"

while True:
    password_ingresada = input("Contraseña: ")
    if password_ingresada == password:
        print("Acceso concedido")
        break
    else:
        intentos_fallidos = intentos_fallidos + 1
        print("Contraseña errónea")

    if intentos_fallidos == 3:
        print("Bloqueo de Tarjeta")
        break
    else:
        pass
