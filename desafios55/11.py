intentos_fallidos = 0
clave_correcta = "secreto"
clave_ingresada = "admin123"

if clave_ingresada == clave_correcta:
    print("Acceso permitido, Bienvenido de nuevo.")
else:
    intentos_fallidos = intentos_fallidos + 1
    print(f"Accesso Denegado, Intentos fallidos: {intentos_fallidos}")