intentos_fallidos = 0
clave_correcta = "secreto"
clave_ingresada = (input("Ingrese 'Admin123' para ingresar: "))

if clave_ingresada == clave_correcta:
    print("Entraste")
else:
    intentos_fallidos += 1
    print("intentos fallidos:", intentos_fallidos)
