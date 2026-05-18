intentos_fallidos = 0

while True:

    password = input("Ingrese su contraseña: ")

    if password == "contraseña123":
        print("¡Contraseña correcta! Acceso concedido.")
        break
    else:
        intentos_fallidos += 1
        print("¡Contraseña incorrecta! Inténtalo de nuevo.")

        if intentos_fallidos >= 3:
            print("¡Tarjeta Bloqueada!")
            break