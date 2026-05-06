intentos_fallidos = 0
while True:
    clave = input("ingrese su clave: ")
    if clave != "carlitos123":
        print("clave incorrecta, intentalo de nuevo")
        intentos_fallidos = intentos_fallidos + 1
        if intentos_fallidos == 3:
            print("bloqueo de tarjeta")
            break
    if clave == "carlitos123":
        print("hola carlitos")