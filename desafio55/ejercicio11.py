clave_secreta = "Admin123"
contador_intentos_fallidos = 0
clave_ingresada = input("Ingrese su clave unica")
while True:
    if contador_intentos_fallidos == 3:
        print("Cuenta bloqueada")
        break
    if clave_ingresada != clave_secreta:
        contador_intentos_fallidos = contador_intentos_fallidos + 1
        clave_ingresada = input(f"Clave incorrecta. Intentos fallidos {contador_intentos_fallidos}")
    else:
        print("Clave valida. Ha ingresado al sistema")
        break
