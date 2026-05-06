intentos_fallidos = 0
claves_correctas = "1234"

while True:
    clave_ingresada = input("Introduce tu clave: ")

    if clave_ingresada == claves_correctas:
        print("Accesso concedido! Bienvenido!.")
        break

    else:
        intentos_fallidos += 1
        print(f"clave incorrecta. intentos fallidos:  {intentos_fallidos}" )

        if intentos_fallidos >= 3:
            print("bloqueo de tarjeta")
            break


