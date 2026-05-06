intentos_fallidos = 0
clave_ingresada = "admin123"

if clave_ingresada == "secreta":
    print("Acceso permitido")

else:
    print("Acceso denegado")
    intentos_fallidos += 1
    print(f"Clave incorrecta, llevas {intentos_fallidos} intentos fallidos")