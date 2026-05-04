intentos_fallidos = 0
clave_correcta = "secreto"
clave_ingresada = "Admin123"
if clave_ingresada == clave_correcta:
    print("entraste")
else:
    intentos_fallidos = intentos_fallidos + 1
    print(f"Intentos fallidos: {intentos_fallidos}")